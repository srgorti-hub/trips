# Test Plan — Travel Guide Generator

## Testing Strategy

This is a static web app with no backend, no build step, and no framework. Testing is primarily **manual** with **automated validation** for data files. No test framework (Jest, Cypress, etc.) is required — this matches the vanilla, zero-dependency philosophy.

---

## Testing Phases

### Phase 1: Data Validation (Automated)
**When**: After updating `trip-data.json` with `location_keywords` (Build Phase 1)
**How**: Node.js or Python validation script

| What | Method | Pass Criteria |
|------|--------|---------------|
| `trip-data.json` schema | Script parses JSON and checks required fields, types, enums | All required fields present, correct types |
| Day count and sequencing | Script checks `days.length` and `day` values | 8 days, sequential 1–8 |
| Date range consistency | Script checks each day date within trip date range | All dates valid |
| Location keywords | Script checks `trip.location_keywords` and each `days[].location_keywords` | All present, ≥ 1 entry each |
| File path references | Script checks that referenced paths follow naming convention | All paths match pattern |
| Elevation file existence | Script checks `elevation/` directory | 8 files present |
| Elevation schema | Script validates each elevation JSON | Points sorted, valid numbers |
| Elevation distance match | Script compares last point km to day distance_km | Within ±1 km |

**Deliverable**: `validate.py` — run once after data creation, re-run if data changes.

### Phase 2: Travel Guide App — Functional Testing (Manual)
**When**: After updating `index.html` with stock photo logic (Build Phase 2)
**How**: Manual browser testing with local HTTP server

**Setup**:
```bash
cd [trip-folder]
python -m http.server 8000
# Open http://localhost:8000
```

**Test execution order**:
1. Initial load — page renders, no console errors (TC-3.1, TC-3.2)
2. Hero section — all metadata correct (TC-4.1–4.4)
3. Tab navigation — all tabs switch correctly (TC-5.1–5.3)
4. Overview tab — stats and accommodations render (TC-6.1–6.2)
5. Day by Day tab — all 8 cards render with correct data (TC-7.1–7.3)
6. Deep Dive — expand each day, verify elevation chart (TC-7.4–7.6)
7. Deep Dive content — waypoints, GPX link, map image, warnings (TC-7.7–7.11)
8. Weather tab — all cards render with correct data (TC-9.1–9.4)
9. Gear tab — checklist, checkboxes, persistence, counter (TC-10.1–10.5)
10. Photo lightbox — open, navigate, close (TC-11.1–11.3)
11. Dark mode — toggle, persistence, chart readability (TC-12.1–12.4)

### Phase 3: Photo Scenarios (Manual)
**When**: After Phase 2 passes
**How**: Test with different photo configurations

| Scenario | Setup | Expected | Test Cases |
|----------|-------|----------|------------|
| Local photos only | Place images in `photos/day-1/` etc. | Local photos displayed | TC-8.1 |
| No local photos, online | Empty `photos/`, internet connected | Unsplash stock photos load | TC-8.2 |
| No local photos, offline | Empty `photos/`, disconnect internet | Photos hidden, no broken images | TC-8.3 |
| Mixed | Some days with local, some without | Local where available, stock for rest | TC-8.4 |
| Hero fallback | No `photos/hero/` file | Stock hero or gradient fallback | TC-8.5 |

### Phase 4: Photo Manager Testing (Manual)
**When**: After building `photos.html` (Build Phase 3)
**How**: Manual browser testing

**Test execution order**:
1. Initial load — reads `trip-data.json`, shows correct day slots (TC-14.1)
2. Missing data file — shows error message (TC-14.2)
3. Drag and drop — image accepted, thumbnail shown (TC-14.3)
4. File picker — click to browse works as fallback (TC-14.4)
5. Multiple photos per day — up to 3 accepted (TC-14.5)
6. Remove photo — X button removes thumbnail (TC-14.6)
7. Non-image rejection — text files rejected (TC-14.7)
8. Zip download — correct folder structure in zip (TC-14.8, TC-14.9)
9. Empty download — blocked or warned (TC-14.10)

### Phase 5: GPX Data Processor Testing (Manual)
**When**: After building/copying `gpx-tool.html` into trip folders
**How**: Manual browser testing with local HTTP server

**Test execution order**:
1. Initial load — reads `trip-data.json`, shows correct day cards with estimated stats (TC-15.1)
2. Missing data file — shows error message (TC-15.2)
3. GPX file drop — parsed, comparison table + chart shown (TC-15.3)
4. Non-GPX rejection — alert shown (TC-15.4)
5. GPX without elevation — alert shown (TC-15.5)
6. Comparison accuracy — diff percentages correct, >10% highlighted (TC-15.7)
7. Mini elevation chart — SVG renders correctly (TC-15.8)
8. Clear & re-drop — results cleared, drop zone reappears (TC-15.9)
9. Download updated trip-data.json — stats replaced correctly (TC-15.10)
10. Download elevation zip — correct folder structure (TC-15.11)
11. Results summary — table shows all days (TC-15.12)
12. Multi-trip — open from patagonia folder, loads patagonia data (TC-15.13)
13. Footer link — navigate from index.html footer (TC-15.14)

### Phase 6: Trip Template Testing (Manual)
**When**: After creating `trip-template.md` (Build Phase 4)
**How**: Actually upload to Claude.ai and test with real conversations

| Test | Input | Expected |
|------|-------|----------|
| Text itinerary | `trip-template.md` + "5-day Camino from Sarria" | Valid `trip-data.json` + elevation files (TC-16.1) |
| Spreadsheet | `trip-template.md` + xlsx with day/distance/accommodation | Claude uses spreadsheet data, fills gaps (TC-16.2) |
| Schema compliance | Output from above tests | Passes all TC-1 validation checks (TC-16.3) |
| Different trip type | `trip-template.md` + "3-day cycling trip in Tuscany" | Valid output adapted for cycling (TC-16.4) |

### Phase 7: Responsive Testing (Manual)
**When**: After Phases 2–5 pass
**How**: Browser DevTools device emulation + real devices if available

| Viewport | Test targets |
|----------|-------------|
| Mobile (375px) | iPhone SE — Travel Guide App (TC-13.1) |
| Mobile (390px) | iPhone 14 — Travel Guide App |
| Tablet (768px) | iPad — Travel Guide + Photo Manager (TC-13.2) |
| Desktop (1440px) | Full layout — all pages (TC-13.3) |

**Check for each viewport**:
- No horizontal scroll
- Text readable without zooming
- Tap targets ≥ 44px
- Images (local and stock) scale appropriately
- Elevation charts fit viewport
- Tabs accessible (scroll if needed on mobile)

### Phase 8: Cross-Browser Testing (Manual)
**When**: After responsive testing
**How**: Open in each browser, run through core flow

| Browser | Priority |
|---------|----------|
| Chrome (latest) | Primary — most users |
| Safari (latest) | High — iPhone/Mac users on trail |
| Firefox (latest) | Medium |
| Edge (latest) | Medium |

**Core flow per browser**:
1. Page loads, hero renders (with stock photo)
2. Tab switching works
3. Day card expand/collapse works
4. Elevation chart renders
5. Gear checkboxes + localStorage
6. Dark mode toggle
7. Photo lightbox (with stock and local photos)

### Phase 9: Error Handling Testing (Manual)
**When**: After core functional tests pass
**How**: Deliberately break things

| Scenario | Expected Result |
|----------|----------------|
| Missing `trip-data.json` | Error message, not blank page (TC-3.3) |
| Missing elevation file | Affected day shows fallback, others work (TC-3.4) |
| Missing local photo files | Stock photo fallback or hidden (TC-8.2, TC-8.3) |
| Corrupt JSON (syntax error) | Error message, not crash |
| Empty `days` array | "No days to display" message |
| Unsplash rate limit hit | Photos hidden gracefully, no errors |

---

## Test Environment

- **Local server**: `python -m http.server 8000` or VS Code Live Server
- **Browsers**: Chrome, Safari, Firefox, Edge (latest versions)
- **Devices**: Desktop + Chrome DevTools device emulation for mobile/tablet
- **Real devices** (if available): iPhone for Safari mobile, Android for Chrome mobile
- **Network testing**: Chrome DevTools Network tab → toggle offline for no-internet tests

---

## Coverage Summary

| Area | Automated | Manual | Test Cases |
|------|-----------|--------|------------|
| Data validation | Yes | — | TC-1, TC-2 |
| Travel Guide App | — | Yes | TC-3 through TC-7 |
| Photo handling | — | Yes | TC-8 |
| Weather & Gear | — | Yes | TC-9, TC-10 |
| Lightbox & Dark mode | — | Yes | TC-11, TC-12 |
| Responsive | — | Yes | TC-13 |
| Photo Manager | — | Yes | TC-14 |
| GPX Data Processor | — | Yes | TC-15 |
| Trip Template | — | Yes | TC-16 |
| Cross-browser | — | Yes | (subset of all TCs) |
| Error handling | — | Yes | TC-3.3, TC-3.4, TC-8.3 |

---

## When to Re-Test

- After any change to `trip-data.json` → re-run Phase 1 (data validation)
- After any change to `index.html` → re-run Phases 2, 3, 7, 8
- After any change to `photos.html` → re-run Phase 4
- After any change to `gpx-tool.html` → re-run Phase 5
- After any change to `trip-template.md` → re-run Phase 6
- After adding a new trip folder → verify tools copied and footer links work (TC-15.13, TC-15.14)
- Before deployment → full regression (all phases)

---

## Definition of Done

All test phases pass:
- [ ] Data validation script runs clean
- [ ] All Travel Guide App test cases pass in Chrome
- [ ] Stock photo fallback works (online and offline graceful)
- [ ] Photo Manager drag-drop and zip export work
- [ ] GPX Data Processor parses files, shows comparisons, exports correctly
- [ ] GPX tool and Photo Manager available in all trip folders (WHW + Patagonia)
- [ ] Footer links work in all trips
- [ ] Trip template produces valid output from Claude.ai
- [ ] Responsive layout correct at all breakpoints
- [ ] Core flow works in Safari, Firefox, Edge
- [ ] Error handling scenarios handled gracefully
