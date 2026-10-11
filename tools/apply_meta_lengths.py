#!/usr/bin/env python3
"""Apply title/description fixes from seo/meta-fixes.json; sync og: tags."""
from __future__ import annotations

import html as H
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "seo" / "meta-fixes.json").read_text(encoding="utf-8"))


def _set_meta(html: str, attr: str, name: str, value: str) -> str:
    """Replace content of <meta {attr}="{name}" content="...">, honouring the actual
    delimiter quote (so apostrophes inside the value don't truncate the match)."""
    esc = H.escape(value, quote=True)
    pat = re.compile(
        r'(<meta\s+' + attr + r'=(["\'])' + re.escape(name) + r'\2\s+content=)(["\'])(.*?)\3',
        re.I | re.S,
    )
    return pat.sub(lambda m: f'{m.group(1)}"{esc}"', html, count=1)


def set_title(html: str, title: str) -> str:
    html = re.sub(r"<title>[^<]*</title>", lambda m: f"<title>{H.escape(title, quote=False)}</title>", html, count=1)
    html = _set_meta(html, "property", "og:title", title)
    html = _set_meta(html, "name", "twitter:title", title)
    return html


def set_desc(html: str, desc: str) -> str:
    # Replace the whole meta description tag to avoid leftover "/> />" fragments.
    html = re.sub(
        r'<meta\s+name=["\']description["\']\s+content=["\'][^"\']*["\']\s*/?\s*>',
        f'<meta name="description" content="{H.escape(desc, quote=True)}" />',
        html,
        count=1,
        flags=re.I,
    )
    html = _set_meta(html, "property", "og:description", desc)
    html = _set_meta(html, "name", "twitter:description", desc)
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
