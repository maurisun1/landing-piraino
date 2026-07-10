document.addEventListener("DOMContentLoaded", function () {
  var bar = document.querySelector(".seller-sticky-bar");
  var hero = document.querySelector(".hero");
  if (!bar || !hero) return;

  var visible = false;
  function onScroll() {
    var show = window.scrollY > hero.offsetHeight * 0.55;
    if (show === visible) return;
    visible = show;
    bar.classList.toggle("visible", show);
    document.body.classList.toggle("seller-has-sticky", show);
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
});
