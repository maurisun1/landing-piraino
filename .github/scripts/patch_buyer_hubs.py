#!/usr/bin/env python3
"""Generate DE/FR buyer hub pages from Italian hub template."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from buyer_provinces import LOMBARD_PROVINCES
from locales import buyer_hub_url, buyer_province_url, city_label, hub_lang_urls

SRC = ROOT / "comprare-casa" / "index.html"
BASE = "https://mauriziopiraino.it"

HUB_I18N = {
    "de": {
        "title": "Haus kaufen in der Lombardei: alle Provinzen | Piraino",
        "desc": "Käuferberatung in allen Provinzen der Lombardei. OMI-Analyse, technische Prüfung und gezielte RE/MAX-Suche.",
        "og_title": "Haus kaufen in der Lombardei: alle Provinzen | Piraino",
        "twitter_desc": "Käuferberatung in 12 Provinzen der Lombardei. OMI-Analyse und technische Prüfung RE/MAX.",
        "kicker": "Käuferberatung · Lombardei",
        "h1": "Haus kaufen in der Lombardei:<br>12 Provinzen, eine Methode.",
        "lead": "OMI-Analyse, technische Prüfung und gezielte Suche. Wählen Sie Ihre Provinz — ich helfe Ihnen, nicht zu viel zu zahlen.",
        "stats_provinces": "Provinzen der Lombardei",
        "stats_omi": "Offizielle OMI-Daten",
        "stats_reply": "Antwort auf Ihre Anfrage",
        "stats_network": "Internationales Netzwerk",
        "why_k": "Warum ein Berater",
        "why_h": "Kein Portal. Eine Methode für Käufer.",
        "why_p": "In jeder Provinz wende ich denselben Ansatz an: OMI-Zahlen, technische Prüfung und gezielte Suche — ohne Zeit mit falschen Inseraten zu verlieren.",
        "cards": [
            ("01", "Fairer Preis", "Sie wissen, ob die Immobilie wirklich so viel wert ist, bevor Sie ein Angebot machen."),
            ("02", "Technische Prüfung", "Konformität, Abweichungen und Dokumente werden vor dem Kauf geprüft."),
            ("03", "Gezielte Suche", "Sie sagen mir einmal, was Sie suchen: ich melde mich nur bei relevanten Objekten."),
            ("04", "RE/MAX-Netzwerk", "Zugang zum MLS-Netzwerk und Sichtbarkeit auf kommende Objekte."),
            ("05", "Verhandlung", "Begleitung in der Verhandlung bis zum Notartermin — mit Zahlen und Strategie."),
            ("06", "12 Provinzen", "Mailand, Bergamo, Brescia, Como und die ganze Lombardei mit demselben Standard."),
        ],
        "pick_h": "Provinz wählen",
        "pick_p": "Jede Seite ist auf den lokalen Markt zugeschnitten: Zonen, Pain Points und konkrete Empfehlungen.",
        "card_tag": "DE →",
        "en_link": 'Bevorzugen Sie Englisch? <a href="/en/buy-home/" style="color:var(--red);font-weight:800">Buy a home in Lombardy →</a>',
        "cta_nav": "Sagen Sie mir, was Sie suchen",
        "footer_s": "Zuerst die Analyse. Dann die richtige Wahl.",
        "footer_aff": "Maurizio Piraino — Immobilienberater bei RE/MAX Associati Real Estate · Mailand, Viale Gran Sasso 31",
        "footer_line": "RE/MAX-Immobilienberater · REA BS-639579 · USt-IdNr. 14597560961",
        "sell_link": "Haus verkaufen",
        "privacy": "Datenschutz",
        "topbar": "Käuferberatung <strong>RE/MAX</strong> · Lombardei · Antwort innerhalb von 24h",
        "wa_text": "Hallo Maurizio, ich suche eine Immobilie in der Lombardei und möchte eine Käuferberatung.",
        "schema_name": "Haus kaufen in der Lombardei",
        "schema_desc": "Hub mit 12 Provinzen der Lombardei für RE/MAX-Käuferberatung",
        "schema_list": "Provinzen der Lombardei — Käuferberatung",
        "skip": "Zum Inhalt springen",
        "lang": "de",
        "locale": "de_DE",
        "in_language": "de-DE",
        "nav_buy": "Kaufen",
        "nav_sell": "Verkaufen",
        "nav_about": "Über mich",
        "nav_path": "Weg",
        "nav_info": "Info",
        "nav_aria": "Sprache wählen",
        "nav_menu": "Hauptmenü",
        "nav_open": "Menü öffnen",
    },
    "fr": {
        "title": "Acheter une maison en Lombardie : toutes les provinces | Piraino",
        "desc": "Conseil acheteurs dans toutes les provinces lombardes. Analyse OMI, vérification technique et recherche ciblée RE/MAX.",
        "og_title": "Acheter une maison en Lombardie : toutes les provinces | Piraino",
        "twitter_desc": "Conseil acheteurs dans 12 provinces lombardes. Analyse OMI et vérification technique RE/MAX.",
        "kicker": "Conseil acheteurs · Lombardie",
        "h1": "Acheter en Lombardie :<br>12 provinces, une seule méthode.",
        "lead": "Analyse OMI, vérification technique et recherche ciblée. Choisissez votre province — je vous aide à ne pas payer trop cher.",
        "stats_provinces": "Provinces lombardes",
        "stats_omi": "Cotations OMI officielles",
        "stats_reply": "Réponse à votre demande",
        "stats_network": "Réseau international",
        "why_k": "Pourquoi un conseiller",
        "why_h": "Pas un portail. Une méthode pour les acheteurs.",
        "why_p": "Dans chaque province j'applique la même approche : chiffres OMI, vérification technique et recherche ciblée — sans vous faire perdre du temps sur de mauvaises annonces.",
        "cards": [
            ("01", "Prix juste", "Vous savez si le bien vaut vraiment le prix demandé, avant de faire une offre."),
            ("02", "Vérification technique", "Conformité, difformités et documents contrôlés avant l'achat."),
            ("03", "Recherche ciblée", "Vous me dites ce que vous cherchez une fois : je vous alerte seulement pour les biens pertinents."),
            ("04", "Réseau RE/MAX", "Accès au réseau MLS et visibilité sur les biens à venir sur le marché."),
            ("05", "Négociation", "Accompagnement en négociation jusqu'à l'acte notarié — avec chiffres et stratégie."),
            ("06", "12 provinces", "Milan, Bergame, Brescia, Côme et toute la Lombardie avec le même standard."),
        ],
        "pick_h": "Choisir la province",
        "pick_p": "Chaque page est adaptée au marché local : zones, points sensibles et conseils spécifiques.",
        "card_tag": "FR →",
        "en_link": 'Vous préférez l\'anglais ? <a href="/en/buy-home/" style="color:var(--red);font-weight:800">Buy a home in Lombardy →</a>',
        "cta_nav": "Dites-moi ce que vous cherchez",
        "footer_s": "D'abord l'analyse. Ensuite le bon choix.",
        "footer_aff": "Maurizio Piraino — Consultant immobilier chez RE/MAX Associati Real Estate · Milan, Viale Gran Sasso 31",
        "footer_line": "Agent immobilier RE/MAX · REA BS-639579 · P.IVA 14597560961",
        "sell_link": "Vendre un bien",
        "privacy": "Confidentialité",
        "topbar": "Conseil acheteurs <strong>RE/MAX</strong> · Lombardie · Réponse sous 24h",
        "wa_text": "Bonjour Maurizio, je cherche un bien en Lombardie et je souhaite un conseil acheteurs.",
        "schema_name": "Acheter une maison en Lombardie",
        "schema_desc": "Hub avec 12 provinces lombardes pour le conseil acheteurs RE/MAX",
        "schema_list": "Provinces lombardes — conseil acheteurs",
        "skip": "Aller au contenu",
        "lang": "fr",
        "locale": "fr_FR",
        "in_language": "fr-FR",
        "nav_buy": "Acheter",
        "nav_sell": "Vendre",
        "nav_about": "Qui je suis",
        "nav_path": "Parcours",
        "nav_info": "Info",
        "nav_aria": "Choisir la langue",
        "nav_menu": "Menu principal",
        "nav_open": "Ouvrir le menu",
    },
}

CARD_BLURBS = {
    "milano": {
        "de": "Schneller, wettbewerbsintensiver Markt. Mikrozonen-Analyse in Stadt und Provinz.",
        "fr": "Marché rapide et compétitif. Analyse micro-zone en ville et en province.",
    },
    "monza": {
        "de": "Brianza: hohe Nachfrage, schnelle Tempi, Preise zone für zone prüfen.",
        "fr": "Brianza : forte demande, délais rapides, prix à vérifier zone par zone.",
    },
    "bergamo": {
        "de": "Città Alta, Bassa, Täler und Provinz — unterschiedliche Mikromärkte.",
        "fr": "Città Alta, Bassa, vallées et province — micro-marchés distincts.",
    },
    "brescia": {
        "de": "Stadt, Franciacorta, Garda und Iseo — jede Zone hat eigene Regeln.",
        "fr": "Ville, Franciacorta, Garda et Iseo — chaque zone a ses règles.",
    },
    "como": {
        "de": "Comer See und Brianza comasca — Premium-Markt, gut analysieren.",
        "fr": "Lac de Côme et Brianza comasca — marché premium à bien analyser.",
    },
    "varese": {
        "de": "Voralpen, Seen und Altomilanese — Zahlen vor der Emotion.",
        "fr": "Préalpes, lacs et Altomilanese — les chiffres avant l'émotion.",
    },
    "lecco": {
        "de": "See, Brianza und Valsassina — verschiedene Märkte, dieselbe Methode.",
        "fr": "Lac, Brianza et Valsassina — marchés distincts, même méthode.",
    },
    "sondrio": {
        "de": "Valtellina: Wohnen, Tourismus und Zweitwohnsitz — Analyse pro Tal.",
        "fr": "Valtellina : résidentiel, tourisme et résidence secondaire — analyse par vallée.",
    },
    "cremona": {
        "de": "Kreisstadt, Crema und Ebene — ruhiger Markt, aber nicht unterschätzen.",
        "fr": "Chef-lieu, Crema et plaine — marché calme mais à ne pas sous-estimer.",
    },
    "lodi": {
        "de": "Lodigiana-Ebene — erschwingliche Preise, technische Prüfung entscheidend.",
        "fr": "Plaine lodigiana — prix accessibles, vérification technique décisive.",
    },
    "mantova": {
        "de": "UNESCO-Zentrum und Ebene — jede Gemeinde hat eigene Dynamiken.",
        "fr": "Centre UNESCO et plaine — chaque commune a ses dynamiques.",
    },
    "pavia": {
        "de": "Universitätsstadt, Oltrepò und Lomellina — drei verschiedene Märkte.",
        "fr": "Ville universitaire, Oltrepò et Lomellina — trois marchés différents.",
    },
}


def _schema_json(lang: str) -> str:
    m = HUB_I18N[lang]
    items = []
    for i, (slug, _it, _en) in enumerate(LOMBARD_PROVINCES, 1):
        items.append({
            "@type": "ListItem",
            "position": i,
            "url": f"{BASE}{buyer_province_url(slug, lang)}",
            "name": city_label(slug, lang),
        })
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "name": m["schema_name"],
                "url": f"{BASE}{buyer_hub_url(lang)}",
                "description": m["schema_desc"],
                "inLanguage": m["in_language"],
                "isPartOf": {"@type": "WebSite", "name": "Maurizio Piraino", "url": f"{BASE}/"},
            },
            {
                "@type": "ItemList",
                "name": m["schema_list"],
                "numberOfItems": 12,
                "itemListElement": items,
            },
        ],
    }
    return json.dumps(graph, ensure_ascii=False, indent=2)


def _province_cards(lang: str) -> str:
    m = HUB_I18N[lang]
    cards = []
    for slug, _it, _en in LOMBARD_PROVINCES:
        href = buyer_province_url(slug, lang)
        name = city_label(slug, lang)
        blurb = CARD_BLURBS.get(slug, {}).get(lang, "")
        img = f"/{slug}.jpg"
        cards.append(
            f'<a class="card" href="{href}"><img src="{img}" alt="{name}" loading="lazy">'
            f'<div class="card-body"><h3>{name}</h3><p>{blurb}</p>'
            f'<div class="card-links"><span>{m["card_tag"]}</span></div></div></a>'
        )
    return "\n        ".join(cards)


def _include_cards(lang: str) -> str:
    m = HUB_I18N[lang]
    return "\n        ".join(
        f'<article class="seller-include-card"><span class="seller-include-icon">{icon}</span>'
        f"<h3>{h}</h3><p>{p}</p></article>"
        for icon, h, p in m["cards"]
    )


def build_hub(lang: str) -> str:
    m = HUB_I18N[lang]
    html = SRC.read_text(encoding="utf-8")
    hub_path = buyer_hub_url(lang)
    canonical = f"{BASE}{hub_path}"
    urls = hub_lang_urls()
    hreflang = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{BASE}{u}" />' for l, u in urls.items()
    )

    html = html.replace('lang="it"', f'lang="{m["lang"]}"', 1)
    html = re.sub(r"<title>[^<]+</title>", f"<title>{m['title']}</title>", html, count=1)
    html = re.sub(r'<meta name="description" content="[^"]+" */>', f'<meta name="description" content="{m['desc']}" />', html, count=1)
    html = re.sub(r'<link rel="canonical" href="[^"]+" */>', f'<link rel="canonical" href="{canonical}" />', html, count=1)
    html = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+" */>\s*', "", html)
    html = html.replace(
        '<link rel="alternate" hreflang="x-default"',
        hreflang + '\n<link rel="alternate" hreflang="x-default"',
    )
    html = re.sub(r'<meta property="og:title" content="[^"]+" */>', f'<meta property="og:title" content="{m["og_title"]}" />', html, count=1)
    html = re.sub(r'<meta property="og:description" content="[^"]+" */>', f'<meta property="og:description" content="{m["desc"]}" />', html, count=1)
    html = re.sub(r'<meta property="og:url" content="[^"]+" */>', f'<meta property="og:url" content="{canonical}" />', html, count=1)
    html = re.sub(r'<meta property="og:locale" content="[^"]+" */>', f'<meta property="og:locale" content="{m["locale"]}" />', html, count=1)
    html = re.sub(r'<meta name="twitter:title" content="[^"]+" */>', f'<meta name="twitter:title" content="{m["og_title"]}" />', html, count=1)
    html = re.sub(r'<meta name="twitter:description" content="[^"]+" */>', f'<meta name="twitter:description" content="{m["twitter_desc"]}" />', html, count=1)

    html = re.sub(
        r'<script type="application/ld\+json">.*?</script>',
        f'<script type="application/ld+json">\n{_schema_json(lang)}\n</script>',
        html,
        count=1,
        flags=re.DOTALL,
    )

    from urllib.parse import quote
    wa = quote(m["wa_text"])
    html = re.sub(
        r'href="https://wa\.me/393514581993\?text=[^"]*"',
        f'href="https://wa.me/393514581993?text={wa}"',
        html,
    )

    html = html.replace("Salta al contenuto", m["skip"])
    html = re.sub(
        r'<div class="topbar-tagline">[^<]+<strong>RE/MAX</strong>[^<]+</div>',
        f'<div class="topbar-tagline">{m["topbar"]}</div>',
        html,
        count=1,
    )
    html = html.replace('aria-label="Seleziona lingua"', f'aria-label="{m["nav_aria"]}"')
    html = html.replace('aria-label="Menu principale"', f'aria-label="{m["nav_menu"]}"')
    html = html.replace('aria-label="Apri menu"', f'aria-label="{m["nav_open"]}"')
    html = html.replace('<span class="nav-group-label">Percorso</span>', f'<span class="nav-group-label">{m["nav_path"]}</span>')
    html = html.replace('<span class="nav-group-label">Info</span>', f'<span class="nav-group-label">{m["nav_info"]}</span>')
    html = html.replace('class="nav-link-primary">Comprare</a>', f'class="nav-link-primary">{m["nav_buy"]}</a>')
    html = html.replace('href="/">Vendere</a>', f'href="/{lang}/">{m["nav_sell"]}</a>' if lang == "de" else f'href="/fr/">{m["nav_sell"]}</a>')
    html = html.replace('href="/#metodo">Chi sono</a>', f'href="/{lang}/#metodo">{m["nav_about"]}</a>' if lang == "de" else f'href="/fr/#metodo">{m["nav_about"]}</a>')
    html = html.replace("Dimmi cosa cerchi", m["cta_nav"])

    html = re.sub(
        r'<div class="kicker">Consulenza acquirenti · Lombardia</div>',
        f'<div class="kicker">{m["kicker"]}</div>',
        html,
        count=1,
    )
    html = re.sub(
        r"<h1>Comprare casa in Lombardia:.*?</h1>",
        f"<h1>{m['h1']}</h1>",
        html,
        flags=re.DOTALL,
        count=1,
    )
    html = re.sub(
        r'<section class="hero hub-hero">.*?<p>Analisi OMI.*?</p>',
        lambda _m: (
            '<section class="hero hub-hero">\n    <div class="container">\n'
            f'      <div class="kicker">{m["kicker"]}</div>\n'
            f'      <h1>{m["h1"]}</h1>\n'
            f'      <p>{m["lead"]}</p>'
        ),
        html,
        count=1,
        flags=re.DOTALL,
    )

    html = html.replace("<span>Province lombarde</span>", f'<span>{m["stats_provinces"]}</span>')
    html = html.replace("<span>Quotazioni ufficiali</span>", f'<span>{m["stats_omi"]}</span>')
    html = html.replace("<span>Risposta alla richiesta</span>", f'<span>{m["stats_reply"]}</span>')
    html = html.replace("<span>Rete internazionale</span>", f'<span>{m["stats_network"]}</span>')

    html = re.sub(
        r'<div class="section-kicker"[^>]*>Perché un consulente</div>\s*<h2>Non un portale.*?</h2>\s*<p>In ogni provincia.*?</p>',
        (
            f'<div class="section-kicker" style="color:var(--red);font-weight:900;text-transform:uppercase;letter-spacing:.14em;font-size:12px">{m["why_k"]}</div>\n'
            f'        <h2>{m["why_h"]}</h2>\n'
            f'        <p>{m["why_p"]}</p>'
        ),
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'<div class="seller-includes-grid">.*?</div>\s*</div>\s*</section>\s*<section class="provinces">',
        f'<div class="seller-includes-grid">\n        {_include_cards(lang)}\n      </div>\n    </div>\n  </section>\n  <section class="provinces">',
        html,
        count=1,
        flags=re.DOTALL,
    )

    html = re.sub(r"<h2>Scegli la provincia</h2>", f"<h2>{m['pick_h']}</h2>", html, count=1)
    html = re.sub(
        r"<p>Ogni pagina è personalizzata per il mercato locale:.*?</p>",
        f"<p>{m['pick_p']}</p>",
        html,
        count=1,
    )
    html = re.sub(
        r'<div class="grid">.*?</div>\s*<p style="text-align:center',
        f'<div class="grid">\n        {_province_cards(lang)}\n      </div>\n      <p style="text-align:center',
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r"<p style=\"text-align:center;margin-top:32px;color:var\(--muted\)\">.*?</p>",
        f'<p style="text-align:center;margin-top:32px;color:var(--muted)">{m["en_link"]}</p>',
        html,
        count=1,
        flags=re.DOTALL,
    )

    html = html.replace("<strong>Prima l'analisi. Poi la scelta giusta.</strong>", f"<strong>{m['footer_s']}</strong>")
    html = re.sub(
        r'<div class="footer-affiliation">[^<]+</div>',
        f'<div class="footer-affiliation">{m["footer_aff"]}</div>',
        html,
        count=1,
    )
    html = re.sub(
        r"Agente Immobiliare affiliato RE/MAX · REA BS-639579 · P\.IVA 14597560961<br>",
        f'{m["footer_line"]}<br>',
        html,
        count=1,
    )
    html = html.replace('>Vendere casa</a>', f'>{m["sell_link"]}</a>')
    html = html.replace('>Privacy</a>', f'>{m["privacy"]}</a>')

    sell_hub = f"/{lang}/" if lang == "de" else "/fr/"
    html = html.replace('href="/"', f'href="{sell_hub}"', 1)

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
