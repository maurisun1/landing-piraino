#!/usr/bin/env python3
"""Make seller province pages secondary in hierarchy (keep vendita SEO)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from buyer_provinces import LOMBARD_PROVINCES
from locales import buyer_province_url


def dual_path_block(city: str, buy: str, lang: str = "it") -> str:
    if lang == "de":
        return f"""    <section class="dual-path consultant-path-lite" aria-label="Wählen Sie Ihren Weg">
      <div class="container dual-path-grid">
        <p class="dual-path-intro"><em>RE/MAX</em> · {city}</p>
        <a class="dual-path-card dual-path-buy" href="{buy}">
          <span class="dual-path-label">01 · Hauptservice</span>
          <strong>Property Finding</strong>
          <p>Persönliche Suche, auch off-market. Beratung für Käufer und Investoren.</p>
          <span class="dual-path-cta">Suche starten →</span>
        </a>
        <a class="dual-path-card dual-path-sell" href="#form">
          <span class="dual-path-label">02 · Verkäufer</span>
          <strong>Bewertung und Verkauf</strong>
          <p>Vertrauliche Analyse auf OMI-Daten und Mikrozone. Keine Verpflichtung zum Mandat.</p>
          <span class="dual-path-cta">Analyse anfordern →</span>
        </a>
      </div>
    </section>
"""
    if lang == "fr":
        return f"""    <section class="dual-path consultant-path-lite" aria-label="Choisissez votre parcours">
      <div class="container dual-path-grid">
        <p class="dual-path-intro"><em>RE/MAX</em> · {city}</p>
        <a class="dual-path-card dual-path-buy" href="{buy}">
          <span class="dual-path-label">01 · Service principal</span>
          <strong>Property Finding</strong>
          <p>Recherche personnalisée, aussi hors marché. Conseil pour acheteurs et investisseurs.</p>
          <span class="dual-path-cta">Commencer la recherche →</span>
        </a>
        <a class="dual-path-card dual-path-sell" href="#form">
          <span class="dual-path-label">02 · Vendeurs</span>
          <strong>Estimation et vente</strong>
          <p>Analyse confidentielle sur données OMI et micro-zone. Aucune obligation de mandat.</p>
          <span class="dual-path-cta">Demander une analyse →</span>
        </a>
      </div>
    </section>
"""
    return f"""    <section class="dual-path consultant-path-lite" aria-label="Scegli il tuo percorso">
      <div class="container dual-path-grid">
        <p class="dual-path-intro"><em>RE/MAX</em> · {city}</p>
        <a class="dual-path-card dual-path-buy" href="{buy}">
          <span class="dual-path-label">01 · Servizio principale</span>
          <strong>Property Finding</strong>
          <p>Ricerca personalizzata anche off-market. Consulenza per acquirenti e investitori.</p>
          <span class="dual-path-cta">Iniziamo la ricerca →</span>
        </a>
        <a class="dual-path-card dual-path-sell" href="#form">
          <span class="dual-path-label">02 · Venditori</span>
          <strong>Valutazione e vendita</strong>
          <p>Analisi riservata su dati OMI e micro-zona. Nessun obbligo di incarico.</p>
          <span class="dual-path-cta">Richiedi analisi →</span>
        </a>
      </div>
    </section>
"""


SERVICES_IT = """    <section class="seller-services consultant-services" id="servizi">
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
"""

SERVICES_DE = """    <section class="seller-services consultant-services" id="servizi">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Leistungen</div>
          <h2>Kauf, Investment oder Verkauf — mit Methode.</h2>
          <p>Property Finding und Investoren zuerst. Verkauf bleibt strukturiert, wenn Sie ihn brauchen.</p>
        </div>
        <div class="seller-services-grid">
          <article class="seller-service-card featured reveal"><div class="seller-service-num">01</div><h3>Property Finding</h3><p>Persönliche Suche auch off-market, Besichtigungen, Verhandlung und Schutz bis zum Notartermin.</p></article>
          <article class="seller-service-card reveal"><div class="seller-service-num">02</div><h3>Beratung für Investoren</h3><p>Renditeobjekte, Wertsteigerung und Ertragsanalyse mit klaren Zahlen.</p></article>
          <article class="seller-service-card reveal"><div class="seller-service-num">03</div><h3>Immobilienkäufer</h3><p>Ersterwerb oder Wohnungswechsel: Dokumentenprüfung und Verhandlungsunterstützung.</p></article>
          <article class="seller-service-card secondary reveal"><div class="seller-service-num">04</div><h3>Bewertung und Verkauf</h3><p>OMI-Analyse, Preisstrategie, RE/MAX-Marketing und Begleitung bis zum Notartermin.</p></article>
        </div>
      </div>
    </section>
"""

SERVICES_FR = """    <section class="seller-services consultant-services" id="servizi">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Services</div>
          <h2>Acheter, investir ou vendre — avec méthode.</h2>
          <p>Property Finding et investisseurs en premier. La vente reste structurée si vous en avez besoin.</p>
        </div>
        <div class="seller-services-grid">
          <article class="seller-service-card featured reveal"><div class="seller-service-num">01</div><h3>Property Finding</h3><p>Recherche personnalisée aussi hors marché, visites, négociation et protection jusqu'à l'acte.</p></article>
          <article class="seller-service-card reveal"><div class="seller-service-num">02</div><h3>Conseil pour investisseurs</h3><p>Opportunités locatives, valorisation et analyse de rendement avec des chiffres clairs.</p></article>
          <article class="seller-service-card reveal"><div class="seller-service-num">03</div><h3>Acheteurs</h3><p>Premier achat ou changement de logement : contrôle documentaire et soutien en négociation.</p></article>
          <article class="seller-service-card secondary reveal"><div class="seller-service-num">04</div><h3>Estimation et vente</h3><p>Analyse OMI, stratégie de prix, marketing RE/MAX et accompagnement jusqu'à l'acte.</p></article>
        </div>
      </div>
    </section>
"""


def mid_cta(city: str, buy: str, lang: str) -> str:
    if lang == "de":
        return f"""    <section class="seller-mid-cta">
      <div class="container reveal">
        <div class="seller-mid-cta-inner">
          <div>
            <p class="seller-mid-kicker">RE/MAX · {city}</p>
            <h2>Suchen, investieren oder verkaufen in {city}?</h2>
            <p>Vertrauliche Beratung auf realen Daten. Keine Verpflichtung, Antwort innerhalb von 24 Stunden.</p>
          </div>
          <div class="seller-mid-actions">
            <a class="btn btn-red" href="{buy}">Property Finding →</a>
            <a class="btn btn-light" href="#form">Verkaufsanalyse →</a>
          </div>
        </div>
      </div>
    </section>
"""
    if lang == "fr":
        return f"""    <section class="seller-mid-cta">
      <div class="container reveal">
        <div class="seller-mid-cta-inner">
          <div>
            <p class="seller-mid-kicker">RE/MAX · {city}</p>
            <h2>Cherchez, investissez ou vendez à {city} ?</h2>
            <p>Conseil confidentiel sur données réelles. Aucune obligation, réponse sous 24 heures.</p>
          </div>
          <div class="seller-mid-actions">
            <a class="btn btn-red" href="{buy}">Property Finding →</a>
            <a class="btn btn-light" href="#form">Analyse vente →</a>
          </div>
        </div>
      </div>
    </section>
"""
    return f"""    <section class="seller-mid-cta">
      <div class="container reveal">
        <div class="seller-mid-cta-inner">
          <div>
            <p class="seller-mid-kicker">RE/MAX · {city}</p>
            <h2>Cerchi casa, investi o vendi a {city}?</h2>
            <p>Consulenza riservata su dati reali. Nessun obbligo, risposta entro 24 ore.</p>
          </div>
          <div class="seller-mid-actions">
            <a class="btn btn-red" href="{buy}">Property Finding →</a>
            <a class="btn btn-light" href="#form">Analisi vendita →</a>
          </div>
        </div>
      </div>
    </section>
"""


def ensure_css(html: str) -> str:
    if "consultant-home.css" in html:
        return html
    for marker in (
        '<link rel="stylesheet" href="/assets/dual-path.css',
        '<link rel="stylesheet" href="/assets/seller-landing.css',
        '<link rel="stylesheet" href="/assets/remax-brand.css',
    ):
        if marker in html:
            # insert after first matching link line
            m = re.search(re.escape(marker) + r'[^>]*>', html)
            if m:
                return html[: m.end()] + '\n  <link rel="stylesheet" href="/assets/consultant-home.css?v=20260715b" />' + html[m.end() :]
    return html


def patch_file(path: Path, city: str, buy: str, lang: str) -> bool:
    html = path.read_text(encoding="utf-8")
    original = html
    html = ensure_css(html)

    # Dual path: buy first
    html = re.sub(
        r'<section class="dual-path".*?</section>\s*',
        dual_path_block(city, buy, lang) + "\n",
        html,
        count=1,
        flags=re.DOTALL,
    )

    services = {"it": SERVICES_IT, "de": SERVICES_DE, "fr": SERVICES_FR}[lang]
    if "seller-services" in html:
        html = re.sub(
            r'<section class="seller-services".*?</section>\s*',
            services + "\n",
            html,
            count=1,
            flags=re.DOTALL,
        )

    if "seller-mid-cta" in html:
        html = re.sub(
            r'<section class="seller-mid-cta".*?</section>\s*',
            mid_cta(city, buy, lang) + "\n",
            html,
            count=1,
            flags=re.DOTALL,
        )

    # Soft agent label in portrait if present
    if lang == "it":
        html = html.replace(
            "Agente Immobiliare affiliato RE/MAX · " + city,
            "Consulente immobiliare RE/MAX · " + city,
        )
        html = html.replace(
            f"Agente Immobiliare affiliato RE/MAX · {city}",
            f"Consulente immobiliare RE/MAX · {city}",
        )

    if html != original:
        path.write_text(html, encoding="utf-8")
        return True
    return False


def main() -> None:
    count = 0
    # IT provinces (skip milano homepage — already consultant home)
    for slug, name, _en in LOMBARD_PROVINCES:
        if slug == "milano":
            continue
        rel = f"{slug}/index.html"
        path = ROOT / rel
        if not path.exists():
            continue
        buy = buyer_province_url(slug, "it")
        if patch_file(path, name, buy, "it"):
            print(f"  patched {rel}")
            count += 1
    for lang in ("de", "fr"):
        for slug, name, _en in LOMBARD_PROVINCES:
            if slug == "milano":
                continue
            rel = f"{lang}/{slug}/index.html"
            path = ROOT / rel
            if not path.exists():
                continue
            from locales import city_label
            city = city_label(slug, lang)
            buy = buyer_province_url(slug, lang)
            if patch_file(path, city, buy, lang):
                print(f"  patched {rel}")
                count += 1
    print(f"Done. {count} files.")


if __name__ == "__main__":
    main()
