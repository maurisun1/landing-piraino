#!/usr/bin/env python3
"""Scan DE/FR pages for Italian text residues."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from buyer_provinces import LOMBARD_PROVINCES

ROOT = Path(__file__).resolve().parents[2]
ITALIAN = re.compile(
    r"\b(che|della|vendere|comprare|immobile|rogito|trattativa|incarico|analisi|mercato|"
    r"acquirente|consulenza|domande|stima|prima di|quartiere|provincia)\b",
    re.I,
)


def visible_chunks(text: str) -> set[str]:
    body = re.sub(r"<script[^>]*>.*?</script>", "", text, flags=re.DOTALL | re.I)
    body = re.sub(r"<style[^>]*>.*?</style>", "", body, flags=re.DOTALL | re.I)
    out: set[str] = set()
    for m in re.finditer(r">([^<]{12,})<", body):
        c = html.unescape(m.group(1).strip())
        if c and "&#9733" not in c:
            out.add(re.sub(r"\s+", " ", c).strip())
    return out


def seller_path(slug: str, lang: str) -> Path:
    if lang == "it":
        return ROOT / ("index.html" if slug == "milano" else f"{slug}/index.html")
    return ROOT / lang / ("index.html" if slug == "milano" else f"{slug}/index.html")


def scan_seller(lang: str) -> list[tuple[str, int]]:
    rows: list[tuple[str, int]] = []
    for slug, _, _ in LOMBARD_PROVINCES:
        it = visible_chunks(seller_path(slug, "it").read_text(encoding="utf-8"))
        loc = visible_chunks(seller_path(slug, lang).read_text(encoding="utf-8"))
        hits = [s for s in it & loc if ITALIAN.search(s)]
        if hits:
            rows.append((slug, len(hits)))
    return sorted(rows, key=lambda x: -x[1])


def main() -> None:
    print("Seller pages — identical IT chunks with Italian markers:")
    for lang in ("de", "fr"):
        rows = scan_seller(lang)
        total = sum(n for _, n in rows)
        print(f"  {lang}: {total} total")
        for slug, n in rows[:6]:
            print(f"    {slug}: {n}")

    for hub in ("de/haus-kaufen/index.html", "fr/acheter-maison/index.html"):
        text = (ROOT / hub).read_text(encoding="utf-8")
        markers = ["Consulenza acquirenti", "Comprare casa", "Perché un consulente", "Scegli la provincia"]
        found = [m for m in markers if m in text]
        print(f"  {hub}: {found or 'OK'}")


if __name__ == "__main__":
    main()
