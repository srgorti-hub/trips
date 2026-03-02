# Travel Guide Generator

Turn a trip idea into a polished, shareable travel guide. Describe your trip to Claude.ai, it generates the content, and a static web page turns it into a beautiful guide you share with your group via URL.

## Quick Start

### 1. Generate trip content with Claude.ai
- Open [Claude.ai](https://claude.ai)
- Upload `trip-template.md` and your itinerary (spreadsheet, notes, or just describe it)
- Claude researches the route and generates `trip-data.json` and elevation profile files
- Download the generated files

### 2. Add photos (optional)
- Open `photos.html` in your browser (via local server)
- Drag and drop your own photos into day slots
- Download the organized zip and unzip into the trip folder
- If you skip this, the guide shows stock photos automatically

### 3. Preview and deploy
```bash
python -m http.server 8000
# Open http://localhost:8000
```
- Review the guide locally
- Deploy to GitHub Pages (see instructions below)
- Share the URL with your group — no login or app install needed

## Folder Structure

```
west-highland-way/
├── index.html              ← Travel Guide (open in browser)
├── photos.html             ← Photo Manager (drag-and-drop organizer)
├── trip-template.md        ← Upload to Claude.ai with your itinerary
├── trip-data.json          ← Generated trip content (from Claude.ai)
├── photos/
│   ├── hero/               ← Hero image (optional — stock fallback)
│   └── day-1/ to day-N/    ← Day photos (optional — stock fallback)
├── maps/
│   └── day-N-map.jpg       ← Trail map images (optional)
├── gpx/
│   └── day-N.gpx           ← GPX files for GPS apps (optional)
├── elevation/
│   └── day-N-profile.json  ← Elevation data for charts
├── docs/                   ← Project documentation
└── README.md               ← This file
```

## How It Works

```
You describe your trip
        ↓
Upload trip-template.md + itinerary to Claude.ai
        ↓
Claude researches and generates trip-data.json + elevation files
        ↓
Drop files into this folder
        ↓
(Optional) Add your own photos via photos.html
        ↓
Deploy to GitHub Pages or any static host
        ↓
Share URL with your group
```

## Guide Features

- **4 tabs**: Overview, Day by Day, Weather, Gear
- **Day cards** with distance, ascent, difficulty, terrain, accommodation
- **Elevation profile charts** (interactive SVG with hover/tap readout)
- **Deep Dive** per day: waypoints, water sources, escape routes, warnings, map, GPX download
- **Weather dashboard**: temperature, precipitation, daylight, wind, alerts
- **Gear checklist**: interactive checkboxes saved in browser
- **Photo lightbox** with keyboard navigation
- **Stock photo fallback**: automatic placeholder photos when you don't provide your own
- **Dark mode** toggle (preference saved)
- **Responsive**: looks great on desktop and mobile — usable on the trail

## Photo Handling

Photos resolve in this order:
1. **Your photos** — from `photos/hero/` and `photos/day-N/` folders
2. **Stock photos** — fetched automatically based on location keywords in trip data
3. **Hidden gracefully** — if offline and no local photos, the layout adjusts cleanly

Use `photos.html` to organize your own photos into the correct folder structure.

## Creating a New Trip

1. Copy this folder and clear out the trip-specific files (`trip-data.json`, `elevation/`, `photos/`, `maps/`, `gpx/`)
2. Keep `index.html`, `photos.html`, `trip-template.md`, and this README
3. Open Claude.ai, upload `trip-template.md` and describe your new trip
4. Download the generated JSON and elevation files
5. Add photos if desired
6. Deploy

Works for any active travel trip — hiking, trekking, cycling, multi-day walks.

## Deploy to GitHub Pages

1. Create a new GitHub repository
2. Push this folder to the repo:
   ```bash
   git init
   git add .
   git commit -m "Travel guide: [Trip Name]"
   git remote add origin https://github.com/[you]/[repo].git
   git push -u origin main
   ```
3. Go to **Settings → Pages** in the repo
4. Set source to **main** branch, root folder
5. Your guide will be live at `https://[you].github.io/[repo]/`

## Local Development

```bash
python -m http.server 8000
```

Open http://localhost:8000 — the guide loads `trip-data.json` and elevation files via fetch, so a local server is required (no `file://` protocol).

## Troubleshooting

- **Blank page**: Make sure you're using a local server, not opening `index.html` directly
- **No elevation charts**: Check that `elevation/day-N-profile.json` files exist
- **Stock photos not loading**: Check internet connection; photos hide gracefully when offline
- **Photos not showing after using photos.html**: Unzip the downloaded file into the trip folder root

## Tech Stack

- Vanilla HTML, CSS, JavaScript — no frameworks, no build tools
- Google Fonts (Plus Jakarta Sans, Fraunces)
- SVG for elevation charts
- localStorage for gear checkboxes and dark mode
- Lorem Picsum for stock photo fallback (no API key needed)
- JSZip (CDN) for photo manager zip export
