(function () {
  var header = document.querySelector('.site-header');
  if (!header) return;

  var toggle = header.querySelector('.nav-toggle');
  var panel = header.querySelector('.nav-panel');
  var backdrop = header.querySelector('.nav-backdrop');
  if (!toggle || !panel) return;

  function setNavTop() {
    var topbar = document.querySelector('.topbar');
    var headerHeight = header.offsetHeight;
    var topbarHeight = topbar ? topbar.offsetHeight : 0;
    document.documentElement.style.setProperty('--nav-top', (topbarHeight + headerHeight) + 'px');
  }

  function closeMenu() {
    header.classList.remove('menu-open');
    toggle.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('nav-open');
    if (backdrop) backdrop.hidden = true;
  }

  function openMenu() {
    setNavTop();
    header.classList.add('menu-open');
    toggle.setAttribute('aria-expanded', 'true');
    document.body.classList.add('nav-open');
    if (backdrop) backdrop.hidden = false;
  }

  toggle.addEventListener('click', function () {
    if (header.classList.contains('menu-open')) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  if (backdrop) {
    backdrop.addEventListener('click', closeMenu);
  }

  panel.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', closeMenu);
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') closeMenu();
  });

  window.addEventListener('resize', function () {
    setNavTop();
    if (window.innerWidth > 980) closeMenu();
  });

  setNavTop();
})();
