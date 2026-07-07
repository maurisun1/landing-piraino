#!/usr/bin/env python3
"""Add RE/MAX Associati Real Estate affiliation to seller pages, hubs and guides."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from buyer_provinces import ABOUT_AGENCY_IT, FOOTER_AFFILIATION_EN, FOOTER_AFFILIATION_IT

ROOT = Path(__file__).resolve().parents[2]

FOOTER_BLOCK_IT = (
    f'        <div class="footer-affiliation">{FOOTER_AFFILIATION_IT}</div>\n'
)
ABOUT_BLOCK = f'          <p class="lead">{ABOUT_AGENCY_IT}</p>\n'

SELLER_PAGES = [
    "index.html",
    "bergamo/index.html",
    "brescia/index.html",
    "monza/index.html",
    "como/index.html",
    "varese/index.html",
    "lecco/index.html",
    "sondrio/index.html",
    "cremona/index.html",
    "lodi/index.html",
    "mantova/index.html",
    "pavia/index.html",
]

FOOTER_INNER_RE = re.compile(
    r'(<div class="container footer-inner">\s*<div>\s*<strong>.*?</strong>\s*)'
    r'(?!        <div class="footer-affiliation">)',
    re.DOTALL,
)

ABOUT_RE = re.compile(
    r'(<section class="about" id="metodo">.*?<h2>.*?</h2>\s*)'
    r'(?=<p class="lead">(?!Opero come consulente immobiliare con RE/MAX Associati))',
    re.DOTALL,
)


def patch_seller(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    original = html
    html = FOOTER_INNER_RE.sub(r"\1" + FOOTER_BLOCK_IT, html, count=1)
    if ABOUT_AGENCY_IT not in html:
        html = ABOUT_RE.sub(r"\1" + ABOUT_BLOCK, html, count=1)
    if html != original:
        path.write_text(html, encoding="utf-8")
        print(f"Patched {path.relative_to(ROOT)}")
        return True
    return False


def patch_hub(path: Path, *, lang: str) -> bool:
    html = path.read_text(encoding="utf-8")
    original = html
    affiliation = FOOTER_AFFILIATION_EN if lang == "en" else FOOTER_AFFILIATION_IT
    block = f'    <div class="footer-affiliation">{affiliation}</div>\n    '
    if "footer-affiliation" in html:
        html = re.sub(
            r'<div class="footer-affiliation">.*?</div>',
            f'<div class="footer-affiliation">{affiliation}</div>',
            html,
            count=1,
        )
    else:
        html = re.sub(
            r'(<footer class="footer">\s*<div class="container">\s*<strong>.*?</strong>\s*)',
            r"\1" + block,
            html,
            count=1,
            flags=re.DOTALL,
        )
    if html != original:
        path.write_text(html, encoding="utf-8")
        print(f"Patched {path.relative_to(ROOT)}")
        return True
    return False


def patch_guide(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    original = html
    line = f'<div class="footer-affiliation">{FOOTER_AFFILIATION_IT}</div>\n  '
    if "footer-affiliation" in html:
        html = re.sub(
            r'<div class="footer-affiliation">.*?</div>',
            f'<div class="footer-affiliation">{FOOTER_AFFILIATION_IT}</div>',
            html,
            count=1,
        )
    else:
        html = re.sub(
            r"(<strong>Maurizio Piraino</strong>\s*)",
            r"\1<br>\n  " + line,
            html,
            count=1,
        )
    if html != original:
        path.write_text(html, encoding="utf-8")
        print(f"Patched {path.relative_to(ROOT)}")
        return True
    return False


def patch_privacy() -> bool:
    path = ROOT / "privacy/index.html"
    html = path.read_text(encoding="utf-8")
    old = "Maurizio Piraino &middot; Agente Immobiliare affiliato RE/MAX<br>"
    new = (
        "Maurizio Piraino &middot; Agente Immobiliare affiliato RE/MAX<br>\n"
        f"  {FOOTER_AFFILIATION_IT}<br>"
    )
    if FOOTER_AFFILIATION_IT in html:
        return False
    if old not in html:
        return False
    path.write_text(html.replace(old, new, 1), encoding="utf-8")
    print(f"Patched {path.relative_to(ROOT)}")
    return True


def main() -> None:
    for rel in SELLER_PAGES:
        patch_seller(ROOT / rel)
    patch_hub(ROOT / "comprare-casa/index.html", lang="it")
    patch_hub(ROOT / "en/buy-home/index.html", lang="en")
    for rel in (
        "guida-prezzi-mq-milano/index.html",
        "guida-prezzi-mq-bergamo/index.html",
        "guida-prezzi-mq-brescia/index.html",
    ):
        patch_guide(ROOT / rel)
    patch_privacy()


if __name__ == "__main__":
    main()
