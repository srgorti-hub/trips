# Figures check: logistics and non-hiking numbers

Checked: 28 Sep 2026, against `trip-data.json` on branch `patagonia-levels`. No data or code files were changed.
Scope: every number in the guide except the hike-day distance, ascent and hours figures and the `levels` blocks (another check covers those).
`trip-data-comprehensive.json` was compared field by field for every path outside `levels`, `stats_note`, `elevation_profile`, `waypoints`, `photos` and `youtube`. It matches `trip-data.json` on every number checked here.

Verdicts: **OK** = matches a primary source or two good secondary sources. **Change** = the guide is wrong or internally inconsistent. **Unsure** = could not be confirmed (usually because the 2026-27 schedule is not published or the page is not public).

## Trip totals and dates

| Where | Value in guide | What I found (source) | Verdict |
|---|---|---|---|
| `trip.total_distance_km` | 75.2 | Sum of hike days 9, 10, 11, 13, 14, 15 = 17.3 + 7.4 + 3.6 + 19.1 + 9.0 + 18.8 = 75.2 (computed from the file) | OK |
| `trip.total_ascent_m` | 2782 | 533 + 236 + 174 + 975 + 178 + 686 = 2782 (computed) | OK |
| Dates vs weekdays (all days) | 19 Nov Thu … 4 Dec Fri | Computed: 20 Nov Fri, 21 Sat, 22 Sun, 23 Mon, 24 Tue, 25 Wed, 26 Thu, 27 Fri, 28 Sat, 29 Sun, 30 Mon, 1 Dec Tue, 2 Wed, 3 Thu, 4 Fri. Every weekday named in the text (Galindo "Fri", Bar Nacional "Sat", El Huerto "Sun", San Telmo Sunday fair on day 4, Monday holiday on day 5, MALBA closed "Tuesdays" on day 6, Isabel "days 7, 10 and 11 are Wed, Sat and Sun") agrees | OK |
| Day 5: holiday | Mon 23 Nov, Día de la Soberanía Nacional moved from Fri 20 Nov | Law 27.399: a movable holiday on a Friday moves to the next Monday. See city-check section below for the official 2026 calendar | See below |

## Flights

| Where | Value in guide | What I found (source) | Verdict |
|---|---|---|---|
| Day 4 `flights[0]` LA 455 SCL→AEP, depart | 11:28 | Published schedule: 12:35 → 14:40 (2 h 05) until 28 Mar 2026 while Chile was on UTC-3; 11:37 → 14:40 from 5 Apr 2026 (Chile winter time). Daily, including Sundays. Chile returned to UTC-3 on 6 Sep 2026, so the summer pattern (about 12:35) should apply on 22 Nov. (flightmapper.net LA 455: http://info.flightmapper.net/flight/LATAM_Airlines_LA_455 ; flightaware/flightera list the same route) | Change depart to "12:35 (check LATAM app)". The guide's own note already says this; the field and the day-4 description still say 11:28 |
| Day 4 LA 455 arrive | 14:40 | Same source: 14:40 in both seasons | OK |
| Day 4 description | "Leave the hotel around 09:00" | With a 12:35 departure, 09:00 is early but safe; 09:30 would also work | OK |
| Day 7 AR 1852 AEP→FTE | 14:20 → 17:40, 3 h 20 | AR 1852 exists on AEP→FTE with a 3 h 20 block time on every published date; times vary by day of week (e.g. Mon 14:15→17:35, Thu 15:20→18:40, Sat 16:40→20:00 from Sep 2026). No Wednesday 25 Nov 2026 entry is public. (http://info.flightmapper.net/flight/Aerolineas_Argentinas_AR_1852 ; FlightAware ARG1852) | Duration OK; times unsure. Recheck in the Aerolíneas app; the guide should carry the same "check the app" note it has for LATAM |
| Day 16 LA 252 PNT→SCL, depart | 12:00 | LA 252 flies PNT→SCL (A320, 2,037 km, 3 h 01 to 3 h 07 block). Last published season: 09:40 → 12:47 (Mon/Wed/Fri, some Sundays); a 14:01 departure appeared from March 2026. No Dec 2026 schedule is public. (http://info.flightmapper.net/flight/LATAM_Airlines_LA_252) | Unsure. 12:00 cannot be confirmed; check the LATAM app |
| Day 16 LA 252 arrive | 14:05 (field and description); "expect about 15:05" (flight note) | Block time is about 3 h 05 and PNT and SCL are both UTC-3 in December, so a 12:00 departure lands about 15:05. The description and `general_info.transport.getting_back` still say 14:05, which contradicts the flight note in the same day | Change: arrive "15:05 (check LATAM app)" in the flight field, day 16 description and `general_info.transport.getting_back` |
| Day 16 description | "The booking shows a duration of 3 h 5 m while the times give 2 h 5 m" | The 3 h 05 duration is the correct one (above) | OK as a warning; simplify once the arrival is fixed |
| Day 2 description | Land 07:40 | Individual inbound flights are not in the data; cannot be checked | Unsure (traveller-specific) |

## Road transfers

| Where | Value in guide | What I found (source) | Verdict |
|---|---|---|---|
| Day 7 `transport_after_hike` FTE airport → Calafate Parque Hotel | 20 km, 20-25 min | OSRM road routing: 20.5 km, about 26 min (router.project-osrm.org). Airport is about 20 km east of town | OK |
| Day 8 `transport_to_start` El Calafate → El Chaltén | 215 km, ~3 h | Ruta0: 214 km, about 2 h 40 of driving (https://www.ruta0.com/ruta/argentina/el-calafate-a-el-chalten/); OSRM 213.7 km. Buses and transfers quote about 3 h | OK |
| Day 8 food stop Parador La Leona | "about 110 km from El Calafate (halfway)", "from 1894" | La Leona is widely listed at about 110 km from El Calafate, halfway to El Chaltén (eldiario.es Ruta 40 guide; interpatagonia). 1894 founding is the standard figure | OK |
| Day 10 `transport_after_hike` and description, El Chaltén → El Calafate | 200 km, ~3 h | Same road as day 8: 214 km. The guide gives 215 km one way and 200 km the other | Change to 215 km |
| Day 11 description | 80 km drive to the park / walkways | OSRM El Calafate → walkways car park: 76.7 km; commonly quoted 78-80 km | OK |
| Day 11 description | Bajo las Sombras port "7 km before the walkways" | Operators: "Puerto Bajo las Sombras (7 km from the Glacier Viewpoint)" (elcalafate.tur.ar Safari Náutico page) | OK |
| Day 12 `transport_to_start` El Calafate → Hotel Las Torres | 275 km, "~4 h plus border" | OSRM: 274 km direct, 281 km via Cerro Castillo. Las Torres' own El Calafate shuttle leaves 07:00 and arrives 13:00, about 6 h with a stop at Esperanza and a 15-min stop at Cerro Castillo, and both border posts (Cancha Carrera AR, Cerro Castillo CL, 7 km apart) (https://blog.lastorres.com/connecting-you-to-las-torres-patagonia-from-argentina). Part of the Argentine side and the approach to the border are gravel | Distance OK. Change duration to "~5 h driving, about 6 h door to door with border and stops" |
| Day 12 `transport_to_start.time` vs `.notes` | "Time to be confirmed by Say Hueque" / "Booked through Hotel Las Torres" | Internal inconsistency; the description also says "booked through Hotel Las Torres" | Change: say who confirms the time (Las Torres or Say Hueque, whichever holds the booking) |
| Day 15 description | 45-minute drive Las Torres → Pudeto | OSRM: 30.8 km on park gravel roads, about 50 min | OK (45-50 min) |
| Day 16 `transport_to_start` Las Torres → Puerto Natales airport | 122 km, ~2 h | OSRM: 113 km direct, 119 km via Cerro Castillo; Rome2rio: 117 km, about 2 h 05-2 h 10 | OK (115-120 km would be slightly more accurate) |
| Day 16 `transport_to_start.notes` | Leave around 09:00 for a 12:00 flight | 2 h drive puts you at PNT around 11:00, one hour before departure. Tight but workable for a small airport; if the flight moves earlier (last season it left at 09:40) this breaks | OK, but recheck once the flight time is confirmed |

## Boats and park fees

| Where | Value in guide | What I found (source) | Verdict |
|---|---|---|---|
| Day 11 Nautical Safari | Leaves 10:00 from Bajo las Sombras, about 1 hour, along Brazo Rico by the south face | Departures 10:00, 11:30 and 14:30 (more on demand), 1 hour, Brazo Rico / south wall (https://www.elcalafate.tur.ar/en-glaciar-perito-moreno/safari-nautico-es.htm ; hieloyaventura.com page did not render) | OK |
| Day 11 description | Glacier face "60 to 70 m above the water" | Sources give 60 m (Parques Nacionales-derived figures) to 70-74 m (Wikipedia and others) | OK |
| Day 11 / `general_info.currency` | Perito Moreno park entry included | Fee is ARS 50,000 for foreigners from 1 Jun 2026 in both park zones; Zona Sur takes card, cash (ARS) or online (https://www.argentina.gob.ar/interior/ambiente/parquesnacionales/losglaciares/tarifas). Inclusion is a booking matter, not checked | OK (inclusion per booking) |
| Day 9 warnings | Los Glaciares fee ARS 50,000 per person per day from 1 Jun 2026, buy on ventaweb.apn.gob.ar, El Chaltén checkpoints take no cash | Official tariff page: foreigners ARS 50,000, "Valores vigentes a partir del 1º de junio de 2026, tanto para la Zona Sur como para la Zona Norte"; Zona Norte "solo con tarjeta de crédito o débito; no se acepta efectivo"; Los Cóndores portal tickets "únicamente online" (same URL). A 2-day ticket gives 50% off the second visit within 72 h (https://trekkingelchalten.com/en/trail-access-fees-in-el-chalten/) | OK |
| Day 10 warnings (missing) | No park fee mentioned | The Cóndores / Águilas trail starts at the Portal Los Cóndores checkpoint and needs the same Zona Norte ticket (trekkingelchalten.com, above) | Change: add the fee to day 10, and suggest buying a 2-day ticket on day 9 (ARS 50,000 + 25,000) |
| Day 14 Grey III | CLP 120,000 round trip from 1 Oct 2026; departures 09:30, 13:00, 16:00; about 2 h 45; 30-45 min walk to the jetty; one pisco sour included | Hotel Lago Grey: round trip adults CLP 120,000 (one way 110,000), "valid prices from October 1st, 2026 to April 30th, 2027"; departures 09:30, 13:00, 16:00; "approximately two hours and forty-five minutes"; walk "thirty to forty-five minutes", plus 10 min back to the hotel; "One Courtesy Pisco Sour Per Person" (https://www.lagogrey.com/en/navigation/) | OK |
| Day 15 Pehoé catamaran | About 30 min crossing; return boats from Paine Grande at 17:00 or 18:40 | Operator timetable Nov 2026-Mar 2027: Paine Grande → Pudeto 09:20 (Spanish page: 08:40), 11:20, 17:00, 18:40; Pudeto → Paine Grande 08:30 (Spanish page: 08:00), 10:30, 16:15, 18:00; CLP 28,000 per leg; about 30 min (https://catamaranpehoe.com/precios-y-horarios, timetable read from the page source). The English and Spanish versions of the page disagree on the first morning boat | OK for the return times in the guide |
| `general_info.currency` | Torres del Paine entry included through Las Torres | Matches the Las Torres all-inclusive description on the day 12 accommodation entry; CONAF fee not quoted in the guide, so nothing to check | OK |

## Weather and daylight (`weather`)

| Where | Value in guide | What I found (source) | Verdict |
|---|---|---|---|
| Santiago late Nov | about 27 °C / 10 °C | 1991-2020 November: 27.2 °C max, 9.6 °C min (climate-data / weather-and-climate summaries) | OK |
| Buenos Aires | about 26 °C / 16 °C | Observatorio Central 1991-2020 November: 26.0 / 16.1 °C (https://en.wikipedia.org/wiki/Climate_of_Buenos_Aires) | OK |
| El Calafate November | about 16 °C / 4 °C, a little warmer in December | FTE airport 1991-2020: Nov 15.8 / 4.0 °C, Dec 17.9 / 6.2 °C (https://en.wikipedia.org/wiki/El_Calafate) | OK |
| Torres del Paine | often around 10 °C by day, close to freezing at night; November is its windiest month | Modelled averages: Nov 8 / 2 °C, Dec 10 / 3 °C; windiest month November at about 37 km/h mean, December 36 km/h (weather-and-climate.com and wanderlog summaries; no official CONAF station table found) | OK (secondary sources only) |
| El Calafate sun times, early December | Sunrise about 05:35, sunset about 21:35, about 16 h | Computed with the NOAA solar formula at 50.34 S, 72.27 W, UTC-3: 1 Dec 05:36 / 21:40 (16.1 h); 4 Dec 05:35 / 21:44 | Change sunset to "about 21:40" (minor) |
| Day 7 kayak note | Sunset about 21:30 on 25 Nov | Computed 21:31 | OK |
| `weather.daylight_hours` | 16 | El Calafate 15.8-16.2 h, Torres del Paine 15.9-16.3 h across the Patagonia days | OK |
| `weather.temp_min_c` / `temp_max_c` | 2 / 16 | Consistent with the ranges above for Patagonia | OK |
| `weather.wind_kmh` | 20-80 | Mean about 36 km/h in November with gusts well above; range is reasonable | OK |
| `weather.precipitation_probability` | 0.35 | El Calafate averages only 2 rain days in November; Torres del Paine is wetter. No single source for "35%" | Unsure (a Patagonia-wide guess; harmless) |

## General info

| Where | Value in guide | What I found (source) | Verdict |
|---|---|---|---|
| Time zones | Santiago, Magallanes and Argentina all UTC-3 in late Nov / Dec; no clock changes | Chile summer time runs from 24:00 on Sat 5 Sep 2026 to 24:00 on Sat 3 Apr 2027 (decree reported by BioBioChile, T13, La Tercera); Magallanes stays on UTC-3 all year; Argentina is UTC-3 all year | OK |
| Power and plugs | 220 V both countries; Chile C and L; Argentina I, C also common | Standard reference data (IEC World Plugs) | OK |
| Argentina emergencies | 911; fire 100; SAME 107 | Santa Cruz joined the national 911 system in 2023 with a dispatch centre in El Calafate (noticias.santacruz.gob.ar SAE-911). El Calafate also lists 100 fire, 101 police, 107 hospital (https://www.elcalafate.tur.ar/numeros-de-emergencias.htm) | OK (could add "101 police" as a backup in El Calafate) |
| Chile emergencies | 131 SAMU, 132 fire, 133 Carabineros, 134 PDI, 136 Socorro Andino | Consulado.gob.cl / chile.gob.cl list the same numbers (137 is the maritime authority) | OK |
| Hospital SAMIC El Calafate | +54 2902 491831, Jorge Newbery 453 | Hospital site and elcalafate.tur.ar: Av. Jorge Newbery 453, +54 2902 491831 | OK |
| CONAF Magallanes | +56 61 223 8554, extension 200 | CONAF regional office, Av. Bulnes 0309, Punta Arenas: (56) 61 2238554 **extension 201**, Mon-Fri 09:00-13:00 (conaf.cl Magallanes page) | Change extension to 201 and hours to "weekdays 09:00-13:00" |
| Clínica Santa María | +56 2 2913 0000, Av. Santa María 0500 | clinicasantamaria.cl: Av. Santa María 0500, Providencia, +56 2 2913 0000 | OK |
| Hospital Alemán | +54 11 4827 7000, Av. Pueyrredón 1640 | hospitalaleman.org.ar contact page | OK |
| Hospital Puerto Natales | "Published phone numbers conflict; call 131" | Not checked further; the advice is sound | OK |
| Currency: card rate | Foreign Visa/Mastercard charged at a rate linked to the dólar MEP | Consistent with the 2024 change for foreign cards; no 2026 reversal found | OK |
| Currency: Argentina hotel VAT | 21% exemption when paying with a foreign card and a foreign passport; cash does not qualify | Regime still in force; ARCA Resolución General 5843/2026 (May 2026) digitised validation and still requires a foreign card or a transfer from abroad (Infobae 6 May 2026; argentina.travel) | OK |
| Currency: Chile hotel VAT | 19% exemption for foreign tourists paying in foreign currency with passport and PDI slip | Standard SII rule | OK |
| Visa: Indian passports, Argentina | Resolución 353/2025, Boletín Oficial 27 Aug 2025, in force from 28 Aug 2025, 90 days with a valid US visa | Boletín Oficial and argentina.gob.ar: signed 26 Aug, published 27 Aug 2025; Indian ordinary passports with a valid US visa, tourist stays up to 90 days | OK |
| Visa: Indian passports, Chile | US visa valid 6+ months on arrival; so valid to early June 2027 | Last Chile entry is 30 Nov 2026, so the visa must run to at least 30 May 2027; "early June 2027" is a safe margin | OK |
| Preparation: "Send Solace Hotel your arrival details by 17 Nov" | 72 h before a 20 Nov 07:40 arrival | 17 Nov 07:40 | OK |
| Say Hueque contact, hotel phone numbers (Solace, Miravida, Calafate Parque, Desierto Suites, Glaciares de la Patagonia, Las Torres), taxi numbers | as listed | Format is valid for each country (Argentine mobiles carry +54 9; landlines area code 2902 El Calafate, 2962 El Chaltén, 11 Buenos Aires; Chile +56 2 Santiago, +56 61 Magallanes, +56 9 mobiles). Numbers not dialled; Solace, Miravida, SAMIC, CONAF, Clínica Santa María and Hospital Alemán confirmed against listings | Format OK; numbers not verified |
| Las Torres phone | "+56 22 898 6043" | Format is unusual: Santiago landlines are written +56 2 2xxx xxxx; "+56 22 898 6043" is the same digits grouped oddly (+56 2 2898 6043) | Change formatting to +56 2 2898 6043 |

## City days (Santiago and Buenos Aires)

Checked by a helper search on 28 Sep 2026 (official sites first). Hours are for the weekday the guide names.

| Where | Value in guide | What I found (source) | Verdict |
|---|---|---|---|
| Day 5 description | Mon 23 Nov holiday (Soberanía Nacional moved from Fri 20 Nov) | Infobae, La Nación and feriadosargentina.com.ar list Mon 23 Nov 2026 under Ley 27.399; the argentina.gob.ar page did not render the date | OK |
| Day 2 funicular | Tue-Sun 10:00-19:45 | Summer hours on funicularsantiago.cl: Tue-Sun 10:00-19:45; Mondays 13:00-19:45 (first Monday of the month closed) | OK |
| Day 2 MNBA | Free, Tue-Sun 10:00-18:30 | mnba.gob.cl: same, last entry 18:20 | OK |
| Day 2 La Chascona | Tue-Sun 10:00-18:00, no booking, English audio guide | fundacionneruda.org: same (Mar-Dec); ticket CLP 11,000 | OK |
| Day 2 La Moneda | Free weekday visits, about 50 min, register ahead | visitaspatrimonio.presidencia.cl: same. Secondary source: register at least a week ahead; the Friday tourist slot is 15:00 only | OK; add "register a week ahead, Friday slot 15:00" |
| Day 3 Precolombino | Tue-Sun 10:00-18:00, Bandera 361 | museo.precolombino.cl: same (closed on public holidays; 21 Nov is not one) | OK |
| Day 3 Mercado Central | Sat until about 19:00; 1872 | santiagoturismo.cl: Sat 07:30-19:00, opened 1872; other listings say 17:00 or 18:00 | 1872 OK; hours unsure. Say "stalls close 17:00-19:00" |
| Days 2-3 Solace Hotel | Sotero Sanz 115, +56 2 2270 8000, 15:00 / 12:00 | Booking.com / SERNATUR listing: same | OK |
| Day 2 Emporio La Rosa | Daily 10:00-19:30 | emporiolarosa.cl: daily 09:30-20:30 | Change to 09:30-20:30 |
| Day 2 Peumayén | Fri 13:30-23:30, closed Sun | Booknbook and other listings: Fri 13:30-21:00, Sat to 21:30, closed Sun and Mon (official site empty) | Change to Fri 13:30-21:00 |
| Day 2 Galindo, Holy Moly, Bocanáriz, El Huerto | as listed | Official pages / OpenTable match | OK |
| Day 3 Bar Nacional, El Naturista (since 1927), Chipe Libre | as listed | Official pages / listings match | OK |
| Day 3 Fuente Alemana | Sat 10:30-21:45, closed Sun | Alameda branch has no official page; listings give Sat to 22:30, Sun closed | Unsure (guide is on the safe side) |
| Day 3 La Piojera | Mon-Sat 12:00-20:30 | santiagoturismo.cl and La Piojera's FAQ: Mon-Sat 12:00-00:00 | Change to 12:00-00:00 |
| Day 5 MALBA | Wed 11-20, Thu-Mon 12-20, closed Tue | malba.org.ar: same; open 12-20 on holidays | OK |
| Day 5 Casa Rosada visits | Free on weekends and holidays, book up to 15 days ahead, passport | Matches (secondary sources; booking site refused the connection) | OK |
| Day 5 warnings | "Museo Casa Rosada closed on Mondays" | argentina.gob.ar: museum open Wed-Sun 11-18, closed Mon **and Tue**, so it is shut on both day 5 and day 6 | Change to "closed Mondays and Tuesdays" |
| Day 5 Recoleta Cemetery | Fee for foreigners, card only, about 09:00-17:00 | buenosaires.gob.ar: daily 9-17; secondary: ARS 24,030 (Jul-Aug 2026), card only | OK |
| Day 5 / day 7 Rosedal | Tue-Sun 10:00-18:00, closed Mon | buenosaires.gob.ar: same, last entry 17:00, no holiday exception stated | OK (closed on Mon 23 Nov) |
| Day 6 Café Tortoni | Daily 08:00-21:00, Av. de Mayo 825 | cafetortoni.com.ar: same | OK |
| Day 4 San Telmo fair | Sun 10:00-17:00 | feriadesantelmo.com: same | OK |
| Days 4-6 Miravida Soho | Darregueyra 2050, +54 11 4774-6433, 15:00 / 11:00 | Yelp / Expedia: same | OK |
| Day 4 Parrilla Don Julio | Daily 19:00-01:00 | parrilladonjulio.com: also lunch 11:30-16:00 daily | Change: add lunch 11:30-16:00 |
| Day 7 Ninina (Gorriti) | Mon-Fri 08:00-21:00 | Yelp (Jun 2026): Mon-Thu 08:00-23:00, Fri to 00:00; no official hours | Change to "from 08:00" (closing time unsure) |
| Days 5-7 La Biela, Coronado, Chuí, La Cabrera, El Cuartito (1934), La Brigada (1992), Cuervo Café | as listed | Official pages / listings match | OK |
| Day 7 warning | Aeroparque about 20 min from Palermo | 6-8 km, 10-25 min by traffic (rome2rio) | OK |

Not checked: El Calafate and El Chaltén restaurant hours and phone numbers, Hotel Las Torres breakfast hours, and the Say Hueque contact details.

## Recommended changes

1. **Day 10 park fee missing.** Add to day 10 warnings: "Los Glaciares fee applies again today (Portal Los Cóndores, card or online only). Buy a 2-day ticket on day 9: the second day is 50% off." Source: argentina.gob.ar Los Glaciares tarifas; trekkingelchalten.com.
2. **Day 16 arrival time.** Set LA 252 `arrive` to "15:05", and change "landing at 14:05" in the day 16 description and "(14:05)" in `general_info.transport.getting_back` to 15:05. Keep "check the LATAM app": the Dec 2026 departure time is not public, and last season the flight left at 09:40.
3. **Day 4 LA 455 departure.** Set `depart` to "12:35" (and the day 4 description) with "check the LATAM app"; arrival 14:40 is unchanged.
4. **Day 12 transfer duration.** Change "~4 h plus border" to "~5 h driving; about 6 h door to door with both border posts and stops" (Las Torres' own shuttle takes 07:00-13:00). Also say who confirms the time: the `time` field says Say Hueque, the notes say Las Torres.
5. **Day 10 transfer distance.** Change 200 km to 215 km, in `transport_after_hike` and in the description, to match day 8.
6. **Day 7 AR 1852 times.** Add "Recheck the time in the Aerolíneas Argentinas app". The flight number and 3 h 20 block time are right, but times vary by weekday and the Wednesday 25 Nov schedule is not public.
7. **Museo Casa Rosada.** Day 5 warning: "closed on Mondays and Tuesdays".
8. **City hours.** Emporio La Rosa 09:30-20:30; La Piojera to 00:00; Peumayén Fri to 21:00 (closed Sun and Mon); Don Julio also lunch 11:30-16:00; Ninina Gorriti "from 08:00"; Mercado Central "stalls close 17:00-19:00 on Saturdays"; La Moneda "register a week ahead; Friday slot 15:00".
9. **CONAF Magallanes.** Extension 201 (not 200); office hours weekdays 09:00-13:00.
10. **Las Torres phone format.** Write +56 2 2898 6043.
11. **Weather.** El Calafate sunset in early December "about 21:40".
12. Optional: Day 16 distance 122 km could read "about 115-120 km"; the 2 h is right.

## Summary

Most logistics figures hold up. The trip totals (75.2 km, 2,782 m), all dates and weekdays, the Grey III fare and timetable, the Pehoé return boats (17:00, 18:40), the Los Glaciares fee (ARS 50,000 from 1 June 2026, no cash in El Chaltén), time zones (all UTC-3), emergency numbers, plugs and climate figures all match sources. The comprehensive backup agrees on every number checked. The main fixes: day 10 needs the park fee, since the Cóndores trail uses a paid checkpoint. Day 16 gives two arrival times (14:05 and 15:05); about 15:05 fits the 3 h flight. LA 455 probably leaves at about 12:35, not 11:28. The day 12 border transfer takes about 6 h door to door, not 4 h plus border. Day 10 says 200 km where day 8 says 215 km. The 25 Nov and 4 Dec flight times can't be checked until the airlines publish them. Several city opening hours need small changes.
