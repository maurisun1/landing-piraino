#!/usr/bin/env python3
"""Inject full-width RE/MAX tricolor stripe after site header."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STRIPE = '  <div class="remax-stripe" aria-hidden="true"></div>\n'

CHROME_CLOSE_RE = re.compile(
    r"(  </header>\n)(?=</div>\s*\n(?:<main|  <main))",
    re.MULTILINE,
)


def patch_file(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    if "site-chrome" not in html or "remax-stripe" in html:
        return False
    new_html, n = CHROME_CLOSE_RE.subn(r"\1" + STRIPE, html, count=1)
    if n != 1:
        return False
    path.write_text(new_html, encoding="utf-8")
    print(f"Patched {path.relative_to(ROOT)}")
    return True


def main() -> None:
    count = 0
    for path in ROOT.rglob("*.html"):
        if patch_file(path):
            count += 1
    print(f"Done. {count} file(s) patched.")


if __name__ == "__main__":
    main()
