"""Take full-page screenshots at desktop, tablet, and mobile widths."""
from playwright.sync_api import sync_playwright
import os

BASE = "/home/cornbread/ETF_Bootstrap"
URL = f"file://{BASE}/index.html"

viewports = [
    ("desktop",  1440, 900),
    ("tablet",   768,  1024),
    ("mobile",   375,  812),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for name, w, h in viewports:
        page = browser.new_page(viewport={"width": w, "height": h})
        page.goto(URL, wait_until="networkidle")
        page.wait_for_timeout(500)  # let any CSS settle
        out = os.path.join(BASE, f"screenshot-{name}.png")
        page.screenshot(path=out, full_page=True)
        print(f"Saved {out}  ({w}x{h})")
        page.close()
    browser.close()
