/**
 * TravelPearl - Interactive Scripts
 * Handles form validation, carousel, smooth scroll, and booking logic
 */

// ===== Form Validation (Bootstrap 5 native) =====
(function initFormValidation() {
  'use strict';
  const forms = document.querySelectorAll('.needs-validation');
  Array.from(forms).forEach(function (form) {
    form.addEventListener('submit', function (event) {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add('was-validated');
    }, false);
  });
})();

// ===== Booking Form Submission (if exists) =====
const bookingForm = document.getElementById('bookingForm');
if (bookingForm) {
  bookingForm.addEventListener('submit', function(event) {
    event.preventDefault();
    
    if (bookingForm.checkValidity()) {
      const formData = new FormData(bookingForm);
      const bookingData = {};
      
      formData.forEach((value, key) => {
        bookingData[key] = value;
      });
      
      console.log('Booking submitted:', bookingData);
      
      // Show success message
      const alertDiv = document.createElement('div');
      alertDiv.className = 'alert alert-success alert-dismissible fade show mt-4';
      alertDiv.role = 'alert';
      alertDiv.innerHTML = `
        <strong>Booking Request Received!</strong> We'll confirm your reservation within 24 hours.
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      `;
      
      bookingForm.insertAdjacentElement('afterend', alertDiv);
      bookingForm.reset();
      bookingForm.classList.remove('was-validated');
      
      // Auto-remove alert after 5 seconds
      setTimeout(() => {
        alertDiv.remove();
      }, 5000);
    } else {
      bookingForm.classList.add('was-validated');
    }
  });
}

// ===== Responsive Image Carousel (1/3/4 cards based on viewport) =====
function initImageCarousel() {
  const track = document.getElementById('carouselTrack');
  const prevBtn = document.querySelector('.carousel-btn-prev');
  const nextBtn = document.querySelector('.carousel-btn-next');
  const indicatorsContainer = document.getElementById('carouselIndicators');

  if (!track || !prevBtn || !nextBtn) return;

  const cards = Array.from(track.querySelectorAll('.carousel-card'));
  const totalCards = cards.length;
  
  let currentIndex = 0;
  let cardsPerView = 4;
  let isAnimating = false;
  let autoplayInterval;

  // Determine cards per view based on viewport
  function updateCardsPerView() {
    const width = window.innerWidth;
    if (width <= 768) {
      cardsPerView = 1;
    } else if (width <= 1024) {
      cardsPerView = 3;
    } else {
      cardsPerView = 4;
    }
  }

  // Calculate total pages
  function getTotalPages() {
    return Math.ceil(totalCards / cardsPerView);
  }

  // Update indicators
  function updateIndicators() {
    const totalPages = getTotalPages();
    indicatorsContainer.innerHTML = '';
    
    for (let i = 0; i < totalPages; i++) {
      const button = document.createElement('button');
      button.className = 'indicator';
      button.setAttribute('data-index', i);
      button.setAttribute('aria-label', `Slide ${i + 1}`);
      if (i === 0) button.classList.add('active');
      
      button.addEventListener('click', () => goToSlide(i));
      indicatorsContainer.appendChild(button);
    }
  }

  // Update carousel position
  function updateCarousel(animate = true) {
    if (!animate) {
      track.style.transition = 'none';
    } else {
      track.style.transition = 'transform 0.5s cubic-bezier(0.4, 0, 0.2, 1)';
    }

    // Calculate offset based on current index and cards per view
    const cardWidth = cards[0].offsetWidth;
    const gap = parseFloat(getComputedStyle(track).gap) || 16;
    const offset = -(currentIndex * cardsPerView) * (cardWidth + gap);
    
    track.style.transform = `translateX(${offset}px)`;

    // Update indicators
    const indicators = indicatorsContainer.querySelectorAll('.indicator');
    indicators.forEach((indicator, index) => {
      indicator.classList.toggle('active', index === currentIndex);
    });
  }

  // Next slide
  function nextSlide() {
    if (isAnimating) return;
    isAnimating = true;

    const totalPages = getTotalPages();
    currentIndex = (currentIndex + 1) % totalPages;
    updateCarousel(true);

    setTimeout(() => {
      isAnimating = false;
    }, 500);
  }

  // Previous slide
  function prevSlide() {
    if (isAnimating) return;
    isAnimating = true;

    const totalPages = getTotalPages();
    currentIndex = (currentIndex - 1 + totalPages) % totalPages;
    updateCarousel(true);

    setTimeout(() => {
      isAnimating = false;
    }, 500);
  }

  // Go to specific slide
  function goToSlide(index) {
    if (isAnimating || index === currentIndex) return;
    isAnimating = true;

    currentIndex = index;
    updateCarousel(true);

    setTimeout(() => {
      isAnimating = false;
    }, 500);
  }

  // Handle window resize
  function handleResize() {
    const oldCardsPerView = cardsPerView;
    updateCardsPerView();
    
    if (oldCardsPerView !== cardsPerView) {
      const totalPages = getTotalPages();
      // Adjust current index if needed
      if (currentIndex >= totalPages) {
        currentIndex = totalPages - 1;
      }
      updateIndicators();
      updateCarousel(false);
    }
  }

  // Start autoplay
  function startAutoplay() {
    autoplayInterval = setInterval(nextSlide, 6000);
  }

  // Stop autoplay
  function stopAutoplay() {
    clearInterval(autoplayInterval);
  }

  // Event listeners
  prevBtn.addEventListener('click', prevSlide);
  nextBtn.addEventListener('click', nextSlide);

  // Pause autoplay on hover
  const carouselContainer = document.querySelector('.carousel-container');
  if (carouselContainer) {
    carouselContainer.addEventListener('mouseenter', stopAutoplay);
    carouselContainer.addEventListener('mouseleave', startAutoplay);
  }

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') {
      prevSlide();
    } else if (e.key === 'ArrowRight') {
      nextSlide();
    }
  });

  // Touch swipe support
  let touchStartX = 0;
  let touchEndX = 0;

  const viewport = document.querySelector('.carousel-viewport');
  if (viewport) {
    viewport.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    viewport.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
    }, { passive: true });
  }

  function handleSwipe() {
    const swipeThreshold = 50;
    const diff = touchStartX - touchEndX;

    if (Math.abs(diff) > swipeThreshold) {
      if (diff > 0) {
        nextSlide();
      } else {
        prevSlide();
      }
    }
  }

  // Window resize listener
  let resizeTimeout;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(handleResize, 150);
  });

  // Initialize
  updateCardsPerView();
  updateIndicators();
  updateCarousel(false);
  startAutoplay();
}

// ===== Smooth Scroll for anchor links =====
document.addEventListener('click', function(event) {
  const link = event.target.closest('a[href^="#"]');
  if (link && !link.classList.contains('btn') && !link.hasAttribute('data-bs-toggle')) {
    const targetId = link.getAttribute('href');
    if (targetId && targetId !== '#' && targetId.length > 1) {
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        event.preventDefault();
        targetElement.scrollIntoView({ behavior: 'smooth' });
      }
    }
  }
});

// ===== Initialize all on page load =====
document.addEventListener('DOMContentLoaded', function() {
  initImageCarousel();
});
