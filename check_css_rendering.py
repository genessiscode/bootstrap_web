#!/usr/bin/env python3
"""
Force CSS reload and check what's actually rendering
"""
from playwright.sync_api import sync_playwright
import time

def check_actual_rendering():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        
        # Disable cache
        page = context.new_page()
        
        # Add timestamp to force CSS reload
        timestamp = int(time.time())
        page.goto(f'file:///home/cornbread/ETF_Bootstrap/index.html?t={timestamp}')
        page.wait_for_load_state('networkidle')
        
        # Force hard reload
        page.reload(wait_until='networkidle')
        
        print("Checking actual button classes in HTML...")
        
        buttons_info = page.evaluate("""
            () => {
                const buttons = Array.from(document.querySelectorAll('.btn'));
                return buttons.slice(0, 6).map((btn, i) => ({
                    index: i,
                    text: btn.textContent.trim().substring(0, 30),
                    classes: btn.className,
                    tagName: btn.tagName,
                    computedBg: window.getComputedStyle(btn).backgroundColor,
                    computedBorder: window.getComputedStyle(btn).border,
                    href: btn.href || 'none'
                }));
            }
        """)
        
        print("\nButton Analysis:")
        print("=" * 80)
        for btn in buttons_info:
            print(f"\nButton {btn['index']}: {btn['text']}")
            print(f"  Tag: {btn['tagName']}")
            print(f"  Classes: {btn['classes']}")
            print(f"  Computed BG: {btn['computedBg']}")
            print(f"  Computed Border: {btn['computedBorder']}")
        
        print("\n\nChecking if custom CSS is actually applied...")
        
        css_check = page.evaluate("""
            () => {
                const testBtn = document.querySelector('.btn-action-primary');
                if (!testBtn) return {error: 'No btn-action-primary found'};
                
                const styles = window.getComputedStyle(testBtn);
                
                // Check all stylesheets
                const sheets = Array.from(document.styleSheets);
                const customSheet = sheets.find(s => s.href && s.href.includes('styles.css'));
                
                let customRules = [];
                if (customSheet) {
                    try {
                        const rules = Array.from(customSheet.cssRules || customSheet.rules);
                        customRules = rules
                            .filter(r => r.selectorText && r.selectorText.includes('btn-action-primary'))
                            .map(r => ({
                                selector: r.selectorText,
                                bgColor: r.style.backgroundColor,
                                borderColor: r.style.borderColor
                            }));
                    } catch(e) {
                        customRules = [{error: e.message}];
                    }
                }
                
                return {
                    elementBg: styles.backgroundColor,
                    elementBorderColor: styles.borderColor,
                    elementBorderRadius: styles.borderRadius,
                    customRulesFound: customRules.length,
                    customRules: customRules,
                    customSheetHref: customSheet ? customSheet.href : 'not found'
                };
            }
        """)
        
        print("CSS Application Check:")
        print("=" * 80)
        print(f"Custom stylesheet: {css_check.get('customSheetHref', 'N/A')}")
        print(f"Custom rules found: {css_check.get('customRulesFound', 0)}")
        print(f"Element background: {css_check.get('elementBg', 'N/A')}")
        print(f"Element border color: {css_check.get('elementBorderColor', 'N/A')}")
        print(f"Element border radius: {css_check.get('elementBorderRadius', 'N/A')}")
        
        if css_check.get('customRules'):
            print("\nFound CSS Rules:")
            for rule in css_check['customRules']:
                print(f"  {rule}")
        
        browser.close()

if __name__ == '__main__':
    check_actual_rendering()
