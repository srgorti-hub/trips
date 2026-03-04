# Concept — Travel Guide Generator

## What It Is
A simple system for turning a trip idea into a polished, shareable travel guide. You describe your trip to Claude.ai, it researches and generates structured content, and a static web page turns that content into a beautiful guide you share with your travel group via URL.

## Why It Exists
Planning a group trip means scattered information: trail details, accommodation options, gear lists, weather expectations, travel logistics. This system brings it all together into a single, mobile-friendly resource that every participant can access — no app install, no login.

Currently, organizers cobble together Google Docs, email threads, and WhatsApp messages. This replaces all of that with: **talk to AI → get a travel guide → share the link**.

## Who It's For

### Primary: Trip Organizer
- Plans group trips (hiking, trekking, active travel)
- Has a rough itinerary (verbal description, notes, or spreadsheet)
- Wants a professional-looking guide without design skills
- Has a Claude.ai account

### Secondary: Trip Participants
- Receive a URL to the published travel guide
- Use it before the trip (planning, gear prep) and during the trip (daily reference)
- Mobile-friendly, no login, no app install

## How It Works

### Step 1: Generate content with Claude.ai
- Open Claude.ai, upload `trip-template.md` and your itinerary (spreadsheet, notes, or just describe it)
- Claude researches your route and generates `trip-data.json` and `elevation/day-N-profile.json` files with day-by-day details, trail info, elevation data, weather, gear lists, and more

### Step 2: Add photos (optional)
- Open `photos.html` in your browser
- Drag and drop your own photos, organized by day
- If you skip this, the guide automatically uses free stock photos based on your locations

### Step 3: Share the guide
- Drop the generated files into the travel guide folder
- Deploy to GitHub Pages (or any static host)
- Share the URL with your group

## What the Guide Includes
- Trip overview and summary
- Day-by-day itinerary with descriptions, distances, difficulty
- **Elevation profile charts** for each day (SVG, interactive — a first-class visual element)
- Trail details and waypoints
- How to prepare (weather, conditions, tips)
- Gear checklist (interactive, saves progress)
- Photos (your own or auto-fetched stock photos)

## Companion Tools (per trip)
Each trip folder includes two companion tools accessible via footer links in the guide:
- **Photo Manager** (`photos.html`) — Drag-and-drop photo organizer for assigning images to days
- **GPX Data Processor** (`gpx-tool.html`) — Drop GPX files per day to generate accurate elevation profiles and distance/ascent stats from real GPS data, replacing estimated values

## Core Value Proposition
- **For the organizer**: Describe your trip → AI does the research → polished guide in minutes
- **For participants**: One URL, all the info, works on any phone

## Design Philosophy
- Clean, card-based layout — AllTrails meets Notion
- **Responsive** — looks great on desktop browsers and mobile phones alike
- Mobile-optimized — usable on the trail
- Data-rich but not cluttered
- Elevation charts are first-class visual elements, not afterthoughts
- Photos enhance context, not decoration

## Technical Philosophy
- Vanilla HTML/CSS/JS — no frameworks, no build tools
- Static files only — no server, no database
- Stock photos fetched from free APIs (Unsplash) when organizer doesn't provide their own
- Portable — the entire trip is a folder that can be zipped, shared, or hosted anywhere

## Deliverables

| File | Location | Purpose |
|------|----------|---------|
| `trip-template.md` | Project root | Upload to Claude.ai with your itinerary — tells Claude how to generate the JSON and elevation data |
| `index.html` | Each trip folder | Travel guide — reads `trip-data.json`, renders elevation charts, fetches stock photos |
| `photos.html` | Each trip folder | Drag-and-drop page to organize your own photos into the right day folders |
| `gpx-tool.html` | Each trip folder | GPX processor — drop GPX files to generate accurate stats and elevation profiles from real GPS data |
| `README.md` | WHW folder | End-to-end workflow instructions |

All three HTML tools (`index.html`, `photos.html`, `gpx-tool.html`) are trip-agnostic — they read `trip-data.json` from their own folder. When creating a new trip, copy all three into the trip folder alongside the generated data files.
