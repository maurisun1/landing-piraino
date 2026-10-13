#!/usr/bin/env python3
"""Add lazy-loading, dimensions and alt to <img> tags (skip LCP hero)."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SIZE_CACHE: dict[str, tuple[int, int]] = {}

KNOWN = {
    "/milano.jpg": (1200, 630),
    "/milano.webp": (1200, 800),
    "/brescia.jpg": (1600, 900),
    "/brescia.webp": (1600, 900),
    "/bergamo.jpg": (1600, 900),
    "/como.jpg": (1600, 900),
    "/foto.jpg": (800, 1000),
    "/foto.webp": (800, 1000),
    "/favicon.svg": (32, 32),
    "/og-default.jpg": (1200, 630),
}


def probe(src: str) -> tuple[int, int] | None:
    clean = src.split("?")[0]
    if clean in KNOWN:
        return KNOWN[clean]
    if clean in SIZE_CACHE:
        return SIZE_CACHE[clean]
    path = ROOT / clean.lstrip("/")
    if not path.is_file():
        return None
    try:
        out = subprocess.check_output(
            [
                "ffprobe",
                "-v",
                "error",
                "-select_streams",
                "v:0",
                "-show_entries",
                "stream=width,height",
                "-of",
                "csv=p=0:s=x",
                str(path),
            ],
            text=True,
        ).strip()
        w, h = out.split("x")
        SIZE_CACHE[clean] = (int(w), int(h))
        return SIZE_CACHE[clean]
    except Exception:
        return None


def fix_img(tag: str, *, is_lcp: bool) -> str:
    # skip if already processed carefully
    src_m = re.search(r'\bsrc=["\']([^"\']+)["\']', tag, re.I)
    if not src_m:
        return tag
    src = src_m.group(1)
    # decorative icons
    decorative = bool(re.search(r"icon_|favicon|logo-?img|wa\.svg|whatsapp", src, re.I))

    attrs = tag[4:-1]  # inside <img ...>
    # alt
    if not re.search(r"\balt=", tag, re.I):
        if decorative:
            tag = tag[:-1] + ' alt="" aria-hidden="true">'
        else:
            name = Path(src.split("?")[0]).stem.replace("-", " ").replace("_", " ")
            tag = tag[:-1] + f' alt="{name}">'

    # width/height
    if not re.search(r"\bwidth=", tag, re.I) or not re.search(r"\bheight=", tag, re.I):
        size = probe(src)
        if size:
            w, h = size
            if not re.search(r"\bwidth=", tag, re.I):
                tag = tag[:-1] + f' width="{w}">'
            if not re.search(r"\bheight=", tag, re.I):
                tag = tag[:-1] + f' height="{h}">'
        elif decorative:
            if not re.search(r"\bwidth=", tag, re.I):
                tag = tag[:-1] + ' width="32">'
            if not re.search(r"\bheight=", tag, re.I):
                tag = tag[:-1] + ' height="32">'

    if is_lcp or re.search(r'fetchpriority=["\']high["\']', tag, re.I):
        # ensure high priority, no lazy
        tag = re.sub(r'\sloading=["\'][^"\']*["\']', "", tag, flags=re.I)
        tag = re.sub(r'\sdecoding=["\'][^"\']*["\']', "", tag, flags=re.I)
        if not re.search(r"fetchpriority=", tag, re.I):
            tag = tag[:-1] + ' fetchpriority="high">'
        if not re.search(r"decoding=", tag, re.I):
            tag = tag[:-1] + ' decoding="async">'
    else:
        if not re.search(r"\bloading=", tag, re.I):
            tag = tag[:-1] + ' loading="lazy">'
        if not re.search(r"\bdecoding=", tag, re.I):
            tag = tag[:-1] + ' decoding="async">'
    return tag


def process(html: str) -> str:
    imgs = list(re.finditer(r"<img\b[^>]*>", html, flags=re.I))
    if not imgs:
        return html
    # first img in main/hero with preload sibling counts as LCP, else first img
    lcp_idx = 0
    for i, m in enumerate(imgs):
        if "fetchpriority" in m.group(0).lower():
            lcp_idx = i
            break
        # hero background often CSS; first content img
    out = []
    last = 0
    for i, m in enumerate(imgs):
        out.append(html[last : m.start()])
        out.append(fix_img(m.group(0), is_lcp=(i == lcp_idx)))
        last = m.end()
    out.append(html[last:])
    return "".join(out)


def main() -> None:
    n = 0
    for p in ROOT.rglob("*.html"):
        if ".git" in p.parts:
            continue
        # skip pure redirect stubs
        t = p.read_text(encoding="utf-8", errors="ignore")
        if "http-equiv" in t.lower() and "refresh" in t.lower() and t.count("<img") == 0:
            continue
        t2 = process(t)
        if t2 != t:
            p.write_text(t2, encoding="utf-8")
            n += 1
    print(f"img attrs updated pages={n}")


if __name__ == "__main__":
    main()
