#!/usr/bin/env python3
"""Generate DE/FR seller pages with professional full-phrase translations."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from buyer_provinces import LOMBARD_PROVINCES
from locales import seller_page_path
from seller_i18n import apply_seller_locale


def generate(lang: str) -> int:
    count = 0
    for slug, _name, _en in LOMBARD_PROVINCES:
        src_rel = seller_page_path(slug, "it")
        dst_rel = seller_page_path(slug, lang)
        src = ROOT / src_rel
        if not src.exists():
            print(f"  skip missing source: {src_rel}")
            continue
        html = apply_seller_locale(src.read_text(encoding="utf-8"), lang, slug)
        dst = ROOT / dst_rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(html, encoding="utf-8")
        print(f"  wrote {dst_rel}")
        count += 1
    return count


def main() -> None:
    print("Generating DE seller pages (professional translations)...")
    generate("de")
    print("Generating FR seller pages (professional translations)...")
    generate("fr")
    print("Done.")


if __name__ == "__main__":
    main()
