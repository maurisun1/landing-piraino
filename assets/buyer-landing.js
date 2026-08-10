(function () {
  var bar = document.querySelector(".buyer-sticky-bar");
  var hero = document.querySelector(".buyer-hero-pro");
  if (!bar || !hero) return;

  document.body.classList.add("buyer-has-sticky");

  var show = function () {
    var rect = hero.getBoundingClientRect();
    if (rect.bottom < 0) bar.classList.add("visible");
    else bar.classList.remove("visible");
  };

  window.addEventListener("scroll", show, { passive: true });
  show();
})();
