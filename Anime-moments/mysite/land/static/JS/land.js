var swiper = new Swiper(".mySwiper", {
  spaceBetween: 30,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  pagination: {
    el: ".swiper-pagination",
  },
  mousewheel: true,
  keyboard: true,
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  loop: true,
});

swiper.el.addEventListener('mouseenter', () => {
  swiper.autoplay.stop();
});

swiper.el.addEventListener('mouseleave', () => {
  swiper.autoplay.start();
});
  