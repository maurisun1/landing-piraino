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

WA_ICON = (
    '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">'
    '<path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>'
    "</svg>"
)


def patch_wa_button(html: str) -> str:
    return re.sub(
        r'<a class="btn btn-outline" href="(https://wa\.me/[^"]+)">Scrivimi su WhatsApp</a>',
        rf'<a class="btn btn-wa seller-form-wa" href="\1">{WA_ICON} Scrivimi su WhatsApp</a>',
        html,
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
        f'          <a class="btn btn-wa seller-form-wa" href="{wa_url}">{WA_ICON} Scrivimi su WhatsApp</a>'
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
    html = patch_wa_button(html)

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
