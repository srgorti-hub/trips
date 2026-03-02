# Requirements — Travel Guide Generator

## Functional Requirements

### FR-1: Two-Phase Workflow
- **FR-1.1**: Phase 1 (Content Generation) — Organizer opens Claude.ai, uploads `trip-template.md` and their itinerary (spreadsheet, notes, or verbal description). Claude researches the route and generates `trip-data.json` and `elevation/day-N-profile.json` files.
- **FR-1.2**: Phase 2 (Distribution) — Organizer drops generated files into the travel guide folder, optionally adds photos via `photos.html`, deploys to GitHub Pages, shares URL. No login required for participants.

### FR-2: Travel Guide App (`index.html`)
- **FR-2.1**: Hero section — full-width hero image (stock or organizer-provided), trip name, destination, dates, group size, stats bar (distance, ascent, days, difficulty), AI-generated summary, YouTube overview link.
- **FR-2.2**: Navigation tabs — Overview, Day by Day, Weather, Gear.
- **FR-2.3**: Overview tab — trip stats card, accommodation list, schematic route overview, YouTube overview embed/link.
- **FR-2.4**: Day-by-Day tab — each day as a card containing:
  - Day number badge (color-coded by difficulty)
  - Date, segment label, accommodation
  - Difficulty badge (Easy / Moderate / Strenuous)
  - Quick stats: distance, ascent, estimated time
  - Written description
  - Terrain tags
  - Photo strip (main photo + 2 thumbnails, lightbox on click)
  - YouTube link
  - Expandable Deep Dive section
- **FR-2.5**: Deep Dive (per day) — elevation profile chart (from `elevation/day-N-profile.json`), waypoints list, water sources, escape routes, warnings, trail surface notes, external links (AllTrails, Komoot, Walk Highlands), GPX download link, map image.
- **FR-2.6**: Weather tab — temperature range card, precipitation probability, daylight hours, wind, alerts box (prominent styling).
- **FR-2.7**: Gear tab — shared checklist from `trip-data.json`, grouped by category, checkboxes with localStorage persistence, essential items starred, progress counter.
- **FR-2.8**: Dark/light mode toggle with localStorage persistence.
- **FR-2.9**: Photo lightbox — click any photo to view full-size with close/navigate controls.
- **FR-2.10**: Elevation profile charts are **must-have** — SVG rendered from JSON, interactive hover/tap for elevation readout, summit marker and label.

### FR-3: Photo Handling
- **FR-3.1**: If organizer provides local photos in `photos/` folders, the guide uses those.
- **FR-3.2**: If no local photos exist, the guide fetches stock photos from Unsplash based on location keywords in `trip-data.json`.
- **FR-3.3**: If no internet connection, photos are gracefully hidden — no broken images, no layout breakage.

### FR-4: Photo Manager (`photos.html`)
- **FR-4.1**: Standalone HTML page for organizing photos.
- **FR-4.2**: Reads `trip-data.json` to know the day structure (number of days, segment names).
- **FR-4.3**: Drag-and-drop interface to assign photos to: hero, or specific days.
- **FR-4.4**: Generates/downloads a zip or organized folder structure matching the expected layout.
- **FR-4.5**: Preview of assigned photos before saving.

### FR-5: Trip Template (`trip-template.md`)
- **FR-5.1**: Markdown document that instructs Claude.ai how to generate trip content.
- **FR-5.2**: Contains the complete `trip-data.json` schema with field descriptions.
- **FR-5.3**: Contains the `elevation/day-N-profile.json` schema.
- **FR-5.4**: Contains the expected folder structure.
- **FR-5.5**: Contains content guidelines — what to research for each day, how detailed descriptions should be, what trail data to include.
- **FR-5.6**: Works with any trip type (hiking, trekking, active travel) — not hardcoded to a specific route.

### FR-6: Data Files
- **FR-6.1**: `trip-data.json` — conforms to prescribed schema (see `api.md`). Contains trip metadata, participants, day-by-day data, weather, gear checklist, and location keywords for stock photo fallback.
- **FR-6.2**: `elevation/day-N-profile.json` — array of `{km, elevation_m}` points plus summit label and km. One file per day.

### FR-7: Folder Structure
- **FR-7.1**: Prescribed folder structure:
  ```
  /[trip-name]/
  ├── index.html
  ├── photos.html
  ├── trip-data.json
  ├── photos/hero/
  ├── photos/day-N/
  ├── maps/day-N-map.jpg
  ├── gpx/day-N.gpx
  ├── elevation/day-N-profile.json
  └── README.md
  ```

## Non-Functional Requirements

### NFR-1: Technology
- Vanilla HTML/CSS/JS only — no frameworks, no build tools, no npm.
- Travel Guide may make runtime API calls for stock photos (Unsplash). All other data read from local files.

### NFR-2: Performance
- App loads fast on mobile connections.
- Stock photo requests are non-blocking — guide renders immediately, photos load asynchronously.
- No external dependencies beyond Google Fonts and Unsplash API.

### NFR-3: Responsiveness
- Travel Guide must look great on both desktop browsers and mobile phones.
- Mobile-optimized for use on the trail.
- Photo Manager is desktop-primary but functional on tablet.

### NFR-4: Browser Support
- Modern browsers: Chrome, Safari, Firefox, Edge (latest 2 versions).

### NFR-5: Accessibility
- Semantic HTML, proper heading hierarchy.
- Alt text on images where available.
- Keyboard-navigable tabs and lightbox.

### NFR-6: Portability
- Entire trip is a self-contained folder — can be zipped, hosted, or shared as files.
- Works from any static host (GitHub Pages, Netlify, even a local file server).

### NFR-7: Deployment
- Deployable to GitHub Pages with no build step.
- Instructions provided in README.md.

## Out of Scope (v1)
- PDF export
- Per-participant personalized gear or fitness plans
- Native mobile app
- Real-time collaboration
- Offline-first with service worker (v2 consideration)
