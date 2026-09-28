# Figures check: Torres del Paine days (13–15)

Independent check of the hiking figures in `trip-data.json` for days 13, 14 and 15. Checked 28 Sep 2026. No data files were changed.

**How the route files were measured.** Distance is the sum of haversine steps between track points. Ascent and descent are given two ways: raw (every rise counted) and with a 5 m hysteresis (a rise counts only after the height has moved 5 m from the last counted point), which removes most GPS jitter. Script: sums over `<trkpt>` in `gpx/day-N.gpx`.

| File | Points | Distance | Ascent raw / 5 m | Descent raw / 5 m | High point |
|---|---|---|---|---|---|
| `gpx/day-13.gpx` | 236 | 19.07 km | 1,008 / 960 m | 1,008 / 960 m | 877 m at km 9.7 |
| `gpx/day-14.gpx` | 159 | 8.99 km | 206 / 135 m | 201 / 133 m | 105 m at km 4.7 |
| `gpx/day-15.gpx` | 88 | 18.83 km | 692 / 670 m | 691 / 669 m | 486 m at km 9.4 |

`maps/` does not exist in the repo, so every `map` field (`maps/day-13-map.jpg` etc.) points at a missing file. The page hides the map section when the file is missing, so nothing shows, but the fields are dead.

---

## Day 13 — Base Torres

| Field | Value in guide | What I found | Verdict |
|---|---|---|---|
| distance_km | 19.1 | GPX 19.07 km. Las Torres 18.8 km ([excursion page](https://lastorres.com/en/circuitos-por-el-dia/las-torres-base/), [tools list](https://tools.lastorres.com/excursions-videos)). Swoop 18.8 km ([Swoop](https://www.swoop-patagonia.com/chile/torres-del-paine/hotels/torres/excursions)). | OK |
| ascent_m / descent_m | 975 / 975 | GPX 1,008 raw, 960 with 5 m hysteresis. 975 sits between. | OK |
| estimated_hours | 9 | Las Torres 8 h total. The walk starts at the hotel door, so this is both walking time and the whole outing. | OK |
| difficulty | Strenuous | Las Torres "High". | OK |
| Waypoint Ascencio bridge | km 1.3 | GPX low point by the river at km 1.3 (124 m). | OK |
| Waypoint Windy Pass | km 3.5 | GPX high point before Chileno is at km 4.2 (464 m). At km 3.5 the track is still climbing (about 330 m). | Change to 4.2 |
| Refugio Chileno (waypoint, text, escape route, food, toilet) | km 5.5 | GPX point nearest PeakVisor's Chileno coordinates (-50.9572, -72.9106) is at km 5.3, 24 m away. PeakVisor gives 4.4 km on a shorter variant ([PeakVisor](https://peakvisor.com/poi/refugio-chileno.html)). | OK (5.3 is closer if you want precision) |
| Torres camp | km 8 | GPX: the climb starts after a dip at km 8.0–8.2. | OK |
| La Morrena begins | km 8.5 | GPX: the steep section starts at km 8.2 (578 m) and reaches the lake at about km 9.2 (+290 m). | Change to 8.2 (minor) |
| Mirador Base Torres | km 9.6 | GPX turnaround at km 9.55–9.74. | OK |
| Text: "45 to 60 minutes" on La Morrena | — | About 1 km and 290 m of climb on the GPX. 45–60 min is realistic for a guided group. | OK |
| stats_note operator line | "about 8 hours, high difficulty" | Matches the Las Torres page. | OK |
| **Easy** Laguna Azul: distance_km | 1.0 | Las Torres "1 km", "an easy 30 minute walk" ([Azul Lagoon page](https://lastorres.com/en/circuitos-por-el-dia/azul-lagoon/)); tools list and Swoop also 1 km. | OK |
| Easy ascent_m | null | Not published anywhere. The page says "easy". Shows as "little climbing", which fits. | OK |
| Easy estimated_hours | 4 | Las Torres "4 hrs total" (whole outing including van). | OK |
| Easy summary: Ascencio horse ride 7 km, 3 h | — | Tools list: 7 km, 3 h, Easy. | OK |
| **Moderate** Chileno: distance_km | 10.0 | GPX 5.34 km each way = 10.7 km. PeakVisor 4.4 km each way = 8.8 km. Las Torres horse+hike: 9.2 km to Chileno and back ([page](https://lastorres.com/en/circuitos-por-el-dia/las-torres-viewpoint-horseback-riding-hiking/)). 10 is a fair middle. | OK |
| Moderate ascent_m | 545 | GPX, hotel → Chileno → hotel: out +362 m, back +71 m = **433 m** (5 m), 464 m raw. The 545 in the research doc comes from PeakVisor's "+419 m", but 419 m is Chileno's altitude, not the climb. Start is at 137 m, so the net rise is about 280 m. | Change to 450 |
| Moderate estimated_hours | 4.5 | About 2 h up (Swoop hotel page, PeakVisor 2 h 15), 1.5 h down, plus a break. Starts at the hotel, so this is also the whole outing. | OK |
| Moderate summary: Lenga Forest 8 km, 3–4 h | — | Las Torres page 3–4 h; tools list 8 km, 3 h, Easy. | OK |
| Optional: Mirador Cuernos half day, about 4 h, 6 km, low | — | Las Torres "6 km", "4 hrs total", "Low" ([Los Cuernos page](https://lastorres.com/en/circuitos-por-el-dia/los-cuernos/)). | OK |
| Optional: Native lenga forest, 3–4 h, 8 km, low to medium | — | As above. | OK |

---

## Day 14 — Full Paine & Lago Grey

| Field | Value in guide | What I found | Verdict |
|---|---|---|---|
| distance_km | 9.0 | Comes from the Wikiloc track Guardería Pudeto → Salto Grande → Mirador Cuernos and back (my measurement: 8.99 km). That walk is not a stop on this tour. Las Torres: "4 km" walking ([Full Paine page](https://lastorres.com/en/circuitos-por-el-dia/full-paine-glacier-grey/)); Swoop copies 4 km; the Las Torres tools list says "1 km". Measured separately, the two walks on the tour add to about 6.5 km: Salto Grande car park to the falls 0.57 km each way on the GPX (1.2–1.4 km round trip; [torresdelpaine.com](https://torresdelpaine.com/en/tourist-attraction/salto-grande-waterfall-viewpoint/) 1.4 km), plus Grey beach and peninsula 5.3 km ([The Photo Hikes](https://thephotohikes.com/mirador-de-los-hielos-hike)) or 5.5 km ([torresdelpaine.com](https://torresdelpaine.com/en/tourist-attraction/glaciar-grey-viewpoint-from-lago-grey-beach/)). | Change to 6.5 (see correction section) |
| ascent_m | 178 | Same wrong track (my measurement: 206 raw / 135 with 5 m). Actual walks: Salto Grande about +18 m (GPX), peninsula +60 m (The Photo Hikes). Komoot shows 260 m for the peninsula, but that is height-model noise on a flat beach; the same author's page says 60 m. | Change to 80 |
| descent_m | 164 | Every walk is out and back from the van, so descent equals ascent. 164 ≠ 178 is itself a sign of a raw GPS track. | Change to 80 |
| estimated_hours | 8 | Las Torres 7–10 h for the whole day. This is the whole outing, not walking (walking is about 2.5–3 h). The tools list's "3 HRS" matches the "3 hrs catamaran" line on the tour page, not the day. | OK as whole-day figure |
| difficulty | Moderate | Las Torres "Easy"; Swoop "Easy". 6.5 km flat with 80 m of climb is Easy. | Change to Easy (decision: then Full and Easy share a rating) |
| stats_note | Wikiloc Pudeto–Salto Grande–Mirador Cuernos | Wrong route. | Replace (text below) |
| Waypoints km 0 / 1 / 2.5 / 4 / 6 / 9 | Hotel, Puente Negro, Nordenskjöld, Sarmiento, Salto Grande, Lago Grey | These are not real positions. Lago Grey is about 25 km from the hotel in a straight line and further by road (the drive to Pudeto alone takes about 45 min), and the numbers do not match walking either. | Remove km (see below) |
| Toilets | Salto Grande km 6, Lago Grey km 9 | Same invented positions. | Set km to null (the toilet list already handles null) |
| Text: "walking adds up to about 9 km" | — | See above. | Change |
| Text: Grey III "about 2 h 45 min round trip" (description and optional_activities) | — | Hotel Lago Grey: "three-hour journey" (English) and "travesía de 3 horas" (Spanish) ([navigation](https://www.lagogrey.com/en/navigation/), [navegación](https://www.lagogrey.com/navegacion/)). Las Torres: "3 hrs catamaran". | Change to "about 3 h" |
| Text: 30 to 45 minute beach walk | — | Hotel Lago Grey, both languages: 30–45 minutes to the boarding area. | OK |
| Text: "a minimum number of passengers" | — | Hotel Lago Grey: minimum 25 passengers. The group is 19, so the boat depends on other passengers. | OK, better to state 25 |
| Grey III price CLP 120,000, from 1 Oct 2026; 09:30, 13:00, 16:00 | — | Hotel Lago Grey: adults CLP 120,000 round trip, 1 Oct 2026 – 30 Apr 2027; departures 09:30, 13:00, 16:00; check-in 1 h before. | OK |
| Food: lunch on the 13:00 boat | — | Las Torres: boat "departing at 1pm", lunch "during the sailing trip". | OK |
| Easy: distance_km | 2.0 | Salto Grande 1.2–1.4 km plus short roadside stops ≈ 2 km. But the Easy summary also offers the Grey III boat, which needs the 30–45 min beach walk each way (about 2.6 km round trip). Easy with the boat is about 4.5 km. | OK for viewpoints only; add "about 4.5 km with the boat" to the summary |
| Easy ascent_m | null | Salto Grande about +18 m. "Little climbing" is right. | OK |
| Easy estimated_hours | 8 | Same van day. | OK |
| Moderate | same_as_full | The standard tour is already the easy peninsula walk; there is no harder version. | OK |
| Optional: Lakes Trail 15 km, 7–8 h, medium | — | Tools list: 15 km, 7–8 h, Moderate. | OK |
| Optional: Laguna Azul about 4 h, easy | — | Las Torres 4 h, Easy. | OK |
| links.alltrails `mirador-cuernos`, links.komoot `tour/1032637103` | — | Both describe the Mirador Cuernos walk, not this day. | Move/replace (see below) |
| elevation_profile, gpx_download, map | day-14 files | Profile and GPX are the Mirador Cuernos walk from the Pudeto ranger station. `maps/day-14-map.jpg` does not exist. | Remove from day 14 (see below) |

---

## Day 15 — French Valley

| Field | Value in guide | What I found | Verdict |
|---|---|---|---|
| Where Full ends | "French Valley viewpoint", stats_note "to Mirador Francés" | GPX high point 486 m at km 9.41 (-51.0082, -73.0532), labelled "French Valley Viewpoint" in the file. Mirador Británico is at about 750–770 m, well above anything on the track. Distance and climb match Paine Grande → Mirador Francés: 18.5 km, 549 m ([Travel Yes Please](https://www.travelyesplease.com/travel-blog-french-valley-day-hike-torres-del-paine/)). **It ends at Mirador Francés.** | OK |
| distance_km | 18.8 | GPX 18.83 km. Travel Yes Please 18.5 km. Las Torres 20 km (English page and tools list) and "18 km de trekking" (Spanish page). | OK |
| ascent_m / descent_m | 686 / 688 | GPX 692/691 raw, 670/669 with 5 m. Travel Yes Please 549 m. | OK |
| estimated_hours | 10 | Las Torres 12 h total with 1.5 h van and 1 h boat, leaving 9.5 h. Walking time for this route is 7–8 h (Travel Yes Please). 10 is neither the whole outing (12) nor walking. | Change (see "hours" below) |
| stats_note: "Británico would add about 5–6 km and 250–300 m" | — | Italiano → Británico is 10.3 km round trip ([torresdelpaine.com](https://torresdelpaine.com/en/tourist-attraction/britanico-viewpoint/)); Italiano → Francés is 1.8 km each way on the GPX. So Británico adds about 3.3 km each way, **about 6.5–7 km** round trip, and about 280 m (770 − 486). | Change to "about 6–7 km and 250–300 m" |
| stats_note / description: "Las Torres lists 700–800 m of height change" | — | Not on the English or Spanish Las Torres pages, the tools list or Swoop. The Spanish page only says "desniveles importantes". Not found in `private-terms.txt`. | Unsure: remove or source it |
| Description: "about 10 hours of that is walking" | — | See estimated_hours. | Change to "about 7 to 8 hours of walking, plus breaks and the wait for the boat" |
| Description: "about 2.5 km up a steep path" (and waypoint note "About 2.5 km above Italiano") | — | GPX: Italiano (km 7.6, -51.0229, -73.0423) to the viewpoint (km 9.4) is 1.8 km with +300 m. Travel Yes Please: "just over a mile" and about 300 m. | Change to "about 2 km" |
| Italiano position: waypoint km 7, toilet km 7, escape route "about km 7", food stop km 7.5 | — | GPX 7.6 km. | Change all to 7.5 |
| French Valley viewpoint waypoint | km 9.5 | GPX 9.4. | OK |
| Return to Paine Grande | km 18.8 | GPX 18.83. | OK |
| Drive 45 min to Pudeto; boat about 30 min | — | Las Torres "1.5 hrs by van" (both ways) and "1 hour by boat" (both ways). | OK |
| Moderate summary: boats back at 17:00 or 18:40 | — | catamaranpehoe.com (both languages) for Nov–Mar: Paine Grande → Pudeto 17:00 and 18:40 (and 08:40/09:20, 11:20). The first outbound boat is still 08:00 (Spanish) vs 08:30 (English); the research doc's note on this stands. Price CLP 28,000 per leg. | OK |
| **Easy** Los Cuernos viewpoint: distance_km | 6.0 | Las Torres 6 km. My measurement of the day-14 GPX from the Salto Grande car park and back: 6.25 km. The Photo Hikes 6.42 km. | OK |
| Easy ascent_m | 150 | The day-14 GPX from the car park: 94 m (5 m) / 145 m raw. The Photo Hikes 150 m. | OK (100–150; 150 is the high end) |
| Easy estimated_hours | 4 | Las Torres "4 hrs total", 1:30 van. Whole outing. | OK |
| **Moderate** Italiano: distance_km | 15.0 | GPX: 7.6 km each way = 15.2 km. | OK |
| Moderate ascent_m | 400 | GPX: out +258 m, back +109 m = 367 m (5 m); 390 m raw. | OK (370 is closer) |
| Moderate estimated_hours | 5.5 | 15 km of rolling trail is about 5–5.5 h of walking. But the day is still about 12 h door to door, because the group waits for the 17:00 boat. This is walking time, unlike the other levels. | Change (see "hours" below) |
| Moderate summary: Patagón 9.5 km, flat, 4 h | — | Tools list: 9.5 km, 4 h, Easy. | OK |
| links.alltrails `campamento-paine-grande-mirador-britanico` | — | That is the Británico route, which the group does not do. AllTrails has "Camp Paine Grande – Camp Italiano – Frances Glacier Lookout": https://www.alltrails.com/trail/chile/magallanes/campamento-paine-grande-campamento-italiano-mirador-glaciar-frances | Change |
| Optional: Los Cuernos Trail about 23 km, 6–8 h, medium to high | — | Tools list 23.2 km, 6–8 h, Medium; Swoop "Medium-High". | OK |
| Optional: horse ride about 13 km, about 6 h | — | Only in Swoop (full-day version). The tools list shows only the half-day rides (7–8 km, 3 h). | Unsure: confirm with Las Torres |
| Warning: "12 hours including transport" | — | Las Torres 12 h total. | OK |

---

## estimated_hours means different things on different days

`index.html` (`hikeTotals`) adds `estimated_hours` across all hike days for the trip total, so mixed meanings end up in one number.

| Day / level | Value | What it measures |
|---|---|---|
| 13 Full | 9 | Whole outing (starts at the hotel door) |
| 13 Easy | 4 | Whole outing, incl. 1.5 h van |
| 13 Moderate | 4.5 | Whole outing (starts at the door) |
| 14 Full | 8 | Whole day incl. van; walking about 2.5–3 h |
| 14 Easy | 8 | Whole day |
| 15 Full | 10 | Neither: whole outing is 12, walking 7–8 |
| 15 Easy | 4 | Whole outing, incl. 1.5 h van |
| 15 Moderate | 5.5 | Walking only; the outing is still about 12 h |

Most values already mean "time away from the hotel". Recommendation: use that meaning everywhere. Day 15 Full → 12, day 15 Moderate → 12. (Alternative, if the team prefers walking time: add a separate `walking_hours` field instead of changing the meaning of this one.)

---

## Day 14 correction

### Proposed values (Full)

| Field | Now | Proposed |
|---|---|---|
| distance_km | 9.0 | **6.5** |
| ascent_m | 178 | **80** |
| descent_m | 164 | **80** |
| estimated_hours | 8 | **8** (whole day; unchanged) |
| difficulty | Moderate | **Easy** |

Basis: Salto Grande out and back 1.2–1.4 km, about +18 m (my GPX measurement, torresdelpaine.com 1.4 km); Grey beach and peninsula 5.3–5.5 km, about +60 m, 1.5–2 h (The Photo Hikes, torresdelpaine.com; Las Torres: "an easy walk to the Peninsula for approximately 1.5 hrs"); the other stops (Puente Negro, Nordenskjöld, Sarmiento, Pehoé) are roadside with no published walking. Las Torres's own figure is 4 km, and its tools list says 1 km. 6.5 km is what the two walks measure; the gap with Las Torres's 4 km is unexplained (they may not walk the full peninsula loop). Ask Las Torres (research doc question 4). If you would rather follow the operator, use 4 km / 60 m.

No public GPX without a login: the Photo Hikes points to Komoot tour 2850899788 ("Mirador de los Hielos Hike", 5.32 km, 1 h 37 min; download needs a Komoot login). Wikiloc returned 403. Start point per The Photo Hikes: Río Pingo guardería/restaurant (-51.1244, -73.1287).

### Proposed stats_note

- source: "Operator figures and published walk lengths"
- source_url: `https://lastorres.com/en/circuitos-por-el-dia/full-paine-glacier-grey/`
- processing: "Salto Grande from the car park and back (about 1.3 km) plus the Grey beach and peninsula walk (about 5.3 km). The rest of the day is by van."
- operator: "Las Torres lists about 4 km of walking and 7 to 10 hours for the whole day, easy."

### Text edits

1. Description, paragraph 1: "Las Torres rates it easy and lists 7 to 10 hours; walking adds up to about 9 km." → "Las Torres rates it easy and lists 7 to 10 hours. The walking is short: about 6 km in total, most of it on the Lago Grey shore."
2. Description, paragraph 2: "a walk along the south shore of Lago Grey to a point looking over the floating ice" → add "(about 5 km there and back, 1.5 hours, flat)". Optional.
3. Description, paragraph 3: "about 2 h 45 min round trip" → "about 3 hours round trip".
4. Description, paragraph 3: "there is a minimum number of passengers" → "it needs at least 25 passengers to sail". Optional but useful for a group of 19.
5. optional_activities, Grey III: duration "About 2 h 45 min" → "About 3 h".
6. levels.easy.summary: after the Grey III sentence, add "With the boat, the beach walk adds about 2.5 km."

### Waypoints

The km values 0, 1, 2.5, 4, 6, 9 are invented. Two options:

- **Recommended: remove `km` from the day-14 waypoints**, keeping them as an ordered list of stops. Note: `index.html` prints `formatDist(wp.km)` without a null check, so a missing km would show "undefined km". The waypoint list needs the same `km != null` guard that the toilet list already has. Until then, the fallback is to keep the stops in the description only and drop the waypoints array.
- Walking-only alternative: two short lists don't fit one km line. If kept, use Salto Grande car park 0, Salto Grande falls 0.6; and Grey guardería 0, beach 0.8, Mirador Isla de los Hielos about 2.6 — but that needs two separate km sequences, so it's worse.

Toilets: set Salto Grande/Pudeto and Lago Grey `km` to null (already handled).

### Route files and links that describe the Mirador Cuernos walk

| Item | Recommendation |
|---|---|
| `gpx/day-14.gpx` | Remove from day 14 (`links.gpx_download`). It is a usable track for the day 15 Easy walk, but it starts at the Pudeto ranger station, 1.4 km before the car park Las Torres uses (9.0 km vs 6.25 km). The data model has no per-level track, and the page always shows the Full track, so there is nowhere to attach it yet. Keep the file in the repo as reference. |
| `elevation/day-14-profile.json` | Remove from day 14 (`elevation_profile`). Same reason. A van day with two short flat walks doesn't need a profile. |
| `maps/day-14-map.jpg` | The file does not exist. Remove the `map` field (same for days 13 and 15, whose map files are also missing). |
| AllTrails `mirador-cuernos` | Remove from day 14. Useful for the day 15 Easy level if levels get links. For day 14, the AllTrails Salto Grande link already sits in `interesting_links`; leave `links.alltrails` empty. |
| Komoot `tour/1032637103` | Remove from day 14. Replace with `https://www.komoot.com/tour/2850899788` (Mirador de los Hielos, the peninsula walk). |

---

## Recommended changes

**Day 13**
- `levels.moderate.ascent_m`: 545 → 450.
- Waypoint Windy Pass km 3.5 → 4.2. La Morrena begins km 8.5 → 8.2 (minor).

**Day 14**
- Full: distance_km 6.5, ascent_m 80, descent_m 80, difficulty Easy, estimated_hours 8 (unchanged). New stats_note as above.
- Text edits 1–6 above.
- Remove waypoint km (with the render guard) or drop the waypoints; toilets km → null.
- Remove `gpx_download`, `elevation_profile`, `map`, AllTrails `mirador-cuernos`; Komoot → tour 2850899788.

**Day 15**
- estimated_hours: Full 10 → 12, Moderate 5.5 → 12 (if "time away from the hotel" is adopted). Description: "about 10 hours of that is walking" → "about 7 to 8 hours of walking, plus breaks and the wait for the boat".
- "about 2.5 km up a steep path" and the waypoint note "About 2.5 km above Italiano" → "about 2 km".
- Italiano km 7 (waypoint, toilet, escape route) → 7.5, matching the food stop.
- stats_note: Británico "about 5–6 km" → "about 6–7 km". Remove or source "700–800 m of height change" (stats_note and description).
- `links.alltrails` → the Paine Grande – Italiano – Frances Glacier Lookout trail.
- Horse ride optional (13 km, 6 h): confirm with Las Torres.

**All days**
- Pick one meaning for `estimated_hours` (recommended: time away from the hotel).
- Remove the `map` fields or add the images.

**Corrections to the research doc (`levels-research-torres-del-paine.md`)**
- PeakVisor "+419 m" is Chileno's altitude, not the climb; the Chileno round trip is about 430–465 m, not 460–545 m.
- Británico is about 3.3 km beyond Francés each way, not about 4 km.
- Grey III is 3 h, minimum 25 passengers.
- "Viewpoint at 890 m" (Base Torres) is no longer on the Las Torres page; the GPX high point is 877 m. Harmless.
