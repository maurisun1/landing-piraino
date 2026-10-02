/**
 * GA4 + Microsoft Clarity, loaded only after cookie consent (GDPR).
 *
 * Set IDs after creating the free properties:
 * - GA4_MEASUREMENT_ID: https://analytics.google.com (Admin → Data streams → Web → G-XXXXXXXX)
 * - CLARITY_ID: https://clarity.microsoft.com (project settings)
 */
(function () {
  var GA4_MEASUREMENT_ID = 'G-68WK7YT5CX';
  var CLARITY_ID = 'yrmwn6l8qe';
  var STORAGE_KEY = 'mp_analytics_consent';
  var CONSENT_VERSION = '2';

  function hasGa4() {
    return typeof GA4_MEASUREMENT_ID === 'string' && /^G-[A-Z0-9]+$/i.test(GA4_MEASUREMENT_ID);
  }

  function hasClarity() {
    return typeof CLARITY_ID === 'string' && /^[a-zA-Z0-9]{8,}$/.test(CLARITY_ID);
  }

  function hasAnyTool() {
    return hasGa4() || hasClarity();
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

  function loadGa4() {
    if (!hasGa4() || window.__mpGa4Loaded) return;
    window.__mpGa4Loaded = true;

    window.dataLayer = window.dataLayer || [];
    window.gtag =
      window.gtag ||
      function () {
        window.dataLayer.push(arguments);
      };
    window.gtag('js', new Date());
    window.gtag('config', GA4_MEASUREMENT_ID, {
      anonymize_ip: true,
      send_page_view: true
    });

    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA4_MEASUREMENT_ID);
    document.head.appendChild(s);
  }

  function loadClarity() {
    if (!hasClarity() || window.__mpClarityLoaded) return;
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

  function loadAnalytics() {
    loadGa4();
    loadClarity();
  }

  function trackEvent(name, params) {
    try {
      if (typeof window.gtag === 'function') {
        window.gtag('event', name, params || {});
      }
    } catch (e) {}
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
        trackEvent('generate_lead', { method: 'form' });
        trackEvent('lead_form_submit');
      },
      true
    );

    document.addEventListener(
      'click',
      function (e) {
        var a = e.target && e.target.closest ? e.target.closest('a[href*="wa.me"], a[href*="whatsapp"]') : null;
        if (!a) return;
        trackEvent('whatsapp_click', { method: 'whatsapp' });
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
      '#mp-cookie-banner{position:fixed;left:12px;right:12px;bottom:12px;z-index:99999;max-width:480px;margin:0 auto;background:#111;color:#f6f1e9;border:1px solid rgba(246,241,233,.12);border-radius:12px;padding:14px 14px 12px;box-shadow:0 10px 28px rgba(0,0,0,.28);font-family:Inter,system-ui,sans-serif;transform:translateY(0);opacity:1;transition:opacity .25s ease,transform .25s ease}' +
      '#mp-cookie-banner.mp-cookie-hide{opacity:0;transform:translateY(10px)}' +
      '#mp-cookie-banner p{margin:0 0 12px;font-size:12.5px;line-height:1.45;color:rgba(246,241,233,.92)}' +
      '#mp-cookie-banner a{color:#fff;text-decoration:underline;text-underline-offset:2px}' +
      '#mp-cookie-banner .mp-cookie-actions{display:flex;flex-wrap:wrap;gap:8px}' +
      '#mp-cookie-banner button{appearance:none;border:0;cursor:pointer;border-radius:999px;padding:9px 14px;font-size:12.5px;font-weight:600;line-height:1}' +
      '#mp-cookie-banner .mp-cookie-accept{background:#dc1c2e;color:#fff}' +
      '#mp-cookie-banner .mp-cookie-reject{background:transparent;color:#f6f1e9;border:1px solid rgba(246,241,233,.35)}';
    document.head.appendChild(style);

    var banner = document.createElement('div');
    banner.id = 'mp-cookie-banner';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-live', 'polite');
    banner.setAttribute('aria-label', 'Preferenze cookie');
    banner.innerHTML =
      '<p>Noi e terze parti selezionate utilizziamo cookie o tecnologie simili per finalità tecniche e, con il tuo consenso, anche per altre finalità come specificato nella <a href="/privacy/">cookie policy</a>.</p>' +
      '<div class="mp-cookie-actions">' +
      '<button type="button" class="mp-cookie-accept">Accetta</button>' +
      '<button type="button" class="mp-cookie-reject">Rifiuta</button>' +
      '</div>';

    banner.querySelector('.mp-cookie-accept').addEventListener('click', function () {
      setConsent('accepted');
      loadAnalytics();
      hideBanner(banner);
    });
    banner.querySelector('.mp-cookie-reject').addEventListener('click', function () {
      setConsent('rejected');
      hideBanner(banner);
    });

    document.body.appendChild(banner);
  }

  function init() {
    if (!hasAnyTool()) return;
    bindConversionHooks();
    var consent = getConsent();
    if (consent === 'accepted') {
      loadAnalytics();
      return;
    }
    if (consent === 'rejected') return;
    window.setTimeout(showBanner, 2000);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
