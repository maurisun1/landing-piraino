#!/usr/bin/env python3
"""Anti-cannibalizzazione SEO: guide OMI su MP → sintesi + canonical VCT."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VCT = "https://valorecasatua.it"

# MP path slug → VCT guide path segment (after /guide/prezzi-mq-)
VCT_OMI = {
    "milano": f"{VCT}/guide/prezzi-mq-milano/",
    "brescia": f"{VCT}/guide/prezzi-mq-brescia/",
    "bergamo": f"{VCT}/guide/prezzi-mq-bergamo/",
    "como": f"{VCT}/guide/prezzi-mq-como/",
    "monza": f"{VCT}/guide/prezzi-mq-monza-brianza/",
    "varese": f"{VCT}/guide/prezzi-mq-varese/",
    "lecco": f"{VCT}/guide/prezzi-mq-lecco/",
    "lodi": f"{VCT}/guide/prezzi-mq-lodi/",
    "mantova": f"{VCT}/guide/prezzi-mq-mantova/",
    "pavia": f"{VCT}/guide/prezzi-mq-pavia/",
    "sondrio": f"{VCT}/guide/prezzi-mq-sondrio/",
    "cremona": f"{VCT}/guide/prezzi-mq-cremona/",
}

# Display names
CITY = {
    "milano": "Milano",
    "brescia": "Brescia",
    "bergamo": "Bergamo",
    "como": "Como",
    "monza": "Monza e Brianza",
    "varese": "Varese",
    "lecco": "Lecco",
    "lodi": "Lodi",
    "mantova": "Mantova",
    "pavia": "Pavia",
    "sondrio": "Sondrio",
    "cremona": "Cremona",
}

# Key figures kept in the MP summary (not full zone tables)
KEY_STATS = {
    "milano": {
        "range": "circa 1.850–16.000 €/mq (abitazioni civili)",
        "center": "zone centrali (es. Brera) fino a ~16.000 €/mq",
        "suburb": "zone suburbane da ~1.850 €/mq",
        "note": "abitazioni signorili in centro possono superare i 20.000 €/mq",
        "seller_cta": "/vendere-casa-milano/",
        "buyer_cta": "/comprare-casa-milano/",
        "image": "/milano.jpg",
    },
    "brescia": {
        "range": "circa 1.250–4.300 €/mq (abitazioni civili)",
        "center": "zone centrali fino a ~4.300 €/mq",
        "suburb": "zone periferiche/suburbane da ~1.250 €/mq",
        "note": "il prezzo reale dipende da piano, stato e micro-zona",
        "seller_cta": "/brescia/",
        "buyer_cta": "/comprare-casa-brescia/",
        "image": "/brescia.jpg",
    },
    "bergamo": {
        "range": "circa 1.400–4.300 €/mq (abitazioni civili)",
        "center": "zone centrali fino a ~4.300 €/mq",
        "suburb": "zone periferiche da ~1.400 €/mq",
        "note": "Città Alta e semicentro hanno dinamiche diverse dal resto della provincia",
        "seller_cta": "/bergamo/",
        "buyer_cta": "/comprare-casa-bergamo/",
        "image": "/bergamo.jpg",
    },
}

GUIDE_CSS = """
  :root{--black:#070707;--cream:#f6f1e9;--warm:#eee3d5;--text:#222;--muted:#707070;--red:#dc1c2e;--red-dark:#b01828;--gold:#003da5;--line:rgba(0,0,0,.10);}
  *{margin:0;padding:0;box-sizing:border-box;}
  body{font-family:'Inter',sans-serif;background:var(--cream);color:var(--text);line-height:1.65;-webkit-font-smoothing:antialiased;}
  .serif{font-family:'Playfair Display',serif;}
  .wrap{max-width:760px;margin:0 auto;padding:0 22px;}
  .eyebrow{color:var(--gold);font-size:12px;font-weight:600;letter-spacing:1.4px;text-transform:uppercase;margin-bottom:14px;}
  h1{font-size:clamp(28px,5vw,42px);line-height:1.15;font-weight:700;color:var(--black);}
  .date{display:flex;align-items:center;gap:7px;color:var(--muted);font-size:14px;margin-top:14px;}
  .lead{font-size:18px;line-height:1.6;margin:26px 0;}
  .lead strong{font-weight:600;}
  section{margin:40px 0;}
  h2{font-family:'Playfair Display',serif;font-size:26px;font-weight:600;color:var(--black);margin-bottom:14px;}
  p{margin:0 0 16px;font-size:16px;color:#333;}
  .key-list{list-style:none;margin:18px 0 28px;padding:0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);}
  .key-list li{padding:12px 0;border-bottom:1px solid var(--line);font-size:15px;}
  .key-list li:last-child{border-bottom:none;}
  .key-list strong{color:var(--black);}
  .vct-box{background:#fff;border:2px solid var(--gold);border-radius:14px;padding:28px 24px;margin:36px 0;text-align:center;}
  .vct-box p{margin:0 0 16px;font-size:17px;color:var(--black);}
  .vct-box a.vct-cta{display:inline-block;background:var(--gold);color:#fff;text-decoration:none;font-weight:700;font-size:15px;padding:14px 28px;border-radius:10px;}
  .vct-box .vct-note{margin-top:14px;font-size:13px;color:var(--muted);}
  .cta{background:var(--black);border-radius:18px;padding:40px 30px;text-align:center;margin:48px 0;}
  .cta p{color:var(--cream);font-size:20px;font-family:'Playfair Display',serif;margin-bottom:22px;}
  .cta a{display:inline-block;background:var(--red);color:#fff;text-decoration:none;font-weight:600;font-size:16px;padding:15px 34px;border-radius:10px;}
  .links{display:flex;flex-wrap:wrap;gap:10px;margin:30px 0;}
  .links a{font-size:14px;color:var(--red-dark);text-decoration:none;border:1px solid var(--line);padding:9px 16px;border-radius:8px;}
  footer{background:var(--warm);padding:30px 0;margin-top:50px;font-size:12.5px;color:var(--muted);line-height:1.6;}
  footer strong{color:var(--text);}
  .disc{font-size:11.5px;margin-top:14px;opacity:.85;}
  .roles{font-size:14px;color:var(--muted);margin:8px 0 0;}
"""


def extract_chrome(html: str) -> str:
    # site-chrome wraps topbar + header + remax-stripe, then closes before <main>
    m = re.search(
        r'(<div class="site-chrome">.*?<div class="remax-stripe"[^>]*>\s*</div>\s*</div>)',
        html,
        re.DOTALL,
    )
    if not m:
        raise RuntimeError("site-chrome not found")
    return m.group(1)


def rewrite_guide(slug: str) -> None:
    path = ROOT / f"guida-prezzi-mq-{slug}" / "index.html"
    old = path.read_text(encoding="utf-8")
    chrome = extract_chrome(old)
    # Soften topbar / WA copy away from "guida OMI completa"
    chrome = chrome.replace(
        f"Guida prezzi OMI · <strong>{CITY[slug]}</strong> · Dati Agenzia Entrate",
        f"Sintesi OMI · <strong>{CITY[slug]}</strong> · Consulenza RE/MAX",
    )
    chrome = re.sub(
        r"vorrei%20informazioni%20sui%20prezzi%20OMI%20a%20[^.\"]+",
        f"vorrei%20una%20consulenza%20su%20{CITY[slug].replace(' ', '%20')}%20e%20i%20valori%20di%20zona",
        chrome,
    )

    stats = KEY_STATS[slug]
    vct_url = VCT_OMI[slug]
    city = CITY[slug]
    mp_url = f"https://mauriziopiraino.it/guida-prezzi-mq-{slug}/"
    title = f"Valori OMI {city}: sintesi e consulenza acquisto | Maurizio Piraino"
    desc = (
        f"Sintesi dei valori OMI a {city} ({stats['range']}). "
        f"Per la guida completa zona per zona vai su ValoreCasaTua.it; "
        f"qui consulenza RE/MAX per comprare o vendere."
    )

    schema = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "WebPage",
      "@id": "{mp_url}#webpage",
      "url": "{mp_url}",
      "name": "{title}",
      "description": "{desc}",
      "inLanguage": "it-IT",
      "isPartOf": {{"@type": "WebSite", "url": "https://mauriziopiraino.it/"}},
      "about": {{
        "@type": "Thing",
        "name": "Valori OMI e consulenza immobiliare a {city}"
      }},
      "mainEntity": {{"@id": "https://mauriziopiraino.it/#agent"}}
    }},
    {{
      "@type": ["Person", "RealEstateAgent"],
      "@id": "https://mauriziopiraino.it/#agent",
      "name": "Maurizio Piraino",
      "jobTitle": "Agente Immobiliare affiliato RE/MAX",
      "identifier": "REA BS-639579",
      "url": "https://mauriziopiraino.it/",
      "telephone": "+39 351 458 1993",
      "areaServed": ["Milano", "Lombardia", "{city}"]
    }}
  ]
}}
</script>"""

    related = []
    for other in ("milano", "bergamo", "brescia"):
        if other == slug:
            related.append(f"<strong>{CITY[other]}</strong>")
        else:
            related.append(
                f'<a href="{VCT_OMI[other]}">Prezzi al mq {CITY[other]} (ValoreCasaTua)</a>'
            )

    body = f"""<!DOCTYPE html>
<html lang="it">
<head>
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="apple-touch-icon" href="/favicon.svg" />
  <meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="robots" content="index, follow" />
<link rel="canonical" href="{vct_url}" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:url" content="{vct_url}" />
<meta property="og:image" content="https://mauriziopiraino.it{stats['image']}" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
{schema}
<style>
{GUIDE_CSS}
</style>
<link rel="stylesheet" href="/assets/site-base.css?v=20260735" />
  <link rel="stylesheet" href="/assets/remax-brand.css?v=20260735" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="stylesheet" href="/assets/site-nav.css?v=20260736" />
</head>
<body>
  <a class="skip-link" href="#main">Salta al contenuto</a>
{chrome}
<main class="wrap" id="main">
  <section style="margin-top:46px;">
    <div class="eyebrow">Sintesi · {city} · Consulenza RE/MAX</div>
    <h1 class="serif">Valori OMI a {city}: come leggerli prima di comprare (o investire)</h1>
    <div class="date">Riferimento OMI 2&deg; semestre 2025 · guida completa su ValoreCasaTua.it</div>
    <p class="lead">I valori OMI dell&apos;Agenzia delle Entrate sono il punto di partenza per orientarsi sul mercato di <strong>{city}</strong>: fascia statistica di zona, non quotazione del singolo immobile. Su questo sito trovi una sintesi operativa e la consulenza RE/MAX; le tabelle zona per zona e l&apos;approfondimento editoriale vivono su <strong>ValoreCasaTua.it</strong>.</p>
    <p class="roles">ValoreCasaTua = portale editoriale · Maurizio Piraino = consulenza professionale (property finding, acquirenti/investitori, vendita).</p>
  </section>

  <section>
    <h2 class="serif">Numeri chiave (sintesi)</h2>
    <p>Secondo gli ultimi dati OMI pubblicati, le abitazioni civili a {city} si collocano in una fascia indicativa di <strong>{stats['range']}</strong>. Tre riferimenti utili prima di un sopralluogo o di un&apos;offerta:</p>
    <ul class="key-list">
      <li><strong>Fascia complessiva:</strong> {stats['range']}</li>
      <li><strong>Fascia alta:</strong> {stats['center']}</li>
      <li><strong>Fascia bassa:</strong> {stats['suburb']}</li>
      <li><strong>Attenzione:</strong> {stats['note']}</li>
      <li><strong>Scostamento tipico:</strong> il prezzo di trattativa può discostarsi anche del 15–20% rispetto alla fascia OMI (piano, stato, affaccio, documenti, domanda della micro-zona).</li>
    </ul>
    <p>Se stai comprando o investendo, uso questi dati insieme a compravendite recenti e verifica tecnica: così eviti di pagare un premium non giustificato o di basare l&apos;offerta su un annuncio fuori mercato.</p>
  </section>

  <div class="vct-box">
    <p><strong>Guida completa OMI {city} 2026</strong> (quotazioni per zona) su ValoreCasaTua.it</p>
    <a class="vct-cta" href="{vct_url}">Apri la guida completa su ValoreCasaTua.it →</a>
    <p class="vct-note">Link dofollow alla fonte editoriale master · nessuna tabella zona-per-zona duplicata su questo sito</p>
  </div>

  <section>
    <h2 class="serif">Cosa faccio io su MaurizioPiraino.it</h2>
    <p>Dopo aver letto i valori di zona, il passo successivo è decidere se quell&apos;immobile conviene per i tuoi obiettivi. Ti affianco su analisi di micro-zona, strategia di prezzo, property finding e percorso di acquisto o vendita con RE/MAX — senza obbligarti a un incarico al primo contatto.</p>
  </section>

  <div class="cta">
    <p>Vuoi una lettura dei valori OMI applicata al tuo caso?</p>
    <a href="{stats['seller_cta'] if slug != 'milano' else '/#form'}">Richiedi consulenza WhatsApp / form</a>
  </div>

  <div class="links">
    <a href="{stats['buyer_cta']}">Comprare casa a {city}</a>
    <a href="{stats['seller_cta']}">Vendere a {city}</a>
    <a href="{VCT}/guide/">Indice guide ValoreCasaTua</a>
  </div>
</main>

<aside class="guide-cta-links" aria-label="Passaggi successivi"><p>Hai un immobile a {city}? <a href="{stats['seller_cta']}">Richiedi analisi di vendita</a> · <a href="{stats['buyer_cta']}">Consulenza per chi compra</a></p></aside>
<nav class="guide-related" aria-label="Guide prezzi OMI su ValoreCasaTua"><p><span>Guide complete Lombardia (ValoreCasaTua):</span> {' · '.join(related)}</p></nav>
<footer><div class="wrap">
  <strong>Maurizio Piraino</strong> <br>
  <div class="footer-affiliation">Maurizio Piraino — Consulente immobiliare presso RE/MAX Associati Real Estate · Milano, Viale Gran Sasso 31</div>
  &middot; Agente Immobiliare affiliato RE/MAX &middot; REA BS-639579
  <div class="disc">I valori OMI sono riferimenti statistici dell&apos;Agenzia delle Entrate e non costituiscono stima o valutazione ai sensi della L. 39/1989. La guida completa zona per zona è su <a href="{vct_url}">ValoreCasaTua.it</a>.</div>
</div></footer>
  <script src="/assets/site-nav.js?v=20260736" defer></script>
</body>
</html>
"""
    path.write_text(body, encoding="utf-8")
    print(f"Rewrote {path.relative_to(ROOT)}")


def retarget_omi_links() -> int:
    """Point MP guida-prezzi and 'Consulta OMI' links to VCT."""
    changed = 0
    html_files = list(ROOT.rglob("*.html"))
    # Skip nothing in guides themselves for related — already rewritten

    replacements = [
        ("/guida-prezzi-mq-milano/", VCT_OMI["milano"]),
        ("/guida-prezzi-mq-brescia/", VCT_OMI["brescia"]),
        ("/guida-prezzi-mq-bergamo/", VCT_OMI["bergamo"]),
        ("https://mauriziopiraino.it/guida-prezzi-mq-milano/", VCT_OMI["milano"]),
        ("https://mauriziopiraino.it/guida-prezzi-mq-brescia/", VCT_OMI["brescia"]),
        ("https://mauriziopiraino.it/guida-prezzi-mq-bergamo/", VCT_OMI["bergamo"]),
    ]

    # Seller / buyer "Consulta i valori OMI" → VCT per province
    zone_link_re = re.compile(
        r'(<p class="seller-zones-link"><a href=")([^"]+)(">)(Consulta i valori OMI[^<]*)(</a></p>)'
    )
    # Also plain centered OMI links and buyer-omi on MI/BS/BG
    consult_re = re.compile(
        r'(<a href=")(/guida-prezzi-mq-(?:milano|brescia|bergamo)/|/comprare-casa-(?:milano|brescia|bergamo|como|varese|lecco|sondrio|cremona|lodi|mantova|pavia|monza)/)("(?:[^>]*)>)(Consulta i valori OMI[^<]*)(</a>)'
    )

    slug_from_href = {
        "/guida-prezzi-mq-milano/": "milano",
        "/guida-prezzi-mq-brescia/": "brescia",
        "/guida-prezzi-mq-bergamo/": "bergamo",
        **{f"/comprare-casa-{s}/": s for s in VCT_OMI},
    }

    for path in html_files:
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        orig = text

        # Don't rewrite absolute self-URLs inside the guide pages' alternate hreflang
        # (canonical already set to VCT). Still replace internal relative guida links.
        for old, new in replacements:
            # Keep hreflang pointing at MP URL for the guide pages themselves
            if path.parent.name.startswith("guida-prezzi-mq-") and "mauriziopiraino.it/guida-prezzi" in old:
                continue
            text = text.replace(f'href="{old}"', f'href="{new}"')

        def zone_sub(m: re.Match[str]) -> str:
            href = m.group(2)
            slug = slug_from_href.get(href)
            if not slug:
                # Try infer from label city
                label = m.group(4)
                for s, name in CITY.items():
                    if name in label or s.capitalize() in label or (s == "monza" and "Monza" in label):
                        slug = s
                        break
            if not slug:
                return m.group(0)
            return f'{m.group(1)}{VCT_OMI[slug]}{m.group(3)}{m.group(4)}{m.group(5)}'

        text = zone_link_re.sub(zone_sub, text)
        text = consult_re.sub(zone_sub, text)

        # Homepage / hub mesh: expand OMI guide row to all provinces on VCT (IT home + buyer hub)
        if path.name == "index.html" or path.parent.name in ("comprare-casa", "vendere-casa"):
            mesh_omi = " · ".join(
                f'<a href="{VCT_OMI[s]}">{CITY[s]}</a>'
                for s in (
                    "milano",
                    "monza",
                    "bergamo",
                    "brescia",
                    "como",
                    "varese",
                    "lecco",
                    "sondrio",
                    "cremona",
                    "lodi",
                    "mantova",
                    "pavia",
                )
            )
            text = re.sub(
                r'(<p class="seo-home-mesh-label">Guide prezzi al mq \(OMI\)</p><p class="seo-home-mesh-links">)(.*?)(</p>)',
                rf"\1{mesh_omi}\3",
                text,
                count=1,
            )
            text = re.sub(
                r'(<p class="seo-mesh-guides">Guide prezzi OMI:\s*)(.*?)(</p>)',
                rf'\1{mesh_omi}\3',
                text,
                count=1,
            )

        # Footer geo OMI row → all VCT
        footer_omi = " &middot; ".join(
            f'<a href="{VCT_OMI[s]}">{CITY[s]}</a>'
            for s in (
                "milano",
                "monza",
                "bergamo",
                "brescia",
                "como",
                "varese",
                "lecco",
                "sondrio",
                "cremona",
                "lodi",
                "mantova",
                "pavia",
            )
        )
        text = re.sub(
            r'(<p class="footer-geo-row"><span class="footer-geo-label">Guide prezzi OMI:</span> )(.*?)(</p>)',
            rf"\1{footer_omi}\3",
            text,
        )

        # Related nav on other pages that still list MP guides
        text = re.sub(
            r'<a href="https://valorecasatua\.it/guide/prezzi-mq-milano/">Prezzi al mq OMI — Milano</a>',
            f'<a href="{VCT_OMI["milano"]}">Prezzi al mq OMI — Milano (ValoreCasaTua)</a>',
            text,
        )

        if text != orig:
            path.write_text(text, encoding="utf-8")
            changed += 1
            print(f"Retargeted links in {path.relative_to(ROOT)}")
    return changed


def patch_seller_footer_geo_script() -> None:
    path = ROOT / ".github" / "scripts" / "seller_footer_geo.py"
    text = path.read_text(encoding="utf-8")
    new_omi = "OMI_HREF = {\n"
    for slug in (
        "milano",
        "monza",
        "bergamo",
        "brescia",
        "como",
        "varese",
        "lecco",
        "sondrio",
        "cremona",
        "lodi",
        "mantova",
        "pavia",
    ):
        new_omi += f'    "{slug}": "{VCT_OMI[slug]}",\n'
    new_omi += "}\n"
    text2 = re.sub(
        r"OMI_HREF = \{.*?\n\}\n",
        new_omi,
        text,
        count=1,
        flags=re.DOTALL,
    )
    # Also change fallback that used comprare-casa
    text2 = text2.replace(
        'omi.append(link(name, f"/comprare-casa-{slug}/"))',
        'omi.append(link(name, OMI_HREF.get(slug, f"{VCT}/guide/")))',
    )
    # Need VCT constant if we use it — actually all slugs are in OMI_HREF now
    text2 = text2.replace(
        'omi.append(link(name, OMI_HREF.get(slug, f"{VCT}/guide/")))',
        'omi.append(link(name, OMI_HREF[slug]))',
    )
    # Simplify loop: always use OMI_HREF
    text2 = re.sub(
        r"    omi = \[\]\n    for slug, name in PROVINCES:\n        if slug in OMI_HREF:\n            omi\.append\(link\(name, OMI_HREF\[slug\]\)\)\n        else:\n            omi\.append\(link\(name, OMI_HREF\[slug\]\)\)\n",
        "    omi = []\n    for slug, name in PROVINCES:\n        omi.append(link(name, OMI_HREF[slug]))\n",
        text2,
    )
    if text2 != text:
        path.write_text(text2, encoding="utf-8")
        print("Updated seller_footer_geo.py OMI_HREF → VCT")


def write_inventory() -> None:
    rows = [
        ("https://mauriziopiraino.it/guida-prezzi-mq-milano/", "Prezzi/OMI Milano (guida lunga → sintesi)", VCT_OMI["milano"]),
        ("https://mauriziopiraino.it/guida-prezzi-mq-brescia/", "Prezzi/OMI Brescia (guida lunga → sintesi)", VCT_OMI["brescia"]),
        ("https://mauriziopiraino.it/guida-prezzi-mq-bergamo/", "Prezzi/OMI Bergamo (guida lunga → sintesi)", VCT_OMI["bergamo"]),
    ]
    # Mentions / deep links only (not duplicate guides)
    for slug, name in CITY.items():
        if slug in ("milano", "brescia", "bergamo"):
            continue
        rows.append(
            (
                f"https://mauriziopiraino.it/comprare-casa-{slug}/ + /{slug}/ (link OMI)",
                f"Link/CTA OMI {name} (nessuna tabella duplicata)",
                VCT_OMI[slug],
            )
        )
    rows.append(
        (
            "https://mauriziopiraino.it/ (mesh + footer Guide OMI)",
            "Hub homepage — link OMI",
            f"{VCT}/guide/",
        )
    )
    rows.append(
        (
            "Guide situazioni (plusvalenza, mutuo, donazione, eredità, APE, ristrutturare, verifica)",
            "Non presenti come URL dedicate su MP (solo menzioni in buyer/seller)",
            "N/A — nessuna azione",
        )
    )
    rows.append(
        (
            "Mercato / report OMI Lombardia",
            "Non presenti come URL dedicate su MP",
            f"{VCT}/mercato-immobiliare-lombardia-2026/ · {VCT}/report-omi-lombardia-2026/",
        )
    )

    lines = [
        "# Fase 0 — Inventario anti-cannibalizzazione (22 settembre 2026)",
        "",
        "Sito MP: https://mauriziopiraino.it · Master VCT: https://valorecasatua.it",
        "",
        "| URL MP | Tema | URL VCT destinazione |",
        "| --- | --- | --- |",
    ]
    for mp, tema, vct in rows:
        lines.append(f"| {mp} | {tema} | {vct} |")
    lines += [
        "",
        "## Duplicate veri (contenuto da ridurre)",
        "- Solo 3 URL con tabelle OMI zona-per-zona + FAQPage/Article/Dataset: Milano, Brescia, Bergamo.",
        "- Nessuna pagina situazione (plusvalenza, mutuo, …) duplicata come URL standalone su MP.",
        "",
        "## Da lasciare intatto",
        "- Home servizi, property finding, investitori, contatti, chi sono, lead form, trust RE/MAX, buyer/seller province (servizi).",
    ]
    out = ROOT / "docs" / "anti-cannibal-vct-inventory.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)}")


def write_before_after() -> None:
    lines = [
        "# Checklist before/after — Anti-cannibalizzazione VCT (22 set 2026)",
        "",
        "## Guide riscritte",
        "",
        "| URL MP | Before | After |",
        "| --- | --- | --- |",
        "| /guida-prezzi-mq-milano/ | Canonical self; title “Valori OMI Milano 2026… tabella”; tabella zone + FAQ; schema Article+FAQPage+Dataset | Canonical → VCT prezzi-mq-milano; title consulenza; sintesi ~300–500 parole; CTA dofollow VCT; schema WebPage+Person/RealEstateAgent |",
        "| /guida-prezzi-mq-brescia/ | Idem (self-canonical, tabella, FAQ) | Idem pattern → VCT prezzi-mq-brescia |",
        "| /guida-prezzi-mq-bergamo/ | Idem (self-canonical, tabella, FAQ) | Idem pattern → VCT prezzi-mq-bergamo |",
        "",
        "## Link hub / footer / zone CTA",
        "",
        "- Homepage `seo-home-mesh` Guide OMI → URL VCT (12 province).",
        "- Footer `Guide prezzi OMI` → URL VCT (12 province).",
        "- `seller-zones-link` / “Consulta i valori OMI…” → VCT della provincia.",
        "- Link interni `/guida-prezzi-mq-*` retargetati a VCT in tutto il sito.",
        "",
        "## Non fatto (per brief)",
        "- Nessun noindex globale.",
        "- Nessun redirect homepage → VCT.",
        "- Pagine non cancellate: restano come sintesi + link.",
        "",
        "## Sitemap",
        "- Guide MP restano in sitemap (URL vive) con priorità ridotta 0.5.",
    ]
    out = ROOT / "docs" / "anti-cannibal-vct-before-after.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)}")


def patch_sitemap_priorities() -> None:
    path = ROOT / ".github" / "scripts" / "update_sitemap.py"
    text = path.read_text(encoding="utf-8")
    text2 = text.replace(
        '("/guida-prezzi-mq-milano/", "0.8"),\n'
        '        ("/guida-prezzi-mq-brescia/", "0.8"),\n'
        '        ("/guida-prezzi-mq-bergamo/", "0.8"),',
        '("/guida-prezzi-mq-milano/", "0.5"),\n'
        '        ("/guida-prezzi-mq-brescia/", "0.5"),\n'
        '        ("/guida-prezzi-mq-bergamo/", "0.5"),',
    )
    if text2 != text:
        path.write_text(text2, encoding="utf-8")
        print("Lowered guide priorities in update_sitemap.py")


def main() -> None:
    write_inventory()
    for slug in ("milano", "brescia", "bergamo"):
        rewrite_guide(slug)
    n = retarget_omi_links()
    print(f"Files with link retargets: {n}")
    patch_seller_footer_geo_script()
    patch_sitemap_priorities()
    write_before_after()


if __name__ == "__main__":
    main()
