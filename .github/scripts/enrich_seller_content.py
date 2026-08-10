#!/usr/bin/env python3
"""Inject rich content sections into seller landing pages."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

CITIES = {
    "index.html": {
        "city": "Milano",
        "area": "Milano e provincia",
        "omi": "/guida-prezzi-mq-milano/",
        "buy": "/comprare-casa-milano/",
        "market_lead": "Milano cambia quartiere per quartiere. Un appartamento a Porta Romana non segue le stesse dinamiche di Lambrate, Isola o Navigli.",
        "zones": [
            "Centro / Duomo",
            "Brera · Moscova",
            "Navigli · Ticinese",
            "Isola · Porta Nuova",
            "Porta Romana",
            "CityLife · Fiera",
            "Lambrate · Ortica",
            "Corso Sempione",
            "Provincia MI",
        ],
        "testimonial_extra": (
            '<article class="testimonial-card reveal"><div class="stars">★★★★★</div>'
            "<p>Eravamo indecisi se vendere ora o aspettare. L'analisi sui dati OMI e sulle compravendite recenti in zona ci ha dato chiarezza senza pressioni commerciali.</p>"
            '<div class="person"><div class="avatar">AC</div><div><strong>Proprietari · CityLife</strong><span>CityLife · Milano</span></div></div></article>'
        ),
    },
    "bergamo/index.html": {
        "city": "Bergamo",
        "area": "Bergamo città e provincia",
        "omi": "/guida-prezzi-mq-bergamo/",
        "buy": "/comprare-casa-bergamo/",
        "market_lead": "Bergamo Alta, Borgo Palazzo, Val Seriana e i comuni della provincia hanno dinamiche di prezzo molto diverse tra loro.",
        "zones": [
            "Città Alta",
            "Centro · Lower Town",
            "Borgo Palazzo",
            "Colognola",
            "Val Seriana",
            "Val Brembana",
            "Dalmine · Treviglio",
            "Lago d'Iseo",
            "Provincia BG",
        ],
        "testimonial_extra": (
            '<article class="testimonial-card reveal"><div class="stars">★★★★★</div>'
            "<p>Vendere un immobile in Città Alta richiede attenzione ai dettagli tecnici e alla comunicazione giusta. L'approccio strutturato ha fatto la differenza nella trattativa.</p>"
            '<div class="person"><div class="avatar">PB</div><div><strong>Proprietario · Città Alta</strong><span>Bergamo Alta</span></div></div></article>'
        ),
    },
    "brescia/index.html": {
        "city": "Brescia",
        "area": "Brescia città e provincia",
        "omi": "/guida-prezzi-mq-brescia/",
        "buy": "/comprare-casa-brescia/",
        "market_lead": "Brescia centro, la Franciacorta, il Garda bresciano e le valli hanno domanda, prezzi e tempi di vendita completamente diversi.",
        "zones": [
            "Centro storico",
            "San Polo · Mompiano",
            "Franciacorta",
            "Lago di Garda",
            "Val Trompia",
            "Desenzano · Salò",
            "Montichiari",
            "Provincia BS",
        ],
        "testimonial_extra": (
            '<article class="testimonial-card reveal"><div class="stars">★★★★★</div>'
            "<p>Immobile in zona Franciacorta: serviva capire il giusto posizionamento rispetto a ville simili in vendita. Analisi precisa e vendita conclusa senza mesi di attesa inutile.</p>"
            '<div class="person"><div class="avatar">LV</div><div><strong>Proprietaria · Franciacorta</strong><span>Erbusco · Brescia</span></div></div></article>'
        ),
    },
}

FAQ_EXTRA = """
          <details><summary>Quanto tempo serve per ricevere l'analisi?</summary><p>Di solito entro 24–48 ore lavorative dal modulo. Se serve approfondire documenti o visite, te lo comunico subito con tempi chiari.</p></details>
          <details><summary>Lavori solo su {city} o anche in provincia?</summary><p>Opero su {area} e, tramite RE/MAX, posso coordinarmi anche con colleghi nelle altre province lombarde se il tuo immobile o il tuo obiettivo lo richiede.</p></details>
          <details><summary>Cosa succede dopo l'analisi se decido di non vendere?</summary><p>Nessun problema. L'analisi resta un asset per te: saprai il valore reale, i tempi di mercato e cosa conviene fare quando deciderai di muoverti.</p></details>
"""


def render_enrichment(cfg: dict) -> str:
    city = cfg["city"]
    zones = "".join(f'<span class="seller-zone-chip">{z}</span>' for z in cfg["zones"])
    return f"""
    <section class="seller-stats-strip" aria-label="Numeri RE/MAX">
      <div class="container seller-stats-grid">
        <div class="seller-stat"><strong>140+</strong><span>Paesi con RE/MAX nel mondo</span></div>
        <div class="seller-stat"><strong>12</strong><span>Province lombarde seguite</span></div>
        <div class="seller-stat"><strong>24h</strong><span>Risposta alla tua richiesta</span></div>
        <div class="seller-stat"><strong>0 €</strong><span>Analisi iniziale · nessun obbligo</span></div>
      </div>
    </section>

    <section class="seller-includes">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Cosa ricevi</div>
          <h2>L'analisi riservata non è una stima automatica.</h2>
          <p>È un confronto strutturato sul tuo immobile, sulla micro-zona e sulla strategia di vendita più adatta a {city}.</p>
        </div>
        <div class="seller-includes-grid">
          <article class="seller-include-card reveal"><span class="seller-include-icon">01</span><h3>Valore di mercato reale</h3><p>Confronto con immobili comparabili venduti e in vendita nella tua zona, non medie generiche.</p></article>
          <article class="seller-include-card reveal"><span class="seller-include-icon">02</span><h3>Dati OMI ufficiali</h3><p>Riferimenti Agenzia delle Entrate integrati con il contesto reale del quartiere o del comune.</p></article>
          <article class="seller-include-card reveal"><span class="seller-include-icon">03</span><h3>Criticità tecniche</h3><p>Piano, conformità, stato, spazi esterni: ciò che un acquirente farà emergere in trattativa.</p></article>
          <article class="seller-include-card reveal"><span class="seller-include-icon">04</span><h3>Tempi di vendita stimati</h3><p>Quanto potrebbe restare online un immobile posizionato correttamente — o no — nel mercato attuale.</p></article>
          <article class="seller-include-card reveal"><span class="seller-include-icon">05</span><h3>Strategia di prezzo</h3><p>Range consigliato, leva trattativa e timing di uscita sul mercato.</p></article>
          <article class="seller-include-card reveal"><span class="seller-include-icon">06</span><h3>Piano RE/MAX</h3><p>Visibilità, rete MLS e canali se decidi di procedere — sempre senza obbligo dopo l'analisi.</p></article>
        </div>
      </div>
    </section>

    <section class="seller-compare">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Perché non basta online</div>
          <h2>Stima automatica vs analisi professionale.</h2>
          <p>Le valutazioni online sono utili come punto di partenza, ma non sostituiscono una lettura tecnica e di mercato del singolo immobile.</p>
        </div>
        <div class="seller-compare-table reveal">
          <div class="seller-compare-row seller-compare-head">
            <span>Criterio</span><span>Stima online</span><span>Analisi RE/MAX</span>
          </div>
          <div class="seller-compare-row"><span>Micro-zona e quartiere</span><span class="no">Media generica</span><span class="yes">Analisi specifica</span></div>
          <div class="seller-compare-row"><span>Stato, piano, affaccio</span><span class="no">Non considerati</span><span class="yes">Valutati uno per uno</span></div>
          <div class="seller-compare-row"><span>Documenti e conformità</span><span class="no">Assenti</span><span class="yes">Verifica tecnica</span></div>
          <div class="seller-compare-row"><span>Strategia di vendita</span><span class="no">Solo un numero</span><span class="yes">Piano completo</span></div>
          <div class="seller-compare-row"><span>Obbligo di incarico</span><span class="na">—</span><span class="yes">Mai, alla prima analisi</span></div>
        </div>
      </div>
    </section>

    <section class="seller-zones">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Zone servite · {city}</div>
          <h2>Conosco il mercato locale, strada per strada.</h2>
          <p>{cfg["market_lead"]}</p>
        </div>
        <div class="seller-zones-wrap reveal">{zones}</div>
        <p class="seller-zones-link"><a href="{cfg["omi"]}">Consulta i valori OMI ufficiali per zona a {city} →</a></p>
      </div>
    </section>

    <section class="seller-services consultant-services" id="servizi">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Servizi</div>
          <h2>Consulenza completa: compra, investi o vendi.</h2>
          <p>Property Finding e investitori in primo piano. La vendita resta un percorso strutturato se ti serve.</p>
        </div>
        <div class="seller-services-grid">
          <article class="seller-service-card featured reveal"><div class="seller-service-num">01</div><h3>Property Finding</h3><p>Ricerca personalizzata anche off-market, visite, negoziazione e tutela fino al rogito.</p></article>
          <article class="seller-service-card reveal"><div class="seller-service-num">02</div><h3>Consulenza per investitori</h3><p>Opportunità a reddito, valorizzazione e analisi della redditività con numeri chiari.</p></article>
          <article class="seller-service-card reveal"><div class="seller-service-num">03</div><h3>Chi compra casa</h3><p>Prima casa o cambio abitazione: verifica documentale e supporto in trattativa.</p></article>
          <article class="seller-service-card secondary reveal"><div class="seller-service-num">04</div><h3>Valutazione e vendita</h3><p>Analisi OMI, strategia di prezzo, marketing RE/MAX e affiancamento fino al rogito.</p></article>
        </div>
      </div>
    </section>

    <section class="seller-mid-cta">
      <div class="container reveal">
        <div class="seller-mid-cta-inner">
          <div>
            <p class="seller-mid-kicker">RE/MAX · {city}</p>
            <h2>Cerchi casa, investi o vendi a {city}?</h2>
            <p>Consulenza riservata su dati reali. Nessun obbligo, risposta entro 24 ore.</p>
          </div>
          <div class="seller-mid-actions">
            <a class="btn btn-red" href="{cfg["buy"]}">Property Finding →</a>
            <a class="btn btn-light" href="#form">Analisi vendita →</a>
          </div>
        </div>
      </div>
    </section>"""


def ensure_dual_path_intro(html: str) -> str:
    if "dual-path-intro" in html:
        return html
    return html.replace(
        '<div class="container dual-path-grid">',
        '<div class="container dual-path-grid">\n        <p class="dual-path-intro"><em>RE/MAX</em> · Scegli il tuo percorso</p>',
        1,
    )


def inject_after_dual_path(html: str, block: str) -> str:
    if "seller-stats-strip" in html:
        return html
    pattern = re.compile(
        r'(<section class="dual-path"[^>]*>.*?</section>)',
        re.DOTALL,
    )
    match = pattern.search(html)
    if not match:
        print("  skip: dual-path not found")
        return html
    return html[: match.end()] + block + html[match.end() :]


def expand_faq(html: str, city: str, area: str) -> str:
    if "Quanto tempo serve per ricevere l'analisi?" in html:
        return html
    extra = FAQ_EXTRA.format(city=city, area=area)
    return html.replace(
        '<details><summary>Non ho fretta di vendere',
        extra + '\n          <details><summary>Non ho fretta di vendere',
        1,
    )


def add_testimonial(html: str, extra: str) -> str:
    marker = '<div class="section-kicker">FAQ</div>'
    if extra[:80] in html or "Proprietario · CityLife" in html or "Proprietario · Città Alta" in html or "Proprietaria · Franciacorta" in html:
        return html
    return html.replace(
        f"        </div>\n      </div>\n    </section>\n    <section>\n      <div class=\"container\">\n        <div class=\"section-head reveal\">\n          {marker}",
        f"        {extra.strip()}\n        </div>\n      </div>\n    </section>\n    <section>\n      <div class=\"container\">\n        <div class=\"section-head reveal\">\n          {marker}",
        1,
    )


def patch_file(rel: str, cfg: dict) -> bool:
    path = ROOT / rel
    html = path.read_text(encoding="utf-8")
    original = html
    html = ensure_dual_path_intro(html)
    html = inject_after_dual_path(html, render_enrichment(cfg))
    html = expand_faq(html, cfg["city"], cfg["area"])
    html = add_testimonial(html, cfg["testimonial_extra"])
    if html != original:
        path.write_text(html, encoding="utf-8")
        print(f"  enriched: {rel}")
        return True
    print(f"  unchanged: {rel}")
    return False


def main() -> None:
    for rel, cfg in CITIES.items():
        patch_file(rel, cfg)
    print("Done.")


if __name__ == "__main__":
    main()
