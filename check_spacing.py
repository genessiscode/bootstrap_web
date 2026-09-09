"""Check navbar bottom vs hero heading top to verify spacing."""
from playwright.sync_api import sync_playwright
import json

BASE = "/home/cornbread/ETF_Bootstrap"
URL = f"file://{BASE}/index.html"

check_js = """() => {
  const nav = document.querySelector('.navbar');
  const hero = document.querySelector('.hero-section');
  const h1 = document.querySelector('.hero-section h1');
  const navRect = nav.getBoundingClientRect();
  const heroRect = hero.getBoundingClientRect();
  const h1Rect = h1.getBoundingClientRect();

  // Check contact headings color
  const contactH5s = document.querySelectorAll('#contact h5');
  const h5Colors = Array.from(contactH5s).map(el => ({
    text: el.textContent,
    color: window.getComputedStyle(el).color,
  }));

  return {
    navbarBottom: Math.round(navRect.bottom),
    heroTop: Math.round(heroRect.top),
    headingTop: Math.round(h1Rect.top),
    gapNavToHeading: Math.round(h1Rect.top - navRect.bottom),
    contactH5Colors: h5Colors,
  };
}"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for name, w, h in [("desktop", 1440, 900), ("mobile", 375, 812)]:
        page = browser.new_page(viewport={"width": w, "height": h})
        page.goto(URL, wait_until="networkidle")
        page.wait_for_timeout(300)
        result = page.evaluate(check_js)
        print(f"\n{name.upper()} ({w}x{h}):")
        print(json.dumps(result, indent=2))
        page.close()
    browser.close()
