# Figures check: El Chaltén and El Calafate (days 9–11)

Checked 28 Sep 2026 against the route files, OpenStreetMap and published sources. No changes were made to `trip-data.json` or `index.html`.

## Method

- **GPX computation.** Haversine distance over every track point. Ascent and descent computed three ways: raw (every rise counted), with a 5 m threshold (a rise or fall is counted only once it reaches 5 m, which removes GPS and terrain-model noise), and with 3 m and 10 m thresholds as a check. The 5 m figure is the one to compare with the guide.
- **Route files.**
  - Day 9: OpenStreetMap trail line with Copernicus GLO-90 heights, already smoothed over ±100 m. Starts and ends at the Laguna Torre trailhead (end of Los Charitos). The Maestri extension is a separate `<rte>` in the same file.
  - Day 10: a Wikiloc GPS recording that starts in town (-49.3308, -72.8894) and ends 470 m away.
  - Day 11: a Wikiloc GPS recording that starts at the top of the walkways and ends at the harbour on the lakeshore.
- **Point locations.** Taken from OpenStreetMap through Overpass and matched to the nearest track point:
  - Los Cóndores trailhead (node 660024150)
  - Mirador de los Cóndores (node 4722282707)
  - Mirador de las Águilas (node 568391373)
  - Chorrillo del Salto waterfall (node 1237892708) and its parking (way 747061337)
- **What the GPX gives, per day:**

| Day | Distance | Ascent raw / 3 m / 5 m / 10 m | Descent (5 m) | Low–high point |
|---|---|---|---|---|
| 9 | 17.28 km | 626 / 575 / **538** / 479 | 538 | 422–676 m, high point at km 8.25 |
| 10 | 7.39 km | 272 / 249 / **238** / 222 | 249 | 381–583 m |
| 11 | 3.58 km | 212 / 160 / **136** / 72 | 243 (raw 317) | 181–303 m; ends 104 m below the start |

The `elevation/day-N-profile.json` files agree with the GPX in shape and in distance: 17.3, 7.4 and 3.6 km. Because they are sampled every 0.5 km, the climb they show is lower: 384, 212 and 9 m. That matters only if anything reads ascent from them. The charts themselves are fine.

---

## Day 9: Laguna Torre

### Full

| Field | Value in guide | What I found | Verdict |
|---|---|---|---|
| distance_km | 17.3 | GPX 17.28 km, trailhead to Mirador Laguna Torre and back. Say Hueque's 19 km (docs/itinerary-v2.md) is probably measured from the hotel. | OK |
| ascent_m / descent_m | 533 / 533 | GPX 538 / 538 with a 5 m threshold (raw 626; 3 m 575). | OK |
| estimated_hours | 7 | Say Hueque: 7–8 h. A standard walking-time estimate (5 km/h plus 1 h per 600 m of climbing) gives about 4.4 h. 7 h is the whole outing with lunch and stops. | OK as the whole outing (see "Hours" below) |
| difficulty | Moderate | Say Hueque: moderate. | OK |
| stats_note.processing: "Maestri adds about 3.7 km and 180 m" | 3.7 km / 180 m | GPX route: 1.87 km one way, +186 m, so 3.7 km return. | OK |
| stats_note.operator: "high point 719 m" | 719 m | Terrain model high point on the main route is 676 m. 719 m is Say Hueque's figure and is quoted as theirs. | OK (quoted) |
| waypoint Fitz Roy canyon / waterfalls | km 1.5, "about 20 minutes" | Patagonia Scout puts Cascada Margarita at about 1.5 km. The GPX shows about 100 m of climbing to km 1.5, so 20 minutes is brisk for 19 people; 25–30 minutes is more likely. | Unsure; "about 25 minutes" is safer |
| waypoint Cerro Torre viewpoint | km 3 | GPX waypoint "Mirador Cerro Torre" at km 2.94 (624 m). [elchalten.com](https://elchalten.com/v4/en/mirador-del-torre-trek-el-chalten.php): 3 km. Patagonia Scout: 2.5 km. | OK |
| waypoint De Agostini camp | km 8 | Camp is about 0.5 km before the lake viewpoint. GPX lake viewpoint is at km 8.64, so about km 8.1. | OK |
| waypoint Laguna Torre | km 9 | GPX "Mirador Laguna Torre" at **km 8.64**. The out-and-back total of 17.3 km also implies 8.6–8.7 km one way. | Change to 8.6 |
| waypoint Mirador Maestri | km 9.5 | GPX route: 1.87 km beyond the lake viewpoint, so **km 10.5**. [AllTrails](https://www.alltrails.com/trail/argentina/santa-cruz/laguna-torre-y-mirador-maestri), [Patagonia Scout](https://patagoniascout.com/hikes/laguna-torre/) and [Nomadic Samuel](https://nomadicsamuel.com/travel-blog/laguna-torre-trail-guide-day-hike-for-cerro-torre-views): about 2 km each way, adding 1–1.5 h. | Change to 10.5 |
| description: "Mirador Maestri ... about 20 minutes beyond the lake" | 20 min | About 2 km and 186 m of climbing along the moraine: about 45 minutes each way. Sources say 1–1.5 h extra for the return trip. | Change to "about 2 km (45 minutes) beyond the lake" |
| description: "Most of the climbing is in the first 2 km" | — | GPX: 126 m of 538 m (23%) is in the first 2 km. 217 m (40%) is in the first 3 km, up to the viewpoint. The research doc's claim that "almost all of the climbing is in the first 3 km" is also contradicted by the route file. The rest comes from the rise along the valley to the moraine (552 m at km 4.3 to 676 m at km 8.25) and from the undulations on the way back. | Change: "The steepest climbing is in the first 3 km, up to the Cerro Torre viewpoint (about 200 m)." |
| description: first viewpoint "about 3 hours round trip from town" | 3 h | [elchalten.com](https://elchalten.com/v4/en/mirador-del-torre-trek-el-chalten.php): about 1.5 h to the viewpoint, so about 3 h return. | OK. It conflicts with Moderate's 3.5 h (below). |
| description: "Say Hueque lists it as 19 km, 7 to 8 hours ... 719 m" | — | Matches docs/itinerary-v2.md line 85. | OK |
| escape_routes: first viewpoint "about km 2 to 3" | — | km 2.9 | OK |

### Moderate: Mirador del Torre and back

| Field | Value in guide | What I found | Verdict |
|---|---|---|---|
| distance_km | 7.0 | GPX, measured the same way as Full (from the trailhead): 2 × 2.94 = **5.9 km**. The 7 km figure comes from [elchalten.com](https://elchalten.com/v4/en/mirador-del-torre-trek-el-chalten.php) and Calafate Tours, measured "from town". AllTrails from Calle Las Loicas: 6.8 km. Full's 17.3 km is from the trailhead, so 7 km mixes two starting points. The effect is that Moderate looks 40% of Full when it is 34%. | Change to 6 |
| ascent_m | 290 | GPX with a 5 m threshold: out 217 m, plus 15 m of small climbs on the way back = **232 m** (raw 270). The 290 m is AllTrails' figure from a different start, and AllTrails figures are raw. The same method as Full's 533 m gives about 230. Calafate Tours gives 150–180 m. | Change to 230 |
| estimated_hours | 3.5 | elchalten.com: 1.5 h each way, so 3 h. The guide's own day 9 description: "about 3 hours round trip from town". AllTrails: 2–2.5 h walking. | Change to 3 (matches the description) |
| difficulty | Moderate | elchalten.com calls it "low". It has a steady 200 m climb, so Moderate is a fair label for this group. | OK |
| summary: "Most of the full day's climbing is in this first section, so the distance drops more than the effort" | — | GPX: 232 of 538 m (43%) for 34% of the distance. "Most" is not supported. Even with the guide's own figures (290/533) it is only 54%. | Change to: "About two-fifths of the full day's climbing is in this first section." Or drop the sentence. |
| name / summary: Cascada Margarita is passed on the way | — | Patagonia Scout: Cascada Margarita at about 1.5 km, before the viewpoint. | OK |

### Easy: Chorrillo del Salto from the RP23 parking

| Field | Value in guide | What I found | Verdict |
|---|---|---|---|
| distance_km | 4.0 | The OSM parking "Chorrillo del Salto" (way 747061337, -49.2998, -72.9036) is **570 m in a straight line** from the waterfall (node 1237892708).<br>[Connect Patagonia](https://connectpatagonia.com/hikes/chorrillo-del-salto/): 1 km round trip from the parking.<br>[mindtrip](https://mindtrip.ai/attraction/el-chalten-santa-cruz/chorrillo-del-salto/at-dEBkfny2): about 1 km each way.<br>[jtreks](https://jtreks.co/el-chalten/articles/chorrillo-del-salto) is the only source for 4 km from an "RP23 pullout ~4 km north of town". That does not fit the other figures: from town it is 6.6 km return, and the marked parking is about 2.9 km north of the town's north edge. The 4 km looks like a different, earlier pullout, or an error. | Change to 1.5 (parking to waterfall and back, with a margin for path bends) |
| ascent_m | 100 | jtreks: "under 100 m" from town. Connect Patagonia: 50 m from town. From the parking it is less than either. | Change to 30 (estimate), or show as "little climbing" (null) |
| estimated_hours | 1.5 | jtreks: 50 min from its pullout. Connect Patagonia: 1 km return, which is about 20–30 min walking. With time at the waterfall, about 1 h, not counting the 10-minute drive each way. | Change to 1 |
| logistics: "About 10 minutes by van or taxi to the parking" | 10 min | About 3–4 km of paved and gravel road north of town. | OK |
| logistics: "Park entry fee applies" | — | [trekkingelchalten.com](https://trekkingelchalten.com/en/trail-access-fees-in-el-chalten/): Chorrillo del Salto is under the Base Fitz Roy access point. | OK |
| difficulty | Easy | All sources: flat and easy. | OK |

---

## Day 10: Los Cóndores and Las Águilas, then the drive to El Calafate

### Full

| Field | Value in guide | What I found | Verdict |
|---|---|---|---|
| distance_km | 7.4 | GPX 7.39 km, starting and ending in town. | OK |
| ascent_m / descent_m | 236 / 243 | GPX with a 5 m threshold: 238 / 249 (raw 272 / 285). Descent is higher because the track ends 13 m lower than it starts. | OK |
| estimated_hours | 2.5 | Say Hueque: 2–3 h. | OK |
| stats_note.operator: "6.99 km and 183 m" | — | Matches docs/itinerary-v2.md line 94. | OK |
| waypoint "Fitz Roy River bridge / park offices" | km 0 | In the route file km 0 is in town. The OSM Los Cóndores trailhead (node 660024150, next to the Centro de Visitantes) is at **km 1.1**. | Change: km 0 = "El Chaltén (town)"; add "Trailhead at the Visitor Centre" at km 1.1 |
| waypoint "Trail junction" | km 0.8 | The OSM information board for the Cóndores/Águilas split (node 11635958574) is at about km 1.6. | Change to 1.6 |
| waypoint Mirador de los Cóndores | km 1.2 | OSM node 4722282707 is on the track at **km 2.4** (507 m). | Change to 2.4 |
| waypoint Mirador de las Águilas | km 2.3 | OSM node 568391373 is on the track at **km 4.1** (543 m). The track's high point is 583 m at km 3.8. | Change to 4.1 |
| waypoint El Chaltén (end) | km 7.4 | 7.39 | OK |
| description: "climbs for about 40 minutes to Mirador de los Cóndores" | 40 min | 1.3 km and 121 m from the trailhead. About 35–45 min at group pace. | OK |
| description: "About 30 minutes further, Mirador de las Águilas" | 30 min | 1.8 km and about 85 m from Los Cóndores to Las Águilas. 30 min is fast for a group; 35–40 min is more likely. | Unsure (roughly right) |
| description and transport_after_hike: "about 200 km and 3 hours" | 200 km / ~3 h | Road distance El Chaltén–El Calafate is 213–220 km: [PatagoniaHub](https://www.patagoniahub.travel/en/routes/el-calafate-to-el-chalten), [transfercalafate.com](https://transfercalafate.com/how-to-get-from-el-calafate-to-el-chalten.html), [interpatagonia](https://www.interpatagonia.com/elcalafate/road-to-el-chalten.html). The time of about 3 h is right. | Change to 215 km |
| food stop: Parador La Leona "about 110 km from El Calafate (halfway)" | — | La Leona is at the Río La Leona bridge on RN40, about 105–110 km from El Calafate. It is roughly halfway. | OK |

### Easy: Los Cóndores only

| Field | Value in guide | What I found | Verdict |
|---|---|---|---|
| distance_km | 2.6 | GPX from the trailhead (km 1.09) to Mirador de los Cóndores (km 2.36) is 1.27 km, so **2.5 km** return. Kitti Around the World: 2.5 km. AllTrails: 2.6 km. This is trailhead-based, while Full's 7.4 km is town-based. From the same town start it would be 4.7 km return. | OK as a trailhead figure. For consistency with Full, either use 4.7, or say "from the trailhead" in the summary. |
| ascent_m | 215 | GPX trailhead to viewpoint: **121 m** (5 m threshold; raw 132). From the town start: 150 m. [triptins / AllTrails summary](https://triptins.com/mirador-de-los-condores/): 130 m. The research doc cites 215 m only as "another source" with no link. 215 m is almost the whole loop's climb (236 m), which is impossible for the first 40% of it. | Change to 130 |
| estimated_hours | 1 | About 40 min up and 25 min down. | OK |
| summary: "This is the steepest part of the loop" | — | GPX: 121 m in 1.3 km (9%), against about 85 m in 1.8 km on to Las Águilas. | OK |
| difficulty | Easy | Short, but steep with loose gravel. | OK |

---

## Day 11: Perito Moreno boat and walkways

### Full

| Field | Value in guide | What I found | Verdict |
|---|---|---|---|
| distance_km | 3.6 | GPX 3.58 km | OK |
| ascent_m / descent_m | 174 / 291 | GPX with a 5 m threshold: 136 / 243. Raw: 212 / 317. The guide's figures sit between the two, which fits Wikiloc's own summary. Walkway stairs are real ups and downs that a threshold can hide, so a 140–175 m range is fair. | OK (unsure between 140 and 174) |
| estimated_hours | 8 | This is the whole day: 08:00 pick-up, 2 × 80 km drive, 1 h boat. Time on the walkways is about 3 h: the Wikiloc recording ran 3 h 18 min, and [Calafate Tours](https://calafate.tours/en/blog/pasarelas-glaciar-perito-moreno) suggests 3–4 h. Days 9 and 10 count walking time. `index.html` (`hikeTotals`, line 2088) adds `estimated_hours` into the header's "Hiking Time" total, so this day adds 8 h of "hiking" for 3.6 km of boardwalk. | Change to 3 (time on the walkways). Keep "Allow 7 to 8 hours in total" in the description. |
| waypoint "Visitor area" | km 3.6, "Back at the top: restaurant, café, bus" | The recording ends at "The Harbor" by the lakeshore (-50.4617, -73.0259, 186–191 m). That is 104 m below the start and 840 m from it. The track does not return to the top. | Change: "Harbour, lower level (km 3.6). Free shuttle back up to the visitor area." |
| waypoint Central circuit | km 1.5 | The central balconies are about km 0.6–1.3 in the recording. | Unsure (roughly right) |
| waypoint Lower circuit | km 3 | The lower and Costa sections run from about km 2.4 to 3.4. | OK |
| stats_note.processing: "from the upper to the lower walkways" | — | Correct, and it ends at the harbour. | OK |
| description: "80 km drive" | 80 km | [Tolkeyen](https://tolkeyenpatagonia.com/en/the-perito-moreno-glacier-walkways/) and [peritomoreno.com](https://www.peritomoreno.com/getting-there-directions/): 80 km. | OK |
| description: boat "leaves at 10:00 from the Bajo las Sombras port, 7 km before the walkways" | 10:00, 7 km | [elcalafate.tur.ar](https://www.elcalafate.tur.ar/en-glaciar-perito-moreno/safari-nautico-es.htm) and [Hielo & Aventura](https://hieloyaventura.com/en/tour/safarinautico-en/): departures at 10:00, 11:30 and 14:30. Puerto Bajo de las Sombras is at RP11 km 70.9, 7 km from the glacier, 1.5 h from El Calafate. That fits an 08:00 pick-up. | OK |
| description: "one-hour Nautical Safari" | 1 h | Same sources: 1 h. | OK |
| description: south face "60 to 70 m above the water" | 60–70 m | [Wikipedia](https://en.wikipedia.org/wiki/Perito_Moreno_Glacier): average 74 m above the lake. Other sources give 60–74 m. | Change to "about 70 m" (minor) |
| description: "Allow 7 to 8 hours in total" | 7–8 h | 08:00 + 1.5 h drive + 1 h boat + 3 h walkways + lunch + 1.5 h drive is about 8–9 h. | OK (8–9 h is also defensible) |

### Easy: boat, then the upper walkways

| Field | Value in guide | What I found | Verdict |
|---|---|---|---|
| distance_km | 1.2 | Calafate Tours: Accessible about 565 m, Central about 600 m, so about 1.2 km. | OK |
| ascent_m | null (shows "little climbing") | Between the top and the central balcony the recording drops about 40 m. Out and back that is about 60 m of climbing (5 m threshold) if walked. The Accessible circuit has a lift to the first balcony. | OK as null. "About 50 m, lift available" would be more precise. |
| estimated_hours | 8 | Same problem as Full: it is the whole day, while the walking is about 1 h (research doc). It also puts 8 h into the Easy "Hiking Time" total. | Change to 1 |
| Moderate note: skip the lower circuit | — | The lower circuit and the climb back from it are where most of the ascent is (GPX: 93 m of descent in the first 1.2 km, and most of the rest below that). | OK |

---

## Hours: what `estimated_hours` means on each day

| Day / level | Value | What it counts |
|---|---|---|
| 9 Full | 7 | Whole guided outing, including lunch at the lake |
| 9 Moderate | 3.5 | Walking plus stops |
| 9 Easy | 1.5 | Walk only; the drive is not included |
| 10 Full / Easy | 2.5 / 1 | Walking time |
| 11 Full / Easy | 8 / 8 | Whole day, including 3 h of driving and the boat |

A reader sees "3.6 km · 174 m ascent · ~8h" and "1.2 km · little climbing · ~8h", which suggests a very slow walk. The header's "Hiking Time" total also adds these 8 h. The simplest consistent rule is **time on foot, including stops on the trail**. Under that rule day 9 Full stays at 7, and day 11 becomes 3 (Full) and 1 (Easy). The full-day length stays in the description.

---

## Recommended changes

Day 9:

1. `levels.moderate.distance_km`: 7.0 → **6**. `ascent_m`: 290 → **230**. `estimated_hours`: 3.5 → **3**.
2. `levels.moderate.summary`: replace "Most of the full day's climbing is in this first section, so the distance drops more than the effort" with "About two-fifths of the full day's climbing is in this first section."
3. `description`: "Most of the climbing is in the first 2 km" → "The steepest climbing is in the first 3 km, up to the Cerro Torre viewpoint (about 200 m)."
4. `description`: "Mirador Maestri ... about 20 minutes beyond the lake" → "about 2 km (45 minutes) beyond the lake".
5. `waypoints`: Laguna Torre km 9 → **8.6**. Mirador Maestri km 9.5 → **10.5**.
6. `levels.easy.distance_km`: 4.0 → **1.5**. `ascent_m`: 100 → **30** (or null). `estimated_hours`: 1.5 → **1**. Keep `to_confirm: true`; the parking location should be confirmed with Say Hueque.

Day 10:

7. `levels.easy.ascent_m`: 215 → **130**. Keep distance 2.6, or add "from the trailhead" to the summary.
8. `waypoints`:
   - km 0 → "El Chaltén (town)"
   - trailhead and Visitor Centre at **1.1**
   - junction **1.6**
   - Los Cóndores **2.4**
   - Las Águilas **4.1**
9. `description` "about 200 km" → **"about 215 km"**. `transport_after_hike[0].distance_km`: 200 → **215**.

Day 11:

10. `estimated_hours`: 8 → **3**. `levels.easy.estimated_hours`: 8 → **1**. Keep "Allow 7 to 8 hours in total" in the description.
11. Last waypoint: "Visitor area, back at the top" → **"Harbour (lower level)"**, note "Free shuttle back up to the visitor area".
12. `description`: "60 to 70 m" → **"about 70 m"** (optional).

Optional: the research doc's line "almost all of the climbing is in the first 3 km" (day 9) should read "about 40%", and its "another source: 215 m" for Los Cóndores should be removed.

## Summary

The Full figures match the route files: day 9 is 17.3 km and 538 m, day 10 is 7.4 km and 238 m, and day 11 is 3.6 km and 136–212 m depending on smoothing.

Three Easy/Moderate values are wrong:

- **Day 10 Easy** climbing is about 130 m, not 215 m.
- **Day 9 Easy** (Chorrillo del Salto from the parking) is about 1.5 km and 1 h. The OSM parking is 570 m from the waterfall.
- **Day 9 Moderate** mixes a from-town distance with a from-trailhead Full. On the same basis it is 6 km and 230 m.

Day 11's 8 h is the whole day, not walking time. It reads oddly beside 1.2 km, and it inflates the "Hiking Time" total. Use 3 h (Full) and 1 h (Easy).

Some waypoints are misplaced: day 10's viewpoints sit at km 2.4 and 4.1, not 1.2 and 2.3, and day 11 ends at the harbour, not at the top. Day 9's Mirador Maestri is 2 km past the lake, not 20 minutes. The El Chaltén–El Calafate drive is about 215 km, not 200 km.
