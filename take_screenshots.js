const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Desktop viewport
  await page.setViewportSize({ width: 1920, height: 1080 });

  // Screenshot index.html
  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle' });
  await page.screenshot({ path: 'screenshot-desktop-new.png', fullPage: true });
  console.log('Desktop screenshot captured');

  // Tablet viewport
  await page.setViewportSize({ width: 768, height: 1024 });
  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle' });
  await page.screenshot({ path: 'screenshot-tablet-new.png', fullPage: true });
  console.log('Tablet screenshot captured');

  // Mobile viewport
  await page.setViewportSize({ width: 375, height: 812 });
  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle' });
  await page.screenshot({ path: 'screenshot-mobile-new.png', fullPage: true });
  console.log('Mobile screenshot captured');

  await browser.close();
  console.log('All screenshots completed');
})();
