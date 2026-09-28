# trip-data.json contract — Patagonia 2026 (v2)

The shared layout between `trip-data.json`, `index.html` and the route files.
It starts from the existing per-day schema (see `trip-template.md`), keeps the whw-chill additions, and adds a few fields this trip needs.
**Any field not listed here keeps its current meaning.**

## Guide days

| Day | Date | `day_type` | Label | GPX / profile |
|---|---|---|---|---|
| 1 | 2026-11-19 | travel | Home city → Santiago | — |
| 2 | 2026-11-20 | city | Santiago | — |
| 3 | 2026-11-21 | city | Santiago | — |
| 4 | 2026-11-22 | travel | Santiago → Buenos Aires | — |
| 5 | 2026-11-23 | city | Buenos Aires | — |
| 6 | 2026-11-24 | city | Buenos Aires | — |
| 7 | 2026-11-25 | travel | Buenos Aires → El Calafate | — |
| 8 | 2026-11-26 | travel | El Calafate → El Chaltén | — |
| 9 | 2026-11-27 | hike | Laguna Torre | gpx/day-9.gpx, elevation/day-9-profile.json |
| 10 | 2026-11-28 | hike | Cóndores & Águilas viewpoints → El Calafate | day-10 |
| 11 | 2026-11-29 | hike | Perito Moreno walkways & Nautical Safari | day-11 |
| 12 | 2026-11-30 | travel | El Calafate → Hotel Las Torres | — |
| 13 | 2026-12-01 | hike | Base Torres | day-13 |
| 14 | 2026-12-02 | hike | Full Paine & Grey Lake | day-14 |
| 15 | 2026-12-03 | hike | French Valley | day-15 |
| 16 | 2026-12-04 | travel | Las Torres → Puerto Natales → Santiago | — |

## New or changed day fields

```jsonc
{
  "day_type": "hike" | "city" | "travel",          // NEW. Required.
  // hike days: distance_km, ascent_m, descent_m, estimated_hours (walking time only, not the whole outing), difficulty, elevation_profile,
  //   links.gpx_download as today.
  // city/travel days: distance_km/ascent_m/descent_m/estimated_hours = 0, difficulty = "Easy" (kept for schema),
  //   elevation_profile = "", links.gpx_download = "", map = "". The app must NOT render stats, difficulty,
  //   elevation, map or GPX for non-hike days.

  "meals": "B / L / D",                             // NEW, optional. What's included, e.g. "Breakfast", "Full board + open bar".

  "flights": [                                      // NEW, optional. No confirmation codes, seats or prices, ever.
    { "airline": "LATAM", "flight": "LA 455",
      "from": "Santiago", "from_code": "SCL", "depart": "11:28",
      "to": "Buenos Aires Aeroparque", "to_code": "AEP", "arrive": "14:40", "arrive_day_offset": 0,
      "notes": "Recheck the time in the LATAM app." }
  ],

  "transport_to_start": {                            // whw-chill field, extended. Optional.
    "type": "Private transfer", "from": "...", "to": "...",
    "duration": "~3 h", "distance_km": 215, "time": "To be confirmed by Say Hueque", "notes": "..." },
  "transport_after_hike": [                          // whw-chill field. Optional.
    { "leg": 1, "type": "Private transfer", "from": "...", "to": "...", "duration": "~3 h", "distance_km": 200, "time": "...", "notes": "..." } ],

  "accommodation": {                                 // CHANGED: options[] replaces name/url.
    "location": "El Chaltén",
    "options": [ { "name": "Desierto Suites", "url": "https://...", "address": "...", "phone": "...", "notes": "Breakfast included. 2 nights." } ]
  },                                                 // null on day 1 (overnight flight) and day 16 (no hotel).

  "optional_activities": [                           // whw-chill field, extended. City suggestions, kayak, Grey boat, Las Torres alternatives.
    { "name": "...", "duration": "...", "time_of_day": "...", "operator": "...", "url": "...", "departure": "...",
      "status": "suggested" | "likely" | "optional" | "alternative", "notes": "..." } ],

  "taxi_services": [ { "name": "...", "phone": "...", "url": "...", "notes": "..." } ],  // whw-chill field. Optional.

  "stats_note": {                                    // NEW (review round 1). Hike days: where the numbers come from.
    "source": "...", "source_url": "...", "processing": "...", "operator": "..." },

  "food_stops": [                                    // EXTENDED (review round 2). km only on hike days, else null.
    { "name": "...", "type": "restaurant|cafe|pub|shop|takeaway", "meal": "breakfast|lunch|dinner|drinks|snack|trail-lunch",
      "km": null, "area": "...", "url": "...", "diet": ["vegetarian"|"vegan"|"vegetarian-friendly"|"vegan-options"],
      "notes": "...", "unconfirmed": true } ],

  "photo_captions": ["..."],                         // NEW, optional. Overrides the automatic Wikimedia caption per photo.

  "levels": {                                        // NEW (levels, 2026-09-28). Hike days only. "Full" is the day itself.
    "easy":     { "name": "...", "summary": "...", "distance_km": 1.5, "ascent_m": 30,   // ascent_m may be null ("little climbing")
                  "estimated_hours": 1, "difficulty": "Easy", "logistics": "...", "to_confirm": true },
    "moderate": { "same_as_full": true, "note": "..." }                                   // or a full option like "easy"
  }
}
```

Hike-day notes:
- `estimated_hours` is **walking time only**, on the day and in `levels`. The whole-day length goes in the description.
- `elevation_profile: null` (explicit) means the day has no single route to chart, e.g. day 14, a van tour with two short walks. The validator reports it as a warning, not a failure.
- `waypoints[].km` may be omitted when the stops are along a drive; the app then shows no distance.

## Trip-level fields

```jsonc
"short_view": {                                      // NEW (2026-09-28). Content for ?view=short.
  "summary": "...",                                  // replaces trip.description on the short Overview
  "must_know": [ { "group": "Before you leave", "items": [ { "title": "...", "text": "...", "url": "optional" } ] } ],
  "gear": [ { "item": "...", "levels": ["easy", "moderate", "full"] } ]   // short packing list, filtered by level
}
```

URL parameters: `?level=easy|moderate|full` (default Full, remembered per browser) and `?view=short`.
Both can be combined. The full guide at Full level shows everything the guide showed before levels were added.

Unchanged and still used on every day type: `label`, `date`, `description`, `warnings`, `interesting_links`
(city sights go here, with real `url` where known), `food_stops`, `photos`, `location_keywords`, `youtube`.
The lists `water_sources`, `escape_routes`, `waypoints`, `toilet_facilities` and `resupply_notes` may be empty on non-hike days; the app hides empty sections.

## Trip-level

- `trip.name` = "Patagonia 2026". `trip.dates` = 2026-11-19 → 2026-12-04. `trip.group_size` = 19.
- `trip.hero_photo_url` (whw-chill): optional.
- `trip.total_distance_km` / `total_ascent_m` = sums over **hike days only**.
- `preparation.what_to_expect`: 16 entries, one per day, each starting "Day N:".
- `general_info.emergency_contacts` includes the Say Hueque travel specialist.
- `general_info.food_tips`: optional {heading: text} shown as "Eating vegetarian and vegan" on General Info.
- `trip.hero_photo_caption`: optional caption for the hero photo.
- `trip-data-comprehensive.json` is a full backup of the data before any simplifying. The app does not read it.

## Never in any published file
Traveller names (anyone's), booking/confirmation codes, Hotels.com/Expedia numbers, seat numbers, prices paid.
