#!/usr/bin/env python3
"""Apply polish v10: fonts, CSS, SEO, engage trust line on key pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FONT_OLD = (
    'family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@600;700;800'
)
FONT_NEW = (
    'family=Source+Sans+3:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800'
)

POLISH_LINK = (
    '<link rel="stylesheet" href="/assets/site-polish-v10.css?v=20260740" />'
)

TRUST = {
    "it": (
        '<ul class="hero-form-trust" aria-label="Garanzie">'
        "<li>Risposta entro 24h</li>"
        "<li>Nessun obbligo di incarico</li>"
        "<li>Referente diretto</li>"
        "</ul>"
    ),
    "de": (
        '<ul class="hero-form-trust" aria-label="Zusicherungen">'
        "<li>Antwort innerhalb von 24h</li>"
        "<li>Keine Mandatsverpflichtung</li>"
        "<li>Direkter Ansprechpartner</li>"
        "</ul>"
    ),
    "fr": (
        '<ul class="hero-form-trust" aria-label="Garanties">'
        "<li>Réponse sous 24h</li>"
        "<li>Sans engagement</li>"
        "<li>Référent direct</li>"
        "</ul>"
    ),
    "en": (
        '<ul class="hero-form-trust" aria-label="Assurances">'
        "<li>Reply within 24h</li>"
        "<li>No mandate obligation</li>"
        "<li>Direct contact</li>"
        "</ul>"
    ),
    "zh": (
        '<ul class="hero-form-trust" aria-label="保障">'
        "<li>24 小时内回复</li>"
        "<li>无委托义务</li>"
        "<li>直接对接</li>"
        "</ul>"
    ),
}

KEY_PAGES = [
    ("index.html", "it"),
    ("de/index.html", "de"),
    ("fr/index.html", "fr"),
    ("zh/index.html", "zh"),
    ("vendere-casa-milano/index.html", "it"),
    ("comprare-casa-milano/index.html", "it"),
    ("en/buy-home-milan/index.html", "en"),
    ("de/haus-kaufen-milan/index.html", "de"),
    ("fr/acheter-maison-milan/index.html", "fr"),
]


def ensure_polish_css(html: str) -> str:
    if "site-polish-v10.css" in html:
        return html
    # after site-nav or remax-brand or consultant-home
    for marker in (
        'site-nav.css?v=20260738" />',
        'site-nav.css?v=20260736" />',
        'remax-brand.css?v=20260735" />',
        'consultant-home.css?v=20260739" />',
        'consultant-home.css?v=20260738" />',
    ):
        if marker in html:
            return html.replace(marker, marker + "\n  " + POLISH_LINK, 1)
    # fallback before </head>
    return html.replace("</head>", f"  {POLISH_LINK}\n</head>", 1)


def swap_font(html: str) -> str:
    html = html.replace(FONT_OLD, FONT_NEW)
    # also Inter in inline CSS font-family stacks
    html = re.sub(
        r"font-family:\s*Inter,\s*Arial,\s*sans-serif",
        'font-family: "Source Sans 3", "Segoe UI", sans-serif',
        html,
    )
    html = re.sub(
        r"font-family:\s*Inter,",
        'font-family: "Source Sans 3",',
        html,
    )
    return html


def bump_css(html: str) -> str:
    for old, new in [
        ("consultant-home.css?v=20260738", "consultant-home.css?v=20260740"),
        ("consultant-home.css?v=20260739", "consultant-home.css?v=20260740"),
        ("site-nav.css?v=20260738", "site-nav.css?v=20260740"),
        ("site-nav.css?v=20260736", "site-nav.css?v=20260740"),
        ("site-base.css?v=20260735", "site-base.css?v=20260740"),
        ("remax-brand.css?v=20260735", "remax-brand.css?v=20260740"),
        ("seller-landing.css?v=20260735", "seller-landing.css?v=20260740"),
        ("seller-landing.css?v=20260737", "seller-landing.css?v=20260740"),
        ("buyer-landing.css?v=20260735", "buyer-landing.css?v=20260740"),
    ]:
        html = html.replace(old, new)
    return html


def insert_form_trust(html: str, lang: str) -> str:
    if "hero-form-trust" in html:
        return html
    trust = TRUST.get(lang)
    if not trust:
        return html
    # after form h2 + first p, before divider — seller/home forms
    patterns = [
        # <h2>...</h2>\n <p>...</p>\n <div class="divider"
        (
            r"(<form[^>]*class=\"[^\"]*form-card[^\"]*\"[^>]*>\s*"
            r"<h2>[^<]*</h2>\s*"
            r"<p>[^<]*</p>\s*)"
            r'(<div class="divider"></div>)'
        ),
        (
            r"(<form[^>]*class=\"[^\"]*form-card[^\"]*\"[^>]*>\s*"
            r"<h2>[^<]*</h2>\s*"
            r"<p>[^<]*</p>\s*)"
            r"(<input type=\"hidden\")"
        ),
    ]
    for pat in patterns:
        html2, n = re.subn(pat, rf"\1{trust}\n          \2", html, count=1, flags=re.S)
        if n:
            return html2
    # buyer hero card: after <h2>Let's talk</h2> or Parliamone
    m = re.search(
        r'(<aside class="buyer-hero-card[^"]*"[^>]*>\s*<h2>[^<]*</h2>\s*<p>[^<]*</p>\s*)',
        html,
    )
    if m:
        return html[: m.end()] + trust + "\n          " + html[m.end() :]
    return html


def seo_home_it(html: str) -> str:
    # twitter Maurizio-first
    html = html.replace(
        'content="Consulente Acquirenti e Investitori | Piraino"',
        'content="Maurizio Piraino | Consulente acquirenti e investitori · Milano"',
    )
    # og:locale
    if 'property="og:locale"' not in html:
        html = html.replace(
            '<meta property="og:type" content="website" />',
            '<meta property="og:type" content="website" />\n'
            '  <meta property="og:locale" content="it_IT" />\n'
            '  <meta property="og:site_name" content="Maurizio Piraino" />',
            1,
        )
    # hreflang en
    if 'hreflang="en"' not in html.split("</head>")[0]:
        html = html.replace(
            '<link rel="alternate" hreflang="it" href="https://mauriziopiraino.it/" />',
            '<link rel="alternate" hreflang="it" href="https://mauriziopiraino.it/" />\n'
            '<link rel="alternate" hreflang="en" href="https://mauriziopiraino.it/en/buy-home-milan/" />',
            1,
        )
    # schema street address
    if "streetAddress" not in html:
        html = html.replace(
            '"address": {\n    "@type": "PostalAddress",\n    "addressRegion": "Lombardia",\n    "addressCountry": "IT"\n  }',
            '"address": {\n    "@type": "PostalAddress",\n'
            '    "streetAddress": "Viale Gran Sasso 31",\n'
            '    "addressLocality": "Milano",\n'
            '    "addressRegion": "Lombardia",\n'
            '    "postalCode": "20131",\n'
            '    "addressCountry": "IT"\n  },\n'
            '  "worksFor": {\n'
            '    "@type": "Organization",\n'
            '    "name": "RE/MAX Associati Real Estate"\n  }',
            1,
        )
    # sharper meta description
    html = html.replace(
        'content="Consulente per acquirenti e investitori immobiliari a Milano e in Lombardia. Con la rete RE/MAX, accompagnamento anche nel resto d\'Italia. Property finding, analisi e assistenza fino al rogito."',
        'content="Maurizio Piraino, consulente per acquirenti e investitori a Milano. Property finding, analisi e tutela fino al rogito. RE/MAX a supporto — risposta entro 24h, nessun obbligo."',
    )
    return html


def seo_generic(html: str, lang: str) -> str:
    locales = {"it": "it_IT", "de": "de_DE", "fr": "fr_FR", "en": "en_US", "zh": "zh_CN"}
    loc = locales.get(lang, "it_IT")
    if 'property="og:locale"' not in html and 'property="og:type"' in html:
        html = html.replace(
            '<meta property="og:type" content="website" />',
            f'<meta property="og:type" content="website" />\n'
            f'  <meta property="og:locale" content="{loc}" />\n'
            f'  <meta property="og:site_name" content="Maurizio Piraino" />',
            1,
        )
    # twitter title if still | Piraino without Maurizio
    html = re.sub(
        r'(name="twitter:title" content=")([^"]*\| Piraino)(")',
        lambda m: m.group(1)
        + ("Maurizio Piraino | " + m.group(2).replace(" | Piraino", "").strip())
        + m.group(3)
        if "Maurizio" not in m.group(2)
        else m.group(0),
        html,
        count=1,
    )
    return html


def soft_mid_engage_it(html: str) -> str:
    """Compact engage band after situations on IT home if missing."""
    if "pb-engage-band" in html:
        return html
    band = """
    <section class="pb-engage-band" aria-label="Prossimo passo">
      <div class="container reveal">
        <div class="pb-engage-inner">
          <div>
            <p class="seller-mid-kicker">Passo successivo</p>
            <h2>Raccontami cosa stai cercando.</h2>
            <p>Casa o investimento: ti rispondo entro 24 ore, senza obbligo di incarico.</p>
          </div>
          <div class="seller-mid-actions">
            <a class="btn btn-red" href="#form">Prenota una consulenza</a>
            <a class="btn btn-light" href="https://wa.me/393514581993?text=Ciao%20Maurizio%2C%20vorrei%20una%20consulenza.">WhatsApp</a>
          </div>
        </div>
      </div>
    </section>
"""
    # insert before testimonials
    if 'id="recensioni"' in html:
        html = html.replace(
            '<section class="testimonials" id="recensioni">',
            band.strip() + '\n\n    <section class="testimonials" id="recensioni">',
            1,
        )
    return html


# CSS for engage band appended via polish file dynamically? add here to polish css via script
ENGAGE_CSS = """
/* Engage band */
.pb-engage-band {
  padding: 48px 0;
  background: linear-gradient(180deg, #fff 0%, var(--surface-tint, #e8eef8) 100%);
}
.pb-engage-inner {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 28px 32px;
  border-radius: 14px;
  background: #0c2749;
  color: #fff;
  box-shadow: 0 18px 48px rgba(12, 39, 73, .14);
}
.pb-engage-inner h2 {
  margin: 6px 0 8px;
  font-size: clamp(1.4rem, 2.4vw, 1.85rem);
  color: #fff !important;
}
.pb-engage-inner p {
  margin: 0;
  color: rgba(255,255,255,.82);
  max-width: 42ch;
}
.pb-engage-inner .seller-mid-kicker {
  color: rgba(255,255,255,.7);
  text-transform: uppercase;
  letter-spacing: .12em;
  font-size: 12px;
  font-weight: 700;
  margin: 0;
}
.pb-engage-inner .seller-mid-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.pb-engage-inner .btn-light {
  background: rgba(255,255,255,.1);
  color: #fff;
  border: 1px solid rgba(255,255,255,.35);
}
@media (max-width: 700px) {
  .pb-engage-inner { padding: 22px; }
  .pb-engage-inner .seller-mid-actions { width: 100%; }
  .pb-engage-inner .btn { flex: 1; justify-content: center; }
}
"""


def process(path: Path, lang: str) -> bool:
    html = path.read_text(encoding="utf-8")
    orig = html
    html = swap_font(html)
    html = bump_css(html)
    html = ensure_polish_css(html)
    html = insert_form_trust(html, lang)
    html = seo_generic(html, lang)
    if path.name == "index.html" and path.parent == ROOT and lang == "it":
        # only root IT home
        pass
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        html = seo_home_it(html)
        html = soft_mid_engage_it(html)
    if rel in {
        "comprare-casa-milano/index.html",
        "vendere-casa-milano/index.html",
        "en/buy-home-milan/index.html",
    }:
        # twitter already handled loosely
        if rel == "comprare-casa-milano/index.html":
            html = html.replace(
                'content="Vuoi comprare casa a Milano senza pagarla troppo? Analisi del prezzo giusto, verifica tecnica prima del rogito e ricerca mirata, anche tramite la rete RE/MAX."',
                'content="Comprare casa a Milano con Maurizio Piraino: analisi del prezzo, verifica tecnica e property finding. RE/MAX a supporto — risposta entro 24h."',
            )
        if rel == "vendere-casa-milano/index.html":
            html = re.sub(
                r'(name="description" content=")[^"]+(")',
                r'\1Vendere casa a Milano con metodo: analisi riservata, strategia di prezzo e piano di marketing. Maurizio Piraino — RE/MAX a supporto, nessun obbligo.\2',
                html,
                count=1,
            )
    if html != orig:
        path.write_text(html, encoding="utf-8")
        return True
    return False


def main() -> None:
    # append engage CSS to polish file once
    polish = ROOT / "assets/site-polish-v10.css"
    css = polish.read_text(encoding="utf-8")
    if ".pb-engage-band" not in css:
        polish.write_text(css.rstrip() + "\n" + ENGAGE_CSS, encoding="utf-8")
        print("engage CSS appended")

    changed = []
    for rel, lang in KEY_PAGES:
        p = ROOT / rel
        if not p.exists():
            print("skip missing", rel)
            continue
        if process(p, lang):
            changed.append(rel)
            print("updated", rel)
        else:
            print("unchanged", rel)

    # Also font+polish on remaining DE/FR seller/buyer hubs lightly
    extras = list(ROOT.glob("de/haus-*.html"))  # none
    for pattern in [
        "de/haus-kaufen/index.html",
        "fr/acheter-maison/index.html",
        "en/buy-home/index.html",
        "zh/mai-fang-milan/index.html",
    ]:
        p = ROOT / pattern
        if p.exists():
            lang = pattern.split("/")[0]
            if process(p, lang if lang != "zh" else "zh"):
                changed.append(pattern)
                print("updated", pattern)

    print(f"done ({len(changed)} files)")


if __name__ == "__main__":
    main()
