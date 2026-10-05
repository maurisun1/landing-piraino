(function () {
  function qs(sel, root) {
    return (root || document).querySelector(sel);
  }
  function qsa(sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function track(name, params) {
    try {
      if (typeof window.gtag === 'function') window.gtag('event', name, params || {});
    } catch (e) {}
    try {
      if (window.clarity) window.clarity('event', name);
    } catch (e) {}
  }

  function fillUtm(form) {
    var params = new URLSearchParams(window.location.search || '');
    ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'].forEach(function (key) {
      var el = form.querySelector('[name="' + key + '"]');
      if (el && params.get(key)) el.value = params.get(key);
    });
    var ref = form.querySelector('[name="referrer"]');
    if (ref && !ref.value) ref.value = document.referrer || '';
    var page = form.querySelector('[name="page"]');
    if (page && !page.value) page.value = window.location.pathname;
  }

  function syncObiettivo(form) {
    var sel = form.querySelector('[name="obiettivo"]');
    if (!sel) return;
    var isRicerca = String(sel.value || '').toLowerCase().indexOf('ricerca') !== -1;
    form.classList.toggle('ricerca-on', isRicerca);
  }

  function initForm(form) {
    if (!form || form.dataset.icReady) return;
    form.dataset.icReady = '1';
    fillUtm(form);

    var leadType = form.getAttribute('data-lead-type') || 'commerciale';
    var step1 = qs('[data-step="1"]', form);
    var step2 = qs('[data-step="2"]', form);
    var prog = qsa('.ic-progress span', form.parentElement);
    var nextBtn = qs('[data-next]', form);
    var backBtn = qs('[data-back]', form);
    var success = form.parentElement ? qs('.ic-success', form.parentElement) : null;
    var started = false;
    var obiettivo = form.querySelector('[name="obiettivo"]');

    function showStep(n) {
      if (step1) step1.classList.toggle('on', n === 1);
      if (step2) step2.classList.toggle('on', n === 2);
      prog.forEach(function (el, i) {
        el.classList.toggle('on', i < n);
      });
    }

    function requiredOk(scope) {
      var ok = true;
      qsa('input[required], select[required], textarea[required]', scope).forEach(function (el) {
        if (el.disabled || el.offsetParent === null && el.type !== 'hidden') {
          /* skip hidden ricerca extras when not visible */
        }
        if (el.closest('.ricerca-extra') && !form.classList.contains('ricerca-on')) return;
        if (el.type === 'checkbox') {
          if (!el.checked) ok = false;
        } else if (!String(el.value || '').trim()) {
          ok = false;
        }
      });
      return ok;
    }

    if (obiettivo) {
      obiettivo.addEventListener('change', function () {
        syncObiettivo(form);
      });
      syncObiettivo(form);
    }

    form.addEventListener(
      'input',
      function () {
        if (started) return;
        started = true;
        track('form_start', { lead_type: leadType, form_step: 1 });
      },
      { once: true }
    );

    if (nextBtn && step2) {
      nextBtn.addEventListener('click', function () {
        if (!requiredOk(step1)) {
          form.reportValidity();
          return;
        }
        showStep(2);
        track('form_step2', { lead_type: leadType });
      });
    }
    if (backBtn) {
      backBtn.addEventListener('click', function () {
        showStep(1);
      });
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!requiredOk(step1 || form)) {
        form.reportValidity();
        return;
      }
      if (step2 && step2.classList.contains('on') && !requiredOk(step2)) {
        form.reportValidity();
        return;
      }

      var hp = form.querySelector('[name="company_website"]');
      if (hp && hp.value) return;

      var btn = form.querySelector('[type="submit"]');
      if (btn) {
        btn.disabled = true;
        btn.textContent = 'Invio…';
      }

      var data = new FormData(form);
      fetch(form.action, {
        method: 'POST',
        body: data,
        headers: { Accept: 'application/json' }
      })
        .then(function (res) {
          if (!res.ok) throw new Error('submit failed');
          track('generate_lead', { lead_type: leadType, method: 'form' });
          track('lead_form_submit', { lead_type: leadType });
          form.style.display = 'none';
          if (success) success.classList.add('on');
        })
        .catch(function () {
          if (btn) {
            btn.disabled = false;
            btn.textContent = btn.getAttribute('data-label') || 'Invia';
          }
          alert('Invio non riuscito. Riprova o scrivimi su WhatsApp.');
        });
    });

    showStep(1);
  }

  function bindCtaTracking() {
    document.addEventListener(
      'click',
      function (e) {
        var el = e.target && e.target.closest ? e.target.closest('[data-cta]') : null;
        if (!el) return;
        var name = el.getAttribute('data-cta');
        if (!name) return;
        track('cta_click', { cta_id: name, lead_type: 'commerciale' });
        track(name, { lead_type: 'commerciale' });
        var obiettivoVal = el.getAttribute('data-obiettivo');
        if (obiettivoVal) {
          var sel = document.querySelector('#obiettivo');
          if (sel) {
            sel.value = obiettivoVal;
            sel.dispatchEvent(new Event('change', { bubbles: true }));
          }
        }
      },
      true
    );

    document.addEventListener(
      'click',
      function (e) {
        var a = e.target && e.target.closest ? e.target.closest('a[href^="mailto:"]') : null;
        if (!a) return;
        track('email_click', { method: 'email' });
        try {
          if (window.clarity) window.clarity('event', 'email_click');
        } catch (err) {}
      },
      true
    );
  }

  function initSticky() {
    var bar = qs('.ic-sticky');
    var hero = qs('.ic-hero');
    if (!bar || !hero) return;
    var visible = false;
    function onScroll() {
      var show = window.scrollY > hero.offsetHeight * 0.55;
      if (show === visible) return;
      visible = show;
      bar.classList.toggle('visible', show);
      document.body.classList.toggle('ic-has-sticky', show);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  function boot() {
    qsa('form.ic-form').forEach(initForm);
    bindCtaTracking();
    initSticky();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
