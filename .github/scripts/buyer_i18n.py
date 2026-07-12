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
        "it": "Dimmi cosa cerchi", "en": "Tell me what you need",
        "de": "Sagen Sie mir, was Sie suchen", "fr": "Dites-moi ce que vous cherchez",
    },
    "kicker": {
        "it": "Comprare casa a {city}", "en": "Buy a home in {city}",
        "de": "Haus kaufen in {city}", "fr": "Acheter une maison à {city}",
    },
    "h1": {
        "it": "Comprare bene a {city} non è trovare una casa.<br>È non pagarla troppo.",
        "en": "Buying well in {city} is not about finding a home.<br>It is about not overpaying.",
        "de": "Gut kaufen in {city} heißt nicht, ein Haus zu finden.<br>Es heißt, nicht zu viel zu zahlen.",
        "fr": "Bien acheter à {city}, ce n'est pas trouver une maison.<br>C'est ne pas la payer trop cher.",
    },
    "lead_strong": {
        "it": "Prima l'analisi. Poi la scelta giusta.",
        "en": "Analysis first. Then the right choice.",
        "de": "Zuerst die Analyse. Dann die richtige Wahl.",
        "fr": "D'abord l'analyse. Ensuite le bon choix.",
    },
    "cta1": {"it": "Dimmi cosa cerchi →", "en": "Tell me what you need →", "de": "Sagen Sie mir, was Sie suchen →", "fr": "Dites-moi ce que vous cherchez →"},
    "cta2": {"it": "Come funziona", "en": "How it works", "de": "So funktioniert es", "fr": "Comment ça marche"},
    "card_h": {"it": "Registra la ricerca", "en": "Register your search", "de": "Suche registrieren", "fr": "Enregistrer votre recherche"},
    "card_p": {
        "it": "Due minuti. Ti richiamo entro 24 ore.",
        "en": "Two minutes. I will call you back within 24 hours.",
        "de": "Zwei Minuten. Ich rufe Sie innerhalb von 24 Stunden zurück.",
        "fr": "Deux minutes. Je vous rappelle sous 24 heures.",
    },
    "card_cta": {"it": "Compila il modulo →", "en": "Fill in the form →", "de": "Formular ausfüllen →", "fr": "Remplir le formulaire →"},
    "card_wa": {"it": "Scrivimi su WhatsApp", "en": "Message me on WhatsApp", "de": "WhatsApp-Nachricht", "fr": "Message WhatsApp"},
    "pain_k": {"it": "Ti riconosci?", "en": "Sound familiar?", "de": "Kommt Ihnen das bekannt vor?", "fr": "Vous vous reconnaissez ?"},
    "pain_h": {
        "it": "Quattro situazioni frequenti — e come le evito",
        "en": "Four common situations — and how I help you avoid them",
        "de": "Vier häufige Situationen — und wie ich sie vermeide",
        "fr": "Quatre situations fréquentes — et comment je vous aide à les éviter",
    },
    "adv_k": {"it": "Perché affidarti a un consulente", "en": "Why work with an advisor", "de": "Warum ein Berater", "fr": "Pourquoi un conseiller"},
    "adv_h": {
        "it": "Quattro vantaggi reali quando compri con me",
        "en": "Four real advantages when you buy with me",
        "de": "Vier echte Vorteile beim Kauf mit mir",
        "fr": "Quatre avantages réels quand vous achetez avec moi",
    },
    "a1t": {"it": "Il prezzo giusto", "en": "The right price", "de": "Der richtige Preis", "fr": "Le bon prix"},
    "a1p": {
        "it": "Analisi della micro-zona sui dati ufficiali OMI: sai se quella casa vale davvero il prezzo richiesto, prima di fare un'offerta.",
        "en": "Micro-area analysis based on official OMI data: you know whether that home is truly worth the asking price before making an offer.",
        "de": "Mikrozonenanalyse auf offiziellen OMI-Daten: Sie wissen, ob das Haus den Preis wirklich wert ist, bevor Sie ein Angebot machen.",
        "fr": "Analyse de micro-zone sur données OMI officielles : vous savez si ce bien vaut vraiment le prix demandé avant de faire une offre.",
    },
    "a2t": {"it": "La rete RE/MAX", "en": "The RE/MAX network", "de": "Das RE/MAX-Netzwerk", "fr": "Le réseau RE/MAX"},
    "a2p": {
        "it": "A volte è possibile conoscere immobili in arrivo prima che finiscano sui portali.",
        "en": "It is sometimes possible to see upcoming listings before they hit the portals.",
        "de": "Manchmal sind künftige Objekte sichtbar, bevor sie auf den Portalen erscheinen.",
        "fr": "Il est parfois possible de voir des biens à venir avant qu'ils n'apparaissent sur les portails.",
    },
    "a3t": {"it": "La verifica prima di comprare", "en": "Checks before you buy", "de": "Prüfung vor dem Kauf", "fr": "Vérification avant d'acheter"},
    "a3p": {
        "it": "Conformità urbanistica e catastale, difformità, documenti: controlli fatti prima dell'acquisto.",
        "en": "Urban planning and cadastral compliance, discrepancies, documents: checks done before the purchase.",
        "de": "Stadtplanung, Kataster, Abweichungen, Dokumente: Prüfungen vor dem Kauf.",
        "fr": "Conformité urbanistique et cadastrale, difformités, documents : contrôles avant l'achat.",
    },
    "a4t": {"it": "Ricerca su misura", "en": "Tailored search", "de": "Maßgeschneiderte Suche", "fr": "Recherche sur mesure"},
    "a4p": {
        "it": "Mi dici cosa cerchi una volta sola. Ti avviso quando esce qualcosa davvero in linea.",
        "en": "Tell me what you need once. I alert you when something truly relevant appears.",
        "de": "Sagen Sie mir einmal, was Sie suchen. Ich benachrichtige Sie bei wirklich passenden Objekten.",
        "fr": "Dites-moi une fois ce que vous cherchez. Je vous alerte quand un bien vraiment pertinent apparaît.",
    },
    "trust_k": {"it": "Chi ti affianca", "en": "Who supports you", "de": "Wer Sie begleitet", "fr": "Qui vous accompagne"},
    "trust_h": {
        "it": "Non un portale. Una persona con numeri e metodo.",
        "en": "Not a portal. A person with data and method.",
        "de": "Kein Portal. Eine Person mit Zahlen und Methode.",
        "fr": "Pas un portail. Une personne avec des chiffres et une méthode.",
    },
    "portrait_sub": {
        "it": "Agente RE/MAX · {city} e Provincia",
        "en": "RE/MAX Agent · {city} and province",
        "de": "RE/MAX-Berater · {city} und Provinz",
        "fr": "Agent RE/MAX · {city} et province",
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
    "s1t": {"it": "Mi dici cosa cerchi", "en": "You tell me what you need", "de": "Sie sagen mir, was Sie suchen", "fr": "Vous me dites ce que vous cherchez"},
    "s1p": {
        "it": "Zona, tipologia, budget e tempi. Bastano due minuti dal modulo.",
        "en": "Area, property type, budget and timing. Two minutes using the form.",
        "de": "Zone, Typ, Budget und Zeitrahmen. Zwei Minuten im Formular.",
        "fr": "Zone, type, budget et délais. Deux minutes via le formulaire.",
    },
    "s2t": {"it": "Analisi e selezione mirata", "en": "Analysis and targeted selection", "de": "Analyse und gezielte Auswahl", "fr": "Analyse et sélection ciblée"},
    "s2p": {
        "it": "Cerco, filtro e verifico prezzo e documenti. Ti propongo solo ciò che ha senso.",
        "en": "I search, filter, verify fair price and documents. I only propose what truly makes sense.",
        "de": "Ich suche, filtere und prüfe Preis und Dokumente. Nur was wirklich Sinn ergibt.",
        "fr": "Je cherche, filtre et vérifie prix et documents. Je ne propose que ce qui a du sens.",
    },
    "s3t": {"it": "Trattativa e acquisto", "en": "Negotiation and purchase", "de": "Verhandlung und Kauf", "fr": "Négociation et achat"},
    "s3p": {
        "it": "Ti affianco fino al rogito, perché tu compri al prezzo giusto e in sicurezza.",
        "en": "I support you through negotiation and closing, so you buy at the right price and with confidence.",
        "de": "Ich begleite Sie bis zum Notartermin — zum richtigen Preis und in Sicherheit.",
        "fr": "Je vous accompagne jusqu'à la signature, pour acheter au bon prix en toute sécurité.",
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
    "form_h": {"it": "Dimmi cosa cerchi", "en": "Tell me what you need", "de": "Was suchen Sie?", "fr": "Dites-moi ce que vous cherchez"},
    "form_p": {
        "it": "Registra la tua ricerca: ti avviso quando trovo qualcosa in linea, e ti dico se il prezzo è giusto.",
        "en": "Register your search: I will alert you when I find something relevant, and tell you whether the price is fair.",
        "de": "Registrieren Sie Ihre Suche: Ich melde mich bei passenden Objekten und sage, ob der Preis stimmt.",
        "fr": "Enregistrez votre recherche : je vous alerte quand je trouve quelque chose de pertinent et si le prix est juste.",
    },
    "form_aside_h": {
        "it": "Compra con i numeri giusti, non con l'ansia.",
        "en": "Buy with the right numbers, not with anxiety.",
        "de": "Kaufen mit den richtigen Zahlen, nicht mit Angst.",
        "fr": "Achetez avec les bons chiffres, pas avec l'anxiété.",
    },
    "form_aside_p": {
        "it": "Compila il modulo: è il primo passo per una ricerca mirata e una valutazione seria del prezzo.",
        "en": "Fill in the form: it is the first step toward a targeted search and a serious price assessment.",
        "de": "Füllen Sie das Formular aus — der erste Schritt zu gezielter Suche und seriöser Preisbewertung.",
        "fr": "Remplissez le formulaire : premier pas vers une recherche ciblée et une évaluation sérieuse du prix.",
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
    "submit": {"it": "Registra la mia ricerca →", "en": "Register my search →", "de": "Suche registrieren →", "fr": "Enregistrer ma recherche →"},
    "form_note": {
        "it": "Risposta entro 24 ore · Nessun obbligo di incarico",
        "en": "Reply within 24 hours · No obligation to appoint",
        "de": "Antwort innerhalb von 24h · Keine Verpflichtung zum Mandat",
        "fr": "Réponse sous 24h · Aucune obligation de mandat",
    },
    "final_h": {
        "it": "Pronto a cercare casa con un metodo, non a caso?",
        "en": "Ready to search with a method, not by chance?",
        "de": "Bereit, mit Methode zu suchen — nicht dem Zufall?",
        "fr": "Prêt à chercher avec une méthode, pas au hasard ?",
    },
    "final_p": {
        "it": "Registra cosa cerchi. Ti richiamo entro 24 ore con un approccio chiaro — nessun obbligo di incarico.",
        "en": "Tell me what you need. I will call you back within 24 hours with a clear approach — no obligation to appoint.",
        "de": "Sagen Sie mir, was Sie suchen. Rückruf innerhalb von 24h — keine Verpflichtung zum Mandat.",
        "fr": "Dites-moi ce que vous cherchez. Je vous rappelle sous 24h — aucune obligation de mandat.",
    },
    "sticky": {"it": "Dimmi cosa cerchi", "en": "Tell me what you need", "de": "Was suchen Sie?", "fr": "Votre recherche"},
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
