#!/usr/bin/env python3
"""Restyle seller lead form like buyer-form-section with per-city background."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SELLER_PAGES = [
    "index.html",
    "bergamo/index.html",
    "brescia/index.html",
    "como/index.html",
    "cremona/index.html",
    "lecco/index.html",
    "lodi/index.html",
    "mantova/index.html",
    "monza/index.html",
    "pavia/index.html",
    "sondrio/index.html",
    "varese/index.html",
]

BENEFITS = """          <ul class="seller-form-benefits">
            <li>Risposta entro 24 ore, nessun obbligo di incarico</li>
            <li>Analisi OMI per zona e tipologia</li>
            <li>Posizionamento prezzo basato su dati reali</li>
            <li>Supporto in trattativa fino al rogito</li>
          </ul>"""

HERO_BLOCK_RE = re.compile(
    r"<section class=\"hero\" id=\"contatto\">\s*"
    r"<div class=\"hero-left\">\s*"
    r"<div class=\"hero-content reveal\">\s*"
    r"(.*?)\s*"
    r"</div>\s*</div>\s*"
    r"<aside class=\"hero-form-wrap\" id=\"form\">",
    re.DOTALL,
)

CITY_BG_RE = re.compile(
    r"\.hero-left::before\{[^}]*url\(([^)]+)\)[^}]*\}",
    re.DOTALL,
)

DEFAULT_WA = (
    "https://wa.me/393514581993?text=Ciao%20Maurizio%2C%20vorrei%20una%20consulenza%20immobiliare."
)


def normalize_bg_url(raw: str) -> str:
    url = raw.strip().strip("'\"")
    if url.startswith("../"):
        url = "/" + url[3:]
    if not url.startswith("/"):
        url = "/" + url
    return f"url('{url}')"


def extract_city_bg(html: str) -> str:
    match = CITY_BG_RE.search(html)
    if match:
        return normalize_bg_url(match.group(1))
    return "url('/milano.jpg')"


def transform_aside(inner: str) -> str:
    if "seller-form-benefits" in inner:
        return inner
    inner = re.sub(r"<div class=\"trust-row\">.*?</div>\s*", "", inner, flags=re.DOTALL)
    inner = re.sub(r"<div class=\"trust\">.*?</div>\s*", "", inner, flags=re.DOTALL)
    wa_match = re.search(r'class="btn btn-outline" href="([^"]+)"', inner)
    wa_url = wa_match.group(1) if wa_match else DEFAULT_WA
    inner = re.sub(r"<div class=\"hero-actions\">.*?</div>\s*", "", inner, flags=re.DOTALL)
    inner = re.sub(r'<a class="btn btn-outline"[^>]*>Scrivimi su WhatsApp</a>\s*', "", inner)
    inner = inner.replace("<h1>", "<h2>").replace("</h1>", "</h2>")
    inner = re.sub(r"\s+$", "", inner)
    return (
        f"{inner}\n{BENEFITS}\n"
        f'          <a class="btn btn-outline" href="{wa_url}">Scrivimi su WhatsApp</a>'
    )


def cleanup_aside(html: str) -> str:
    # Remove duplicate benefits / WA blocks from re-runs
    html = re.sub(
        r"(<ul class=\"seller-form-benefits\">.*?</ul>\s*"
        r'<a class="btn btn-outline"[^>]*>Scrivimi su WhatsApp</a>\s*)'
        r"(?:<ul class=\"seller-form-benefits\">.*?</ul>\s*"
        r'<a class="btn btn-outline"[^>]*>Scrivimi su WhatsApp</a>\s*)+',
        r"\1",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r"(<div class=\"seller-form-aside reveal\">\s*)"
        r"(?:<div class=\"trust\">.*?</div>\s*)+",
        r"\1",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r"</aside>\s*</div>\s*</section>",
        "      </aside>\n      </div>\n    </section>",
        html,
        count=1,
    )
    return html


def patch_page(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    original = html
    city_bg = extract_city_bg(html)

    def replacer(match: re.Match[str]) -> str:
        aside = transform_aside(match.group(1))
        return (
            f'<section class="hero seller-form-section" id="contatto" '
            f'style="--seller-city-bg: {city_bg}">\n'
            f'      <div class="container seller-form-layout">\n'
            f'        <div class="seller-form-aside reveal">\n'
            f"{aside}\n"
            f'        </div>\n'
            f'        <aside class="hero-form-wrap seller-form-panel" id="form">'
        )

    html = HERO_BLOCK_RE.sub(replacer, html, count=1)

    html = re.sub(
        r"(</aside>\s*)</section>(\s*<section class=\"dual-path\")",
        r"\1      </div>\n    </section>\2",
        html,
        count=1,
    )

    html = html.replace(
        '<form class="form-card reveal"',
        '<form class="form-card seller-form-card reveal"',
        1,
    )

    html = cleanup_aside(html)

    if html != original:
        path.write_text(html, encoding="utf-8")
        print(f"  patched: {path.relative_to(ROOT)}")
        return True
    print(f"  skip: {path.relative_to(ROOT)}")
    return False


def main() -> None:
    changed = 0
    for rel in SELLER_PAGES:
        path = ROOT / rel
        if not path.exists():
            print(f"  missing: {rel}")
            continue
        if patch_page(path):
            changed += 1
    print(f"Done. {changed} file(s) updated.")


if __name__ == "__main__":
    main()
