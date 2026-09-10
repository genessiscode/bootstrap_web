const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1920, height: 1080 });

  console.log('\n=== COMPREHENSIVE STYLING AUDIT ===\n');

  const pages = [
    { name: 'Index', url: 'http://localhost:8080/index.html' },
    { name: 'About', url: 'http://localhost:8080/about.html' },
    { name: 'Services', url: 'http://localhost:8080/services.html' },
    { name: 'Blogs', url: 'http://localhost:8080/blogs.html' },
    { name: 'Contact', url: 'http://localhost:8080/contact.html' }
  ];

  for (const pageInfo of pages) {
    console.log(`\n--- ${pageInfo.name} Page ---`);
    await page.goto(pageInfo.url, { waitUntil: 'networkidle' });

    // Check carousel buttons
    const carouselBtns = await page.$$('.carousel-btn');
    if (carouselBtns.length > 0) {
      const btnStyle = await carouselBtns[0].evaluate(el => {
        const style = window.getComputedStyle(el);
        return {
          bg: style.backgroundColor,
          border: style.border,
          borderRadius: style.borderRadius,
          display: style.display
        };
      });
      console.log('✓ Carousel buttons:', carouselBtns.length, btnStyle);
    }

    // Check badge styles
    const badges = await page.$$('.badge-soft-primary, .badge-subtle-neutral');
    if (badges.length > 0) {
      const badgeStyle = await badges[0].evaluate(el => {
        const style = window.getComputedStyle(el);
        return {
          bg: style.backgroundColor,
          color: style.color,
          borderRadius: style.borderRadius,
          padding: style.padding
        };
      });
      console.log('✓ Badges:', badges.length, badgeStyle);
    }

    // Check card designs
    const cards = await page.$$('.card-surface, .card-feature');
    if (cards.length > 0) {
      const cardStyle = await cards[0].evaluate(el => {
        const style = window.getComputedStyle(el);
        return {
          bg: style.backgroundColor,
          border: style.border,
          borderRadius: style.borderRadius,
          boxShadow: style.boxShadow
        };
      });
      console.log('✓ Cards:', cards.length, cardStyle);
    }

    // Check icon circles
    const iconCircles = await page.$$('.icon-circle-surface');
    if (iconCircles.length > 0) {
      const iconStyle = await iconCircles[0].evaluate(el => {
        const style = window.getComputedStyle(el);
        return {
          bg: style.backgroundColor,
          borderRadius: style.borderRadius,
          width: style.width,
          height: style.height
        };
      });
      console.log('✓ Icon circles:', iconCircles.length, iconStyle);
    }

    // Check trust badges
    const trustBadges = await page.$$('.trust-badge');
    if (trustBadges.length > 0) {
      const trustStyle = await trustBadges[0].evaluate(el => {
        const style = window.getComputedStyle(el);
        return {
          bg: style.backgroundColor,
          border: style.border,
          borderRadius: style.borderRadius
        };
      });
      console.log('✓ Trust badges:', trustBadges.length, trustStyle);
    }

    // Check buttons
    const buttons = await page.$$('.btn-action-primary, .btn-primary');
    if (buttons.length > 0) {
      const btnStyle = await buttons[0].evaluate(el => {
        const style = window.getComputedStyle(el);
        return {
          bg: style.backgroundColor,
          color: style.color,
          borderRadius: style.borderRadius
        };
      });
      console.log('✓ Primary buttons:', buttons.length, btnStyle);
    }
  }

  console.log('\n=== RESPONSIVE TESTING ===\n');

  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle' });

  const viewports = [
    { name: 'Desktop', width: 1920, height: 1080 },
    { name: 'Tablet', width: 768, height: 1024 },
    { name: 'Mobile', width: 375, height: 812 }
  ];

  for (const vp of viewports) {
    await page.setViewportSize({ width: vp.width, height: vp.height });
    await page.waitForTimeout(500);

    const carouselCards = await page.$$('.carousel-card');
    const visibleCards = await page.$$('.carousel-card:visible');

    console.log(`${vp.name} (${vp.width}x${vp.height}):`);
    console.log(`  - Total carousel cards: ${carouselCards.length}`);
    console.log(`  - Visible cards: ${visibleCards.length}`);

    if (carouselCards.length > 0) {
      const cardWidth = await carouselCards[0].evaluate(el => {
        const style = window.getComputedStyle(el);
        return {
          flex: style.flex,
          width: style.width
        };
      });
      console.log(`  - Card sizing:`, cardWidth);
    }
  }

  console.log('\n=== AUDIT COMPLETE ===\n');
  await browser.close();
})();
