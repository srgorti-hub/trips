# Patagonia itinerary — v2 (Say Hueque, Pre Final)

Source for rebuilding `trip-data.json`. Extracted 2026-09-27 from the Say Hueque trip page
(status "Pre Final", last modified 2026-09-21) via its API
(`api-yourtrip.sayhueque.com/api/tpsql/*`) and a headless render of the page.

> Deliberately left out of this file because the repo publishes to GitHub Pages: traveller
> names and per-person prices. Both exist in the API if we decide to use them.

## Trip header

| Field | Value | → `trip-data.json` |
|---|---|---|
| Operator title | "IITB-H8-'88 Amazing trip to Patagonia" | `trip.name` (wording TBD, see plan Q8) |
| Operator | Say Hueque (FIT). Torres del Paine portion run by Hotel Las Torres ("Programa Las Torres Clásico 05D/04N") | new: `general_info` / description |
| Dates | Thu 26 Nov 2026 → Fri 4 Dec 2026 · 9 days · 8 nights | `trip.dates` (was 22–30 Nov) |
| Group | 19 travellers (was 21) | `trip.group_size` |
| Rooms | El Chaltén: 4 Double Std, 4 Double Superior, 1 Double Duplex, 1 Single Std. El Calafate & Las Torres: 9 Double + 1 Single | info only |
| Flights | **None booked / not included** | gap — plan Q1, Q2 |
| Travel specialist | Helena Moretti, Say Hueque · +54 9 11 3282 3270 · helenam@sayhueque.travel | `general_info.emergency_contacts` (confirm Q9) |
| Guest relations | Joaquina Alvarez (no contact details shown) | — |

### Included (verbatim)
- 2 Nights in El Chalten · 2 Nights in El Calafate · 4 Nights in Torres del Paine
- Transfers & Meals mentioned in the itinerary.
- Tours described in the itinerary.
- Bilingual guides (English/Spanish) when mentioned in the itinerary.

### Not included (verbatim)
- Fees & Mandatory Documentation, except when mentioned in the itinerary (sayhueque.com/travel-guide/argentina/#tab-7)
- International or Domestic Flights (quoted separately if requested).
- Travel / Medical Insurance.
- Tips.
- Hotels, transfers, tours and other services not described in the itinerary.

### Hotels

| Nights | Hotel | Location | Check-in → out | Basis | Times |
|---|---|---|---|---|---|
| 2 | Desierto Suites | El Chaltén | 26 Nov → 28 Nov | Breakfast | not given |
| 2 | Glaciares de la Patagonia | El Calafate | 28 Nov → 30 Nov | Breakfast | not given |
| 4 | Hotel Las Torres (Superior rooms) | Torres del Paine, Chile | 30 Nov → 4 Dec | Full board + open bar + park excursions | in 15:00 / out 11:00 |

Hotel URLs are not in the itinerary; they will be found and checked (check L1).

---

## Guide structure: 16 days, 19 Nov – 4 Dec

The guide now opens with the pre-trip for the two organisers (source: `patagonia/pre_patagonia_trip.json`,
which holds booking codes and **must not be committed or published**). The Say Hueque days follow as guide days 8–16.

| Guide day | Date | Where | Key facts |
|---|---|---|---|
| 1 | Thu 19 Nov | Austin → Atlanta → Santiago | DL 2011 AUS 13:50 → ATL 17:03; DL 147 ATL 20:30 → SCL 07:40 (+1). Overnight flight. |
| 2 | Fri 20 Nov | Santiago | Land 07:40. Solace Hotel Santiago (Monseñor Sotero Sanz 115, Providencia · +56 2 2270 8000), check-in 15:00 → ask about early check-in or leaving bags. Easy day: Cerro San Cristóbal, Lastarria / Bellas Artes, La Chascona. |
| 3 | Sat 21 Nov | Santiago | Only full day. Historic centre + Precolombino museum, Mercado Central / La Vega lunch; **or** a Maipo / Casablanca wine day. |
| 4 | Sun 22 Nov | Santiago → Buenos Aires | Check-out 12:00, leave ~09:00. LA 455 SCL 11:28 → AEP 14:40 (⚠ recheck times: Chile summer-time change). Miravida Soho Hotel & Wine Bar (Darregueyra 2050, Palermo Soho · +54 11 4774 6433), check-in 15:00. Palermo evening; San Telmo fair optional. |
| 5 | Mon 23 Nov | Buenos Aires | Recoleta + cemetery, MALBA, tango evening. |
| 6 | Tue 24 Nov | Buenos Aires | Plaza de Mayo, Casa Rosada, Café Tortoni, La Boca / Caminito; parrilla dinner. |
| 7 | Wed 25 Nov | Buenos Aires → El Calafate | Rosedal morning; check-out 11:00. AR 1852 AEP 14:20 → FTE 17:40. Taxi to **Calafate Parque Hotel**. **Sunset kayak on Lago Argentino, likely (moved from 29 Nov; to be confirmed).** |
| 8–16 | 26 Nov – 4 Dec | Patagonia | Say Hueque Days 1–9 below. |
| 16 end | Fri 4 Dec | PNT → Santiago | LA 252 PNT 12:00 → SCL 14:05 (booking says "3h 5m" but the times give 2h 05m; ⚠ check for a stop). Several of the group are on this flight. The guide ends on landing; everyone flies home separately. |

Hotel tips to carry over: pay in USD with a foreign passport to skip Chile's 19% VAT (Solace); non-Argentine card + passport + entry record skips Argentina's 21% VAT (Miravida); the Miravida booking card and matching ID are needed at check-in; Solace asks for arrival details 72 h ahead.
Kept off the site: flight/hotel confirmation codes, seats, prices, names (e.g. "booked in <name>'s name" becomes "booked under the reservation holder's name").

---

## Day by day (Say Hueque; guide days 8–16)

Legend: **Svc** = booked service line · **Meals** B/L/D · ⚠ = gap / to confirm · Δ = change vs current app data.

### Day 1 — Thu 26 Nov · El Calafate → El Chaltén
- **Svc:** Transfer El Calafate hotel → El Chaltén hotel, private, driver only. ~3 h, ~215 km. Time: "at the specified time" ⚠ (booking status still initial/unconfirmed).
- **Stay:** Desierto Suites, El Chaltén (night 1 of 2).
- **Meals:** none listed (breakfast from Day 2).
- **Operator intro text (El Chaltén):** "Hike the trails of El Chaltén, Argentina's trekking capital. With views of Mount Fitz Roy and pristine wilderness… Towering peaks like Fitz Roy and Cerro Torre dominate the skyline…"
- ⚠ Starts from "your hotel in El Calafate": the night of 25 Nov (and the flight into FTE) is **not** part of the booking.
- Δ date 22 Nov → 26 Nov; distance 220 → 215 km; hotel now named.
- JSON: transfer day, 0 km. Needs `transport_to_start` (from/to/duration/distance) and `accommodation.options[{name,url}]`.

### Day 2 — Fri 27 Nov · Laguna Torre (full-day, private guide)
- **Svc:** Full-Day Trekking Laguna Torre, private, English-speaking guide (Walk Patagonia). **Pickup 08:30 at hotel.**
- **Operator stats:** 7–8 h · **19 km** · Moderate · max altitude 719 m. (Δ app: 18 km / 490 m / 7 h.)
- **Not included:** box lunch, National Park entrance fee.
- **Bring:** rucksack, water, snacks, box lunch, warm layer, sunglasses, waterproof jacket, hat, sunscreen, trekking boots.
- **Route (verbatim, abridged):** trail starts in town following the Fitz Roy River → Fitz Roy River canyon & waterfalls (~20 min) → first viewpoint with Cerro Torre, glaciers and the Adela range (shorter option: 3 h back to town from here) → valley to De Agostini base camp → Laguna Torre → lunch → back by the same path.
- **Stay:** Desierto Suites (night 2). **Meals:** B.
- JSON: `food_stops` needs a box-lunch buy-point the evening before (El Chaltén bakery/deli). Needs a GPX (still missing).

### Day 3 — Sat 28 Nov · Cóndores & Águilas viewpoints → transfer to El Calafate
- **Svc 1:** Half-Day Trekking Cóndores & Águilas Viewpoints, private, English-speaking guide (Walk Patagonia). **Starts 09:00**, at hotel or meeting point. Walk back to the hotel on your own.
- **Operator stats:** 2–3 h · **6.99 km** · Easy · altitude 537 m · **gain 183 m**. 1 guide per 15 people. (Δ app: 4.8 km / 220 m / 2.5 h — see conflict C2.)
- **Route (verbatim, abridged):** cross the Fitz Roy River bridge at the town entrance → National Park offices → ~40 min climb to Los Cóndores (condors between the Río de las Vueltas and Río Fitz Roy valleys) → ~30 min to Las Águilas (steppe, Lago Viedma).
- **Svc 2:** Transfer El Chaltén hotel → El Calafate hotel, private, driver only. ~3 h, ~200 km. Time not given ⚠.
- **Stay:** Glaciares de la Patagonia, El Calafate (night 1 of 2). **Meals:** B.
- Δ date 24 → 28 Nov; hotel named.

### Day 4 — Sun 29 Nov · Perito Moreno walkways + Nautical Safari
- **Svc:** Full-Day Perito Moreno Glacier Walkways with Nautical Safari, private, English-speaking guide (Huellas del Sur). **Hotel pickup 08:00; boat 10:00.** Los Glaciares NP entrance **included**; Nautical Safari ticket included.
- **Flow (verbatim, abridged):** 80 km to the park → Bajo las Sombras port (7 km before the walkways) → 1 h boat on Brazo Rico along the south face of the glacier → bus to the walkways → guide briefing at the main balcony → free time on the walkway circuits → back to hotel at the set meeting time.
- **Duration:** 7–8 h (boat 1 h). **Not included:** lunch/box lunch. Boat is weather-dependent.
- **Bring:** warm layers, waterproof jacket & trousers, gloves, wool hat, sunglasses, sunscreen, water, small backpack.
- **Stay:** Glaciares de la Patagonia (night 2). **Meals:** B.
- Δ **Sunset kayak is cancelled** in the booking — remove it from description, waypoints, warnings, gear, what_to_expect. Date 25 → 29 Nov.

### Day 5 — Mon 30 Nov · El Calafate → Hotel Las Torres (border crossing)
- **Svc:** Transfer El Calafate → Hotel Las Torres, private, driver only (booked through Las Torres). ~4 h, ~275 km. Time not given ⚠.
- **Border (verbatim, key points):** bring passport. Every passenger must complete the SAG **digital affidavit** (https://djsimple.sag.gob.cl/) on their phone within **48 h before crossing**. No fresh food, plants or seeds into Chile; declare anything you are unsure of.
- **Las Torres arrival:** staff briefing; depending on arrival time, a half-day activity (lenga forest walk, horse riding, organic garden).
- **Las Torres programme includes (verbatim, abridged):** Superior room, all meals, open bar, bilingual guides on excursions, Torres del Paine NP entrance, Wi-Fi, all park excursions, Wellness Centre discount. **Not included:** premium wines/spirits, transfers outside scheduled times, tips, laundry, **Grey Lake boat (book early, limited)**, insurance.
- **Stay:** Hotel Las Torres (night 1 of 4), check-in 15:00. **Meals:** B (Calafate) + D (Las Torres), open bar.
- Δ date 26 → 30 Nov; duration 5–6 h → ~4 h; distance now 275 km.

### Day 6 — Tue 1 Dec · Base Torres (recommended; chosen on site)
- **Svc:** "Choose an excursion included in the Las Torres program". Recommended: **Trekking to the Base Torres viewpoint**.
- **Route (verbatim, abridged):** from the hotel up the Ascencio Valley → lenga forest → La Morrena (hardest section) → Base Torres viewpoint → snack/photos → back the same way.
- **Operator stats:** 8 h · Difficulty High. (App: 20 km / 900 m / 9 h, Strenuous.)
- **Stay:** Las Torres (2/4). **Meals:** B/L/D.
- Δ date 27 Nov → 1 Dec. Same hike as current Day 6.

### Day 7 — Wed 2 Dec · Full Paine + Grey Lake (recommended; chosen on site)
- **Svc:** Choose an excursion. Recommended: **Full Paine with Grey Lake**.
- **Flow (verbatim, abridged):** road tour with stops at Puente Negro, Nordenskjöld lookout, Sarmiento lookout, Lago Pehoé, Salto Grande waterfall → gourmet lunch → choice of (a) hike along the south shore of Lago Grey to see icebergs, or (b) **Grey Glacier boat (~3 h, external operator, not included, weather-dependent)**.
- **Operator stats:** 7–10 h · Easy.
- **Stay:** Las Torres (3/4). **Meals:** B/L/D.
- Δ **Swapped:** this was Day 8 in the app. Date 29 Nov → 2 Dec.

### Day 8 — Thu 3 Dec · French Valley (recommended; chosen on site)
- **Svc:** Choose an excursion. Recommended: **French Valley**.
- **Flow (verbatim, abridged):** 45 min drive → Pudeto → catamaran Hielos Patagónicos, 30 min across Lago Pehoé → Paine Grande → mostly flat trail (~300 m change) along Lago Skottsberg → Italiano campsite (turn-back option) → steep climb through lenga forest and rock ~2.5 km → viewpoint below Los Cuernos / French Glacier → back to the boat.
- **Operator stats:** 12 h · High · total altitude change 700–800 m. Transfer and Pehoé boat included. (App: 20 km / 702 m / 10 h.)
- **Stay:** Las Torres (4/4). **Meals:** B/L/D.
- Δ **Swapped:** this was Day 7 in the app. Date 28 Nov → 3 Dec. Hours 10 → 12.

### Day 9 — Fri 4 Dec · Las Torres → Puerto Natales Airport (PNT)
- **Svc:** Transfer Las Torres → **Puerto Natales Airport**, private, driver only. ~2 h, ~122 km. Time not given ⚠ (booking: "info incomplete").
- Farewell text mentions a possible half-day excursion depending on departure time. Check-out 11:00.
- **Meals:** B (lunch unclear ⚠).
- Δ destination was "Puerto Natales" (town, with a hotel); now **airport, no hotel**. Date 30 Nov → 4 Dec. ⚠ Onward flight not booked.

---

## Known conflicts between sources (to resolve in check D2)

| # | Day | Operator says | App says | Other |
|---|---|---|---|---|
| C1 | 2 Laguna Torre | 19 km, max alt 719 m | 18 km / 490 m / 7 h | no GPX yet |
| C2 | 3 Cóndores | 6.99 km, +183 m | 4.8 km / 220 m | earlier session cut 7.4 → 4.8 |
| C3 | 6 Base Torres | 8 h | 20 km / 900 m / 9 h; text says "18 km"; training says "850 m" | |
| C4 | 7 Full Paine | 7–10 h, Easy | 9 km / 178 m (old day 8); what_to_expect says "10 km, 300 m" | Grey shore hike optional |
| C5 | 8 French Valley | 12 h, 700–800 m | 20 km / 702 m / 10 h | |
| C6 | 1 / 3 transfers | 215 km / 200 km | 220 km | |

## JSON mapping notes
- Move `accommodation` to whw-chill's `options[{name,url}]` shape (supports the URL, which today's app never shows).
- Use whw-chill's `transport_to_start` for days 1, 3, 5, 9 and `optional_activities` for day 5 (Las Torres half-day options), day 7 (Grey Lake boat), day 9 (half-day excursion).
- Days 6–8 should say plainly that the excursion is picked on site from the Las Torres list. The recommended hike is the default content.
- `participants`: today these are placeholders ("Organizer" / "Participant"). What goes here depends on plan Q9.
