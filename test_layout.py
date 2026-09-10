#!/usr/bin/env python3
"""
Playwright DOM audit for TravelPearl index.html layout verification.
Checks: carousel indicator positioning, image overlaps, search bar placement, responsive behavior.
"""
from playwright.sync_api import sync_playwright

checks_js = """() => {
  const results = {};
  
  // 1. Search bar position relative to badges
  const searchBar = document.querySelector('.input-group');
  const trustBadges = document.querySelector('.d-flex.justify-content-center.flex-wrap.gap-2');
  if (searchBar && trustBadges) {
    const searchRect = searchBar.getBoundingClientRect();
    const badgesRect = trustBadges.getBoundingClientRect();
    results.searchBarAboveBadges = searchRect.bottom < badgesRect.top;
    results.searchBarBottom = Math.round(searchRect.bottom);
    results.badgesTop = Math.round(badgesRect.top);
    results.gap = Math.round(badgesRect.top - searchRect.bottom);
  }
  
  // 2. Carousel indicators positioning relative to images
  const indicators = document.querySelector('.carousel-indicators');
  const carouselImages = document.querySelectorAll('.carousel-image');
  if (indicators && carouselImages.length > 0) {
    const indicatorsRect = indicators.getBoundingClientRect();
    const lastImage = carouselImages[carouselImages.length - 1];
    const imageRect = lastImage.getBoundingClientRect();
    results.indicatorsTop = Math.round(indicatorsRect.top);
    results.lastImageBottom = Math.round(imageRect.bottom);
    results.indicatorsOverlapImages = indicatorsRect.top < imageRect.bottom;
    results.clearance = Math.round(indicatorsRect.top - imageRect.bottom);
  }
  
  // 3. Search icon size
  const searchIcon = document.querySelector('.search-icon');
  if (searchIcon) {
    results.searchIconSize = {
      rendered: { w: searchIcon.offsetWidth, h: searchIcon.offsetHeight },
      natural: { w: searchIcon.naturalWidth, h: searchIcon.naturalHeight }
    };
  }
  
  // 4. Feature icons size
  const featureIcons = document.querySelectorAll('.feature-icon-sm');
  if (featureIcons.length > 0) {
    const first = featureIcons[0];
    results.featureIconSmSize = {
      rendered: { w: first.offsetWidth, h: first.offsetHeight },
      natural: { w: first.naturalWidth, h: first.naturalHeight }
    };
  }
  
  // 5. Search bar height
  if (searchBar) {
    results.searchBarHeight = Math.round(searchBar.getBoundingClientRect().height);
  }
  
  // 6. Carousel container dimensions and cards per row
  const carouselContainer = document.querySelector('.carousel-container');
  const carouselGroup = document.querySelector('.carousel-group');
  if (carouselContainer) {
    const rect = carouselContainer.getBoundingClientRect();
    results.carouselContainer = {
      width: Math.round(rect.width),
      height: Math.round(rect.height)
    };
  }
  if (carouselGroup) {
    const computedStyle = window.getComputedStyle(carouselGroup);
    results.carouselGridColumns = computedStyle.gridTemplateColumns;
    const cards = carouselGroup.querySelectorAll('.carousel-card');
    results.carouselCardsCount = cards.length;
  }
  
  // 7. Hamburger menu visibility
  const toggler = document.querySelector('.navbar-toggler');
  if (toggler) {
    results.hamburgerVisible = window.getComputedStyle(toggler).display !== 'none';
  }
  
  // 8. Hero section padding
  const heroSection = document.querySelector('.hero-section');
  if (heroSection) {
    const cs = window.getComputedStyle(heroSection);
    results.heroPadding = {
      top: cs.paddingTop,
      bottom: cs.paddingBottom
    };
  }
  
  return results;
}"""

url = "file:///home/cornbread/ETF_Bootstrap/index.html"

print("TravelPearl Layout Audit")
print("=" * 60)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    viewports = [
        ("Desktop", 1440, 900),
        ("Tablet", 768, 1024),
        ("Mobile", 375, 812)
    ]
    
    for name, width, height in viewports:
        print(f"\n{name} ({width}x{height})")
        print("-" * 60)
        
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(800)  # Allow carousel/animations to settle
        
        result = page.evaluate(checks_js)
        
        # Search bar position
        if 'searchBarAboveBadges' in result:
            status = "✓ PASS" if result['searchBarAboveBadges'] else "✗ FAIL"
            print(f"Search bar above badges: {status}")
            print(f"  Search bottom: {result.get('searchBarBottom')}px")
            print(f"  Badges top: {result.get('badgesTop')}px")
            print(f"  Gap: {result.get('gap')}px")
        
        # Carousel indicators
        if 'indicatorsOverlapImages' in result:
            overlap = result['indicatorsOverlapImages']
            status = "✗ OVERLAP" if overlap else "✓ CLEAR"
            print(f"\nCarousel indicators: {status}")
            print(f"  Last image bottom: {result.get('lastImageBottom')}px")
            print(f"  Indicators top: {result.get('indicatorsTop')}px")
            print(f"  Clearance: {result.get('clearance')}px")
        
        # Search icon sizing
        if 'searchIconSize' in result:
            icon = result['searchIconSize']
            print(f"\nSearch icon:")
            print(f"  Rendered: {icon['rendered']['w']}x{icon['rendered']['h']}px")
            print(f"  Natural: {icon['natural']['w']}x{icon['natural']['h']}px")
        
        # Feature icon sizing
        if 'featureIconSmSize' in result:
            icon = result['featureIconSmSize']
            print(f"\nFeature icon (small):")
            print(f"  Rendered: {icon['rendered']['w']}x{icon['rendered']['h']}px")
            print(f"  Natural: {icon['natural']['w']}x{icon['natural']['h']}px")
        
        # Search bar height
        if 'searchBarHeight' in result:
            height_val = result['searchBarHeight']
            status = "✓" if 40 <= height_val <= 60 else "⚠"
            print(f"\nSearch bar height: {height_val}px {status}")
        
        # Hamburger visibility
        if 'hamburgerVisible' in result:
            visible = result['hamburgerVisible']
            expected = name in ["Tablet", "Mobile"]
            status = "✓" if visible == expected else "✗"
            print(f"\nHamburger menu visible: {visible} {status}")
        
        # Carousel grid columns
        if 'carouselGridColumns' in result:
            grid = result['carouselGridColumns']
            cards = result.get('carouselCardsCount', 0)
            print(f"\nCarousel grid layout:")
            print(f"  Grid template: {grid}")
            print(f"  Cards in first group: {cards}")
        
        # Screenshot
        screenshot_path = f"screenshot_{name.lower()}.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"\nScreenshot: {screenshot_path}")
        
        page.close()
    
    browser.close()

print("\n" + "=" * 60)
print("Audit complete")
