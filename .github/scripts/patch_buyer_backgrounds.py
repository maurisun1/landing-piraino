#!/usr/bin/env python3
"""Align buyer page backgrounds with seller: city photo form section + cream steps."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

BUYER_PAGES = sorted(ROOT.glob("comprare-casa-*/index.html")) + sorted(
    ROOT.glob("en/buy-home-*/index.html")
)

COME_DARK = '<section id="come" style="background:var(--dark);color:#fff;padding:74px 0">'
COME_LIGHT = '<section id="come" class="steps" style="padding:74px 0">'

STEPS_H3_OLD = (
    ".steps-buy h3 { margin: 6px 0 8px; color: #fff; font-family: Inter, Arial, sans-serif; font-size: 20px; }"
)
STEPS_H3_NEW = (
    ".steps-buy h3 { margin: 6px 0 8px; color: var(--dark); font-family: Inter, Arial, sans-serif; font-size: 20px; }"
)
STEPS_P_OLD = ".steps-buy p { color: rgba(255,255,255,.72); margin: 0; }"
STEPS_P_NEW = ".steps-buy p { color: var(--muted); margin: 0; }"

STEPS_H2_WHITE = (
    "font-size:clamp(26px,3.5vw,38px);margin:10px 0 0;color:#fff"
)
STEPS_H2_DEFAULT = "font-size:clamp(26px,3.5vw,38px);margin:10px 0 0"

FORM_SECTION_RE = re.compile(
    r'<section id="contatto" class="buyer-form-section"(?:\s+style="--buyer-city-bg:[^"]*")?>'
)
HERO_IMG_RE = re.compile(
    r'<img class="buyer-hero-img" src="([^"]+)"'
)
WA_OUTLINE = re.compile(
    r'(<div class="buyer-form-aside reveal">.*?<a class=")btn btn-outline(" href="https://wa\.me/)',
    re.DOTALL,
)
WA_BTN = (
    r'\1btn btn-wa buyer-form-wa\2'
)


def patch_file(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    original = html

    if COME_DARK in html:
        html = html.replace(COME_DARK, COME_LIGHT)
    html = html.replace(STEPS_H3_OLD, STEPS_H3_NEW)
    html = html.replace(STEPS_P_OLD, STEPS_P_NEW)
    html = html.replace(STEPS_H2_WHITE, STEPS_H2_DEFAULT)

    hero = HERO_IMG_RE.search(html)
    if hero:
        img = hero.group(1)
        replacement = (
            f'<section id="contatto" class="buyer-form-section" '
            f'style="--buyer-city-bg: url(\'{img}\')">'
        )
        html = FORM_SECTION_RE.sub(replacement, html, count=1)

    wa_icon = (
        '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">'
        '<path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg> '
    )
    marker = '<ul class="buyer-form-benefits">'
    idx = html.find(marker)
    if idx != -1:
        wa_start = html.find('class="btn btn-outline"', idx)
        aside_end = html.find("</div>", html.find('<div class="buyer-form-aside', idx))
        if wa_start != -1 and wa_start < aside_end:
            before = html[:wa_start]
            after = html[wa_start:]
            after = after.replace('class="btn btn-outline"', 'class="btn btn-wa buyer-form-wa"', 1)
            if wa_icon not in after[:200]:
                after = after.replace(">Scrivimi su WhatsApp<", f">{wa_icon}Scrivimi su WhatsApp<", 1)
                after = after.replace(">Message me on WhatsApp<", f">{wa_icon}Message me on WhatsApp<", 1)
                after = after.replace(">Write me on WhatsApp<", f">{wa_icon}Write me on WhatsApp<", 1)
            html = before + after

    if html != original:
        path.write_text(html, encoding="utf-8")
        print(f"Patched {path.relative_to(ROOT)}")
        return True
    print(f"Skip {path.relative_to(ROOT)} (no changes)")
    return False


def main() -> None:
    changed = sum(patch_file(p) for p in BUYER_PAGES)
    print(f"Done: {changed} file(s) updated")


if __name__ == "__main__":
    main()
