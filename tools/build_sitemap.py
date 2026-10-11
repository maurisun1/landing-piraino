#!/usr/bin/env python3
"""Rebuild sitemap.xml with all indexable, self-canonical pages."""
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://mauriziopiraino.it"
OUT = ROOT / "sitemap.xml"

ROBOTS_RE = re.compile(r'name=["\']robots["\'][^>]*content=["\']([^"\']+)["\']', re.I)
CANON_RE = re.compile(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', re.I)


def page_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return BASE + "/"
    return BASE + "/" + str(path.parent.relative_to(ROOT)).replace("\\", "/") + "/"


def lastmod(path: Path) -> str:
    ts = path.stat().st_mtime
    return dt.datetime.fromtimestamp(ts, dt.timezone.utc).strftime("%Y-%m-%d")


def priority_for(url: str) -> str:
    if url.rstrip("/") == BASE:
        return "1.0"
    if "/immobili-commerciali" in url or "/sviluppo-immobiliare" in url:
        return "0.85"
    if "/guida-prezzi" in url or "/valutazione-casa" in url:
        return "0.85"
    if "/comprare-casa" in url or "/vendere-casa" in url:
        return "0.9"
    if url.count("/") <= 4:  # province hubs
        return "0.8"
    return "0.7"


def is_indexable(path: Path, text: str, url: str) -> bool:
    # skip zh entirely
    if "/zh/" in url or url.endswith("/zh"):
        return False
    robots = ROBOTS_RE.search(text)
    if robots and re.search(r"noindex", robots.group(1), re.I):
        return False
    canon = CANON_RE.search(text)
    if canon:
        c = canon.group(1).rstrip("/") + ("/" if not canon.group(1).endswith("/") and canon.group(1) != BASE else "")
        # normalize
        cu = canon.group(1)
        if cu.rstrip("/") != url.rstrip("/"):
            # external or different page canonical
            return False
    return True


def main() -> None:
    entries = []
    for p in sorted(ROOT.rglob("index.html")):
        # skip tooling / github
        rel = str(p.relative_to(ROOT))
        if rel.startswith(".github/") or rel.startswith("tools/") or rel.startswith("seo/"):
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        url = page_url(p)
        if not is_indexable(p, text, url):
            continue
        entries.append((url, lastmod(p), priority_for(url)))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url, lm, pr in entries:
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append(f"    <lastmod>{lm}</lastmod>")
        lines.append("    <changefreq>monthly</changefreq>")
        lines.append(f"    <priority>{pr}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"sitemap urls={len(entries)} -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
