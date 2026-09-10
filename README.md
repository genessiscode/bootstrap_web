# TravelPearl - Bootstrap 5 Responsive Website

A premier Sri Lanka travel and hospitality interface built with Bootstrap 5.3.3. Designed with a clean, high-contrast visual architecture featuring soft canvas tones, rounded container surfaces, consistent typography, robust client-side validation, and zero external dependencies.

## Project Structure
- `index.html`: Master landing page (Hero search, 4 feature pillars, accommodations, destinations, pricing matrix table, booking request form, guest reviews, FAQ accordion)
- `services.html`: Dedicated travel & hospitality services hub (6 core services, 3-tier hospitality packages, custom itinerary CTA, service FAQ)
- `about.html`: Corporate journey & brand heritage (Story & mission, 4 foundational pillars, chronological milestones, executive leadership team)
- `blogs.html`: Sri Lanka travel guides portal (Featured long-form editorial showcase, 6-topic travel guides matrix)
- `blog_read.html`: Long-form travel guide reading template (Top 5 Pristine Beaches in Sri Lanka, seasonal comparison table, travel alert)
- `contact.html`: Island concierge & support hub (3 regional operational desks, comprehensive travel inquiry form, guarantees sidebar, FAQ)
- `member1.html` to `member6.html`: Dedicated team member profiles documenting individual coursework roles and technical implementations
- `css/styles.css`: Central stylesheet containing global design tokens, typography rules, card surfaces, button systems, and component styles
- `scripts/scripts.js`: Universal client-side JavaScript logic (Bootstrap 5 validation, alert dismissals, interactive triggers)
- `assets/vendor/bootstrap/`: Localized Bootstrap 5.3.3 CSS and bundled JavaScript (zero CDN dependencies)
- `assets/images/` & `assets/icons/`: Local SVG graphics and PNG icon assets

## Design Specifications & Standards
- **Color Palette & Tokens:** Modern high-contrast system with deep indigo primary (`#533afd`), deep ink text (`#0d253d`), subtle canvas background (`#f6f9fc`), and crisp neutral borders (`#e3e8ee`).
- **Surface Elevation:** 20px card border radii with subtle multidimensional drop shadows (`0 1px 3px rgba(13, 37, 61, 0.04), 0 6px 16px rgba(13, 37, 61, 0.03)`).
- **Typography:** Unified Helvetica Neue / Arial sans-serif font stack applied across all body copy, headings, buttons, and form inputs.
- **Button Styling:** Pill-shaped (`border-radius: 9999px`) solid action buttons (`.btn-action-primary`, `.btn-action-secondary`, `.btn-action-light`) maintaining single button colors per section.
- **Self-Contained:** 100% local assets with zero external font, script, or stylesheet CDN dependencies.

## Team Member Responsibilities
- **Member 1 (Kasun Chiwantha):** Lead Page Editor & Master Landing Page Architect — Main Landing Page (`index.html`), Global Design Tokens (`css/styles.css`), Typography, and Grid Consistency.
- **Member 2 (Sanuk Jayathunga):** Hospitality & Services Portfolio Architect — Services Hub (`services.html`), 6 Core Service Cards, 3-Tier Hospitality Pricing Architecture, and Feature Matrices.
- **Member 3 (Vijayarengar Hemakesh):** Narrative, Heritage & Corporate Identity Architect — About Page (`about.html`), Story & Mission, Four Foundational Pillars, and Organizational Milestones.
- **Member 4 (Umar Luqman):** Content Discovery & Editorial Hub Architect — Travel Guides Portal (`blogs.html`), Featured Story Showcase, 6-Topic Guide Grid.
- **Member 5 (Kaveesha Nawod):** Long-Form Reader Experience & Article UX Architect — Inner Blog Reading Template (`blog_read.html`), Seasonality Matrix, Pull Quotes, Safety Advisories.
- **Member 6 (Eranda Sandeep):** Concierge Hub & Form Validation Architect — Contact Hub (`contact.html`), Regional Desks, Form Validation Logic (`scripts/scripts.js`).

## How to Test & Run
1. Open any HTML file (e.g. `index.html`, `services.html`) directly in any web browser (`file://` protocol supported).
2. Test responsive breakpoints across mobile (375px), tablet (768px), and desktop (1440px) via browser DevTools.
3. Run test suites:
   - `python3 audit.py`: Audits layout spacing, icon scaling, and component bounding boxes.
   - `python3 check_spacing.py`: Validates navbar height and fixed-top offset clearances.
   - `node verify-layout.js`: Playwright automated responsive screenshot generator.
