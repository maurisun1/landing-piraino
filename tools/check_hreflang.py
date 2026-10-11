#!/usr/bin/env python3
"""Verify hreflang reciprocity across all pages. Exit 1 on errors."""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://mauriziopiraino.it"

ALT_RE = re.compile(
    r'<link\s+rel=["\']alternate["\']\s+hreflang=["\']([^"\']+)["\']\s+href=["\']([^"\']+)["\']',
    re.I,
)
CANON_RE = re.compile(r'rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', re.I)
ROBOTS_RE = re.compile(r'name=["\']robots["\'][^>]*content=["\']([^"\']+)["\']', re.I)


def file_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return BASE + "/"
    return BASE + "/" + rel[: -len("index.html")].rstrip("/") + "/"


def url_to_file(url: str) -> Path | None:
    if not url.startswith(BASE):
        return None
    path = url[len(BASE) :].strip("/")
    if not path:
        return ROOT / "index.html"
    f = ROOT / path / "index.html"
    return f if f.is_file() else None


def main() -> int:
    errors = []
    # page -> {lang: href}
    pages = {}
    for p in ROOT.rglob("index.html"):
        t = p.read_text(encoding="utf-8", errors="ignore")
        alts = {m.group(1): m.group(2) for m in ALT_RE.finditer(t)}
        if not alts:
            continue
        pages[file_url(p)] = {"alts": alts, "path": p, "text": t}

    for url, data in pages.items():
        alts = data["alts"]
        # zh-Hans should not appear (task 5)
        if "zh-Hans" in alts:
            errors.append(f"{url}: still declares zh-Hans -> {alts['zh-Hans']}")
        for lang, href in alts.items():
            if lang == "x-default":
                continue
            target = url_to_file(href)
            if target is None:
                errors.append(f"{url}: hreflang {lang} points to missing URL {href}")
                continue
            # target must not be noindex
            tt = target.read_text(encoding="utf-8", errors="ignore")
            robots = ROBOTS_RE.search(tt)
            if robots and re.search(r"noindex", robots.group(1), re.I):
                errors.append(f"{url}: hreflang {lang} points to noindex page {href}")
                continue
            # reciprocity: target should list this page (or at least same group)
            t_alts = {m.group(1): m.group(2) for m in ALT_RE.finditer(tt)}
            if not t_alts:
                errors.append(f"{url}: target {href} has no hreflang back")
                continue
            # every alt on source (except maybe x-default) should appear on target with same href
            for lang2, href2 in alts.items():
                if lang2 not in t_alts:
                    errors.append(f"{url}: target {href} missing hreflang {lang2}")
                elif t_alts[lang2] != href2:
                    errors.append(
                        f"{url}: target {href} hreflang {lang2} mismatch {t_alts[lang2]} != {href2}"
                    )

    print(f"checked {len(pages)} pages with hreflang")
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors[:80]:
            print(" -", e)
        if len(errors) > 80:
            print(f" ... +{len(errors)-80} more")
        return 1
    print("OK: reciprocity clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
