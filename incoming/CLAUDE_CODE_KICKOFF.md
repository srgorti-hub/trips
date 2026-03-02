# Claude Code — Kickoff Prompt
## Active Travel Companion App

You are building the **Active Travel Companion App** — a two-surface system for planning and presenting active travel trips (hiking, walking). Read the full requirements before writing any code.

---

## Your Starting Files

You have been given two files:

1. **`travel-app-requirements-v3.md`** — full product requirements, data schemas, feature specs, and build priorities. Read this first and in full.
2. **`travel-demo.html`** — an interactive visual prototype showing both surfaces (Studio and Travel Guide App). Open this in a browser to understand the intended look and feel. Build fresh from this as reference — do not extend it.

---

## What You Are Building

### Surface 1: Travel Guide App (`index.html`)
A beautiful, static single-page web app that reads from a local folder structure and renders a day-by-day travel guide for trip participants. No live API calls at runtime. Hosted on GitHub Pages and shared with the group via URL.

### Surface 2: Studio Artifact (`studio.html`)
A form-based content review UI for the trip organizer. Used once per trip to review AI-suggested content, approve it day by day, and export a `trip-data.json` file. Built once, reused for every trip.

---

## Reference Trip (use for all dummy data)
**West Highland Way, Scotland, May 2025**
- 8 days, 154 km, Milngavie → Fort William
- 4 participants
- Mix of Moderate and Strenuous days
- Key highlights: Loch Lomond, Rannoch Moor, Devil's Staircase, Glencoe approach
- See requirements doc for full day-by-day breakdown

---

## Build Order

Follow this sequence exactly:

1. **Read** `travel-app-requirements-v3.md` in full
2. **Open** `travel-demo.html` to internalize the visual design
3. **Create** `trip-data.json` — all 8 WHW days, fully populated per schema in requirements
4. **Create** `elevation/day-N-profile.json` — realistic WHW elevation data for all 8 days
5. **Build** `index.html` — Travel Guide App (full build, mobile-responsive)
6. **Build** `studio.html` — Studio Artifact (reusable, not trip-specific)
7. **Write** GitHub Pages deployment instructions (`DEPLOY.md`)
8. **Write** `README.md` — folder setup, workflow overview, how Studio → App handoff works

---

## Key Technical Constraints

- `index.html` reads only from local files — no fetch calls to external APIs at runtime
- Elevation profile charts are **must-have** — render from `elevation/day-N-profile.json` using SVG or Canvas
- Folder structure must match exactly what is specified in requirements (see Prescribed Folder Structure section)
- Studio exports `trip-data.json` matching the schema in requirements exactly
- Both surfaces must be mobile-responsive
- Use only vanilla HTML/CSS/JS — no frameworks, no build tools, no npm

---

## Design Direction

- Reference: AllTrails meets Notion
- Card-based layout, clean typography, strong data hierarchy
- Color-code difficulty: green = Easy, amber = Moderate/Strenuous
- Elevation charts are first-class visual elements
- Photos set context, not decoration
- See `travel-demo.html` for full visual reference — match its aesthetic quality

---

## Start Here

> Read `travel-app-requirements-v3.md`, then open `travel-demo.html` in a browser, then begin with step 3 (create `trip-data.json`).
