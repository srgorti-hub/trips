# YouTube link review (language check)

Checked 2026-09-28. Titles and channels come from YouTube oEmbed. Language, length, views, publish date, embeddability and caption tracks come from each watch page.

## Direct links

| Day | Place | Old video (title, channel) | Language | Action |
|---|---|---|---|---|
| Overview | Whole trip | [hZ2nbVpkoyk](https://www.youtube.com/watch?v=hZ2nbVpkoyk): "The BEST Day Trips & Hikes in Torres Del Paine", Matt and Danielle, 2026, 23 min | English | Kept |
| 9 | Laguna Torre | [pk0Iy_fxgww](https://www.youtube.com/watch?v=pk0Iy_fxgww): "Laguna Torre Hike ... El Chaltén to Cerro Torre", Travels by Vedrana Sucic, 2025, 4 min | English | Kept |
| 10 | Los Cóndores & Las Águilas viewpoints | [sd8vYf-DBeo](https://www.youtube.com/watch?v=sd8vYf-DBeo): "Mirador de los Cóndores y las Águilas, El Chaltén, Argentina", Jose Pablo Informa, 2024, 5 min, 165 views | **Spanish** (Spanish description, Spanish caption track only) | **Replaced** |
| 11 | Perito Moreno boat + walkways | [w9Hy1kZF0NY](https://www.youtube.com/watch?v=w9Hy1kZF0NY): "Perito Moreno Glacier Argentina: Boat Tour, Boardwalks & Travel Guide", Adventures of Lauren & Jason, 2024, 11 min | English | Kept |
| 13 | Base Torres | [6TpUnSmBGnM](https://www.youtube.com/watch?v=6TpUnSmBGnM): "Mirador Base Las Torres // BEST Hike in Torres del Paine?", Adventures of Lauren & Jason, 2024, 10 min | English | Kept |
| 14 | Paine road tour + Lago Grey | [GGXoLOlxKkQ](https://www.youtube.com/watch?v=GGXoLOlxKkQ): "Torres del Paine National Park! Grey Lake, Lake Pehoé, Milodon Cave, Mirador Cuernos // Vlog 4", Elizabeth Clem, 2024, 21 min | English | Kept |
| 15 | French Valley | [x4ZTW-3bPKU](https://www.youtube.com/watch?v=x4ZTW-3bPKU): "Mirador Britanico Hike in Torres Del Paine Patagonia - Chile 4K", Swanson Digital, 2022, 7 min | English (description; mostly footage with no captions) | Kept |

### Replacement, day 10

New: [EH1WcC0fjAc](https://www.youtube.com/watch?v=EH1WcC0fjAc), "Easy Hikes in El Chalten | Condor Lookout (Fitz Roy view) & Chorillo del Salto | Patagonia Argentina", Adventure with Sunny. Published 2025-06-20, 12 min 15 s, about 4,500 views. It can be embedded, is narrated in English, and has English captions.

Why this one: it is the only recent English video I found that covers the Cóndores viewpoint. The other results were Spanish ([AbO1a532XeE](https://www.youtube.com/watch?v=AbO1a532XeE), [nRCQejc0VzA](https://www.youtube.com/watch?v=nRCQejc0VzA), [iUuZd_WrfIY](https://www.youtube.com/watch?v=iUuZd_WrfIY)), Spanish with an English line in the title ([NdiuOrgHOTg](https://www.youtube.com/watch?v=NdiuOrgHOTg), 2013), or a walk-through with no narration ([xTMeLpVkfP0](https://www.youtube.com/watch?v=xTMeLpVkfP0), Wingspreader, 2022, 21 min, no captions). Wingspreader is the backup if you want footage of the full walk up.

Limitation: the new video covers Cóndores and the Chorrillo del Salto waterfall. It does not show the extra 15 minutes out to Las Águilas. I found no English video that covers Las Águilas.

### Edit made

Only `days[10].youtube` in `patagonia/trip-data.json` changed (1 line). The file has CRLF line endings, so a `json.dump` rewrite would have changed every line. I replaced the ID as an exact byte string instead and then confirmed the file still parses. `git diff --stat` shows 1 file, 1 insertion, 1 deletion.

The old ID `sd8vYf-DBeo` still appears in `patagonia/trip-data-comprehensive.json:1805` (the full backup). I left it alone. No descriptions or link text mention the old video.

Validator (`python tools/validate_trip.py patagonia`): 0 fail, 54 warn. All 54 warnings are missing photo or map files for days 1–16 and have nothing to do with this change.

## Search-query days (not changed, suggestions only)

The app sends these queries to YouTube search, and the results depend on YouTube's ranking and the viewer's locale. Queries about Santiago and Buenos Aires return mostly English results for an English-locale viewer. The Patagonia transfer and town queries are more likely to bring up Spanish or Portuguese vlogs. Views are approximate as of the check date.

| Day | Current query | Likely results | Suggested direct link |
|---|---|---|---|
| 1 | Santiago Chile travel guide | Mostly English | None needed |
| 2 | Cerro San Cristóbal funicular Santiago | Mostly Portuguese and Spanish | No strong English video found (best: [WB32mGcpR4o](https://www.youtube.com/watch?v=WB32mGcpR4o), 17 views, no narration). Consider changing the query to "Cerro San Cristobal Santiago Chile travel guide". |
| 3 | Santiago Chile historic centre walking tour | Mixed, mostly English | None needed |
| 4 | Palermo Soho Buenos Aires | Mixed | None needed |
| 5 | Recoleta Cemetery Buenos Aires | Mostly English | None needed |
| 6 | Plaza de Mayo Casa Rosada Buenos Aires | Mixed; Spanish news clips possible | Optional: add "tour" to the query |
| 7 | El Calafate Lago Argentino | Likely Spanish | [ky8K3BK2mow](https://www.youtube.com/watch?v=ky8K3BK2mow): "EL CALAFATE TRAVEL GUIDE", Samuel and Audrey, 2026, 27 min, ~34k views, English captions. Alternative: [8R6oFevjHHg](https://www.youtube.com/watch?v=8R6oFevjHHg), Before You Go, 2022, 10 min, ~54k views. |
| 8 | El Calafate to El Chaltén Ruta 40 drive | Mixed Spanish and Portuguese | Weak English options: [DDGjQJQvz9o](https://www.youtube.com/watch?v=DDGjQJQvz9o) (Bez Tropiku, 2019, 2 min, footage only) and [ElO7QWZlcQo](https://www.youtube.com/watch?v=ElO7QWZlcQo) (2025, 5 min, 148 views). Keeping the search query is reasonable. |
| 12 | El Calafate to Torres del Paine border crossing | Mixed | [HxSZPLc3Xqg](https://www.youtube.com/watch?v=HxSZPLc3Xqg): "Patagonia Bus Travel Guide: Chile - Argentina Border Crossing", Adventure with Sunny, 2025, 14 min, ~14k views, English captions. Alternative: [NiyWiYs47jo](https://www.youtube.com/watch?v=NiyWiYs47jo), Samuel and Audrey, 2021, 13 min, ~23k views. |
| 16 | Torres del Paine to Puerto Natales drive | Mixed | [-UmXu6gbTOc](https://www.youtube.com/watch?v=-UmXu6gbTOc): "Driving from Puerto Natales to Torres Del Paine National Park", Travel with Suri, 2024, 5 min, ~3.5k views, English captions (the drive in the opposite direction). |

All suggested videos were checked on their watch pages. Each was public and embeddable on the check date.
