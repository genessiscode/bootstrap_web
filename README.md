# TravelEase - Bootstrap 5 Responsive Website

Website frontend using Bootstrap 5 for hotel booking interface.

## Project Structure
- `index.html`: Main HTML file
- `css/styles.css`: Custom CSS with design specifications
- `scripts/scripts.js`: JavaScript functionality
- `assets/`: Images, icons, and other assets
- `member_roles.md`: Team member responsibilities

## Member Responsibilities


**Project:** Responsive Bootstrap 5 website for a travel/hotel booking interface  
**Team:** 6 members  
**Deliverable:** One ZIP containing all HTML, CSS, JS, Bootstrap, and image files

---

## Member responsibilities (≈ 3‑4 marks each)

| Member | Core component (2 marks) | Supporting task (1‑2 marks) |
|--------|--------------------------|-----------------------------|
| **1** | **Navbar & responsive grid skeleton** – build a responsive Bootstrap navbar with at least 4 links and the basic container/row/column layout that will power the home page (covers the 2‑mark navbar requirement and part of the 4‑mark grid requirement). | — |
| **2** | **Cards** – create at least 3 cards presenting hotel features, amenities, or testimonials (2‑mark requirement). | **Image handling** – ensure images inside cards are responsive, thumbnail‑styled, and properly aligned (2‑mark requirement). |
| **3** | **Button styles** – demonstrate at least 3 different Bootstrap button styles (primary, success, danger, etc.) with meaningful purposes (2‑mark requirement). | **Booking form** – develop a functional‑looking form with ≥ 3 controls (e.g., check‑in date, check‑out date, number of guests) and basic client‑side validation (2‑mark requirement). |
| **4** | **Table** – build a table showing room types, pricing, and availability (2‑mark requirement). | **Table styling** – apply at least two Bootstrap table utilities (e.g., striped + hover, or bordered + responsive) and make the table responsive on narrow screens (2‑mark requirement). |
| **5** | **UI/UX & alerts/badges** – add at least one Bootstrap alert or badge for messages/ratings (1‑mark requirement). | **Design style** – apply the group‑approved visual language: pill‑shaped containers (50 px border‑radius), solid `rgb()` backgrounds (no rgba glass, no gradients), Helvetica/Arial sans‑serif for order IDs and numeric text, brand‑blue **only** for button hover state, no hover lifts/fades/transforms. Also add creative layout touches that raise the overall presentation (3‑marks “UI/UX, Creativity & Code Organization”). |
| **6** | **Testing & finalization** – test the completed site on mobile, tablet, and desktop browsers; verify that the navbar collapses, the grid reflows, cards, buttons, form, and table all work. | **Polish & submission** – fix any responsiveness bugs, run a quick accessibility check, add inline comments to HTML/CSS, organize the project folder (partials/, assets/, etc.), and create the final ZIP for submission (covers the remaining “code organization” marks and ensures the group can run the site from the main HTML file). |

### Quick checklist per member

- **Member 1:** Navbar collapses into a hamburger on ≤ 992px; grid uses `.container`, `.row`, `.col-{sm,md}`.  
- **Member 2:** ≥ 3 cards, each with an `.img-fluid` image, `.card-title`, `.card-text`.  
- **Member 3:** Buttons use `.btn .btn-primary` etc.; form fields have `name` attributes and `required` where appropriate.  
- **Member 4:** Table with `.table .table-striped` or `.table .table-hover`; column for “Price” formatted in Helvetica/Arial.  
- **Member 5:** Alert `.alert .alert-info` or `.badge` placed strategically; all backgrounds `background: rgb(240,240,240)` (example); no `box-shadow` or `transform` on hover.  
- **Member 6:** Run `chrome DevTools → Toggle device toolbar` on phone, tablet, laptop; commit a clean `git` repo; zip the folder as `hotel-booking-interface.zip`.

---

*All members should keep their code well‑commented and follow the project’s file‑naming conventions (e.g., `index.html`, `styles.css`, `scripts.js`, `images/…`).*## Design Specifications
- Pill-shaped containers with 50px border-radius
- Solid rgb() backgrounds (no gradients or glassmorphism)
- Helvetica/Arial sans-serif typography (no monospace)
- Brand blue (#2563eb) only for button hover state
- No emojis, no gradients, no glassmorphism effects
- No cursor-following beam animations
- No em-dashes or inconsistent spacing
- All text in plain, readable format without robotic phrasing

## How to Run
1. Open index.html in any modern browser
2. Test on different screen sizes using Chrome DevTools
3. Verify all interactive elements function properly
4. Compress the project folder into ZIP for submission

## Bootstrap Components Used
- Navbar (responsive)
- Grid system (container, row, col)
- Cards (feature and room cards)
- Buttons (primary, success, outline styles)
- Forms (email and booking forms)
- Tables (striped, hover, bordered, dark)
- Alerts and badges
- Responsive images