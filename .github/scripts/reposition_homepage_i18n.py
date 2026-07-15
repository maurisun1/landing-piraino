#!/usr/bin/env python3
"""Apply consultant repositioning to DE/FR Milano homepages."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def apply_locale(path: Path, L: dict) -> None:
    html = path.read_text(encoding="utf-8")
    if "consultant-home.css" not in html:
        html = html.replace(
            '<link rel="stylesheet" href="/assets/dual-path.css?v=20260735" />',
            '<link rel="stylesheet" href="/assets/dual-path.css?v=20260735" />\n'
            '  <link rel="stylesheet" href="/assets/consultant-home.css?v=20260715" />',
        )

    # Hero
    pattern = re.compile(
        r'<div class="hero-agent reveal">.*?</a>\n          </div>\n        <aside class="hero-form-wrap',
        re.DOTALL,
    )
    hero = f"""<div class="hero-agent reveal">
            <img src="/foto.jpg" alt="Maurizio Piraino" width="56" height="56" decoding="async" />
            <div>
              <strong>Maurizio Piraino</strong>
              <span>{L['agent_span']}</span>
            </div>
          </div>
<div class="eyebrow">{L['eyebrow']}</div>
          <h1>{L['h1']}</h1>
          <p>
            {L['lead']}
          </p>
          <ul class="seller-form-benefits">
            <li>{L['b1']}</li>
            <li>{L['b2']}</li>
            <li>{L['b3']}</li>
            <li>{L['b4']}</li>
          </ul>
          <a class="btn btn-wa seller-form-wa" href="{L['wa']}"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg> {L['wa_label']}</a>
          </div>
        <aside class="hero-form-wrap"""
    html2, n = pattern.subn(hero, html, count=1)
    if n != 1:
        print(f"  warn hero {path}")
    else:
        html = html2

    # Form head (match DE/FR existing titles)
    for old_h2 in (
        "Erhalten Sie eine vertrauliche Immobilienberatung",
        "Recevez une consultation immobilière confidentielle",
        "Ricevi una consulenza immobiliare riservata",
    ):
        if old_h2 in html:
            html = html.replace(old_h2, L["form_h2"], 1)
            break
    for old_p in (
        "Keine automatische Schätzung. Nur eine echte Analyse auf Basis Ihres lokalen Marktes.",
        "Aucune estimation automatique. Une analyse réelle basée sur le marché de votre zone.",
    ):
        if old_p in html:
            html = html.replace(old_p, L["form_p"], 1)
            break

    # Intent selector if missing
    if 'name="intento"' not in html and 'id="intentoVal"' not in html:
        html = html.replace(
            '<input type="hidden" name="landing"',
            f'<input type="hidden" name="intento" id="intentoVal" value="{L["intent1"]}" />\n'
            '          <input type="hidden" name="landing"',
            1,
        )
    if "intent-grid" not in html:
        html = re.sub(
            r'(<div class="form-step active" id="formStep1">\s*<p class="step-note">)([^<]+)(</p>)',
            rf'\1{L["step_note"]}\3\n            <label>{L["intent_label"]}</label>\n'
            f'            <div class="intent-grid" role="group" aria-label="{L["intent_label"]}">\n'
            f'              <div class="intent-card on" data-v="{L["intent1"]}" onclick="setIntent(this)">{L["intent1"]}</div>\n'
            f'              <div class="intent-card" data-v="{L["intent2"]}" onclick="setIntent(this)">{L["intent2"]}</div>\n'
            f'              <div class="intent-card" data-v="{L["intent3"]}" onclick="setIntent(this)">{L["intent3"]}</div>\n'
            f'            </div>',
            html,
            count=1,
        )

    # Replace dual-path
    path_block = f"""    <section class="consultant-path" aria-label="{L['path_aria']}">
      <div class="container consultant-path-grid">
        <p class="consultant-path-intro"><em>RE/MAX</em> · {L['path_intro']}</p>
        <a class="consultant-path-card consultant-path-primary" href="{L['buy_hub']}">
          <span class="consultant-path-label">01 · {L['path1_label']}</span>
          <strong>Property Finding</strong>
          <p>{L['path1_p']}</p>
          <span class="consultant-path-cta">{L['path1_cta']}</span>
        </a>
        <a class="consultant-path-card consultant-path-invest" href="#servizi">
          <span class="consultant-path-label">02 · {L['path2_label']}</span>
          <strong>{L['path2_h']}</strong>
          <p>{L['path2_p']}</p>
          <span class="consultant-path-cta">{L['path2_cta']}</span>
        </a>
        <a class="consultant-path-card consultant-path-sell" href="#form">
          <span class="consultant-path-label">03 · {L['path3_label']}</span>
          <strong>{L['path3_h']}</strong>
          <p>{L['path3_p']}</p>
          <span class="consultant-path-cta">{L['path3_cta']}</span>
        </a>
      </div>
    </section>
"""
    if "consultant-path" not in html:
        html = re.sub(
            r'<section class="dual-path".*?</section>\s*',
            path_block + "\n",
            html,
            count=1,
            flags=re.DOTALL,
        )

    # Services
    services = f"""    <section class="seller-services consultant-services" id="servizi">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">{L['serv_kicker']}</div>
          <h2>{L['serv_h2']}</h2>
          <p>{L['serv_p']}</p>
        </div>
        <div class="seller-services-grid">
          <article class="seller-service-card featured reveal">
            <div class="seller-service-num">01</div>
            <h3>Property Finding</h3>
            <p>{L['s1_p']}</p>
          </article>
          <article class="seller-service-card reveal">
            <div class="seller-service-num">02</div>
            <h3>{L['s2_h']}</h3>
            <p>{L['s2_p']}</p>
          </article>
          <article class="seller-service-card reveal">
            <div class="seller-service-num">03</div>
            <h3>{L['s3_h']}</h3>
            <p>{L['s3_p']}</p>
          </article>
          <article class="seller-service-card secondary reveal">
            <div class="seller-service-num">04</div>
            <h3>{L['s4_h']}</h3>
            <p>{L['s4_p']}</p>
          </article>
        </div>
      </div>
    </section>
"""
    html = re.sub(
        r'<section class="seller-services".*?</section>\s*',
        services + "\n",
        html,
        count=1,
        flags=re.DOTALL,
    )

    # Mid CTA + final CTA soft replacements
    html = re.sub(
        r'<section class="seller-mid-cta".*?</section>',
        f"""    <section class="seller-mid-cta">
      <div class="container reveal">
        <div class="seller-mid-cta-inner">
          <div>
            <p class="seller-mid-kicker">RE/MAX · {L['mid_kicker']}</p>
            <h2>{L['mid_h2']}</h2>
            <p>{L['mid_p']}</p>
          </div>
          <div class="seller-mid-actions">
            <a class="btn btn-red" href="#form">{L['cta']}</a>
            <a class="btn btn-light" href="{L['buy_hub']}">{L['mid_sec']}</a>
          </div>
        </div>
      </div>
    </section>""",
        html,
        count=1,
        flags=re.DOTALL,
    )

    html = re.sub(
        r'<section class="final-cta".*?</section>',
        f"""    <section class="final-cta">
      <div class="container reveal">
        <h2>{L['final_h2']}</h2>
        <p>{L['final_p']}</p>
        <div class="hero-actions" style="justify-content:center">
          <a class="btn btn-red" href="#form">{L['cta']}</a>
          <a class="btn btn-wa" href="{L['wa']}"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg> WhatsApp</a>
        </div>
      </div>
    </section>""",
        html,
        count=1,
        flags=re.DOTALL,
    )

    if "function setIntent" not in html:
        html = html.replace(
            "    function onMqChange(val){",
            """
    function setIntent(el){
      document.querySelectorAll('.intent-card').forEach(c => c.classList.remove('on'));
      el.classList.add('on');
      var i = document.getElementById('intentoVal');
      if (i) i.value = el.getAttribute('data-v');
    }

    function onMqChange(val){""",
        )

    # Footer tagline soft
    for old, new in L.get("footer_swaps", []):
        html = html.replace(old, new)

    path.write_text(html, encoding="utf-8")
    print(f"  wrote {path.relative_to(ROOT)}")


DE = {
    "agent_span": "Berater für Käufer und Investoren · RE/MAX",
    "eyebrow": "Mailand · Lombardei · Immobilienberatung",
    "h1": "Berater für Immobilienkäufer und Investoren",
    "lead": 'Der Partner für alle, die ein Haus kaufen oder in Immobilien investieren. <strong>Analyse vor dem Kauf</strong>, persönliche Suche, Dokumentenprüfung und Begleitung bis zum Notartermin.',
    "b1": "Property Finding — auch off-market",
    "b2": "Dedizierte Beratung für Investoren",
    "b3": "Dokumentenprüfung und Verhandlung",
    "b4": "Begleitung bis zum Notartermin — ohne Erstverpflichtung",
    "wa": "https://wa.me/393514581993?text=Hallo%20Maurizio%2C%20ich%20m%C3%B6chte%20eine%20Beratung.%20Ich%20suche%20eine%20Immobilie%20%2F%20eine%20Investition.",
    "wa_label": "Erzählen Sie mir, was Sie suchen",
    "form_h2": "Vereinbaren Sie eine vertrauliche Beratung",
    "form_p": "Anzeigen allein reichen nicht. Erzählen Sie mir Ihr Ziel — Kauf, Investment oder Verkauf.",
    "step_note": "Zuerst: was brauchen Sie?",
    "intent_label": "Ihr Ziel",
    "intent1": "Kauf",
    "intent2": "Investment",
    "intent3": "Verkauf",
    "path_aria": "Wählen Sie Ihren Weg",
    "path_intro": "Wie kann ich helfen",
    "path1_label": "Hauptservice",
    "path1_p": "Persönliche Immobiliensuche — auch off-market. Auswahl, Besichtigungen, Verhandlung und Begleitung bis zum Notartermin.",
    "path1_cta": "Suche starten →",
    "path2_label": "Investoren",
    "path2_h": "Beratung für Investoren",
    "path2_p": "Renditeobjekte, Wertsteigerung, Wirtschaftlichkeitsanalyse — mit Verhandlungsunterstützung.",
    "path2_cta": "Investment analysieren →",
    "path3_label": "Verkäufer",
    "path3_h": "Bewertung und Verkauf",
    "path3_p": "Vorhanden, aber nicht dominant: Bewertung, Strategie und Vermarktung.",
    "path3_cta": "Analyse anfordern →",
    "buy_hub": "/de/haus-kaufen/",
    "serv_kicker": "Professionelle Leistungen",
    "serv_h2": "Ich verkaufe keine Anzeigen. Ich helfe bei besseren Entscheidungen.",
    "serv_p": "Schutz von Käufern und Investoren — von der Suche bis zum Notartermin.",
    "s1_p": "Hauptservice: maßgeschneiderte Immobiliensuche.",
    "s2_h": "Beratung für Investoren",
    "s2_p": "Chancen, Rendite und Wertsteigerung mit klaren Zahlen.",
    "s3_h": "Beratung für Immobilienkäufer",
    "s3_p": "Für Ersterwerb oder Wohnungswechsel — inkl. Abstimmungen mit Bank und Notar.",
    "s4_h": "Leistungen für Verkäufer",
    "s4_p": "Bewertung, Verkaufsstrategie und Vermarktung — nachrangig im Fokus.",
    "mid_kicker": "Beratung",
    "mid_h2": "Suchen wir gemeinsam die richtige Immobilie.",
    "mid_p": "Erzählen Sie mir, was Sie suchen — Wohnen oder Investment. Persönliche Antwort in 24 Stunden.",
    "cta": "Beratung vereinbaren",
    "mid_sec": "Provinz wählen →",
    "final_h2": "Vereinbaren Sie eine Beratung. Suchen wir gemeinsam die richtige Immobilie.",
    "final_p": "Analyse, Suche und Schutz bis zum Notartermin — ohne Portal-Improvisation.",
    "footer_swaps": [
        ("Zuerst die Analyse. Dann der Verkauf.", "Zuerst die Analyse. Dann die richtige Entscheidung."),
    ],
}

FR = {
    "agent_span": "Conseiller acheteurs et investisseurs · RE/MAX",
    "eyebrow": "Milan · Lombardie · Conseil immobilier",
    "h1": "Conseiller pour acheteurs et investisseurs immobiliers",
    "lead": "L'allié de ceux qui achètent un logement et de ceux qui investissent. <strong>Analyse avant l'achat</strong>, recherche personnalisée, contrôle documentaire et accompagnement jusqu'à l'acte.",
    "b1": "Property Finding — aussi hors marché",
    "b2": "Conseil dédié aux investisseurs",
    "b3": "Contrôle documentaire et négociation",
    "b4": "Accompagnement jusqu'à l'acte — sans engagement initial",
    "wa": "https://wa.me/393514581993?text=Bonjour%20Maurizio%2C%20je%20souhaite%20une%20consultation.%20Je%20cherche%20une%20maison%20%2F%20un%20investissement.",
    "wa_label": "Parlez-moi de votre recherche",
    "form_h2": "Réservez une consultation confidentielle",
    "form_p": "Feuilleter des annonces ne suffit pas. Parlez-moi de votre objectif — achat, investissement ou vente.",
    "step_note": "D'abord : de quoi avez-vous besoin ?",
    "intent_label": "Votre objectif",
    "intent1": "Achat",
    "intent2": "Investissement",
    "intent3": "Vente",
    "path_aria": "Choisissez votre parcours",
    "path_intro": "Comment puis-je vous aider",
    "path1_label": "Service principal",
    "path1_p": "Recherche personnalisée du bien idéal, aussi hors marché. Sélection, visites, négociation et coordination jusqu'à l'acte.",
    "path1_cta": "Commençons la recherche →",
    "path2_label": "Investisseurs",
    "path2_h": "Conseil pour investisseurs",
    "path2_p": "Opportunités locatives, valorisation, analyse économique — avec soutien en négociation.",
    "path2_cta": "Analysons votre investissement →",
    "path3_label": "Vendeurs",
    "path3_h": "Estimation et vente",
    "path3_p": "Présente mais non dominante : estimation, stratégie et commercialisation.",
    "path3_cta": "Demander une analyse →",
    "buy_hub": "/fr/acheter-maison/",
    "serv_kicker": "Services professionnels",
    "serv_h2": "Je ne vends pas des annonces. Je vous aide à mieux décider.",
    "serv_p": "Protection de l'acheteur et de l'investisseur — de la recherche à l'acte.",
    "s1_p": "Service principal : recherche personnalisée du bien idéal.",
    "s2_h": "Conseil pour investisseurs",
    "s2_p": "Opportunités, rendement et valorisation avec des chiffres clairs.",
    "s3_h": "Conseil pour acheteurs",
    "s3_p": "Premier achat ou changement de logement — coordination banque et notaire.",
    "s4_h": "Services pour vendeurs",
    "s4_p": "Estimation, stratégie et commercialisation — présentes mais secondaires.",
    "mid_kicker": "Conseil",
    "mid_h2": "Cherchons ensemble le bon bien.",
    "mid_p": "Parlez-moi de votre recherche — logement ou investissement. Réponse sous 24 h.",
    "cta": "Réserver une consultation",
    "mid_sec": "Choisir la province →",
    "final_h2": "Réservez une consultation. Cherchons ensemble le bon bien.",
    "final_p": "Analyse, recherche et protection jusqu'à l'acte — sans improvisation de portail.",
    "footer_swaps": [
        ("D'abord l'analyse. Ensuite la vente.", "D'abord l'analyse. Ensuite la bonne décision."),
    ],
}


def main() -> None:
    apply_locale(ROOT / "de/index.html", DE)
    apply_locale(ROOT / "fr/index.html", FR)
    print("Done.")


if __name__ == "__main__":
    main()
