#!/usr/bin/env python3
"""Ensure a single full-width red stripe under site chrome."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STRIPE = '  <div class="remax-stripe" aria-hidden="true"></div>\n'

# Collapse duplicate stripe + stray closing divs after </header>
DUPES_RE = re.compile(
    r"(  </header>\n  <div class=\"remax-stripe\" aria-hidden=\"true\"></div>\n</div>\n)"
    r"(?:  <div class=\"remax-stripe\" aria-hidden=\"true\"></div>\n</div>\n)+",
    re.MULTILINE,
)

INSERT_RE = re.compile(
    r"(  </header>\n)(?=</div>\s*\n(?:<main|  <main))",
    re.MULTILINE,
)


def fix_stripes(html: str) -> str:
    if "site-chrome" not in html:
        return html
    if DUPES_RE.search(html):
        html = DUPES_RE.sub(r"\1", html, count=1)
    if "remax-stripe" not in html:
        html = INSERT_RE.sub(r"\1" + STRIPE, html, count=1)
    return html


def patch_file(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    fixed = fix_stripes(html)
    if fixed != html:
        path.write_text(fixed, encoding="utf-8")
        print(f"Fixed {path.relative_to(ROOT)}")
        return True
    return False


def main() -> None:
    count = 0
    for path in sorted(ROOT.rglob("*.html")):
        if patch_file(path):
            count += 1
    print(f"Done. {count} file(s) fixed.")


if __name__ == "__main__":
    main()
