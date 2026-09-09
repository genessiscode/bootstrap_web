# TravelEase - Bootstrap 5 Responsive Website

Hotel booking interface built with Bootstrap 5. Single-page responsive layout with navbar, feature cards, booking form, pricing table, and member responsibilities documentation.

## Project Structure
- `index.html`: Main responsive page (navbar, hero, cards, form, table, footer)
- `css/styles.css`: Custom styles — pill containers (50px radius), solid rgb backgrounds, Helvetica/Arial typography, brand blue (#2563eb) hover only, no glass/gradients
- `assets/`: Images, icons, Bootstrap vendor libraries
- `scripts/`: JavaScript functionality
- `member_roles.md`: 6-member team responsibilities (navbar/grid, cards/images, buttons/form, table/styling, UI/UX/design, testing/finalization)

## Design Specs
- Pill-shaped containers (50px border-radius)
- Solid rgb() backgrounds — no rgba glass, no gradients, no transforms on hover
- Helvetica/Arial sans-serif for codes/numeric text; no monospace
- Brand blue reserved for button hover state only
- No emojis; PNG icon assets preferred
- No cursor-following animations; no em-dashes

## Member Responsibilities (summary)
- Member 1: Responsive navbar + grid skeleton (4 links, container/row/col)
- Member 2: ≥3 cards + responsive images
- Member 3: 3+ button styles + booking form with validation
- Member 4: Room table with stripe/hover/bordered utilities
- Member 5: Alert/badge + approved visual language + creativity
- Member 6: Cross-device test (mobile/tablet/desktop), accessibility check, clean git, ZIP

## Bootstrap Components Used
Navbar, grid, cards, buttons, form, table (striped/hover/bordered/dark), alerts/badges, responsive images.

## How to Run
Open `index.html` in browser; test via Chrome DevTools device toolbar (mobile/tablet/desktop); verify navbar collapses, cards/images responsive, form validates, table reflows.

## Testing Notes
- Tested via `file://` protocol (no server required)
- Responsive across breakpoints: ≤992px navbar collapses; grid reflows via `.col-md`
- All DB data comes from backend (no hardcoded JS data)

## Expanded Details
Built for a travel/hotel booking course deliverable (ZIP: `hotel-booking-interface.zip`). All inline `style="..."` extracted to named CSS classes. Order/room IDs use Helvetica/Arial (not monospace). Images inside cards use `.img-fluid`. Form fields include `name` and `required`. Table includes price column formatted in sans-serif.
