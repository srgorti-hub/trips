# Build Plan — Travel Guide Generator

## What Already Exists

The previous build produced working versions of several files. This plan updates and extends them rather than starting from scratch.

| Existing File | Status | Action |
|---------------|--------|--------|
| `trip-data.json` | Working, 8 WHW days | Update: add `location_keywords` fields |
| `elevation/day-N-profile.json` (×8) | Working | No changes needed |
| `index.html` | Working, all tabs functional | Update: add stock photo fallback, map/GPX links in Deep Dive |
| `studio.html` | Working but no longer needed | Delete |
| `DEPLOY.md` | Working | Fold into README |
| `README.md` | Working | Rewrite for new workflow |

## Phase Overview

| Phase | Deliverable | Depends On | Status |
|-------|-------------|------------|--------|
| 1 | Update `trip-data.json` (add `location_keywords`) | Schema in `api.md` | DONE |
| 2 | Update `index.html` (stock photos, map/GPX links) | Phase 1 | DONE |
| 3 | Build Photo Manager (`photos.html`) | Phase 1 (day structure) | DONE |
| 4 | Create `trip-template.md` | Schema in `api.md` | DONE |
| 5 | Write `README.md` | All phases | DONE |
| 6 | Cleanup (delete `studio.html`, reorganize folder) | All phases | DONE |

---

## Phase 1: Update `trip-data.json`

**Goal**: Add `location_keywords` to existing trip data so the Travel Guide can fetch stock photos.

### Steps
1. Add `location_keywords` array to `trip` object (broad destination terms)
2. Add `location_keywords` array to each of the 8 `days` entries (segment-specific terms)
3. Validate JSON still conforms to updated schema in `api.md`

### Milestone
`trip-data.json` has `location_keywords` at trip level and all 8 day levels.

---

## Phase 2: Update Travel Guide App (`index.html`)

**Goal**: Add stock photo fallback and map/GPX support to the existing working guide.

### Steps

#### 2a: Photo Resolution Logic
1. Add photo resolver function:
   - Check if local photo path exists (try fetch, check response)
   - If missing, fetch from Unsplash using `location_keywords`
   - If Unsplash fails (no internet, rate limit), hide photo gracefully
2. Apply to hero image
3. Apply to day photo strips
4. Ensure no broken image icons — use CSS fallback or hide element

#### 2b: Unsplash Integration
1. Use Unsplash Source URL format (no API key needed for basic usage) or Unsplash API with anonymous access
2. Build search query from `location_keywords` array
3. Load photos asynchronously — show placeholder/skeleton while loading
4. Cache fetched URLs in sessionStorage to avoid re-fetching on tab switch

#### 2c: Map & GPX Links in Deep Dive
1. If `days[N].map` exists, render map image in Deep Dive section
2. If `days[N].links.gpx_download` exists, render GPX download button
3. Handle missing files gracefully (hide elements, don't break layout)

#### 2d: Testing
1. Test with local photos present → should use local
2. Test with no local photos → should fetch from Unsplash
3. Test with no internet → should hide photos, everything else works
4. Test responsive layout with stock photos (different aspect ratios)
5. Test dark mode with all photo states

### Milestone
Guide displays stock photos when no local photos exist. Map images and GPX downloads appear in Deep Dive when available. No broken images under any condition.

---

## Phase 3: Build Photo Manager (`photos.html`)

**Goal**: Drag-and-drop page for organizers to assign photos to days and export organized folders.

### Steps

#### 3a: Page Structure & Styling
1. Create `photos.html` with HTML5 boilerplate
2. Use same design system as `index.html` (colors, fonts, card style)
3. Include JSZip via CDN for client-side zip generation

#### 3b: Data Loading
1. Fetch `trip-data.json` to read day count and segment labels
2. Dynamically generate drop zones: 1 hero slot + 1 per day

#### 3c: Drop Zones
1. Hero image drop zone (large, prominent)
2. Per-day drop zones labeled with day number and segment name (e.g., "Day 1 — Milngavie to Drymen")
3. Dashed border styling for empty zones
4. Visual feedback on drag-over (highlight border)

#### 3d: Photo Assignment
1. Accept drag-and-drop files (images only)
2. Also support click-to-browse file picker as fallback
3. Show thumbnail previews of assigned photos
4. Support multiple photos per day (up to 3 — main + 2 thumbnails)
5. Remove button (X) on each thumbnail
6. Reorder within a slot by dragging

#### 3e: Zip Export
1. "Download Photos" button
2. Build zip with correct folder structure:
   ```
   photos/
   ├── hero/hero.jpg
   ├── day-1/img1.jpg, img2.jpg, img3.jpg
   ├── day-2/...
   └── ...
   ```
3. Rename files to match expected naming convention
4. Trigger browser download of zip

#### 3f: Responsive
1. Desktop-primary (drag-and-drop)
2. Tablet: functional with file picker
3. Basic mobile support

### Milestone
Organizer can drag photos into day slots, see previews, and download a correctly structured zip file.

---

## Phase 4: Create `trip-template.md`

**Goal**: A document the organizer uploads to Claude.ai alongside their itinerary. Tells Claude exactly how to generate the trip content.

### Steps
1. Write clear instructions section:
   - What Claude should do (research the route, generate structured content)
   - How to handle the itinerary input (spreadsheet, notes, or verbal description)
   - What to research for each day (distances, terrain, accommodations, waypoints, etc.)
2. Include complete `trip-data.json` schema with field descriptions
3. Include `elevation/day-N-profile.json` schema
4. Include expected folder structure
5. Include content guidelines:
   - Description length and tone (informative, inspiring, 2–3 paragraphs per day)
   - How to choose `location_keywords` (specific, photogenic landmarks)
   - How to rate difficulty
   - What makes good waypoints, water sources, escape routes, warnings
6. Include a short example snippet (1 day of output) so Claude sees the expected format
7. Test by actually uploading to Claude.ai with a sample itinerary and verifying output

### Milestone
Uploading `trip-template.md` + a rough itinerary to Claude.ai produces a valid, complete `trip-data.json` and elevation files on the first try.

---

## Phase 5: Write `README.md`

**Goal**: End-to-end instructions that any organizer can follow.

### Steps
1. Project overview (what this is, what it produces)
2. Quick start (the 3-step workflow: generate → add photos → deploy)
3. Detailed workflow:
   - How to use `trip-template.md` with Claude.ai
   - How to use `photos.html`
   - How to set up the trip folder
4. Folder structure reference
5. Local development (how to preview with `python -m http.server`)
6. Deployment to GitHub Pages (step-by-step)
7. Troubleshooting (CORS, missing files, stock photos not loading)

### Milestone
A non-technical organizer can follow the README from start to a deployed travel guide.

---

## Phase 6: Cleanup

**Goal**: Remove old artifacts, organize the project folder.

### Steps
1. Delete `studio.html` from project root
2. Delete old `DEPLOY.md` from `west-highland-way/` (content now in README)
3. Move reusable files (`index.html`, `photos.html`, `trip-template.md`, `README.md`) to project root
4. Ensure `west-highland-way/` contains only trip-specific files (trip-data.json, elevation/, photos/, maps/, gpx/)
5. Verify everything still works after reorganization

### Milestone
Clean folder structure. No dead files. Project root has reusable tools, trip folder has trip-specific data.

---

---

## Phase 7: GPX Data Processor (`gpx-tool.html`)

**Goal**: Build a GPX processing tool that parses real GPS data and compares it against estimated stats in `trip-data.json`.

**Status**: DONE

### Steps
1. Create `gpx-tool.html` with matching design system (same fonts, colors, card style)
2. Load `trip-data.json` to get day structure and estimated stats
3. Build per-day drop zones for GPX file upload
4. Implement GPX parser (XML → track points with lat/lon/ele)
5. Implement stats calculator (haversine distance, ascent/descent with noise threshold, max elevation)
6. Implement elevation profile generator (sampled at 0.5km intervals)
7. Render comparison tables (estimated vs. GPX with diff %)
8. Render mini SVG elevation charts per day
9. Export updated `trip-data.json` with GPX-derived stats
10. Export elevation data as zip (JSZip)

### Milestone
Organizer can drop GPX files for each day, see stat comparisons and elevation profiles, and download updated trip data.

---

## Phase 8: Multi-Trip Tool Availability

**Goal**: Make `photos.html` and `gpx-tool.html` available in every trip folder, not just WHW.

**Status**: DONE

### Steps
1. Copy `gpx-tool.html` from `west-highland-way/` to `patagonia/`
2. Copy `photos.html` from `west-highland-way/` to `patagonia/`
3. Add footer links (Photo Manager + GPX Data Processor) to `patagonia/index.html`
4. Verify tools load `trip-data.json` correctly from the Patagonia folder

### Milestone
Both trips have all three tools. Footer links work. New trips follow the same pattern: copy all three HTML files into the trip folder.

---

## Dependencies Graph

```
Phase 1 (update trip-data.json)
   │
   ├──► Phase 2 (update index.html)
   │
   └──► Phase 3 (photos.html)

Phase 4 (trip-template.md) ← independent, can run in parallel

Phase 5 (README) ← depends on all above
   │
   └──► Phase 6 (cleanup) ← last

Phase 7 (gpx-tool.html) ← depends on Phase 1

Phase 8 (multi-trip tools) ← depends on Phases 3, 7
```

All phases complete.
