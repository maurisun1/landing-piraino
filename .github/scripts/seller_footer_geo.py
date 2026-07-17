#!/usr/bin/env python3
"""Build seller footer geo block with all 12 Lombard provinces."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

PROVINCES = [
    ("milano", "Milano"),
    ("monza", "Monza e Brianza"),
    ("bergamo", "Bergamo"),
    ("brescia", "Brescia"),
    ("como", "Como"),
    ("varese", "Varese"),
    ("lecco", "Lecco"),
    ("sondrio", "Sondrio"),
    ("cremona", "Cremona"),
    ("lodi", "Lodi"),
    ("mantova", "Mantova"),
    ("pavia", "Pavia"),
]

def seller_href(slug: str) -> str:
    from locales import seller_url

    return seller_url(slug, "it")

OMI_HREF = {
    "milano": "/guida-prezzi-mq-milano/",
    "bergamo": "/guida-prezzi-mq-bergamo/",
    "brescia": "/guida-prezzi-mq-brescia/",
}


def link(name: str, href: str, *, current: bool = False) -> str:
    if current:
        return f"<strong>{name}</strong>"
    return f'<a href="{href}">{name}</a>'


def join_links(parts: list[str]) -> str:
    return " &middot; ".join(parts)


def build_footer_geo(current: str) -> str:
    sedi = []
    for slug, name in PROVINCES:
        sedi.append(link(name, seller_href(slug), current=(slug == current)))

    omi = []
    for slug, name in PROVINCES:
        if slug in OMI_HREF:
            omi.append(link(name, OMI_HREF[slug]))
        else:
            omi.append(link(name, f"/comprare-casa-{slug}/"))

    buy = [
        '<a href="/comprare-casa/"><strong>Tutte le province lombarde (12)</strong></a>',
    ]
    buy += [link(name, f"/comprare-casa-{slug}/") for slug, name in PROVINCES]

    rows = [
        f'<p class="footer-geo-row"><span class="footer-geo-label">Sedi operative:</span> {join_links(sedi)}</p>',
        f'<p class="footer-geo-row"><span class="footer-geo-label">Guide prezzi OMI:</span> {join_links(omi)}</p>',
        f'<p class="footer-geo-row"><span class="footer-geo-label">Vuoi comprare?</span> {join_links(buy)}</p>',
        '<p class="footer-geo-row"><a href="/privacy/">Privacy</a></p>',
    ]
    return '    <div class="container footer-geo">\n      ' + "\n      ".join(rows) + "\n    </div>"


FOOTER_GEO_RE = re.compile(
    r'\s*<div class="container footer-geo">.*?</div>\s*(?=</footer>)',
    re.DOTALL,
)


def patch_seller(path: Path, current: str) -> None:
    html = path.read_text(encoding="utf-8")
    block = build_footer_geo(current)
    new_html, n = FOOTER_GEO_RE.subn(f"\n{block}\n", html, count=1)
    if n != 1:
        raise SystemExit(f"Footer geo not found in {path}")
    path.write_text(new_html, encoding="utf-8")
    print(f"Patched {path.relative_to(ROOT)}")


def main() -> None:
    from locales import seller_page_path

    for slug, _name in PROVINCES:
        rel = seller_page_path(slug, "it")
        path = ROOT / rel
        if path.exists():
            patch_seller(path, slug)


if __name__ == "__main__":
    main()
