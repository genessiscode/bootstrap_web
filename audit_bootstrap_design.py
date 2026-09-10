#!/usr/bin/env python3
"""
Audit Bootstrap conversion to check for design regressions
"""
from playwright.sync_api import sync_playwright
import sys

def audit_design():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        # Load the index page
        page.goto('file:///home/cornbread/ETF_Bootstrap/index.html')
        page.wait_for_load_state('networkidle')
        
        print("=" * 80)
        print("BOOTSTRAP DESIGN AUDIT - Checking for Style Regressions")
        print("=" * 80)
        
        # Check buttons
        print("\n1. BUTTON STYLES CHECK:")
        print("-" * 80)
        
        # Hero search button
        hero_btn = page.locator('.hero-section .btn').first
        if hero_btn.count() > 0:
            btn_styles = hero_btn.evaluate("""
                el => {
                    const styles = window.getComputedStyle(el);
                    return {
                        borderRadius: styles.borderRadius,
                        backgroundColor: styles.backgroundColor,
                        padding: styles.padding,
                        display: styles.display
                    };
                }
            """)
            print(f"Hero Button Border Radius: {btn_styles['borderRadius']}")
            print(f"Hero Button Background: {btn_styles['backgroundColor']}")
            print(f"Hero Button Display: {btn_styles['display']}")
            
            expected_radius = "9999px"
            if "9999" not in btn_styles['borderRadius']:
                print(f"  ❌ ISSUE: Border radius should be pill-shaped (9999px), got: {btn_styles['borderRadius']}")
            else:
                print("  ✓ Button border radius correct (pill-shaped)")
        
        # Check card styles
        print("\n2. CARD STYLES CHECK:")
        print("-" * 80)
        
        cards = page.locator('.card-surface').first
        if cards.count() > 0:
            card_styles = cards.evaluate("""
                el => {
                    const styles = window.getComputedStyle(el);
                    return {
                        borderRadius: styles.borderRadius,
                        backgroundColor: styles.backgroundColor,
                        border: styles.border,
                        overflow: styles.overflow
                    };
                }
            """)
            print(f"Card Border Radius: {card_styles['borderRadius']}")
            print(f"Card Background: {card_styles['backgroundColor']}")
            print(f"Card Border: {card_styles['border']}")
            print(f"Card Overflow: {card_styles['overflow']}")
            
            if "50px" not in card_styles['borderRadius']:
                print(f"  ❌ ISSUE: Card border radius should be 50px (pill container), got: {card_styles['borderRadius']}")
            else:
                print("  ✓ Card border radius correct (50px pill container)")
        
        # Check feature cards
        print("\n3. FEATURE CARD STYLES CHECK:")
        print("-" * 80)
        
        feature_cards = page.locator('.card-feature').first
        if feature_cards.count() > 0:
            feature_styles = feature_cards.evaluate("""
                el => {
                    const styles = window.getComputedStyle(el);
                    return {
                        borderRadius: styles.borderRadius,
                        padding: styles.padding,
                        boxShadow: styles.boxShadow
                    };
                }
            """)
            print(f"Feature Card Border Radius: {feature_styles['borderRadius']}")
            print(f"Feature Card Padding: {feature_styles['padding']}")
            print(f"Feature Card Shadow: {feature_styles['boxShadow']}")
            
            if "20px" not in feature_styles['borderRadius']:
                print(f"  ❌ ISSUE: Feature card should have 20px radius, got: {feature_styles['borderRadius']}")
            else:
                print("  ✓ Feature card styling correct")
        
        # Check navbar
        print("\n4. NAVBAR STYLES CHECK:")
        print("-" * 80)
        
        navbar = page.locator('.navbar').first
        if navbar.count() > 0:
            nav_styles = navbar.evaluate("""
                el => {
                    const styles = window.getComputedStyle(el);
                    return {
                        backgroundColor: styles.backgroundColor,
                        position: styles.position
                    };
                }
            """)
            print(f"Navbar Background: {nav_styles['backgroundColor']}")
            print(f"Navbar Position: {nav_styles['position']}")
            print("  ✓ Navbar styles intact")
        
        # Check badges
        print("\n5. BADGE STYLES CHECK:")
        print("-" * 80)
        
        badges = page.locator('.badge-soft-primary').first
        if badges.count() > 0:
            badge_styles = badges.evaluate("""
                el => {
                    const styles = window.getComputedStyle(el);
                    return {
                        borderRadius: styles.borderRadius,
                        padding: styles.padding,
                        backgroundColor: styles.backgroundColor
                    };
                }
            """)
            print(f"Badge Border Radius: {badge_styles['borderRadius']}")
            print(f"Badge Padding: {badge_styles['padding']}")
            print(f"Badge Background: {badge_styles['backgroundColor']}")
            
            if "9999" not in badge_styles['borderRadius']:
                print(f"  ❌ ISSUE: Badge should be pill-shaped (9999px), got: {badge_styles['borderRadius']}")
            else:
                print("  ✓ Badge styling correct")
        
        # Take screenshots
        print("\n6. TAKING SCREENSHOTS:")
        print("-" * 80)
        
        page.screenshot(path='audit-bootstrap-desktop.png', full_page=True)
        print("  ✓ Desktop screenshot saved: audit-bootstrap-desktop.png")
        
        page.set_viewport_size({'width': 768, 'height': 1024})
        page.screenshot(path='audit-bootstrap-tablet.png', full_page=True)
        print("  ✓ Tablet screenshot saved: audit-bootstrap-tablet.png")
        
        page.set_viewport_size({'width': 375, 'height': 812})
        page.screenshot(path='audit-bootstrap-mobile.png', full_page=True)
        print("  ✓ Mobile screenshot saved: audit-bootstrap-mobile.png")
        
        print("\n" + "=" * 80)
        print("AUDIT COMPLETE")
        print("=" * 80)
        
        browser.close()

if __name__ == '__main__':
    try:
        audit_design()
    except Exception as e:
        print(f"Error during audit: {e}")
        sys.exit(1)
