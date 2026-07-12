#!/usr/bin/env python3
"""Generate DE/FR seller pages from Italian templates."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from buyer_provinces import LOMBARD_PROVINCES
from locales import seller_page_path

# Longest phrases first to avoid partial replacements.
PHRASES_DE = [
    ("Richiedi Analisi", "Analyse anfordern"),
    ("Richiedi analisi", "Analyse anfordern"),
    ("Scrivimi su WhatsApp", "Schreiben Sie mir auf WhatsApp"),
    ("Salta al contenuto", "Zum Inhalt springen"),
    ("Apri menu", "Menü öffnen"),
    ("Menu principale", "Hauptmenü"),
    ("Consulente RE/MAX", "RE/MAX-Berater"),
    ("Risposta entro 24h", "Antwort innerhalb von 24h"),
    ("Nessun obbligo di incarico", "Keine Verpflichtung zum Mandat"),
    ("Agente Immobiliare affiliato", "Immobilienberater affiliato"),
    ("Consulenza immobiliare", "Immobilienberatung"),
    ("Prima l'analisi. Poi la scelta giusta.", "Zuerst die Analyse. Dann die richtige Wahl."),
    ("Come funziona", "So funktioniert es"),
    ("Chi sono", "Über mich"),
    ("Vendere", "Verkaufen"),
    ("Comprare", "Kaufen"),
    ("Percorso", "Weg"),
    ("Info", "Info"),
    ("Mercato", "Markt"),
    ("Esperienze", "Erfahrungen"),
    ("Domande frequenti", "Häufige Fragen"),
    ("Pronto a vendere", "Bereit zu verkaufen"),
    ("Richiedi una consulenza", "Beratung anfordern"),
    ("Analisi OMI", "OMI-Analyse"),
    ("micro-zona", "Mikrozone"),
    ("rogito", "Notartermin"),
    ("trattativa", "Verhandlung"),
    ("immobile", "Immobilie"),
    ("casa", "Haus"),
    ("vendere", "verkaufen"),
    ("acquirente", "Käufer"),
    ("proprietario", "Eigentümer"),
    ("prezzo giusto", "richtiger Preis"),
    ("prezzo richiesto", "geforderten Preis"),
    ("Agenzia Entrate", "Steuerbehörde"),
    ("Dati ufficiali", "Offizielle Daten"),
    ("Rete internazionale", "Internationales Netzwerk"),
    ("RE/MAX Associati Real Estate", "RE/MAX Associati Real Estate"),
    ("Maurizio Piraino", "Maurizio Piraino"),
    ('lang="it"', 'lang="de"'),
    ("og:locale\" content=\"it_IT\"", "og:locale\" content=\"de_DE\""),
]

PHRASES_FR = [
    ("Richiedi Analisi", "Demander une analyse"),
    ("Richiedi analisi", "Demander une analyse"),
    ("Scrivimi su WhatsApp", "Écrivez-moi sur WhatsApp"),
    ("Salta al contenuto", "Aller au contenu"),
    ("Apri menu", "Ouvrir le menu"),
    ("Menu principale", "Menu principal"),
    ("Consulente RE/MAX", "Consultant RE/MAX"),
    ("Risposta entro 24h", "Réponse sous 24h"),
    ("Nessun obbligo di incarico", "Aucune obligation de mandat"),
    ("Agente Immobiliare affiliato", "Agent immobilier affilié"),
    ("Consulenza immobiliare", "Conseil immobilier"),
    ("Prima l'analisi. Poi la scelta giusta.", "D'abord l'analyse. Ensuite le bon choix."),
    ("Come funziona", "Comment ça marche"),
    ("Chi sono", "Qui je suis"),
    ("Vendere", "Vendre"),
    ("Comprare", "Acheter"),
    ("Percorso", "Parcours"),
    ("Info", "Info"),
    ("Mercato", "Marché"),
    ("Esperienze", "Expériences"),
    ("Domande frequenti", "Questions fréquentes"),
    ("Pronto a vendere", "Prêt à vendre"),
    ("Richiedi una consulenza", "Demander un conseil"),
    ("Analisi OMI", "Analyse OMI"),
    ("micro-zona", "micro-zone"),
    ("rogito", "acte notarié"),
    ("trattativa", "négociation"),
    ("immobile", "bien immobilier"),
    ("casa", "maison"),
    ("vendere", "vendre"),
    ("acquirente", "acheteur"),
    ("proprietario", "propriétaire"),
    ("prezzo giusto", "bon prix"),
    ("prezzo richiesto", "prix demandé"),
    ("Agenzia Entrate", "Agence des Entrées"),
    ("Dati ufficiali", "Données officielles"),
    ("Rete internazionale", "Réseau international"),
    ("RE/MAX Associati Real Estate", "RE/MAX Associati Real Estate"),
    ("Maurizio Piraino", "Maurizio Piraino"),
    ('lang="it"', 'lang="fr"'),
    ("og:locale\" content=\"it_IT\"", "og:locale\" content=\"fr_FR\""),
]


def apply_phrases(html: str, phrases: list[tuple[str, str]]) -> str:
    for src, dst in phrases:
        html = html.replace(src, dst)
    return html


def patch_canonical(html: str, lang: str, slug: str) -> str:
    from locales import seller_url
    url = f"https://mauriziopiraino.it{seller_url(slug, lang)}"
    html = re.sub(r'<link rel="canonical" href="[^"]+" */>', f'<link rel="canonical" href="{url}" />', html, count=1)
    html = re.sub(r'<meta property="og:url" content="[^"]+" */>', f'<meta property="og:url" content="{url}" />', html, count=1)
    return html


def generate(lang: str, phrases: list[tuple[str, str]]) -> int:
    count = 0
    for slug, _name, _en in LOMBARD_PROVINCES:
        src_rel = seller_page_path(slug, "it")
        dst_rel = seller_page_path(slug, lang)
        src = ROOT / src_rel
        if not src.exists():
            print(f"  skip missing source: {src_rel}")
            continue
        html = src.read_text(encoding="utf-8")
        html = apply_phrases(html, phrases)
        html = patch_canonical(html, lang, slug)
        dst = ROOT / dst_rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(html, encoding="utf-8")
        print(f"  wrote {dst_rel}")
        count += 1
    return count


def main() -> None:
    print("Generating DE seller pages...")
    generate("de", PHRASES_DE)
    print("Generating FR seller pages...")
    generate("fr", PHRASES_FR)
    print("Done.")


if __name__ == "__main__":
    main()
