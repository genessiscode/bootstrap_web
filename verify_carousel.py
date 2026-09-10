#!/usr/bin/env python3
"""
Quick verification: Carousel cards visible per viewport
"""
from playwright.sync_api import sync_playwright

verify_js = """() => {
  const track = document.querySelector('.carousel-track');
  const viewport = document.querySelector('.carousel-viewport');
  const cards = track.querySelectorAll('.carousel-card');
  
  const viewportWidth = viewport.offsetWidth;
  const cardStyle = window.getComputedStyle(cards[0]);
  const cardFlexBasis = cardStyle.flexBasis;
  
  // Count visible cards based on flex-basis
  let visibleCount = 0;
  if (cardFlexBasis.includes('100%')) {
    visibleCount = 1;
  } else if (cardFlexBasis.includes('33.333%') || cardFlexBasis.includes('calc(33')) {
    visibleCount = 3;
  } else if (cardFlexBasis.includes('25%') || cardFlexBasis.includes('calc(25')) {
    visibleCount = 4;
  }
  
  return {
    totalCards: cards.length,
    cardFlexBasis: cardFlexBasis,
    visibleCardsPerSlide: visibleCount,
    viewportWidth: Math.round(viewportWidth)
  };
}"""

url = "file:///home/cornbread/ETF_Bootstrap/index.html"

print("Carousel Responsive Verification")
print("=" * 50)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    tests = [
        ("Desktop", 1440, 900, 4),
        ("Tablet", 900, 1024, 3),
        ("Mobile", 375, 812, 1)
    ]
    
    all_passed = True
    
    for name, width, height, expected in tests:
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(500)
        
        result = page.evaluate(verify_js)
        
        visible = result['visibleCardsPerSlide']
        status = "✓ PASS" if visible == expected else "✗ FAIL"
        
        if visible != expected:
            all_passed = False
        
        print(f"\n{name} ({width}x{height})")
        print(f"  Expected: {expected} cards per slide")
        print(f"  Actual: {visible} cards per slide")
        print(f"  Flex basis: {result['cardFlexBasis']}")
        print(f"  Status: {status}")
        
        page.close()
    
    browser.close()
    
    print("\n" + "=" * 50)
    if all_passed:
        print("✓ All tests PASSED!")
    else:
        print("✗ Some tests FAILED")
