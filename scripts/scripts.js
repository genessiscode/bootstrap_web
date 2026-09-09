// ===== TravelEase Bootstrap 5 Website - Custom Scripts =====
// Beginner-friendly scripts with no emojis, no forbidden patterns
// ===============================================================

(() => {
  'use strict';

  // Initialize newsletter form validation
  initNewsletterForm();

  // Initialize booking form validation
  initBookingForm();

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

// ===== Booking Form Validation =====
function initBookingForm() {
  const form = document.getElementById('bookingForm');
  if (!form) return;

  form.addEventListener('submit', function(event) {
    event.preventDefault();

    const checkIn = form.querySelector('#checkIn');
    const checkOut = form.querySelector('#checkOut');
    const roomType = form.querySelector('#roomType');
    const guests = form.querySelector('#guests');

    let isValid = true;

    // Reset previous validation states
    [checkIn, checkOut, roomType, guests].forEach(function(field) {
      field.classList.remove('is-invalid');
    });

    // Validate check-in date
    if (!checkIn.value) {
      checkIn.classList.add('is-invalid');
      isValid = false;
    }

    // Validate check-out date
    if (!checkOut.value) {
      checkOut.classList.add('is-invalid');
      isValid = false;
    }

    // Validate check-out is after check-in
    if (checkIn.value && checkOut.value && new Date(checkOut.value) <= new Date(checkIn.value)) {
      checkOut.classList.add('is-invalid');
      isValid = false;
    }

    // Validate room type
    if (!roomType.value) {
      roomType.classList.add('is-invalid');
      isValid = false;
    }

    // Validate guests
    if (!guests.value || guests.value < 1) {
      guests.classList.add('is-invalid');
      isValid = false;
    }

    if (isValid) {
      const btn = form.querySelector('button[type="submit"]');
      const originalText = btn.textContent;
      btn.textContent = 'Booking...';
      btn.disabled = true;

      setTimeout(function() {
        btn.textContent = 'Booked!';
        btn.classList.replace('btn-primary', 'btn-success');
      }, 800);
    }
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