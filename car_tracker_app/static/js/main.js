/*/ Get all elements with the "fade-in" and "slide-in" classes
const fadeInElements = document.querySelectorAll('.fade-in');
const slideInElements = document.querySelectorAll('.slide-in-from-left, .slide-in-from-right');

// Create an Intersection Observer
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('show'); // Trigger the animation
      observer.unobserve(entry.target); // Stop observing once animated
    }
  });
});

// Observe each element
fadeInElements.forEach((el) => observer.observe(el));
slideInElements.forEach((el) => observer.observe(el));*/