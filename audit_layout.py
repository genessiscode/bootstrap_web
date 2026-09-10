from playwright.sync_api import sync_playwright
import json

CHECKS_JS = r"""
() => {
  const r = {};
  const carouselImgs = document.querySelectorAll('#carouselExampleIndicators .carousel-item img');
  r.carouselImages = Array.from(carouselImgs).map(img => ({
    src: img.src.split('/').pop(),
    rendered: {w: img.offsetWidth, h: img.offsetHeight},
    natural: {w: img.naturalWidth, h: img.naturalHeight},
    complete: img.complete,
    broken: img.complete && img.naturalWidth === 0
  }));
  const ig = document.querySelector('.hero-section .input-group');
  r.heroInputGroup = ig ? {
    height: ig.offsetHeight,
    children: Array.from(ig.children).map(c => ({
      tag: c.tagName,
      className: c.className,
      height: c.offsetHeight,
      width: c.offsetWidth
    }))
  } : null;
  const icons = document.querySelectorAll('.hero-section img[src*="assets/icons"]');
  r.heroIcons = Array.from(icons).map(img => ({
    src: img.src.split('/').pop(),
    rendered: {w: img.offsetWidth, h: img.offsetHeight},
    natural: {w: img.naturalWidth, h: img.naturalHeight},
    complete: img.complete,
    broken: img.complete && img.naturalWidth === 0
  }));
  const body = document.body;
  r.overflow = body.scrollWidth > window.innerWidth;
  const navbar = document.querySelector('nav.navbar');
  r.navbar = navbar ? {
    height: navbar.offsetHeight,
    position: window.getComputedStyle(navbar).position,
    top: window.getComputedStyle(navbar).top
  } : null;
  const hero = document.querySelector('header.hero-section');
  r.heroOffsetTop = hero ? hero.offsetTop : null;
  const carousel = document.querySelector('#carouselExampleIndicators');
  r.carousel = carousel ? {
    rendered: {w: carousel.offsetWidth, h: carousel.offsetHeight},
    imageDisplay: window.getComputedStyle(document.querySelector('#carouselExampleIndicators .carousel-item img')).display,
    width: window.getComputedStyle(document.querySelector('#carouselExampleIndicators .carousel-item img')).width
  } : null;
  return r;
}
""";

def main():
    url = "file:///home/cornbread/ETF_Bootstrap/index.html"
    results = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for vw, vh, label in [(1440, 900, "desktop"), (768, 1024, "tablet"), (375, 812, "mobile")]:
            page = browser.new_page(viewport={"width": vw, "height": vh})
            page.goto(url, wait_until="networkidle")
            page.wait_for_timeout(500)
            result = page.evaluate(CHECKS_JS)
            results[f"index-{label}"] = result
            page.screenshot(path=f"audit-index-{label}.png", full_page=True)
            page.close()
        browser.close()
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
