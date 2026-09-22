#!/usr/bin/env python3
"""Apply SEO audit fixes: hreflang, H1, internal links, sitemap completeness.

Fixes from the Sept 2026 Search Console audit:
- Reciprocal hreflang clusters across IT/EN/DE/FR (and ZH where present)
- Restore <h1> on seller landings (hero was demoted to <h2>)
- Cross-link OMI price guides
- Strengthen buyer hub language alternates
- Regenerate sitemap including /de/ and /fr/ consultant homes
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from buyer_provinces import LOMBARD_PROVINCES  # noqa: E402
from locales import (  # noqa: E402
    buyer_hub_url,
    buyer_province_url,
    seller_hub_url,
    seller_page_path,
    seller_url,
)

BASE = "https://mauriziopiraino.it"
TODAY = date.today().isoformat()

ALT_RE = re.compile(
    r'\s*<link rel="alternate" hreflang="[^"]+" href="[^"]+"\s*/?>',
    re.IGNORECASE,
)
CANONICAL_RE = re.compile(
    r'(<link rel="canonical" href="[^"]+"\s*/?>)',
    re.IGNORECASE,
)
HERO_H2_RE = re.compile(
    r'(<div class="eyebrow">[^<]*</div>\s*)<h2>(.*?)</h2>',
    re.DOTALL,
)
GUIDE_RELATED = {
    "milano": ("https://valorecasatua.it/guide/prezzi-mq-milano/", "Milano"),
    "bergamo": ("https://valorecasatua.it/guide/prezzi-mq-bergamo/", "Bergamo"),
    "brescia": ("https://valorecasatua.it/guide/prezzi-mq-brescia/", "Brescia"),
}


def hreflang_block(urls: dict[str, str], *, x_default: str | None = None) -> str:
    """Build reciprocal alternate link tags. urls maps lang-code -> absolute URL."""
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
        # Fallback: insert before </head>
        return html.replace("</head>", f"{block}\n</head>", 1)
    return html[: m.end()] + "\n" + block + html[m.end() :]


def abs_url(path: str) -> str:
    if path.startswith("http"):
        return path
    return BASE + path


def fix_seller_h1(html: str) -> tuple[str, bool]:
    """Promote the seller hero title from h2 → h1 when no h1 exists."""
    if re.search(r"<h1[\s>]", html, re.IGNORECASE):
        return html, False
    if HERO_H2_RE.search(html):
        html2, n = HERO_H2_RE.subn(r"\1<h1>\2</h1>", html, count=1)
        return html2, n == 1
    # Broader fallback: first h2 in seller-form-aside
    html2, n = re.subn(
        r'(<div class="seller-form-aside[^"]*"[^>]*>[\s\S]*?)<h2>(.*?)</h2>',
        r"\1<h1>\2</h1>",
        html,
        count=1,
    )
    if n == 1:
        return html2, True
    html2, n = re.subn(r"<h2>(.*?)</h2>", r"<h1>\1</h1>", html, count=1)
    return html2, n == 1


def seller_hreflang_urls(slug: str) -> dict[str, str]:
    """Only same-intent seller pages (IT/DE/FR). No EN buy-home mismatch."""
    return {
        "it": abs_url(seller_url(slug, "it")),
        "de": abs_url(seller_url(slug, "de")),
        "fr": abs_url(seller_url(slug, "fr")),
    }


def home_hreflang_urls() -> dict[str, str]:
    urls = {
        "it": f"{BASE}/",
        "de": f"{BASE}/de/",
        "fr": f"{BASE}/fr/",
    }
    zh = ROOT / "zh" / "index.html"
    if zh.exists():
        urls["zh-Hans"] = f"{BASE}/zh/"
    return urls


def buyer_hub_hreflang_urls() -> dict[str, str]:
    urls = {lang: abs_url(buyer_hub_url(lang)) for lang in ("it", "en", "de", "fr")}
    zh = ROOT / "zh" / "mai-fang" / "index.html"
    if zh.exists():
        urls["zh-Hans"] = f"{BASE}/zh/mai-fang/"
    return urls


def seller_hub_hreflang_urls() -> dict[str, str]:
    return {
        "it": abs_url(seller_hub_url("it")),
        "de": abs_url(seller_hub_url("de")),
        "fr": abs_url(seller_hub_url("fr")),
    }


def buyer_province_hreflang_urls(slug: str) -> dict[str, str]:
    urls = {lang: abs_url(buyer_province_url(slug, lang)) for lang in ("it", "en", "de", "fr")}
    es = "milan" if slug == "milano" else slug
    zh = ROOT / "zh" / f"mai-fang-{es}" / "index.html"
    if zh.exists():
        urls["zh-Hans"] = f"{BASE}/zh/mai-fang-{es}/"
    return urls


def patch_file(path: Path, html: str) -> None:
    path.write_text(html, encoding="utf-8")


def guide_related_nav(current: str) -> str:
    links = []
    for key, (href, label) in GUIDE_RELATED.items():
        if key == current:
            links.append(f"<strong>{label}</strong>")
        else:
            links.append(f'<a href="{href}">Prezzi al mq {label}</a>')
    joined = " · ".join(links)
    return (
        f'<nav class="guide-related" aria-label="Altre guide prezzi OMI">'
        f"<p><span>Altre guide Lombardia:</span> {joined}</p></nav>\n"
    )


def patch_price_guides() -> int:
    changed = 0
    for key, (href, _label) in GUIDE_RELATED.items():
        path = ROOT / href.strip("/") / "index.html"
        if not path.exists():
            continue
        html = path.read_text(encoding="utf-8")
        # hreflang: IT-only guides — still declare self + x-default
        html = inject_hreflang(html, {"it": abs_url(href)}, x_default=abs_url(href))
        if 'class="guide-related"' not in html:
            block = guide_related_nav(key)
            # Insert before footer or main close
            if '<footer' in html:
                html = html.replace("<footer", block + "<footer", 1)
            elif "</main>" in html:
                html = html.replace("</main>", block + "</main>", 1)
            else:
                html = html.replace("</body>", block + "</body>", 1)
        # Soft CTA to buy/sell for the city
        seller = seller_url(key if key != "milano" else "milano", "it")
        buyer = buyer_province_url(key if key != "milano" else "milano", "it")
        city = {"milano": "Milano", "bergamo": "Bergamo", "brescia": "Brescia"}[key]
        cta = (
            f'<aside class="guide-cta-links" aria-label="Passaggi successivi">'
            f'<p>Hai un immobile a {city}? '
            f'<a href="{seller}">Richiedi analisi di vendita</a> · '
            f'<a href="{buyer}">Consulenza per chi compra</a></p></aside>\n'
        )
        if 'class="guide-cta-links"' not in html:
            if 'class="guide-related"' in html:
                html = html.replace(
                    '<nav class="guide-related"',
                    cta + '<nav class="guide-related"',
                    1,
                )
            elif "<footer" in html:
                html = html.replace("<footer", cta + "<footer", 1)
        patch_file(path, html)
        print(f"  guide: {path.relative_to(ROOT)}")
        changed += 1
    return changed


def patch_seller_pages() -> int:
    changed = 0
    for slug, _it, _en in LOMBARD_PROVINCES:
        for lang in ("it", "de", "fr"):
            rel = seller_page_path(slug, lang)
            path = ROOT / rel
            if not path.exists():
                print(f"  skip missing seller: {rel}")
                continue
            html = path.read_text(encoding="utf-8")
            html, h1_fixed = fix_seller_h1(html)
            html = inject_hreflang(html, seller_hreflang_urls(slug))
            patch_file(path, html)
            print(f"  seller{' +h1' if h1_fixed else ''}: {rel}")
            changed += 1
    # ZH milan seller if present
    zh = ROOT / "zh" / "chu-shou-milan" / "index.html"
    if zh.exists():
        html = zh.read_text(encoding="utf-8")
        html, h1_fixed = fix_seller_h1(html)
        urls = seller_hreflang_urls("milano")
        urls["zh-Hans"] = f"{BASE}/zh/chu-shou-milan/"
        html = inject_hreflang(html, urls)
        patch_file(zh, html)
        print(f"  seller{' +h1' if h1_fixed else ''}: zh/chu-shou-milan/")
        changed += 1
    return changed


def patch_homes_and_hubs() -> int:
    changed = 0
    # Consultant homes
    for rel, urls in (
        ("index.html", home_hreflang_urls()),
        ("de/index.html", home_hreflang_urls()),
        ("fr/index.html", home_hreflang_urls()),
    ):
        path = ROOT / rel
        if not path.exists():
            continue
        html = inject_hreflang(path.read_text(encoding="utf-8"), urls)
        patch_file(path, html)
        print(f"  home: {rel}")
        changed += 1
    zh_home = ROOT / "zh" / "index.html"
    if zh_home.exists():
        html = inject_hreflang(zh_home.read_text(encoding="utf-8"), home_hreflang_urls())
        patch_file(zh_home, html)
        print("  home: zh/index.html")
        changed += 1

    # Buyer hubs
    hub_urls = buyer_hub_hreflang_urls()
    for lang in ("it", "en", "de", "fr"):
        path = ROOT / buyer_hub_url(lang).strip("/") / "index.html"
        if not path.exists():
            continue
        html = inject_hreflang(path.read_text(encoding="utf-8"), hub_urls)
        patch_file(path, html)
        print(f"  buyer hub: {path.relative_to(ROOT)}")
        changed += 1
    zh_hub = ROOT / "zh" / "mai-fang" / "index.html"
    if zh_hub.exists():
        html = inject_hreflang(zh_hub.read_text(encoding="utf-8"), hub_urls)
        patch_file(zh_hub, html)
        print("  buyer hub: zh/mai-fang/")
        changed += 1

    # Seller hubs
    sell_urls = seller_hub_hreflang_urls()
    for lang in ("it", "de", "fr"):
        path = ROOT / seller_hub_url(lang).strip("/") / "index.html"
        if not path.exists():
            continue
        html = inject_hreflang(path.read_text(encoding="utf-8"), sell_urls)
        patch_file(path, html)
        print(f"  seller hub: {path.relative_to(ROOT)}")
        changed += 1
    return changed


def patch_buyer_provinces() -> int:
    """Ensure full IT/EN/DE/FR (+ZH) hreflang on all buyer province pages."""
    changed = 0
    for slug, _it, _en in LOMBARD_PROVINCES:
        urls = buyer_province_hreflang_urls(slug)
        for lang in ("it", "en", "de", "fr"):
            rel = buyer_province_url(slug, lang).strip("/") + "/index.html"
            path = ROOT / rel
            if not path.exists():
                continue
            html = inject_hreflang(path.read_text(encoding="utf-8"), urls)
            patch_file(path, html)
            changed += 1
        es = "milan" if slug == "milano" else slug
        zh = ROOT / "zh" / f"mai-fang-{es}" / "index.html"
        if zh.exists():
            html = inject_hreflang(zh.read_text(encoding="utf-8"), urls)
            patch_file(zh, html)
            changed += 1
    print(f"  buyer provinces patched: {changed}")
    return changed


def strengthen_seller_hub_internal_links() -> int:
    """Add a compact province mesh + OMI guides block on seller hubs if thin."""
    changed = 0
    cards = []
    for slug, it_name, _en in LOMBARD_PROVINCES:
        href = seller_url(slug, "it")
        cards.append(f'<a href="{href}">{it_name}</a>')
    links = " · ".join(cards)
    mesh = (
        '<section class="seo-internal-mesh" aria-label="Province lombarde">'
        '<div class="container">'
        "<h2>Vendere casa in Lombardia — scegli la provincia</h2>"
        f'<p class="seo-mesh-links">{links}</p>'
        '<p class="seo-mesh-guides">Guide prezzi OMI: '
        '<a href="https://valorecasatua.it/guide/prezzi-mq-milano/">Milano</a> · '
        '<a href="https://valorecasatua.it/guide/prezzi-mq-bergamo/">Bergamo</a> · '
        '<a href="https://valorecasatua.it/guide/prezzi-mq-brescia/">Brescia</a></p>'
        '<p class="seo-mesh-buy">Stai cercando casa? '
        '<a href="/comprare-casa/">Property Finding in Lombardia →</a></p>'
        "</div></section>\n"
    )
    path = ROOT / "vendere-casa" / "index.html"
    if path.exists():
        html = path.read_text(encoding="utf-8")
        if 'class="seo-internal-mesh"' not in html:
            if "<footer" in html:
                html = html.replace("<footer", mesh + "<footer", 1)
            else:
                html = html.replace("</main>", mesh + "</main>", 1)
            patch_file(path, html)
            print("  internal mesh: vendere-casa/")
            changed += 1

    buy_cards = []
    for slug, it_name, _en in LOMBARD_PROVINCES:
        href = buyer_province_url(slug, "it")
        buy_cards.append(f'<a href="{href}">{it_name}</a>')
    buy_links = " · ".join(buy_cards)
    buy_mesh = (
        '<section class="seo-internal-mesh" aria-label="Province lombarde">'
        '<div class="container">'
        "<h2>Comprare casa in Lombardia — scegli la provincia</h2>"
        f'<p class="seo-mesh-links">{buy_links}</p>'
        '<p class="seo-mesh-guides">Guide prezzi OMI: '
        '<a href="https://valorecasatua.it/guide/prezzi-mq-milano/">Milano</a> · '
        '<a href="https://valorecasatua.it/guide/prezzi-mq-bergamo/">Bergamo</a> · '
        '<a href="https://valorecasatua.it/guide/prezzi-mq-brescia/">Brescia</a></p>'
        '<p class="seo-mesh-buy">Devi vendere? '
        '<a href="/vendere-casa/">Analisi di vendita →</a></p>'
        "</div></section>\n"
    )
    path = ROOT / "comprare-casa" / "index.html"
    if path.exists():
        html = path.read_text(encoding="utf-8")
        if 'class="seo-internal-mesh"' not in html:
            if "<footer" in html:
                html = html.replace("<footer", buy_mesh + "<footer", 1)
            else:
                html = html.replace("</main>", buy_mesh + "</main>", 1)
            patch_file(path, html)
            print("  internal mesh: comprare-casa/")
            changed += 1
    return changed


def url_entry(loc: str, *, priority: str, changefreq: str = "monthly") -> str:
    return f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>"""


def rebuild_sitemap() -> int:
    entries: list[str] = []
    entries.append(url_entry(f"{BASE}/", priority="1.0"))
    entries.append(url_entry(f"{BASE}/de/", priority="0.95"))
    entries.append(url_entry(f"{BASE}/fr/", priority="0.95"))
    if (ROOT / "zh" / "index.html").exists():
        entries.append(url_entry(f"{BASE}/zh/", priority="0.85"))

    for lang in ("it", "de", "fr"):
        entries.append(
            url_entry(
                f"{BASE}{seller_url('milano', lang)}",
                priority="0.9" if lang == "it" else "0.85",
            )
        )

    for slug, _it, _en in LOMBARD_PROVINCES:
        if slug == "milano":
            continue
        entries.append(url_entry(f"{BASE}{seller_url(slug, 'it')}", priority="0.9"))
        for lang in ("de", "fr"):
            entries.append(url_entry(f"{BASE}{seller_url(slug, lang)}", priority="0.75"))

    for path, priority in (
        ("/guida-prezzi-mq-milano/", "0.85"),
        ("/guida-prezzi-mq-brescia/", "0.85"),
        ("/guida-prezzi-mq-bergamo/", "0.85"),
        ("/privacy/", "0.3"),
    ):
        entries.append(
            url_entry(
                f"{BASE}{path}",
                priority=priority,
                changefreq="yearly" if path == "/privacy/" else "monthly",
            )
        )

    for lang in ("it", "en", "de", "fr"):
        entries.append(
            url_entry(
                f"{BASE}{buyer_hub_url(lang)}",
                priority="0.95" if lang == "it" else "0.85",
            )
        )
    for lang in ("it", "de", "fr"):
        entries.append(
            url_entry(
                f"{BASE}{seller_hub_url(lang)}",
                priority="0.95" if lang == "it" else "0.85",
            )
        )

    for slug, _it, _en in LOMBARD_PROVINCES:
        for lang in ("it", "en", "de", "fr"):
            pri = (
                "0.9"
                if lang == "it" and slug in ("milano", "bergamo", "brescia")
                else "0.85"
                if lang == "it"
                else "0.75"
            )
            entries.append(url_entry(f"{BASE}{buyer_province_url(slug, lang)}", priority=pri))

    # ZH buyer pages if present
    for slug, _it, _en in LOMBARD_PROVINCES:
        es = "milan" if slug == "milano" else slug
        if (ROOT / "zh" / f"mai-fang-{es}" / "index.html").exists():
            entries.append(url_entry(f"{BASE}/zh/mai-fang-{es}/", priority="0.7"))
    if (ROOT / "zh" / "mai-fang" / "index.html").exists():
        entries.append(url_entry(f"{BASE}/zh/mai-fang/", priority="0.8"))
    if (ROOT / "zh" / "chu-shou" / "index.html").exists():
        entries.append(url_entry(f"{BASE}/zh/chu-shou/", priority="0.8"))
    if (ROOT / "zh" / "chu-shou-milan" / "index.html").exists():
        entries.append(url_entry(f"{BASE}/zh/chu-shou-milan/", priority="0.7"))

    # Deduplicate while preserving order
    seen: set[str] = set()
    unique: list[str] = []
    for e in entries:
        loc = re.search(r"<loc>([^<]+)</loc>", e)
        if not loc:
            continue
        if loc.group(1) in seen:
            continue
        seen.add(loc.group(1))
        unique.append(e)

    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(unique)
        + "\n</urlset>\n"
    )
    out = ROOT / "sitemap.xml"
    out.write_text(xml, encoding="utf-8")
    print(f"  sitemap.xml: {len(unique)} URLs")
    return len(unique)


def add_minimal_mesh_css() -> None:
    """Tiny styles for new SEO mesh / guide related blocks (if site-base exists)."""
    css_candidates = [
        ROOT / "assets" / "site-base.css",
        ROOT / "assets" / "seller-landing.css",
        ROOT / "assets" / "consultant-home.css",
    ]
    snippet = """
/* SEO audit: internal mesh + related guides */
.seo-internal-mesh{padding:48px 0;background:#f4f7fc;border-top:1px solid rgba(0,61,165,.08)}
.seo-internal-mesh h2{font-size:clamp(22px,3vw,30px);margin:0 0 16px;color:#003da5}
.seo-mesh-links,.seo-mesh-guides,.seo-mesh-buy{margin:0 0 12px;line-height:1.9;color:#333}
.seo-mesh-links a,.seo-mesh-guides a,.seo-mesh-buy a{color:#003da5;font-weight:700;text-decoration:underline;text-underline-offset:2px}
.guide-related,.guide-cta-links{max-width:1100px;margin:28px auto;padding:0 20px}
.guide-related p,.guide-cta-links p{margin:0;padding:16px 18px;background:#f4f7fc;border:1px solid rgba(0,61,165,.1);border-radius:12px;line-height:1.7}
.guide-related a,.guide-cta-links a{color:#003da5;font-weight:700}
"""
    for css in css_candidates:
        if css.exists() and "seo-internal-mesh" not in css.read_text(encoding="utf-8"):
            with css.open("a", encoding="utf-8") as f:
                f.write(snippet)
            print(f"  css: {css.relative_to(ROOT)}")
            return
    # Write a small dedicated file and note it — pages already load site-base
    target = ROOT / "assets" / "site-base.css"
    if target.exists():
        with target.open("a", encoding="utf-8") as f:
            f.write(snippet)
        print("  css appended to site-base.css")


def main() -> None:
    print("1) Seller H1 + hreflang…")
    n1 = patch_seller_pages()
    print("2) Homes + hubs hreflang…")
    n2 = patch_homes_and_hubs()
    print("3) Buyer provinces hreflang…")
    n3 = patch_buyer_provinces()
    print("4) Price guides cross-links…")
    n4 = patch_price_guides()
    print("5) Internal link mesh on hubs…")
    n5 = strengthen_seller_hub_internal_links()
    print("6) Sitemap…")
    n6 = rebuild_sitemap()
    print("7) CSS…")
    add_minimal_mesh_css()
    print(f"Done. pages≈{n1 + n2 + n3 + n4 + n5}, sitemap={n6}")


if __name__ == "__main__":
    main()
