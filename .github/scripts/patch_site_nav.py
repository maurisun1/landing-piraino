#!/usr/bin/env python3
"""Patch site navigation: grouped desktop nav + organized mobile hamburger."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE = "20260720"

WA_ICON = (
    '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">'
    '<path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>'
    "</svg>"
)

NAV_CSS = f'<link rel="stylesheet" href="/assets/site-nav.css?v={CACHE}" />'
NAV_JS = f'<script src="/assets/site-nav.js?v={CACHE}" defer></script>'

TOPBAR_RE = re.compile(
    r'<div class="topbar">\s*<div class="container topbar-inner">.*?</div>\s*</div>\s*',
    re.DOTALL,
)
CHROME_HEADER_RE = re.compile(
    r'(?:<div class="site-chrome">\s*)?(?:<div class="topbar">\s*<div class="container topbar-inner">.*?</div>\s*</div>\s*)?<header class="site-header">.*?</header>(?:\s*</div>)?',
    re.DOTALL,
)
HEADER_RE = re.compile(
    r'<header(?:\s+class="[^"]*")?>.*?</header>\s*',
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

GUIDE_OMI = {
    "milano": "/guida-prezzi-mq-milano/",
    "bergamo": "/guida-prezzi-mq-bergamo/",
    "brescia": "/guida-prezzi-mq-brescia/",
}


def render_nav_group(label: str, links: list[str], *, extra_class: str = "") -> str:
    cls = f"nav-group {extra_class}".strip()
    links_html = "\n              ".join(links)
    return f"""          <div class="{cls}">
            <span class="nav-group-label">{label}</span>
            <div class="nav-group-links">
              {links_html}
            </div>
          </div>"""


SHORT_BRAND = "Maurizio Piraino"


def render_nav(
    *,
    tagline: str | None,
    brand: str,
    groups: list[str],
    lang_link: str | None,
    wa_url: str,
    wa_topbar: str,
    wa_short: str,
    cta_href: str,
    cta_label: str,
    lang: str = "it",
) -> str:
    menu_label = "Apri menu" if lang == "it" else "Open menu"
    aria_nav = "Menu principale" if lang == "it" else "Main menu"
    groups_html = "\n".join(groups)
    lang_block = ""
    if lang_link:
        lang_block = f"""
          <div class="nav-group nav-group-lang">
            {lang_link}
          </div>"""
    topbar = ""
    chrome_open = ""
    chrome_close = ""
    if tagline:
        chrome_open = '  <div class="site-chrome">\n'
        chrome_close = "\n</div>"
        topbar = f"""  <div class="topbar">
    <div class="container topbar-inner">
      <div class="topbar-tagline">{tagline}</div>
      <a class="topbar-wa topbar-wa-desktop" href="{wa_url}">{WA_ICON} {wa_topbar}</a>
    </div>
  </div>
"""
    return f"""{chrome_open}{topbar}  <header class="site-header">
    <div class="container site-nav">
      <div class="brand-wrap">
        <a class="brand" href="/">{brand}</a>
        <span class="remax-nav-badge">RE/MAX</span>
      </div>
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
{groups_html}{lang_block}
          <a class="btn btn-red nav-cta" href="{cta_href}">{cta_label}</a>
        </nav>
      </div>
      <div class="nav-backdrop" hidden></div>
    </div>
  </header>{chrome_close}"""


def ensure_assets(html: str) -> str:
    html = re.sub(
        r'\s*<script src="/assets/site-nav\.js[^"]*" defer></script>',
        "",
        html,
    )
    # Keep a single site-nav.css link (avoid duplicates from cache bumps / re-runs)
    html = re.sub(
        r'\s*<link rel="stylesheet" href="/assets/site-nav\.css\?v=\d+" />\s*',
        "\n",
        html,
    )
    if "</head>" in html:
        html = html.replace("</head>", f"  {NAV_CSS}\n</head>", 1)
    if NAV_JS not in html and "</body>" in html:
        html = html.replace("</body>", f"  {NAV_JS}\n</body>", 1)
    return html


def strip_nav_hide_rules(html: str) -> str:
    for rule in NAV_HIDE_RULES:
        html = re.sub(rule, "", html)
    html = re.sub(
        r"@media\(max-width:560px\)\{\.nav-links a\{display:none\}\.nav \.btn\{[^}]+\}\}",
        "",
        html,
    )
    return html


def replace_header(html: str, new_header: str) -> str:
    if CHROME_HEADER_RE.search(html):
        return CHROME_HEADER_RE.sub(new_header, html, count=1)
    html = TOPBAR_RE.sub("", html)
    if HEADER_RE.search(html):
        return HEADER_RE.sub(new_header, html, count=1)
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


def extract_wa_url(block: str) -> str:
    match = re.search(r'href="(https://wa\.me/[^"]+)"', block)
    return match.group(1) if match else "https://wa.me/393514581993"


def extract_tagline(block: str) -> str | None:
    match = re.search(r'<div class="topbar-tagline">(.*?)</div>', block, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def extract_brand(block: str) -> str:
    match = re.search(r'<a class="brand" href="/">(.*?)</a>', block, re.DOTALL)
    return match.group(1).strip() if match else 'Maurizio Piraino <span>·</span> RE/MAX'


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


def infer_tagline(path: Path, lang: str) -> str | None:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "Agente Immobiliare affiliato <strong>RE/MAX</strong> · Milano"
    if rel == "bergamo/index.html":
        return "Agente Immobiliare affiliato <strong>RE/MAX</strong> · Bergamo · Città Alta · Provincia"
    if rel == "brescia/index.html":
        return "Agente Immobiliare affiliato <strong>RE/MAX</strong> · Brescia · Franciacorta · Laghi"
    if rel.endswith("/index.html") and "/" in rel and not rel.startswith("comprare-casa") and not rel.startswith("en/"):
        slug = rel.split("/")[0]
        city = CITY_LABELS_IT.get(slug, slug.title())
        return f"Agente Immobiliare affiliato <strong>RE/MAX</strong> · {city}"
    if rel.startswith("comprare-casa-"):
        slug = rel.split("/")[0].replace("comprare-casa-", "")
        city = CITY_LABELS_IT.get(slug, slug.title())
        return f"Consulenza acquirenti <strong>RE/MAX</strong> · {city} · Risposta entro 24h"
    if rel.startswith("en/buy-home-"):
        slug = rel.split("/")[1].replace("buy-home-", "")
        city = CITY_LABELS_EN.get(slug, slug.title())
        return f"Buyer advisory <strong>RE/MAX</strong> · {city} · Reply within 24h"
    return None


def seller_nav_groups(*, sell_href: str, buy_href: str, lang: str = "it") -> list[str]:
    if lang == "en":
        return [
            render_nav_group(
                "Path",
                [
                    f'<a href="{sell_href}" class="nav-link-primary">Sell</a>',
                    f'<a href="{buy_href}">Buy</a>',
                ],
                extra_class="nav-group-path",
            ),
            render_nav_group(
                "About",
                [
                    '<a href="#metodo">Method</a>',
                    '<a href="#remax">RE/MAX</a>',
                ],
                extra_class="nav-group-info",
            ),
        ]
    return [
        render_nav_group(
            "Percorso",
            [
                f'<a href="{sell_href}" class="nav-link-primary">Vendere</a>',
                f'<a href="{buy_href}">Comprare</a>',
            ],
            extra_class="nav-group-path",
        ),
        render_nav_group(
            "Info",
            [
                '<a href="#metodo">Metodo</a>',
                '<a href="#remax">RE/MAX</a>',
            ],
            extra_class="nav-group-info",
        ),
    ]


def buyer_nav_groups(
    *,
    sell_href: str,
    omi_href: str,
    lang: str = "it",
) -> list[str]:
    if lang == "en":
        return [
            render_nav_group(
                "Path",
                [
                    '<a href="/comprare-casa/" class="nav-link-primary">Buy</a>',
                    f'<a href="{sell_href}">Sell</a>',
                ],
                extra_class="nav-group-path",
            ),
            render_nav_group(
                "About",
                [
                    '<a href="#metodo">Method</a>',
                    '<a href="#remax">RE/MAX</a>',
                    f'<a href="{omi_href}">OMI prices</a>',
                ],
                extra_class="nav-group-info",
            ),
        ]
    return [
        render_nav_group(
            "Percorso",
            [
                '<a href="/comprare-casa/" class="nav-link-primary">Comprare</a>',
                f'<a href="{sell_href}">Vendere</a>',
            ],
            extra_class="nav-group-path",
        ),
        render_nav_group(
            "Info",
            [
                '<a href="#metodo">Metodo</a>',
                '<a href="#remax">RE/MAX</a>',
                f'<a href="{omi_href}">Prezzi OMI</a>',
            ],
            extra_class="nav-group-info",
        ),
    ]


def hub_nav_groups(*, lang: str) -> list[str]:
    if lang == "en":
        return [
            render_nav_group(
                "Path",
                [
                    '<a href="/en/buy-home/" class="nav-link-primary">Buy</a>',
                    '<a href="/">Sell</a>',
                ],
                extra_class="nav-group-path",
            ),
            render_nav_group(
                "About",
                [
                    '<a href="#remax">RE/MAX</a>',
                    '<a href="/comprare-casa/">Provinces IT</a>',
                ],
                extra_class="nav-group-info",
            ),
        ]
    return [
        render_nav_group(
            "Percorso",
            [
                '<a href="/comprare-casa/" class="nav-link-primary">Comprare</a>',
                '<a href="/">Vendere</a>',
            ],
            extra_class="nav-group-path",
        ),
        render_nav_group(
            "Info",
            [
                '<a href="#remax">RE/MAX</a>',
                '<a href="/en/buy-home/">English</a>',
            ],
            extra_class="nav-group-info",
        ),
    ]


def guide_nav_groups(*, city: str, seller_href: str) -> list[str]:
    return [
        render_nav_group(
            "Percorso",
            [
                '<a href="/">Home</a>',
                '<a href="/comprare-casa/" class="nav-link-primary">Comprare</a>',
                f'<a href="{seller_href}">Vendere a {city}</a>',
            ],
            extra_class="nav-group-path",
        ),
    ]


def patch_page(path: Path, **nav_kwargs) -> bool:
    html = path.read_text(encoding="utf-8")
    block = extract_header_block(html)
    if not block:
        print(f"  skip (no header): {path}")
        return False

    new_header = render_nav(**nav_kwargs)
    html = replace_header(html, new_header)
    html = strip_nav_hide_rules(html)
    html = ensure_assets(html)
    path.write_text(html, encoding="utf-8")
    print(f"  patched: {path.relative_to(ROOT)}")
    return True


def seller_href_for_city(slug: str) -> str:
    return "/" if slug == "milano" else f"/{slug}/"


def en_buyer_slug(slug: str) -> str:
    return "milan" if slug == "milano" else slug


def seller_page_paths() -> list[tuple[str, str, str]]:
    pages = [("index.html", "/", "/en/buy-home-milan/")]
    for slug, _name, _en in __import__(
        "buyer_provinces", fromlist=["LOMBARD_PROVINCES"]
    ).LOMBARD_PROVINCES:
        if slug == "milano":
            continue
        pages.append(
            (
                f"{slug}/index.html",
                seller_href_for_city(slug),
                f"/en/buy-home-{en_buyer_slug(slug)}/",
            )
        )
    return pages


def buyer_omi_href(slug: str) -> str:
    if slug in GUIDE_OMI:
        return GUIDE_OMI[slug]
    return "#contatto"


def main() -> None:
    print("Patching seller pages...")
    for rel, sell, en_link in seller_page_paths():
        path = ROOT / rel
        if not path.exists():
            print(f"  skip (missing): {rel}")
            continue
        block = extract_header_block(path.read_text(encoding="utf-8"))
        patch_page(
            path,
            tagline=extract_tagline(block) or infer_tagline(path, "it"),
            brand=SHORT_BRAND,
            groups=seller_nav_groups(sell_href=sell, buy_href="/comprare-casa/"),
            lang_link=f'<a href="{en_link}" class="lang-link">EN</a>',
            wa_url=extract_wa_url(block),
            wa_topbar="WhatsApp",
            wa_short="WA",
            cta_href=extract_cta(block)[0],
            cta_label=extract_cta(block)[1],
            lang="it",
        )

    print("Patching buyer province pages...")
    for path in sorted(ROOT.glob("comprare-casa-*/index.html")):
        slug = path.parent.name.replace("comprare-casa-", "")
        block = extract_header_block(path.read_text(encoding="utf-8"))
        en_slug = "milan" if slug == "milano" else slug
        patch_page(
            path,
            tagline=extract_tagline(block) or infer_tagline(path, "it"),
            brand=SHORT_BRAND,
            groups=buyer_nav_groups(
                sell_href=seller_href_for_city(slug),
                omi_href=buyer_omi_href(slug),
            ),
            lang_link=f'<a href="/en/buy-home-{en_slug}/" class="lang-link">EN</a>',
            wa_url=extract_wa_url(block),
            wa_topbar="WhatsApp",
            wa_short="WA",
            cta_href=extract_cta(block)[0],
            cta_label=extract_cta(block)[1],
            lang="it",
        )

    for path in sorted(ROOT.glob("en/buy-home-*/index.html")):
        slug = path.parent.name.replace("buy-home-", "")
        it_slug = "milano" if slug == "milan" else slug
        block = extract_header_block(path.read_text(encoding="utf-8"))
        patch_page(
            path,
            tagline=extract_tagline(block) or infer_tagline(path, "en"),
            brand=SHORT_BRAND,
            groups=buyer_nav_groups(
                sell_href=seller_href_for_city(it_slug),
                omi_href=buyer_omi_href(it_slug),
                lang="en",
            ),
            lang_link=f'<a href="/comprare-casa-{it_slug}/" class="lang-link">IT</a>',
            wa_url=extract_wa_url(block),
            wa_topbar="WhatsApp",
            wa_short="WA",
            cta_href=extract_cta(block)[0],
            cta_label=extract_cta(block)[1],
            lang="en",
        )

    print("Patching hub pages...")
    for rel, lang in [("comprare-casa/index.html", "it"), ("en/buy-home/index.html", "en")]:
        path = ROOT / rel
        block = extract_header_block(path.read_text(encoding="utf-8"))
        if lang == "en":
            lang_link = '<a href="/comprare-casa/" class="lang-link">IT</a>'
            wa_text = "Message on WhatsApp"
        else:
            lang_link = '<a href="/en/buy-home/" class="lang-link">EN</a>'
            wa_text = "Scrivimi su WhatsApp"
        patch_page(
            path,
            tagline=extract_tagline(block)
            or (
                "Consulenza acquirenti <strong>RE/MAX</strong> · Lombardia · Risposta entro 24h"
                if lang == "it"
                else "Buyer advisory <strong>RE/MAX</strong> · Lombardy · Reply within 24h"
            ),
            brand=SHORT_BRAND,
            groups=hub_nav_groups(lang=lang),
            lang_link=lang_link,
            wa_url=extract_wa_url(block)
            or "https://wa.me/393514581993?text=Ciao%20Maurizio%2C%20sto%20cercando%20casa%20in%20Lombardia.",
            wa_topbar=wa_text,
            wa_short="WhatsApp",
            cta_href=extract_cta(block)[0],
            cta_label=extract_cta(block)[1],
            lang=lang,
        )

    print("Patching OMI guides...")
    for city, seller in [
        ("Milano", "/"),
        ("Bergamo", "/bergamo/"),
        ("Brescia", "/brescia/"),
    ]:
        path = ROOT / f"guida-prezzi-mq-{city.lower()}/index.html"
        wa_url = f"https://wa.me/393514581993?text=Ciao%20Maurizio%2C%20vorrei%20informazioni%20sui%20prezzi%20OMI%20a%20{city}."
        patch_page(
            path,
            tagline=f"Guida prezzi OMI · <strong>{city}</strong> · Dati Agenzia Entrate",
            brand="Maurizio Piraino",
            groups=guide_nav_groups(city=city, seller_href=seller),
            lang_link=None,
            wa_url=wa_url,
            wa_topbar="WhatsApp",
            wa_short="WA",
            cta_href=f"{seller}#form",
            cta_label="Richiedi analisi",
            lang="it",
        )

    print("Done.")


if __name__ == "__main__":
    main()
