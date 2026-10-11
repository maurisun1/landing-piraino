#!/usr/bin/env python3
"""Build /valutazione-casa-{slug}/ from seo/valutazione-template.json (Brescia first)."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "seo" / "valutazione-template.json").read_text(encoding="utf-8"))


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def build(city: dict) -> str:
    name = city["name"]
    slug = city["slug"]
    base = f"https://mauriziopiraino.it/valutazione-casa-{slug}/"
    title = city["title"]
    desc = city["description"]
    assert len(title) <= 70
    assert len(desc) <= 155, len(desc)

    faq = [
        (
            f"La valutazione casa a {name} è davvero gratuita?",
            "Sì: la prima analisi è gratuita e non crea obbligo di incarico. Se poi decidiamo di lavorare insieme, le condizioni si concordano per iscritto.",
        ),
        (
            f"Valutazione e perizia immobiliare a {name}: che differenza c’è?",
            "La valutazione operativa serve a posizionare l’immobile sul mercato. La perizia è un atto tecnico con valenza formale (es. mutui, successioni) e segue regole diverse.",
        ),
        (
            "Usate solo i valori OMI?",
            "No. L’OMI è un riferimento statistico. Lo affianco a listini, annunci, tempi di vendita e alle caratteristiche reali dell’immobile.",
        ),
        (
            f"Operate solo in città o anche in provincia di {name}?",
            f"Opero su {city['zones_label']}, direttamente e con la rete professionale quando serve.",
        ),
        (
            "Quanto tempo serve per una prima stima?",
            "Di solito entro 24–48 ore lavorative dal ricevimento dei dati essenziali (zona, tipologia, stato, eventuali documenti).",
        ),
    ]
    faq_entities = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for q, a in faq
    ]
    faq_html = "\n".join(
        f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faq
    )

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "@id": f"{base}#service",
                "name": f"Valutazione casa {name}",
                "serviceType": "Valutazione immobiliare",
                "provider": {"@id": "https://mauriziopiraino.it/#agent"},
                "areaServed": name,
                "url": base,
                "description": desc,
            },
            {
                "@type": "FAQPage",
                "@id": f"{base}#faq",
                "mainEntity": faq_entities,
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://mauriziopiraino.it/"},
                    {"@type": "ListItem", "position": 2, "name": f"Vendere a {name}", "item": f"https://mauriziopiraino.it{city['sell_url']}"},
                    {"@type": "ListItem", "position": 3, "name": f"Valutazione casa {name}", "item": base},
                ],
            },
            {
                "@type": ["Person", "RealEstateAgent"],
                "@id": "https://mauriziopiraino.it/#agent",
                "name": "Maurizio Piraino",
                "url": "https://mauriziopiraino.it/",
                "telephone": "+39-351-458-1993",
            },
        ],
    }

    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}" />
<meta name="robots" content="index, follow" />
<link rel="canonical" href="{base}" />
<link rel="alternate" hreflang="it" href="{base}" />
<link rel="alternate" hreflang="x-default" href="{base}" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{esc(title)}" />
<meta property="og:description" content="{esc(desc)}" />
<meta property="og:url" content="{base}" />
<meta property="og:image" content="https://mauriziopiraino.it{esc(city['hero_img'].split('?')[0])}" />
<meta property="og:locale" content="it_IT" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/assets/site-base.css?v=20260760" />
<link rel="stylesheet" href="/assets/remax-brand.css?v=20260760" />
<link rel="stylesheet" href="/assets/site-nav.css?v=20261009" />
<link rel="stylesheet" href="/assets/seller-landing.css?v=20260760" />
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip-link" href="#main">Vai al contenuto</a>
<div class="site-chrome">
<div class="topbar"><div class="container topbar-inner">
  <div class="topbar-tagline"><strong>Maurizio Piraino</strong> · Valutazione casa · {esc(name)}</div>
  <div class="topbar-actions">
    <a class="topbar-phone" href="tel:+393514581993">351 458 1993</a>
    <a class="topbar-wa topbar-wa-desktop" href="https://wa.me/393514581993?text=Buongiorno%2C%20vorrei%20una%20valutazione%20casa%20a%20{esc(name)}.">WhatsApp</a>
  </div>
</div></div>
<header class="site-header"><div class="container site-nav">
  <a class="brand" href="/"><span class="brand-name">Maurizio Piraino</span><span class="remax-nav-badge">RE/MAX</span></a>
  <div class="site-nav-actions">
    <a class="btn btn-wa nav-wa-compact" href="https://wa.me/393514581993?text=Buongiorno%2C%20vorrei%20una%20valutazione%20casa%20a%20{esc(name)}." aria-label="WhatsApp">WA</a>
    <button type="button" class="nav-toggle" aria-label="Apri menu" aria-expanded="false" aria-controls="site-nav-panel"><span class="nav-toggle-bar"></span><span class="nav-toggle-bar"></span><span class="nav-toggle-bar"></span></button>
  </div>
  <div class="nav-panel" id="site-nav-panel">
    <nav class="nav-links" aria-label="Menu principale">
      <div class="nav-group nav-group-path">
        <span class="nav-group-label">Percorso</span>
        <div class="nav-group-links">
          <a href="/comprare-casa/" class="nav-link-core">Comprare</a>
          <a href="{esc(city['sell_url'])}" class="nav-link-primary nav-link-core">Vendere</a>
          <span class="nav-path-sep" aria-hidden="true"></span>
          <a href="/immobili-commerciali/" class="nav-link-soft">Commerciali</a>
          <a href="/sviluppo-immobiliare/" class="nav-link-soft">Sviluppo</a>
        </div>
      </div>
      <a class="btn btn-red nav-cta" href="#contatto">Richiedi valutazione</a>
    </nav>
  </div>
  <div class="nav-backdrop" hidden></div>
</div></header>
<div class="remax-stripe" aria-hidden="true"></div>
</div>

<main id="main">
<section class="hero seller-form-section" id="contatto" style="--seller-city-bg: url('{esc(city['hero_img'])}');">
  <div class="container seller-form-layout">
    <div class="seller-form-aside reveal">
      <p class="eyebrow">Valutazione immobiliare · {esc(name)}</p>
      <h1>{esc(city['h1'])}</h1>
      <p class="lead">Non una cifra a caso: una stima utile per decidere se vendere, a che prezzo riposizionarti e quali passi fare prima di pubblicare l&apos;annuncio.</p>
      <ul class="hero-bullets">
        <li>Analisi di zona, OMI e mercato reale</li>
        <li>Lettura dei limiti di listini e annunci</li>
        <li>Nessun obbligo di incarico al primo contatto</li>
      </ul>
    </div>
    <form class="form-card seller-form-card reveal" action="https://formspree.io/f/mvzlgeqb" method="POST" id="leadForm">
      <input type="hidden" name="_subject" value="Valutazione casa {esc(name)}" />
      <input type="hidden" name="lead_type" value="valutazione" />
      <input type="hidden" name="landing" value="/valutazione-casa-{esc(slug)}/" />
      <h2>Richiedi una stima gratuita</h2>
      <p class="form-note">Risposta entro 24–48 ore lavorative.</p>
      <div class="field"><label for="nome">Nome *</label><input id="nome" name="nome" required autocomplete="name" /></div>
      <div class="field"><label for="telefono">Telefono *</label><input id="telefono" name="telefono" type="tel" required autocomplete="tel" /></div>
      <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" /></div>
      <div class="field"><label for="zona">Zona / comune *</label><input id="zona" name="zona" required placeholder="Es. Brescia, Franciacorta, Desenzano…" /></div>
      <div class="field"><label for="tipologia">Tipologia</label>
        <select id="tipologia" name="tipologia">
          <option value="">Seleziona</option>
          <option>Appartamento</option>
          <option>Villa / villetta</option>
          <option>Attico</option>
          <option>Altro</option>
        </select>
      </div>
      <div class="field"><label for="messaggio">Messaggio</label><textarea id="messaggio" name="messaggio" placeholder="Superficie, piano, stato, eventuali documenti"></textarea></div>
      <label class="check"><input type="checkbox" name="privacy" value="si" required /> Ho letto l&apos;<a href="/privacy/">informativa privacy</a>.</label>
      <button type="submit" class="btn btn-red">Invia richiesta</button>
    </form>
  </div>
</section>

<section class="seller-services">
  <div class="container" style="max-width:820px">
    <h2>Come facciamo la valutazione</h2>
    <p>La <strong>valutazione casa a {esc(name)}</strong> parte dai dati dell&apos;immobile e della micro-zona, non da una media provinciale. Raccolgo informazioni su superficie commerciale e calpestabile, piano, stato manutentivo, classe energetica, esposizione, vista, box o posto auto, spese condominiali e contesto urbano; poi confronto il posizionamento con i riferimenti OMI, con i listini disponibili e con ciò che il mercato sta davvero assorbendo in quel momento.</p>
    <p>L&apos;obiettivo non è &quot;dire un numero alto per prendere l&apos;incarico&quot;. L&apos;obiettivo è darti una stima difendibile: abbastanza ambiziosa da non regalare valore, abbastanza realistica da generare visite e trattative. A {esc(name)} questo equilibrio cambia tra città, Franciacorta e laghi: per questo la lettura è locale e non si riduce a un moltiplicatore generico al metro quadro.</p>
    <p>Il metodo è sequenziale. Prima inquadro la domanda e l&apos;offerta nella micro-zona. Poi leggo i limiti delle fonti pubbliche. Infine correggo per le caratteristiche del singolo immobile: un piano alto luminoso con documenti in ordine non si valuta come un piano basso umido con pratiche incomplete, anche se la fascia OMI è la stessa.</p>
    <p>Quando serve, affianco la stima a indicazioni pratiche: cosa migliorare prima di pubblicare, quali documenti preparare, come impostare prezzo e strategia di uscita, se conviene partire più alti o più contenuti. È una valutazione al servizio della decisione, non un esercizio teorico. Se i dati che mi mandi sono incompleti, ti dico subito cosa manca invece di inventare precisione.</p>
  </div>
</section>

<section class="seller-services" style="background:#f5f7fa">
  <div class="container" style="max-width:820px">
    <h2>Valutazione vs perizia immobiliare a {esc(name)}</h2>
    <p>Molti proprietari cercano online &quot;perizia immobiliare {esc(name)}&quot; intendendo in realtà una stima di mercato. Conviene distinguere con chiarezza, perché strumenti diversi rispondono a scopi diversi:</p>
    <ul>
      <li><strong>Valutazione / stima di mercato:</strong> serve a vendere o a capire il valore di scambio. È operativa, commerciale, orientata a prezzo, tempi e platea di acquirenti reali.</li>
      <li><strong>Perizia:</strong> è un elaborato tecnico con finalità formali (mutuo, successione, contenzioso, divisione). Ha regole, responsabilità professionali e costi diversi.</li>
    </ul>
    <p>Su questa pagina offro una <strong>valutazione gratuita</strong> di orientamento commerciale. Non è una perizia ai sensi della normativa sulle stime formali e non sostituisce il lavoro di un perito iscritto quando ti serve un atto tecnico. Se ti serve una perizia formale, ti indico il percorso corretto con professionisti abilitati.</p>
    <p>Questa distinzione evita due errori tipici: aspettarsi da una stima commerciale lo stesso valore legale di una perizia, oppure pagare una perizia quando ti serve solo capire a che prezzo puoi uscire sul mercato di {esc(name)}. Partire dal bisogno reale (vendere, rinegoziare, confrontare offerte) fa risparmiare tempo e riduce fraintendimenti.</p>
  </div>
</section>

<section class="seller-services">
  <div class="container" style="max-width:820px">
    <h2>Listino Borsa Immobiliare e OMI: limiti</h2>
    <p>Per una <strong>valutazione immobili {esc(name)}</strong> uso più fonti, ma conosco i limiti di ciascuna. Nessuna tabella, da sola, &quot;vale&quot; la tua casa:</p>
    <ul>
      <li><strong>OMI:</strong> fasce statistiche pubbliche per zona e tipologia. Utili, aggiornate periodicamente, ma non descrivono il singolo appartamento né lo stato di manutenzione.</li>
      <li><strong>Listini / Borsa Immobiliare:</strong> riferimenti di mercato locale con metodologie proprie. Sono un secondo sguardo, non una verità assoluta sul prezzo di chiusura.</li>
      <li><strong>Annunci online:</strong> prezzi richiesti, spesso sopra il prezzo finale. Guardarli senza correzioni porta a sovrastime e a immobilizzarsi sul mercato.</li>
    </ul>
    <p>Il <strong>listino immobiliare {esc(name)}</strong> e i valori OMI aiutano a inquadrare la zona; la stima seria nasce quando questi numeri incontrano lo stato reale dell&apos;immobile, la domanda e i tempi di vendita osservati. Due immobili nella stessa fascia possono avere esiti molto diversi se cambiano piano, esposizione, classe energetica o completezza documentale.</p>
    <p>Per approfondire le fasce OMI puoi leggere anche la <a href="{esc(city['guide_url'])}">guida valori OMI {esc(name)}</a>. Lì trovi il contesto statistico; qui trasformiamo quel contesto in una lettura utile per decidere se e come vendere.</p>
  </div>
</section>

<section class="seller-services" style="background:#f5f7fa">
  <div class="container" style="max-width:820px">
    <h2>Quanto costa la valutazione</h2>
    <p><strong>La prima valutazione è gratuita.</strong> Nessun costo nascosto per il primo confronto. La consulenza iniziale non costituisce obbligo di conferimento incarico: decidi dopo aver capito il quadro, senza pressione commerciale sul primo contatto.</p>
    <p>Se poi scegli di affidarmi la vendita, le condizioni economiche si concordano in modo trasparente e per iscritto, come previsto dall&apos;attività di mediazione. Niente sorprese sul primo contatto e nessuna &quot;stima omaggio&quot; legata a un incarico già deciso in anticipo.</p>
    <p>Gratis non significa superficiale: significa che il primo lavoro di lettura (zona, tipologia, stato, fonti di mercato) è incluso nella consulenza iniziale. Se i documenti o i dati sono incompleti, ti dico cosa serve per raffinare la stima invece di inventare un numero definitivo.</p>
  </div>
</section>

<section class="seller-services">
  <div class="container" style="max-width:820px">
    <h2>Zone di {esc(name)} e provincia</h2>
    <p>Il mercato non è uniforme. Una valutazione a {esc(name)} cambia se l&apos;immobile è in città, in Franciacorta, sul Garda o verso Iseo. Per questo la parola &quot;Brescia&quot; da sola non basta: serve la micro-zona e, spesso, il comune preciso.</p>
    <ul>
      <li><strong>Brescia città:</strong> micro-zone diverse per servizi, collegamenti e stock abitativo. Centro, quartieri consolidati e aree in trasformazione non si muovono allo stesso ritmo.</li>
      <li><strong>Franciacorta:</strong> domanda spesso legata a qualità abitativa e contesto; prezzi e tempi non seguono automaticamente il centro città. Ville, cascine e residenziale moderno richiedono letture distinte.</li>
      <li><strong>Lago di Garda:</strong> forte componente lifestyle e, in alcuni comuni, seconda casa; la stagionalità, la vista e la tipologia pesano di più che in città.</li>
      <li><strong>Lago d&apos;Iseo:</strong> mercato più contenuto, da leggere comune per comune, senza copiare le dinamiche del Garda o della città.</li>
    </ul>
    <p>Quando chiedo la zona non è formalità: è il punto di partenza della stima. Senza micro-zona, ogni media è poco utile. Se hai un immobile in provincia, indica anche accessibilità, servizi e tipologia: spesso pesano quanto il nome del comune.</p>
  </div>
</section>

<section class="seller-services" style="background:#f5f7fa">
  <div class="container" style="max-width:820px">
    <h2>Come scegliere il consulente giusto a {esc(name)}</h2>
    <p>Per una valutazione seria cerca qualcuno che non si limita a ripetere una media da portale. In pratica:</p>
    <ul>
      <li>distingue OMI, listini e prezzi reali di chiusura;</li>
      <li>ti spiega il metodo, non solo il numero finale;</li>
      <li>non promette miracoli di prezzo senza evidenze di mercato;</li>
      <li>opera in trasparenza su costi e incarico;</li>
      <li>conosce il territorio (città e provincia), non solo i portali;</li>
      <li>ti dice anche quando conviene non vendere subito, se i documenti o lo stato non sono pronti.</li>
    </ul>
    <p>Io lavoro come agente immobiliare affiliato RE/MAX, con base operativa in Lombardia. Su {esc(name)} affianco i proprietari con analisi riservata e, se ha senso, con la strategia di vendita completa: prezzo, presentazione, canali e gestione delle trattative. Puoi anche partire dall&apos;<a href="{esc(city['sell_url'])}">area venditori {esc(name)}</a> o dalla pagina per <a href="{esc(city['buy_url'])}">chi compra a {esc(name)}</a>.</p>
    <p>Se stai confrontando più consulenti, porta gli stessi dati a tutti (zona, metri, piano, stato, eventuali lavori) e confronta la qualità delle spiegazioni, non solo il numero più alto. Il prezzo più alto promesso senza metodo è spesso il primo passo verso mesi di invenduto.</p>
  </div>
</section>

<section class="seller-services">
  <div class="container" style="max-width:820px">
    <h2>FAQ — Valutazione casa {esc(name)}</h2>
    {faq_html}
  </div>
</section>

<section class="seller-services" style="background:#0f1c2e;color:#fff">
  <div class="container" style="max-width:720px;text-align:center">
    <h2 style="color:#fff">Richiedi la tua valutazione gratuita</h2>
    <p style="color:rgba(255,255,255,.88)">Raccontami zona, tipologia e stato dell&apos;immobile: ti do una prima lettura utile per decidere.</p>
    <p><a class="btn btn-red" href="#contatto">Torna al form</a>
    <a class="btn" style="margin-left:10px;border:1px solid rgba(255,255,255,.4);color:#fff" href="https://wa.me/393514581993?text=Buongiorno%2C%20vorrei%20una%20valutazione%20casa%20a%20{esc(name)}.">WhatsApp</a></p>
  </div>
</section>
</main>

<footer class="footer"><div class="container footer-inner">
  <div>
    <strong>Maurizio Piraino</strong>
    <div class="footer-affiliation">Agente immobiliare affiliato RE/MAX Associati Real Estate · Milano</div>
    <div>REA BS-639579 · P.IVA 14597560961<br><small>La consulenza iniziale non costituisce obbligo di conferimento incarico. Analisi commerciali, non perizie.</small></div>
  </div>
  <div class="footer-links">
    <a href="{esc(city['sell_url'])}">Vendere a {esc(name)}</a>
    <a href="{esc(city['guide_url'])}">Valori OMI {esc(name)}</a>
    <a href="{esc(city['buy_url'])}">Comprare a {esc(name)}</a>
    <a href="/">Home</a>
    <a href="/privacy/">Privacy</a>
  </div>
</div></footer>
<script src="/assets/site-nav.js?v=20261009" defer></script>
<script src="/assets/analytics.js?v=20261002i" defer></script>
</body>
</html>
"""


def main() -> None:
    for city in DATA["cities"]:
        html_out = build(city)
        words = len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", html_out), flags=re.UNICODE))
        out = ROOT / f"valutazione-casa-{city['slug']}" / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html_out, encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)} words~{words} desc_len={len(city['description'])}")


if __name__ == "__main__":
    main()
