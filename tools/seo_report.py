#!/usr/bin/env python3
"""Final SEO report for all index.html pages."""
from __future__ import annotations

import html as H
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://mauriziopiraino.it"


def page_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return BASE + "/"
    return BASE + "/" + path.parent.relative_to(ROOT).as_posix() + "/"


def main() -> int:
    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    sitemap = set(re.findall(r"<loc>([^<]+)</loc>", sm))

    rows = []
    fails = []
    for path in sorted(ROOT.rglob("index.html")):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(".github/"):
            continue
        t = path.read_text(encoding="utf-8", errors="ignore")
        url = page_url(path)
        robots_m = re.search(r'name=["\']robots["\'][^>]*content=["\']([^"\']+)', t)
        robots = robots_m.group(1) if robots_m else "missing"
        canon_m = re.search(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', t)
        canon = canon_m.group(1) if canon_m else ""
        self_can = canon.rstrip("/") == url.rstrip("/")
        title_m = re.search(r"<title>([^<]+)", t)
        title = title_m.group(1) if title_m else ""
        desc_m = re.search(r'name=["\']description["\'][^>]*content=["\']([^"\']*)', t)
        desc = H.unescape(desc_m.group(1)) if desc_m else ""
        h1n = len(re.findall(r"<h1\b", t, re.I))
        dado = "DATO DA INSERIRE" in t
        in_sm = url in sitemap or (url.rstrip("/") + "/") in sitemap
        indexable = "noindex" not in robots.lower()
        row = {
            "url": url,
            "robots": robots,
            "self_canonical": self_can,
            "in_sitemap": in_sm,
            "title_len": len(title),
            "desc_len": len(desc),
            "h1": h1n,
            "dato": dado,
            "indexable": indexable,
        }
        rows.append(row)
        if indexable and not in_sm:
            fails.append(f"index but not in sitemap: {url}")
        if indexable and not self_can:
            fails.append(f"index but not self-canonical: {url} -> {canon}")
        if (not indexable) and in_sm:
            fails.append(f"noindex in sitemap: {url}")
        if dado:
            fails.append(f"DATO DA INSERIRE: {url}")
        if len(title) > 60:
            fails.append(f"title>{60}: {url} ({len(title)}) {title}")
        if desc and (len(desc) < 120 or len(desc) > 155):
            fails.append(f"desc out of 120-155: {url} ({len(desc)})")
        if h1n != 1:
            # report-only: not a hard gate in task 5 rules
            pass

    print(f"pages={len(rows)} sitemap={len(sitemap)}")
    print(f"titles>60={sum(1 for r in rows if r['title_len']>60)}")
    print(f"desc_out={sum(1 for r in rows if r['desc_len'] and (r['desc_len']<120 or r['desc_len']>155))}")
    print(f"dato={sum(1 for r in rows if r['dato'])}")
    print(f"indexable={sum(1 for r in rows if r['indexable'])}")
    print(f"h1_ne_1={sum(1 for r in rows if r['h1']!=1)}")
    print(f"fails={len(fails)}")
    for f in fails[:80]:
        print("FAIL:", f)
    if len(fails) > 80:
        print(f"... +{len(fails)-80} more")
    # CSV-ish summary lines
    print("\n--- per-page ---")
    for r in rows:
        print(
            f"{r['url']}\tindex={r['indexable']}\tself={r['self_canonical']}\t"
            f"robots={r['robots']}\tsitemap={r['in_sitemap']}\t"
            f"title={r['title_len']}\tdesc={r['desc_len']}\th1={r['h1']}\tdato={r['dato']}"
        )
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
