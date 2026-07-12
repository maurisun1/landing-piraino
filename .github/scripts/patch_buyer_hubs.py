#!/usr/bin/env python3
"""Generate DE/FR buyer hub pages from Italian hub template."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from buyer_provinces import LOMBARD_PROVINCES
from locales import buyer_hub_url, buyer_province_url, hub_lang_urls

SRC = ROOT / "comprare-casa" / "index.html"

HUB_META = {
    "de": {
        "title": "Haus kaufen in der Lombardei: alle Provinzen | Piraino",
        "desc": "Käuferberatung in allen Provinzen der Lombardei. OMI-Analyse, technische Prüfung und gezielte RE/MAX-Suche.",
        "kicker": "Käuferberatung · Lombardei",
        "h1": "Haus kaufen in der Lombardei:<br>12 Provinzen, eine Methode.",
        "lead": "OMI-Analyse, technische Prüfung und gezielte Suche. Wählen Sie Ihre Provinz — ich helfe Ihnen, nicht zu viel zu zahlen.",
        "why_k": "Warum ein Berater",
        "why_h": "Kein Portal. Eine Methode für Käufer.",
        "why_p": "In jeder Provinz wende ich denselben Ansatz an: OMI-Zahlen, technische Prüfung und gezielte Suche.",
        "pick_h": "Provinz wählen",
        "pick_p": "Jede Seite ist auf den lokalen Markt zugeschnitten.",
        "cta": "Sagen Sie mir, was Sie suchen",
        "lang": "de",
        "path_prefix": "/de/haus-kaufen-",
        "hub_path": "/de/haus-kaufen/",
        "card_tag": "DE →",
    },
    "fr": {
        "title": "Acheter une maison en Lombardie : toutes les provinces | Piraino",
        "desc": "Conseil acheteurs dans toutes les provinces lombardes. Analyse OMI, vérification technique et recherche ciblée RE/MAX.",
        "kicker": "Conseil acheteurs · Lombardie",
        "h1": "Acheter en Lombardie :<br>12 provinces, une seule méthode.",
        "lead": "Analyse OMI, vérification technique et recherche ciblée. Choisissez votre province — je vous aide à ne pas payer trop cher.",
        "why_k": "Pourquoi un conseiller",
        "why_h": "Pas un portail. Une méthode pour les acheteurs.",
        "why_p": "Dans chaque province j'applique la même approche : chiffres OMI, vérification technique et recherche ciblée.",
        "pick_h": "Choisir la province",
        "pick_p": "Chaque page est adaptée au marché local.",
        "cta": "Dites-moi ce que vous cherchez",
        "lang": "fr",
        "path_prefix": "/fr/acheter-maison-",
        "hub_path": "/fr/acheter-maison/",
        "card_tag": "FR →",
    },
}


def province_cards(lang: str) -> str:
    m = HUB_META[lang]
    cards = []
    for slug, it_name, en_name in LOMBARD_PROVINCES:
        href = buyer_province_url(slug, lang)
        name = it_name if lang == "it" else en_name
        img = f"/{slug if slug != 'monza' else 'monza'}.jpg"
        if slug == "milano":
            img = "/milano.jpg"
        cards.append(
            f'<a class="card" href="{href}"><img src="{img}" alt="{name}" loading="lazy">'
            f'<div class="card-body"><h3>{name}</h3><p></p>'
            f'<div class="card-links"><span>{m["card_tag"]}</span></div></div></a>'
        )
    return "\n        ".join(cards)


def build_hub(lang: str) -> str:
    m = HUB_META[lang]
    html = SRC.read_text(encoding="utf-8")
    base = "https://mauriziopiraino.it"
    urls = hub_lang_urls()
    hreflang = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{urls[l].replace("/", base + "/") if urls[l].startswith("/") else base + urls[l]}" />'
        for l in urls
    )
    # Fix hreflang URLs
    hreflang_lines = []
    for l, u in urls.items():
        hreflang_lines.append(f'<link rel="alternate" hreflang="{l}" href="{base}{u}" />')
    hreflang = "\n".join(hreflang_lines)

    html = html.replace('lang="it"', f'lang="{m["lang"]}"')
    html = re.sub(r"<title>[^<]+</title>", f"<title>{m['title']}</title>", html)
    html = re.sub(r'<meta name="description" content="[^"]+" */>', f'<meta name="description" content="{m["desc"]}" />', html)
    html = re.sub(r'<link rel="canonical" href="[^"]+" */>', f'<link rel="canonical" href="{base}{m["hub_path"]}" />', html)
    html = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+" */>\s*', "", html)
    html = html.replace(
        '<link rel="alternate" hreflang="x-default"',
        hreflang + '\n<link rel="alternate" hreflang="x-default"',
    )
    html = re.sub(r'content="it_IT"', f'content="{m["lang"]}_{"DE" if lang == "de" else "FR"}"', html, count=1)
    html = html.replace("Comprare casa in Lombardia:", m["h1"].split("<br>")[0] + ":")
    html = html.replace(
        '<div class="kicker">Consulenza acquirenti · Lombardia</div>',
        f'<div class="kicker">{m["kicker"]}</div>',
    )
    html = re.sub(
        r"<h1>Comprare casa in Lombardia:.*?</h1>",
        f"<h1>{m['h1']}</h1>",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r"<p>Analisi OMI.*?</p>",
        f"<p>{m['lead']}</p>",
        html,
        count=1,
    )
    # Replace province card links
    for slug, it_name, en_name in LOMBARD_PROVINCES:
        it_href = buyer_province_url(slug, "it")
        loc_href = buyer_province_url(slug, lang)
        html = html.replace(f'href="{it_href}"', f'href="{loc_href}"', 1)
    html = html.replace("Dimmi cosa cerchi", m["cta"])
    html = html.replace("Salta al contenuto", "Zum Inhalt springen" if lang == "de" else "Aller au contenu")
    return html


def main() -> None:
    for lang in ("de", "fr"):
        rel = buyer_hub_url(lang).strip("/") + "/index.html"
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(build_hub(lang), encoding="utf-8")
        print(f"Wrote {rel}")


if __name__ == "__main__":
    main()
