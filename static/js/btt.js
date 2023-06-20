window.addEventListener('scroll', function() {
  if (window.pageYOffset > 200) {
      document.querySelector('.scroll-top')
          .classList.add('show');
  } else {
      document.querySelector('.scroll-top')
          .classList.remove('show');
  }
});

function scrollToTop() {
  window.scrollTo(0, 0);
};

window.addEventListener('scroll', function() {
  var element = document.querySelector('.hero-down');

  if (window.pageYOffset > 125) {
      element.classList.add('hidden');
  } else {
      element.classList.remove('hidden');
  }
});