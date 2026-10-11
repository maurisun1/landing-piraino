#!/usr/bin/env python3
"""Apply hreflang link tags from seo/hreflang-map.json to all pages in each group."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = json.loads((ROOT / "seo" / "hreflang-map.json").read_text(encoding="utf-8"))
BASE = MAP["base"]

ALT_BLOCK_RE = re.compile(
    r'(?:<link\s+rel=["\']alternate["\']\s+hreflang=["\'][^"\']+["\']\s+href=["\'][^"\']+["\']\s*/?>\s*)+',
    re.I,
)
ALT_SINGLE_RE = re.compile(
    r'<link\s+rel=["\']alternate["\']\s+hreflang=["\'][^"\']+["\']\s+href=["\'][^"\']+["\']\s*/?>\s*',
    re.I,
)


def url_to_file(url: str) -> Path:
    path = url.replace(BASE, "").strip("/")
    if not path:
        return ROOT / "index.html"
    return ROOT / path / "index.html"


def build_links(group: dict) -> str:
    # stable order
    order = ["it", "en", "de", "fr", "x-default"]
    lines = []
    for lang in order:
        if lang in group:
            lines.append(f'<link rel="alternate" hreflang="{lang}" href="{group[lang]}" />')
    # any other langs
    for lang, href in group.items():
        if lang not in order:
            lines.append(f'<link rel="alternate" hreflang="{lang}" href="{href}" />')
    return "\n".join(lines) + "\n"


def apply_to_file(path: Path, links: str) -> bool:
    text = path.read_text(encoding="utf-8")
    # remove existing alternate hreflang
    new = ALT_SINGLE_RE.sub("", text)
    # insert after canonical if present, else after <title>
    if re.search(r'rel=["\']canonical["\']', new, re.I):
        new2, n = re.subn(
            r'(<link\s+rel=["\']canonical["\'][^>]*>\s*)',
            r"\1" + links,
            new,
            count=1,
            flags=re.I,
        )
        if n == 0:
            return False
        new = new2
    else:
        new2, n = re.subn(r"(</title>\s*)", r"\1" + links, new, count=1, flags=re.I)
        if n == 0:
            return False
        new = new2
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def strip_zh_hreflang_everywhere() -> int:
    """Remove zh-Hans alternate tags from all non-zh pages (and zh pages too for cleanliness)."""
    n = 0
    zh_re = re.compile(
        r'<link\s+rel=["\']alternate["\']\s+hreflang=["\']zh-Hans["\']\s+href=["\'][^"\']+["\']\s*/?>\s*',
        re.I,
    )
    for p in ROOT.rglob("index.html"):
        t = p.read_text(encoding="utf-8")
        nt, c = zh_re.subn("", t)
        if c:
            p.write_text(nt, encoding="utf-8")
            n += c
    return n


def main() -> None:
    removed = strip_zh_hreflang_everywhere()
    updated = 0
    for group in MAP["groups"]:
        links = build_links(group)
        for lang, url in group.items():
            if lang == "x-default":
                continue
            f = url_to_file(url)
            if not f.is_file():
                print("MISSING", url)
                continue
            if apply_to_file(f, links):
                updated += 1
    print(f"hreflang applied pages={updated} zh-Hans tags removed={removed}")


if __name__ == "__main__":
    main()
