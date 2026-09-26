#!/usr/bin/env python3
"""Slim DE/FR homes + vendere Milano; Maurizio-first IT buyer titles → ~8.5."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def remove_sections_by_class(html: str, class_names: list[str]) -> str:
    """Remove top-level <section> elements whose class token matches any name."""
    # Token match: avoid "market" deleting "seller-marketing-plan"
    alts = "|".join(rf"(?:^|\s){re.escape(c)}(?:\s|$)" for c in class_names)
    pattern = re.compile(
        rf'<section\b[^>]*\bclass="(?=[^"]*(?:{alts}))[^"]*"[^>]*>',
        re.I,
    )
    while True:
        m = pattern.search(html)
        if not m:
            break
        start = m.start()
        # walk to matching close, respecting nested sections
        i = m.end()
        depth = 1
        while depth and i < len(html):
            nxt_open = html.find("<section", i)
            nxt_close = html.find("</section>", i)
            if nxt_close == -1:
                break
            if nxt_open != -1 and nxt_open < nxt_close:
                depth += 1
                i = nxt_open + 8
            else:
                depth -= 1
                i = nxt_close + len("</section>")
        html = html[:start] + html[i:]
    return html


def slim_hero_benefits(html: str, lang: str) -> str:
    benefits = {
        "de": """\
          <ul class="seller-form-benefits">
            <li>Property Finding auf Maß</li>
            <li>Klare Zahlen vor dem Angebot</li>
            <li>Begleitung bis zum Notartermin</li>
          </ul>""",
        "fr": """\
          <ul class="seller-form-benefits">
            <li>Property Finding sur mesure</li>
            <li>Chiffres clairs avant l'offre</li>
            <li>Accompagnement jusqu'à l'acte</li>
          </ul>""",
    }
    if lang not in benefits:
        return html
    return re.sub(
        r"<ul class=\"seller-form-benefits\">.*?</ul>",
        benefits[lang],
        html,
        count=1,
        flags=re.S,
    )


PB_STRIP = {
    "de": """
    <section class="pb-strip" aria-label="Kurzüberblick">
      <div class="container pb-strip-grid">
        <div><strong>Maurizio</strong><span>Direkter Ansprechpartner, kein Callcenter</span></div>
        <div><strong>Methode</strong><span>Analyse vor Emotion</span></div>
        <div><strong>Netzwerk</strong><span>RE/MAX als Unterstützung, nicht im Zentrum</span></div>
        <div><strong>24h</strong><span>Persönliche Antwort</span></div>
      </div>
    </section>
""",
    "fr": """
    <section class="pb-strip" aria-label="En bref">
      <div class="container pb-strip-grid">
        <div><strong>Maurizio</strong><span>Référent direct, pas un call center</span></div>
        <div><strong>Méthode</strong><span>Analyse avant l'émotion</span></div>
        <div><strong>Réseau</strong><span>RE/MAX en soutien, pas au centre</span></div>
        <div><strong>24h</strong><span>Réponse personnelle</span></div>
      </div>
    </section>
""",
}

ABOUT = {
    "de": """
    <section class="about pb-about" id="metodo">
      <div class="container about-grid">
        <div class="portrait-card reveal">
          <img src="foto.jpg" loading="lazy" decoding="async" alt="Maurizio Piraino — Immobilienberater in Mailand" />
          <div class="portrait-info">
            <strong>Maurizio Piraino</strong>
            <span>Berater für Käufer und Investoren · Mailand</span>
            <div class="badges">
              <div class="badge">REA BS-639579</div>
              <div class="badge">Vermessungsingenieur</div>
              <div class="badge">RE/MAX Associati</div>
            </div>
          </div>
        </div>
        <div class="reveal">
          <div class="section-kicker">Über mich</div>
          <h2>Der Bezugspunkt sind Sie. Die Methode ist meine.</h2>
          <p class="lead">Ich arbeite in Mailand und der Lombardei als Berater für Käufer und Investoren. Die RE/MAX-Affiliation gibt mir Netzwerk und Werkzeuge: Verantwortung und Beziehung bleiben persönlich.</p>
          <div class="quote">„Ich begleite Sie nicht beim Kauf einer Anzeige. Ich helfe bei der besten Entscheidung.“</div>
          <div class="method-grid pb-method">
            <div class="card"><div class="num">1</div><h3>Zuhören</h3><p>Ziel, Budget, Timing — wir starten bei Ihnen.</p></div>
            <div class="card"><div class="num">2</div><h3>Suche</h3><p>Gezielte Auswahl, auch außerhalb der Portale.</p></div>
            <div class="card"><div class="num">3</div><h3>Schutz</h3><p>Dokumente, Angebot, Notar — ohne Überraschungen.</p></div>
          </div>
        </div>
      </div>
    </section>
""",
    "fr": """
    <section class="about pb-about" id="metodo">
      <div class="container about-grid">
        <div class="portrait-card reveal">
          <img src="foto.jpg" loading="lazy" decoding="async" alt="Maurizio Piraino — conseiller immobilier à Milan" />
          <div class="portrait-info">
            <strong>Maurizio Piraino</strong>
            <span>Conseiller acheteurs et investisseurs · Milan</span>
            <div class="badges">
              <div class="badge">REA BS-639579</div>
              <div class="badge">Géomètre</div>
              <div class="badge">RE/MAX Associati</div>
            </div>
          </div>
        </div>
        <div class="reveal">
          <div class="section-kicker">Qui je suis</div>
          <h2>Le point de référence, c'est vous. La méthode est la mienne.</h2>
          <p class="lead">J'opère à Milan et en Lombardie comme conseiller pour acheteurs et investisseurs. L'affiliation RE/MAX me donne réseau et outils : la responsabilité et la relation restent personnelles.</p>
          <div class="quote">« Je ne vous accompagne pas à acheter une annonce. Je vous aide à prendre la meilleure décision. »</div>
          <div class="method-grid pb-method">
            <div class="card"><div class="num">1</div><h3>Écoute</h3><p>Objectif, budget, délais — on part de vous.</p></div>
            <div class="card"><div class="num">2</div><h3>Recherche</h3><p>Sélection ciblée, aussi hors portails.</p></div>
            <div class="card"><div class="num">3</div><h3>Protection</h3><p>Documents, offre, acte — sans surprise.</p></div>
          </div>
        </div>
      </div>
    </section>
""",
}

SERVICES = {
    "de": """
    <section class="seller-services consultant-services pb-services" id="servizi">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Leistungen</div>
          <h2>Ich schütze Käufer und Investoren — von der Suche bis zum Notar.</h2>
          <p>Und bringe dieselbe Methode zu Verkäufern, wenn nötig.</p>
        </div>
        <div class="seller-services-grid">
          <article class="seller-service-card featured reveal">
            <div class="seller-service-num">01</div>
            <h3>Property Finding</h3>
            <p>Persönliche Suche, Besichtigungen, Verhandlung und Koordination bis zum Notartermin.</p>
          </article>
          <article class="seller-service-card reveal">
            <div class="seller-service-num">02</div>
            <h3>Investoren</h3>
            <p>Renditeobjekte und Wertsteigerung mit klarer Wirtschaftlichkeitsanalyse.</p>
          </article>
          <article class="seller-service-card reveal">
            <div class="seller-service-num">03</div>
            <h3>Immobilienkäufer</h3>
            <p>Ersterwerb oder Wechsel: Dokumentenprüfung und Verhandlungsunterstützung.</p>
          </article>
          <article class="seller-service-card secondary reveal">
            <div class="seller-service-num">04</div>
            <h3>Sie verkaufen</h3>
            <p>Maximum ohne Unterverkauf: Analyse, Strategie und Verkaufsplan. <a href="/de/haus-verkaufen-milan/" style="color:inherit;text-decoration:underline">Mehr erfahren →</a></p>
          </article>
        </div>
        <div class="seller-compare-table reveal pb-compare">
          <div class="seller-compare-row seller-compare-head">
            <span>Aspekt</span><span>Allein / Portal</span><span>Mit mir</span>
          </div>
          <div class="seller-compare-row"><span>Suche</span><span class="no">Nur öffentliche Anzeigen</span><span class="yes">Auch off-market</span></div>
          <div class="seller-compare-row"><span>Dokumente</span><span class="no">Auf eigenes Risiko</span><span class="yes">Prüfung vor dem Angebot</span></div>
          <div class="seller-compare-row"><span>Preis</span><span class="no">Emotion</span><span class="yes">Strukturierte Verhandlung</span></div>
        </div>
      </div>
    </section>
""",
    "fr": """
    <section class="seller-services consultant-services pb-services" id="servizi">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Services</div>
          <h2>Je protège acheteurs et investisseurs, de la recherche à l'acte.</h2>
          <p>Et j'apporte la même méthode à ceux qui vendent, quand il le faut.</p>
        </div>
        <div class="seller-services-grid">
          <article class="seller-service-card featured reveal">
            <div class="seller-service-num">01</div>
            <h3>Property Finding</h3>
            <p>Recherche personnalisée, visites, négociation et coordination jusqu'à l'acte.</p>
          </article>
          <article class="seller-service-card reveal">
            <div class="seller-service-num">02</div>
            <h3>Investisseurs</h3>
            <p>Opportunités de rendement et valorisation avec analyse claire.</p>
          </article>
          <article class="seller-service-card reveal">
            <div class="seller-service-num">03</div>
            <h3>Acheteurs</h3>
            <p>Première maison ou changement : contrôle documentaire et soutien en négociation.</p>
          </article>
          <article class="seller-service-card secondary reveal">
            <div class="seller-service-num">04</div>
            <h3>Vous vendez</h3>
            <p>Obtenir le maximum sans brader : analyse, stratégie et plan de vente. <a href="/fr/vendre-maison-milan/" style="color:inherit;text-decoration:underline">Découvrir →</a></p>
          </article>
        </div>
        <div class="seller-compare-table reveal pb-compare">
          <div class="seller-compare-row seller-compare-head">
            <span>Aspect</span><span>Seul / portail</span><span>Avec moi</span>
          </div>
          <div class="seller-compare-row"><span>Recherche</span><span class="no">Seules annonces publiques</span><span class="yes">Aussi hors marché</span></div>
          <div class="seller-compare-row"><span>Documents</span><span class="no">À votre risque</span><span class="yes">Vérification avant l'offre</span></div>
          <div class="seller-compare-row"><span>Prix</span><span class="no">Émotivité</span><span class="yes">Négociation structurée</span></div>
        </div>
      </div>
    </section>
""",
}

SITUATIONS = {
    "de": """
    <section class="situations pb-situations">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Dieser Weg ist für Sie, wenn</div>
          <h2>Schutz und Methode — keine Anzeigen zum Durchscrollen.</h2>
        </div>
        <div class="situations-grid pb-situations-grid">
          <article class="card reveal"><div class="num">01</div><h3>Sie suchen ein Zuhause</h3><p>Gefilterte Suche statt Monate mit falschen Anzeigen.</p></article>
          <article class="card reveal"><div class="num">02</div><h3>Sie investieren</h3><p>Zahlen zu Rendite und Risiko, bevor Kapital gebunden wird.</p></article>
          <article class="card reveal"><div class="num">03</div><h3>Sie fürchten, zu viel zu zahlen</h3><p>Daten, Dokumente und eine Verhandlung in Ihrem Interesse.</p></article>
        </div>
      </div>
    </section>
""",
    "fr": """
    <section class="situations pb-situations">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Ce parcours est pour vous si</div>
          <h2>Protection et méthode, pas des annonces à feuilleter.</h2>
        </div>
        <div class="situations-grid pb-situations-grid">
          <article class="card reveal"><div class="num">01</div><h3>Vous cherchez un logement</h3><p>Une recherche filtrée, pas des mois d'annonces inutiles.</p></article>
          <article class="card reveal"><div class="num">02</div><h3>Vous investissez</h3><p>Des chiffres sur rendement et risque avant d'engager le capital.</p></article>
          <article class="card reveal"><div class="num">03</div><h3>Vous craignez de payer trop</h3><p>Données, documents et négociation construite sur vos intérêts.</p></article>
        </div>
      </div>
    </section>
""",
}

TESTIMONIALS = {
    "de": """
    <section class="testimonials" id="recensioni">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Erfahrungen</div>
          <h2>Wer mit mir entschieden hat — nicht zufällig.</h2>
        </div>
        <div class="testimonial-grid pb-testimonials">
          <article class="testimonial-card reveal"><div class="stars">★★★★★</div><p>Monatelange Suche in Mailand. Gefilterte Recherche und Dokumentenprüfung vor dem Angebot haben Zeit und teure Fehler gespart.</p><div class="person"><div class="avatar">EL</div><div><strong>Käuferin · Porta Romana</strong><span>Ersterwerb · Mailand</span></div></div></article>
          <article class="testimonial-card reveal"><div class="stars">★★★★★</div><p>Für das Investment wollte ich klare Zahlen. Sachliche Analyse, kein Druck: Auswahl und Abschluss mit Bewusstsein.</p><div class="person"><div class="avatar">MR</div><div><strong>Investor · Navigli</strong><span>Renditeobjekt · Mailand</span></div></div></article>
          <article class="testimonial-card reveal"><div class="stars">★★★★★</div><p>Bei Besichtigungen klare technische Antworten zu Dokumenten und Risiken. Die Verhandlung war sicherer.</p><div class="person"><div class="avatar">SF</div><div><strong>Käuferin · Isola</strong><span>Wohnungswechsel · Mailand</span></div></div></article>
        </div>
      </div>
    </section>
""",
    "fr": """
    <section class="testimonials" id="recensioni">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Expériences</div>
          <h2>Ceux qui ont décidé avec moi, pas au hasard.</h2>
        </div>
        <div class="testimonial-grid pb-testimonials">
          <article class="testimonial-card reveal"><div class="stars">★★★★★</div><p>Des mois à chercher à Milan. Recherche filtrée et contrôle documentaire avant l'offre : moins de temps perdu et d'erreurs coûteuses.</p><div class="person"><div class="avatar">EL</div><div><strong>Acheteuse · Porta Romana</strong><span>Première maison · Milan</span></div></div></article>
          <article class="testimonial-card reveal"><div class="stars">★★★★★</div><p>Pour l'investissement, je voulais des chiffres clairs. Analyse sobre, sans pression : sélection et closing en conscience.</p><div class="person"><div class="avatar">MR</div><div><strong>Investisseur · Navigli</strong><span>Bien de rendement · Milan</span></div></div></article>
          <article class="testimonial-card reveal"><div class="stars">★★★★★</div><p>Lors des visites, réponses techniques claires sur documents et points critiques. La négociation a été plus sûre.</p><div class="person"><div class="avatar">SF</div><div><strong>Acheteuse · Isola</strong><span>Changement de logement · Milan</span></div></div></article>
        </div>
      </div>
    </section>
""",
}

FAQ = {
    "de": """
    <section class="faq pb-faq">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">FAQ</div>
          <h2>Häufige Fragen</h2>
        </div>
        <div class="faq-grid">
          <details open><summary>Sind Sie Makler oder Käuferberater?</summary><p>Ich bin Maurizio Piraino, RE/MAX-Immobilienberater. Ich begleite Käufer und Investoren — und auch Verkäufer, mit derselben Methode.</p></details>
          <details><summary>Was ist Property Finding?</summary><p>Die persönliche Immobiliensuche: Bedarf, Auswahl auch off-market, Besichtigungen, Verhandlung und Koordination bis zum Notar.</p></details>
          <details><summary>Verpflichtet die Erstberatung?</summary><p>Nein. Das erste Gespräch dient dazu zu klären, ob eine Zusammenarbeit Sinn ergibt.</p></details>
          <details><summary>Und wenn ich verkaufen muss?</summary><p>Fordern Sie eine vertrauliche Analyse an: realer Wert, Verkaufshemmnisse und Präsentation. <a href="/de/haus-verkaufen-milan/">Zur Verkaufsseite →</a></p></details>
          <details><summary>Was hat ValoreCasaTua.it damit zu tun?</summary><p>ValoreCasaTua ist das redaktionelle Portal (Guides und Preise). Hier finden Sie mich und die professionellen Leistungen.</p></details>
        </div>
      </div>
    </section>
""",
    "fr": """
    <section class="faq pb-faq">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">FAQ</div>
          <h2>Questions fréquentes</h2>
        </div>
        <div class="faq-grid">
          <details open><summary>Êtes-vous agent ou conseiller acheteurs ?</summary><p>Je suis Maurizio Piraino, agent immobilier affilié RE/MAX. Je suis acheteurs et investisseurs — et aussi les vendeurs, avec la même méthode.</p></details>
          <details><summary>Qu'est-ce que le Property Finding ?</summary><p>La recherche personnalisée du bien : besoins, sélection aussi hors marché, visites, négociation et coordination jusqu'à l'acte.</p></details>
          <details><summary>La première consultation crée-t-elle des obligations ?</summary><p>Non. Le premier échange sert à comprendre si travailler ensemble a du sens.</p></details>
          <details><summary>Et si je dois vendre ?</summary><p>Demandez une analyse confidentielle : valeur réelle, freins à la vente et présentation. <a href="/fr/vendre-maison-milan/">Page vente →</a></p></details>
          <details><summary>Quel lien avec ValoreCasaTua.it ?</summary><p>ValoreCasaTua est le portail éditorial (guides et prix). Ici vous me trouvez, moi, et les services professionnels.</p></details>
        </div>
      </div>
    </section>
""",
}

EDITORIAL = {
    "de": """
    <section class="editorial-bridge" aria-label="ValoreCasaTua">
      <div class="container">
        <div class="editorial-bridge-inner reveal">
          <div>
            <div class="section-kicker">Zwei Rollen, null Verwirrung</div>
            <h2>Ich schließe den Weg ab. ValoreCasaTua informiert.</h2>
            <p>Guides und Quadratmeterpreise bleiben auf dem redaktionellen Portal. Hier arbeiten Sie mit mir: Property Finding, Investoren und Verkauf bei Bedarf.</p>
          </div>
          <div class="editorial-bridge-actions">
            <a class="btn btn-red" href="#form">Beratung vereinbaren</a>
            <a class="btn btn-outline-dark" href="https://valorecasatua.it/" rel="noopener" target="_blank">ValoreCasaTua.it →</a>
          </div>
        </div>
      </div>
    </section>
""",
    "fr": """
    <section class="editorial-bridge" aria-label="ValoreCasaTua">
      <div class="container">
        <div class="editorial-bridge-inner reveal">
          <div>
            <div class="section-kicker">Deux rôles, zéro confusion</div>
            <h2>Je clôture le parcours. ValoreCasaTua informe.</h2>
            <p>Guides et prix au m² restent sur le portail éditorial. Ici vous travaillez avec moi : property finding, investisseurs et vente si besoin.</p>
          </div>
          <div class="editorial-bridge-actions">
            <a class="btn btn-red" href="#form">Réserver une consultation</a>
            <a class="btn btn-outline-dark" href="https://valorecasatua.it/" rel="noopener" target="_blank">ValoreCasaTua.it →</a>
          </div>
        </div>
      </div>
    </section>
""",
}

FINAL_CTA = {
    "de": """
    <section class="final-cta">
      <div class="container reveal">
        <h2>Sprechen wir darüber. Suchen wir gemeinsam die richtige Immobilie.</h2>
        <p>Wohnen oder Investment: Analyse, Suche und Schutz bis zum Notar — mit mir als einzigem Ansprechpartner.</p>
        <div class="hero-actions" style="justify-content:center">
          <a class="btn btn-red" href="#form">Beratung vereinbaren</a>
          <a class="btn btn-wa" href="https://wa.me/393514581993?text=Hallo%20Maurizio%2C%20ich%20m%C3%B6chte%20eine%20Beratung.%20Ich%20suche%20eine%20Immobilie%20%2F%20eine%20Investition.">WhatsApp</a>
        </div>
      </div>
    </section>
""",
    "fr": """
    <section class="final-cta">
      <div class="container reveal">
        <h2>Parlons-en. Cherchons ensemble le bon bien.</h2>
        <p>Logement ou investissement : analyse, recherche et protection jusqu'à l'acte — avec moi comme seul référent.</p>
        <div class="hero-actions" style="justify-content:center">
          <a class="btn btn-red" href="#form">Réserver une consultation</a>
          <a class="btn btn-wa" href="https://wa.me/393514581993?text=Bonjour%20Maurizio%2C%20je%20souhaite%20une%20consultation.%20Je%20cherche%20une%20maison%20%2F%20un%20investissement.">WhatsApp</a>
        </div>
      </div>
    </section>
""",
}


def replace_section_class(html: str, class_token: str, new_html: str) -> str:
    pattern = re.compile(
        rf"<section\b[^>]*\bclass=\"[^\"]*{re.escape(class_token)}[^\"]*\"[^>]*>",
        re.I,
    )
    m = pattern.search(html)
    if not m:
        print(f"  WARN: section {class_token} not found for replace")
        return html
    start = m.start()
    i = m.end()
    depth = 1
    while depth and i < len(html):
        nxt_open = html.find("<section", i)
        nxt_close = html.find("</section>", i)
        if nxt_close == -1:
            break
        if nxt_open != -1 and nxt_open < nxt_close:
            depth += 1
            i = nxt_open + 8
        else:
            depth -= 1
            i = nxt_close + len("</section>")
    return html[:start] + new_html.strip() + "\n" + html[i:]


def slim_home(path: Path, lang: str) -> None:
    html = path.read_text(encoding="utf-8")
    # Remove dense seller-centric blocks
    html = remove_sections_by_class(
        html,
        [
            "seller-stats-strip",
            "seller-includes",
            "seller-compare",
            "seller-zones",
            "seller-mid-cta",
            "network",
            # use class="market" via id mercato — bare "market" matches marketing-plan
            "steps",
        ],
    )
    html = slim_hero_benefits(html, lang)

    # Insert pb-strip after hero (before consultant-path)
    if 'class="pb-strip"' not in html:
        html = html.replace(
            '<section class="consultant-path"',
            PB_STRIP[lang].strip() + '\n\n    <section class="consultant-path"',
            1,
        )

    # Replace core blocks
    html = replace_section_class(html, "about", ABOUT[lang])
    html = replace_section_class(html, "seller-services", SERVICES[lang])
    html = replace_section_class(html, "situations", SITUATIONS[lang])
    html = replace_section_class(html, "testimonials", TESTIMONIALS[lang])
    html = replace_section_class(html, "faq", FAQ[lang])
    html = replace_section_class(html, "final-cta", FINAL_CTA[lang])

    # Insert editorial before final-cta
    if "editorial-bridge" not in html:
        html = html.replace(
            '<section class="final-cta"',
            EDITORIAL[lang].strip() + '\n\n    <section class="final-cta"',
            1,
        )

    # Slim path sell card copy
    if lang == "de":
        html = html.replace(
            "<p>Vorhanden, aber nicht dominant: Bewertung, Strategie und Vermarktung.</p>",
            "<p>Vertrauliche Analyse, Preisstrategie und Verkaufsplan.</p>",
        )
    if lang == "fr":
        html = html.replace(
            "<p>Présent mais non dominant : estimation, stratégie et commercialisation.</p>",
            "<p>Analyse confidentielle, stratégie de prix et plan de vente.</p>",
        )

    # CSS bump
    html = html.replace(
        "consultant-home.css?v=20260738", "consultant-home.css?v=20260739"
    )
    html = html.replace(
        "consultant-home.css?v=20260735", "consultant-home.css?v=20260739"
    )

    path.write_text(html, encoding="utf-8")
    n = len(re.findall(r"<section\b", html))
    print(f"  {path}: {n} sections")


SELLER_PB_STRIP = """
    <section class="pb-strip" aria-label="In sintesi">
      <div class="container pb-strip-grid">
        <div><strong>Maurizio</strong><span>Referente diretto per la vendita</span></div>
        <div><strong>Analisi</strong><span>Prezzo sulla micro-zona</span></div>
        <div><strong>Piano</strong><span>Marketing e staging se serve</span></div>
        <div><strong>0 €</strong><span>Analisi iniziale · nessun obbligo</span></div>
      </div>
    </section>
"""

SELLER_ABOUT = """
    <section class="about pb-about" id="metodo">
      <div class="container about-grid">
        <div class="portrait-card reveal">
          <img src="/foto.jpg" loading="lazy" decoding="async" alt="Maurizio Piraino — consulente immobiliare a Milano" />
          <div class="portrait-info">
            <strong>Maurizio Piraino</strong>
            <span>Consulente immobiliare · Milano</span>
            <div class="badges">
              <div class="badge">REA BS-639579</div>
              <div class="badge">Geometra</div>
              <div class="badge">RE/MAX Associati</div>
            </div>
          </div>
        </div>
        <div class="reveal">
          <div class="section-kicker">Chi sono</div>
          <h2>Prima l'analisi. Poi la vendita.</h2>
          <p class="lead">Opero a Milano con RE/MAX Associati Real Estate. La consulenza resta personale: l'affiliazione aggiunge rete, MLS e visibilità quando serve.</p>
          <div class="quote">“Un prezzo sbagliato non è sfortuna. È mancanza di metodo.”</div>
          <div class="method-grid pb-method">
            <div class="card"><div class="num">1</div><h3>Analisi</h3><p>Micro-zona, comparabili, criticità tecniche.</p></div>
            <div class="card"><div class="num">2</div><h3>Strategia</h3><p>Prezzo, timing, presentazione e target.</p></div>
            <div class="card"><div class="num">3</div><h3>Esecuzione</h3><p>Marketing, visite, trattativa fino al rogito.</p></div>
          </div>
        </div>
      </div>
    </section>
"""

SELLER_SERVICES = """
    <section class="seller-services consultant-services pb-services" id="servizi">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Percorso vendita</div>
          <h2>Dalla valutazione al rogito, senza improvvisare.</h2>
          <p>Stesso metodo che uso con chi compra — applicato a chi vende.</p>
        </div>
        <div class="seller-services-grid">
          <article class="seller-service-card featured reveal">
            <div class="seller-service-num">01</div>
            <h3>Valutazione e prezzo</h3>
            <p>Analisi riservata sulla micro-zona, non una stima automatica.</p>
          </article>
          <article class="seller-service-card reveal">
            <div class="seller-service-num">02</div>
            <h3>Piano di marketing</h3>
            <p>Promozione, rete RE/MAX e staging se serve — passo dopo passo.</p>
          </article>
          <article class="seller-service-card reveal">
            <div class="seller-service-num">03</div>
            <h3>Trattativa e rogito</h3>
            <p>Visite, offerte e chiusura con tutela documentale.</p>
          </article>
          <article class="seller-service-card secondary reveal">
            <div class="seller-service-num">04</div>
            <h3>Vendi per ricomprare</h3>
            <p>Ti seguo anche nella ricerca della nuova casa. <a href="#vendi-per-ricomprare" style="color:inherit;text-decoration:underline">Scopri →</a></p>
          </article>
        </div>
        <div class="seller-compare-table reveal pb-compare">
          <div class="seller-compare-row seller-compare-head">
            <span>Aspetto</span><span>Da solo / online</span><span>Con me</span>
          </div>
          <div class="seller-compare-row"><span>Prezzo</span><span class="no">Media generica</span><span class="yes">Micro-zona reale</span></div>
          <div class="seller-compare-row"><span>Documenti</span><span class="no">A rischio</span><span class="yes">Verifica prima</span></div>
          <div class="seller-compare-row"><span>Visibilità</span><span class="no">Solo portali</span><span class="yes">Rete RE/MAX + piano</span></div>
        </div>
      </div>
    </section>
"""


def slim_seller_milano() -> None:
    path = ROOT / "vendere-casa-milano/index.html"
    html = path.read_text(encoding="utf-8")
    html = remove_sections_by_class(
        html,
        [
            "seller-stats-strip",
            "seller-includes",
            "seller-compare",
            "seller-zones",
            "seller-mid-cta",
            "situations",
            "network",
            # use class="market" via id mercato — bare "market" matches marketing-plan
            "steps",
        ],
    )
    # pb-strip after dual-path
    if 'class="pb-strip"' not in html:
        # insert after dual-path section closes — before next section or marketing
        html = re.sub(
            r'(</section>\s*)(?=<section class="seller-marketing-plan"|<section class="seller-services")',
            r"\1" + SELLER_PB_STRIP + "\n",
            html,
            count=1,
        )
        if 'class="pb-strip"' not in html:
            html = html.replace(
                '<section class="seller-services',
                SELLER_PB_STRIP.strip() + '\n\n    <section class="seller-services',
                1,
            )

    html = replace_section_class(html, "about", SELLER_ABOUT)
    html = replace_section_class(html, "seller-services", SELLER_SERVICES)

    # titles
    html = html.replace(
        "<title>Agente Immobiliare Milano | Valutazione Casa &middot; Piraino</title>",
        "<title>Maurizio Piraino | Piano di vendita · Milano</title>",
        1,
    )
    html = html.replace(
        'content="Agente Immobiliare affiliato RE/MAX Milano | Valutazione Casa"',
        'content="Maurizio Piraino | Piano di vendita · Milano"',
        1,
    )
    html = html.replace(
        "consultant-home.css?v=20260738", "consultant-home.css?v=20260739"
    )

    # slim hero benefits if still 4 long items
    html = re.sub(
        r"<ul class=\"seller-form-benefits\">.*?</ul>",
        """<ul class="seller-form-benefits">
            <li>Analisi riservata, nessun obbligo</li>
            <li>Strategia di prezzo sulla micro-zona</li>
            <li>Piano marketing e staging se serve</li>
          </ul>""",
        html,
        count=1,
        flags=re.S,
    )

    path.write_text(html, encoding="utf-8")
    print(f"  seller milano: {len(re.findall(r'<section\\b', html))} sections")


CITY_TITLES = {
    "milano": "Milano",
    "bergamo": "Bergamo",
    "brescia": "Brescia",
    "como": "Como",
    "cremona": "Cremona",
    "lecco": "Lecco",
    "lodi": "Lodi",
    "mantova": "Mantova",
    "monza": "Monza e Brianza",
    "pavia": "Pavia",
    "sondrio": "Sondrio",
    "varese": "Varese",
}


def fix_it_buyer_titles() -> None:
    hub = ROOT / "comprare-casa/index.html"
    t = hub.read_text(encoding="utf-8")
    t = re.sub(
        r"<title>[^<]+</title>",
        "<title>Maurizio Piraino | Comprare casa in Lombardia</title>",
        t,
        count=1,
    )
    t = re.sub(
        r'(property="og:title" content=")[^"]+"',
        r'\1Maurizio Piraino | Comprare casa in Lombardia"',
        t,
        count=1,
    )
    hub.write_text(t, encoding="utf-8")
    print("  hub titles")

    for slug, city in CITY_TITLES.items():
        path = ROOT / f"comprare-casa-{slug}/index.html"
        if not path.exists():
            continue
        t = path.read_text(encoding="utf-8")
        title = f"Maurizio Piraino | Consulenza acquirenti · {city}"
        t = re.sub(r"<title>[^<]+</title>", f"<title>{title}</title>", t, count=1)
        t = re.sub(
            r'(property="og:title" content=")[^"]+"',
            rf'\1{title}"',
            t,
            count=1,
        )
        path.write_text(t, encoding="utf-8")
        print(f"  {path.name}")


def main() -> None:
    print("Slim DE home")
    slim_home(ROOT / "de/index.html", "de")
    print("Slim FR home")
    slim_home(ROOT / "fr/index.html", "fr")
    print("Slim vendere Milano")
    slim_seller_milano()
    print("IT buyer titles")
    fix_it_buyer_titles()
    print("done")


if __name__ == "__main__":
    main()
