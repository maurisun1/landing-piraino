#!/usr/bin/env python3
"""Patch site navigation: hamburger menu + prominent WhatsApp."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

WA_ICON = (
    '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">'
    '<path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>'
    "</svg>"
)

NAV_CSS = '<link rel="stylesheet" href="/assets/site-nav.css" />'
NAV_JS = '<script src="/assets/site-nav.js" defer></script>'

TOPBAR_RE = re.compile(
    r'<div class="topbar">\s*<div class="container topbar-inner">.*?</div>\s*</div>',
    re.DOTALL,
)
HEADER_RE = re.compile(
    r'<header(?:\s+class="[^"]*")?>.*?</header>',
    re.DOTALL,
)

NAV_HIDE_RULES = [
    r"\.nav-links a\{display:none\}",
    r"\.nav-links a \{ display: none; \}",
    r"\.topbar a\{display:none\}",
    r"\.topbar a \{ display: none; \}",
    r"\.nav \.btn\{display:none\}",
    r"\.nav \.btn \{ display: none; \}",
    r"@media\(max-width:560px\)\{\.nav-links a\{display:none\}[^}]*\}",
]


def render_nav(
    *,
    tagline: str | None,
    brand: str,
    links: list[str],
    wa_url: str,
    wa_topbar: str,
    wa_nav: str,
    wa_short: str,
    cta_href: str,
    cta_label: str,
    lang: str = "it",
) -> str:
    menu_label = "Apri menu" if lang == "it" else "Open menu"
    aria_nav = "Menu principale" if lang == "it" else "Main menu"
    links_html = "\n          ".join(links)
    topbar = ""
    if tagline:
        topbar = f"""  <div class="topbar">
    <div class="container topbar-inner">
      <div class="topbar-tagline">{tagline}</div>
      <a class="topbar-wa topbar-wa-desktop" href="{wa_url}">{WA_ICON} {wa_topbar}</a>
    </div>
  </div>
"""
    return f"""{topbar}  <header class="site-header">
    <div class="container site-nav">
      <a class="brand" href="/">{brand}</a>
      <div class="site-nav-actions">
        <a class="btn btn-wa nav-wa-compact" href="{wa_url}" aria-label="WhatsApp">{WA_ICON}<span class="nav-wa-label">{wa_short}</span></a>
        <button type="button" class="nav-toggle" aria-label="{menu_label}" aria-expanded="false" aria-controls="site-nav-panel">
          <span class="nav-toggle-bar"></span>
          <span class="nav-toggle-bar"></span>
          <span class="nav-toggle-bar"></span>
        </button>
      </div>
      <div class="nav-panel" id="site-nav-panel">
        <nav class="nav-links" aria-label="{aria_nav}">
          {links_html}
          <a class="btn btn-wa nav-wa-full" href="{wa_url}">{WA_ICON} {wa_nav}</a>
          <a class="btn btn-red nav-cta" href="{cta_href}">{cta_label}</a>
        </nav>
      </div>
      <div class="nav-backdrop" hidden></div>
    </div>
  </header>"""


def ensure_assets(html: str) -> str:
    if NAV_CSS not in html:
        if "</head>" in html:
            html = html.replace("</head>", f"  {NAV_CSS}\n</head>", 1)
        elif "<body>" in html:
            html = html.replace("<body>", f"{NAV_CSS}\n<body>", 1)
    if NAV_JS not in html:
        html = html.replace("</body>", f"  {NAV_JS}\n</body>", 1)
    return html


def strip_nav_hide_rules(html: str) -> str:
    for rule in NAV_HIDE_RULES:
        html = re.sub(rule, "", html)
    html = re.sub(r"@media\(max-width:560px\)\{\.nav-links a\{display:none\}\.nav \.btn\{[^}]+\}\}", "", html)
    return html


def extract_header_block(html: str) -> str:
    parts = []
    topbar = TOPBAR_RE.search(html)
    header = HEADER_RE.search(html)
    if topbar:
        parts.append(topbar.group(0))
    if header:
        parts.append(header.group(0))
    return "\n".join(parts)


def replace_header(html: str, new_header: str) -> str:
    html = TOPBAR_RE.sub("", html)
    if HEADER_RE.search(html):
        return HEADER_RE.sub(new_header, html, count=1)
    return html


CITY_LABELS_IT = {
    "milano": "Milano",
    "bergamo": "Bergamo",
    "brescia": "Brescia",
    "como": "Como",
    "varese": "Varese",
    "lecco": "Lecco",
    "monza": "Monza e Brianza",
    "sondrio": "Sondrio",
    "cremona": "Cremona",
    "lodi": "Lodi",
    "mantova": "Mantova",
    "pavia": "Pavia",
}

CITY_LABELS_EN = {
    "milan": "Milan",
    "bergamo": "Bergamo",
    "brescia": "Brescia",
    "como": "Como",
    "varese": "Varese",
    "lecco": "Lecco",
    "monza": "Monza and Brianza",
    "sondrio": "Sondrio",
    "cremona": "Cremona",
    "lodi": "Lodi",
    "mantova": "Mantova",
    "pavia": "Pavia",
}


def infer_tagline(path: Path, lang: str) -> str | None:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "Agente Immobiliare affiliato <strong>RE/MAX</strong> · Milano"
    if rel == "bergamo/index.html":
        return "Agente Immobiliare affiliato <strong>RE/MAX</strong> · Bergamo · Città Alta · Provincia"
    if rel == "brescia/index.html":
        return "Agente Immobiliare affiliato <strong>RE/MAX</strong> · Brescia · Franciacorta · Laghi"
    if rel.startswith("comprare-casa-"):
        slug = rel.split("/")[0].replace("comprare-casa-", "")
        city = CITY_LABELS_IT.get(slug, slug.title())
        return f"Consulenza acquirenti <strong>RE/MAX</strong> · {city} · Risposta entro 24h"
    if rel.startswith("en/buy-home-"):
        slug = rel.split("/")[1].replace("buy-home-", "")
        city = CITY_LABELS_EN.get(slug, slug.title())
        return f"Buyer advisory <strong>RE/MAX</strong> · {city} · Reply within 24h"
    return None


def extract_wa_url(block: str) -> str:
    match = re.search(r'href="(https://wa\.me/[^"]+)"', block)
    return match.group(1) if match else "https://wa.me/393514581993"


def extract_tagline(block: str) -> str | None:
    match = re.search(r'<div class="topbar-tagline">(.*?)</div>', block, re.DOTALL)
    if match:
        return match.group(1).strip()
    match = re.search(r'<div class="topbar-inner">\s*<div[^>]*>(.*?)</div>', block, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def extract_brand(block: str) -> str:
    match = re.search(r'<a class="brand" href="/">(.*?)</a>', block, re.DOTALL)
    return match.group(1).strip() if match else 'Maurizio Piraino <span>·</span> RE/MAX'


def extract_nav_links(block: str) -> list[str]:
    nav_match = re.search(r'<nav class="nav-links"[^>]*>(.*?)</nav>', block, re.DOTALL)
    if not nav_match:
        return []
    inner = nav_match.group(1)
    links = []
    for match in re.finditer(r"<a\b[^>]*>.*?</a>", inner, re.DOTALL):
        tag = match.group(0)
        if "btn-wa" in tag or "nav-cta" in tag:
            continue
        if 'class="btn btn-red"' in tag or ('class="btn"' in tag and "btn-red" not in tag):
            continue
        links.append(tag.strip())
    return links


def extract_cta(block: str) -> tuple[str, str]:
    for pattern in (
        r'<a class="btn btn-red nav-cta" href="([^"]+)">(.*?)</a>',
        r'<a class="btn btn-red" href="([^"]+)">(.*?)</a>',
        r'<a class="btn nav-cta" href="([^"]+)">(.*?)</a>',
        r'<a class="btn" href="([^"]+)">(.*?)</a>',
    ):
        match = re.search(pattern, block, re.DOTALL)
        if match:
            return match.group(1), re.sub(r"\s+", " ", match.group(2)).strip()
    return "#contatto", "Contatto"


def patch_standard_page(path: Path, *, lang: str, wa_topbar: str, wa_nav: str, wa_short: str, extra_links: list[str] | None = None) -> bool:
    html = path.read_text(encoding="utf-8")
    block = extract_header_block(html)
    if not block:
        print(f"  skip (no header): {path}")
        return False
    wa_url = extract_wa_url(block)
    tagline = extract_tagline(block) or infer_tagline(path, lang)
    brand = extract_brand(block)
    links = extract_nav_links(block)
    cta_href, cta_label = extract_cta(block)

    if extra_links:
        for link in extra_links:
            href = re.search(r'href="([^"]+)"', link).group(1)
            if not any(href in existing for existing in links):
                insert_at = 2 if len(links) >= 2 else len(links)
                links.insert(insert_at, link)

    new_header = render_nav(
        tagline=tagline,
        brand=brand,
        links=links,
        wa_url=wa_url,
        wa_topbar=wa_topbar,
        wa_nav=wa_nav,
        wa_short=wa_short,
        cta_href=cta_href,
        cta_label=cta_label,
        lang=lang,
    )

    html = replace_header(html, new_header)
    html = strip_nav_hide_rules(html)
    html = ensure_assets(html)
    path.write_text(html, encoding="utf-8")
    print(f"  patched: {path.relative_to(ROOT)}")
    return True


def patch_hub(path: Path, *, lang: str) -> bool:
    is_en = lang == "en"
    html = path.read_text(encoding="utf-8")
    block = extract_header_block(html)
    if not block:
        return False
    brand = extract_brand(block)
    cta_href, cta_label = extract_cta(block)

    if is_en:
        tagline = "Buyer advisory <strong>RE/MAX</strong> · Lombardy · Reply within 24h"
        links = [
            '<a href="/">Sell</a>',
            '<a href="/en/buy-home/">Provinces</a>',
            '<a href="/comprare-casa/" class="lang-link">IT</a>',
        ]
        wa_url = "https://wa.me/393514581993?text=Hi%20Maurizio%2C%20I%20am%20looking%20to%20buy%20in%20Lombardy%20and%20would%20like%20buyer%20advisory."
        wa_topbar = wa_nav = "Message on WhatsApp"
        wa_short = "WhatsApp"
    else:
        tagline = "Consulenza acquirenti <strong>RE/MAX</strong> · Lombardia · Risposta entro 24h"
        links = [
            '<a href="/">Vendere</a>',
            '<a href="/comprare-casa/">Province</a>',
            '<a href="/en/buy-home/" class="lang-link">EN</a>',
        ]
        wa_url = "https://wa.me/393514581993?text=Ciao%20Maurizio%2C%20sto%20cercando%20casa%20in%20Lombardia%20e%20vorrei%20una%20consulenza%20acquirente."
        wa_topbar = wa_nav = "Scrivimi su WhatsApp"
        wa_short = "WhatsApp"

    new_header = render_nav(
        tagline=tagline,
        brand=brand,
        links=links,
        wa_url=wa_url,
        wa_topbar=wa_topbar,
        wa_nav=wa_nav,
        wa_short=wa_short,
        cta_href=cta_href,
        cta_label=cta_label,
        lang=lang,
    )
    html = replace_header(html, new_header)
    html = strip_nav_hide_rules(html)
    html = ensure_assets(html)
    path.write_text(html, encoding="utf-8")
    print(f"  patched hub: {path.relative_to(ROOT)}")
    return True


def patch_guide(path: Path, *, city: str, seller_href: str) -> bool:
    html = path.read_text(encoding="utf-8")
    wa_url = f"https://wa.me/393514581993?text=Ciao%20Maurizio%2C%20vorrei%20informazioni%20sui%20prezzi%20OMI%20a%20{city}."
    new_header = render_nav(
        tagline=f"Guida prezzi OMI · <strong>{city}</strong> · Dati Agenzia Entrate",
        brand="Maurizio Piraino",
        links=[
            '<a href="/">Home</a>',
            '<a href="/comprare-casa/">Comprare</a>',
            f'<a href="{seller_href}">Vendere a {city}</a>',
        ],
        wa_url=wa_url,
        wa_topbar="WhatsApp",
        wa_nav="Scrivimi su WhatsApp",
        wa_short="WA",
        cta_href=f"{seller_href}#form",
        cta_label="Richiedi analisi",
        lang="it",
    )
    html = replace_header(html, new_header)
    html = ensure_assets(html)
    path.write_text(html, encoding="utf-8")
    print(f"  patched guide: {path.relative_to(ROOT)}")
    return True


def main() -> None:
    print("Patching seller pages...")
    patch_standard_page(
        ROOT / "index.html",
        lang="it",
        wa_topbar="WhatsApp",
        wa_nav="Consulenza su WhatsApp",
        wa_short="WA",
    )
    for city, extra in [("bergamo", '<a href="/comprare-casa/">Comprare</a>'), ("brescia", '<a href="/comprare-casa/">Comprare</a>')]:
        patch_standard_page(
            ROOT / city / "index.html",
            lang="it",
            wa_topbar="WhatsApp",
            wa_nav="Consulenza su WhatsApp",
            wa_short="WA",
            extra_links=[extra],
        )

    print("Patching buyer province pages...")
    for path in sorted(ROOT.glob("comprare-casa-*/index.html")):
        patch_standard_page(
            path,
            lang="it",
            wa_topbar="WhatsApp",
            wa_nav="Scrivimi su WhatsApp",
            wa_short="WA",
        )
    for path in sorted(ROOT.glob("en/buy-home-*/index.html")):
        patch_standard_page(
            path,
            lang="en",
            wa_topbar="WhatsApp",
            wa_nav="Message on WhatsApp",
            wa_short="WA",
        )

    print("Patching hub pages...")
    patch_hub(ROOT / "comprare-casa/index.html", lang="it")
    patch_hub(ROOT / "en/buy-home/index.html", lang="en")

    print("Patching OMI guides...")
    patch_guide(ROOT / "guida-prezzi-mq-milano/index.html", city="Milano", seller_href="/")
    patch_guide(ROOT / "guida-prezzi-mq-bergamo/index.html", city="Bergamo", seller_href="/bergamo/")
    patch_guide(ROOT / "guida-prezzi-mq-brescia/index.html", city="Brescia", seller_href="/brescia/")

    print("Done.")


if __name__ == "__main__":
    main()
