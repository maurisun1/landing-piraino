#!/usr/bin/env python3
"""Fix malformed CSS link tags and ensure remax-brand.css loads site-wide."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE = "20260710"
BRAND_LINK = f'  <link rel="stylesheet" href="/assets/remax-brand.css?v={CACHE}" />'

BROKEN = re.compile(
    r'href="(/assets/[^"?]+\?v=\d+)\s*/>',
    re.MULTILINE,
)


def fix_file(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    original = html

    html = BROKEN.sub(rf'href="\1" />', html)

    html = re.sub(
        r'href="(/assets/[^"]+\.css)\?v=\d+"',
        rf'href="\1?v={CACHE}"',
        html,
    )

    if "remax-brand.css" not in html:
        if "dual-path.css" in html:
            html = html.replace(
                f'/assets/dual-path.css?v={CACHE}" />',
                f'/assets/dual-path.css?v={CACHE}" />\n{BRAND_LINK}',
                1,
            )
        elif "site-base.css" in html:
            html = html.replace(
                f'/assets/site-base.css?v={CACHE}" />',
                f'/assets/site-base.css?v={CACHE}" />\n{BRAND_LINK}',
                1,
            )

    html = re.sub(
        r'\s*<script src="/assets/site-nav\.js[^"]*" defer></script>',
        "",
        html,
    )
    nav_js = f'  <script src="/assets/site-nav.js?v={CACHE}" defer></script>'
    if nav_js not in html and "</body>" in html:
        html = html.replace("</body>", f"{nav_js}\n</body>", 1)

    if html != original:
        path.write_text(html, encoding="utf-8")
        print(f"  fixed: {path.relative_to(ROOT)}")
        return True
    return False


def main() -> None:
    changed = 0
    for path in sorted(ROOT.rglob("*.html")):
        if fix_file(path):
            changed += 1
    print(f"Done. {changed} file(s) updated.")


if __name__ == "__main__":
    main()
