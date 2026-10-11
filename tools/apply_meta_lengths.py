#!/usr/bin/env python3
"""Apply title/description fixes from seo/meta-fixes.json; sync og: tags."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "seo" / "meta-fixes.json").read_text(encoding="utf-8"))


def set_title(html: str, title: str) -> str:
    html = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", html, count=1)
    if re.search(r'property=["\']og:title["\']', html):
        html = re.sub(
            r'(property=["\']og:title["\']\s+content=["\'])([^"\']*)(["\'])',
            rf"\g<1>{title}\g<3>",
            html,
            count=1,
        )
    return html


def set_desc(html: str, desc: str) -> str:
    html = re.sub(
        r'(name=["\']description["\']\s+content=["\'])([^"\']*)(["\'])',
        rf"\g<1>{desc}\g<3>",
        html,
        count=1,
    )
    if re.search(r'property=["\']og:description["\']', html):
        html = re.sub(
            r'(property=["\']og:description["\']\s+content=["\'])([^"\']*)(["\'])',
            rf"\g<1>{desc}\g<3>",
            html,
            count=1,
        )
    return html


def main() -> int:
    n = 0
    for path_str, fix in DATA["pages"].items():
        if path_str in ("", "/", ".", "index.html"):
            path = ROOT / "index.html"
        else:
            path = ROOT / path_str.lstrip("/") / "index.html"
        if not path.is_file():
            print("MISSING", path_str)
            continue
        html = path.read_text(encoding="utf-8")
        title = fix.get("title")
        desc = fix.get("description")
        if title:
            assert len(title) <= 60, (path_str, len(title), title)
            html = set_title(html, title)
        if desc:
            assert 120 <= len(desc) <= 155, (path_str, len(desc), desc)
            html = set_desc(html, desc)
        path.write_text(html, encoding="utf-8")
        n += 1
        print(f"fixed {path.relative_to(ROOT)} t={len(title) if title else '-'} d={len(desc) if desc else '-'}")
    print(f"updated {n} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
