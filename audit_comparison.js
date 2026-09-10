const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  console.log('=== Visual Audit Report ===\n');

  // Desktop viewport
  await page.setViewportSize({ width: 1920, height: 1080 });
  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle' });

  // Check for previous button in carousel
  const prevButton = await page.$('.carousel-btn-prev');
  console.log('✓ Previous button exists:', prevButton !== null);

  // Check for next button in carousel
  const nextButton = await page.$('.carousel-btn-next');
  console.log('✓ Next button exists:', nextButton !== null);

  // Check for badges
  const badges = await page.$$('.badge, .badge-soft-primary, .badge-subtle-neutral');
  console.log('✓ Badge count:', badges.length);

  // Check for card designs
  const cards = await page.$$('.card, .card-surface, .card-feature');
  console.log('✓ Card count:', cards.length);

  // Check for trust badges
  const trustBadges = await page.$$('.trust-badge');
  console.log('✓ Trust badge count:', trustBadges.length);

  // Check carousel indicators
  const indicators = await page.$$('.carousel-indicators .indicator');
  console.log('✓ Carousel indicators:', indicators.length);

  // Check for button styles
  const buttons = await page.$$('.btn, .btn-action-primary, .btn-action-secondary');
  console.log('✓ Button count:', buttons.length);

  // Get computed styles for key elements
  const heroSection = await page.$('.hero-section');
  if (heroSection) {
    const bgColor = await heroSection.evaluate(el => window.getComputedStyle(el).backgroundColor);
    console.log('✓ Hero section background:', bgColor);
  }

  // Check for card border radius
  const firstCard = await page.$('.card-surface');
  if (firstCard) {
    const borderRadius = await firstCard.evaluate(el => window.getComputedStyle(el).borderRadius);
    console.log('✓ Card border-radius:', borderRadius);
  }

  // Check for icon-circle-surface
  const iconCircles = await page.$$('.icon-circle-surface');
  console.log('✓ Icon circles:', iconCircles.length);

  // Check carousel button visibility
  const carouselBtn = await page.$('.carousel-btn');
  if (carouselBtn) {
    const isVisible = await carouselBtn.isVisible();
    const bgColor = await carouselBtn.evaluate(el => window.getComputedStyle(el).backgroundColor);
    console.log('✓ Carousel button visible:', isVisible);
    console.log('✓ Carousel button bg:', bgColor);
  }

  console.log('\n=== Testing Responsive Behavior ===\n');

  // Tablet test
  await page.setViewportSize({ width: 768, height: 1024 });
  await page.waitForTimeout(500);
  const carouselCards = await page.$$('.carousel-card');
  console.log('✓ Carousel cards visible (tablet):', carouselCards.length);

  // Mobile test
  await page.setViewportSize({ width: 375, height: 812 });
  await page.waitForTimeout(500);
  const mobileCards = await page.$$('.carousel-card');
  console.log('✓ Carousel cards visible (mobile):', mobileCards.length);

  await browser.close();
  console.log('\n=== Audit Complete ===');
})();
