#!/usr/bin/env python3
"""
Detailed style audit - checks all elements for correct styling
"""
from playwright.sync_api import sync_playwright

def detailed_audit():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        page.goto('file:///home/cornbread/ETF_Bootstrap/index.html')
        page.wait_for_load_state('networkidle')
        
        print("\n" + "=" * 80)
        print("DETAILED STYLE AUDIT - Checking computed styles")
        print("=" * 80)
        
        issues = []
        
        # Check all buttons
        print("\n1. ALL BUTTONS CHECK:")
        print("-" * 80)
        buttons = page.locator('.btn').all()
        print(f"Found {len(buttons)} buttons")
        
        for i, btn in enumerate(buttons[:5]):  # Check first 5
            styles = btn.evaluate("""
                el => {
                    const cs = window.getComputedStyle(el);
                    return {
                        bg: cs.backgroundColor,
                        color: cs.color,
                        borderRadius: cs.borderRadius,
                        padding: cs.padding,
                        border: cs.border,
                        text: el.textContent.trim().substring(0, 30)
                    };
                }
            """)
            print(f"\nButton {i+1}: '{styles['text']}'")
            print(f"  Background: {styles['bg']}")
            print(f"  Color: {styles['color']}")
            print(f"  Border Radius: {styles['borderRadius']}")
            print(f"  Padding: {styles['padding']}")
            
            # Check if primary button has correct background
            if 'btn-primary' in btn.get_attribute('class') or 'btn-action-primary' in btn.get_attribute('class'):
                if styles['bg'] == 'rgba(0, 0, 0, 0)' or styles['bg'] == 'transparent':
                    issues.append(f"Button '{styles['text']}' has transparent background - should be primary color")
        
        # Check all cards
        print("\n\n2. ALL CARDS CHECK:")
        print("-" * 80)
        cards = page.locator('.card, .card-surface, .card-feature').all()
        print(f"Found {len(cards)} cards")
        
        for i, card in enumerate(cards[:5]):  # Check first 5
            styles = card.evaluate("""
                el => {
                    const cs = window.getComputedStyle(el);
                    return {
                        bg: cs.backgroundColor,
                        border: cs.border,
                        borderRadius: cs.borderRadius,
                        boxShadow: cs.boxShadow
                    };
                }
            """)
            print(f"\nCard {i+1}:")
            print(f"  Background: {styles['bg']}")
            print(f"  Border: {styles['border']}")
            print(f"  Border Radius: {styles['borderRadius']}")
            print(f"  Box Shadow: {styles['boxShadow'][:80]}...")
            
            if styles['bg'] == 'rgba(0, 0, 0, 0)':
                issues.append(f"Card {i+1} has transparent background - should be white")
        
        # Check badges
        print("\n\n3. BADGES CHECK:")
        print("-" * 80)
        badges = page.locator('.badge, .badge-soft-primary, .badge-subtle-neutral, [class*="badge"]').all()
        print(f"Found {len(badges)} badges")
        
        for i, badge in enumerate(badges[:5]):
            styles = badge.evaluate("""
                el => {
                    const cs = window.getComputedStyle(el);
                    return {
                        bg: cs.backgroundColor,
                        color: cs.color,
                        borderRadius: cs.borderRadius,
                        text: el.textContent.trim()
                    };
                }
            """)
            print(f"\nBadge {i+1}: '{styles['text']}'")
            print(f"  Background: {styles['bg']}")
            print(f"  Color: {styles['color']}")
            print(f"  Border Radius: {styles['borderRadius']}")
            
            if styles['bg'] == 'rgba(0, 0, 0, 0)':
                issues.append(f"Badge '{styles['text']}' has transparent background")
        
        # Check Bootstrap is loaded
        print("\n\n4. BOOTSTRAP VERIFICATION:")
        print("-" * 80)
        bootstrap_loaded = page.evaluate("""
            () => {
                // Check if Bootstrap CSS is loaded
                const links = Array.from(document.querySelectorAll('link[rel="stylesheet"]'));
                const bootstrapLink = links.find(l => l.href.includes('bootstrap'));
                
                // Check if Bootstrap JS is loaded
                const scripts = Array.from(document.querySelectorAll('script'));
                const bootstrapScript = scripts.find(s => s.src.includes('bootstrap'));
                
                return {
                    cssLoaded: !!bootstrapLink,
                    jsLoaded: !!bootstrapScript,
                    cssHref: bootstrapLink ? bootstrapLink.href : null,
                    jsHref: bootstrapScript ? bootstrapScript.src : null
                };
            }
        """)
        
        print(f"Bootstrap CSS loaded: {bootstrap_loaded['cssLoaded']}")
        print(f"  Path: {bootstrap_loaded['cssHref']}")
        print(f"Bootstrap JS loaded: {bootstrap_loaded['jsLoaded']}")
        print(f"  Path: {bootstrap_loaded['jsHref']}")
        
        # Summary
        print("\n\n" + "=" * 80)
        print("ISSUES FOUND:")
        print("=" * 80)
        
        if issues:
            for issue in issues:
                print(f"  ⚠️  {issue}")
        else:
            print("  ✓ No major styling issues detected!")
        
        print("\n" + "=" * 80)
        
        browser.close()
        
        return len(issues)

if __name__ == '__main__':
    issue_count = detailed_audit()
    exit(0 if issue_count == 0 else 1)
