# Test Cases — Travel Guide Generator

## TC-1: trip-data.json Validation

### TC-1.1: Schema Compliance
- **Input**: Generated `trip-data.json`
- **Expected**: Valid JSON, parses without error
- **Verify**: All required fields present, correct types, no null required fields

### TC-1.2: Day Count
- **Input**: `trip-data.json` with 8 days
- **Expected**: `days` array has exactly 8 entries, `day` fields are 1–8 sequential

### TC-1.3: Date Range
- **Input**: Trip dates May 10–17, 2025
- **Expected**: Each day's `date` falls within range, day 1 = start date, day 8 = end date

### TC-1.4: Difficulty Values
- **Input**: Each day's `difficulty` field
- **Expected**: One of `Easy`, `Moderate`, `Strenuous` — no other values

### TC-1.5: File Path References
- **Input**: All photo, map, elevation_profile, gpx_download paths in JSON
- **Expected**: Paths follow convention (`photos/day-N/`, `elevation/day-N-profile.json`, etc.)

### TC-1.6: Weather Data
- **Input**: `weather` block
- **Expected**: `precipitation_probability` between 0.0–1.0, `temp_min_c` < `temp_max_c`

### TC-1.7: Gear Checklist
- **Input**: `gear_checklist` array
- **Expected**: ≥ 15 items, each has `category`, `item`, `essential` (boolean), multiple categories represented

### TC-1.8: Location Keywords
- **Input**: `trip.location_keywords` and each `days[].location_keywords`
- **Expected**: Trip-level has ≥ 1 keyword. Each day has ≥ 1 keyword. Keywords are descriptive location terms suitable for photo search.

---

## TC-2: Elevation Profile Data

### TC-2.1: File Existence
- **Input**: Check `elevation/` directory
- **Expected**: 8 files: `day-1-profile.json` through `day-8-profile.json`

### TC-2.2: Schema Compliance
- **Input**: Each elevation JSON
- **Expected**: Has `points` array with `{km, elevation_m}` objects. Optional `summit_label` and `summit_km`.

### TC-2.3: Point Ordering
- **Input**: `points` array in each file
- **Expected**: Sorted by `km` ascending, first point km ≈ 0

### TC-2.4: Distance Match
- **Input**: Last point's `km` vs corresponding day's `distance_km`
- **Expected**: Last point's km approximately matches day distance (±1 km)

### TC-2.5: Realistic Elevation
- **Input**: Elevation values across all days
- **Expected**: Values between 0–1200m (WHW range), no negative elevations, summit matches known WHW peaks

---

## TC-3: Travel Guide App — Loading

### TC-3.1: Initial Load
- **Input**: Open `index.html` via local HTTP server
- **Expected**: Page loads without console errors, hero section visible, all tabs present

### TC-3.2: Data Fetch
- **Input**: `trip-data.json` present in root
- **Expected**: Trip name, dates, stats render correctly in hero section

### TC-3.3: Missing Data Graceful Handling
- **Input**: Remove `trip-data.json`, load page
- **Expected**: Meaningful error message displayed, no white screen or unhandled exception

### TC-3.4: Missing Elevation File
- **Input**: Remove one `elevation/day-N-profile.json`
- **Expected**: That day's Deep Dive shows placeholder or "No elevation data" — other days unaffected

---

## TC-4: Travel Guide App — Hero Section

### TC-4.1: Trip Metadata Display
- **Expected**: Trip name, destination, date range, group size all visible and correct

### TC-4.2: Stats Bar
- **Expected**: Total distance, total ascent, number of days displayed with correct values

### TC-4.3: Trip Summary
- **Expected**: Description paragraph renders, is readable

### TC-4.4: YouTube Link
- **Expected**: If `youtube_overview` present, link/button is visible and clickable

---

## TC-5: Travel Guide App — Tab Navigation

### TC-5.1: Default Tab
- **Expected**: Overview tab active on page load

### TC-5.2: Tab Switching
- **Input**: Click each tab (Overview, Day by Day, Weather, Gear)
- **Expected**: Correct panel shown, other panels hidden, active tab visually highlighted

### TC-5.3: No Page Reload
- **Input**: Switch between all tabs
- **Expected**: No full page reload, instant switching

---

## TC-6: Travel Guide App — Overview Tab

### TC-6.1: Stats Card
- **Expected**: Shows trip totals matching `trip-data.json`

### TC-6.2: Accommodation List
- **Expected**: Lists all 8 days with day number, segment label, accommodation name and location

---

## TC-7: Travel Guide App — Day by Day Tab

### TC-7.1: Day Card Count
- **Expected**: 8 day cards rendered

### TC-7.2: Day Card Content
- **Input**: Each day card
- **Expected**: Day number, date, segment label, difficulty badge, distance, ascent, estimated hours, description, terrain tags all present

### TC-7.3: Difficulty Color Coding
- **Expected**: Easy days get green badge, Moderate/Strenuous get amber badge

### TC-7.4: Deep Dive Expand/Collapse
- **Input**: Click Deep Dive toggle on a day card
- **Expected**: Section expands smoothly, shows elevation chart and detail sections. Click again to collapse.

### TC-7.5: Elevation Chart Renders
- **Input**: Expand Deep Dive on each day
- **Expected**: SVG elevation chart visible with correct shape, axis labels, summit marker

### TC-7.6: Elevation Chart Interaction
- **Input**: Hover/tap on elevation chart
- **Expected**: Shows elevation and distance readout at cursor position

### TC-7.7: Waypoints Display
- **Input**: Day with waypoints in data
- **Expected**: Waypoints listed with km markers and notes

### TC-7.8: External Links
- **Input**: Day with AllTrails/Komoot/Walk Highlands links
- **Expected**: Links render as clickable buttons/links, open in new tab

### TC-7.9: GPX Download
- **Input**: Day with `links.gpx_download` path
- **Expected**: Download button/link visible. If GPX file exists, download works. If not, link hidden gracefully.

### TC-7.10: Map Image
- **Input**: Day with `map` path
- **Expected**: Map image renders in Deep Dive if file exists. If not, section hidden gracefully.

### TC-7.11: Warnings Display
- **Input**: Day with warnings in data
- **Expected**: Warnings section visible, styled prominently (icon + highlight)

---

## TC-8: Travel Guide App — Photos

### TC-8.1: Local Photos Present
- **Input**: Place actual image files in `photos/day-1/`
- **Expected**: Local photos displayed in photo strip and lightbox

### TC-8.2: No Local Photos — Stock Fallback
- **Input**: Empty `photos/` folder, valid `location_keywords` in data
- **Expected**: Stock photos fetched from Unsplash, displayed in photo strip

### TC-8.3: No Local Photos, No Internet
- **Input**: Empty `photos/`, disconnect from internet
- **Expected**: Photos hidden gracefully — no broken image icons, no layout breakage, all other content works

### TC-8.4: Mixed — Some Days Have Local, Some Don't
- **Input**: Local photos for days 1–3, no local photos for days 4–8
- **Expected**: Days 1–3 show local photos, days 4–8 show stock photos (or hidden if offline)

### TC-8.5: Hero Image Fallback
- **Input**: No file in `photos/hero/`
- **Expected**: Stock photo based on `trip.location_keywords`, or gradient/color background if offline

### TC-8.6: Stock Photo Aspect Ratios
- **Input**: Stock photos with varying aspect ratios
- **Expected**: Photos cropped/contained appropriately, no layout distortion

---

## TC-9: Travel Guide App — Weather Tab

### TC-9.1: Temperature Card
- **Expected**: Shows min/max temperatures from data, visual bar accurate

### TC-9.2: Precipitation Card
- **Expected**: Shows probability as percentage

### TC-9.3: Daylight Hours
- **Expected**: Correct hours displayed

### TC-9.4: Alerts
- **Expected**: Alert items styled prominently, all alerts from data rendered

---

## TC-10: Travel Guide App — Gear Tab

### TC-10.1: Checklist Renders
- **Expected**: All gear items from `trip-data.json` rendered, grouped by category

### TC-10.2: Essential Star
- **Expected**: Items with `essential: true` have star/indicator

### TC-10.3: Checkbox Interaction
- **Input**: Check 3 items, reload page
- **Expected**: Same 3 items still checked (localStorage persistence)

### TC-10.4: Progress Counter
- **Input**: Check 5 of 25 items
- **Expected**: Counter shows "5 of 25 items checked"

### TC-10.5: Clear All
- **Input**: Check several items, then click Clear All
- **Expected**: All checkboxes unchecked, counter resets, localStorage cleared

---

## TC-11: Travel Guide App — Photo Lightbox

### TC-11.1: Open Lightbox
- **Input**: Click a photo in a day card
- **Expected**: Full-screen overlay opens with photo displayed large

### TC-11.2: Close Lightbox
- **Input**: Press Escape / click X / click backdrop
- **Expected**: Lightbox closes, returns to normal view

### TC-11.3: Navigate Photos
- **Input**: Day has multiple photos, open lightbox, click next/prev
- **Expected**: Navigates between photos within that day

---

## TC-12: Travel Guide App — Dark Mode

### TC-12.1: Toggle
- **Input**: Click dark mode toggle
- **Expected**: Background, text, card colors invert to dark palette

### TC-12.2: Persistence
- **Input**: Enable dark mode, reload page
- **Expected**: Dark mode still active (localStorage)

### TC-12.3: Chart Readability
- **Input**: View elevation chart in dark mode
- **Expected**: Chart colors, labels, gridlines readable against dark background

### TC-12.4: Stock Photos in Dark Mode
- **Input**: View stock photos in dark mode
- **Expected**: Photos display correctly, no jarring contrast issues with surrounding dark UI

---

## TC-13: Travel Guide App — Responsive

### TC-13.1: Mobile (< 768px)
- **Expected**: Single-column layout, readable text, tap-friendly targets (≥ 44px), tabs accessible

### TC-13.2: Tablet (768–1024px)
- **Expected**: Appropriate layout, no horizontal overflow

### TC-13.3: Desktop (> 1024px)
- **Expected**: Full layout, cards at optimal width, generous whitespace, no wasted space

---

## TC-14: Photo Manager (`photos.html`)

### TC-14.1: Initial Load
- **Input**: Open `photos.html` via local HTTP server (with `trip-data.json` present)
- **Expected**: Page loads, shows hero slot + 8 day slots with correct segment labels

### TC-14.2: Missing trip-data.json
- **Input**: Open `photos.html` without `trip-data.json`
- **Expected**: Error message: "trip-data.json not found" — not a blank/broken page

### TC-14.3: Drag and Drop
- **Input**: Drag an image file onto Day 1 slot
- **Expected**: Image accepted, thumbnail preview shown in the slot

### TC-14.4: File Picker Fallback
- **Input**: Click on a day slot (instead of drag)
- **Expected**: File picker opens, selected image appears as thumbnail

### TC-14.5: Multiple Photos Per Day
- **Input**: Drop 3 images into Day 2 slot
- **Expected**: All 3 thumbnails shown, up to max allowed

### TC-14.6: Remove Photo
- **Input**: Click X on a thumbnail
- **Expected**: Photo removed from slot

### TC-14.7: Non-Image Rejection
- **Input**: Drag a `.txt` file onto a slot
- **Expected**: File rejected, not added

### TC-14.8: Zip Download
- **Input**: Assign photos to hero + 3 days, click Download
- **Expected**: Zip file downloads with correct folder structure (`photos/hero/`, `photos/day-1/`, etc.)

### TC-14.9: Zip Folder Structure
- **Input**: Unzip downloaded file
- **Expected**: Folders match expected convention, files renamed to `img1.jpg`, `img2.jpg`, etc.

### TC-14.10: Empty Download Blocked
- **Input**: No photos assigned, click Download
- **Expected**: Download disabled or warning shown

---

## TC-15: GPX Data Processor (`gpx-tool.html`)

### TC-15.1: Initial Load
- **Input**: Open `gpx-tool.html` via local HTTP server (with `trip-data.json` present)
- **Expected**: Page loads, shows day cards with correct segment labels and estimated stats

### TC-15.2: Missing trip-data.json
- **Input**: Open `gpx-tool.html` without `trip-data.json`
- **Expected**: Error message displayed — not a blank/broken page

### TC-15.3: GPX File Drop
- **Input**: Drop a valid GPX file onto Day 1 slot
- **Expected**: File parsed, comparison table shown with estimated vs. GPX stats, mini elevation chart rendered

### TC-15.4: Non-GPX File Rejection
- **Input**: Drop a `.txt` file onto a day slot
- **Expected**: Alert shown, file not processed

### TC-15.5: GPX Without Elevation Data
- **Input**: Drop a GPX file that has no `<ele>` elements
- **Expected**: Alert: "GPX file does not contain elevation data"

### TC-15.6: GPX With Few Points
- **Input**: Drop a GPX file with fewer than 2 track points
- **Expected**: Alert: "GPX file contains fewer than 2 track points"

### TC-15.7: Comparison Table Accuracy
- **Input**: Drop GPX for a day with known distance
- **Expected**: GPX distance matches known value. Diff percentage calculated correctly. >10% differences highlighted amber.

### TC-15.8: Mini Elevation Chart
- **Input**: Drop GPX for a day with elevation data
- **Expected**: SVG chart renders with correct elevation shape, axis labels, summit marker

### TC-15.9: Clear & Re-Drop
- **Input**: Process a GPX file, then click "Clear & re-drop"
- **Expected**: Results cleared, drop zone reappears, day can be re-processed

### TC-15.10: Download Updated trip-data.json
- **Input**: Process GPX for 3 days, click "Download trip-data.json"
- **Expected**: Downloaded JSON has GPX-derived stats for processed days, original estimates for unprocessed days, updated totals

### TC-15.11: Download Elevation Data Zip
- **Input**: Process GPX for 3 days, click "Download Elevation Data"
- **Expected**: Zip contains `elevation/day-N-profile.json` for each processed day with correct schema

### TC-15.12: Results Summary Table
- **Input**: Process GPX for multiple days
- **Expected**: Summary table appears showing all days with estimated vs. GPX values side by side

### TC-15.13: Multi-Trip Availability
- **Input**: Open `gpx-tool.html` from `patagonia/` folder (with patagonia `trip-data.json`)
- **Expected**: Loads patagonia trip data, shows correct day cards for Patagonia trip

### TC-15.14: Footer Link Navigation
- **Input**: Click "GPX Data Processor" link in trip `index.html` footer
- **Expected**: Navigates to `gpx-tool.html`, which loads correctly

---

## TC-16: Trip Template (`trip-template.md`)

### TC-16.1: Claude.ai End-to-End
- **Input**: Upload `trip-template.md` + a rough text itinerary (e.g., "5-day Camino de Santiago from Sarria") to Claude.ai
- **Expected**: Claude generates valid `trip-data.json` with all required fields and elevation JSONs

### TC-16.2: Spreadsheet Input
- **Input**: Upload `trip-template.md` + an xlsx with day/distance/accommodation columns
- **Expected**: Claude uses spreadsheet data and fills in remaining fields via research

### TC-16.3: Output Schema Compliance
- **Input**: JSON output from Claude.ai
- **Expected**: Passes all TC-1 validation checks (schema, types, required fields, location_keywords)

### TC-16.4: Different Trip Type
- **Input**: Upload `trip-template.md` + "3-day cycling trip through Tuscany"
- **Expected**: Claude generates valid output adapted for cycling (not hardcoded to hiking)
