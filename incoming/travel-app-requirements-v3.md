# Active Travel Companion App — Requirements v3

## Project Overview
A self-contained active travel guide system built across two surfaces:
1. **The Studio** — an organizer-facing content review UI (Claude.ai artifact)
2. **The Travel Guide App** — a participant-facing day-by-day experience (static web app)

Content is researched in Claude.ai chat (web search, AI generation), reviewed in the Studio, then handed off to Claude Code to build the Travel Guide App.

**Design reference**: AllTrails meets Notion — card-based, clean typography, data-rich, purposeful imagery. Functional beauty, not editorial flair.

**Reference trip for all development and testing**: West Highland Way, Scotland, May 2025 — 8 days, 154 km, Milngavie to Fort William.

---

## Visual & UX Reference
`travel-demo.html` — a fully designed, interactive prototype demonstrating both surfaces. Claude Code should use this as the visual and UX reference. **Build fresh** from this reference rather than extending it — the demo has no real architecture.

---

## Three-Phase Workflow

### Phase 1 — Content Studio (Claude.ai Chat + Studio Artifact)
Two surfaces working in tandem in the same Claude.ai browser session.

**Claude.ai Chat** does all intelligent work:
- Parses raw itinerary (spreadsheet, text, URLs, Gmail)
- Web searches for trail guides, AllTrails/Komoot pages, tourism boards, hiking blogs
- Finds YouTube links (route vlogs, drone footage, scenic overviews)
- Suggests photo search terms per day and location
- Retrieves weather and seasonal context for destination + month
- Generates gear list from terrain and weather profile
- Asks clarifying questions only when genuinely ambiguous

**The Studio Artifact** is a form-based UI — does no AI work itself:
- Displays Claude's suggestions in a structured, editable interface
- Organizer reviews and edits content day by day
- Approve/pending state tracked per day and per content section
- On completion, exports a validated `trip-data.json`

### Phase 2 — App Build (Claude Code)
- Receives: requirements doc + `trip-data.json` + populated asset folder
- Builds: static `index.html` reading from local assets only — no live API calls at runtime
- Output: beautiful, functional travel guide app

### Phase 3 — Distribution
- Claude Code deploys folder to GitHub Pages
- Organizer shares single URL with group
- No login required, opens in any browser
- Any participant can take the code into Claude Code and customize their own version

**Alternative (v1.5)**: Claude Code can also produce a fully self-contained single `index.html` with all assets base64-encoded inline — shareable as a file, no hosting required.

---

## Deliverables Summary

| Deliverable | Produced by | Used by |
|-------------|-------------|---------|
| Studio Artifact | Claude Code (one-time build) | Organizer in Claude.ai |
| `trip-data.json` | Studio Artifact export | Claude Code |
| Asset folder | Organizer (manual download) | Claude Code |
| `index.html` Travel Guide App | Claude Code | Participants via GitHub Pages |
| Self-contained HTML (v1.5) | Claude Code (optional) | File-based sharing |

The Studio Artifact is a one-time build — used for every future trip, not rebuilt per trip.

---

## Prescribed Folder Structure

```
/[trip-name]/
├── index.html                  ← Travel Guide App (built by Claude Code)
├── trip-data.json              ← Structured trip data (exported from Studio)
├── photos/
│   ├── hero/                   ← Trip-level hero images (1–3)
│   ├── day-1/                  ← 2–5 images per day
│   ├── day-2/
│   └── ...
├── maps/
│   └── day-1-map.jpg           ← Trail map screenshots or exports
├── gpx/
│   └── day-1.gpx
├── elevation/
│   └── day-1-profile.json      ← Elevation data for chart rendering
└── docs/
    └── [participant uploads]   ← Personal training plans, medical info, etc.
```

No assets are fetched at runtime. The app reads only from this folder.

---

## trip-data.json Schema

```json
{
  "trip": {
    "name": "West Highland Way",
    "destination": "Scotland",
    "dates": { "start": "2025-05-10", "end": "2025-05-17" },
    "group_size": 4,
    "total_distance_km": 154,
    "total_ascent_m": 4800,
    "youtube_overview": "https://youtube.com/...",
    "description": "AI-generated trip summary paragraph"
  },
  "participants": [
    { "name": "Gorti", "role": "organizer" },
    { "name": "Friend Name", "role": "participant" }
  ],
  "days": [
    {
      "day": 1,
      "label": "Milngavie to Drymen",
      "date": "2025-05-10",
      "distance_km": 19.5,
      "ascent_m": 260,
      "descent_m": 190,
      "estimated_hours": 5.5,
      "difficulty": "Moderate",
      "terrain_tags": ["Farmland", "Woodland", "Good paths"],
      "description": "AI-generated day description",
      "accommodation": { "name": "Winnock Hotel", "location": "Drymen" },
      "resupply_notes": "Co-op in Drymen, closes 9pm",
      "water_sources": ["Balmaha", "Drymen village"],
      "escape_routes": ["Bus from Drymen or Balmaha to Glasgow"],
      "warnings": [],
      "waypoints": [
        { "name": "Mugdock Country Park", "km": 4 },
        { "name": "Conic Hill summit", "km": 14, "note": "Panoramic loch views" }
      ],
      "links": {
        "alltrails": "https://...",
        "komoot": "https://...",
        "walk_highlands": "https://...",
        "gpx_download": "gpx/day-1.gpx"
      },
      "youtube": "https://youtube.com/...",
      "photos": ["photos/day-1/img1.jpg", "photos/day-1/img2.jpg"],
      "map": "maps/day-1-map.jpg",
      "elevation_profile": "elevation/day-1-profile.json"
    }
  ],
  "weather": {
    "month": "May",
    "temp_min_c": 8,
    "temp_max_c": 15,
    "precipitation_probability": 0.6,
    "daylight_hours": 17,
    "wind_kmh": "15–30",
    "description": "Cool days, cold evenings. Expect rain on ~6 of 8 days.",
    "alerts": [
      "Midges emerge late May — carry repellent and head net",
      "Keep waterproofs accessible at all times — weather changes rapidly"
    ]
  },
  "gear_checklist": [
    { "category": "Footwear & Clothing", "item": "Waterproof hiking boots", "essential": true },
    { "category": "Footwear & Clothing", "item": "Waterproof jacket", "essential": true },
    { "category": "Navigation & Safety", "item": "OS Map 1:25000", "essential": true }
  ]
}
```

### elevation/day-N-profile.json Schema
```json
{
  "points": [
    { "km": 0, "elevation_m": 50 },
    { "km": 2, "elevation_m": 80 },
    { "km": 14, "elevation_m": 361 }
  ],
  "summit_label": "Conic Hill 361m",
  "summit_km": 14
}
```

---

## Travel Guide App — Feature Spec

### Visual Design
- Card-based layout, clean sans-serif typography, strong data hierarchy
- Purposeful imagery — photos set context, not decoration
- Elevation charts as first-class visual elements
- Dark/light mode support
- Mobile-responsive

### 1. Hero Section
- Full-width hero image from `photos/hero/`
- Trip name, destination, dates, group size
- Trip stats bar: total distance, total ascent, days, difficulty
- AI-generated trip summary
- YouTube overview link

### 2. Navigation Tabs
- Overview · Day by Day · Weather · Gear

### 3. Overview Tab
- Trip stats card, accommodation list, schematic route map
- YouTube overview embed/link

### 4. Day by Day Tab — Day Cards
Each day rendered as a card:
- Day number badge (color-coded by difficulty: green=easy, amber=moderate/strenuous)
- Date, segment label, accommodation
- Difficulty badge (Easy / Moderate / Strenuous)
- Quick stats: distance, ascent, estimated time
- Written description
- Terrain tags
- Photo strip (main photo + 2 thumbnails, lightbox on click)
- YouTube link
- Expandable **Deep Dive** section (see below)

### 5. Deep Dive (expandable per day card)
- **Elevation profile chart** — rendered from `elevation/day-N-profile.json` — MUST-HAVE, not optional
- Waypoints list
- Water sources
- Escape routes
- Warnings (highlighted if present)
- Trail surface notes
- External links: AllTrails, Komoot, Walk Highlands, GPX download

### 6. Weather Tab
- Temperature range card with visual bar
- Precipitation probability card
- Daylight hours card
- Wind card
- Alerts box (styled prominently)

### 7. Gear Tab
- Shared group checklist rendered from `trip-data.json` gear block
- Grouped by category
- Checkboxes (state held in localStorage or memory)
- Essential items marked with star
- Progress counter (X of Y items checked)

---

## Studio Artifact — Feature Spec
Built once by Claude Code. Reused for every trip.

### Layout
- Sticky top nav with trip name and Export button
- Left sidebar: scrollable day list with status indicators (approved / pending / empty)
- Main panel: day-by-day content review

### Sidebar
- Trip metadata (name, dates, distance, group size)
- Day list with status dots
- Progress bar (X of N days approved)

### Day Panel (one per day)
Each panel contains collapsible sections:
- **Hike Statistics** — editable fields: distance, ascent, descent, estimated time, difficulty
- **Day Description** — textarea with "Regenerate with AI" button
- **Trail Links** — list of suggested URLs, each with approve checkbox, replace, remove actions; add new URL input
- **YouTube** — single approved video with replace option
- **Photos** — grid of suggested photos, approve/reject per image, search for more button

### Status Tracking
- Each section has Approved / Needs Review badge
- Day status (sidebar dot) reflects overall day completion
- Export blocked until all days approved

### Export
- Sticky export bar at bottom of each panel
- Shows approval progress summary
- "Export trip-data.json" button — downloads structured JSON matching schema above

---

## Build Priorities for Claude Code

Build in this order:

1. `trip-data.json` — populate with West Highland Way dummy data (all 8 days)
2. Elevation JSON files — one per day with realistic WHW profile data
3. Travel Guide App `index.html` — full build using demo as visual reference
4. Studio Artifact — separate HTML file, reusable across trips
5. GitHub Pages deployment — instructions or script
6. README — folder setup, how to run, how to use Studio → App workflow

---

## Out of Scope for v1
- PDF export (v2)
- Group photo albums with annotations (separate project)
- Per-participant personalised gear or fitness plans
- Native mobile app
- Live API calls at runtime

---

## Handoff Checklist
- [x] Requirements v3 (this doc)
- [x] `travel-demo.html` — visual and UX reference
- [ ] Organizer populates asset folder before running app build step
