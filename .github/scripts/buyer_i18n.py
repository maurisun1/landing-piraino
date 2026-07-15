"""Buyer landing UI strings and locale helpers (IT / EN / DE / FR)."""

from __future__ import annotations

from buyer_provinces import (
    ABOUT_AGENCY_EN,
    ABOUT_AGENCY_IT,
    DEFAULT_BUYER_TESTIMONIALS_EN,
    DEFAULT_BUYER_TESTIMONIALS_IT,
    DEFAULT_FORM_BENEFITS_IT,
    DEFAULT_FAQ_WORK_A_IT,
    DEFAULT_FAQ_WORK_IT,
    DEFAULT_HERO_LIST_IT,
    DEFAULT_PAIN_IT,
    DEFAULT_STATS_IT,
    DEFAULT_TRUST_IT,
    FOOTER_AFFILIATION_EN,
    FOOTER_AFFILIATION_IT,
)

DEFAULT_STATS_DE = [
    ("OMI", "Offizielle Daten der Steuerbehörde"),
    ("24h", "Antwort auf Ihre Anfrage"),
    ("✓", "Keine Verpflichtung zum Mandat"),
    ("RE/MAX", "Internationales Netzwerk"),
]

DEFAULT_STATS_FR = [
    ("OMI", "Données officielles de l'Agence des Entrées"),
    ("24h", "Réponse à votre demande"),
    ("✓", "Aucune obligation de mandat"),
    ("RE/MAX", "Réseau international"),
]

DEFAULT_TRUST_DE = [
    ("OMI", "Preis basierend auf offiziellen Daten"),
    ("RE/MAX", "Zugang zum MLS-Netzwerk"),
    ("Geometer", "Echte technische Prüfung"),
]

DEFAULT_TRUST_FR = [
    ("OMI", "Prix basé sur des données officielles"),
    ("RE/MAX", "Accès au réseau MLS"),
    ("Géomètre", "Vérification technique réelle"),
]

DEFAULT_FORM_BENEFITS_DE = [
    "Rückruf innerhalb von 24 Stunden, keine Verpflichtung zum Mandat",
    "Preisanalyse für die gewünschte Zone",
    "Benachrichtigung bei wirklich relevanten Objekten",
    "Begleitung bis zum Notartermin",
]

DEFAULT_FORM_BENEFITS_FR = [
    "Rappel sous 24 heures, aucune obligation de mandat",
    "Analyse de prix pour la zone recherchée",
    "Alerte lorsqu'un bien vraiment pertinent apparaît",
    "Accompagnement jusqu'à la signature notariale",
]

DEFAULT_HERO_LIST_DE = [
    "OMI-Preisanalyse für Ihre Zone",
    "Technische Prüfung vor dem Angebot",
    "Gezielte Suche, kein Anzeigen-Spam",
]

DEFAULT_HERO_LIST_FR = [
    "Analyse OMI des prix pour votre zone",
    "Vérification technique avant l'offre",
    "Recherche ciblée, sans spam d'annonces",
]

DEFAULT_PAIN_DE = [
    ("01", "Sie fürchten, zu viel zu zahlen", "Sie finden ein Haus, das Ihnen gefällt, und wissen nicht, ob der Preis für die Zone realistisch ist."),
    ("02", "Sie verpassen die Chance wegen eines falschen Angebots", "Wettbewerbsmarkt: ein zu niedriges Angebot schließt Sie aus, ein zu hohes kostet Sie jahrelang."),
    ("03", "Sie haben keine Zeit für Dutzende Inserate", "Portale, Besichtigungen, Verhandlungen: ohne Filter verlieren Sie Wochen mit falschen Objekten."),
    ("04", "Sie befürchten versteckte Probleme", "Abweichungen, Dokumente, Auflagen: sie nach dem Kauf zu entdecken ist zu spät — und teuer."),
]

DEFAULT_PAIN_FR = [
    ("01", "Vous craignez de payer trop cher", "Vous trouvez une maison qui vous plaît sans savoir si le prix demandé est réaliste pour ce quartier."),
    ("02", "Vous perdez l'occasion avec une mauvaise offre", "Marché compétitif : une offre trop basse vous élimine, une offre trop haute vous coûte cher pendant des années."),
    ("03", "Vous n'avez pas le temps pour des dizaines d'annonces", "Portails, visites, négociations : sans filtre vous perdez des semaines sur les mauvais biens."),
    ("04", "Vous craignez des problèmes cachés", "Non-conformités, documents, contraintes : les découvrir après l'achat est trop tard — et coûteux."),
]

DEFAULT_BUYER_TESTIMONIALS_DE = [
    ("MR", "Käufer · Mailand", "Navigli", "Ich wollte den geforderten Preis bieten. Die OMI-Mikrozonenanalyse hat mir rund 15.000 € in der Verhandlung gespart."),
    ("GL", "Paar · Erstes Eigenheim", "Bergamo", "Wir haben den Kauf einer Immobilie mit Katasterabweichungen vermieden. Prüfungen vor dem Angebot, reibungsloser Notartermin."),
    ("SF", "Käufer · Brescia", "Franciacorta", "Wettbewerbsmarkt: mit dem richtigen Timing und den richtigen Zahlen zum fairen Preis geschlossen."),
]

DEFAULT_BUYER_TESTIMONIALS_FR = [
    ("MR", "Acheteur · Milan", "Navigli", "J'allais faire une offre au prix demandé. L'analyse OMI de la micro-zone m'a fait économiser environ 15 000 € dans la négociation."),
    ("GL", "Couple · première maison", "Bergamo", "Nous avons évité d'acheter un bien avec des difformités cadastrales. Contrôles avant l'offre, acte sans surprise."),
    ("SF", "Acheteur · Brescia", "Franciacorta", "Marché compétitif : grâce au bon timing et aux bons chiffres, clôture au prix juste."),
]

FOOTER_AFFILIATION_DE = (
    "Maurizio Piraino — Immobilienberater bei RE/MAX Associati Real Estate "
    "· Mailand, Viale Gran Sasso 31"
)
FOOTER_AFFILIATION_FR = (
    "Maurizio Piraino — Consultant immobilier chez RE/MAX Associati Real Estate "
    "· Milan, Viale Gran Sasso 31"
)

ABOUT_AGENCY_DE = (
    "Ich arbeite als Immobilienberater mit RE/MAX Associati Real Estate in Mailand, einer Agentur mit "
    "über 25 Jahren Markterfahrung und unter den Top-30-RE/MAX-Büros in Italien. So verbinde ich "
    "persönliche Beratung mit der Stärke eines internationalen Netzwerks."
)
ABOUT_AGENCY_FR = (
    "J'opère comme consultant immobilier avec RE/MAX Associati Real Estate à Milan, une agence avec "
    "plus de 25 ans d'activité sur le marché et parmi les 30 premières RE/MAX en Italie. Cela me permet "
    "d'allier une approche conseil personnelle à la force d'un réseau international."
)

DEFAULT_FAQ_WORK_DE = "Arbeiten Sie nur in {city}?"
DEFAULT_FAQ_WORK_A_DE = "Ich begleite Käufer in ganz der Lombardei, mit besonderem Fokus auf {city} und angrenzende Provinzen."

DEFAULT_FAQ_WORK_FR = "Travaillez-vous uniquement à {city} ?"
DEFAULT_FAQ_WORK_A_FR = "J'accompagne des acheteurs dans toute la Lombardie, avec une attention particulière à {city} et aux provinces voisines."


def ui(lang: str, key: str, **kwargs: str) -> str:
    pack = _UI[key]
    text = pack.get(lang, pack["it"])
    return text.format(**kwargs) if kwargs else text


_UI: dict[str, dict[str, str]] = {
    "brand": {
        "it": "Maurizio Piraino <span>·</span> Agente Immobiliare affiliato RE/MAX",
        "en": "Maurizio Piraino <span>·</span> RE/MAX Real Estate Agent",
        "de": "Maurizio Piraino <span>·</span> RE/MAX Immobilienberater",
        "fr": "Maurizio Piraino <span>·</span> Agent immobilier RE/MAX",
    },
    "topbar": {
        "it": "Consulenza acquirenti <strong>RE/MAX</strong> · {city} · Risposta entro 24h",
        "en": "Buyer advisory <strong>RE/MAX</strong> · {city} · Reply within 24 hours",
        "de": "Käuferberatung <strong>RE/MAX</strong> · {city} · Antwort innerhalb von 24h",
        "fr": "Conseil acheteurs <strong>RE/MAX</strong> · {city} · Réponse sous 24h",
    },
    "topbar_wa": {
        "it": "Scrivimi su WhatsApp", "en": "Message me on WhatsApp",
        "de": "Schreiben Sie mir auf WhatsApp", "fr": "Écrivez-moi sur WhatsApp",
    },
    "nav_method": {"it": "Chi sono", "en": "About me", "de": "Über mich", "fr": "Qui je suis"},
    "nav_omi": {"it": "Prezzi OMI", "en": "OMI prices", "de": "OMI-Preise", "fr": "Prix OMI"},
    "nav_cta": {
        "it": "Prenota una consulenza", "en": "Book a consultation",
        "de": "Beratung vereinbaren", "fr": "Réserver une consultation",
    },
    "kicker": {
        "it": "Property Finding · {city}", "en": "Property Finding · {city}",
        "de": "Property Finding · {city}", "fr": "Property Finding · {city}",
    },
    "h1": {
        "it": "Cerchiamo insieme l'immobile giusto a {city}.<br>Con analisi, tutela e metodo.",
        "en": "Let's find the right property in {city} together.<br>With analysis, protection and method.",
        "de": "Suchen wir gemeinsam die richtige Immobilie in {city}.<br>Mit Analyse, Schutz und Methode.",
        "fr": "Cherchons ensemble le bon bien à {city}.<br>Avec analyse, protection et méthode.",
    },
    "lead_strong": {
        "it": "Prima l'analisi. Poi la scelta giusta.",
        "en": "Analysis first. Then the right choice.",
        "de": "Zuerst die Analyse. Dann die richtige Wahl.",
        "fr": "D'abord l'analyse. Ensuite le bon choix.",
    },
    "cta1": {"it": "Prenota una consulenza →", "en": "Book a consultation →", "de": "Beratung vereinbaren →", "fr": "Réserver une consultation →"},
    "cta2": {"it": "Come funziona", "en": "How it works", "de": "So funktioniert es", "fr": "Comment ça marche"},
    "card_h": {"it": "Avvia il Property Finding", "en": "Start Property Finding", "de": "Property Finding starten", "fr": "Lancer le Property Finding"},
    "card_p": {
        "it": "Raccontami cosa cerchi. Ti richiamo entro 24 ore.",
        "en": "Tell me what you are looking for. I will call within 24 hours.",
        "de": "Erzählen Sie mir, was Sie suchen. Rückruf innerhalb von 24 Stunden.",
        "fr": "Parlez-moi de votre recherche. Je vous rappelle sous 24 heures.",
    },
    "card_cta": {"it": "Inizia la consulenza →", "en": "Start the consultation →", "de": "Beratung starten →", "fr": "Commencer la consultation →"},
    "card_wa": {"it": "Scrivimi su WhatsApp", "en": "Message me on WhatsApp", "de": "WhatsApp-Nachricht", "fr": "Message WhatsApp"},
    "pain_k": {"it": "Ti riconosci?", "en": "Sound familiar?", "de": "Kommt Ihnen das bekannt vor?", "fr": "Vous vous reconnaissez ?"},
    "pain_h": {
        "it": "Quattro situazioni frequenti — e come le evito",
        "en": "Four common situations — and how I help you avoid them",
        "de": "Vier häufige Situationen — und wie ich sie vermeide",
        "fr": "Quatre situations fréquentes — et comment je vous aide à les éviter",
    },
    "adv_k": {"it": "Property Finding e tutela", "en": "Property Finding and protection", "de": "Property Finding und Schutz", "fr": "Property Finding et protection"},
    "adv_h": {
        "it": "Quattro pilastri della consulenza per acquirenti e investitori",
        "en": "Four pillars of advisory for buyers and investors",
        "de": "Vier Säulen der Beratung für Käufer und Investoren",
        "fr": "Quatre piliers du conseil pour acheteurs et investisseurs",
    },
    "a1t": {"it": "Property Finding", "en": "Property Finding", "de": "Property Finding", "fr": "Property Finding"},
    "a1p": {
        "it": "Ricerca personalizzata — anche off-market — selezione, visite e negoziazione fino al rogito.",
        "en": "Personalised search — including off-market — selection, viewings and negotiation through to completion.",
        "de": "Persönliche Suche — auch off-market — Auswahl, Besichtigungen und Verhandlung bis zum Notartermin.",
        "fr": "Recherche personnalisée — aussi hors marché — sélection, visites et négociation jusqu'à l'acte.",
    },
    "a2t": {"it": "Consulenza per investitori", "en": "Investor advisory", "de": "Investorenberatung", "fr": "Conseil investisseurs"},
    "a2p": {
        "it": "Opportunità a reddito, valorizzazione e stima della redditività — con numeri prima dell'emozione.",
        "en": "Yield opportunities, value-add and return estimates — numbers before emotion.",
        "de": "Renditeobjekte, Wertsteigerung und Ertragsanalyse — Zahlen vor Emotion.",
        "fr": "Opportunités locatives, valorisation et estimation du rendement — les chiffres avant l'émotion.",
    },
    "a3t": {"it": "Verifica documentale", "en": "Document verification", "de": "Dokumentenprüfung", "fr": "Contrôle documentaire"},
    "a3p": {
        "it": "Conformità, titoli e criticità tecniche: controlli prima dell'offerta, non dopo il rogito.",
        "en": "Compliance, title and technical risks: checks before the offer, not after completion.",
        "de": "Konformität, Titel und technische Risiken: Prüfung vor dem Angebot, nicht nach dem Notartermin.",
        "fr": "Conformité, titres et risques techniques : contrôles avant l'offre, pas après l'acte.",
    },
    "a4t": {"it": "Negoziazione e tutela", "en": "Negotiation and protection", "de": "Verhandlung und Schutz", "fr": "Négociation et protection"},
    "a4p": {
        "it": "Affiancamento in trattativa e fino al rogito: il tuo interesse viene prima.",
        "en": "Support in negotiation through to completion: your interest comes first.",
        "de": "Begleitung in der Verhandlung bis zum Notartermin: Ihr Interesse hat Vorrang.",
        "fr": "Accompagnement en négociation jusqu'à l'acte : votre intérêt passe avant.",
    },
    "trust_k": {"it": "Chi ti affianca", "en": "Who supports you", "de": "Wer Sie begleitet", "fr": "Qui vous accompagne"},
    "trust_h": {
        "it": "Non un portale. Una persona con numeri e metodo.",
        "en": "Not a portal. A person with data and method.",
        "de": "Kein Portal. Eine Person mit Zahlen und Methode.",
        "fr": "Pas un portail. Une personne avec des chiffres et une méthode.",
    },
    "portrait_sub": {
        "it": "Consulente acquirenti e investitori · {city}",
        "en": "Buyer & investor advisor · {city}",
        "de": "Berater für Käufer und Investoren · {city}",
        "fr": "Conseiller acheteurs et investisseurs · {city}",
    },
    "b2": {"it": "Geometra", "en": "Surveyor", "de": "Geometer", "fr": "Géomètre"},
    "b3": {"it": "Dati OMI", "en": "OMI data", "de": "OMI-Daten", "fr": "Données OMI"},
    "m_k": {"it": "Mercato {city}", "en": "{city} market", "de": "Markt {city}", "fr": "Marché {city}"},
    "m_h": {
        "it": "Ogni zona ha regole diverse. I numeri vengono prima dell'emozione.",
        "en": "Each area has different rules. Numbers come before emotion.",
        "de": "Jede Zone hat eigene Regeln. Zahlen vor Emotion.",
        "fr": "Chaque zone a ses règles. Les chiffres avant l'émotion.",
    },
    "omi": {"it": "Consulta i valori OMI per zona →", "en": "See OMI values by area →", "de": "OMI-Werte nach Zone →", "fr": "Consulter les valeurs OMI par zone →"},
    "s_k": {"it": "Come funziona", "en": "How it works", "de": "So funktioniert es", "fr": "Comment ça marche"},
    "s_h": {"it": "Tre passi. Nessuna pressione.", "en": "Three steps. No pressure.", "de": "Drei Schritte. Kein Druck.", "fr": "Trois étapes. Sans pression."},
    "s1t": {"it": "Consulenza iniziale", "en": "Initial consultation", "de": "Erstberatung", "fr": "Consultation initiale"},
    "s1p": {
        "it": "Obiettivo abitativo o di investimento, budget, zone e criteri. Nessuna pressione.",
        "en": "Home or investment goal, budget, areas and criteria. No pressure.",
        "de": "Wohn- oder Investmentziel, Budget, Zonen und Kriterien. Kein Druck.",
        "fr": "Objectif habitat ou investissement, budget, zones et critères. Sans pression.",
    },
    "s2t": {"it": "Property Finding e verifica", "en": "Property Finding and checks", "de": "Property Finding und Prüfung", "fr": "Property Finding et contrôles"},
    "s2p": {
        "it": "Ricerca anche off-market, selezione, visite e controllo documentale prima dell'offerta.",
        "en": "Search including off-market, selection, viewings and document checks before any offer.",
        "de": "Suche auch off-market, Auswahl, Besichtigungen und Dokumentenprüfung vor dem Angebot.",
        "fr": "Recherche aussi hors marché, sélection, visites et contrôle documentaire avant l'offre.",
    },
    "s3t": {"it": "Negoziazione e rogito", "en": "Negotiation and completion", "de": "Verhandlung und Notartermin", "fr": "Négociation et acte"},
    "s3p": {
        "it": "Trattativa, banca, notaio e tecnici: tutela fino al passaggio di proprietà.",
        "en": "Negotiation, bank, notary and surveyors: protection through to transfer of ownership.",
        "de": "Verhandlung, Bank, Notar und Techniker: Schutz bis zur Eigentumsübertragung.",
        "fr": "Négociation, banque, notaire et techniciens : protection jusqu'au transfert de propriété.",
    },
    "exp_k": {"it": "Esperienze", "en": "Experiences", "de": "Erfahrungen", "fr": "Expériences"},
    "exp_h": {
        "it": "Chi ha comprato con metodo, non a caso.",
        "en": "People who bought with a method, not by chance.",
        "de": "Käufer mit Methode, nicht dem Zufall.",
        "fr": "Ceux qui ont acheté avec méthode, pas au hasard.",
    },
    "faq_h": {"it": "Le domande di chi compra", "en": "Questions from buyers", "de": "Fragen von Käufern", "fr": "Les questions des acheteurs"},
    "fq1": {"it": "Quanto costa il servizio per chi compra?", "en": "How much does the buyer service cost?", "de": "Was kostet die Käuferberatung?", "fr": "Combien coûte le service pour les acheteurs ?"},
    "fq1a": {
        "it": "Ne parliamo con chiarezza fin dal primo contatto. Il valore che ti faccio risparmiare evitando di pagare troppo conta più della provvigione.",
        "en": "We discuss it clearly from the first contact. The value you save by avoiding overpaying matters more than the fee.",
        "de": "Wir besprechen es klar vom ersten Kontakt an. Was Sie durch Vermeidung von Überzahlung sparen, zählt mehr als die Provision.",
        "fr": "Nous en parlons clairement dès le premier contact. Ce que vous économisez en évitant de payer trop compte plus que les honoraires.",
    },
    "fq2": {"it": "Mi fate vedere solo le vostre case?", "en": "Do you only show your own listings?", "de": "Zeigen Sie nur Ihre eigenen Objekte?", "fr": "Ne me montrez-vous que vos propres biens ?"},
    "fq2a": {
        "it": "No. L'obiettivo è trovare la casa giusta per te, non piazzarti un immobile.",
        "en": "No. The goal is to find the right home for you, not to push a property.",
        "de": "Nein. Ziel ist das richtige Haus für Sie — kein Verkaufsdruck.",
        "fr": "Non. L'objectif est de trouver la bonne maison pour vous, pas de vous imposer un bien.",
    },
    "fq3": {"it": "Come fate a sapere se il prezzo è giusto?", "en": "How do you know if the price is fair?", "de": "Woher wissen Sie, ob der Preis fair ist?", "fr": "Comment savez-vous si le prix est juste ?"},
    "fq3a": {
        "it": "Con un'analisi della micro-zona basata sui dati ufficiali OMI e sulle caratteristiche reali dell'immobile.",
        "en": "With a micro-area analysis based on official OMI data and the property's real characteristics.",
        "de": "Durch Mikrozonenanalyse auf offiziellen OMI-Daten und den tatsächlichen Merkmalen der Immobilie.",
        "fr": "Par une analyse de micro-zone basée sur les données OMI officielles et les caractéristiques réelles du bien.",
    },
    "fq4": {"it": "Posso comprare prima di aver venduto la mia casa?", "en": "Can I buy before selling my current home?", "de": "Kann ich kaufen, bevor ich mein Haus verkaufe?", "fr": "Puis-je acheter avant d'avoir vendu ma maison ?"},
    "fq4a": {
        "it": "Sì, ed è frequente. Va pianificata con i tempi e i numeri giusti.",
        "en": "Yes, and it is common. It needs to be planned with the right timing and numbers.",
        "de": "Ja, das ist häufig. Es braucht die richtige Planung mit Timing und Zahlen.",
        "fr": "Oui, c'est fréquent. Il faut le planifier avec les bons délais et les bons chiffres.",
    },
    "form_h": {"it": "Prenota una consulenza", "en": "Book a consultation", "de": "Beratung vereinbaren", "fr": "Réserver une consultation"},
    "form_p": {
        "it": "Raccontami casa o investimento: avvio il Property Finding e ti dico se il prezzo ha senso.",
        "en": "Tell me about home or investment: I start Property Finding and tell you if the price makes sense.",
        "de": "Erzählen Sie von Wohnen oder Investment: ich starte Property Finding und prüfe den Preis.",
        "fr": "Parlez-moi habitat ou investissement : je lance le Property Finding et vérifie si le prix a du sens.",
    },
    "form_aside_h": {
        "it": "Non un portale. Un consulente che tutela il tuo acquisto.",
        "en": "Not a portal. An advisor who protects your purchase.",
        "de": "Kein Portal. Ein Berater, der Ihren Kauf schützt.",
        "fr": "Pas un portail. Un conseiller qui protège votre achat.",
    },
    "form_aside_p": {
        "it": "Compila il modulo: primo passo del Property Finding — ricerca, verifica e negoziazione.",
        "en": "Fill in the form: first step of Property Finding — search, checks and negotiation.",
        "de": "Formular ausfüllen: erster Schritt von Property Finding — Suche, Prüfung und Verhandlung.",
        "fr": "Remplissez le formulaire : première étape du Property Finding — recherche, contrôles et négociation.",
    },
    "lbl_name": {"it": "Nome *", "en": "Name *", "de": "Name *", "fr": "Nom *"},
    "lbl_phone": {"it": "Telefono / WhatsApp *", "en": "Phone / WhatsApp *", "de": "Telefon / WhatsApp *", "fr": "Téléphone / WhatsApp *"},
    "lbl_zone": {"it": "Zona o comune cercato *", "en": "Area or municipality *", "de": "Gesuchte Zone oder Gemeinde *", "fr": "Zone ou commune recherchée *"},
    "lbl_type": {"it": "Tipologia", "en": "Property type", "de": "Objekttyp", "fr": "Type de bien"},
    "lbl_budget": {"it": "Budget indicativo", "en": "Indicative budget", "de": "Ungefähres Budget", "fr": "Budget indicatif"},
    "lbl_time": {"it": "Tempistiche", "en": "Timing", "de": "Zeitrahmen", "fr": "Délais"},
    "lbl_msg": {"it": "Cosa è importante per te? (opzionale)", "en": "What matters most to you? (optional)", "de": "Was ist Ihnen wichtig? (optional)", "fr": "Qu'est-ce qui compte pour vous ? (optionnel)"},
    "type0": {"it": "Indifferente", "en": "No preference", "de": "Keine Präferenz", "fr": "Sans préférence"},
    "type1": {"it": "Bilocale", "en": "Two-bedroom", "de": "Zweizimmer", "fr": "Deux pièces"},
    "type2": {"it": "Trilocale", "en": "Three-bedroom", "de": "Dreizimmer", "fr": "Trois pièces"},
    "type3": {"it": "Quattro locali o più", "en": "Four bedrooms or more", "de": "Vier Zimmer oder mehr", "fr": "Quatre pièces ou plus"},
    "type4": {"it": "Villa / indipendente", "en": "Villa / detached house", "de": "Villa / Einfamilienhaus", "fr": "Villa / maison indépendante"},
    "type5": {"it": "Altro", "en": "Other", "de": "Sonstiges", "fr": "Autre"},
    "time1": {"it": "Sto cercando attivamente", "en": "Actively searching", "de": "Aktiv auf der Suche", "fr": "Recherche active"},
    "time2": {"it": "Entro 3-6 mesi", "en": "Within 3-6 months", "de": "Innerhalb von 3–6 Monaten", "fr": "Dans les 3 à 6 mois"},
    "time3": {"it": "Sto solo valutando", "en": "Just exploring", "de": "Nur am Überlegen", "fr": "Je me renseigne seulement"},
    "privacy": {
        "it": 'Ho letto l\'<a href="/privacy/" style="color:inherit;text-decoration:underline">informativa privacy</a> e acconsento ad essere ricontattato.',
        "en": 'I have read the <a href="/privacy/" style="color:inherit;text-decoration:underline">privacy policy</a> and agree to be contacted.',
        "de": 'Ich habe die <a href="/privacy/" style="color:inherit;text-decoration:underline">Datenschutzerklärung</a> gelesen und stimme der Kontaktaufnahme zu.',
        "fr": 'J\'ai lu la <a href="/privacy/" style="color:inherit;text-decoration:underline">politique de confidentialité</a> et j\'accepte d\'être recontacté.',
    },
    "submit": {"it": "Prenota la consulenza →", "en": "Book the consultation →", "de": "Beratung buchen →", "fr": "Réserver la consultation →"},
    "form_note": {
        "it": "Risposta entro 24 ore · Nessun obbligo di incarico",
        "en": "Reply within 24 hours · No obligation to appoint",
        "de": "Antwort innerhalb von 24h · Keine Verpflichtung zum Mandat",
        "fr": "Réponse sous 24h · Aucune obligation de mandat",
    },
    "final_h": {
        "it": "Prenota una consulenza. Cerchiamo insieme l'immobile giusto.",
        "en": "Book a consultation. Let's find the right property together.",
        "de": "Vereinbaren Sie eine Beratung. Suchen wir gemeinsam die richtige Immobilie.",
        "fr": "Réservez une consultation. Cherchons ensemble le bon bien.",
    },
    "final_p": {
        "it": "Casa o investimento: ti richiamo entro 24 ore. Property Finding, verifica e tutela fino al rogito — nessun obbligo.",
        "en": "Home or investment: I call within 24 hours. Property Finding, checks and protection to completion — no obligation.",
        "de": "Wohnen oder Investment: Rückruf in 24h. Property Finding, Prüfung und Schutz bis zum Notartermin — ohne Pflicht.",
        "fr": "Habitat ou investissement : rappel sous 24h. Property Finding, contrôles et protection jusqu'à l'acte — sans obligation.",
    },
    "sticky": {"it": "Prenota consulenza", "en": "Book consultation", "de": "Beratung buchen", "fr": "Réserver consultation"},
    "footer_s": {
        "it": "Prima l'analisi. Poi la scelta giusta.",
        "en": "Analysis first. Then the right choice.",
        "de": "Zuerst die Analyse. Dann die richtige Wahl.",
        "fr": "D'abord l'analyse. Ensuite le bon choix.",
    },
    "footer_n": {
        "it": "La consulenza iniziale non costituisce obbligo di conferimento incarico.",
        "en": "The initial consultation does not create an obligation to appoint an agent.",
        "de": "Die Erstberatung begründet keine Verpflichtung zur Beauftragung.",
        "fr": "La consultation initiale ne crée aucune obligation de mandat.",
    },
    "agent": {
        "it": "Agente Immobiliare affiliato RE/MAX",
        "en": "RE/MAX Real Estate Agent",
        "de": "RE/MAX Immobilienberater",
        "fr": "Agent immobilier affilié RE/MAX",
    },
    "skip": {"it": "Salta al contenuto", "en": "Skip to content", "de": "Zum Inhalt springen", "fr": "Aller au contenu"},
    "menu": {"it": "Apri menu", "en": "Open menu", "de": "Menü öffnen", "fr": "Ouvrir le menu"},
    "aria_nav": {"it": "Menu principale", "en": "Main menu", "de": "Hauptmenü", "fr": "Menu principal"},
    "sticky_region": {"it": "Azioni rapide", "en": "Quick actions", "de": "Schnellaktionen", "fr": "Actions rapides"},
    "sell_label": {"it": "Vuoi vendere?", "en": "Selling instead?", "de": "Stattdessen verkaufen?", "fr": "Vous vendez plutôt ?"},
    "buy_label": {"it": "Comprare", "en": "Buy", "de": "Kaufen", "fr": "Acheter"},
    "sell_st": {"it": "Consulenza vendita", "en": "Seller advisory", "de": "Verkäuferberatung", "fr": "Conseil vendeur"},
    "budget_empty": {
        "it": "Preferisco non indicarlo", "en": "Prefer not to say",
        "de": "Möchte ich nicht angeben", "fr": "Je préfère ne pas indiquer",
    },
    "ph_name": {"it": "Es. Marco Rossi", "en": "e.g. Marco Rossi", "de": "z. B. Marco Rossi", "fr": "ex. Marco Rossi"},
    "ph_phone": {"it": "Es. 348 000 0000", "en": "e.g. +39 348 000 0000", "de": "z. B. +39 348 000 0000", "fr": "ex. +39 348 000 0000"},
    "portrait_alt": {
        "it": "Maurizio Piraino Agente Immobiliare RE/MAX {city}",
        "en": "Maurizio Piraino RE/MAX real estate agent {city}",
        "de": "Maurizio Piraino RE/MAX Immobilienberater {city}",
        "fr": "Maurizio Piraino agent immobilier RE/MAX {city}",
    },
}
