"""Dynamic province-specific DE/FR replacements for seller pages."""

from __future__ import annotations

import re

from locales import city_label

# (Italian template with {city}, German with {city}, French with {city})
_DYNAMIC: list[tuple[str, str, str]] = [
    (
        "A {city} e provincia, vendere bene non è fortuna. È strategia.",
        "In {city} und Provinz ist gut verkaufen kein Glück — es ist Strategie.",
        "À {city} et en province, bien vendre n'est pas une question de chance — c'est une stratégie.",
    ),
    (
        "Prima di decidere, vuoi leggere il mercato reale della tua zona — {city} e provincia — e non muoverti a sensazione.",
        "Bevor Sie entscheiden, möchten Sie den realen Markt Ihrer Zone lesen — {city} und Provinz — und nicht nach Gefühl handeln.",
        "Avant de décider, vous voulez lire le marché réel de votre zone — {city} et province — et non pas agir sur l'émotion.",
    ),
    (
        "Ogni vendita ha criticità diverse. Il primo passo è capire cosa può rallentare, svalutare o valorizzare il tuo immobile a {city} e in provincia.",
        "Jeder Verkauf hat andere Herausforderungen. Der erste Schritt: verstehen, was Ihre Immobilie in {city} und Provinz verzögern, entwerten oder aufwerten kann.",
        "Chaque vente a ses enjeux. Première étape : comprendre ce qui peut ralentir, dévaloriser ou valoriser votre bien à {city} et en province.",
    ),
    (
        "Prima di firmare qualsiasi cosa, vuoi una strategia chiara, riservata e costruita sulla realtà del mercato a {city}.",
        "Bevor Sie etwas unterschreiben, möchten Sie eine klare, vertrauliche Strategie auf Basis des realen Marktes in {city}.",
        "Avant de signer quoi que ce soit, vous voulez une stratégie claire, confidentielle, fondée sur la réalité du marché à {city}.",
    ),
    (
        "o migliaia di euro nella trattativa. Prima della vendita, servono dati reali, metodo e posizionamento corretto.",
        "oder in der Verhandlung Tausende Euro. Vor dem Verkauf brauchen Sie echte Daten, Methode und die richtige Positionierung.",
        "ou des milliers d'euros en négociation. Avant de vendre, il faut des données réelles, une méthode et un positionnement juste.",
    ),
    (
        "Ti mostro il mercato reale della tua zona, le criticità dell'immobile e la strategia più adatta — prima ancora di parlare di incarico.",
        "Ich zeige Ihnen den realen Markt Ihrer Zone, die Risiken der Immobilie und die passende Strategie — bevor wir über ein Mandat sprechen.",
        "Je vous montre le marché réel de votre zone, les points sensibles du bien et la stratégie adaptée — avant tout mandat.",
    ),
    (
        "Definiamo prezzo, timing, comunicazione e profilo dell'acquirente più adatto alla tua zona e tipologia.",
        "Wir definieren Preis, Timing, Kommunikation und das passende Käuferprofil für Ihre Zone und Objekttyp.",
        "Nous définissons le prix, le timing, la communication et le profil acheteur adapté à votre zone et type de bien.",
    ),
    (
        "Brescia cambia zona per zona. Ogni mercato ha le sue regole.",
        "Brescia ändert sich von Zone zu Zone. Jeder Markt hat seine eigenen Regeln.",
        "Brescia change de zone en zone. Chaque marché a ses propres règles.",
    ),
    (
        "Domanda locale solida, acquirenti principalmente italiani. Ogni zona, piano e stato dell'immobile incide significativamente sul valore.",
        "Solide lokale Nachfrage, überwiegend italienische Käufer. Zone, Etage und Zustand beeinflussen den Wert erheblich.",
        "Demande locale solide, acheteurs principalement italiens. Zone, étage et état du bien influencent fortement la valeur.",
    ),
    (
        "Mesi online, poche visite, offerte basse: spesso il problema non è la casa, ma il posizionamento sbagliato per quella zona — che a {city} cambia significativamente da una micro-zona all'altra.",
        "Monate online, wenige Besichtigungen, niedrige Angebote: oft liegt es nicht an der Immobilie, sondern an der falschen Positionierung — in {city} ändert sich der Markt von Mikrozone zu Mikrozone.",
        "Mois en ligne, peu de visites, offres basses : souvent le problème n'est pas le bien, mais un mauvais positionnement — à {city}, le marché change nettement d'une micro-zone à l'autre.",
    ),
    (
        "Ogni vendita ha criticità diverse. Il primo passo è capire cosa può rallentare, svalutare o valorizzare il tuo immobile.",
        "Jeder Verkauf hat andere Herausforderungen. Der erste Schritt: verstehen, was Ihre Immobilie verzögern, entwerten oder aufwerten kann.",
        "Chaque vente a ses enjeux. Première étape : comprendre ce qui peut ralentir, dévaloriser ou valoriser votre bien.",
    ),
    (
        "Mesi online, poche visite, offerte basse: spesso il problema non è la casa, ma il posizionamento sbagliato per quella zona — che a {city} cambia significativamente tra centro, collina e pianura.",
        "Monate online, wenige Besichtigungen, niedrige Angebote: oft liegt es nicht an der Immobilie, sondern an der falschen Positionierung — in {city} ändert sich der Markt erheblich zwischen Zentrum, Hügel und Ebene.",
        "Mois en ligne, peu de visites, offres basses : souvent le problème n'est pas le bien, mais un mauvais positionnement — à {city}, le marché change nettement entre centre, collines et plaine.",
    ),
]

# Card 03 — «Hai ricevuto valutazioni troppo diverse» (province-specific tails)
_CARD03_TOWN1: dict[str, str] = {
    "como": "Cernobbio",
    "varese": "Busto Arsizio",
    "lecco": "Merate",
    "sondrio": "Tirano",
    "cremona": "Crema",
    "lodi": "Codogno",
    "mantova": "Suzzara",
    "pavia": "Vigevano",
}

_CARD03_STANDARD = (
    "Vuoi capire su quali dati si basa il prezzo e distinguere una stima seria da una promessa &mdash; specialmente quando le valutazioni variano tra {city} città, {town1} e i comuni in provincia.",
    "Sie möchten verstehen, worauf der Preis basiert, und eine seriöse Schätzung von einer leeren Zusage unterscheiden &mdash; besonders wenn die Bewertungen zwischen {city} Stadt, {town1} und Provinzgemeinden variieren.",
    "Vous voulez comprendre sur quelles données repose le prix et distinguer une estimation sérieuse d'une promesse &mdash; surtout quand les évaluations varient entre {city} ville, {town1} et les communes de province.",
)

_CARD03_MONZA = (
    "Vuoi capire su quali dati si basa il prezzo e distinguere una stima seria da una promessa &mdash; specialmente quando le valutazioni variano tra Monza, Seregno e i comuni in provincia.",
    "Sie möchten verstehen, worauf der Preis basiert, und eine seriöse Schätzung von einer leeren Zusage unterscheiden &mdash; besonders wenn die Bewertungen zwischen Monza, Seregno und Provinzgemeinden variieren.",
    "Vous voulez comprendre sur quelles données repose le prix et distinguer une estimation sérieuse d'une promesse &mdash; surtout quand les évaluations varient entre Monza, Seregno et les communes de province.",
)

_CARD03_BRESCIA = (
    "Vuoi capire su quali dati si basa il prezzo e distinguere una stima seria da una promessa &mdash; specialmente su immobili in zone turistiche.",
    "Sie möchten verstehen, worauf der Preis basiert, und eine seriöse Schätzung von einer leeren Zusage unterscheiden &mdash; besonders bei Immobilien in Tourismusgebieten.",
    "Vous voulez comprendre sur quelles données repose le prix et distinguer une estimation sérieuse d'une promesse &mdash; surtout pour les biens en zones touristiques.",
)

_ENTITY_MAP = (
    ("À", "&Agrave;"), ("à", "&agrave;"),
    ("È", "&Egrave;"), ("è", "&egrave;"),
    ("É", "&Eacute;"), ("é", "&eacute;"),
    ("Ì", "&Igrave;"), ("ì", "&igrave;"),
    ("Ò", "&Ograve;"), ("ò", "&ograve;"),
    ("Ù", "&Ugrave;"), ("ù", "&ugrave;"),
    ("—", "&mdash;"), ("·", "&middot;"),
)

_CURVY = (
    ("\u2019", "'"),
    ("\u2018", "'"),
    ("\u201c", '"'),
    ("\u201d", '"'),
)


def _to_entities(text: str) -> str:
    out = text
    for char, ent in _ENTITY_MAP:
        out = out.replace(char, ent)
    return out


def _text_variants(text: str) -> list[str]:
    seen: set[str] = set()
    variants = [text, _to_entities(text)]
    for src, dst in _CURVY:
        for base in list(variants):
            if src in base:
                v = base.replace(src, dst)
                variants.append(v)
            if dst in base:
                v = base.replace(dst, src)
                variants.append(v)
    out: list[str] = []
    for v in variants:
        if v not in seen:
            seen.add(v)
            out.append(v)
    return out


def _card03_template(slug: str) -> tuple[str, str, str] | None:
    if slug in _CARD03_TOWN1:
        return _CARD03_STANDARD
    if slug == "monza":
        return _CARD03_MONZA
    if slug == "brescia":
        return _CARD03_BRESCIA
    return None


def build_card03_pairs(lang: str, slug: str) -> list[tuple[str, str]]:
    tpl = _card03_template(slug)
    if not tpl:
        return []
    it_tpl, de_tpl, fr_tpl = tpl
    dst_tpl = de_tpl if lang == "de" else fr_tpl
    city_it = city_label(slug, "it")
    city = city_label(slug, lang)
    if slug in _CARD03_TOWN1:
        town1 = _CARD03_TOWN1[slug]
        it = it_tpl.format(city=city_it, town1=town1)
        dst = dst_tpl.format(city=city, town1=town1)
    else:
        it = it_tpl
        dst = dst_tpl
    pairs: list[tuple[str, str]] = []
    for it_var in _text_variants(it):
        pairs.append((it_var, dst))
    return pairs


def build_province_pairs(lang: str, slug: str) -> list[tuple[str, str]]:
    city_it = city_label(slug, "it")
    city = city_label(slug, lang)
    pairs: list[tuple[str, str]] = []
    for it_tpl, de_tpl, fr_tpl in _DYNAMIC:
        dst_tpl = de_tpl if lang == "de" else fr_tpl
        it = it_tpl.format(city=city_it)
        dst = dst_tpl.format(city=city)
        for it_var in _text_variants(it):
            pairs.append((it_var, dst))
    pairs.extend(build_card03_pairs(lang, slug))
    return sorted(pairs, key=lambda p: len(p[0]), reverse=True)


def apply_hero_regex(html: str, lang: str, slug: str) -> str:
    city_it = city_label(slug, "it")
    city = city_label(slug, lang)
    if lang == "de":
        repl = (
            f"Von {city} bis zu den Gemeinden der Provinz — jede Mikrozone hat eigene Dynamiken. "
            f"<strong>Ein falscher Preis kann Sie Monate auf dem Markt kosten</strong> "
            f"oder in der Verhandlung Tausende Euro. Vor dem Verkauf brauchen Sie echte Daten, Methode und die richtige Positionierung."
        )
    else:
        repl = (
            f"De {city} aux communes de la province, chaque micro-zone a ses dynamiques. "
            f"<strong>Un mauvais prix peut vous coûter des mois sur le marché</strong> "
            f"ou des milliers d'euros en négociation. Avant de vendre, il faut des données réelles, une méthode et un positionnement juste."
        )
    pattern = (
        rf"Da {re.escape(city_it)} ai comuni di provincia, ogni micro-zona ha dinamiche proprie\. "
        rf"<strong>Un prezzo sbagliato pu(?:ò|&ograve;) costarti mesi sul mercato</strong> "
        rf"o migliaia di euro nella trattativa\. Prima della vendita, servono dati reali, metodo e posizionamento corretto\."
    )
    return re.sub(pattern, repl, html, count=1)


# Milano / global polish — curly apostrophe variants included via _text_variants
FINAL_POLISH: list[tuple[str, str, str]] = [
    (
        "Provincia MI",
        "Provinz MI",
        "Province MI",
    ),
    (
        "No. L'analisi iniziale non crea obbligo di conferimento incarico. Serve a darti informazioni chiare per decidere meglio.",
        "Nein. Die Erstanalyse begründet keine Verpflichtung zur Beauftragung. Sie gibt Ihnen klare Informationen für eine bessere Entscheidung.",
        "Non. L'analyse initiale ne crée aucune obligation de mandat. Elle vous donne des informations claires pour mieux décider.",
    ),
    (
        "Prima dell'annuncio va capito chi è l'acquirente più probabile e cosa lo convince a fare un'offerta.",
        "Vor der Anzeige muss klar sein, wer der wahrscheinlichste Käufer ist und was ihn zum Angebot bewegt.",
        "Avant l'annonce, il faut identifier l'acheteur le plus probable et ce qui le convaincra de faire une offre.",
    ),
    (
        "La differenza resta nel modo in cui l'immobile viene analizzato, posizionato e presentato.",
        "Der Unterschied liegt darin, wie die Immobilie analysiert, positioniert und präsentiert wird.",
        "La différence réside dans la façon dont le bien est analysé, positionné et présenté.",
    ),
    (
        "La differenza resta nel modo in cui l'immobile viene analizzato, posizionato e presentato per la sua zona specifica.",
        "Der Unterschied liegt darin, wie die Immobilie analysiert, positioniert und präsentiert wird — für ihre konkrete Zone.",
        "La différence réside dans la façon dont le bien est analysé, positionné et présenté pour sa zone spécifique.",
    ),
    (
        "Durante le visite è stato fondamentale avere risposte tecniche chiare su documentazione, stato dell'immobile e strategia di vendita. Questo ha reso la trattativa più fluida.",
        "Bei Besichtigungen waren klare technische Antworten zu Dokumentation, Zustand und Verkaufsstrategie entscheidend. Das machte die Verhandlung reibungsloser.",
        "Lors des visites, des réponses techniques claires sur la documentation, l'état du bien et la stratégie de vente ont été essentielles. La négociation s'est déroulée plus facilement.",
    ),
    (
        "Per trasparenza e fiducia. La consulenza resta personale, ma l'affiliazione al network RE/MAX aggiunge riconoscibilità e supporto commerciale.",
        "Aus Transparenz und Vertrauen. Die Beratung bleibt persönlich, die RE/MAX-Affiliation verleiht aber Wiedererkennung und kommerzielle Unterstützung.",
        "Par transparence et confiance. Le conseil reste personnel, mais l'affiliation au réseau RE/MAX apporte reconnaissance et soutien commercial.",
    ),
    (
        "Prima della pubblicazione sono state individuate alcune criticità che avrebbero potuto rallentare la trattativa. Risolverle in anticipo ha migliorato la presentazione dell'immobile.",
        "Vor der Veröffentlichung wurden Schwachstellen erkannt, die die Verhandlung verzögert hätten. Die frühzeitige Lösung verbesserte die Präsentation der Immobilie.",
        "Avant la publication, des points sensibles susceptibles de ralentir la négociation ont été identifiés. Les résoudre à l'avance a amélioré la présentation du bien.",
    ),
]


def build_final_polish_pairs(lang: str) -> list[tuple[str, str]]:
    idx = 1 if lang == "de" else 2
    pairs: list[tuple[str, str]] = []
    for it, de, fr in FINAL_POLISH:
        dst = de if lang == "de" else fr
        for it_var in _text_variants(it):
            pairs.append((it_var, dst))
    return sorted(pairs, key=lambda p: len(p[0]), reverse=True)


def apply_market_links(html: str, lang: str, slug: str) -> str:
    city_it = city_label(slug, "it")
    city = city_label(slug, lang)
    if lang == "de":
        html = html.replace(
            f"Consulta i dati di mercato per {city_it} →",
            f"Marktdaten für {city} →",
        )
        html = html.replace(
            f"Consulta i valori OMI ufficiali per zona a {city_it} →",
            f"Offizielle OMI-Werte nach Zone in {city} →",
        )
        html = html.replace(
            "Consulta i valori OMI per zona →",
            f"OMI-Werte nach Zone in {city} →",
        )
    else:
        html = html.replace(
            f"Consulta i dati di mercato per {city_it} →",
            f"Données de marché pour {city} →",
        )
        html = html.replace(
            f"Consulta i valori OMI ufficiali per zona a {city_it} →",
            f"Valeurs OMI officielles par zone à {city} →",
        )
        html = html.replace(
            "Consulta i valori OMI per zona →",
            f"Valeurs OMI par zone à {city} →",
        )
    return html


def apply_province_all(html: str, lang: str, slug: str) -> str:
    for src, dst in build_province_pairs(lang, slug):
        if src in html:
            html = html.replace(src, dst)
    for src, dst in build_final_polish_pairs(lang):
        if src in html:
            html = html.replace(src, dst)
    html = apply_hero_regex(html, lang, slug)
    html = apply_market_links(html, lang, slug)
    return html
