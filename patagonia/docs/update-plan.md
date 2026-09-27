# Patagonia guide — update plan (v2 itinerary + pre-trip + whw-chill port)

Plan agreed and built 2026-09-27; see Status at the end. Itinerary source: [itinerary-v2.md](itinerary-v2.md).

## Decisions (answered 2026-09-27)

| # | Decision |
|---|---|
| Q1 | The guide becomes **16 days, 19 Nov – 4 Dec**: Austin → Santiago (2 nights) → Buenos Aires (3 nights) → El Calafate 25 Nov (**Calafate Parque Hotel**, taxi from FTE) → Say Hueque days as guide days 8–16. Source: `pre_patagonia_trip.json`. |
| Q2 | The guide ends with **LA 252 PNT 12:00 → SCL 14:05 on 4 Dec**. Several of the group are on it. No flights home in the guide. |
| Q3 | Passports: **a mix of US and Indian**. The entry section covers both, for Argentina and Chile. |
| Q4 | Private transfers show duration and distance, plus "time to be confirmed by Say Hueque". |
| Q5 | Grey Glacier boat: shown as **optional** (not included, book ahead, weather-dependent) next to the lakeshore walk. |
| Q6 | Las Torres days: the recommended excursion in full, plus 1–2 one-line alternatives each day. |
| Q7 | Sunset kayak moves to the **25 Nov evening, El Calafate**, marked "likely — to be confirmed". Removed from 29 Nov. |
| Q8 | Trip name: **"Patagonia 2026"**. |
| Q9 | Public site may show: the Say Hueque specialist's contact details, and hotel addresses and phones. **Not** any traveller names (including the organisers'), booking codes, seats or prices. |
| Q10 | Update in place at `srgorti-hub.github.io/trips/patagonia/`, and refresh the trip picker card. |
| Q11 | I source a Laguna Torre GPX (public track, checked against the operator's 19 km, source cited). |
| Q12 | Housekeeping approved: commit `whw-chill/`; delete the 5 duplicate root GPX files + the 2 unused O-Circuit files; delete `patagonia-files.zip`. The WHW resampled GPX files stay untracked. |

## What changes, in one table

| Area | Today | After |
|---|---|---|
| Span | 9 days, 22–30 Nov | 16 days, 19 Nov – 4 Dec (7 city/travel days + 9 Patagonia) |
| Group | 21 | 19 (the pre-trip days are written for the two of you, without names) |
| Hotels | 3 generic names; only Las Torres named | Solace · Miravida · Calafate Parque · Desierto Suites · Glaciares de la Patagonia · Las Torres, each with a checked link |
| 25 Nov | — | arrive FTE, taxi, sunset kayak (likely) |
| 29 Nov | walkways + boat + kayak | walkways + boat |
| 2 / 3 Dec | French Valley / Full Paine | **swapped**: Full Paine + Grey / French Valley, each with alternatives |
| 4 Dec | to Puerto Natales, hotel night | Las Torres → PNT → LA 252 to Santiago; guide ends |
| Border | generic biosecurity note | SAG digital affidavit within 48 h (link), passport, no fresh food; entry rules for US + Indian passports |
| App shell | Patagonia fork | whw-chill shell + new transport/flight and options blocks (§1) |

## 1. App changes (port from whw-chill + what this trip needs)

From whw-chill (the two index.html files are ~97% the same code):
1. Transparent top nav with the toggles on the hero; tab bar sticky at `top:0`; remove the "Trail & Co" logo and footer line.
2. `hero_photo_url` plus the photo lookup order: local file → URL in the data → Wikimedia → hide.
3. Accommodation `options[{name,url}]` shown as links, plus address/phone (new, per Q9).
4. Difficulty mix one per line; `resolveYoutubeLink` / `resolveServiceLink`; points of interest fall back to Google only when there is no URL.
5. Taxi-services section. It's useful now for the FTE → hotel taxi on 25 Nov.

Keep from Patagonia: removing the leading "Day N:" in What to Expect.

New, because this trip is now travel-heavy:
6. Show `transport_to_start` / `transport_after_hike` and a **flight** form (flight no., from → to, times; no codes or seats) at the top of the day detail.
7. Show `optional_activities` — Santiago/BA suggestions, kayak, Grey boat, Las Torres alternatives.
8. **City and travel days must look right, not like empty hiking days.** No 0-km stats row, no empty elevation chart, no "Difficulty: Easy", no hidden GPX button. Hero totals (km, ascent, "hiking days") count hiking days only. Overview cards label them "City" / "Travel".
9. Small leftovers: the `<title>`, the "files.zip from Claude.ai" upload screen, the always-"Wikimedia Commons" photo credit, the Walk Highlands slot (hide when empty).

Not in scope: Acelrix design system (neither trip app uses it), print, offline, live weather.

## 2. Checks I will run (and report pass/fail on)

### A. Data integrity (a `validate.py` script, which the test plan promised but was never written)
- A1. JSON parses. Every key the app reads is present and the right shape (template rules: difficulty enum, precipitation 0–1, `essential` is a boolean, keywords ≥ 1, allowed types).
- A2. Dates: 16 days, numbered 1–16, consecutive, 19 Nov – 4 Dec. Weekdays match the bookings.
- A3. Totals equal the sum of the hiking days.
- A4. Each elevation profile ends at `distance_km` (±5%) and matches `ascent_m` (±10%). **Fails today** on 4 days.
- A5. Waypoint, toilet and food-stop km values are ≤ the day's distance. **Fails today** on 2 days.
- A6. Every referenced file exists; list files nothing points to.
- A7. Stale-text sweep, including the old dates, "21", "kayak" on 29 Nov, a Puerto Natales hotel, the old day order, "18 km", "850m", "3,000m altitude", and the trip picker's "97 km · 3,054 m".
- A8. Prose (description, what_to_expect, training) quotes the same numbers as the day fields.
- A9. **Privacy scan** of every published file: no confirmation codes or Hotels.com/Expedia numbers (the exact terms live in the git-ignored `patagonia/private-terms.txt`), traveller names, seats or prices. Also check that `pre_patagonia_trip.json` is git-ignored.

### B. Links (every URL fetched and read, not just a 200 status)
- B1. Six hotel sites: each is the right property.
- B2. AllTrails and Komoot: each points to the right trail, re-mapped for the swapped days. Replace the Komoot search query.
- B3. YouTube: a real video per hiking day where one can be confirmed; otherwise keep the search.
- B4. Points of interest and city sights (museums, Neruda house, MALBA etc.): official pages where they exist.
- B5. Operational: SAG affidavit, Las Torres, Parques Nacionales / CONAF, Argentina/Chile immigration pages.

### C. Facts that must be right on the day (primary/official sources, cited in my report)
- C1. **Entry rules for US and Indian passports**, Argentina and Chile. For Indian passports: visa vs Argentina's electronic travel authorisation, and whether a valid US visa changes it. Note Chile being entered twice (20 Nov SCL, 30 Nov by land) and Argentina twice (22 Nov, 25 Nov domestic onward).
- C2. SAG affidavit and the 48 h window; biosecurity rules (also apply on arrival at SCL on 20 Nov).
- C3. Park fees: Los Glaciares for El Chaltén (not included), Perito Moreno (included), Torres del Paine (included via Las Torres).
- C4. Emergency numbers, both countries plus hospitals.
- C5. Weather: Santiago, Buenos Aires, El Chaltén/El Calafate and Torres del Paine for late Nov / early Dec.
- C6. Time zones and **flight times**: LA 455 after Chile's summer-time change; LA 252 "3h 5m" vs 2h 05m (a stop?). Check with LATAM's public schedule.
- C7. Currency and cash for Argentina and Chile now; the VAT exemptions quoted in the hotel tips.
- C8. Sunset kayak (25 Nov): the operator's evening departure time vs a 17:40 landing and the taxi into town.
- C9. Santiago/BA suggestions: closing days on the planned dates (e.g. museums closed Mondays; La Chascona timed entry; the San Telmo fair on Sunday).

### D. Route stats
- D1. Source a Laguna Torre GPX (Q11). Days without hiking get no elevation profile at all (replacing the fake drive profiles).
- D2. **Rule:** shown numbers come from the GPX of the guided route. The operator's figure goes in the text where it differs (e.g. Cóndores 7.0 km / +183 m vs 4.8 km / 220 m).
- D3. Regenerate all profiles through `gpx-tool.html`.

### E. Visual (run and screenshot)
- E1. Every tab, light and dark, desktop and phone width.
- E2. A city day, a travel day, a hiking day and a Las Torres day: blocks render, links work, no broken images, units toggle.
- E3. Photos page, GPX tool, trip picker card.
- E4. No leftover setup text on screen.

### F. Before publishing
- F1. Privacy scan (A9) passes.
- F2. Housekeeping per Q12.
- F3. One commit per phase; say how far ahead of origin we are and ask before any push.

## 3. Still open (not blocking the start)
- Transfer times (Q4): from Say Hueque, later.
- Kayak on 25 Nov: booking to be confirmed.
- Grey boat: whether anyone books it.

## 4. Order of work

1. **Housekeeping** (Q12) and git-ignore `pre_patagonia_trip.json`. Commit.
2. In parallel:
   - **2a. App** — §1 changes in `index.html`, tested against a sample of city, travel and hiking days.
   - **2b. Data** — new 16-day `trip-data.json`, with the B and C research running alongside.
   - **2c. Routes** — Laguna Torre GPX + profile regeneration (D).
3. **Validate and publish** — `validate.py` (A), visual pass (E), privacy (F1), trip picker card, commit, ask to push.

## Status (2026-09-27)

Done:
- App: whw-chill port, day types (hike/city/travel), flights, transfers, options, hotel address/phone, meals; city/travel warnings shown in the day body. Old 9-day data still renders.
- Data: 16-day `trip-data.json`. `python tools/validate_trip.py patagonia` → 0 fail (warnings are only missing photo/map images, which fall back to Wikimedia). 77 URLs fetched: all load except AllTrails, which blocks automated requests (pages confirmed via search).
- Routes: GPX + profiles for hike days 9, 10, 11, 13, 14, 15. Laguna Torre built from OpenStreetMap + Copernicus DEM. Days 10 and 13 elevations smoothed (decision: smoothed GPX). French Valley trimmed of the boat legs.
- Final hike figures: Laguna Torre 17.3 km / +533 m · Cóndores 7.4 / +236 · Perito Moreno 3.6 / +174 · Base Torres 19.1 / +975 · Full Paine 9.0 / +178 · French Valley 18.8 / +686. Totals 75.2 km / 2,782 m.
- Trip picker card, trip template (new fields), `tools/validate_trip.py`.

Found during checks (in the guide as notes):
- **LA 252 (4 Dec) is nonstop, ~3 h 05 m.** Both ends are UTC−3 in December, so the booked 14:05 arrival is likely a winter-time figure; expect ~15:05.
- **LA 455 (22 Nov)** likely departs ~12:30 under Chile summer time, not 11:28; arrival 14:40 unchanged.
- Mon 23 Nov is an Argentine public holiday (moved from 20 Nov). MALBA closed Tuesdays; Rosedal closed Mondays; La Catedral milonga Tue–Sat only.
- Indian passports: Argentina and Chile both waive the visa with a qualifying valid US visa (Chile: valid ≥ 6 months on arrival, incl. the 30 Nov land entry).
- Los Glaciares fee for El Chaltén: ARS 50,000/day, online only (ventaweb.apn.gob.ar). Torres del Paine entry is covered by Las Torres.
- The sunset kayak may start ~18:00, which a 17:40 landing can't make; the guide says to confirm.

Still open:
- Check LA 455 / LA 252 / AR 1852 times in the airline apps.
- Transfer times from Say Hueque (four transfers). Tell Say Hueque the 25 Nov hotel (Calafate Parque) for the 26 Nov pickup.
- Kayak booking; Grey boat bookings.
- Desierto Suites has no working website (Instagram used); Calafate Parque's phone is the chain's central line.
- Unverified: Las Torres alternative excursions (from a reseller), Puerto Natales hospital phone, Torres del Paine climate figures.
- Final screenshot pass after your dry run.
