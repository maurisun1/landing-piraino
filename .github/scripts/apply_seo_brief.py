#!/usr/bin/env python3
"""Apply SEO brief fixes (web design manager, Sept 2026).

Priority 1: Seller city hreflang must NOT point EN → buy-home (wrong intent).
            Keep only IT/DE/FR reciprocal seller alternates.
Priority 2: Template-level related-links on seller provinces + homepage mesh.
Priority 3: Stronger title/meta + schema hygiene on guida-prezzi-mq-milano.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from buyer_provinces import LOMBARD_PROVINCES  # noqa: E402
from locales import (  # noqa: E402
    buyer_province_url,
    city_label,
    seller_hub_url,
    seller_page_path,
    seller_url,
)

BASE = "https://mauriziopiraino.it"

ALT_RE = re.compile(
    r'\s*<link rel="alternate" hreflang="[^"]+" href="[^"]+"\s*/?>',
    re.IGNORECASE,
)
CANONICAL_RE = re.compile(
    r'(<link rel="canonical" href="[^"]+"\s*/?>)',
    re.IGNORECASE,
)
RELATED_RE = re.compile(
    r'\s*<nav class="seo-related"[^>]*>.*?</nav>\s*',
    re.DOTALL | re.IGNORECASE,
)
HOME_MESH_RE = re.compile(
    r'\s*<section class="seo-home-mesh"[^>]*>.*?</section>\s*',
    re.DOTALL | re.IGNORECASE,
)

OMI_GUIDES = {
    "milano": "/guida-prezzi-mq-milano/",
    "bergamo": "/guida-prezzi-mq-bergamo/",
    "brescia": "/guida-prezzi-mq-brescia/",
}

RELATED_COPY = {
    "it": {
        "aria": "Pagine correlate",
        "title": "Approfondisci",
        "omi": "Prezzi al mq OMI — {city}",
        "buy": "Comprare casa a {city}",
        "sell_hub": "Vendere casa in Lombardia",
        "buy_hub": "Property Finding in Lombardia",
    },
    "de": {
        "aria": "Verwandte Seiten",
        "title": "Weiterführend",
        "omi": "OMI-Preise pro m² — {city}",
        "buy": "Haus kaufen in {city}",
        "sell_hub": "Haus verkaufen in der Lombardei",
        "buy_hub": "Property Finding in der Lombardei",
    },
    "fr": {
        "aria": "Pages liées",
        "title": "À voir aussi",
        "omi": "Prix au m² OMI — {city}",
        "buy": "Acheter une maison à {city}",
        "sell_hub": "Vendre en Lombardie",
        "buy_hub": "Property Finding en Lombardie",
    },
}


def abs_url(path: str) -> str:
    return path if path.startswith("http") else BASE + path


def hreflang_block(urls: dict[str, str], *, x_default: str | None = None) -> str:
    lines = [
        f'<link rel="alternate" hreflang="{lang}" href="{url}" />'
        for lang, url in urls.items()
    ]
    default = x_default or urls.get("it") or next(iter(urls.values()))
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{default}" />')
    return "\n".join(lines)


def inject_hreflang(html: str, urls: dict[str, str], *, x_default: str | None = None) -> str:
    block = hreflang_block(urls, x_default=x_default)
    html = ALT_RE.sub("", html)
    m = CANONICAL_RE.search(html)
    if not m:
        return html.replace("</head>", f"{block}\n</head>", 1)
    return html[: m.end()] + "\n" + block + html[m.end() :]


def seller_hreflang_urls(slug: str) -> dict[str, str]:
    """Only same-intent seller pages (IT/DE/FR). No EN — there is no EN seller landing."""
    return {
        "it": abs_url(seller_url(slug, "it")),
        "de": abs_url(seller_url(slug, "de")),
        "fr": abs_url(seller_url(slug, "fr")),
    }


def seller_hub_hreflang_urls() -> dict[str, str]:
    return {
        "it": abs_url(seller_hub_url("it")),
        "de": abs_url(seller_hub_url("de")),
        "fr": abs_url(seller_hub_url("fr")),
    }


def related_block(slug: str, lang: str) -> str:
    c = RELATED_COPY[lang]
    city = city_label(slug, lang)
    links: list[str] = []
    if slug in OMI_GUIDES:
        links.append(f'<a href="{OMI_GUIDES[slug]}">{c["omi"].format(city=city)}</a>')
    links.append(f'<a href="{buyer_province_url(slug, lang)}">{c["buy"].format(city=city)}</a>')
    links.append(f'<a href="{seller_hub_url(lang)}">{c["sell_hub"]}</a>')
    buy_hub = {
        "it": "/comprare-casa/",
        "de": "/de/haus-kaufen/",
        "fr": "/fr/acheter-maison/",
    }[lang]
    links.append(f'<a href="{buy_hub}">{c["buy_hub"]}</a>')
    items = "\n    ".join(f"<li>{link}</li>" for link in links)
    return (
        f'<nav class="seo-related" aria-label="{c["aria"]}">\n'
        f'  <div class="container">\n'
        f'    <p class="seo-related-title">{c["title"]}</p>\n'
        f"    <ul>\n    {items}\n    </ul>\n"
        f"  </div>\n"
        f"</nav>\n"
    )


def inject_before_footer(html: str, block: str) -> str:
    if "<footer" in html:
        return html.replace("<footer", block + "<footer", 1)
    if "</main>" in html:
        return html.replace("</main>", block + "</main>", 1)
    return html.replace("</body>", block + "</body>", 1)


def fix_seller_hreflang_and_related() -> int:
    changed = 0
    for slug, _it, _en in LOMBARD_PROVINCES:
        urls = seller_hreflang_urls(slug)
        for lang in ("it", "de", "fr"):
            rel = seller_page_path(slug, lang)
            path = ROOT / rel
            if not path.exists():
                continue
            html = path.read_text(encoding="utf-8")
            html = inject_hreflang(html, urls)
            html = RELATED_RE.sub("\n", html)
            html = inject_before_footer(html, related_block(slug, lang))
            path.write_text(html, encoding="utf-8")
            print(f"  seller: {rel}")
            changed += 1

    # Milan ZH seller if present — keep zh + IT/DE/FR, no EN buy
    zh = ROOT / "zh" / "chu-shou-milan" / "index.html"
    if zh.exists():
        urls = seller_hreflang_urls("milano")
        urls["zh-Hans"] = f"{BASE}/zh/chu-shou-milan/"
        html = inject_hreflang(zh.read_text(encoding="utf-8"), urls)
        zh.write_text(html, encoding="utf-8")
        print("  seller: zh/chu-shou-milan/")
        changed += 1

    # Seller hubs: drop EN alternate that shared IT URL
    for lang in ("it", "de", "fr"):
        path = ROOT / seller_hub_url(lang).strip("/") / "index.html"
        if not path.exists():
            continue
        html = inject_hreflang(path.read_text(encoding="utf-8"), seller_hub_hreflang_urls())
        path.write_text(html, encoding="utf-8")
        print(f"  seller hub: {path.relative_to(ROOT)}")
        changed += 1
    return changed


def patch_homepage_mesh() -> bool:
    path = ROOT / "index.html"
    html = path.read_text(encoding="utf-8")
    html = HOME_MESH_RE.sub("\n", html)
    province_links = []
    for slug, name, _en in LOMBARD_PROVINCES:
        href = seller_url(slug, "it")
        province_links.append(f'<a href="{href}">{name}</a>')
    buy_links = []
    for slug, name, _en in LOMBARD_PROVINCES:
        buy_links.append(f'<a href="{buyer_province_url(slug, "it")}">{name}</a>')
    mesh = (
        '<section class="seo-home-mesh" aria-label="Esplora province e guide">'
        '<div class="container">'
        "<h2>Province e guide utili</h2>"
        "<p>Scegli la provincia per una valutazione di vendita, "
        "oppure consulta i valori OMI ufficiali e le pagine per chi compra.</p>"
        '<p class="seo-home-mesh-label">Vendere per provincia</p>'
        f'<p class="seo-home-mesh-links">{" · ".join(province_links)}</p>'
        '<p class="seo-home-mesh-label">Guide prezzi al mq (OMI)</p>'
        '<p class="seo-home-mesh-links">'
        '<a href="/guida-prezzi-mq-milano/">Milano</a> · '
        '<a href="/guida-prezzi-mq-bergamo/">Bergamo</a> · '
        '<a href="/guida-prezzi-mq-brescia/">Brescia</a></p>'
        '<p class="seo-home-mesh-label">Comprare casa</p>'
        f'<p class="seo-home-mesh-links"><a href="/comprare-casa/"><strong>Tutte le province</strong></a> · '
        f'{" · ".join(buy_links)}</p>'
        "</div></section>\n"
    )
    html = inject_before_footer(html, mesh)
    path.write_text(html, encoding="utf-8")
    print("  homepage mesh: index.html")
    return True


def patch_buyer_related() -> int:
    """Add related links on buyer province pages (IT) toward sell + OMI."""
    changed = 0
    for slug, name, _en in LOMBARD_PROVINCES:
        path = ROOT / buyer_province_url(slug, "it").strip("/") / "index.html"
        if not path.exists():
            continue
        html = path.read_text(encoding="utf-8")
        html = RELATED_RE.sub("\n", html)
        links = []
        if slug in OMI_GUIDES:
            links.append(
                f'<li><a href="{OMI_GUIDES[slug]}">Prezzi al mq OMI — {name}</a></li>'
            )
        links.append(
            f'<li><a href="{seller_url(slug, "it")}">Vendere casa a {name}</a></li>'
        )
        links.append('<li><a href="/vendere-casa/">Hub vendere casa in Lombardia</a></li>')
        links.append('<li><a href="/comprare-casa/">Tutte le province — comprare</a></li>')
        block = (
            '<nav class="seo-related" aria-label="Pagine correlate">\n'
            '  <div class="container">\n'
            '    <p class="seo-related-title">Approfondisci</p>\n'
            f"    <ul>\n    {''.join(links)}\n    </ul>\n"
            "  </div>\n"
            "</nav>\n"
        )
        html = inject_before_footer(html, block)
        path.write_text(html, encoding="utf-8")
        changed += 1
    print(f"  buyer related: {changed}")
    return changed


def patch_milano_guide() -> None:
    path = ROOT / "guida-prezzi-mq-milano" / "index.html"
    html = path.read_text(encoding="utf-8")

    new_title = "Valori OMI Milano 2026: prezzi al mq per zona (tabella aggiornata)"
    new_desc = (
        "Valori OMI Milano 2026 e prezzi al mq per zona (2° sem. 2025): "
        "da 1.850 a 16.000 €/mq. Tabella aggiornata e analisi micro-zona prima di vendere o comprare."
    )
    new_og = "Valori OMI Milano 2026: prezzi al mq per zona"

    html = re.sub(r"<title>[^<]*</title>", f"<title>{new_title}</title>", html, count=1)
    html = re.sub(
        r'<meta name="description" content="[^"]*"\s*/?>',
        f'<meta name="description" content="{new_desc}" />',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:title" content="[^"]*"\s*/?>',
        f'<meta property="og:title" content="{new_og}" />',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:description" content="[^"]*"\s*/?>',
        f'<meta property="og:description" content="{new_desc}" />',
        html,
        count=1,
    )
    # Fix broken schema absolute URLs (missing slash after domain)
    html = html.replace(
        "https://mauriziopiraino.itguida-prezzi-mq-milano/",
        "https://mauriziopiraino.it/guida-prezzi-mq-milano/",
    )
    html = html.replace(
        '"headline": "Prezzi al mq per zona a Milano: i valori OMI aggiornati"',
        f'"headline": "{new_title}"',
    )
    html = html.replace(
        '"dateModified": "2026-06-09"',
        '"dateModified": "2026-09-21"',
    )

    # Add Dataset schema once (supports rich results / clarity for OMI table queries)
    if '"@type": "Dataset"' not in html and '"@type":"Dataset"' not in html:
        dataset = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Valori OMI Milano 2026 — prezzi al mq per zona",
  "description": "Tabella dei valori OMI (Agenzia delle Entrate) per zone di Milano, 2° semestre 2025 / riferimento 2026.",
  "url": "https://mauriziopiraino.it/guida-prezzi-mq-milano/",
  "creator": {"@type": "Person", "name": "Maurizio Piraino"},
  "license": "https://www.agenziaentrate.gov.it/",
  "keywords": ["OMI Milano 2026", "valori OMI Milano", "prezzi al mq Milano"],
  "spatialCoverage": "Milano, Lombardia, Italia",
  "temporalCoverage": "2025-07/2025-12"
}
</script>
"""
        html = html.replace("</head>", dataset + "</head>", 1)

    path.write_text(html, encoding="utf-8")
    print("  guide title/meta/schema: guida-prezzi-mq-milano/")


def ensure_css() -> None:
    css_path = ROOT / "assets" / "site-base.css"
    snippet = """
/* SEO brief: related links + homepage mesh */
.seo-related{padding:36px 0;background:#fff;border-top:1px solid rgba(0,61,165,.08)}
.seo-related-title{font-size:12px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;color:#dc1c2e;margin:0 0 12px}
.seo-related ul{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.seo-related a{color:#003da5;font-weight:700;text-decoration:underline;text-underline-offset:2px}
.seo-home-mesh{padding:56px 0;background:#f4f7fc;border-top:1px solid rgba(0,61,165,.08)}
.seo-home-mesh h2{font-size:clamp(24px,3vw,34px);margin:0 0 12px;color:#003da5}
.seo-home-mesh > .container > p{margin:0 0 18px;color:#444;max-width:720px}
.seo-home-mesh-label{font-size:12px;font-weight:900;letter-spacing:.12em;text-transform:uppercase;color:#dc1c2e;margin:20px 0 8px !important}
.seo-home-mesh-links{line-height:1.9;margin:0 !important}
.seo-home-mesh-links a{color:#003da5;font-weight:700;text-decoration:underline;text-underline-offset:2px}
"""
    text = css_path.read_text(encoding="utf-8")
    if "seo-home-mesh" not in text:
        css_path.write_text(text + snippet, encoding="utf-8")
        print("  css: site-base.css")


def sync_audit_helper() -> None:
    """Keep apply_seo_audit.py seller_hreflang_urls aligned (no EN buy mismatch)."""
    path = ROOT / ".github" / "scripts" / "apply_seo_audit.py"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    old = '''def seller_hreflang_urls(slug: str) -> dict[str, str]:
    """IT/DE/FR seller pages; EN points to buyer province (no EN seller)."""
    return {
        "it": abs_url(seller_url(slug, "it")),
        "en": abs_url(buyer_province_url(slug, "en")),
        "de": abs_url(seller_url(slug, "de")),
        "fr": abs_url(seller_url(slug, "fr")),
    }'''
    new = '''def seller_hreflang_urls(slug: str) -> dict[str, str]:
    """Only same-intent seller pages (IT/DE/FR). No EN buy-home mismatch."""
    return {
        "it": abs_url(seller_url(slug, "it")),
        "de": abs_url(seller_url(slug, "de")),
        "fr": abs_url(seller_url(slug, "fr")),
    }'''
    if old in text:
        text = text.replace(old, new)
        # Also fix seller hub EN share
        text = text.replace(
            '''def seller_hub_hreflang_urls() -> dict[str, str]:
    return {
        "it": abs_url(seller_hub_url("it")),
        "de": abs_url(seller_hub_url("de")),
        "fr": abs_url(seller_hub_url("fr")),
        # EN has no seller hub — share IT
        "en": abs_url(seller_hub_url("it")),
    }''',
            '''def seller_hub_hreflang_urls() -> dict[str, str]:
    return {
        "it": abs_url(seller_hub_url("it")),
        "de": abs_url(seller_hub_url("de")),
        "fr": abs_url(seller_hub_url("fr")),
    }''',
        )
        path.write_text(text, encoding="utf-8")
        print("  synced apply_seo_audit.py")


def main() -> None:
    print("1) Seller hreflang (drop EN buy-home) + related links…")
    fix_seller_hreflang_and_related()
    print("2) Homepage + buyer related links…")
    patch_homepage_mesh()
    patch_buyer_related()
    print("3) Milano OMI guide title/meta/schema…")
    patch_milano_guide()
    print("4) CSS + sync audit helper…")
    ensure_css()
    sync_audit_helper()
    print("Done.")


if __name__ == "__main__":
    main()
