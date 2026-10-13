#!/usr/bin/env python3
"""Final SEO verification across sitemap URLs + local HTML checks."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://mauriziopiraino.it"
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
SITEMAP = set(re.findall(r"<loc>([^<]+)</loc>", sm))


def url_to_path(url: str) -> Path:
    path = urlparse(url).path
    if path in ("", "/"):
        return ROOT / "index.html"
    return ROOT / path.strip("/") / "index.html"


def main() -> int:
    fails = []
    # Build noindex set
    noindex_urls = set()
    for p in ROOT.rglob("index.html"):
        if ".git" in p.parts:
            continue
        t = p.read_text(encoding="utf-8", errors="ignore")
        if re.search(r'name=["\']robots["\'][^>]*noindex', t, re.I) or re.search(
            r'http-equiv=["\']refresh["\']', t, re.I
        ):
            rel = p.relative_to(ROOT).as_posix()
            if rel == "index.html":
                noindex_urls.add(BASE + "/")
            else:
                noindex_urls.add(BASE + "/" + str(p.parent.relative_to(ROOT)) + "/")

    for url in sorted(SITEMAP):
        path = url_to_path(url)
        if not path.is_file():
            fails.append(f"MISSING FILE {url}")
            continue
        t = path.read_text(encoding="utf-8", errors="ignore")
        if re.search(r'http-equiv=["\']refresh["\']', t, re.I):
            fails.append(f"refresh in sitemap page {url}")
        robots = re.search(r'name=["\']robots["\'][^>]*content=["\']([^"\']+)', t)
        robots = robots.group(1) if robots else "missing"
        if re.search(r"noindex", robots, re.I):
            fails.append(f"noindex in sitemap {url}")
        canon = re.search(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', t)
        canon = canon.group(1) if canon else ""
        if canon.rstrip("/") != url.rstrip("/"):
            fails.append(f"canonical mismatch {url} -> {canon}")
        h1 = len(re.findall(r"<h1\b", t, re.I))
        if h1 != 1:
            fails.append(f"H1 count={h1} {url}")
        # hreflang reciprocity vs sitemap
        alts = re.findall(r'rel=["\']alternate["\'][^>]*hreflang=["\']([^"\']+)["\'][^>]*href=["\']([^"\']+)', t, re.I)
        alts += re.findall(r'hreflang=["\']([^"\']+)["\'][^>]*href=["\']([^"\']+)["\'][^>]*rel=["\']alternate["\']', t, re.I)
        for lang, href in alts:
            if lang.startswith("zh"):
                fails.append(f"zh hreflang on {url}")
            if href.rstrip("/") + "/" not in {u if u.endswith("/") else u + "/" for u in SITEMAP} and href.rstrip("/") != BASE:
                # allow exact sitemap match
                if href not in SITEMAP:
                    fails.append(f"hreflang to non-sitemap {url} -> {lang}:{href}")
            if href in noindex_urls:
                fails.append(f"hreflang to noindex {url} -> {href}")

        # internal bad links
        for href in re.findall(r'href=["\']([^"\']+)["\']', t):
            if href.startswith("/zh/") or href.startswith(f"{BASE}/zh/"):
                fails.append(f"internal zh link {url} -> {href}")
            if href in ("/index.html", f"{BASE}/index.html"):
                fails.append(f"index.html link {url}")
            if href.startswith("/") and not href.startswith("//"):
                # local path
                target = href.split("#")[0].split("?")[0]
                if target.endswith("/") or target.count("/") >= 1:
                    # map to url
                    full = BASE + (target if target.endswith("/") or target == "" else target + "/")
                    if target == "/":
                        full = BASE + "/"
                    elif not target.endswith("/") and "." not in Path(target).name:
                        full = BASE + target.rstrip("/") + "/"
                    if full in noindex_urls and "refresh" not in t.lower():
                        # linking to noindex from indexable is discouraged for zh; allow evaluation pages?
                        if "/zh/" in full:
                            fails.append(f"link to noindex {url} -> {full}")

        # VCT in footer/nav
        footer = re.search(r"<footer[\s\S]*?</footer>", t, re.I)
        nav = re.search(r'<nav[^>]*class="[^"]*nav-links[\s\S]*?</nav>', t, re.I)
        for block_name, block in (("footer", footer), ("nav", nav)):
            if not block:
                continue
            if "valorecasatua.it" in block.group(0).lower():
                fails.append(f"VCT link in {block_name} on {url}")

        # images
        for img in re.findall(r"<img\b[^>]*>", t, re.I):
            if not re.search(r"\balt=", img, re.I):
                fails.append(f"img missing alt on {url}: {img[:80]}")
            if not re.search(r"\bwidth=", img, re.I) or not re.search(r"\bheight=", img, re.I):
                fails.append(f"img missing w/h on {url}: {img[:80]}")

    print(f"sitemap_urls={len(SITEMAP)} fails={len(fails)}")
    for f in fails[:100]:
        print("FAIL:", f)
    if len(fails) > 100:
        print(f"... +{len(fails)-100} more")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
