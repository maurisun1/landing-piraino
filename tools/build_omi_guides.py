#!/usr/bin/env python3
"""Build /guida-prezzi-mq-*/ pages from seo/omi-guides.json (self-canonical, expanded content)."""
from __future__ import annotations

import json
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "seo" / "omi-guides.json").read_text(encoding="utf-8"))


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def clean_zones(city: dict) -> list[dict]:
    """Keep only rows with real values; drop any cell with [DATO DA INSERIRE]."""
    out = []
    for z in city["zones"]:
        vals = f"{z.get('min','')} {z.get('max','')}"
        if "[DATO DA INSERIRE]" in vals:
            continue
        out.append(z)
    return out


def zone_rows(city: dict) -> str:
    rows = []
    for z in clean_zones(city):
        rows.append(
            f"<tr><td>{esc(z['zone'])}</td><td>{esc(z['min'])}</td>"
            f"<td>{esc(z['max'])}</td><td>{esc(z['note'])}</td></tr>"
        )
    return "\n".join(rows)


def table_footnote(city: dict) -> str:
    href = city.get("valutazione_url") or "#valutazione"
    label = "valutazione gratuita"
    return (
        f'<p class="note omi-table-footnote">Valori indicativi su base OMI (Agenzia delle Entrate). '
        f'Per la micro-zona esatta richiedi una <a href="{esc(href)}">{label}</a>.</p>'
    )


def faq_entities_schema(city: dict, base: str) -> str:
    name = city["name"]
    faqs = [
        (
            f"Cosa sono i valori OMI a {name}?",
            f"Sono fasce statistiche dell'Agenzia delle Entrate per micro-zona e tipologia. "
            f"Servono come riferimento, non come stima del singolo immobile.",
        ),
        (
            f"I prezzi OMI coincidono con i prezzi di compravendita a {name}?",
            "Non necessariamente. Il prezzo reale dipende da stato, piano, domanda, documenti e trattativa. "
            "Lo scostamento tipico può arrivare al 15–20% rispetto alla fascia.",
        ),
        (
            f"Posso usare l'OMI come perizia a {name}?",
            "No. L'OMI non è una perizia ai sensi della L. 39/1989. Per una valutazione operativa "
            "serve analisi di immobile, zona e mercato recente.",
        ),
        (
            f"Dove trovo le tabelle OMI complete per {name}?",
            f"Le tabelle ufficiali sono dell'Agenzia delle Entrate; un approfondimento editoriale zona per zona "
            f"è anche su ValoreCasaTua.it. Qui trovi lettura consulenziale e supporto RE/MAX.",
        ),
        (
            f"Come richiedo una valutazione a {name}?",
            "Puoi scrivere su WhatsApp o usare il form: ti rispondo con una prima lettura senza obbligo di incarico.",
        ),
    ]
    entities = []
    for q, a in faqs:
        entities.append(
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
        )
    import json as _json

    return _json.dumps(
        {"@type": "FAQPage", "@id": f"{base}#faq", "mainEntity": entities},
        ensure_ascii=False,
    )


def faq_html(city: dict) -> str:
    name = city["name"]
    items = [
        (
            f"Cosa sono i valori OMI a {name}?",
            f"Sono fasce statistiche dell&apos;Agenzia delle Entrate per micro-zona e tipologia. "
            f"Servono come riferimento, non come stima del singolo immobile.",
        ),
        (
            f"I prezzi OMI coincidono con i prezzi di compravendita a {name}?",
            "Non necessariamente. Il prezzo reale dipende da stato, piano, domanda, documenti e trattativa. "
            "Lo scostamento tipico può arrivare al 15–20% rispetto alla fascia.",
        ),
        (
            f"Posso usare l&apos;OMI come perizia a {name}?",
            "No. L&apos;OMI non è una perizia ai sensi della L. 39/1989. Per una valutazione operativa "
            "serve analisi di immobile, zona e mercato recente.",
        ),
        (
            f"Dove trovo le tabelle OMI complete per {name}?",
            f"Le tabelle ufficiali sono dell&apos;Agenzia delle Entrate; un approfondimento editoriale zona per zona "
            f"è anche su <a href=\"{esc(city['vct_url'])}\">ValoreCasaTua.it</a>. Qui trovi lettura consulenziale e supporto RE/MAX.",
        ),
        (
            f"Come richiedo una valutazione a {name}?",
            "Puoi scrivere su WhatsApp o usare il form: ti rispondo con una prima lettura senza obbligo di incarico.",
        ),
    ]
    out = []
    for q, a in items:
        out.append(f"<details><summary>{q}</summary><p>{a}</p></details>")
    return "\n".join(out)


def factors_list(city: dict) -> str:
    return "\n".join(f"<li>{esc(x)}</li>" for x in city["local_factors"])


def related_links(city: dict) -> str:
    return "\n".join(
        f'<a href="{esc(x["href"])}">{esc(x["label"])}</a>' for x in city["related_internal"]
    )


def build_page(city: dict) -> str:
    year = DATA["year"]
    name = city["name"]
    slug = city["slug"]
    base = f"https://mauriziopiraino.it/guida-prezzi-mq-{slug}/"
    title = city["title"]
    desc = city["description"]
    assert len(title) <= 60, (slug, len(title), title)
    assert len(desc) <= 155, (slug, len(desc), desc)

    faq_schema = faq_entities_schema(city, base)

    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="apple-touch-icon" href="/favicon.svg" />
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}" />
<meta name="robots" content="index, follow" />
<link rel="canonical" href="{base}" />
<link rel="alternate" hreflang="it" href="{base}" />
<link rel="alternate" hreflang="x-default" href="{base}" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{esc(title)}" />
<meta property="og:description" content="{esc(desc)}" />
<meta property="og:url" content="{base}" />
<meta property="og:image" content="https://mauriziopiraino.it{esc(city['hero_img'].split('?')[0])}" />
<meta property="og:locale" content="it_IT" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "WebPage",
      "@id": "{base}#webpage",
      "url": "{base}",
      "name": {json.dumps(title, ensure_ascii=False)},
      "description": {json.dumps(desc, ensure_ascii=False)},
      "inLanguage": "it-IT",
      "isPartOf": {{"@type": "WebSite", "url": "https://mauriziopiraino.it/"}},
      "mainEntity": {{"@id": "https://mauriziopiraino.it/#agent"}}
    }},
    {{
      "@type": ["Person", "RealEstateAgent"],
      "@id": "https://mauriziopiraino.it/#agent",
      "name": "Maurizio Piraino",
      "jobTitle": "Agente Immobiliare affiliato RE/MAX",
      "url": "https://mauriziopiraino.it/",
      "telephone": "+39 351 458 1993",
      "areaServed": ["{esc(name)}", "Lombardia"]
    }},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://mauriziopiraino.it/"}},
        {{"@type": "ListItem", "position": 2, "name": "Valori OMI {esc(name)}", "item": "{base}"}}
      ]
    }},
    {faq_schema}
  ]
}}
</script>
<style>
:root{{--black:#070707;--cream:#f6f1e9;--warm:#eee3d5;--text:#222;--muted:#707070;--red:#dc1c2e;--red-dark:#b01828;--gold:#003da5;--line:rgba(0,0,0,.10);}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{font-family:'Inter',sans-serif;background:var(--cream);color:var(--text);line-height:1.65;-webkit-font-smoothing:antialiased;}}
.serif{{font-family:'Playfair Display',serif;}}
.wrap{{max-width:760px;margin:0 auto;padding:0 22px;}}
.eyebrow{{color:var(--gold);font-size:12px;font-weight:600;letter-spacing:1.4px;text-transform:uppercase;margin-bottom:14px;}}
h1{{font-size:clamp(28px,5vw,42px);line-height:1.15;font-weight:700;color:var(--black);}}
.date{{display:flex;align-items:center;gap:7px;color:var(--muted);font-size:14px;margin-top:14px;}}
.lead{{font-size:18px;line-height:1.6;margin:26px 0;}}
section{{margin:40px 0;}}
h2{{font-family:'Playfair Display',serif;font-size:26px;font-weight:600;color:var(--black);margin-bottom:14px;}}
p{{margin:0 0 16px;font-size:16px;color:#333;}}
ul,ol{{margin:0 0 16px 1.2em;}}
li{{margin:0 0 8px;}}
table.omi-table{{width:100%;border-collapse:collapse;font-size:14px;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;margin:18px 0 24px;}}
table.omi-table th,table.omi-table td{{padding:10px 12px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;}}
table.omi-table th{{background:rgba(0,61,165,.06);font-size:12px;text-transform:uppercase;letter-spacing:.04em;}}
.note{{font-size:13px;color:var(--muted);}}
.vct-box{{background:#fff;border:2px solid var(--gold);border-radius:14px;padding:28px 24px;margin:36px 0;text-align:center;}}
.vct-box a.vct-cta{{display:inline-block;background:var(--gold);color:#fff;text-decoration:none;font-weight:700;font-size:15px;padding:14px 28px;border-radius:10px;}}
.vct-box .vct-note{{margin-top:14px;font-size:13px;color:var(--muted);}}
.cta{{background:var(--black);border-radius:18px;padding:40px 30px;text-align:center;margin:48px 0;}}
.cta p{{color:var(--cream);font-size:20px;font-family:'Playfair Display',serif;margin-bottom:22px;}}
.cta a{{display:inline-block;background:var(--red);color:#fff;text-decoration:none;font-weight:600;font-size:16px;padding:15px 34px;border-radius:10px;}}
.links{{display:flex;flex-wrap:wrap;gap:10px;margin:30px 0;}}
.links a{{font-size:14px;color:var(--red-dark);text-decoration:none;border:1px solid var(--line);padding:9px 16px;border-radius:8px;background:#fff;}}
details{{border-bottom:1px solid var(--line);padding:12px 0;}}
summary{{cursor:pointer;font-weight:700;color:var(--black);}}
details p{{margin:10px 0 0;}}
footer{{background:var(--warm);padding:30px 0;margin-top:50px;font-size:12.5px;color:var(--muted);line-height:1.6;}}
.disc{{font-size:11.5px;margin-top:14px;opacity:.85;}}
</style>
<link rel="stylesheet" href="/assets/site-base.css?v=20260735" />
<link rel="stylesheet" href="/assets/remax-brand.css?v=20260735" />
<link rel="stylesheet" href="/assets/site-nav.css?v=20261009" />
</head>
<body>
<a class="skip-link" href="#main">Salta al contenuto</a>
<div class="site-chrome">
  <div class="topbar">
    <div class="container topbar-inner">
      <div class="topbar-tagline"><strong>Maurizio Piraino</strong> · Valori OMI · {esc(name)}</div>
      <div class="topbar-contact">
        <a class="topbar-phone" href="tel:+393514581993">351 458 1993</a>
        <a class="topbar-wa topbar-wa-desktop" href="https://wa.me/393514581993?text=Ciao%20Maurizio%2C%20vorrei%20parlare%20dei%20valori%20OMI%20a%20{esc(name)}.">WhatsApp</a>
      </div>
    </div>
  </div>
  <header class="site-header">
    <div class="container site-nav">
      <div class="brand-wrap">
        <a class="brand" href="/">Maurizio Piraino</a>
        <span class="remax-nav-badge">RE/MAX</span>
      </div>
      <div class="site-nav-actions">
        <a class="btn btn-wa nav-wa-compact" href="https://wa.me/393514581993?text=Ciao%20Maurizio%2C%20vorrei%20parlare%20dei%20valori%20OMI%20a%20{esc(name)}." aria-label="WhatsApp">WA</a>
        <button type="button" class="nav-toggle" aria-label="Apri menu" aria-expanded="false" aria-controls="site-nav-panel">
          <span class="nav-toggle-bar"></span><span class="nav-toggle-bar"></span><span class="nav-toggle-bar"></span>
        </button>
      </div>
      <div class="nav-panel" id="site-nav-panel">
        <nav class="nav-links" aria-label="Menu principale">
          <div class="nav-group nav-group-path">
            <span class="nav-group-label">Percorso</span>
            <div class="nav-group-links">
              <a href="/comprare-casa/" class="nav-link-core">Comprare</a>
              <a href="{esc(city['sell_url'])}" class="nav-link-core">Vendere</a>
              <span class="nav-path-sep" aria-hidden="true"></span>
              <a href="/immobili-commerciali/" class="nav-link-soft">Commerciali</a>
              <a href="/sviluppo-immobiliare/" class="nav-link-soft">Sviluppo</a>
            </div>
          </div>
          <a class="btn btn-red nav-cta" href="#valutazione">Richiedi valutazione</a>
        </nav>
      </div>
      <div class="nav-backdrop" hidden></div>
    </div>
  </header>
  <div class="remax-stripe" aria-hidden="true"></div>
</div>

<main class="wrap" id="main">
  <section style="margin-top:46px;">
    <div class="eyebrow">Guida OMI {year} · {esc(name)} · Consulenza RE/MAX</div>
    <h1 class="serif">{esc(city['h1'])}</h1>
    <div class="date">Riferimento: {esc(DATA['omi_ref'])}</div>
    <p class="lead">Capire i <strong>valori OMI a {esc(name)}</strong> serve prima di comprare, vendere o investire: ti danno una cornice statistica di zona. Non sostituiscono l&apos;analisi del singolo immobile, ma evitano di partire da un prezzo &quot;a sensazione&quot; o da un annuncio fuori mercato.</p>
    <p>Su questo sito trovi una lettura operativa dei dati e il supporto consulenziale. Le tabelle ufficiali restano dell&apos;Agenzia delle Entrate; un approfondimento editoriale zona per zona è anche su <a href="{esc(city['vct_url'])}">ValoreCasaTua.it</a>.</p>
  </section>

  <section id="valori">
    <h2 class="serif">Valori OMI {esc(name)} {year} per zona</h2>
    <p>Secondo i dati OMI più recenti disponibili, le abitazioni civili a {esc(name)} si collocano in una fascia indicativa di <strong>{esc(city['range_text'])}</strong>. La tabella sotto è una sintesi orientativa delle fasce note; per il dettaglio di micro-zona serve il confronto ufficiale e una lettura sul singolo immobile.</p>
    <table class="omi-table">
      <thead><tr><th>Zona / ambito</th><th>Min €/mq</th><th>Max €/mq</th><th>Nota</th></tr></thead>
      <tbody>
{zone_rows(city)}
      </tbody>
    </table>
{table_footnote(city)}
    <p class="note">I valori OMI sono fasce (min–max) per tipologia e stato conservativo, non prezzi di listino. Prima di un&apos;offerta o di una messa in vendita conviene confrontarli con compravendite recenti e con lo stato reale dell&apos;immobile.</p>
    <p>A {esc(name)} la differenza tra due immobili &quot;vicini sulla mappa&quot; può essere ampia: cambia la micro-zona, cambia la domanda, cambiano i tempi di vendita. Per questo la lettura OMI va sempre calata sul contesto locale e sull&apos;obiettivo (acquisto abitativo, investimento, vendita rapida o valorizzazione).</p>
  </section>

  <div class="vct-box">
    <p><strong>Approfondimento editoriale zona per zona</strong> su ValoreCasaTua.it</p>
    <a class="vct-cta" href="{esc(city['vct_url'])}">Apri la guida completa su ValoreCasaTua.it →</a>
    <p class="vct-note">Link alla fonte editoriale · qui restano consulenza e lettura operativa</p>
  </div>

  <section id="come-leggere">
    <h2 class="serif">Come si leggono le quotazioni OMI</h2>
    <p>L&apos;<strong>OMI</strong> (Osservatorio del Mercato Immobiliare) pubblica fasce di valore al mq basate su un campione di compravendite e su criteri statistici. È uno strumento pubblico, aggiornato periodicamente, utile per orientarsi — non per chiudere un prezzo al centesimo.</p>
    <p><strong>OMI vs prezzi reali di mercato:</strong> l&apos;OMI descrive un intervallo tipico di zona. Il prezzo reale nasce da trattativa, urgenza delle parti, qualità dell&apos;immobile e pressione della domanda. Un annuncio sopra la fascia alta non è automaticamente &quot;fuori mercato&quot; se l&apos;immobile è raro o ristrutturato in modo eccellente; allo stesso modo, un prezzo dentro la fascia non garantisce un buon affare.</p>
    <p>In pratica uso l&apos;OMI così:</p>
    <ol>
      <li>inquadro la micro-zona e la tipologia (civile, signorile, villino, ecc.);</li>
      <li>confronto la fascia con annunci e, dove possibile, con compravendite recenti;</li>
      <li>correggo per stato, piano, classe energetica e documenti;</li>
      <li>definisco una strategia di prezzo o di offerta coerente con l&apos;obiettivo.</li>
    </ol>
    <p>Se stai comprando a {esc(name)}, ti serve capire se stai pagando un premium giustificato. Se stai vendendo, ti serve un posizionamento credibile: troppo alto brucia l&apos;annuncio; troppo basso lascia valore sul tavolo.</p>
  </section>

  <section id="quanto-vale">
    <h2 class="serif">Quanto vale la mia casa a {esc(name)}?</h2>
    <p>La domanda giusta non è solo &quot;quanto dice l&apos;OMI?&quot;, ma &quot;quanto può valere <em>questo</em> immobile, in <em>questa</em> micro-zona, in <em>queste</em> condizioni di mercato?&quot;. Fattori che spostano il prezzo:</p>
    <ul>
{factors_list(city)}
    </ul>
    <p>Due appartamenti con la stessa superficie OMI possono avere esiti molto diversi: uno piano alto luminoso con documenti in ordine si muove meglio di un piano basso umido con pratiche incomplete. La valutazione operativa tiene conto di questi elementi e della platea di acquirenti reali a {esc(name)}.</p>
    <p>Per i proprietari: una stima utile serve a decidere se vendere ora, se riposizionare il prezzo, se investire in home staging o in lavori mirati. Per gli acquirenti: serve a calibrare l&apos;offerta e a evitare aste al rialzo emotive.</p>
  </section>

  <section id="omi-vs-listini">
    <h2 class="serif">OMI vs Borsa Immobiliare / listini: differenze</h2>
    <p>Oltre all&apos;OMI esistono listini e rilevazioni di settore (ad esempio riferimenti di Borsa Immobiliare o osservatori privati). Non misurano tutti la stessa cosa:</p>
    <ul>
      <li><strong>OMI:</strong> fasce statistiche pubbliche per zona e tipologia; base utile e confrontabile nel tempo.</li>
      <li><strong>Listini / Borsa Immobiliare:</strong> spesso raccolgono prezzi medi o valori di riferimento di mercato locale, con metodologie proprie; utili come secondo sguardo, non come verità assoluta.</li>
      <li><strong>Annunci online:</strong> esprimono prezzi <em>richiesti</em>, spesso sopra il prezzo finale di compravendita.</li>
    </ul>
    <p>La lettura corretta combina queste fonti senza confonderle. A {esc(name)} uso OMI come telaio, poi verifico tenuta degli annunci e feedback reale di visite e offerte. È questo che trasforma un numero al mq in una decisione.</p>
  </section>

  <section id="faq">
    <h2 class="serif">FAQ — Valori OMI {esc(name)}</h2>
    {faq_html(city)}
  </section>

  <section id="valutazione">
    <h2 class="serif">Richiedi una valutazione gratuita</h2>
    <p>Se vuoi una lettura dei valori OMI applicata al tuo caso a {esc(name)} — compra, vendita o investimento — possiamo partire da un primo confronto senza obbligo di incarico.</p>
    <div class="cta">
      <p>Richiedi una valutazione gratuita</p>
      <a href="https://wa.me/393514581993?text=Ciao%20Maurizio%2C%20vorrei%20una%20valutazione%20a%20{esc(name)}.">Scrivimi su WhatsApp</a>
    </div>
  </section>

  <div class="links">
{related_links(city)}
    <a href="{esc(city['vct_url'])}">Guida completa su ValoreCasaTua</a>
  </div>
</main>

<aside class="guide-cta-links" aria-label="Passaggi successivi"><p>Hai un immobile a {esc(name)}? <a href="{esc(city['sell_url'])}">Area venditori</a> · <a href="{esc(city['buy_url'])}">Consulenza per chi compra</a></p></aside>
<footer><div class="wrap">
  <strong>Maurizio Piraino</strong><br>
  <div class="footer-affiliation">Maurizio Piraino — Consulente immobiliare presso RE/MAX Associati Real Estate · Milano, Viale Gran Sasso 31</div>
  · Agente Immobiliare affiliato RE/MAX · REA BS-639579
  <div class="disc">I valori OMI sono riferimenti statistici dell&apos;Agenzia delle Entrate e non costituiscono stima o valutazione ai sensi della L. 39/1989. Approfondimento editoriale anche su <a href="{esc(city['vct_url'])}">ValoreCasaTua.it</a>.</div>
</div></footer>
<script src="/assets/site-nav.js?v=20261009" defer></script>
<script src="/assets/analytics.js?v=20261002i" defer></script>
</body>
</html>
"""


def main() -> None:
    import re

    for city in DATA["cities"]:
        dropped = [
            z["zone"]
            for z in city["zones"]
            if "[DATO DA INSERIRE]" in f"{z.get('min','')} {z.get('max','')}"
        ]
        html_out = build_page(city)
        if "[DATO DA INSERIRE]" in html_out:
            raise SystemExit(f"Refusing to write guide with placeholder: {city['slug']}")
        text = re.sub(r"<[^>]+>", " ", html_out)
        words = len(re.findall(r"\w+", text, flags=re.UNICODE))
        out = ROOT / f"guida-prezzi-mq-{city['slug']}" / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html_out, encoding="utf-8")
        msg = f"wrote {out.relative_to(ROOT)} words~{words} title_len={len(city['title'])} desc_len={len(city['description'])}"
        if dropped:
            msg += f" dropped_rows={dropped}"
        print(msg)


if __name__ == "__main__":
    main()
