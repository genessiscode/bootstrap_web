"""Audit the rendered layout at desktop/tablet/mobile — check icon sizes,
card alignment, search bar, table, and general spacing via DOM queries."""
from playwright.sync_api import sync_playwright
import json, os

BASE = "/home/cornbread/ETF_Bootstrap"
URL = f"file://{BASE}/index.html"

viewports = [
    ("desktop",  1440, 900),
    ("tablet",   768,  1024),
    ("mobile",   375,  812),
]

checks_js = """() => {
  const r = {};

  // 1. Feature icons (48x48 CSS)
  const featureIcons = document.querySelectorAll('.feature-icon');
  r.featureIcons = Array.from(featureIcons).map(el => ({
    src: el.src.split('/').pop(),
    rendered: { w: el.offsetWidth, h: el.offsetHeight },
    natural: { w: el.naturalWidth, h: el.naturalHeight },
  }));

  // 2. Feature-icon-sm (24x24 CSS)
  const smIcons = document.querySelectorAll('.feature-icon-sm');
  r.smallIcons = Array.from(smIcons).map(el => ({
    src: el.src.split('/').pop(),
    rendered: { w: el.offsetWidth, h: el.offsetHeight },
    natural: { w: el.naturalWidth, h: el.naturalHeight },
  }));

  // 3. Search icon
  const searchIcon = document.querySelector('.search-icon');
  if (searchIcon) {
    r.searchIcon = {
      rendered: { w: searchIcon.offsetWidth, h: searchIcon.offsetHeight },
      natural: { w: searchIcon.naturalWidth, h: searchIcon.naturalHeight },
    };
  }

  // 4. Feature cards (check if same row)
  const featureCards = document.querySelectorAll('.card-feature');
  r.featureCards = Array.from(featureCards).map(el => {
    const rect = el.getBoundingClientRect();
    return { top: Math.round(rect.top), left: Math.round(rect.left), w: Math.round(rect.width), h: Math.round(rect.height) };
  });

  // 5. Room cards
  const roomCards = document.querySelectorAll('#rooms .card');
  r.roomCards = Array.from(roomCards).map(el => {
    const rect = el.getBoundingClientRect();
    const img = el.querySelector('img');
    return {
      top: Math.round(rect.top), left: Math.round(rect.left),
      w: Math.round(rect.width), h: Math.round(rect.height),
      imgLoaded: img ? (img.naturalWidth > 0) : false,
      imgRendered: img ? { w: img.offsetWidth, h: img.offsetHeight } : null,
    };
  });

  // 6. Table
  const table = document.querySelector('.table');
  if (table) {
    const rect = table.getBoundingClientRect();
    r.table = { w: Math.round(rect.width), h: Math.round(rect.height), overflow: rect.width > window.innerWidth };
  }

  // 7. Search bar
  const inputGroup = document.querySelector('.hero-section .input-group');
  if (inputGroup) {
    const rect = inputGroup.getBoundingClientRect();
    r.searchBar = { w: Math.round(rect.width), h: Math.round(rect.height) };
  }

  // 8. Navbar toggler visibility
  const toggler = document.querySelector('.navbar-toggler');
  if (toggler) {
    const style = window.getComputedStyle(toggler);
    r.hamburger = { display: style.display, visible: style.display !== 'none' };
  }

  // 9. Page total height
  r.pageHeight = document.documentElement.scrollHeight;
  r.viewportWidth = window.innerWidth;

  return r;
}"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for name, w, h in viewports:
        page = browser.new_page(viewport={"width": w, "height": h})
        page.goto(URL, wait_until="networkidle")
        page.wait_for_timeout(500)
        result = page.evaluate(checks_js)
        print(f"\n{'='*60}")
        print(f"  {name.upper()} ({w}x{h})")
        print(f"{'='*60}")
        print(json.dumps(result, indent=2))
        page.close()
    browser.close()
