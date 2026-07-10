#!/usr/bin/env python3
"""Engagement patches: localize seller provinces, hero portrait, sticky bar."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))

from buyer_provinces import LOMBARD_PROVINCES, NEW_PROVINCES
from patch_seller_provinces import build_page
from seller_footer_geo import patch_seller as patch_footer_geo
from seller_localize import SELLER_LOCALIZE, build_testimonials_html

ROOT = Path(__file__).resolve().parents[2]
CACHE = "20260725"

SELLER_PAGES = ["index.html"] + [
    f"{slug}/index.html" for slug, _, _ in LOMBARD_PROVINCES if slug != "milano"
]
PROVINCE_SLUGS = [slug for slug in SELLER_LOCALIZE]

HERO_AGENT_RE = re.compile(r'<div class="hero-agent">.*?</div>\s*', re.DOTALL)
STICKY_RE = re.compile(
    r'\s*<div class="seller-sticky-bar".*?</div>\s*'
    r'(?:<script src="/assets/seller-sticky\.js[^"]*" defer></script>\s*)?',
    re.DOTALL,
)
ORPHAN_STICKY_JS_RE = re.compile(
    r'\s*<script src="/assets/seller-sticky\.js[^"]*" defer></script>\s*'
)

BERGAMO_REMNANTS = [
    ("Bergamo e Provincia", "{portrait_span}"),
    (
        '"A Bergamo, Citt&agrave; Alta e la Citt&agrave; Bassa sono due mercati diversi. Conoscere questa differenza prima del lancio vale migliaia di euro sulla trattativa."',
        "{quote}",
    ),
    (
        "La maggior parte degli agenti tratta tutto allo stesso modo. Io costruisco una strategia su misura per la zona specifica &mdash; Bergamo centro, collina, provincia &mdash; prima ancora di pubblicare la prima foto.",
        "{strategy}",
    ),
    (
        "Confronti zona per zona &mdash; Citt&agrave; Alta, Citt&agrave; Bassa, valli, pianura &mdash; e posizionamento corretto del prezzo.",
        "{method_1_p}",
    ),
    (
        "L'affiliazione RE/MAX aggiunge autorit&agrave;, rete e maggiore visibilit&agrave; &mdash; anche per acquirenti che si spostano da Milano verso Bergamo e per chi cerca soluzioni sul Lago d'Iseo bergamasco.",
        "{network_p}",
    ),
    (
        "Un marchio riconoscibile rassicura i proprietari e gli acquirenti &mdash; anche da fuori provincia e da acquirenti che si spostano da Milano verso Bergamo.",
        "{network_1_p}",
    ),
]


def city_label(slug: str) -> str:
    for s, it, _en in LOMBARD_PROVINCES:
        if s == slug:
            return it
    return slug.title()


def zone_chips_for(slug: str) -> list[str]:
    if slug in NEW_PROVINCES:
        return NEW_PROVINCES[slug]["datalist_it"][:-1]
    return [f"{city_label(slug)} città"]


def foto_src(rel: str) -> str:
    return "foto.jpg" if rel == "index.html" else "../foto.jpg"


def city_from_path(rel: str) -> str:
    if rel == "index.html":
        return "Milano"
    slug = rel.split("/")[0]
    return city_label(slug)


def wa_url_for(rel: str) -> str:
    city = city_from_path(rel)
    text = quote(f"Ciao Maurizio, vorrei ricevere un'analisi riservata del mio immobile a {city}.")
    return f"https://wa.me/393514581993?text={text}"


def hero_agent_block(rel: str) -> str:
    src = foto_src(rel)
    return f"""          <div class="hero-agent reveal">
            <img src="{src}" alt="Maurizio Piraino" width="56" height="56" decoding="async" />
            <div>
              <strong>Maurizio Piraino</strong>
              <span>Consulente RE/MAX · Risposta entro 24h</span>
            </div>
          </div>
"""


def sticky_block(rel: str) -> str:
    wa = wa_url_for(rel)
    return f"""  <div class="seller-sticky-bar" role="region" aria-label="Azioni rapide">
    <div class="seller-sticky-inner">
      <a class="btn btn-red" href="#form">Richiedi analisi</a>
      <a class="btn btn-outline" href="{wa}" aria-label="WhatsApp">WA</a>
    </div>
  </div>
  <script src="/assets/seller-sticky.js?v={CACHE}" defer></script>
"""


def fix_wa_urls(html: str, city: str) -> str:
    wa_text = quote(f"Ciao Maurizio, vorrei ricevere un'analisi riservata del mio immobile a {city}.")
    html = re.sub(
        r'href="https://wa\.me/393514581993\?text=[^"]*"',
        f'href="https://wa.me/393514581993?text={wa_text}"',
        html,
    )
    return html


def fix_eyebrow_and_footer_tagline(html: str, slug: str) -> str:
    city = city_label(slug)
    tagline = NEW_PROVINCES[slug]["footer_geo_it"].replace(" · ", " &middot; ")
    html = re.sub(
        r'<div class="eyebrow">[^<]+</div>',
        f'<div class="eyebrow">{city} &middot; Analisi immobiliare riservata</div>',
        html,
        count=1,
    )
    html = html.replace(
        f"Bergamo &middot; {tagline}",
        tagline,
    )
    html = html.replace(
        "Bergamo &middot; Citt&agrave; Alta &middot; Valle Seriana &middot; Provincia",
        tagline,
    )
    return html


def fix_schema_and_faq(html: str, slug: str) -> str:
    city = city_label(slug)
    html = re.sub(
        r'A [^"]+ la differenza tra Città Alta e Città Bassa, o tra i vari quartieri, può incidere significativamente sul valore\.',
        f'A {city} ogni comune e quartiere ha dinamiche proprie che incidono in modo significativo sul valore reale.',
        html,
        count=1,
    )
    html = re.sub(
        r'Opero su tutto il territorio di [^<]+&mdash; Bergamo citt&agrave;, Citt&agrave; Alta, Valle Seriana, Valle Brembana, comuni di cintura e Bassa bergamasca\. Ogni zona ha dinamiche proprie\.',
        f'Opero su {city} e provincia, con attenzione alle micro-zone e alle dinamiche locali del mercato immobiliare.',
        html,
        count=1,
    )
    return html


def scrub_bergamo_remainders(html: str, slug: str) -> str:
    city = city_label(slug)
    zones = zone_chips_for(slug)
    z1 = zones[0]
    z2 = zones[1] if len(zones) > 1 else zones[0]
    z3 = zones[2] if len(zones) > 2 else zones[0]

    replacements = [
        (
            "Dal centro di Bergamo a Citt&agrave; Alta, dalla Valle Seriana alla Bassa, ogni zona ha dinamiche proprie.",
            f"Da {city} ai comuni di provincia, ogni micro-zona ha dinamiche proprie.",
        ),
        (
            'list="zoneBG" placeholder="Scrivi zona o comune (es. Citt&agrave; Alta, Seriate, Treviglio...)"',
            f'list="zoneSeller" placeholder="Scrivi zona o comune (es. {z1}, {z2}...)"',
        ),
        ("nel territorio bergamasco", f"a {city} e in provincia"),
        ("nel territorio bergamasco.", f"a {city} e in provincia."),
        ("mercato bergamasco", f"mercato a {city}"),
        ("RE/MAX · Bergamo", f"RE/MAX · {city}"),
        ("Bergamo, valle o provincia", f"{city} e provincia"),
        ("Bergamo, valli o provincia", f"{city} e provincia"),
        ("territorio bergamasco", f"territorio di {city}"),
        (
            "Citt&agrave; Alta, la Citt&agrave; Bassa e i comuni in provincia",
            f"{z1}, {z2} e i comuni in provincia",
        ),
        (
            "che a Bergamo cambia significativamente tra centro, collina e pianura",
            f"che a {city} cambia significativamente da una micro-zona all'altra",
        ),
        (
            "Opero su tutto il territorio bergamasco &mdash; Bergamo citt&agrave;, Citt&agrave; Alta, Valle Seriana, Valle Brembana, comuni di cintura e Bassa bergamasca. Ogni zona ha dinamiche proprie.",
            f"Opero su {city} e provincia, con attenzione alle micro-zone e alle dinamiche locali del mercato immobiliare.",
        ),
        ("Lavori solo su Bergamo o anche in provincia?", f"Lavori solo su {city} o anche in provincia?"),
        (
            "Opero su Bergamo città e provincia e, tramite RE/MAX",
            f"Opero su {city} e provincia e, tramite RE/MAX",
        ),
        (
            f"A {city} la differenza tra Citt&agrave; Alta e Citt&agrave; Bassa, o tra i vari quartieri, pu&ograve; incidere significativamente sul valore.",
            f"A {city} ogni comune e quartiere ha dinamiche proprie che incidono in modo significativo sul valore reale.",
        ),
        ("in Città Alta o in provincia?", "e in provincia?"),
        (f"a {city}, e in provincia?", f"a {city} e in provincia?"),
        ("Città Alta e provincia.", f"{city} e provincia."),
        ("Citt&agrave; Alta e provincia", f"{city} e provincia"),
        ("Mercato Bergamasco", f"Mercato {city}"),
        ("Mercato Bergamo", f"Mercato {city}"),
        (
            "Bergamo Alta, Borgo Palazzo, Val Seriana e i comuni della provincia hanno dinamiche di prezzo molto diverse tra loro.",
            f"Ogni comune e micro-zona di {city} ha dinamiche di prezzo proprie.",
        ),
        (
            '<div class="eyebrow">Bergamo &middot; Analisi immobiliare riservata</div>',
            f'<div class="eyebrow">{city} &middot; Analisi immobiliare riservata</div>',
        ),
    ]
    for old, new in replacements:
        html = html.replace(old, new)
    return html


def rebuild_seller_zones(html: str, slug: str) -> str:
    city = city_label(slug)
    chips_html = "".join(f'<span class="seller-zone-chip">{c}</span>' for c in zone_chips_for(slug))
    buyer_link = f"/comprare-casa-{slug}/"
    section = f"""    <section class="seller-zones">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Zone servite · {city}</div>
          <h2>Conosco il mercato locale, strada per strada.</h2>
          <p>Opero su {city} e provincia: ogni comune e micro-zona ha dinamiche di prezzo proprie.</p>
        </div>
        <div class="seller-zones-wrap reveal">{chips_html}</div>
        <p class="seller-zones-link"><a href="{buyer_link}">Consulta i valori OMI ufficiali per zona a {city} →</a></p>
      </div>
    </section>"""
    return re.sub(
        r"<section class=\"seller-zones\">.*?</section>",
        section,
        html,
        count=1,
        flags=re.DOTALL,
    )


def patch_zones_and_meta(html: str, slug: str) -> str:
    city = city_label(slug)
    html = rebuild_seller_zones(html, slug)
    html = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="Vendere casa a {city} e in provincia? Analisi immobiliare riservata su dati reali, prima di parlare di incarico."',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="keywords" content="[^"]*Bergamo[^"]*"',
        f'<meta name="keywords" content="agente immobiliare {city}, agente RE/MAX {city}, valutazione casa {city}, vendere casa {city}, Maurizio Piraino immobiliare {city}"',
        html,
        count=1,
    )
    return html


def localize_province(html: str, slug: str) -> str:
    data = SELLER_LOCALIZE.get(slug)
    if not data:
        return html

    city = city_label(slug)
    html = scrub_bergamo_remainders(html, slug)
    html = fix_wa_urls(html, city)
    html = fix_eyebrow_and_footer_tagline(html, slug)
    html = fix_schema_and_faq(html, slug)

    for old_tpl, new_tpl in BERGAMO_REMNANTS:
        old = old_tpl.format(city=city) if "{city}" in old_tpl else old_tpl
        new = new_tpl.format(**data)
        html = html.replace(old, new, 1)

    html = re.sub(
        r'<div class="quote">"[^"]*Citt&agrave; Alta[^"]*"</div>',
        f'<div class="quote">{data["quote"]}</div>',
        html,
        count=1,
    )

    html = re.sub(
        r"<span>Agente Immobiliare affiliato RE/MAX.*?</span>",
        f'<span>Agente Immobiliare affiliato {data["portrait_span"]}</span>',
        html,
        count=1,
    )

    html = re.sub(
        r'<p class="lead">Sono un Agente Immobiliare affiliato RE/MAX con background da geometra e imprenditore\. Conosco le specificit&agrave; del mercato a [^<]+</p>',
        f'<p class="lead">Sono un Agente Immobiliare affiliato RE/MAX con background da geometra e imprenditore. {data["about_lead"]}</p>',
        html,
        count=1,
    )

    html = re.sub(
        r'<div class="section-kicker">Mercato [^<]+</div>\s*<h2>[^<]+</h2>\s*<p>[^<]+</p>',
        (
            f'<div class="section-kicker">{data["market_kicker"]}</div>\n'
            f'          <h2>{data["market_h2"]}</h2>\n'
            f'          <p>{data["market_intro"]}</p>'
        ),
        html,
        count=1,
    )

    market_cards = (
        f'<div class="market-card reveal"><span>{data["market_1_span"]}</span><strong>{data["market_1_h"]}</strong>'
        f'<p>{data["market_1_p"]}</p></div>\n'
        f'          <div class="market-card reveal"><span>{data["market_2_span"]}</span><strong>{data["market_2_h"]}</strong>'
        f'<p>{data["market_2_p"]}</p></div>\n'
        f'          <div class="market-card reveal"><span>{data["market_3_span"]}</span><strong>{data["market_3_h"]}</strong>'
        f'<p>{data["market_3_p"]}</p></div>'
    )
    html = re.sub(
        r'<div class="market-grid">\s*<div class="market-card reveal">.*?</div>\s*</div>',
        f'<div class="market-grid">\n          {market_cards}\n        </div>',
        html,
        count=1,
        flags=re.DOTALL,
    )

    testimonials = build_testimonials_html(data["testimonials"])  # type: ignore[arg-type]
    html = re.sub(
        r'<div class="testimonial-grid">.*?</div>\s*</div>\s*</section>\s*<section class="faq">',
        f'<div class="testimonial-grid">\n{testimonials}\n        </div>\n      </div>\n    </section>\n\n    <section class="faq">',
        html,
        count=1,
        flags=re.DOTALL,
    )

    html = re.sub(
        r'<h2>Prima di vendere casa a [^<]+</h2>\s*<p>[^<]+</p>',
        f'<h2>{data["final_h2"]}</h2>\n        <p>{data["final_p"]}</p>',
        html,
        count=1,
    )

    html = patch_zones_and_meta(html, slug)
    return html


def patch_hero_agent(html: str, rel: str) -> str:
    html = HERO_AGENT_RE.sub("", html)
    marker = '<div class="eyebrow">'
    if marker in html and "hero-agent" not in html:
        html = html.replace(marker, hero_agent_block(rel) + marker, 1)
    return html


def patch_sticky(html: str, rel: str) -> str:
    html = STICKY_RE.sub("\n", html)
    html = ORPHAN_STICKY_JS_RE.sub("\n", html)
    wa = wa_url_for(rel)
    clean_tail = (
        "  </script>\n"
        "</div>\n"
        f'  <script src="/assets/site-nav.js?v={CACHE}" defer></script>\n'
        f'{sticky_block(rel).strip()}\n'
        "\n</body>"
    )
    html = re.sub(
        r"  </script>\n</div>.*?</body>",
        clean_tail,
        html,
        count=1,
        flags=re.DOTALL,
    )
    return html


def patch_trust_row(html: str) -> str:
    return html.replace(
        '<div class="trust"><strong>100%</strong><span>Riservatezza</span></div>',
        '<div class="trust"><strong>24h</strong><span>Risposta garantita</span></div>',
        1,
    )


def regenerate_province_pages() -> None:
    for slug in PROVINCE_SLUGS:
        out = ROOT / slug / "index.html"
        out.write_text(build_page(slug), encoding="utf-8")
        print(f"Regenerated {out.relative_to(ROOT)}")


def patch_page(rel: str) -> None:
    path = ROOT / rel
    if not path.exists():
        return
    html = path.read_text(encoding="utf-8")
    slug = "milano" if rel == "index.html" else rel.split("/")[0]

    if slug in SELLER_LOCALIZE:
        html = localize_province(html, slug)
    elif slug in NEW_PROVINCES:
        html = patch_zones_and_meta(html, slug)

    html = patch_hero_agent(html, rel)
    html = patch_sticky(html, rel)
    html = patch_trust_row(html)

    path.write_text(html, encoding="utf-8")
    print(f"Patched {rel}")


def patch_hub() -> None:
    for rel in ("comprare-casa/index.html", "en/buy-home/index.html"):
        path = ROOT / rel
        if not path.exists():
            continue
        html = path.read_text(encoding="utf-8")
        hero_css = (
            ".hero{background:linear-gradient(180deg,rgba(7,7,7,.78),rgba(7,7,7,.9)),"
            "url(/milano.jpg) center/cover no-repeat;color:#fff;padding:96px 0 80px;text-align:center}"
        )
        html = re.sub(
            r"\.hero\{background:var\(--black\);color:#fff;padding:72px 0 64px;text-align:center\}",
            hero_css,
            html,
            count=1,
        )
        if 'rel="preload" as="image" href="/milano.jpg"' not in html:
            html = html.replace(
                "</head>",
                '  <link rel="preload" as="image" href="/milano.jpg" fetchpriority="high" />\n</head>',
                1,
            )
        path.write_text(html, encoding="utf-8")
        print(f"Patched hub {rel}")


def main() -> None:
    regenerate_province_pages()
    for rel in SELLER_PAGES:
        patch_page(rel)
    for slug in PROVINCE_SLUGS:
        patch_footer_geo(ROOT / f"{slug}/index.html", slug)
    patch_hub()


if __name__ == "__main__":
    main()
