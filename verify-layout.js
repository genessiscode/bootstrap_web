const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  // Navigate to the local file
  await page.goto('file://' + process.cwd() + '/index.html');

  // Wait for network idle
  await page.waitForLoadState('networkidle');

  // Define viewport sizes to test: mobile, tablet, desktop
  const viewports = [
    { width: 375, height: 667, label: 'mobile' },
    { width: 768, height: 1024, label: 'tablet' },
    { width: 1280, height: 720, label: 'desktop' }
  ];

  for (const vp of viewports) {
    await page.setViewportSize({ width: vp.width, height: vp.height });
    await page.waitForTimeout(500); // let CSS adjust
    const screenshotPath = `screenshot-${vp.label}.png`;
    await page.screenshot({ path: screenshotPath, fullPage: true });
    console.log(`Saved ${screenshotPath}`);
  }

  // Also check for any visible overflow or issues
  const bodyClass = await page.evaluate(() => document.body.className);
  console.log('Body class:', bodyClass);

  // Check if any elements have overflow
  const overflow = await page.evaluate(() => {
    const problematic = [];
    const checkEl = (el) => {
      const style = getComputedStyle(el);
      if (style.overflow === 'auto' || style.overflow === 'scroll' || style.overflow === 'hidden') {
        // skip
        return;
      }
      if (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1) {
        problematic.push({
          tag: el.tagName,
          class: el.className,
          scrollWidth: el.scrollWidth,
          clientWidth: el.clientWidth,
          scrollHeight: el.scrollHeight,
          clientHeight: el.clientHeight
        });
      }
      Array.from(el.children).forEach(checkEl);
    };
    checkEl(document.body);
    return problematic;
  });
  if (overflow.length > 0) {
    console.warn('Potential overflow elements:', overflow);
  } else {
    console.log('No overflow detected.');
  }

  await browser.close();
})();