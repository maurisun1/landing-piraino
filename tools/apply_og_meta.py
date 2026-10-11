#!/usr/bin/env python3
"""Ensure OG + Twitter meta on all HTML pages; shorten home description."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://mauriziopiraino.it"
DEFAULT_OG = "/og-default.jpg"

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.I | re.S)
DESC_RE = re.compile(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', re.I)
CANON_RE = re.compile(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', re.I)
OG_RE = re.compile(r'<meta\s+property=["\']og:[^"\']+["\'][^>]*>\s*', re.I)
TW_RE = re.compile(r'<meta\s+name=["\']twitter:[^"\']+["\'][^>]*>\s*', re.I)
LOCALE_ALT_RE = re.compile(r'<meta\s+property=["\']og:locale:alternate["\'][^>]*>\s*', re.I)

HOME_DESC = (
    "Maurizio Piraino, consulente acquirenti e investitori a Milano. "
    "Property finding, analisi e tutela fino al rogito. RE/MAX."
)


def page_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return BASE + "/"
    return BASE + "/" + str(path.parent.relative_to(ROOT)).replace("\\", "/") + "/"


def lang_locale(path: Path) -> tuple[str, list[str]]:
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith("en/"):
        return "en_US", ["it_IT", "de_DE", "fr_FR"]
    if rel.startswith("de/"):
        return "de_DE", ["it_IT", "en_US", "fr_FR"]
    if rel.startswith("fr/"):
        return "fr_FR", ["it_IT", "en_US", "de_DE"]
    if rel.startswith("zh/"):
        return "zh_CN", ["it_IT"]
    return "it_IT", ["en_US", "de_DE", "fr_FR"]


def ensure_default_image() -> None:
    dest = ROOT / "og-default.jpg"
    if dest.exists():
        return
    src = ROOT / "milano.jpg"
    if src.exists():
        shutil.copyfile(src, dest)
        print("CREATED og-default.jpg from milano.jpg (replace with branded 1200x630)")


def upsert_meta(text: str, path: Path) -> str:
    title_m = TITLE_RE.search(text)
    title = re.sub(r"\s+", " ", title_m.group(1)).strip() if title_m else "Maurizio Piraino"
    desc_m = DESC_RE.search(text)
    desc = desc_m.group(1) if desc_m else title
    if path.resolve() == (ROOT / "index.html").resolve():
        # shorten home description
        text = DESC_RE.sub(
            f'<meta name="description" content="{HOME_DESC}" />',
            text,
            count=1,
        )
        desc = HOME_DESC

    canon_m = CANON_RE.search(text)
    url = canon_m.group(1) if canon_m else page_url(path)

    # prefer existing og:image if any
    img_m = re.search(r'property=["\']og:image["\']\s+content=["\']([^"\']+)["\']', text, re.I)
    if not img_m:
        img_m = re.search(r'content=["\']([^"\']+)["\']\s+property=["\']og:image["\']', text, re.I)
    image = img_m.group(1) if img_m else BASE + DEFAULT_OG

    locale, alts = lang_locale(path)
    og_type = "website"
    if "guida-prezzi" in str(path) or "valutazione-casa" in str(path):
        og_type = "article"

    block = (
        f'<meta property="og:type" content="{og_type}" />\n'
        f'<meta property="og:title" content="{title}" />\n'
        f'<meta property="og:description" content="{desc}" />\n'
        f'<meta property="og:url" content="{url}" />\n'
        f'<meta property="og:image" content="{image}" />\n'
        f'<meta property="og:locale" content="{locale}" />\n'
    )
    for a in alts:
        block += f'<meta property="og:locale:alternate" content="{a}" />\n'
    block += '<meta name="twitter:card" content="summary_large_image" />\n'

    # strip old og/twitter/locale alternate
    text = OG_RE.sub("", text)
    text = TW_RE.sub("", text)
    text = LOCALE_ALT_RE.sub("", text)

    if re.search(r'rel=["\']canonical["\']', text, re.I):
        text = re.sub(
            r'(<link\s+rel=["\']canonical["\'][^>]*>\s*)',
            r"\1" + block,
            text,
            count=1,
            flags=re.I,
        )
    else:
        text = re.sub(r"(</title>\s*)", r"\1" + block, text, count=1, flags=re.I)
    return text


def main() -> None:
    ensure_default_image()
    n = 0
    for p in ROOT.rglob("index.html"):
        if str(p).find("/.git/") != -1:
            continue
        t = p.read_text(encoding="utf-8", errors="ignore")
        nt = upsert_meta(t, p)
        if nt != t:
            p.write_text(nt, encoding="utf-8")
            n += 1
    print(f"og/twitter updated pages={n}")
    print(f"home description length={len(HOME_DESC)}")


if __name__ == "__main__":
    main()
