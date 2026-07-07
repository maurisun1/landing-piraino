#!/usr/bin/env python3
"""Generate seller landing pages for Lombard provinces missing a dedicated /{slug}/ page."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))

from buyer_provinces import LOMBARD_PROVINCES, NEW_PROVINCES

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / "bergamo/index.html"

EXISTING = {"milano", "bergamo", "brescia"}


def city_label(slug: str) -> str:
    for s, it, _en in LOMBARD_PROVINCES:
        if s == slug:
            return it
    return slug.title()


def tagline_for(slug: str) -> str:
    if slug in NEW_PROVINCES:
        return NEW_PROVINCES[slug]["footer_geo_it"]
    return {
        "milano": "Milano",
        "bergamo": "Bergamo · Città Alta · Provincia",
        "brescia": "Brescia · Franciacorta · Laghi",
    }.get(slug, city_label(slug))


def zones_for(slug: str) -> list[str]:
    if slug in NEW_PROVINCES:
        return NEW_PROVINCES[slug]["datalist_it"][:-1]
    return [f"{city_label(slug)} città", f"Altra zona provincia {city_label(slug)}"]


def build_page(slug: str) -> str:
    city = city_label(slug)
    html = TEMPLATE.read_text(encoding="utf-8")
    tagline = tagline_for(slug)

    html = html.replace("/guida-prezzi-mq-bergamo/", f"/comprare-casa-{slug}/")
    html = html.replace("guida-prezzi-mq-bergamo", f"comprare-casa-{slug}")

    replacements = [
        ("https://mauriziopiraino.it/bergamo/", f"https://mauriziopiraino.it/{slug}/"),
        ('href="/bergamo/"', f'href="/{slug}/"'),
        ('content="https://mauriziopiraino.it/bergamo/"', f'content="https://mauriziopiraino.it/{slug}/"'),
        ("/bergamo.jpg", f"/{slug}.jpg"),
        ("../bergamo.jpg", f"/{slug}.jpg"),
        ("/en/buy-home-bergamo/", f"/en/buy-home-{'milan' if slug == 'milano' else slug}/"),
        ("/comprare-casa-bergamo/", f"/comprare-casa-{slug}/"),
        ("Landing Bergamo RE/MAX Premium", f"Landing {city} RE/MAX Premium"),
        ("Agente Immobiliare Bergamo", f"Agente Immobiliare {city}"),
        ("RE/MAX Bergamo", f"RE/MAX {city}"),
        ("affiliato RE/MAX Bergamo", f"affiliato RE/MAX {city}"),
        ("vendere casa a Bergamo", f"vendere casa a {city}"),
        ("Vendere casa a Bergamo", f"Vendere casa a {city}"),
        ("casa a Bergamo", f"casa a {city}"),
        ("a Bergamo", f"a {city}"),
        ("A Bergamo", f"A {city}"),
        ("Bergamo e provincia", f"{city} e provincia"),
        ("Bergamo · Città Alta · Provincia", tagline),
        ("Città Alta · Valle Seriana · Provincia", tagline),
        ("Citt&agrave; Alta &middot; Valle Seriana &middot; Provincia", tagline.replace(" · ", " &middot; ")),
        ("Bergamo &middot; Citt&agrave; Alta &middot; Valle Seriana &middot; Provincia", tagline.replace(" · ", " &middot; ")),
        ("Bergamo &middot; Citt&agrave; Alta &middot; Provincia", tagline.replace(" · ", " &middot; ")),
        (
            "Opero su tutto il territorio bergamasco — Bergamo città, Città Alta, Valle Seriana, Valle Brembana, comuni di cintura e Bassa bergamasca. Ogni zona ha dinamiche proprie.",
            f"Opero su {city} e provincia, con attenzione alle micro-zone e alle dinamiche locali del mercato immobiliare.",
        ),
        (
            "A Bergamo la differenza tra Città Alta e Città Bassa, o tra i vari quartieri, può incidere significativamente sul valore.",
            f"A {city} ogni comune e quartiere ha dinamiche proprie che incidono in modo significativo sul valore reale.",
        ),
        (
            "Valutazione riservata su Bergamo, valli e provincia. Nessun obbligo di incarico.",
            f"Valutazione riservata su {city} e provincia. Nessun obbligo di incarico.",
        ),
        (
            "Comprare a Bergamo senza pagare troppo. Analisi OMI e verifica tecnica.",
            f"Comprare a {city} con metodo. Analisi OMI e verifica tecnica.",
        ),
        ("Comprare a Bergamo →", f"Comprare a {city} →"),
        ("strategia di vendita più adatta a Bergamo.", f"strategia di vendita più adatta a {city}."),
        ("Mercato Bergamo", f"Mercato {city}"),
        (
            "Conosco le specificit&agrave; di ogni zona del territorio bergamasco &mdash; dalla Citt&agrave; Alta al tessuto residenziale della Bassa, dalla Valle Seriana ai comuni di cintura. Ogni micro-mercato ha regole proprie.",
            f"Conosco le specificit&agrave; del mercato a {city} e in provincia. Ogni micro-zona ha regole proprie che incidono su prezzo e tempi di vendita.",
        ),
        ("Consulta i valori OMI ufficiali per zona a Bergamo →", f"Consulta i dati di mercato per {city} →"),
        ("Consulta i valori OMI per zona →", f"Consulta i dati di mercato per {city} →"),
        ("RE/MAX · Bergamo", f"RE/MAX · {city}"),
        ('"Bergamo"', f'"{city}"'),
        ("keywords\" content=\"agente immobiliare Bergamo", f"keywords\" content=\"agente immobiliare {city}"),
    ]
    for old, new in replacements:
        html = html.replace(old, new)

    wa_base = quote(f"Ciao Maurizio, vorrei ricevere un'analisi riservata del mio immobile a {city}.")
    html = re.sub(
        r"wa\.me/393514581993\?text=[^\"']+",
        f"wa.me/393514581993?text={wa_base}",
        html,
    )

    zone_options = "\n".join(f"              <option>{z}</option>" for z in zones_for(slug))
    html = re.sub(
        r"<datalist id=\"zone[^\"]*\">.*?</datalist>",
        f'<datalist id="zoneSeller">\n{zone_options}\n            </datalist>',
        html,
        count=1,
        flags=re.DOTALL,
    )

    return html


def write_page(slug: str) -> None:
    out = ROOT / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_page(slug), encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)}")


def main() -> None:
    for slug, _name in [(s, n) for s, n, _e in LOMBARD_PROVINCES if s not in EXISTING]:
        write_page(slug)


if __name__ == "__main__":
    main()
