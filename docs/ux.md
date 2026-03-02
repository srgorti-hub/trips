# UX — Travel Guide Generator

## Design Language
- **Reference**: AllTrails meets Notion
- **Typography**: Clean sans-serif body (Plus Jakarta Sans), serif headings (Fraunces)
- **Layout**: Card-based, strong data hierarchy
- **Color palette**:
  - Background: warm off-white (#F5F3EF)
  - Surface: white (#FFFFFF)
  - Primary: deep green (#2C4A1E)
  - Accent: amber (#D4721A)
  - Text: near-black (#1C1C1A), muted sage (#6B7569)
- **Difficulty color coding**: Green = Easy, Amber = Moderate/Strenuous
- **Imagery**: Purposeful — photos set context, not decoration
- **Elevation charts**: First-class visual elements, prominent placement

---

## Travel Guide App (`index.html`)

### User: Trip Participant
Arrives via shared URL. No login, no setup.

### Screen Layout
Single-page app with fixed top nav and tabbed content below hero.

### User Flow

```
Land on page → See hero + trip summary
  → Browse tabs: Overview | Day by Day | Weather | Gear
  → Overview: see trip stats, accommodations, route overview
  → Day by Day: scroll day cards, expand Deep Dive for details
  → Weather: review conditions, read alerts
  → Gear: check off items (persisted in localStorage)
```

### Hero Section
- Full-width hero image (organizer-provided from `photos/hero/`, or stock photo from Unsplash based on destination)
- Trip name (large serif heading)
- Destination + date range
- Stats bar: total distance | total ascent | days | group size
- AI-generated trip summary paragraph
- YouTube overview link/button

### Tab Navigation
- Horizontal tab bar directly below hero
- Four tabs: **Overview** · **Day by Day** · **Weather** · **Gear**
- Active tab highlighted with green underline
- Tabs are sticky below the hero on scroll

### Overview Tab
- Trip stats card (distance, ascent, days, difficulty distribution)
- Accommodation list (day, location, name)
- Schematic route map or route overview
- YouTube overview embed or prominent link

### Day by Day Tab
Each day renders as a card:

**Card Header**
- Day number badge (circle, color-coded by difficulty)
- Segment label (e.g., "Milngavie to Drymen")
- Date
- Difficulty badge pill

**Card Body**
- Quick stats row: distance | ascent | estimated hours
- Written description (2–3 paragraphs)
- Terrain tags (pills)
- Accommodation info
- Photo strip: 1 main image + 2 thumbnails → lightbox on click
  - Uses organizer photos from `photos/day-N/` if available
  - Falls back to Unsplash stock photos based on location keywords
  - Gracefully hidden if no internet and no local photos

**Card Footer**
- YouTube link button
- "Deep Dive" expand/collapse toggle

**Deep Dive (expanded)**
- Elevation profile chart (SVG, rendered from `elevation/day-N-profile.json`)
  - X-axis: distance (km), Y-axis: elevation (m)
  - Summit label and marker
  - Hover/tap for elevation readout at point
- Waypoints list (with km markers and notes)
- Water sources
- Escape routes
- Warnings (highlighted, icon-prefixed)
- Resupply notes
- Map image (from `maps/day-N-map.jpg` if available)
- External links: AllTrails, Komoot, Walk Highlands
- GPX download link (from `gpx/day-N.gpx` if available)

### Weather Tab
- Temperature range card (min/max with visual bar)
- Precipitation probability (percentage + description)
- Daylight hours card
- Wind speed card
- Alerts box (prominent styling — amber/warning background, icon-prefixed alerts)
- Summary description paragraph

### Gear Tab
- Grouped by category (collapsible sections)
- Each item: checkbox + name + essential star if applicable
- Progress counter at top: "X of Y items checked"
- Checkbox state persisted in localStorage
- "Clear all" reset option

### Photo Lightbox
- Triggered by clicking any photo
- Full-screen overlay with dark backdrop
- Navigation arrows (prev/next) if multiple photos in context
- Close button (X) and Escape key to dismiss
- Caption if available

### Dark/Light Mode
- Toggle in top nav
- CSS custom properties switch between palettes
- Preference persisted in localStorage

### Desktop Layout (1024px+)
- Max content width ~1100px, centered
- Day cards use generous whitespace and larger typography
- Elevation charts render at full width within card
- Photo strips display horizontally (main + thumbnails side by side)
- Two-column layout where appropriate (e.g., overview stats + accommodations)

### Tablet Layout (768–1024px)
- Single column, slightly reduced margins
- Photo strips still horizontal
- Elevation charts scale to container width

### Mobile Layout (< 768px)
- Single-column, full-width cards
- Tabs become horizontally scrollable if needed
- Photo strips stack vertically
- Elevation charts scale to viewport width
- Touch-friendly tap targets (minimum 44px)

---

## Photo Manager (`photos.html`)

### User: Trip Organizer
Used locally before deployment. Desktop-primary.

### Screen Layout
Simple single-page layout: header, day grid, download area.

### User Flow

```
Open photos.html → It reads trip-data.json to get day structure
  → See grid: Hero slot + one slot per day
  → Drag and drop photos into each slot
  → Preview what's assigned
  → Download organized folder (zip) or save to disk
```

### Header
- Title: "Photo Manager"
- Trip name and day count (read from `trip-data.json`)
- Brief instructions: "Drag photos into each day. Download the organized folder when done."

### Photo Grid
- **Hero slot** — large drop zone at top labeled "Hero Image"
- **Day slots** — one drop zone per day, labeled with day number and segment name
- Each slot:
  - Dashed border drop zone when empty
  - Shows thumbnails of assigned photos
  - Supports multiple photos per day (main + thumbnails)
  - Remove button (X) on each thumbnail
  - Reorder by dragging within a slot

### Preview
- Click any thumbnail to see full-size preview
- Shows how photos map to the guide structure

### Download/Export
- "Download Photos" button
- Generates a zip file with the correct folder structure:
  ```
  photos/
  ├── hero/hero.jpg
  ├── day-1/photo-1.jpg, photo-2.jpg, photo-3.jpg
  ├── day-2/...
  └── ...
  ```
- Organizer unzips into the trip folder

### Responsive Behavior
- Desktop-primary (drag and drop works best with mouse)
- Tablet: functional, file picker fallback for drag-and-drop
- Mobile: basic file picker, but not the intended use case

---

## Interaction Patterns

| Pattern | Behavior |
|---------|----------|
| Tab switching | Instant, no page reload |
| Day card expand | Smooth accordion animation |
| Photo lightbox | Fade-in overlay, swipe on mobile |
| Gear checkbox | Immediate localStorage persist |
| Dark mode toggle | Instant CSS variable swap |
| Stock photo load | Async, non-blocking — placeholder shown until loaded |
| Photo manager drag-drop | Visual feedback on hover, thumbnail on drop |
| Photo manager download | Zip generated client-side via JSZip |
