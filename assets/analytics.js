/**
 * Microsoft Clarity + cookie consent (GDPR).
 * Set CLARITY_ID after creating a project at https://clarity.microsoft.com
 */
(function () {
  var CLARITY_ID = '';
  var STORAGE_KEY = 'mp_analytics_consent';
  var CONSENT_VERSION = '1';

  function hasValidId() {
    return typeof CLARITY_ID === 'string' && /^[a-zA-Z0-9]{8,}$/.test(CLARITY_ID);
  }

  function getConsent() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      var data = JSON.parse(raw);
      if (!data || data.v !== CONSENT_VERSION) return null;
      return data.choice === 'accepted' ? 'accepted' : data.choice === 'rejected' ? 'rejected' : null;
    } catch (e) {
      return null;
    }
  }

  function setConsent(choice) {
    try {
      localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify({ v: CONSENT_VERSION, choice: choice, t: Date.now() })
      );
    } catch (e) {}
  }

  function loadClarity() {
    if (!hasValidId() || window.__mpClarityLoaded) return;
    window.__mpClarityLoaded = true;
    (function (c, l, a, r, i, t, y) {
      c[a] =
        c[a] ||
        function () {
          (c[a].q = c[a].q || []).push(arguments);
        };
      t = l.createElement(r);
      t.async = 1;
      t.src = 'https://www.clarity.ms/tag/' + i;
      y = l.getElementsByTagName(r)[0];
      y.parentNode.insertBefore(t, y);
    })(window, document, 'clarity', 'script', CLARITY_ID);
  }

  function markConversion(name) {
    try {
      if (typeof window.clarity === 'function') {
        window.clarity('set', name, 'true');
      }
    } catch (e) {}
  }

  function bindConversionHooks() {
    document.addEventListener(
      'submit',
      function (e) {
        var form = e.target;
        if (!form || form.tagName !== 'FORM') return;
        markConversion('lead_form_submit');
      },
      true
    );

    document.addEventListener(
      'click',
      function (e) {
        var a = e.target && e.target.closest ? e.target.closest('a[href*="wa.me"], a[href*="whatsapp"]') : null;
        if (!a) return;
        markConversion('whatsapp_click');
      },
      true
    );
  }

  function hideBanner(el) {
    if (!el) return;
    el.classList.add('mp-cookie-hide');
    window.setTimeout(function () {
      if (el.parentNode) el.parentNode.removeChild(el);
    }, 280);
  }

  function showBanner() {
    if (document.getElementById('mp-cookie-banner')) return;

    var style = document.createElement('style');
    style.textContent =
      '#mp-cookie-banner{position:fixed;left:16px;right:16px;bottom:16px;z-index:99999;max-width:560px;margin:0 auto;background:#111;color:#f6f1e9;border:1px solid rgba(246,241,233,.14);border-radius:14px;padding:16px 18px;box-shadow:0 18px 48px rgba(0,0,0,.35);font-family:Inter,system-ui,sans-serif;transform:translateY(0);opacity:1;transition:opacity .25s ease,transform .25s ease}' +
      '#mp-cookie-banner.mp-cookie-hide{opacity:0;transform:translateY(12px)}' +
      '#mp-cookie-banner p{margin:0 0 12px;font-size:13.5px;line-height:1.5;color:rgba(246,241,233,.92)}' +
      '#mp-cookie-banner a{color:#fff;text-decoration:underline;text-underline-offset:2px}' +
      '#mp-cookie-banner .mp-cookie-actions{display:flex;flex-wrap:wrap;gap:8px}' +
      '#mp-cookie-banner button{appearance:none;border:0;cursor:pointer;border-radius:999px;padding:10px 16px;font-size:13px;font-weight:600}' +
      '#mp-cookie-banner .mp-cookie-accept{background:#dc1c2e;color:#fff}' +
      '#mp-cookie-banner .mp-cookie-reject{background:transparent;color:#f6f1e9;border:1px solid rgba(246,241,233,.35)}';
    document.head.appendChild(style);

    var banner = document.createElement('div');
    banner.id = 'mp-cookie-banner';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-live', 'polite');
    banner.setAttribute('aria-label', 'Preferenze cookie');
    banner.innerHTML =
      '<p>Usiamo Microsoft Clarity (solo se accetti) per capire come le pagine vengono usate e migliorare il sito. Nessuna pubblicità. Dettagli nella <a href="/privacy/">privacy</a>.</p>' +
      '<div class="mp-cookie-actions">' +
      '<button type="button" class="mp-cookie-accept">Accetta</button>' +
      '<button type="button" class="mp-cookie-reject">Solo necessari</button>' +
      '</div>';

    banner.querySelector('.mp-cookie-accept').addEventListener('click', function () {
      setConsent('accepted');
      loadClarity();
      hideBanner(banner);
    });
    banner.querySelector('.mp-cookie-reject').addEventListener('click', function () {
      setConsent('rejected');
      hideBanner(banner);
    });

    document.body.appendChild(banner);
  }

  function init() {
    if (!hasValidId()) return;
    bindConversionHooks();
    var consent = getConsent();
    if (consent === 'accepted') {
      loadClarity();
      return;
    }
    if (consent === 'rejected') return;
    showBanner();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
