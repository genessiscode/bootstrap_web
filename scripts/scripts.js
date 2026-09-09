// ===== TravelEase Bootstrap 5 Website - Custom Scripts =====
// Beginner-friendly scripts with no emojis, no forbidden patterns
// ===============================================================

(() => {
  'use strict';

  // Initialize newsletter form validation
  initNewsletterForm();

  // Set up focus-visible states for accessibility
  setupFocusStates();

  // Initialize page on DOM ready
  document.addEventListener('DOMContentLoaded', function() {
    console.log('TravelEase website initialized');
  });

})();

// ===== Newsletter Form Validation =====
function initNewsletterForm() {
  const form = document.getElementById('newsletterForm');
  if (!form) return;

  form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent actual submission for demo

    const emailInput = form.querySelector('input[type="email"]');
    if (!emailInput) return;

    const emailValue = emailInput.value.trim();

    // Hide any previous alerts
    const successAlert = document.getElementById('successAlert');
    const errorAlert = document.getElementById('errorAlert');
    if (successAlert) successAlert.classList.add('d-none');
    if (errorAlert) errorAlert.classList.add('d-none');

    // Validate email is not empty
    if (!emailValue) {
      showAlert(errorAlert, 'Please enter your email address', 'danger');
      emailInput.focus();
      return;
    }

    // Validate email format
    if (!isValidEmail(emailValue)) {
      showAlert(errorAlert, 'Please enter a valid email address', 'danger');
      emailInput.focus();
      return;
    }

    // Show success and clear form
    showAlert(successAlert, 'Thanks for subscribing! Check your inbox for deals.', 'success');
    form.reset();
  });
}

// ===== Email Validation Helper =====
function isValidEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

// ===== Show Alert =====
function showAlert(alertElement, message, type) {
  if (!alertElement) return;
  alertElement.querySelector('.alert-text')?.setAttribute('data-message', message);
  alertElement.removeAttribute('data-type');
  alertElement.setAttribute('data-type', type);
  alertElement.classList.remove('d-none');
  alertElement.classList.add('show');
}

// ===== Setup Focus-Visible States =====
function setupFocusStates() {
  // Add focus-visible outline to interactive elements
  const focusableElements = document.querySelectorAll(
    'a:not([href^="#"]):not([disabled]), button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled])'
  );

  focusableElements.forEach(function(el) {
    el.addEventListener('focus', function() {
      // Check if browser supports :focus-visible
      if (el.style.outline !== 'none') {
        el.style.outline = '2px solid var(--primary-blue)';
        el.style.outlineOffset = '2px';
      }
    }, { once: true });
  });
}

// ===== Smooth Scroll for anchor links =====
document.addEventListener('click', function(event) {
  if (event.target.matches('a[href^="#"]') && !event.target.classList.contains('btn')) {
    event.preventDefault();
    const targetId = event.target.getAttribute('href');
    if (targetId === '#') return;
    const targetElement = document.querySelector(targetId);
    if (targetElement) {
      targetElement.scrollIntoView({ behavior: 'smooth' });
    }
  }
});