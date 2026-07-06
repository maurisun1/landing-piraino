#!/usr/bin/env python3
"""Apply SEO/UX audit improvements across the site."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

FAVICON_LINKS = """<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="apple-touch-icon" href="/favicon.svg" />"""

BASE_CSS = '<link rel="stylesheet" href="/assets/site-base.css?v=20260709" />'
REMAX_BRAND_CSS = '<link rel="stylesheet" href="/assets/remax-brand.css?v=20260709" />'
DUAL_PATH_CSS = '<link rel="stylesheet" href="/assets/dual-path.css?v=20260709" />'

PROVINCE_HERO = {
    "milano": ("/milano.jpg", "Milano", "Milano"),
    "bergamo": ("/bergamo.jpg", "Bergamo", "Bergamo"),
    "brescia": ("/brescia.jpg", "Brescia", "Brescia"),
    "como": ("/como.jpg", "Como", "Como"),
    "varese": ("/varese.jpg", "Varese", "Varese"),
    "lecco": ("/lecco.jpg", "Lecco", "Lecco"),
    "monza": ("/monza.jpg", "Monza e Brianza", "Monza e Brianza"),
    "sondrio": ("/sondrio.jpg", "Sondrio", "Sondrio"),
    "cremona": ("/cremona.jpg", "Cremona", "Cremona"),
    "lodi": ("/lodi.jpg", "Lodi", "Lodi"),
    "mantova": ("/mantova.jpg", "Mantova", "Mantova"),
    "pavia": ("/pavia.jpg", "Pavia", "Pavia"),
    "milan": ("/milano.jpg", "Milan", "Milan"),
}

DUAL_PATH = {
    "index.html": {
        "sell_href": "#form",
        "sell_title": "Analisi del tuo immobile",
        "sell_p": "Valutazione riservata su dati OMI e micro-zona. Nessun obbligo di incarico.",
        "sell_cta": "Richiedi analisi →",
        "buy_href": "/comprare-casa-milano/",
        "buy_title": "Consulenza acquirente",
        "buy_p": "Milano e 12 province lombarde. Non pagare l'emozione del momento.",
        "buy_cta": "Comprare a Milano →",
    },
    "bergamo/index.html": {
        "sell_href": "#form",
        "sell_title": "Analisi del tuo immobile",
        "sell_p": "Valutazione riservata su Bergamo, valli e provincia. Nessun obbligo di incarico.",
        "sell_cta": "Richiedi analisi →",
        "buy_href": "/comprare-casa-bergamo/",
        "buy_title": "Consulenza acquirente",
        "buy_p": "Comprare a Bergamo senza pagare troppo. Analisi OMI e verifica tecnica.",
        "buy_cta": "Comprare a Bergamo →",
    },
    "brescia/index.html": {
        "sell_href": "#form",
        "sell_title": "Analisi del tuo immobile",
        "sell_p": "Valutazione su città, Franciacorta e laghi. Nessun obbligo di incarico.",
        "sell_cta": "Richiedi analisi →",
        "buy_href": "/comprare-casa-brescia/",
        "buy_title": "Consulenza acquirente",
        "buy_p": "Comprare a Brescia con metodo: laghi, colline e città.",
        "buy_cta": "Comprare a Brescia →",
    },
}


def ensure_head_assets(html: str, *, dual_path: bool = False, preload: str | None = None) -> str:
    if FAVICON_LINKS not in html:
        html = html.replace("<meta charset", f"{FAVICON_LINKS}\n  <meta charset", 1)
    if BASE_CSS not in html:
        html = html.replace("</head>", f"  {BASE_CSS}\n  {REMAX_BRAND_CSS}\n</head>", 1)
    elif REMAX_BRAND_CSS not in html:
        html = html.replace(BASE_CSS, f"{BASE_CSS}\n  {REMAX_BRAND_CSS}", 1)
    if dual_path and DUAL_PATH_CSS not in html:
        html = html.replace("</head>", f"  {DUAL_PATH_CSS}\n</head>", 1)
    if preload and f'href="{preload}"' not in html:
        html = html.replace(
            "</head>",
            f'  <link rel="preload" as="image" href="{preload}" fetchpriority="high" />\n</head>',
            1,
        )
    return html


def ensure_skip_link(html: str) -> str:
    skip = '<a class="skip-link" href="#main">Salta al contenuto</a>'
    if skip in html:
        return html
    return html.replace("<body>", f"<body>\n  {skip}", 1)


def inject_dual_path(html: str, cfg: dict) -> str:
    block = f"""
    <section class="dual-path" aria-label="Scegli il tuo percorso">
      <div class="container dual-path-grid">
        <p class="dual-path-intro"><em>RE/MAX</em> · Scegli il tuo percorso</p>
        <a class="dual-path-card dual-path-sell" href="{cfg['sell_href']}">
          <span class="dual-path-label">Vuoi vendere</span>
          <strong>{cfg['sell_title']}</strong>
          <p>{cfg['sell_p']}</p>
          <span class="dual-path-cta">{cfg['sell_cta']}</span>
        </a>
        <a class="dual-path-card dual-path-buy" href="{cfg['buy_href']}">
          <span class="dual-path-label">Cerchi casa</span>
          <strong>{cfg['buy_title']}</strong>
          <p>{cfg['buy_p']}</p>
          <span class="dual-path-cta">{cfg['buy_cta']}</span>
        </a>
      </div>
    </section>"""
    if 'class="dual-path"' in html:
        return html
    for pattern in (
        "</section>\n\n    <section>",
        "</section>\n    <section>",
    ):
        if pattern in html:
            return html.replace(pattern, f"</section>{block}\n    <section>", 1)
    return html


def remove_late_buyer_section(html: str) -> str:
    pattern = re.compile(
        r'\s*<section class="final-cta" style="background:var\(--cream\)[^"]*"[^>]*>.*?Per chi compra.*?</section>',
        re.DOTALL,
    )
    return pattern.sub("", html)


def add_en_nav_link(html: str) -> str:
    if 'href="/en/buy-home-milan/"' in html or 'href="/en/buy-home/"' in html:
        return html
    return html.replace(
        '<a href="/comprare-casa/">Comprare</a>',
        '<a href="/comprare-casa/">Comprare</a>\n          <a href="/en/buy-home-milan/" class="lang-link">EN</a>',
        1,
    )


def unify_seller_schema(html: str) -> str:
    agent_block = {
        "@context": "https://schema.org",
        "@type": "RealEstateAgent",
        "@id": "https://mauriziopiraino.it/#agent",
        "name": "Maurizio Piraino",
        "url": "https://mauriziopiraino.it/",
        "image": "https://mauriziopiraino.it/foto.jpg",
        "telephone": "+393514581993",
        "email": "maurizio.piraino@remax.it",
        "address": {
            "@type": "PostalAddress",
            "addressRegion": "Lombardia",
            "addressCountry": "IT",
        },
        "areaServed": ["Milano", "Bergamo", "Brescia", "Lombardia"],
        "description": "Agente Immobiliare affiliato RE/MAX. Consulenza per venditori e acquirenti in Lombardia.",
        "sameAs": ["https://www.instagram.com/mauriziopiraino.immobiliare"],
    }
    website = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Maurizio Piraino — RE/MAX",
        "url": "https://mauriziopiraino.it/",
        "inLanguage": "it-IT",
        "publisher": {"@id": "https://mauriziopiraino.it/#agent"},
    }
    agent_json = json.dumps(agent_block, ensure_ascii=False, indent=2)
    website_json = json.dumps(website, ensure_ascii=False)

    html = re.sub(
        r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "RealEstateAgent"[\s\S]*?\}\s*</script>',
        f'<script type="application/ld+json">\n  {agent_json}\n  </script>',
        html,
        count=1,
    )
    html = re.sub(
        r'<script type="application/ld\+json">\{"@context":"https://schema.org","@type":"RealEstateAgent"[\s\S]*?\}</script>',
        f'<script type="application/ld+json">\n  {agent_json}\n  </script>',
        html,
        count=1,
    )

    # Remove duplicate WebSite blocks, then ensure exactly one exists before FAQ
    html = re.sub(
        r'<script type="application/ld\+json">\s*\{"@context": "https://schema.org", "@type": "WebSite"[\s\S]*?\}\s*</script>\s*',
        "",
        html,
    )
    if '"@type": "FAQPage"' in html and website_json not in html:
        html = html.replace(
            '<script type="application/ld+json">',
            f'<script type="application/ld+json">\n  {website_json}\n  </script>\n  <script type="application/ld+json">',
            1,
        )
    return html


def detect_province_slug(path: Path) -> str | None:
    name = path.parent.name
    if name.startswith("comprare-casa-"):
        return name.replace("comprare-casa-", "")
    if name.startswith("buy-home-"):
        return name.replace("buy-home-", "")
    return None


def patch_buyer_page(path: Path) -> None:
    slug = detect_province_slug(path)
    if not slug or slug not in PROVINCE_HERO:
        return
    img, alt_it, alt_en = PROVINCE_HERO[slug]
    is_en = "/en/" in str(path)
    alt = alt_en if is_en else alt_it

    html = path.read_text(encoding="utf-8")
    html = ensure_head_assets(html, preload=img)
    html = ensure_skip_link(html)

    html = re.sub(
        r'<section class="buyer-hero-pro" style="--hero-img: url\(\'[^\']+\'\)">',
        f'<section class="buyer-hero-pro">\n      <img class="buyer-hero-img" src="{img}" alt="{alt}" width="1920" height="1080" fetchpriority="high" decoding="async" />',
        html,
        count=1,
    )
    html = html.replace("<main>", '<main id="main">', 1)
    html = re.sub(
        r'(<aside class="buyer-hero-card[^>]*>\s*)<h3>(.*?)</h3>',
        r"\1<h2>\2</h2>",
        html,
        count=1,
        flags=re.DOTALL,
    )
    # Fix accidental h2 in first pain card from prior runs
    html = re.sub(
        r'(<article class="buyer-pain-card reveal"><div class="num">01</div>)<h2>(.*?)</h[23]>',
        r"\1<h3>\2</h3>",
        html,
        count=1,
    )

    html = html.replace(
        '<div class="buyer-sticky-bar">',
        '<div class="buyer-sticky-bar" role="region" aria-label="Azioni rapide">',
        1,
    )

    path.write_text(html, encoding="utf-8")
    print(f"  buyer: {path.relative_to(ROOT)}")


def patch_seller_page(rel: str) -> None:
    path = ROOT / rel
    html = path.read_text(encoding="utf-8")
    preload = "/milano.jpg" if rel == "index.html" else f"/{rel.split('/')[0]}.jpg"
    html = ensure_head_assets(html, dual_path=True, preload=preload)
    html = ensure_skip_link(html)
    html = inject_dual_path(html, DUAL_PATH[rel])
    html = remove_late_buyer_section(html)
    html = add_en_nav_link(html)
    html = unify_seller_schema(html)
    html = html.replace("<main>", '<main id="main">', 1)
    path.write_text(html, encoding="utf-8")
    print(f"  seller: {rel}")


def patch_omi_guide(path: Path, city: str, buyer_path: str, seller_path: str) -> None:
    html = path.read_text(encoding="utf-8")
    html = ensure_head_assets(html)
    html = ensure_skip_link(html)

    if "twitter:card" not in html:
        html = html.replace(
            "</head>",
            '  <meta name="twitter:card" content="summary_large_image" />\n</head>',
            1,
        )

    buyer_link = f'<a href="{buyer_path}">Comprare casa a {city}</a>'
    if buyer_link not in html:
        html = html.replace(
            '<div class="links">',
            f'<div class="links">\n    {buyer_link}',
            1,
        )

    cta_buyer = f'<p style="margin-top:14px"><a href="{buyer_path}" style="color:var(--red);font-weight:700">Stai comprando a {city}? Consulenza acquirente →</a></p>'
    if buyer_path not in html:
        html = html.replace(
            '<div class="cta">',
            f'{cta_buyer}\n  <div class="cta">',
            1,
        )

    html = re.sub(
        r'"@type": "Article"[\s\S]*?"citation": "[^"]+"\s*\}',
        lambda m: m.group(0).rstrip("}") + ',\n  "url": "https://mauriziopiraino.it' + str(path.relative_to(ROOT).parent) + '/",\n  "inLanguage": "it-IT",\n  "mainEntityOfPage": "https://mauriziopiraino.it' + str(path.relative_to(ROOT).parent) + '/"\n}',
        html,
        count=1,
    )

    html = html.replace("<main>", '<main id="main">', 1)
    path.write_text(html, encoding="utf-8")
    print(f"  omi: {path.relative_to(ROOT)}")


def main() -> None:
    print("Seller pages...")
    for rel in DUAL_PATH:
        patch_seller_page(rel)

    print("Buyer pages...")
    for path in sorted(ROOT.glob("comprare-casa-*/index.html")):
        patch_buyer_page(path)
    for path in sorted(ROOT.glob("en/buy-home-*/index.html")):
        patch_buyer_page(path)

    print("OMI guides...")
    patch_omi_guide(ROOT / "guida-prezzi-mq-milano/index.html", "Milano", "/comprare-casa-milano/", "/")
    patch_omi_guide(ROOT / "guida-prezzi-mq-bergamo/index.html", "Bergamo", "/comprare-casa-bergamo/", "/bergamo/")
    patch_omi_guide(ROOT / "guida-prezzi-mq-brescia/index.html", "Brescia", "/comprare-casa-brescia/", "/brescia/")

    print("Done.")


if __name__ == "__main__":
    main()
