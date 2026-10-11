#!/usr/bin/env python3
"""Build seo/hreflang-map.json from filesystem: only existing, indexable (non-noindex) pages."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://mauriziopiraino.it"

# Logical translation groups: IT path -> possible alt paths by lang
# Only entries whose files exist AND are indexable will be kept.
PROVINCES = [
    "milano", "milan", "bergamo", "brescia", "como", "varese", "lecco",
    "monza", "sondrio", "cremona", "lodi", "mantova", "pavia",
]

CANDIDATES = []

# Home
CANDIDATES.append({
    "it": "/",
    "en": "/en/",
    "de": "/de/",
    "fr": "/fr/",
    # zh excluded from hreflang (task 5)
})

# Buyer hubs
CANDIDATES.append({
    "it": "/comprare-casa/",
    "en": "/en/buy-home/",
    "de": "/de/haus-kaufen/",
    "fr": "/fr/acheter-maison/",
})

# Seller hub / milano seller
CANDIDATES.append({
    "it": "/vendere-casa/",
    "de": "/de/haus-verkaufen/",
    "fr": "/fr/vendre-maison/",
})
CANDIDATES.append({
    "it": "/vendere-casa-milano/",
    "de": "/de/haus-verkaufen-milan/",
    "fr": "/fr/vendre-maison-milan/",
})

# Buyer provinces
BUYER_MAP = {
    "milano": ("/comprare-casa-milano/", "/en/buy-home-milan/", "/de/haus-kaufen-milan/", "/fr/acheter-maison-milan/"),
    "bergamo": ("/comprare-casa-bergamo/", "/en/buy-home-bergamo/", "/de/haus-kaufen-bergamo/", "/fr/acheter-maison-bergamo/"),
    "brescia": ("/comprare-casa-brescia/", "/en/buy-home-brescia/", "/de/haus-kaufen-brescia/", "/fr/acheter-maison-brescia/"),
    "como": ("/comprare-casa-como/", "/en/buy-home-como/", "/de/haus-kaufen-como/", "/fr/acheter-maison-como/"),
    "varese": ("/comprare-casa-varese/", "/en/buy-home-varese/", "/de/haus-kaufen-varese/", "/fr/acheter-maison-varese/"),
    "lecco": ("/comprare-casa-lecco/", "/en/buy-home-lecco/", "/de/haus-kaufen-lecco/", "/fr/acheter-maison-lecco/"),
    "monza": ("/comprare-casa-monza/", "/en/buy-home-monza/", "/de/haus-kaufen-monza/", "/fr/acheter-maison-monza/"),
    "sondrio": ("/comprare-casa-sondrio/", "/en/buy-home-sondrio/", "/de/haus-kaufen-sondrio/", "/fr/acheter-maison-sondrio/"),
    "cremona": ("/comprare-casa-cremona/", "/en/buy-home-cremona/", "/de/haus-kaufen-cremona/", "/fr/acheter-maison-cremona/"),
    "lodi": ("/comprare-casa-lodi/", "/en/buy-home-lodi/", "/de/haus-kaufen-lodi/", "/fr/acheter-maison-lodi/"),
    "mantova": ("/comprare-casa-mantova/", "/en/buy-home-mantova/", "/de/haus-kaufen-mantova/", "/fr/acheter-maison-mantova/"),
    "pavia": ("/comprare-casa-pavia/", "/en/buy-home-pavia/", "/de/haus-kaufen-pavia/", "/fr/acheter-maison-pavia/"),
}
for city, (it, en, de, fr) in BUYER_MAP.items():
    CANDIDATES.append({"it": it, "en": en, "de": de, "fr": fr})

# Seller provinces IT + DE/FR mirrors (EN often absent)
SELLER_IT = {
    "bergamo": "/bergamo/",
    "brescia": "/brescia/",
    "como": "/como/",
    "varese": "/varese/",
    "lecco": "/lecco/",
    "monza": "/monza/",
    "sondrio": "/sondrio/",
    "cremona": "/cremona/",
    "lodi": "/lodi/",
    "mantova": "/mantova/",
    "pavia": "/pavia/",
}
for city, it in SELLER_IT.items():
    CANDIDATES.append({
        "it": it,
        "de": f"/de/{city}/",
        "fr": f"/fr/{city}/",
    })

# Standalone IT pages (self-only or known pairs)
STANDALONE = [
    "/immobili-commerciali/",
    "/sviluppo-immobiliare/",
    "/sviluppo-immobiliare/vendere-terreno-edificabile/",
    "/sviluppo-immobiliare/ricerca-aree-edificabili/",
    "/sviluppo-immobiliare/commercializzazione-cantieri/",
    "/vendere-casa/casa-invenduta/",
    "/guida-prezzi-mq-milano/",
    "/guida-prezzi-mq-brescia/",
    "/guida-prezzi-mq-bergamo/",
    "/valutazione-casa-brescia/",
    "/privacy/",
    "/comprare-casa/",  # already above with alts
]
for p in STANDALONE:
    if not any(c.get("it") == p for c in CANDIDATES):
        CANDIDATES.append({"it": p})


def path_to_file(url_path: str) -> Path:
    p = url_path.strip("/")
    if not p:
        return ROOT / "index.html"
    return ROOT / p / "index.html"


def is_indexable(path: Path) -> bool:
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8", errors="ignore")
    # stub di redirect (vedi tools/prune_defr.py): non è una pagina indicizzabile
    if re.search(r'http-equiv=["\']refresh["\']', text, re.I):
        return False
    robots = re.search(r'name=["\']robots["\']\s+content=["\']([^"\']+)["\']', text, re.I)
    if robots and re.search(r"\bnoindex\b", robots.group(1), re.I):
        return False
    # also meta robots content="noindex
    if re.search(r'content=["\'][^"\']*\bnoindex\b', text, re.I) and "robots" in text[:2500].lower():
        # careful: already handled; double-check head
        head = text[:4000]
        m = re.search(r'<meta[^>]+name=["\']robots["\'][^>]*>', head, re.I)
        if m and re.search(r"noindex", m.group(0), re.I):
            return False
    return True


def abs_url(path: str) -> str:
    if path == "/":
        return BASE + "/"
    return BASE + path.rstrip("/") + "/"


def main() -> None:
    groups = []
    seen_it = set()
    for cand in CANDIDATES:
        group = {}
        for lang, path in cand.items():
            if lang == "zh" or lang == "zh-Hans":
                continue  # task 5: exclude zh from hreflang
            f = path_to_file(path)
            if is_indexable(f):
                hreflang = "zh-Hans" if lang.startswith("zh") else lang
                group[hreflang] = abs_url(path)
        if "it" not in group:
            # allow groups that are only EN? skip if no IT and not intentional
            # keep if at least 1 indexable and has it key missing because file missing
            continue
        key = group["it"]
        if key in seen_it:
            # merge alts
            for g in groups:
                if g["it"] == key:
                    g.update(group)
                    break
            continue
        seen_it.add(key)
        group["x-default"] = group["it"]
        groups.append(group)

    # Also discover orphan EN/DE/FR indexable pages not in map: leave them self+x-default via apply script
    out = {
        "base": BASE,
        "note": "Only indexable existing URLs. zh-Hans excluded (noindex). x-default = IT.",
        "groups": groups,
    }
    dest = ROOT / "seo" / "hreflang-map.json"
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {dest.relative_to(ROOT)} groups={len(groups)}")
    multi = sum(1 for g in groups if len([k for k in g if k != "x-default"]) > 1)
    print(f"multi-lang groups={multi}")


if __name__ == "__main__":
    main()
