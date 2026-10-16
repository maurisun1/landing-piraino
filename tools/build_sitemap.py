#!/usr/bin/env python3
"""Rebuild sitemap.xml with indexable pages + xhtml hreflang annotations."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://mauriziopiraino.it"
OUT = ROOT / "sitemap.xml"
MAP = ROOT / "seo" / "hreflang-map.json"

ROBOTS_RE = re.compile(r'name=["\']robots["\'][^>]*content=["\']([^"\']+)["\']', re.I)
CANON_RE = re.compile(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', re.I)
REFRESH_RE = re.compile(r'http-equiv=["\']refresh["\']', re.I)


def page_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return BASE + "/"
    return BASE + "/" + path.parent.relative_to(ROOT).as_posix() + "/"


def lastmod(path: Path) -> str:
    """Date of the last git commit that modified this file (YYYY-MM-DD).

    This is the commit date, not the build clock and not the checkout mtime.
    A dirty working tree does not move the date: commit the file first, then
    rebuild the sitemap. Fails if git has no history for the file (for example
    a shallow clone that does not contain the commit).
    """
    rel = path.relative_to(ROOT).as_posix()
    try:
        log = subprocess.check_output(
            ["git", "log", "-1", "--format=%cs", "--", rel],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        raise SystemExit(f"git log failed for {rel}: {exc}") from exc
    if not log:
        raise SystemExit(
            f"No git commit found for {rel}. Commit the file before rebuilding the sitemap."
        )
    return log


def priority_for(url: str) -> str:
    if url.rstrip("/") == BASE:
        return "1.0"
    if "/immobili-commerciali" in url or "/sviluppo-immobiliare" in url:
        return "0.85"
    if "/valutazione-casa" in url:
        return "0.85"
    if "/comprare-casa" in url or "/vendere-casa" in url:
        return "0.9"
    if url.count("/") <= 4:
        return "0.8"
    return "0.7"


def is_indexable(path: Path, text: str, url: str) -> bool:
    if "/zh/" in url or url.endswith("/zh"):
        return False
    if REFRESH_RE.search(text):
        return False
    robots = ROBOTS_RE.search(text)
    if robots and re.search(r"noindex", robots.group(1), re.I):
        return False
    canon = CANON_RE.search(text)
    if canon:
        cu = canon.group(1)
        if cu.rstrip("/") != url.rstrip("/"):
            return False
    return True


def load_hreflang_by_url() -> dict[str, dict[str, str]]:
    if not MAP.is_file():
        return {}
    data = json.loads(MAP.read_text(encoding="utf-8"))
    out: dict[str, dict[str, str]] = {}
    for g in data.get("groups", []):
        for lang, url in g.items():
            if lang == "x-default":
                continue
            out.setdefault(url, g)
        if "it" in g:
            out[g["it"]] = g
    return out


def main() -> None:
    hreflang_map = load_hreflang_by_url()
    entries = []
    for p in sorted(ROOT.rglob("index.html")):
        rel = str(p.relative_to(ROOT))
        if rel.startswith((".github/", "tools/", "seo/")):
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        url = page_url(p)
        if not is_indexable(p, text, url):
            continue
        entries.append((url, lastmod(p), priority_for(url), hreflang_map.get(url, {"it": url, "x-default": url})))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for url, lm, pr, group in entries:
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append(f"    <lastmod>{lm}</lastmod>")
        lines.append("    <changefreq>monthly</changefreq>")
        lines.append(f"    <priority>{pr}</priority>")
        # xhtml hreflang
        langs = [(k, v) for k, v in group.items()]
        # ensure self
        seen = set()
        for lang, href in langs:
            if href in seen:
                continue
            seen.add(href)
            lines.append(
                f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{href}" />'
            )
        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"sitemap urls={len(entries)} -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
