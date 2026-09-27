"""Validate a trip folder's trip-data.json and its referenced files.

Usage:  python tools/validate_trip.py patagonia [--stale "text1" "text2" ...]

Checks (see patagonia/docs/update-plan.md §2 A):
  A1 schema and enums     A2 dates             A3 totals
  A4 profile vs stats     A5 km values in range A6 referenced/orphan files
  A7 stale text           A8 prose vs numbers (warn)  A9 privacy scan
Exit code 1 if any FAIL.
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

DIFFICULTY = {"Easy", "Moderate", "Strenuous"}
DAY_TYPES = {"hike", "city", "travel"}
PUBLISHED_EXT = {".html", ".json", ".gpx", ".md", ".js", ".css", ".txt"}

# Shapes of booking data that must never be published. Exact names and codes
# go in <trip>/private-terms.txt (git-ignored, one term per line) so this
# published script doesn't itself leak them.
PRIVACY_PATTERNS = [
    r"\bWEFI\d{6}\b",                              # Say Hueque booking refs
    r"(?<![\d.])734[09]\d{10}(?![\d.])",           # Expedia / Hotels.com itinerary numbers
    r"\bseat_", r"\bseats?\s*:?\s*\d{1,2}[A-K]\b",
    r"USD\s*(286|584)",
]

results = {"FAIL": [], "WARN": [], "PASS": []}


def report(level, check, msg):
    results[level].append(f"[{check}] {msg}")


def load_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def is_hike(day):
    # Same rule as the app's isHikeDay: missing, null or "" all count as a hike
    return not day.get("day_type") or day["day_type"] == "hike"


def check_schema(data):
    for key in ("trip", "days", "weather", "gear_checklist", "preparation", "general_info"):
        if key not in data:
            report("FAIL", "A1", f"missing top-level key '{key}'")
    trip = data.get("trip", {})
    if not trip.get("location_keywords"):
        report("FAIL", "A1", "trip.location_keywords is empty")
    w = data.get("weather", {})
    p = w.get("precipitation_probability")
    if p is not None and not (0 <= p <= 1):
        report("FAIL", "A1", f"weather.precipitation_probability {p} not in 0..1")
    for g in data.get("gear_checklist", []):
        if not isinstance(g.get("essential"), bool):
            report("FAIL", "A1", f"gear '{g.get('item')}' essential is not a boolean")
    for d in data.get("days", []):
        n = d.get("day")
        if d.get("day_type") is not None and d["day_type"] not in DAY_TYPES:
            report("FAIL", "A1", f"day {n}: day_type '{d['day_type']}' not in {sorted(DAY_TYPES)}")
        if d.get("difficulty") not in DIFFICULTY:
            report("FAIL", "A1", f"day {n}: difficulty '{d.get('difficulty')}'")
        if not d.get("location_keywords"):
            report("FAIL", "A1", f"day {n}: location_keywords empty")
        acc = d.get("accommodation")
        if acc is not None and "options" in acc:
            for o in acc["options"]:
                if not o.get("name"):
                    report("FAIL", "A1", f"day {n}: accommodation option without name")
    report("PASS", "A1", "schema checked")


def check_dates(data):
    trip = data["trip"]
    start = dt.date.fromisoformat(trip["dates"]["start"])
    end = dt.date.fromisoformat(trip["dates"]["end"])
    days = data["days"]
    if start > end:
        report("FAIL", "A2", "trip start after end")
    if len(days) != (end - start).days + 1:
        report("WARN", "A2", f"{len(days)} days but trip dates span {(end - start).days + 1}")
    first = dt.date.fromisoformat(days[0]["date"])
    for i, d in enumerate(days):
        if d.get("day") != i + 1:
            report("FAIL", "A2", f"day index {i} numbered {d.get('day')}")
        date = dt.date.fromisoformat(d["date"])
        if date != first + dt.timedelta(days=i):
            report("FAIL", "A2", f"day {d.get('day')} date {date} not consecutive")
        if not start <= date <= end:
            report("FAIL", "A2", f"day {d.get('day')} date {date} outside trip dates")
    wte = data.get("preparation", {}).get("what_to_expect", [])
    if len(wte) != len(days):
        report("FAIL", "A2", f"what_to_expect has {len(wte)} entries for {len(days)} days")
    report("PASS", "A2", f"{len(days)} days, {start} -> {end}")


def check_totals(data):
    hikes = [d for d in data["days"] if is_hike(d)]
    km = round(sum(d.get("distance_km", 0) for d in hikes), 1)
    up = sum(d.get("ascent_m", 0) for d in hikes)
    t = data["trip"]
    if abs(t.get("total_distance_km", 0) - km) > 0.15:
        report("FAIL", "A3", f"total_distance_km {t.get('total_distance_km')} != sum {km}")
    if t.get("total_ascent_m") != up:
        report("FAIL", "A3", f"total_ascent_m {t.get('total_ascent_m')} != sum {up}")
    for d in data["days"]:
        if not is_hike(d) and (d.get("distance_km") or d.get("ascent_m")):
            report("FAIL", "A3", f"day {d['day']} is {d['day_type']} but has distance/ascent")
    report("PASS", "A3", f"hike totals {km} km / {up} m")


def profile_stats(points):
    gain = loss = 0.0
    for a, b in zip(points, points[1:]):
        diff = b["elevation_m"] - a["elevation_m"]
        if diff > 0:
            gain += diff
        else:
            loss -= diff
    return points[-1]["km"], gain, loss


def check_profiles(data, root):
    for d in data["days"]:
        n = d["day"]
        prof = d.get("elevation_profile")
        if not is_hike(d):
            if prof:
                report("FAIL", "A4", f"day {n} ({d['day_type']}) should not have an elevation profile")
            continue
        if not prof:
            report("FAIL", "A4", f"hike day {n} has no elevation profile")
            continue
        p = root / prof
        if not p.exists():
            continue  # reported by A6
        pts = load_json(p).get("points", [])
        if len(pts) < 2:
            report("FAIL", "A4", f"day {n}: profile has {len(pts)} points")
            continue
        end_km, gain, _ = profile_stats(pts)
        dist = d.get("distance_km", 0)
        if dist and abs(end_km - dist) / dist > 0.05:
            report("FAIL", "A4", f"day {n}: profile ends at {end_km} km, day says {dist} km")
        asc = d.get("ascent_m", 0)
        # A 0.5 km profile smooths out short climbs, so it always shows less gain than
        # the full-resolution track. Only a profile showing MORE gain means a mismatch.
        if asc and gain > asc * 1.10:
            report("WARN", "A4", f"day {n}: profile gain ~{gain:.0f} m exceeds day's {asc} m")
    report("PASS", "A4", "profiles checked")


def check_km_ranges(data):
    for d in data["days"]:
        if not is_hike(d):
            continue
        dist = d.get("distance_km", 0)
        for field in ("waypoints", "toilet_facilities", "food_stops"):
            for item in d.get(field, []) or []:
                km = item.get("km")
                if isinstance(km, (int, float)) and km > dist + 0.05:
                    # a finish-point a few hundred metres past the stated distance is rounding
                    report("WARN" if km <= dist * 1.05 else "FAIL", "A5", f"day {d['day']} {field} '{item.get('name')}' at km {km} > {dist}")
    report("PASS", "A5", "km ranges checked")


def check_files(data, root):
    referenced = set()
    for d in data["days"]:
        refs = [d.get("elevation_profile"), d.get("map"), (d.get("links") or {}).get("gpx_download")]
        refs += d.get("photos", []) or []
        for r in filter(None, refs):
            if r.startswith("http"):
                continue
            referenced.add(Path(r).as_posix())
            # photos and maps are optional: the app falls back / hides them
            level = "WARN" if r.startswith(("photos/", "maps/")) else "FAIL"
            if not (root / r).exists():
                report(level, "A6", f"day {d['day']}: missing file {r}")
    for sub in ("gpx", "elevation"):
        for f in (root / sub).glob("*"):
            rel = f.relative_to(root).as_posix()
            if f.is_file() and rel not in referenced:
                report("WARN", "A6", f"orphan file {rel}")
    report("PASS", "A6", f"{len(referenced)} referenced paths checked")


def check_stale(root, stale):
    text = (root / "trip-data.json").read_text(encoding="utf-8")
    for s in stale:
        for m in re.finditer(re.escape(s), text, flags=re.IGNORECASE):
            ctx = text[max(0, m.start() - 50): m.end() + 50].replace("\n", " ")
            report("FAIL", "A7", f"stale text '{s}': ...{ctx}...")
    report("PASS", "A7", f"{len(stale)} stale strings checked")


def check_prose_numbers(data):
    """Warn when a hike description quotes a km figure far from distance_km."""
    for d in data["days"]:
        if not is_hike(d):
            continue
        dist = d.get("distance_km", 0)
        for m in re.finditer(r"(\d+(?:[.,]\d+)?)\s*km\s+(?:round[- ]trip|return|in total|total)", d.get("description", "")):
            val = float(m.group(1).replace(",", "."))
            if dist and abs(val - dist) / dist > 0.1:
                report("WARN", "A8", f"day {d['day']}: text says '{m.group(0)}', distance_km {dist}")
    report("PASS", "A8", "prose numbers scanned")


def check_privacy(root):
    patterns = list(PRIVACY_PATTERNS)
    terms = root / "private-terms.txt"
    if terms.exists():
        patterns += [rf"{re.escape(t.strip())}" for t in terms.read_text(encoding="utf-8").splitlines() if t.strip()]
    else:
        report("WARN", "A9", "no private-terms.txt; scanning generic patterns only")
    hits = 0
    for f in root.rglob("*"):
        if not f.is_file() or f.suffix.lower() not in PUBLISHED_EXT:
            continue
        if f.name in ("pre_patagonia_trip.json", "private-terms.txt"):
            continue  # git-ignored private sources
        text = f.read_text(encoding="utf-8", errors="ignore")
        for pat in patterns:
            for m in re.finditer(pat, text):
                hits += 1
                report("FAIL", "A9", f"{f.relative_to(root)}: '{m.group(0)}'")
    report("PASS", "A9", f"privacy scan ({hits} hits)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--stale", nargs="*", default=[])
    args = ap.parse_args()
    root = Path(args.folder)
    try:
        data = load_json(root / "trip-data.json")
    except Exception as e:  # noqa: BLE001 - report any parse failure
        print(f"FAIL [A1] trip-data.json does not parse: {e}")
        return 1
    checks = [
        ("A1", lambda: check_schema(data)), ("A2", lambda: check_dates(data)),
        ("A3", lambda: check_totals(data)), ("A4", lambda: check_profiles(data, root)),
        ("A5", lambda: check_km_ranges(data)), ("A6", lambda: check_files(data, root)),
        ("A7", lambda: check_stale(root, args.stale)), ("A8", lambda: check_prose_numbers(data)),
        ("A9", lambda: check_privacy(root)),
    ]
    for name, run in checks:
        try:
            run()
        except (KeyError, IndexError, TypeError, ValueError) as e:
            # incomplete data: report it and keep going so the other results still print
            report("FAIL", name, f"could not run, missing or malformed field: {e!r}")
    for level in ("FAIL", "WARN"):
        for line in results[level]:
            print(f"{level} {line}")
    print(f"\n{len(results['FAIL'])} fail, {len(results['WARN'])} warn")
    return 1 if results["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
