# Architecture — Travel Guide Generator

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                      CONTENT CREATION                           │
│                                                                 │
│  Organizer uploads trip-template.md + itinerary to Claude.ai    │
│  Claude researches route, generates:                            │
│    → trip-data.json                                             │
│    → elevation/day-N-profile.json                               │
│                                                                 │
└──────────────────────────────┬──────────────────────────────────┘
                               │ download generated files
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                      ASSEMBLY                                   │
│                                                                 │
│  Organizer drops files into trip folder:                        │
│    → trip-data.json + elevation/ (from Claude.ai)               │
│    → photos/ (via photos.html drag-and-drop — optional)         │
│    → maps/, gpx/ (manually sourced — optional)                  │
│                                                                 │
└──────────────────────────────┬──────────────────────────────────┘
                               │ git push
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DISTRIBUTION                               │
│                                                                 │
│  GitHub Pages ──► Participants access via URL                   │
│  (or any static host, or local server, or zipped folder)        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Tech Stack

| Layer | Choice | Rationale |
|-------|--------|-----------|
| Language | Vanilla JavaScript (ES6+) | No build step, runs anywhere |
| Markup | HTML5 | Semantic, accessible |
| Styling | CSS3 with Custom Properties | Dark/light mode via variable swap, no preprocessor |
| Fonts | Google Fonts (Plus Jakarta Sans, Fraunces) | Clean typography |
| Charts | SVG (inline, generated via JS) | No charting library needed for elevation profiles |
| Storage | localStorage | Gear checkbox state, dark mode preference |
| Data format | JSON | `trip-data.json` and `elevation/*.json` |
| Stock photos | Unsplash API (no key for anonymous access) | Free fallback when organizer doesn't provide photos |
| Zip generation | JSZip (CDN) | Client-side zip in photos.html |
| Hosting | GitHub Pages | Free, static, no build step |
| No backend | — | All data is local files + one optional stock photo API |

## Component Architecture

### Travel Guide App (`index.html`)

Single HTML file with embedded CSS and JS.

```
index.html
├── <head>
│   ├── Meta tags, fonts
│   └── <style> — all CSS (custom properties, layout, components, responsive, dark mode)
│
├── <body>
│   ├── Top nav (logo, dark mode toggle)
│   ├── Hero section (rendered from trip-data.json)
│   ├── Tab bar (Overview | Day by Day | Weather | Gear)
│   ├── Tab panels
│   │   ├── #overview — stats, accommodations, route
│   │   ├── #days — day cards (generated from trip.days[])
│   │   ├── #weather — weather cards (from trip.weather)
│   │   └── #gear — checklist (from trip.gear_checklist[])
│   ├── Photo lightbox overlay
│   └── Footer
│
└── <script>
    ├── Data loading (fetch trip-data.json, elevation JSONs)
    ├── Photo resolver (check local photos → fallback to Unsplash → hide gracefully)
    ├── Rendering functions (renderHero, renderDays, renderWeather, renderGear)
    ├── Elevation chart renderer (SVG generation from profile data)
    ├── Tab controller
    ├── Lightbox controller
    ├── Gear checkbox manager (localStorage)
    ├── Dark mode controller (localStorage)
    └── Init / bootstrap
```

### Photo Manager (`photos.html`)

Single HTML file. Reads `trip-data.json` for day structure.

```
photos.html
├── <head>
│   ├── Meta tags, fonts
│   ├── <script src="jszip.min.js"> (CDN)
│   └── <style> — all CSS
│
├── <body>
│   ├── Header (title, trip name, instructions)
│   ├── Photo grid
│   │   ├── Hero drop zone
│   │   └── Day drop zones (one per day, labeled with segment name)
│   └── Download bar (generate zip button)
│
└── <script>
    ├── Load trip-data.json (get day count, segment names)
    ├── Drag-and-drop handler (file assignment to days)
    ├── Thumbnail renderer (preview assigned photos)
    ├── Reorder / remove controls
    ├── Zip generator (JSZip — build photos/ folder structure)
    └── Init
```

### Trip Template (`trip-template.md`)

Markdown file — not code. Uploaded to Claude.ai alongside the organizer's itinerary.

```
trip-template.md
├── Instructions for Claude (what to research, how detailed to be)
├── trip-data.json schema (complete field reference with descriptions)
├── elevation/day-N-profile.json schema
├── Expected folder structure
├── Content guidelines (description length, what trail data to include)
└── Example snippets (so Claude understands the expected output format)
```

## Data Flow

```
1. Organizer opens Claude.ai, uploads trip-template.md + itinerary
2. Claude researches the route and generates trip-data.json + elevation JSONs
3. Organizer downloads the generated files
4. Organizer optionally adds photos via photos.html (drag-and-drop → zip)
5. Organizer optionally adds maps and GPX files manually
6. Organizer drops all files into the trip folder alongside index.html
7. Folder pushed to GitHub → GitHub Pages serves it
8. Participants open URL on phone/desktop
9. index.html fetches trip-data.json + elevation JSONs locally
10. For photos: checks photos/ folder first, falls back to Unsplash API
```

## Photo Resolution Logic

```
For each photo slot (hero, day-1, day-2, etc.):
  1. Check if local file exists: photos/hero/hero.jpg or photos/day-N/*.jpg
     → YES: use local file
     → NO: continue
  2. Check trip-data.json for location keywords (e.g., "Rannoch Moor", "Loch Lomond")
     → Fetch from Unsplash using location keyword as search query
     → If fetch succeeds: display stock photo
     → If fetch fails (no internet, rate limit): hide photo gracefully, no broken image
```

## File/Folder Structure

```
/TravelPlanner/                ← Project root (reusable across trips)
├── index.html                 ← Travel Guide App template
├── photos.html                ← Photo Manager tool
├── trip-template.md           ← Upload to Claude.ai
├── README.md                  ← Workflow instructions
└── docs/                      ← Project documentation

/[trip-name]/                  ← Per-trip folder (e.g., west-highland-way/)
├── index.html                 ← Copy of Travel Guide App
├── trip-data.json             ← Generated by Claude.ai
├── photos/
│   ├── hero/                  ← Hero images (optional)
│   └── day-N/                 ← Day photos (optional)
├── maps/
│   └── day-N-map.jpg          ← Trail map images (optional)
├── gpx/
│   └── day-N.gpx              ← GPX files for download (optional)
└── elevation/
    └── day-N-profile.json     ← Elevation data for charts
```

## Key Design Decisions

### 1. Single-file approach (index.html)
All CSS and JS embedded in one HTML file. Maximizes portability — no build step. Tradeoff: larger file, no code splitting. Acceptable for this app's size.

### 2. Claude.ai for content generation (no API key)
The organizer uses their existing Claude.ai account — no API key, no cost beyond their subscription. The `trip-template.md` document provides Claude with the schema and instructions. This is simpler than building an API integration.

### 3. Stock photos via Unsplash
Unsplash allows anonymous access for low-volume usage. The guide fetches photos based on location keywords in `trip-data.json`. If the organizer provides their own photos, those take priority. No API key required for basic usage.

### 4. SVG for elevation charts
Custom SVG generation via JavaScript rather than a charting library. The elevation profile is a simple line chart with area fill — doesn't warrant a library dependency.

### 5. localStorage for state
Gear checkboxes and dark mode preference are the only user state. localStorage is sufficient — no user accounts, no sync needed.

### 6. Client-side zip for photo manager
JSZip generates the organized photo folder structure entirely in the browser. No server upload, no backend. The organizer unzips into their trip folder.

### 7. No service worker / offline (v1)
v1 relies on connectivity for stock photos. Local photos and all other content work without internet. Full offline support is a v2 consideration.

## Integration Points

| From | To | Mechanism |
|------|-----|-----------|
| Organizer + itinerary | Claude.ai | Upload `trip-template.md` + itinerary file |
| Claude.ai | Trip folder | Organizer downloads generated JSON files |
| Organizer photos | Trip folder | `photos.html` → zip download → unzip into folder |
| Trip folder | GitHub Pages | `git push` to repo with Pages enabled |
| GitHub Pages | Participants | HTTPS URL |
| `index.html` | Unsplash | Runtime fetch for stock photos (fallback only) |
