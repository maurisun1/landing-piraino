#!/usr/bin/env python3
"""Generate seller province hubs (parallel to comprare-casa hubs)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from buyer_provinces import LOMBARD_PROVINCES
from locales import buyer_hub_url, city_label, seller_url

BASE = "https://mauriziopiraino.it"

BLURBS = {
    "milano": {
        "it": "Micro-zone, OMI e strategia di prezzo prima dell'annuncio.",
        "de": "Mikrozonen, OMI und Preisstrategie vor der Anzeige.",
        "fr": "Micro-zones, OMI et stratégie de prix avant l'annonce.",
    },
    "monza": {
        "it": "Brianza: domanda alta, tempi rapidi, posizionamento decisivo.",
        "de": "Brianza: hohe Nachfrage, schnelle Zeiten, Positionierung entscheidend.",
        "fr": "Brianza : forte demande, délais rapides, positionnement décisif.",
    },
    "bergamo": {
        "it": "Città Alta, Bassa, valli e provincia — mercati diversi.",
        "de": "Città Alta, Unterstadt, Täler und Provinz — unterschiedliche Märkte.",
        "fr": "Città Alta, ville basse, vallées et province — marchés distincts.",
    },
    "brescia": {
        "it": "Città, Franciacorta e laghi — ogni area ha regole proprie.",
        "de": "Stadt, Franciacorta und Seen — jede Zone hat eigene Regeln.",
        "fr": "Ville, Franciacorta et lacs — chaque zone a ses règles.",
    },
    "como": {
        "it": "Lago e Brianza comense — analisi micro-zona obbligatoria.",
        "de": "See und Brianza comense — Mikrozonenanalyse unverzichtbar.",
        "fr": "Lac et Brianza comasca — analyse micro-zone indispensable.",
    },
    "varese": {
        "it": "Prealpi, Altomilanese e laghi — numeri prima dell'emozione.",
        "de": "Voralpen, Altomilanese und Seen — Zahlen vor Emotion.",
        "fr": "Préalpes, Altomilanese et lacs — chiffres avant l'émotion.",
    },
    "lecco": {
        "it": "Lago, Brianza e Valsassina — stesso metodo, dinamiche diverse.",
        "de": "See, Brianza und Valsassina — gleiche Methode, andere Dynamiken.",
        "fr": "Lac, Brianza et Valsassina — même méthode, dynamiques différentes.",
    },
    "sondrio": {
        "it": "Valtellina: residenziale e seconda casa — analisi per valle.",
        "de": "Valtellina: Wohnen und Zweitwohnsitz — Analyse nach Tal.",
        "fr": "Valtellina : résidentiel et résidence secondaire — analyse par vallée.",
    },
    "cremona": {
        "it": "Capoluogo, Crema e pianura — mercato tranquillo da leggere bene.",
        "de": "Hauptstadt, Crema und Ebene — ruhiger Markt, klar lesen.",
        "fr": "Chef-lieu, Crema et plaine — marché calme à bien lire.",
    },
    "lodi": {
        "it": "Pianura lodigiana — prezzi e tempi da verificare sul reale.",
        "de": "Lodigiana-Ebene — Preise und Zeiten am realen Markt prüfen.",
        "fr": "Plaine lodigiana — prix et délais à vérifier sur le réel.",
    },
    "mantova": {
        "it": "Centro UNESCO e pianura — ogni comune ha dinamiche proprie.",
        "de": "UNESCO-Zentrum und Ebene — jede Gemeinde hat eigene Dynamiken.",
        "fr": "Centre UNESCO et plaine — chaque commune a ses dynamiques.",
    },
    "pavia": {
        "it": "Città, Oltrepò e Lomellina — tre mercati, un metodo.",
        "de": "Stadt, Oltrepò und Lomellina — drei Märkte, eine Methode.",
        "fr": "Ville, Oltrepò et Lomellina — trois marchés, une méthode.",
    },
}

COPY = {
    "it": {
        "title": "Vendere casa in Lombardia: tutte le province | Piraino",
        "desc": "Analisi immobiliare riservata e strategia di vendita in tutte le province lombarde. Dati OMI, micro-zona e metodo RE/MAX — senza obbligo di incarico.",
        "kicker": "Analisi vendita · Lombardia",
        "h1": "Vendere casa in Lombardia:<br>12 province, un metodo chiaro.",
        "lead": "Valutazione su dati reali, posizionamento prezzo e strategia. Scegli la provincia — prima l'analisi, poi la vendita.",
        "why_k": "Perché un'analisi prima",
        "why_h": "Non un annuncio. Una strategia di vendita.",
        "why_p": "In ogni provincia applico lo stesso approccio: dati OMI, micro-zona, criticità tecniche e piano di uscita sul mercato — senza improvvisazione.",
        "cards": [
            ("01", "Valore reale", "Confronto con compravendite e domanda reale della tua zona, non medie generiche."),
            ("02", "Dati OMI", "Riferimenti ufficiali integrati con il contesto della micro-zona."),
            ("03", "Criticità", "Documenti, stato e leve di trattativa prima della pubblicazione."),
            ("04", "Posizionamento", "Prezzo, timing e target acquirente per accelerare senza svalutare."),
            ("05", "Rete RE/MAX", "Visibilità MLS e collaborazione tra professionisti se decidi di procedere."),
            ("06", "12 province", "Milano e tutta la Lombardia con lo stesso standard consulenziale."),
        ],
        "pick_h": "Scegli la provincia",
        "pick_p": "Ogni pagina è personalizzata per il mercato locale: zone, dinamiche e consigli specifici.",
        "buy_link": 'Stai cercando casa? <a href="/comprare-casa/" style="color:var(--red);font-weight:800">Property Finding in Lombardia →</a>',
        "cta": "Richiedi analisi",
        "footer_s": "Prima l'analisi. Poi la vendita.",
        "sell_label": "Vendere",
        "buy_label": "Comprare",
        "topbar": "Analisi vendita <strong>RE/MAX</strong> · Lombardia · Risposta entro 24h",
        "wa": "Ciao%20Maurizio%2C%20vorrei%20un'analisi%20riservata%20per%20vendere%20casa%20in%20Lombardia.",
        "schema_name": "Vendere casa in Lombardia",
        "schema_desc": "Hub con 12 province lombarde per analisi e strategia di vendita RE/MAX",
        "schema_list": "Province lombarde — vendere casa",
        "path": "vendere-casa/index.html",
        "url": "/vendere-casa/",
        "lang": "it",
        "locale": "it_IT",
        "in_lang": "it-IT",
        "buy_hub": "/comprare-casa/",
        "home": "/",
        "hreflang": {
            "it": "/vendere-casa/",
            "de": "/de/haus-verkaufen/",
            "fr": "/fr/vendre-maison/",
        },
    },
    "de": {
        "title": "Haus verkaufen in der Lombardei: alle Provinzen | Piraino",
        "desc": "Vertrauliche Immobilienanalyse und Verkaufsstrategie in allen Provinzen der Lombardei. OMI-Daten, Mikrozone und RE/MAX-Methode — ohne Verpflichtung zum Mandat.",
        "kicker": "Verkaufsanalyse · Lombardei",
        "h1": "Haus verkaufen in der Lombardei:<br>12 Provinzen, eine klare Methode.",
        "lead": "Bewertung auf realen Daten, Preispositionierung und Strategie. Wählen Sie die Provinz — zuerst die Analyse, dann der Verkauf.",
        "why_k": "Warum erst analysieren",
        "why_h": "Keine Anzeige. Eine Verkaufsstrategie.",
        "why_p": "In jeder Provinz derselbe Ansatz: OMI-Daten, Mikrozone, technische Risiken und Marktstart — ohne Improvisation.",
        "cards": [
            ("01", "Realer Wert", "Vergleich mit Transaktionen und realer Nachfrage — keine generischen Mittelwerte."),
            ("02", "OMI-Daten", "Offizielle Referenzen, integriert mit dem Mikrozonen-Kontext."),
            ("03", "Risiken", "Dokumente, Zustand und Verhandlungshebel vor der Veröffentlichung."),
            ("04", "Positionierung", "Preis, Timing und Käuferprofil — schneller verkaufen ohne Entwertung."),
            ("05", "RE/MAX-Netz", "MLS-Sichtbarkeit und Zusammenarbeit, wenn Sie fortfahren."),
            ("06", "12 Provinzen", "Mailand und die ganze Lombardei mit demselben Beratungsstandard."),
        ],
        "pick_h": "Provinz wählen",
        "pick_p": "Jede Seite ist auf den lokalen Markt zugeschnitten.",
        "buy_link": 'Suchen Sie eine Immobilie? <a href="/de/haus-kaufen/" style="color:var(--red);font-weight:800">Property Finding in der Lombardei →</a>',
        "cta": "Analyse anfordern",
        "footer_s": "Zuerst die Analyse. Dann der Verkauf.",
        "sell_label": "Verkaufen",
        "buy_label": "Kaufen",
        "topbar": "Verkaufsanalyse <strong>RE/MAX</strong> · Lombardei · Antwort innerhalb von 24h",
        "wa": "Hallo%20Maurizio%2C%20ich%20m%C3%B6chte%20eine%20vertrauliche%20Analyse%20zum%20Verkauf%20in%20der%20Lombardei.",
        "schema_name": "Haus verkaufen in der Lombardei",
        "schema_desc": "Hub mit 12 Provinzen der Lombardei für Verkaufsanalyse RE/MAX",
        "schema_list": "Provinzen der Lombardei — Haus verkaufen",
        "path": "de/haus-verkaufen/index.html",
        "url": "/de/haus-verkaufen/",
        "lang": "de",
        "locale": "de_DE",
        "in_lang": "de-DE",
        "buy_hub": "/de/haus-kaufen/",
        "home": "/de/",
        "hreflang": {
            "it": "/vendere-casa/",
            "de": "/de/haus-verkaufen/",
            "fr": "/fr/vendre-maison/",
        },
    },
    "fr": {
        "title": "Vendre une maison en Lombardie : toutes les provinces | Piraino",
        "desc": "Analyse immobilière confidentielle et stratégie de vente dans toutes les provinces lombardes. Données OMI, micro-zone et méthode RE/MAX — sans obligation de mandat.",
        "kicker": "Analyse vente · Lombardie",
        "h1": "Vendre en Lombardie :<br>12 provinces, une méthode claire.",
        "lead": "Estimation sur données réelles, positionnement prix et stratégie. Choisissez la province — d'abord l'analyse, ensuite la vente.",
        "why_k": "Pourquoi analyser d'abord",
        "why_h": "Pas une annonce. Une stratégie de vente.",
        "why_p": "Dans chaque province la même approche : données OMI, micro-zone, risques techniques et sortie sur le marché — sans improvisation.",
        "cards": [
            ("01", "Valeur réelle", "Comparaison avec transactions et demande réelle — pas de moyennes génériques."),
            ("02", "Données OMI", "Références officielles intégrées au contexte de micro-zone."),
            ("03", "Points sensibles", "Documents, état et leviers de négociation avant publication."),
            ("04", "Positionnement", "Prix, timing et profil acheteur — vendre plus vite sans dévaloriser."),
            ("05", "Réseau RE/MAX", "Visibilité MLS et collaboration si vous décidez de poursuivre."),
            ("06", "12 provinces", "Milan et toute la Lombardie avec le même standard de conseil."),
        ],
        "pick_h": "Choisir la province",
        "pick_p": "Chaque page est adaptée au marché local.",
        "buy_link": 'Vous cherchez un bien ? <a href="/fr/acheter-maison/" style="color:var(--red);font-weight:800">Property Finding en Lombardie →</a>',
        "cta": "Demander une analyse",
        "footer_s": "D'abord l'analyse. Ensuite la vente.",
        "sell_label": "Vendre",
        "buy_label": "Acheter",
        "topbar": "Analyse vente <strong>RE/MAX</strong> · Lombardie · Réponse sous 24h",
        "wa": "Bonjour%20Maurizio%2C%20je%20souhaite%20une%20analyse%20confidentielle%20pour%20vendre%20en%20Lombardie.",
        "schema_name": "Vendre une maison en Lombardie",
        "schema_desc": "Hub avec 12 provinces lombardes pour analyse et stratégie de vente RE/MAX",
        "schema_list": "Provinces lombardes — vendre une maison",
        "path": "fr/vendre-maison/index.html",
        "url": "/fr/vendre-maison/",
        "lang": "fr",
        "locale": "fr_FR",
        "in_lang": "fr-FR",
        "buy_hub": "/fr/acheter-maison/",
        "home": "/fr/",
        "hreflang": {
            "it": "/vendere-casa/",
            "de": "/de/haus-verkaufen/",
            "fr": "/fr/vendre-maison/",
        },
    },
}


def cards_html(lang: str) -> str:
    parts = []
    for slug, name, _en in LOMBARD_PROVINCES:
        href = seller_url(slug, lang)
        label = city_label(slug, lang)
        img = f"/{'milano' if slug == 'milano' else slug}.jpg"
        blurb = BLURBS.get(slug, {}).get(lang, BLURBS[slug]["it"])
        tag = {"it": "IT →", "de": "DE →", "fr": "FR →"}[lang]
        parts.append(
            f'<a class="card" href="{href}"><img src="{img}" alt="{label}" loading="lazy">'
            f'<div class="card-body"><h3>{label}</h3><p>{blurb}</p>'
            f'<div class="card-links"><span>{tag}</span></div></div></a>'
        )
    return "\n        ".join(parts)


def why_cards(copy: dict) -> str:
    return "".join(
        f'<article class="seller-include-card"><span class="seller-include-icon">{n}</span>'
        f"<h3>{h}</h3><p>{p}</p></article>"
        for n, h, p in copy["cards"]
    )


def build(lang: str) -> str:
    c = COPY[lang]
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "name": c["schema_name"],
                "url": f"{BASE}{c['url']}",
                "description": c["schema_desc"],
                "inLanguage": c["in_lang"],
                "isPartOf": {"@type": "WebSite", "name": "Maurizio Piraino", "url": f"{BASE}/"},
            },
            {
                "@type": "ItemList",
                "name": c["schema_list"],
                "numberOfItems": 12,
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": i + 1,
                        "url": f"{BASE}{seller_url(slug, lang)}",
                        "name": city_label(slug, lang),
                    }
                    for i, (slug, _n, _e) in enumerate(LOMBARD_PROVINCES)
                ],
            },
        ],
    }
    hl = "".join(
        f'<link rel="alternate" hreflang="{code}" href="{BASE}{url}" />\n'
        for code, url in c["hreflang"].items()
    )
    hl += f'<link rel="alternate" hreflang="x-default" href="{BASE}/vendere-casa/" />\n'

    return f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="robots" content="index,follow" />
<title>{c['title']}</title>
<meta name="description" content="{c['desc']}" />
<link rel="canonical" href="{BASE}{c['url']}" />
{hl}<meta property="og:title" content="{c['title']}" />
<meta property="og:description" content="{c['desc']}" />
<meta property="og:type" content="website" />
<meta property="og:url" content="{BASE}{c['url']}" />
<meta property="og:locale" content="{c['locale']}" />
<meta property="og:image" content="{BASE}/milano.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=2)}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">
<style>
:root{{--black:#070707;--cream:#f6f1e9;--text:#222;--muted:#707070;--red:#dc1c2e;--red-dark:#b01828;--gold:#003da5;--line:rgba(0,0,0,.10);--radius:18px}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Inter,Arial,sans-serif;color:var(--text);background:var(--cream);line-height:1.6}}a{{color:inherit;text-decoration:none}}
.container{{width:min(1180px,calc(100% - 40px));margin:0 auto}}
.btn{{display:inline-flex;align-items:center;justify-content:center;min-height:50px;padding:0 24px;border-radius:7px;font-weight:900;background:linear-gradient(135deg,var(--red),var(--red-dark));color:#fff;box-shadow:0 14px 28px rgba(220,28,46,.25)}}
.btn-outline-dark{{background:#fff;color:var(--text);border:1px solid rgba(0,0,0,.15);box-shadow:none}}
.hero{{color:#fff;text-align:center;background:linear-gradient(135deg,#0c2749,#003da5);padding:72px 0 64px}}
.hero .kicker{{color:#ffd6d9;font-size:12px;font-weight:900;letter-spacing:.18em;text-transform:uppercase}}
.hero h1{{font-family:"Playfair Display",serif;font-size:clamp(32px,5vw,52px);margin:12px 0 16px;line-height:1.08}}
.hero p{{max-width:640px;margin:0 auto;color:rgba(255,255,255,.76);font-size:18px}}
.seller-stats-strip{{background:#fff;border-bottom:1px solid var(--line);padding:22px 0}}
.seller-stats-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;text-align:center}}
.seller-stat strong{{display:block;font-size:22px;color:#003da5}}
.seller-stat span{{font-size:12px;color:var(--muted);font-weight:700}}
.seller-includes{{padding:64px 0}}
.section-head{{text-align:center;margin-bottom:36px}}
.section-head h2{{font-family:"Playfair Display",serif;font-size:clamp(26px,3.5vw,38px);margin:8px 0 10px}}
.section-head p{{color:var(--muted);max-width:620px;margin:0 auto}}
.seller-includes-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}}
.seller-include-card{{background:#fff;border:1px solid #e6ddcf;border-radius:var(--radius);padding:22px}}
.seller-include-icon{{display:inline-block;font-weight:900;color:var(--red);margin-bottom:8px}}
.provinces{{padding:24px 0 88px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}}
.card{{background:#fff;border:1px solid #e6ddcf;border-radius:var(--radius);overflow:hidden;transition:transform .2s,box-shadow .2s}}
.card:hover{{transform:translateY(-3px);box-shadow:0 16px 36px rgba(0,0,0,.08)}}
.card img{{width:100%;height:150px;object-fit:cover;display:block}}
.card-body{{padding:16px 18px 20px}}
.card-body h3{{margin:0 0 8px;font-family:"Playfair Display",serif;font-size:22px}}
.card-body p{{margin:0 0 12px;color:var(--muted);font-size:14px}}
.card-links span{{font-weight:900;color:var(--red);font-size:13px}}
.footer{{background:#111;color:rgba(255,255,255,.72);padding:36px 0;text-align:center}}
.footer strong{{color:#fff;display:block;margin-bottom:10px}}
.editorial-bridge{{padding:48px 0;background:#fff;border-top:1px solid rgba(0,0,0,.06)}}
.editorial-bridge-inner{{display:grid;grid-template-columns:1.4fr 1fr;gap:28px;align-items:center;padding:32px 36px;border-radius:18px;background:var(--cream);border:1px solid rgba(0,61,165,.1)}}
.editorial-bridge h2{{font-family:"Playfair Display",serif;font-size:clamp(24px,3vw,32px);margin:0 0 12px;line-height:1.2}}
.editorial-bridge p{{margin:0;color:var(--muted)}}
.editorial-bridge-actions{{display:flex;flex-direction:column;gap:12px}}
.section-kicker{{font-size:12px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;color:var(--red);margin-bottom:8px}}
@media(max-width:800px){{.seller-stats-grid,.editorial-bridge-inner{{grid-template-columns:1fr 1fr}}.editorial-bridge-inner{{grid-template-columns:1fr}}}}
@media(max-width:520px){{.seller-stats-grid{{grid-template-columns:1fr}}}}
</style>
<link rel="stylesheet" href="/assets/site-nav.css?v=20260736" />
<link rel="stylesheet" href="/assets/site-base.css?v=20260736" />
<link rel="stylesheet" href="/assets/remax-brand.css?v=20260736" />
<link rel="stylesheet" href="/assets/consultant-home.css?v=20260715b" />
</head>
<body>
  <div class="site-chrome">
  <div class="topbar">
    <div class="container topbar-inner">
      <div class="topbar-tagline">{c['topbar']}</div>
      <div class="topbar-contact">
        <a class="topbar-wa topbar-wa-desktop" href="https://wa.me/393514581993?text={c['wa']}">WhatsApp</a>
      </div>
    </div>
  </div>
  <header class="site-header">
    <div class="container site-nav">
      <div class="brand-wrap">
        <a class="brand" href="{c['home']}">Maurizio Piraino</a>
        <span class="remax-nav-badge">RE/MAX</span>
      </div>
      <div class="site-nav-actions">
        <button type="button" class="nav-toggle" aria-label="Menu" aria-expanded="false" aria-controls="site-nav-panel">
          <span class="nav-toggle-bar"></span><span class="nav-toggle-bar"></span><span class="nav-toggle-bar"></span>
        </button>
      </div>
      <div class="nav-panel" id="site-nav-panel">
        <nav class="nav-links" aria-label="Menu">
          <div class="nav-group nav-group-path">
            <span class="nav-group-label">Percorso</span>
            <div class="nav-group-links">
              <a href="{c['url']}" class="nav-link-primary">{c['sell_label']}</a>
              <a href="{c['buy_hub']}">{c['buy_label']}</a>
            </div>
          </div>
          <a class="btn btn-red nav-cta" href="{seller_url('milano', lang)}">{c['cta']}</a>
        </nav>
      </div>
      <div class="nav-backdrop" hidden></div>
    </div>
  </header>
  <div class="remax-stripe" aria-hidden="true"></div>
</div>
<main id="main">
  <section class="hero hub-hero">
    <div class="container">
      <div class="kicker">{c['kicker']}</div>
      <h1>{c['h1']}</h1>
      <p>{c['lead']}</p>
    </div>
  </section>
  <section class="hub-stats-bar seller-stats-strip" aria-label="Stats">
    <div class="container seller-stats-grid">
      <div class="seller-stat"><strong>12</strong><span>Province</span></div>
      <div class="seller-stat"><strong>OMI</strong><span>Dati ufficiali</span></div>
      <div class="seller-stat"><strong>24h</strong><span>Risposta</span></div>
      <div class="seller-stat"><strong>0 €</strong><span>Analisi iniziale</span></div>
    </div>
  </section>
  <section class="seller-includes">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">{c['why_k']}</div>
        <h2>{c['why_h']}</h2>
        <p>{c['why_p']}</p>
      </div>
      <div class="seller-includes-grid">{why_cards(c)}</div>
    </div>
  </section>
  <section class="provinces">
    <div class="container">
      <div class="section-head">
        <h2>{c['pick_h']}</h2>
        <p>{c['pick_p']}</p>
      </div>
      <div class="grid">
        {cards_html(lang)}
      </div>
      <p style="text-align:center;margin-top:32px;color:var(--muted)">{c['buy_link']}</p>
    </div>
  </section>
</main>
<section class="editorial-bridge" aria-label="ValoreCasaTua">
  <div class="container">
    <div class="editorial-bridge-inner">
      <div>
        <div class="section-kicker">ValoreCasaTua</div>
        <h2>ValoreCasaTua.it informa. Qui trasformiamo l'informazione in consulenza.</h2>
        <p>Guide e approfondimenti sul portale editoriale. Su MaurizioPiraino.it: analisi vendita, Property Finding e tutela fino al rogito.</p>
      </div>
      <div class="editorial-bridge-actions">
        <a class="btn" href="{seller_url('milano', lang)}">{c['cta']}</a>
        <a class="btn btn-outline-dark" href="https://valorecasatua.it/" rel="noopener" target="_blank">ValoreCasaTua.it →</a>
      </div>
    </div>
  </div>
</section>
<footer class="footer">
  <div class="container">
    <strong>{c['footer_s']}</strong>
    <div>Maurizio Piraino — RE/MAX Associati Real Estate · Milano</div>
    <div style="margin-top:12px">
      <a href="{c['buy_hub']}" style="color:inherit;text-decoration:underline">{c['buy_label']}</a>
      · <a href="https://valorecasatua.it/" rel="noopener" target="_blank" style="color:inherit;text-decoration:underline">ValoreCasaTua.it</a>
      · <a href="/privacy/" style="color:inherit;text-decoration:underline">Privacy</a>
    </div>
  </div>
</footer>
<script src="/assets/site-nav.js?v=20260736" defer></script>
</body>
</html>
"""


def main() -> None:
    for lang in ("it", "de", "fr"):
        rel = COPY[lang]["path"]
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(build(lang), encoding="utf-8")
        print(f"  wrote {rel}")
    print("Done.")


if __name__ == "__main__":
    main()
