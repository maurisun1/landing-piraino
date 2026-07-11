#!/usr/bin/env python3
"""Patch and generate buyer landing pages."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from buyer_provinces import (
    DEFAULT_BUDGET_PROVINCE,
    DEFAULT_FAQ_WORK_A_IT,
    DEFAULT_FAQ_WORK_IT,
    DEFAULT_BUYER_TESTIMONIALS_EN,
    DEFAULT_BUYER_TESTIMONIALS_IT,
    DEFAULT_FORM_BENEFITS_IT,
    DEFAULT_HERO_LIST_IT,
    DEFAULT_PAIN_IT,
    DEFAULT_STATS_IT,
    DEFAULT_TRUST_IT,
    ABOUT_AGENCY_IT,
    ABOUT_AGENCY_EN,
    FOOTER_AFFILIATION_EN,
    FOOTER_AFFILIATION_IT,
    LOMBARD_PROVINCES,
    MILANO_BUDGET,
    NEW_PROVINCES,
    OMI_LINKS,
    SELLER_LINKS,
    seller_link_for,
)

ROOT = Path(__file__).resolve().parents[2]
STYLE_TEMPLATE = ROOT / "comprare-casa-bergamo" / "index.html"

COMMON = {
    "formspree": "https://formspree.io/f/mvzlgeqb",
    "wa": "393514581993",
    "email": "maurizio.piraino@remax.it",
    "instagram": "https://www.instagram.com/mauriziopiraino.immobiliare",
    "phone": "+39 351 458 1993",
    "rea": "REA BS-639579",
    "piva": "P.IVA 14597560961",
    "foto": "/foto.jpg",
}

PAGES = [
    {
        "path": "comprare-casa-bergamo/index.html",
        "lang": "it",
        "hero_img": "/bergamo.jpg",
        "city": "Bergamo",
        "city_slug": "bergamo",
        "omi": "/guida-prezzi-mq-bergamo/",
        "seller_link": "/bergamo/",
        "lang_link": "/en/buy-home-bergamo/",
        "lang_label": "EN",
        "form_hidden": "Comprare casa Bergamo - acquirente",
        "form_subject": "Richiesta acquirente - Bergamo",
        "datalist_id": "zoneBG",
        "datalist": [
            "Bergamo Città Alta", "Bergamo Città Bassa", "Dalmine / Osio",
            "Seriate / Scanzorosciate", "Valle Seriana", "Valle Brembana",
            "Treviglio / Romano di Lombardia", "Altra zona provincia Bergamo",
        ],
        "budget": [
            ("", "Preferisco non indicarlo"),
            ("150000", "Fino a 150.000 €"),
            ("150000-250000", "150.000 - 250.000 €"),
            ("250000-400000", "250.000 - 400.000 €"),
            ("400000-600000", "400.000 - 600.000 €"),
            ("600000+", "Oltre 600.000 €"),
        ],
        "zone_placeholder": "Es. Città Alta, Seriate, Treviglio...",
        "msg_placeholder": "Es. cerco trilocale in Città Bassa, casa in Valle Seriana, max 2° piano...",
        "footer_geo": "Bergamo · Città Alta · Valle Seriana · Provincia",
        "wa_text": "Ciao Maurizio, sto cercando casa a Bergamo e vorrei una consulenza acquirente.",
        "market": [
            ("Bergamo città", "Città Alta e Bassa", "Due mercati diversi: domanda solida, prezzi e tempi che cambiano strada per strada."),
            ("Valli", "Seriana e Brembana", "Qualità di vita, verde e prezzi spesso più accessibili del capoluogo — ma servono numeri giusti."),
            ("Provincia", "Cintura e pianura", "Dalmine, Seriate, Treviglio: chi esce da Milano cerca spazio, ma la concorrenza c'è lo stesso."),
        ],
        "quote": "A Bergamo, Città Alta e Città Bassa non seguono le stesse regole. Conoscere la micro-zona prima dell'offerta vale migliaia di euro.",
        "about_lead": "Agente RE/MAX con background da geometra. Conosco le dinamiche di Bergamo centro, valli e provincia — e ti dico se il prezzo ha senso, prima che tu lo scopra dopo il rogito.",
        "stats": [
            ("OMI", "Dati ufficiali Agenzia Entrate"),
            ("24h", "Risposta alla tua richiesta"),
            ("✓", "Nessun obbligo di incarico"),
            ("RE/MAX", "Rete internazionale"),
        ],
        "pain": [
            ("01", "Hai paura di pagare troppo", "Vedi una casa che ti piace e non sai se il prezzo richiesto è realistico per quella strada."),
            ("02", "Perdi l'occasione per un'offerta sbagliata", "Mercato competitivo: un'offerta bassa ti esclude, una troppo alta ti costa per anni."),
            ("03", "Non hai tempo per decine di annunci", "Portali, visite, trattative: senza filtro perdi settimane su immobili che non erano per te."),
            ("04", "Temi problemi nascosti", "Difformità, documenti, vincoli: scoprirli dopo il rogito è troppo tardi — e costoso."),
        ],
        "hero_list": [
            "Analisi prezzo su dati OMI della tua zona",
            "Verifica tecnica prima dell'offerta",
            "Ricerca mirata, senza spam di annunci",
        ],
        "trust_row": [
            ("OMI", "Prezzo basato su dati ufficiali"),
            ("RE/MAX", "Accesso alla rete MLS"),
            ("Geometra", "Verifica tecnica reale"),
        ],
        "form_benefits": [
            "Ti richiamo entro 24 ore, nessun obbligo di incarico",
            "Analisi del prezzo giusto per la zona che cerchi",
            "Alert quando esce qualcosa davvero in linea",
            "Supporto in trattativa fino al rogito",
        ],
        "faq_work": "Lavori solo a Bergamo?",
        "faq_work_a": "Bergamo, valli e provincia sono il focus, ma seguo acquirenti anche su Milano e Brescia.",
    },
    {
        "path": "comprare-casa-brescia/index.html",
        "lang": "it",
        "hero_img": "/brescia.jpg",
        "city": "Brescia",
        "city_slug": "brescia",
        "omi": "/guida-prezzi-mq-brescia/",
        "seller_link": "/brescia/",
        "lang_link": "/en/buy-home-brescia/",
        "lang_label": "EN",
        "form_hidden": "Comprare casa Brescia - acquirente",
        "form_subject": "Richiesta acquirente - Brescia",
        "datalist_id": "zoneBS",
        "datalist": [
            "Brescia città", "Franciacorta", "Lago di Garda bresciano", "Lago d'Iseo",
            "Valle Trompia", "Valle Camonica", "Bassa bresciana", "Altra zona provincia Brescia",
        ],
        "budget": [
            ("", "Preferisco non indicarlo"),
            ("150000", "Fino a 150.000 €"),
            ("150000-250000", "150.000 - 250.000 €"),
            ("250000-400000", "250.000 - 400.000 €"),
            ("400000-600000", "400.000 - 600.000 €"),
            ("600000+", "Oltre 600.000 €"),
        ],
        "zone_placeholder": "Es. Franciacorta, Desenzano, centro Brescia...",
        "msg_placeholder": "Es. trilocale in Franciacorta, villa sul lago, budget max 350.000 €...",
        "footer_geo": "Brescia · Franciacorta · Lago di Garda · Lago d'Iseo",
        "wa_text": "Ciao Maurizio, sto cercando casa a Brescia e vorrei una consulenza acquirente.",
        "market": [
            ("Città", "Brescia centro", "Domanda stabile, prezzi che cambiano quartiere per quartiere."),
            ("Franciacorta", "Colline e borghi", "Mercato premium: serve sapere se il prezzo è allineato alla micro-zona."),
            ("Laghi", "Garda e Iseo", "Competizione alta, anche da acquirenti internazionali — l'analisi prima dell'offerta è decisiva."),
        ],
        "quote": "In Franciacorta o sul Garda, due case simili possono valere cifre molto diverse. La micro-zona decide — non l'emozione del momento.",
        "about_lead": "Seguo acquirenti su Brescia città, Franciacorta, laghi e valli. Con i dati OMI e la verifica tecnica ti aiuto a comprare al prezzo giusto, non a quello dell'annuncio.",
        "stats": [
            ("OMI", "Dati ufficiali Agenzia Entrate"),
            ("24h", "Risposta alla tua richiesta"),
            ("✓", "Nessun obbligo di incarico"),
            ("RE/MAX", "Rete internazionale"),
        ],
        "pain": [
            ("01", "Non sai se il prezzo sul lago è giusto", "Franciacorta e Garda hanno dinamiche premium: serve un confronto reale, non il prezzo richiesto."),
            ("02", "Competi con altri acquirenti", "Un'offerta mal calibrata ti fa perdere la casa — o ti lega a un prezzo troppo alto."),
            ("03", "Cerchi in zone molto diverse", "Città, colline, laghi: ogni area ha regole diverse e serve un filtro serio."),
            ("04", "Vuoi evitare sorprese tecniche", "Prima dell'offerta devi sapere se ci sono criticità urbanistiche o catastali."),
        ],
        "hero_list": [
            "Analisi OMI su città, laghi e Franciacorta",
            "Verifica documenti prima dell'offerta",
            "Selezione mirata, niente annunci a caso",
        ],
        "trust_row": [
            ("OMI", "Prezzo basato su dati ufficiali"),
            ("RE/MAX", "Accesso alla rete MLS"),
            ("Geometra", "Verifica tecnica reale"),
        ],
        "form_benefits": [
            "Risposta entro 24 ore, nessun obbligo di incarico",
            "Analisi prezzo per la zona che cerchi",
            "Avviso quando trovo qualcosa in linea",
            "Affiancamento in trattativa fino al rogito",
        ],
        "faq_work": "Lavori solo a Brescia?",
        "faq_work_a": "Brescia, Franciacorta, laghi e provincia sono il focus, ma seguo acquirenti anche su Milano e Bergamo.",
    },
    {
        "path": "comprare-casa-milano/index.html",
        "lang": "it",
        "hero_img": "/milano.jpg",
        "city": "Milano",
        "city_slug": "milano",
        "omi": "/guida-prezzi-mq-milano/",
        "seller_link": "/",
        "lang_link": "/en/buy-home-milan/",
        "lang_label": "EN",
        "form_hidden": "Comprare casa Milano - acquirente",
        "form_subject": "Richiesta acquirente - Milano",
        "datalist_id": "comuniMI",
        "datalist_file": "milano_datalist.html",
        "budget": [
            ("", "Preferisco non indicarlo"),
            ("200000", "Fino a 200.000 €"),
            ("200000-350000", "200.000 - 350.000 €"),
            ("350000-500000", "350.000 - 500.000 €"),
            ("500000-800000", "500.000 - 800.000 €"),
            ("800000+", "Oltre 800.000 €"),
        ],
        "zone_placeholder": "Es. Navigli, Sesto San Giovanni...",
        "msg_placeholder": "Es. trilocale luminoso con balcone, vicino metro, max piano 3...",
        "footer_geo": "Milano · Provincia · Navigli · Isola",
        "wa_text": "Ciao Maurizio, sto cercando casa a Milano e vorrei una consulenza acquirente.",
        "market": [
            ("Milano città", "Zone centrali", "Domanda alta, tempi rapidi: un prezzo sbagliato costa caro."),
            ("Provincia", "Comuni MI", "Più spazio, prezzi diversi — ma ogni comune ha la sua dinamica."),
            ("Investimento", "Location e servizi", "Metro, scuole, riqualificazioni: il valore reale non è solo nei mq."),
        ],
        "quote": "A Milano il prezzo giusto cambia da una strada all'altra. L'analisi OMI sulla micro-zona vale più di dieci visite a caso.",
        "about_lead": "Milano è veloce e competitiva. Ti aiuto a capire se un immobile vale davvero il prezzo richiesto, a muoverti con tempismo e a non scoprire problemi dopo la proposta.",
        "stats": [
            ("OMI", "Dati ufficiali Agenzia Entrate"),
            ("24h", "Risposta alla tua richiesta"),
            ("✓", "Nessun obbligo di incarico"),
            ("RE/MAX", "Rete internazionale"),
        ],
        "pain": [
            ("01", "Perdi casa per pochi minuti", "Mercato veloce: senza numeri giusti arrivi tardi o offri troppo."),
            ("02", "Non capisci se il prezzo è giusto", "Annunci e prezzi richiesti spesso non riflettono il valore reale della micro-zona."),
            ("03", "Sei sommerso dagli annunci", "Centinaia di listing: serve un filtro serio, non ore sui portali."),
            ("04", "Temi difformità o vincoli", "A Milano le verifiche prima dell'offerta evitano errori costosi al rogito."),
        ],
        "hero_list": [
            "Analisi OMI su Milano e provincia",
            "Verifica tecnica prima dell'offerta",
            "Accesso alla rete RE/MAX",
        ],
        "trust_row": [
            ("OMI", "Prezzo basato su dati ufficiali"),
            ("RE/MAX", "Accesso alla rete MLS"),
            ("Geometra", "Verifica tecnica reale"),
        ],
        "form_benefits": [
            "Risposta entro 24 ore, nessun obbligo di incarico",
            "Analisi prezzo per zona e tipologia",
            "Alert su immobili davvero rilevanti",
            "Supporto in trattativa fino al rogito",
        ],
        "faq_work": "Lavori solo a Milano?",
        "faq_work_a": "Milano e provincia sono il cuore, ma seguo acquirenti anche su Brescia e Bergamo.",
    },
]


def t(cfg, key, it, en):
    if cfg["lang"] == "en":
        return en
    return it


def province_urls(slug, lang):
    en_slug = "milan" if slug == "milano" else slug
    if lang == "en":
        return f"/en/buy-home-{en_slug}/"
    return "/comprare-casa-milano/" if slug == "milano" else f"/comprare-casa-{slug}/"


def footer_links(cfg):
    slug = cfg["city_slug"]
    is_en = cfg["lang"] == "en"
    parts = []
    for s, it_name, en_name in LOMBARD_PROVINCES:
        name = en_name if is_en else it_name
        url = province_urls(s, cfg["lang"])
        if s == slug:
            parts.append(f"<strong>{name}</strong>")
        else:
            parts.append(f'<a href="{url}" style="color:inherit;text-decoration:underline">{name}</a>')
    buy_label = "Buy" if is_en else "Comprare"
    sell_label = "Selling instead?" if is_en else "Vuoi vendere?"
    sell_map = {
        "milano": ("Milan seller analysis", "Analisi vendita Milano"),
        "brescia": ("Seller analysis Brescia", "Analisi vendita Brescia"),
        "bergamo": ("Seller analysis Bergamo", "Analisi vendita Bergamo"),
    }
    st = sell_map.get(slug, ("Seller advisory", "Consulenza vendita"))
    st = st[1] if cfg["lang"] == "it" else st[0]
    joined = " · ".join(parts)
    return (
        f'{sell_label} <a href="{cfg["seller_link"]}" style="color:inherit;text-decoration:underline">{st}</a> '
        f'· {buy_label}: {joined} · '
        f'<a href="/privacy/" style="color:inherit;text-decoration:underline">Privacy</a>'
    )


def build_body(cfg):
    lang = cfg["lang"]
    is_en = lang == "en"
    brand = t(cfg, "brand",
              "Maurizio Piraino <span>·</span> Agente Immobiliare affiliato RE/MAX",
              "Maurizio Piraino <span>·</span> RE/MAX Real Estate Agent")
    topbar_left = t(cfg, "topbar",
                    f'Consulenza acquirenti <strong>RE/MAX</strong> · {cfg["city"]} · Risposta entro 24h',
                    f'Buyer advisory <strong>RE/MAX</strong> · {cfg["city"]} · Reply within 24 hours')
    topbar_wa = t(cfg, "topbar_wa", "Scrivimi su WhatsApp", "Message me on WhatsApp")
    nav_method = t(cfg, "nav", "Metodo", "Method")
    nav_remax = "RE/MAX"
    nav_omi = t(cfg, "nav_omi", "Prezzi OMI", "OMI prices")
    nav_cta = t(cfg, "nav_cta", "Dimmi cosa cerchi", "Tell me what you need")
    kicker = t(cfg, "kicker", f'Comprare casa a {cfg["city"]}', f'Buy a home in {cfg["city"]}')
    h1 = t(cfg, "h1",
           f'Comprare bene a {cfg["city"]} non è trovare una casa.<br>È non pagarla troppo.',
           f'Buying well in {cfg["city"]} is not about finding a home.<br>It is about not overpaying.')
    leads = {
        "bergamo": (
            "A Bergamo e provincia — Città Alta, Città Bassa, valli e comuni di cintura — ogni micro-mercato ha regole diverse. È facile pagare più del dovuto o comprare con problemi nascosti. Il mio ruolo è evitartelo.",
            "In Bergamo and its province — Città Alta, Città Bassa, valleys and surrounding towns — each micro-market has its own rules. It is easy to overpay or buy a home with hidden issues. My role is to help you avoid that.",
        ),
        "brescia": (
            "A Brescia e provincia — dal centro a Franciacorta, dal Garda all'Iseo — ogni zona ha dinamiche diverse. È facile pagare troppo, perdere un'occasione o comprare con criticità nascoste.",
            "In Brescia and its province — from the city centre to Franciacorta, from Lake Garda to Lake Iseo — each area has different dynamics. It is easy to overpay, lose a property, or buy a home with hidden issues.",
        ),
        "milano": (
            "Il mercato milanese è veloce e competitivo: è facile pagare troppo, arrivare tardi o comprare con problemi nascosti. Il mio ruolo è aiutarti a evitarlo.",
            "Milan's market is competitive and opaque: it is easy to overpay, lose a property to another buyer, or buy a home with hidden issues. My role is to help you avoid that.",
        ),
    }
    lead = cfg.get("lead") or leads[cfg["city_slug"]][1 if is_en else 0]
    lead_strong = t(cfg, "lead_strong", "Prima l'analisi. Poi la scelta giusta.", "Analysis first. Then the right choice.")
    cta1 = t(cfg, "cta1", "Dimmi cosa cerchi →", "Tell me what you need →")
    cta2 = t(cfg, "cta2", "Come funziona", "How it works")
    card_h = t(cfg, "card_h", "Registra la ricerca", "Register your search")
    card_p = t(cfg, "card_p", "Due minuti. Ti richiamo entro 24 ore.", "Two minutes. I will call you back within 24 hours.")
    card_cta = t(cfg, "card_cta", "Compila il modulo →", "Fill in the form →")
    card_wa = t(cfg, "card_wa", "Scrivimi su WhatsApp", "Message me on WhatsApp")

    pain_kicker = t(cfg, "pain_k", "Ti riconosci?", "Sound familiar?")
    pain_h2 = t(cfg, "pain_h", "Quattro situazioni frequenti — e come le evito", "Four common situations — and how I help you avoid them")

    adv_kicker = t(cfg, "adv_k", "Perché affidarti a un consulente", "Why work with an advisor")
    adv_h2 = t(cfg, "adv_h", "Quattro vantaggi reali quando compri con me", "Four real advantages when you buy with me")
    advantages = [
        (t(cfg, "a1t", "Il prezzo giusto", "The right price"),
         t(cfg, "a1p", "Analisi della micro-zona sui dati ufficiali OMI: sai se quella casa vale davvero il prezzo richiesto, prima di fare un'offerta.", "Micro-area analysis based on official OMI data: you know whether that home is truly worth the asking price before making an offer.")),
        (t(cfg, "a2t", "La rete RE/MAX", "The RE/MAX network"),
         t(cfg, "a2p", "A volte è possibile conoscere immobili in arrivo prima che finiscano sui portali.", "It is sometimes possible to see upcoming listings before they hit the portals.")),
        (t(cfg, "a3t", "La verifica prima di comprare", "Checks before you buy"),
         t(cfg, "a3p", "Conformità urbanistica e catastale, difformità, documenti: controlli fatti prima dell'acquisto.", "Urban planning and cadastral compliance, discrepancies, documents: checks done before the purchase.")),
        (t(cfg, "a4t", "Ricerca su misura", "Tailored search"),
         t(cfg, "a4p", "Mi dici cosa cerchi una volta sola. Ti avviso quando esce qualcosa davvero in linea.", "Tell me what you need once. I alert you when something truly relevant appears.")),
    ]
    icons = ["◎", "◈", "✓", "→"]

    trust_kicker = t(cfg, "trust_k", "Chi ti affianca", "Who supports you")
    trust_h2 = t(cfg, "trust_h", "Non un portale. Una persona con numeri e metodo.", "Not a portal. A person with data and method.")
    portrait_alt = t(cfg, "portrait_alt",
                     f'Maurizio Piraino Agente Immobiliare RE/MAX {cfg["city"]}',
                     f'Maurizio Piraino RE/MAX real estate agent {cfg["city"]}')
    portrait_sub = t(cfg, "portrait_sub",
                     f"Agente RE/MAX · {cfg['city']} e Provincia",
                     f"RE/MAX Agent · {cfg['city']} and province")
    badges = [
        t(cfg, "b1", "REA BS-639579", "REA BS-639579"),
        t(cfg, "b2", "Geometra", "Surveyor"),
        t(cfg, "b3", "Dati OMI", "OMI data"),
    ]

    market_kicker = t(cfg, "m_k", f"Mercato {cfg['city']}", f"{cfg['city']} market")
    market_h2 = t(cfg, "m_h", "Ogni zona ha regole diverse. I numeri vengono prima dell'emozione.", "Each area has different rules. Numbers come before emotion.")
    omi_text = cfg.get(
        "omi_text",
        t(cfg, "omi", "Consulta i valori OMI per zona →", "See OMI values by area →"),
    )

    steps_kicker = t(cfg, "s_k", "Come funziona", "How it works")
    steps_h2 = t(cfg, "s_h", "Tre passi. Nessuna pressione.", "Three steps. No pressure.")
    steps = [
        (t(cfg, "s1t", "Mi dici cosa cerchi", "You tell me what you need"),
         t(cfg, "s1p", "Zona, tipologia, budget e tempi. Bastano due minuti dal modulo.", "Area, property type, budget and timing. Two minutes using the form.")),
        (t(cfg, "s2t", "Analisi e selezione mirata", "Analysis and targeted selection"),
         t(cfg, "s2p", "Cerco, filtro e verifico prezzo e documenti. Ti propongo solo ciò che ha senso.", "I search, filter, verify fair price and documents. I only propose what truly makes sense.")),
        (t(cfg, "s3t", "Trattativa e acquisto", "Negotiation and purchase"),
         t(cfg, "s3p", "Ti affianco fino al rogito, perché tu compri al prezzo giusto e in sicurezza.", "I support you through negotiation and closing, so you buy at the right price and with confidence.")),
    ]

    faq_kicker = "FAQ"
    exp_kicker = t(cfg, "exp_k", "Esperienze", "Experiences")
    exp_h2 = t(cfg, "exp_h", "Chi ha comprato con metodo, non a caso.", "People who bought with a method, not by chance.")
    testimonials = cfg.get("testimonials") or (
        DEFAULT_BUYER_TESTIMONIALS_EN if is_en else DEFAULT_BUYER_TESTIMONIALS_IT
    )
    testimonial_cards = "".join(
        f'<article class="buyer-testimonial-card reveal"><div class="buyer-testimonial-stars">★★★★★</div>'
        f'<p>{text}</p><div class="buyer-testimonial-person"><div class="buyer-testimonial-avatar">{av}</div>'
        f'<div><strong>{title}</strong><span>{zone}</span></div></div></article>'
        for av, title, zone, text in testimonials
    )
    faq_h2 = t(cfg, "faq_h", "Le domande di chi compra", "Questions from buyers")
    faqs = [
        (t(cfg, "fq1", "Quanto costa il servizio per chi compra?", "How much does the buyer service cost?"),
         t(cfg, "fq1a", "Ne parliamo con chiarezza fin dal primo contatto. Il valore che ti faccio risparmiare evitando di pagare troppo conta più della provvigione.", "We discuss it clearly from the first contact. The value you save by avoiding overpaying matters more than the fee.")),
        (t(cfg, "fq2", "Mi fate vedere solo le vostre case?", "Do you only show your own listings?"),
         t(cfg, "fq2a", "No. L'obiettivo è trovare la casa giusta per te, non piazzarti un immobile.", "No. The goal is to find the right home for you, not to push a property.")),
        (t(cfg, "fq3", "Come fate a sapere se il prezzo è giusto?", "How do you know if the price is fair?"),
         t(cfg, "fq3a", "Con un'analisi della micro-zona basata sui dati ufficiali OMI e sulle caratteristiche reali dell'immobile.", "With a micro-area analysis based on official OMI data and the property's real characteristics.")),
        (t(cfg, "fq4", "Posso comprare prima di aver venduto la mia casa?", "Can I buy before selling my current home?"),
         t(cfg, "fq4a", "Sì, ed è frequente. Va pianificata con i tempi e i numeri giusti.", "Yes, and it is common. It needs to be planned with the right timing and numbers.")),
        (cfg["faq_work"], cfg["faq_work_a"]),
    ]

    form_h2 = t(cfg, "form_h", "Dimmi cosa cerchi", "Tell me what you need")
    form_p = t(cfg, "form_p", "Registra la tua ricerca: ti avviso quando trovo qualcosa in linea, e ti dico se il prezzo è giusto.", "Register your search: I will alert you when I find something relevant, and tell you whether the price is fair.")
    form_aside_h = t(cfg, "form_aside_h", "Compra con i numeri giusti, non con l'ansia.", "Buy with the right numbers, not with anxiety.")
    form_aside_p = t(cfg, "form_aside_p", "Compila il modulo: è il primo passo per una ricerca mirata e una valutazione seria del prezzo.", "Fill in the form: it is the first step toward a targeted search and a serious price assessment.")
    lbl_name = t(cfg, "lbl_name", "Nome *", "Name *")
    lbl_phone = t(cfg, "lbl_phone", "Telefono / WhatsApp *", "Phone / WhatsApp *")
    lbl_zone = t(cfg, "lbl_zone", "Zona o comune cercato *", "Area or municipality *")
    lbl_type = t(cfg, "lbl_type", "Tipologia", "Property type")
    lbl_budget = t(cfg, "lbl_budget", "Budget indicativo", "Indicative budget")
    lbl_time = t(cfg, "lbl_time", "Tempistiche", "Timing")
    lbl_msg = t(cfg, "lbl_msg", "Cosa è importante per te? (opzionale)", "What matters most to you? (optional)")
    type_opts = [
        ("", t(cfg, "type0", "Indifferente", "No preference")),
        ("bilocale", t(cfg, "type1", "Bilocale", "Two-bedroom")),
        ("trilocale", t(cfg, "type2", "Trilocale", "Three-bedroom")),
        ("quattro", t(cfg, "type3", "Quattro locali o più", "Four bedrooms or more")),
        ("villa", t(cfg, "type4", "Villa / indipendente", "Villa / detached house")),
        ("altro", t(cfg, "type5", "Altro", "Other")),
    ]
    time_opts = [
        ("", "—"),
        ("attivo", t(cfg, "time1", "Sto cercando attivamente", "Actively searching")),
        ("3-6", t(cfg, "time2", "Entro 3-6 mesi", "Within 3-6 months")),
        ("valuto", t(cfg, "time3", "Sto solo valutando", "Just exploring")),
    ]
    ph_name = "e.g. Marco Rossi" if is_en else "Es. Marco Rossi"
    ph_phone = "e.g. +39 348 000 0000" if is_en else "Es. 348 000 0000"
    privacy = t(cfg, "privacy",
                'Ho letto l\'<a href="/privacy/" style="color:inherit;text-decoration:underline">informativa privacy</a> e acconsento ad essere ricontattato.',
                'I have read the <a href="/privacy/" style="color:inherit;text-decoration:underline">privacy policy</a> and agree to be contacted.')
    submit = t(cfg, "submit", "Registra la mia ricerca →", "Register my search →")
    form_note = t(cfg, "form_note", "Risposta entro 24 ore · Nessun obbligo di incarico", "Reply within 24 hours · No obligation to appoint")

    final_h2 = t(cfg, "final_h", "Pronto a cercare casa con un metodo, non a caso?", "Ready to search with a method, not by chance?")
    final_p = t(cfg, "final_p", "Registra cosa cerchi. Ti richiamo entro 24 ore con un approccio chiaro — nessun obbligo di incarico.", "Tell me what you need. I will call you back within 24 hours with a clear approach — no obligation to appoint.")
    sticky = t(cfg, "sticky", "Dimmi cosa cerchi", "Tell me what you need")

    footer_strong = t(cfg, "footer_s", "Prima l'analisi. Poi la scelta giusta.", "Analysis first. Then the right choice.")
    footer_note = t(cfg, "footer_n",
                    "La consulenza iniziale non costituisce obbligo di conferimento incarico.",
                    "The initial consultation does not create an obligation to appoint an agent.")
    agent_label = t(cfg, "agent", "Agente Immobiliare affiliato RE/MAX", "RE/MAX Real Estate Agent")
    footer_affiliation = t(cfg, "footer_aff", FOOTER_AFFILIATION_IT, FOOTER_AFFILIATION_EN)
    agency_bio = t(cfg, "agency_bio", ABOUT_AGENCY_IT, ABOUT_AGENCY_EN)

    pain_cards = "".join(
        f'<article class="buyer-pain-card reveal"><div class="num">{n}</div><h3>{h}</h3><p>{p}</p></article>'
        for n, h, p in cfg["pain"]
    )
    adv_cards = "".join(
        f'<div class="adv-card reveal"><div class="buyer-adv-icon">{icon}</div><h3>{h}</h3><p>{p}</p></div>'
        for icon, (h, p) in zip(icons, advantages)
    )
    market_cards = "".join(
        f'<div class="buyer-market-card reveal"><span>{s}</span><h3>{h}</h3><p>{p}</p></div>'
        for s, h, p in cfg["market"]
    )
    stats = "".join(
        f'<div><strong>{a}</strong><span>{b}</span></div>' for a, b in cfg["stats"]
    )
    hero_list = "".join(f"<li>{x}</li>" for x in cfg["hero_list"])
    trust_row = "".join(
        f'<div class="trust"><strong>{a}</strong><span>{b}</span></div>' for a, b in cfg["trust_row"]
    )
    form_benefits = "".join(f"<li>{x}</li>" for x in cfg["form_benefits"])
    badge_html = "".join(f'<span class="buyer-badge">{b}</span>' for b in badges)
    type_select = "".join(f'<option value="{v}">{l}</option>' for v, l in type_opts)
    time_select = "".join(f'<option value="{v}">{l}</option>' for v, l in time_opts)
    budget_select = "".join(f'<option value="{v}">{l}</option>' for v, l in cfg["budget"])
    faq_html = "".join(
        f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs
    )
    steps_html = "".join(
        f'<div class="reveal"><div class="num" style="color:var(--gold);font-size:2rem;font-family:\'Playfair Display\',serif">{i}</div>'
        f'<h3>{h}</h3><p>{p}</p></div>'
        for i, (h, p) in enumerate(steps, 1)
    )

    wa_url = f"https://wa.me/{COMMON['wa']}?text={cfg['wa_text'].replace(' ', '%20').replace(',', '%2C').replace("'", '%27')}"
    wa_icon = (
        '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">'
        '<path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>'
        "</svg>"
    )
    menu_label = "Open menu" if is_en else "Apri menu"
    aria_nav = "Main menu" if is_en else "Menu principale"
    wa_topbar = "WhatsApp"
    wa_nav = topbar_wa
    wa_short = "WA"

    return f"""  <div class="topbar">
    <div class="container topbar-inner">
      <div class="topbar-tagline">{topbar_left}</div>
      <a class="topbar-wa topbar-wa-desktop" href="{wa_url}">{wa_icon} {wa_topbar}</a>
    </div>
  </div>
  <header class="site-header">
    <div class="container site-nav">
      <a class="brand" href="/">{brand}</a>
      <div class="site-nav-actions">
        <a class="btn btn-wa nav-wa-compact" href="{wa_url}" aria-label="WhatsApp">{wa_icon}<span class="nav-wa-label">{wa_short}</span></a>
        <button type="button" class="nav-toggle" aria-label="{menu_label}" aria-expanded="false" aria-controls="site-nav-panel">
          <span class="nav-toggle-bar"></span>
          <span class="nav-toggle-bar"></span>
          <span class="nav-toggle-bar"></span>
        </button>
      </div>
      <div class="nav-panel" id="site-nav-panel">
        <nav class="nav-links" aria-label="{aria_nav}">
          <a href="#metodo">{nav_method}</a>
          <a href="#remax">{nav_remax}</a>
          <a href="{cfg['omi']}">{nav_omi}</a>
          <a href="{cfg['lang_link']}" class="lang-link">{cfg['lang_label']}</a>
          <a class="btn btn-red nav-cta" href="#contatto">{nav_cta}</a>
        </nav>
      </div>
      <div class="nav-backdrop" hidden></div>
    </div>
  </header>

  <main id="main">
    <section class="buyer-hero-pro">
      <img class="buyer-hero-img" src="{cfg['hero_img']}" alt="{cfg['city']}" width="1920" height="1080" fetchpriority="high" decoding="async" />
      <div class="container buyer-hero-pro-grid">
        <div class="buyer-hero-pro-copy reveal">
          <span class="section-kicker" style="color:var(--gold)">{kicker}</span>
          <h1>{h1}</h1>
          <p class="lead">{lead} <strong style="color:#fff">{lead_strong}</strong></p>
          <div class="hero-actions" style="margin-top:30px">
            <a class="btn btn-red" href="#contatto">{cta1}</a>
            <a class="btn btn-outline" href="#come">{cta2}</a>
          </div>
          <div class="buyer-trust-row">{trust_row}</div>
        </div>
        <aside class="buyer-hero-card reveal">
          <h2>{card_h}</h2>
          <p>{card_p}</p>
          <ul class="buyer-hero-list">{hero_list}</ul>
          <div class="hero-actions">
            <a class="btn btn-red" href="#contatto">{card_cta}</a>
            <a class="btn btn-outline" href="{wa_url}">{card_wa}</a>
          </div>
        </aside>
      </div>
    </section>

    <section class="buyer-stats-strip">
      <div class="container buyer-stats-grid">{stats}</div>
    </section>

    <section class="buyer-pain">
      <div class="container">
        <div class="section-head"><span class="section-kicker">{pain_kicker}</span>
        <h2 style="font-family:'Playfair Display',serif;font-size:clamp(26px,3.5vw,38px);margin:10px 0 0">{pain_h2}</h2></div>
        <div class="buyer-pain-grid">{pain_cards}</div>
      </div>
    </section>

    <section style="background:var(--cream);padding:74px 0">
      <div class="container">
        <div class="section-head"><span class="section-kicker">{adv_kicker}</span>
        <h2 style="font-family:'Playfair Display',serif;font-size:clamp(26px,3.5vw,38px);margin:10px 0 0">{adv_h2}</h2></div>
        <div class="adv-grid">{adv_cards}</div>
      </div>
    </section>

    <section id="metodo" class="buyer-trust-block">
      <div class="container buyer-trust-grid">
        <div class="buyer-portrait reveal">
          <img src="{COMMON['foto']}" loading="lazy" decoding="async" alt="{portrait_alt}" />
          <div class="buyer-portrait-meta">
            <strong>Maurizio Piraino</strong>
            <span>{portrait_sub}</span>
            <div class="buyer-badges">{badge_html}</div>
          </div>
        </div>
        <div class="reveal">
          <span class="section-kicker">{trust_kicker}</span>
          <h2 style="font-family:'Playfair Display',serif;font-size:clamp(26px,3.5vw,38px);margin:10px 0 14px">{trust_h2}</h2>
          <p class="lead" style="margin:0 0 12px">{agency_bio}</p>
          <p class="lead" style="margin:0 0 8px">{cfg['about_lead']}</p>
          <blockquote class="buyer-quote">{cfg['quote']}</blockquote>
        </div>
      </div>
    </section>

    <section id="remax" class="buyer-market">
      <div class="container">
        <div class="section-head"><span class="section-kicker" style="color:var(--gold)">{market_kicker}</span>
        <h2 style="font-family:'Playfair Display',serif;font-size:clamp(26px,3.5vw,38px);margin:10px 0 0;color:#fff">{market_h2}</h2></div>
        <div class="buyer-market-grid">{market_cards}</div>
        <p style="text-align:center"><a class="buyer-omi-link" href="{cfg['omi']}">{omi_text}</a></p>
      </div>
    </section>

    <section id="come" class="steps" style="padding:74px 0">
      <div class="container">
        <div class="section-head"><span class="section-kicker" style="color:var(--gold)">{steps_kicker}</span>
        <h2 style="font-family:'Playfair Display',serif;font-size:clamp(26px,3.5vw,38px);margin:10px 0 0">{steps_h2}</h2></div>
        <div class="steps-buy">{steps_html}</div>
      </div>
    </section>

    <section id="esperienze" class="buyer-testimonials">
      <div class="container">
        <div class="section-head"><span class="section-kicker">{exp_kicker}</span>
        <h2 style="font-family:'Playfair Display',serif;font-size:clamp(26px,3.5vw,38px);margin:10px 0 0">{exp_h2}</h2></div>
        <div class="buyer-testimonial-grid">{testimonial_cards}</div>
      </div>
    </section>

    <section style="background:var(--cream);padding:74px 0">
      <div class="container">
        <div class="section-head"><span class="section-kicker">{faq_kicker}</span>
        <h2 style="font-family:'Playfair Display',serif;font-size:clamp(26px,3.5vw,38px);margin:10px 0 0">{faq_h2}</h2></div>
        <div class="faq-buy">{faq_html}</div>
      </div>
    </section>

    <section id="contatto" class="buyer-form-section" style="--buyer-city-bg: url('{cfg['hero_img']}')">
      <div class="container buyer-form-layout">
        <div class="buyer-form-aside reveal">
          <h2>{form_aside_h}</h2>
          <p>{form_aside_p}</p>
          <ul class="buyer-form-benefits">{form_benefits}</ul>
          <a class="btn btn-wa buyer-form-wa" href="{wa_url}">{wa_icon} {card_wa}</a>
        </div>
        <form class="buyer-form reveal" action="{COMMON['formspree']}" method="POST" id="buyerForm">
          <h2>{form_h2}</h2>
          <p style="color:var(--muted);margin:0 0 20px">{form_p}</p>
          <input type="hidden" name="landing" value="{cfg['form_hidden']}" />
          <input type="hidden" name="_subject" value="{cfg['form_subject']}" />
          <div class="buyer-grid">
            <div><label class="field" for="b_nome">{lbl_name}</label><input id="b_nome" name="nome" type="text" required placeholder="{ph_name}"></div>
            <div><label class="field" for="b_tel">{lbl_phone}</label><input id="b_tel" name="telefono" type="tel" required placeholder="{ph_phone}"></div>
            <div><label class="field" for="b_zona">{lbl_zone}</label><input id="b_zona" name="zona" type="text" list="{cfg['datalist_id']}" required placeholder="{cfg['zone_placeholder']}" autocomplete="off"></div>
            <div><label class="field" for="b_tip">{lbl_type}</label><select id="b_tip" name="tipologia">{type_select}</select></div>
            <div><label class="field" for="b_budget">{lbl_budget}</label><select id="b_budget" name="budget">{budget_select}</select></div>
            <div><label class="field" for="b_tempi">{lbl_time}</label><select id="b_tempi" name="tempistiche">{time_select}</select></div>
          </div>
          <div style="margin-top:14px"><label class="field" for="b_msg">{lbl_msg}</label><textarea id="b_msg" name="messaggio" rows="3" placeholder="{cfg['msg_placeholder']}"></textarea></div>
          <label class="buyer-check"><input type="checkbox" name="privacy" required><span>{privacy}</span></label>
          <button type="submit" class="btn btn-red" style="margin-top:20px;width:100%">{submit}</button>
          <p style="text-align:center;color:var(--muted);font-size:12.5px;margin:14px 0 0">{form_note}</p>
        </form>
      </div>
    </section>

    <section class="buyer-final-cta">
      <div class="container">
        <h2>{final_h2}</h2>
        <p>{final_p}</p>
        <div class="buyer-final-actions">
          <a class="btn btn-red" href="#contatto">{cta1}</a>
          <a class="btn btn-wa" href="{wa_url}">{wa_icon} {card_wa}</a>
        </div>
      </div>
    </section>
  </main>

  <datalist id="{cfg['datalist_id']}">
    {{DATALIST}}
  </datalist>

  <div class="buyer-sticky-bar" role="region" aria-label="{'Quick actions' if is_en else 'Azioni rapide'}">
    <div class="buyer-sticky-inner">
      <a class="btn btn-red" href="#contatto">{sticky}</a>
      <a class="btn btn-outline" href="{wa_url}" aria-label="WhatsApp">WA</a>
    </div>
  </div>

  <footer class="footer">
    <div class="container footer-inner">
      <div>
        <strong>{footer_strong}</strong>
        <div class="footer-affiliation">{footer_affiliation}</div>
        <div>{agent_label} · {COMMON['rea']} · {COMMON['piva']} · {cfg['footer_geo']}<br><small>{footer_note}</small></div>
      </div>
      <div class="footer-links">
        <a href="https://wa.me/{COMMON['wa']}">WhatsApp</a>
        <a href="mailto:{COMMON['email']}">Email</a>
        <a href="{COMMON['instagram']}">Instagram</a>
        <a href="tel:{COMMON['phone'].replace(' ', '')}">{COMMON['phone']}</a>
      </div>
    </div>
    <div class="container footer-secondary">{footer_links(cfg)}</div>
  </footer>
  <script src="/assets/buyer-landing.js" defer></script>
  <script src="/assets/site-nav.js" defer></script>"""


def extract_datalist(html: str, datalist_id: str) -> str:
    marker = f'<datalist id="{datalist_id}">'
    start = html.find(marker)
    if start == -1:
        return ""
    end = html.find("</datalist>", start)
    inner = html[start + len(marker):end]
    return inner.strip()


def patch_page(cfg):
    path = ROOT / cfg["path"]
    html = path.read_text(encoding="utf-8")

    if 'href="/assets/buyer-landing.css?v=20260712"' not in html:
        html = html.replace("</style>\n</head>", '</style>\n<link rel="stylesheet" href="/assets/buyer-landing.css?v=20260712" />\n</head>')
    if 'href="/assets/site-nav.css?v=20260712"' not in html:
        html = html.replace(
            '<link rel="stylesheet" href="/assets/buyer-landing.css?v=20260712" />',
            '<link rel="stylesheet" href="/assets/buyer-landing.css?v=20260712" />\n<link rel="stylesheet" href="/assets/site-nav.css?v=20260712" />',
        )

    datalist = extract_datalist(html, cfg["datalist_id"])
    if not datalist and "datalist" in cfg:
        datalist = "\n".join(f"              <option>{o}</option>" for o in cfg["datalist"])

    body = build_body(cfg).replace("{DATALIST}", datalist)

    body_start = html.find("<body>")
    body_end = html.rfind("</body>")
    if body_start == -1 or body_end == -1:
        raise ValueError(f"Cannot patch {path}")
    new_html = html[: body_start + len("<body>")] + "\n" + body + "\n" + html[body_end:]
    path.write_text(new_html, encoding="utf-8")
    print(f"Patched {cfg['path']}")


def make_en(cfg_it):
    en = dict(cfg_it)
    en["path"] = en["path"].replace("comprare-casa-", "en/buy-home-").replace("milano", "milan")
    en["path"] = {
        "bergamo": "en/buy-home-bergamo/index.html",
        "brescia": "en/buy-home-brescia/index.html",
        "milano": "en/buy-home-milan/index.html",
    }[cfg_it["city_slug"]]
    en["lang"] = "en"
    en["lang_link"] = {
        "bergamo": "/comprare-casa-bergamo/",
        "brescia": "/comprare-casa-brescia/",
        "milano": "/comprare-casa-milano/",
    }[cfg_it["city_slug"]]
    en["lang_label"] = "IT"
    en["form_hidden"] = {
        "bergamo": "Buy home Bergamo - buyer EN",
        "brescia": "Buy home Brescia - buyer EN",
        "milano": "Buy home Milan - buyer EN",
    }[cfg_it["city_slug"]]
    en["form_subject"] = {
        "bergamo": "Buyer request - Bergamo EN",
        "brescia": "Buyer request - Brescia EN",
        "milano": "Buyer request - Milan EN",
    }[cfg_it["city_slug"]]
    if cfg_it["city_slug"] == "bergamo":
        en["datalist"] = [
            "Bergamo Città Alta", "Bergamo Città Bassa", "Dalmine / Osio",
            "Seriate / Scanzorosciate", "Valle Seriana", "Valle Brembana",
            "Treviglio / Romano di Lombardia", "Other area in Bergamo province",
        ]
        en["zone_placeholder"] = "e.g. Città Alta, Seriate, Treviglio..."
        en["msg_placeholder"] = "e.g. three-bedroom in Città Bassa, home in Valle Seriana, max 2nd floor..."
        en["footer_geo"] = "Bergamo · Città Alta · Valle Seriana · Province"
        en["wa_text"] = "Hi Maurizio, I am looking to buy in Bergamo and would like buyer advisory."
        en["market"] = [
            ("Bergamo city", "Città Alta and Bassa", "Two different markets: solid demand, prices and timing that change street by street."),
            ("Valleys", "Seriana and Brembana", "Quality of life and green surroundings — but you still need the right numbers."),
            ("Province", "Belt towns and plain", "Dalmine, Seriate, Treviglio: more space than Milan, but competition is still real."),
        ]
        en["quote"] = "In Bergamo, Città Alta and Città Bassa do not follow the same rules. Knowing the micro-area before your offer saves thousands of euros."
        en["about_lead"] = "RE/MAX agent with a surveyor background. I know Bergamo centre, valleys and province — and I tell you whether the price makes sense before you discover it after closing."
        en["pain"] = [
            ("01", "You fear overpaying", "You find a home you like and cannot tell if the asking price is realistic for that street."),
            ("02", "You lose out with the wrong offer", "Competitive market: a low offer excludes you, a high one costs you for years."),
            ("03", "You have no time for dozens of listings", "Portals, viewings, negotiations: without a filter you waste weeks on the wrong homes."),
            ("04", "You worry about hidden issues", "Discrepancies, documents, restrictions: discovering them after closing is too late — and expensive."),
        ]
        en["hero_list"] = [
            "Price analysis based on OMI data for your area",
            "Technical checks before you offer",
            "Targeted search, no listing spam",
        ]
        en["trust_row"] = [
            ("OMI", "Price based on official data"),
            ("RE/MAX", "Access to the MLS network"),
            ("Surveyor", "Real technical checks"),
        ]
        en["form_benefits"] = [
            "I call you back within 24 hours, no obligation to appoint",
            "Fair price analysis for the area you want",
            "Alert when something truly relevant appears",
            "Support through negotiation and closing",
        ]
        en["faq_work"] = "Do you work only in Bergamo?"
        en["faq_work_a"] = "Bergamo, its valleys and province are the focus, but I also support buyers in Milan and Brescia."
    elif cfg_it["city_slug"] == "brescia":
        en["datalist"] = [
            "Brescia city centre", "Franciacorta", "Lake Garda (Brescia side)", "Lake Iseo",
            "Trompia Valley", "Camonica Valley", "Lower Brescia", "Other area in Brescia province",
        ]
        en["zone_placeholder"] = "e.g. Franciacorta, Desenzano, Brescia centre..."
        en["msg_placeholder"] = "e.g. three-bedroom in Franciacorta, lakefront villa, max budget €350,000..."
        en["footer_geo"] = "Brescia · Franciacorta · Lake Garda · Lake Iseo"
        en["wa_text"] = "Hi Maurizio, I am looking to buy in Brescia and would like buyer advisory."
        en["market"] = [
            ("City", "Brescia centre", "Stable demand, prices that change neighbourhood by neighbourhood."),
            ("Franciacorta", "Hills and villages", "Premium market: you need to know if the price fits the micro-area."),
            ("Lakes", "Garda and Iseo", "High competition, including international buyers — analysis before the offer is decisive."),
        ]
        en["quote"] = "In Franciacorta or on Lake Garda, two similar homes can be worth very different amounts. The micro-area decides — not the emotion of the moment."
        en["about_lead"] = "I support buyers in Brescia city, Franciacorta, lakes and valleys. With OMI data and technical checks I help you buy at the right price, not the listing price."
        en["pain"] = [
            ("01", "You are not sure lake prices are fair", "Franciacorta and Garda are premium markets: you need a real comparison, not the asking price."),
            ("02", "You compete with other buyers", "A poorly calibrated offer makes you lose the home — or locks you into too high a price."),
            ("03", "You search across very different areas", "City, hills, lakes: each area has different rules and needs a serious filter."),
            ("04", "You want to avoid technical surprises", "Before the offer you need to know about urban planning or cadastral issues."),
        ]
        en["hero_list"] = [
            "OMI analysis across city, lakes and Franciacorta",
            "Document checks before you offer",
            "Targeted selection, no random listings",
        ]
        en["trust_row"] = [
            ("OMI", "Price based on official data"),
            ("RE/MAX", "Access to the MLS network"),
            ("Surveyor", "Real technical checks"),
        ]
        en["form_benefits"] = [
            "Reply within 24 hours, no obligation to appoint",
            "Price analysis for the area you want",
            "Alert when I find something relevant",
            "Support through negotiation and closing",
        ]
        en["faq_work"] = "Do you work only in Brescia?"
        en["faq_work_a"] = "Brescia, Franciacorta, lakes and province are the focus, but I also support buyers in Milan and Bergamo."
    else:
        en["zone_placeholder"] = "e.g. Navigli, Sesto San Giovanni..."
        en["msg_placeholder"] = "e.g. bright three-bedroom with balcony, near metro, max 3rd floor..."
        en["footer_geo"] = "Milan · Province · Navigli · Isola"
        en["wa_text"] = "Hi Maurizio, I am looking to buy in Milan and would like buyer advisory."
        en["market"] = [
            ("Milan city", "Central areas", "High demand, fast timing: the wrong price costs dearly."),
            ("Province", "Milan municipalities", "More space, different prices — but each town has its own dynamics."),
            ("Investment", "Location and services", "Metro, schools, regeneration: real value is not just square metres."),
        ]
        en["quote"] = "In Milan the right price changes from one street to the next. OMI micro-area analysis is worth more than ten random viewings."
        en["about_lead"] = "Milan is fast and competitive. I help you understand whether a home is truly worth the asking price, move with the right timing, and avoid discovering problems after your offer."
        en["pain"] = [
            ("01", "You lose a home within minutes", "Fast market: without the right numbers you arrive late or overpay."),
            ("02", "You cannot tell if the price is fair", "Listings and asking prices often do not reflect real micro-area value."),
            ("03", "You are overwhelmed by listings", "Hundreds of ads: you need a serious filter, not hours on portals."),
            ("04", "You fear discrepancies or restrictions", "In Milan, checks before the offer avoid costly mistakes at closing."),
        ]
        en["hero_list"] = [
            "OMI analysis across Milan and province",
            "Technical checks before you offer",
            "Access to the RE/MAX network",
        ]
        en["trust_row"] = [
            ("OMI", "Price based on official data"),
            ("RE/MAX", "Access to the MLS network"),
            ("Surveyor", "Real technical checks"),
        ]
        en["form_benefits"] = [
            "Reply within 24 hours, no obligation to appoint",
            "Price analysis by area and property type",
            "Alerts on truly relevant homes",
            "Support through negotiation and closing",
        ]
        en["faq_work"] = "Do you work only in Milan?"
        en["faq_work_a"] = "Milan and province are the focus, but I also support buyers in Brescia and Bergamo."
    en["budget"] = [
        ("", "Prefer not to say"),
        ("150000", "Up to €150,000"),
        ("150000-250000", "€150,000 - €250,000"),
        ("250000-400000", "€250,000 - €400,000"),
        ("400000-600000", "€400,000 - €600,000"),
        ("600000+", "Over €600,000"),
    ] if cfg_it["city_slug"] != "milano" else [
        ("", "Prefer not to say"),
        ("200000", "Up to €200,000"),
        ("200000-350000", "€200,000 - €350,000"),
        ("350000-500000", "€350,000 - €500,000"),
        ("500000-800000", "€500,000 - €800,000"),
        ("800000+", "Over €800,000"),
    ]
    return en


def get_styles():
    html = STYLE_TEMPLATE.read_text(encoding="utf-8")
    start = html.index("<style>")
    end = html.index("</style>") + len("</style>")
    return html[start:end]


def build_head(cfg):
    is_en = cfg["lang"] == "en"
    slug = cfg["city_slug"]
    canonical = f"https://mauriziopiraino.it{province_urls(slug, cfg['lang'])}"
    it_url = f"https://mauriziopiraino.it{province_urls(slug, 'it')}"
    en_url = f"https://mauriziopiraino.it{province_urls(slug, 'en')}"
    city = cfg["city_en"] if is_en else cfg["city_it"]
    img = f"https://mauriziopiraino.it{cfg['hero_img']}"

    if is_en:
        title = f"Buy a home in {city}: buyer advisory | Piraino"
        desc = cfg.get(
            "meta_desc",
            f"Want to buy in {city} without overpaying? Fair price analysis, technical checks and targeted RE/MAX search.",
        )
        service = f"Home buying advisory in {city}"
        service_type = "Real estate buyer advisory"
        locale = "en_GB"
        faq_work = cfg["faq_work"]
        faq_work_a = cfg["faq_work_a"]
    else:
        title = f"Comprare casa a {city}: consulenza per acquirenti | Piraino"
        desc = cfg.get(
            "meta_desc",
            f"Vuoi comprare casa a {city} senza pagarla troppo? Analisi del prezzo giusto, verifica tecnica e ricerca mirata RE/MAX.",
        )
        service = f"Consulenza per l'acquisto di casa a {city}"
        service_type = "Consulenza immobiliare per acquirenti"
        locale = "it_IT"
        faq_work = cfg["faq_work"]
        faq_work_a = cfg["faq_work_a"]

    lang_attr = "en" if is_en else "it"
    schema = (
        '{"@context":"https://schema.org","@graph":['
        '{"@type":"RealEstateAgent","@id":"https://mauriziopiraino.it/#agent","name":"Maurizio Piraino","url":"https://mauriziopiraino.it/","areaServed":["Milano","Provincia di Milano","Brescia","Bergamo","Lombardia"],"telephone":"+39 351 458 1993"},'
        f'{{"@type":"Service","name":"{service}","serviceType":"{service_type}","provider":{{"@id":"https://mauriziopiraino.it/#agent"}},"areaServed":"{city}","url":"{canonical}"}},'
        '{"@type":"FAQPage","mainEntity":['
        '{"@type":"Question","name":"Quanto costa il servizio per chi compra?","acceptedAnswer":{"@type":"Answer","text":"Ne parliamo con chiarezza fin dal primo contatto, senza sorprese."}},'
        f'{{"@type":"Question","name":"{faq_work}","acceptedAnswer":{{"@type":"Answer","text":"{faq_work_a}"}}}}'
        "]}]}"
    )

    return f"""<!DOCTYPE html>
<html lang="{lang_attr}">
<head>
<meta charset="UTF-8" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="apple-touch-icon" href="/favicon.svg" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="robots" content="index,follow" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="canonical" href="{canonical}" />
<link rel="alternate" hreflang="it" href="{it_url}" />
<link rel="alternate" hreflang="en" href="{en_url}" />
<link rel="alternate" hreflang="x-default" href="{it_url}" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:type" content="website" />
<meta property="og:url" content="{canonical}" />
<meta property="og:locale" content="{locale}" />
<meta property="og:image" content="{img}" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="preload" as="image" href="{img}" fetchpriority="high" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">
<script type="application/ld+json">{schema}</script>
{get_styles()}
<link rel="stylesheet" href="/assets/buyer-landing.css?v=20260712" />
<link rel="stylesheet" href="/assets/site-nav.css?v=20260712" />
<link rel="stylesheet" href="/assets/site-base.css?v=20260712" />
<link rel="stylesheet" href="/assets/remax-brand.css?v=20260712" />
</head>
<body>
  <a class="skip-link" href="#main">{'Skip to content' if is_en else 'Salta al contenuto'}</a>
"""


def build_new_cfg(slug, lang):
    meta = NEW_PROVINCES[slug]
    city_it = next(c[1] for c in LOMBARD_PROVINCES if c[0] == slug)
    city_en = next(c[2] for c in LOMBARD_PROVINCES if c[0] == slug)
    content = meta["it" if lang == "it" else "en"]
    is_en = lang == "en"
    omi = OMI_LINKS.get(slug, "#contatto")
    budget = meta.get("budget", MILANO_BUDGET if slug in ("milano", "monza") else DEFAULT_BUDGET_PROVINCE)
    if is_en and slug not in ("milano", "monza"):
        budget = [
            ("", "Prefer not to say"),
            ("150000", "Up to €150,000"),
            ("150000-250000", "€150,000 - €250,000"),
            ("250000-400000", "€250,000 - €400,000"),
            ("400000-600000", "€400,000 - €600,000"),
            ("600000+", "Over €600,000"),
        ]
    elif is_en:
        budget = [
            ("", "Prefer not to say"),
            ("200000", "Up to €200,000"),
            ("200000-350000", "€200,000 - €350,000"),
            ("350000-500000", "€350,000 - €500,000"),
            ("500000-800000", "€500,000 - €800,000"),
            ("800000+", "Over €800,000"),
        ]

    city_label = city_en if is_en else city_it
    faq_work = content.get("faq_work", DEFAULT_FAQ_WORK_IT.format(city=city_label))
    faq_work_a = content.get("faq_work_a", DEFAULT_FAQ_WORK_A_IT.format(city=city_label))

    if is_en:
        faq_work = content.get("faq_work", f"Do you work only in {city_en}?")
        faq_work_a = content.get(
            "faq_work_a",
            f"I support buyers across Lombardy, with particular focus on {city_en} and neighbouring provinces.",
        )
        trust_row = [
            ("OMI", "Price based on official data"),
            ("RE/MAX", "Access to the MLS network"),
            ("Surveyor", "Real technical checks"),
        ]
        stats = [
            ("OMI", "Official Revenue Agency data"),
            ("24h", "Reply to your request"),
            ("✓", "No obligation to appoint"),
            ("RE/MAX", "International network"),
        ]
        form_benefits = content.get("form_benefits", [
            "Reply within 24 hours, no obligation to appoint",
            "Fair price analysis for the area you want",
            "Alert when something truly relevant appears",
            "Support through negotiation and closing",
        ])
        hero_list = content.get("hero_list", [
            "Price analysis based on OMI data for your area",
            "Technical checks before you offer",
            "Targeted search, no listing spam",
        ])
        pain = content.get("pain", [
            ("01", "You fear overpaying", "You find a home you like and cannot tell if the asking price is realistic."),
            ("02", "You lose out with the wrong offer", "A poorly calibrated offer makes you lose the home or overpay."),
            ("03", "You have no time for dozens of listings", "Without a filter you waste weeks on the wrong homes."),
            ("04", "You worry about hidden issues", "Discovering problems after closing is too late — and expensive."),
        ])
        omi_text = "Request OMI area analysis →" if omi == "#contatto" else "See OMI values by area →"
        footer_geo = meta["footer_geo_en"]
        datalist = meta["datalist_en"]
    else:
        trust_row = DEFAULT_TRUST_IT
        stats = DEFAULT_STATS_IT
        form_benefits = content.get("form_benefits", DEFAULT_FORM_BENEFITS_IT)
        hero_list = content.get("hero_list", DEFAULT_HERO_LIST_IT)
        pain = content.get("pain", DEFAULT_PAIN_IT)
        omi_text = "Richiedi analisi OMI della zona →" if omi == "#contatto" else "Consulta i valori OMI per zona →"
        footer_geo = meta["footer_geo_it"]
        datalist = meta["datalist_it"]

    en_slug = "milan" if slug == "milano" else slug
    path = (
        f"en/buy-home-{en_slug}/index.html"
        if is_en
        else ("comprare-casa-milano/index.html" if slug == "milano" else f"comprare-casa-{slug}/index.html")
    )

    return {
        "path": path,
        "lang": lang,
        "hero_img": meta["hero_img"],
        "city": city_label,
        "city_it": city_it,
        "city_en": city_en,
        "city_slug": slug,
        "omi": omi,
        "omi_text": omi_text,
        "seller_link": seller_link_for(slug),
        "lang_link": province_urls(slug, "en" if lang == "it" else "it"),
        "lang_label": "EN" if lang == "it" else "IT",
        "form_hidden": f"{'Comprare casa' if lang == 'it' else 'Buy home'} {city_label} - {'acquirente' if lang == 'it' else 'buyer EN'}",
        "form_subject": f"{'Richiesta acquirente' if lang == 'it' else 'Buyer request'} - {city_label}{'' if lang == 'it' else ' EN'}",
        "datalist_id": meta["datalist_id"],
        "datalist": datalist,
        "budget": budget,
        "zone_placeholder": content["zone_placeholder"],
        "msg_placeholder": content["msg_placeholder"],
        "footer_geo": footer_geo,
        "wa_text": content["wa_text"],
        "market": content["market"],
        "quote": content["quote"],
        "about_lead": content["about_lead"],
        "lead": content["lead"],
        "stats": stats,
        "pain": pain,
        "hero_list": hero_list,
        "trust_row": trust_row,
        "form_benefits": form_benefits,
        "faq_work": faq_work,
        "faq_work_a": faq_work_a,
    }


def write_page(cfg):
    datalist = "\n".join(f"              <option>{o}</option>" for o in cfg["datalist"])
    body = build_body(cfg).replace("{DATALIST}", datalist)
    html = build_head(cfg) + body + "\n</body>\n</html>\n"
    path = ROOT / cfg["path"]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print(f"Wrote {cfg['path']}")


def main():
    for cfg in PAGES:
        patch_page(cfg)
        patch_page(make_en(cfg))

    for slug in NEW_PROVINCES:
        write_page(build_new_cfg(slug, "it"))
        write_page(build_new_cfg(slug, "en"))


if __name__ == "__main__":
    main()
