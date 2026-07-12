#!/usr/bin/env python3
"""Regenerate sitemap.xml with IT / EN / DE / FR URLs."""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from buyer_provinces import LOMBARD_PROVINCES
from locales import buyer_hub_url, buyer_province_url, seller_url

ROOT = Path(__file__).resolve().parents[2]
BASE = "https://mauriziopiraino.it"
TODAY = date.today().isoformat()


def url_entry(loc: str, *, priority: str, changefreq: str = "monthly") -> str:
    return f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>"""


def main() -> None:
    entries: list[str] = []

    entries.append(url_entry(f"{BASE}/", priority="1.0"))
    for lang in ("de", "fr"):
        entries.append(url_entry(f"{BASE}{seller_url('milano', lang)}", priority="0.85"))

    for slug, _it, _en in LOMBARD_PROVINCES:
        if slug == "milano":
            continue
        entries.append(url_entry(f"{BASE}{seller_url(slug, 'it')}", priority="0.9"))
        for lang in ("de", "fr"):
            entries.append(url_entry(f"{BASE}{seller_url(slug, lang)}", priority="0.75"))

    for path, priority in (
        ("/guida-prezzi-mq-milano/", "0.8"),
        ("/guida-prezzi-mq-brescia/", "0.8"),
        ("/guida-prezzi-mq-bergamo/", "0.8"),
        ("/privacy/", "0.3"),
    ):
        entries.append(url_entry(f"{BASE}{path}", priority=priority, changefreq="yearly" if path == "/privacy/" else "monthly"))

    for lang in ("it", "en", "de", "fr"):
        entries.append(url_entry(f"{BASE}{buyer_hub_url(lang)}", priority="0.95" if lang == "it" else "0.85"))

    for slug, _it, _en in LOMBARD_PROVINCES:
        for lang in ("it", "en", "de", "fr"):
            pri = "0.9" if lang == "it" and slug in ("milano", "bergamo", "brescia") else "0.85" if lang == "it" else "0.75"
            entries.append(url_entry(f"{BASE}{buyer_province_url(slug, lang)}", priority=pri))

    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(entries)
        + "\n</urlset>\n"
    )
    out = ROOT / "sitemap.xml"
    out.write_text(xml, encoding="utf-8")
    print(f"Wrote {out} ({len(entries)} URLs)")


if __name__ == "__main__":
    main()
