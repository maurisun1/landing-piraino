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
    document.documentElement.style.setProperty('--nav-top', topbarHeight + headerHeight + 'px');
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
    link.addEventListener('click', function () {
      var href = link.getAttribute('href') || '';
      // Same-page anchors: close immediately for visual feedback.
      if (href.charAt(0) === '#' && href.length > 1) {
        closeMenu();
        return;
      }
      // Cross-page links: do not close synchronously — on mobile that can
      // cancel navigation and force a second tap.
      if (href && href.charAt(0) !== '#') {
        return;
      }
      closeMenu();
    });
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
      closeMenu();
      closeLangMenus();
    }
  });

  window.addEventListener('resize', function () {
    setNavTop();
    if (window.innerWidth > 980) closeMenu();
  });

  function closeLangMenus(except) {
    document.querySelectorAll('details.lang-switcher[open]').forEach(function (el) {
      if (except && el === except) return;
      el.open = false;
    });
  }

  document.querySelectorAll('details.lang-switcher').forEach(function (details) {
    details.addEventListener('toggle', function () {
      if (details.open) closeLangMenus(details);
    });
  });

  document.addEventListener('click', function (event) {
    var open = document.querySelector('details.lang-switcher[open]');
    if (!open) return;
    if (open.contains(event.target)) return;
    open.open = false;
  });

  setNavTop();
})();
