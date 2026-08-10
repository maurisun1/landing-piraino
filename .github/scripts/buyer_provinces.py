"""Content and metadata for Lombard buyer landing pages."""

LOMBARD_PROVINCES = [
    ("milano", "Milano", "Milan"),
    ("monza", "Monza e Brianza", "Monza and Brianza"),
    ("bergamo", "Bergamo", "Bergamo"),
    ("brescia", "Brescia", "Brescia"),
    ("como", "Como", "Como"),
    ("varese", "Varese", "Varese"),
    ("lecco", "Lecco", "Lecco"),
    ("sondrio", "Sondrio", "Sondrio"),
    ("cremona", "Cremona", "Cremona"),
    ("lodi", "Lodi", "Lodi"),
    ("mantova", "Mantova", "Mantova"),
    ("pavia", "Pavia", "Pavia"),
]

def seller_link_for(slug: str) -> str:
    from locales import seller_url

    return seller_url(slug, "it")


SELLER_LINKS = {slug: seller_link_for(slug) for slug, _name, _en in LOMBARD_PROVINCES}

OMI_LINKS = {
    "milano": "/guida-prezzi-mq-milano/",
    "brescia": "/guida-prezzi-mq-brescia/",
    "bergamo": "/guida-prezzi-mq-bergamo/",
}

AGENCY_NAME = "RE/MAX Associati Real Estate"
AGENCY_ADDRESS = "Viale Gran Sasso 31, Milano"
AGENCY_CREDENTIALS_IT = "oltre 25 anni di attività · tra le prime 30 agenzie RE/MAX in Italia"
AGENCY_CREDENTIALS_EN = "over 25 years on the market · among the top 30 RE/MAX offices in Italy"

FOOTER_AFFILIATION_IT = (
    "Maurizio Piraino — Consulente immobiliare presso RE/MAX Associati Real Estate "
    "· Milano, Viale Gran Sasso 31"
)
FOOTER_AFFILIATION_EN = (
    "Maurizio Piraino — Real estate consultant at RE/MAX Associati Real Estate "
    "· Milan, Viale Gran Sasso 31"
)

ABOUT_AGENCY_IT = (
    "Opero come consulente immobiliare con RE/MAX Associati Real Estate a Milano, agenzia con "
    "oltre 25 anni di attività sul mercato e tra le prime 30 RE/MAX in Italia. Questo mi "
    "permette di unire un metodo consulenziale personale alla forza di una rete internazionale."
)
ABOUT_AGENCY_EN = (
    "I work as a real estate consultant with RE/MAX Associati Real Estate in Milan, an agency with "
    "over 25 years on the market and among the top 30 RE/MAX offices in Italy. This lets me "
    "combine a personal advisory approach with the strength of an international network."
)

DEFAULT_BUDGET_PROVINCE = [
    ("", "Preferisco non indicarlo"),
    ("150000", "Fino a 150.000 €"),
    ("150000-250000", "150.000 - 250.000 €"),
    ("250000-400000", "250.000 - 400.000 €"),
    ("400000-600000", "400.000 - 600.000 €"),
    ("600000+", "Oltre 600.000 €"),
]

MILANO_BUDGET = [
    ("", "Preferisco non indicarlo"),
    ("200000", "Fino a 200.000 €"),
    ("200000-350000", "200.000 - 350.000 €"),
    ("350000-500000", "350.000 - 500.000 €"),
    ("500000-800000", "500.000 - 800.000 €"),
    ("800000+", "Oltre 800.000 €"),
]

DEFAULT_STATS_IT = [
    ("OMI", "Dati ufficiali Agenzia Entrate"),
    ("24h", "Risposta alla tua richiesta"),
    ("✓", "Nessun obbligo di incarico"),
    ("RE/MAX", "Rete internazionale"),
]

DEFAULT_TRUST_IT = [
    ("OMI", "Prezzo basato su dati ufficiali"),
    ("RE/MAX", "Accesso alla rete MLS"),
    ("Geometra", "Verifica tecnica reale"),
]

DEFAULT_PAIN_IT = [
    ("01", "Hai paura di pagare troppo", "Vedi una casa che ti piace e non sai se il prezzo richiesto è realistico per quella zona."),
    ("02", "Investi senza numeri chiari", "Redditività, rischio e valorizzazione restano nebulosi: serve analisi prima del capitale."),
    ("03", "Perdi tempo tra annunci inutili", "Portali e visite senza Property Finding: settimane su immobili che non erano per te."),
    ("04", "Temi problemi nascosti", "Difformità, documenti, vincoli: scoprirli dopo il rogito è troppo tardi — e costoso."),
]

DEFAULT_HERO_LIST_IT = [
    "Property Finding anche off-market",
    "Verifica documentale prima dell'offerta",
    "Consulenza per casa o investimento",
]

DEFAULT_FORM_BENEFITS_IT = [
    "Ti richiamo entro 24 ore, nessun obbligo di incarico",
    "Property Finding personalizzato per zona e obiettivo",
    "Analisi prezzo e redditività quando investi",
    "Supporto in trattativa fino al rogito",
]

DEFAULT_BUYER_TESTIMONIALS_IT = [
    ("MR", "Acquirente · Milano", "Navigli", "Stavo per fare un'offerta al prezzo richiesto. L'analisi OMI sulla micro-zona mi ha fatto risparmiare circa 15.000 € sulla trattativa."),
    ("GL", "Coppia · prima casa", "Bergamo", "Ci ha evitato di comprare un immobile con difformità catastale. Controlli fatti prima dell'offerta, rogito senza sorprese."),
    ("SF", "Acquirente · Brescia", "Franciacorta", "Mercato competitivo: grazie al tempismo e ai numeri giusti abbiamo chiuso al prezzo corretto, non quello dell'annuncio."),
]

DEFAULT_BUYER_TESTIMONIALS_EN = [
    ("MR", "Buyer · Milan", "Navigli", "I was about to offer the asking price. OMI micro-area analysis saved me around €15,000 in the negotiation."),
    ("GL", "Couple · first home", "Bergamo", "Avoided buying a property with cadastral discrepancies. Checks done before the offer, smooth closing."),
    ("SF", "Buyer · Brescia", "Franciacorta", "Competitive market: with the right timing and numbers we closed at the fair price, not the listing price."),
]

DEFAULT_FAQ_WORK_IT = "Lavori solo in {city}?"
DEFAULT_FAQ_WORK_A_IT = "Seguo acquirenti in tutta la Lombardia, con attenzione particolare a {city} e alle province limitrofe."

NEW_PROVINCES = {
    "como": {
        "hero_img": "/como.jpg",
        "datalist_id": "zoneCO",
        "datalist_it": [
            "Como città", "Cernobbio", "Moltrasio", "Cantù", "Erba",
            "Mariano Comense", "Altra zona provincia Como",
        ],
        "datalist_en": [
            "Como city", "Cernobbio", "Moltrasio", "Cantù", "Erba",
            "Mariano Comense", "Other area in Como province",
        ],
        "footer_geo_it": "Como · Lago di Como · Brianza · Provincia",
        "footer_geo_en": "Como · Lake Como · Brianza · Province",
        "it": {
            "lead": "A Como e sul Lago di Como — dal centro storico alla Brianza comense — ogni micro-zona ha prezzi e tempi diversi. È facile pagare il fascino del lago più del valore reale dell'immobile.",
            "quote": "Sul Lago di Como due ville a pochi minuti possono valere cifre molto diverse. La micro-zona decide — non la vista da cartolina.",
            "about_lead": "Seguo acquirenti su Como città, lago e Brianza. Con dati OMI e verifica tecnica ti aiuto a capire se il prezzo ha senso, prima dell'offerta.",
            "wa_text": "Ciao Maurizio, sto cercando casa a Como e vorrei una consulenza acquirente.",
            "zone_placeholder": "Es. Como centro, Cernobbio, Cantù...",
            "msg_placeholder": "Es. trilocale con vista lago, budget max 450.000 €, max 2° piano...",
            "market": [
                ("Lago di Como", "Fronte lago e borghi", "Mercato premium: domanda interna e internazionale, prezzi che cambiano comune per comune."),
                ("Como città", "Centro e quartieri", "Residenziale solido, forte interesse da chi lavora tra Como e Milano."),
                ("Brianza comense", "Cantù e cintura", "Più spazio e collegamenti verso Milano: prezzi diversi dal lago, ma serve analisi seria."),
            ],
            "pain": [
                ("01", "Pagheresti per la vista, non per la casa", "Sul lago è facile lasciarsi guidare dall'emozione e scoprire dopo che il prezzo era fuori mercato."),
                ("02", "Competi con acquirenti da fuori", "Seconda casa e mercato internazionale: un'offerta sbagliata ti fa perdere l'immobile o pagarlo troppo."),
                ("03", "Non distingui lago da cintura", "Como città, lago e Brianza hanno dinamiche diverse: serve un filtro per zona, non per foto."),
                ("04", "Temi vincoli e destinazioni d'uso", "Fronte lago e centro storico: verifiche urbanistiche cruciali prima dell'offerta."),
            ],
        },
        "en": {
            "lead": "In Como and on Lake Como — from the historic centre to the Brianza belt — each micro-area has different prices and timing. It is easy to pay for lake charm more than the property's real value.",
            "quote": "On Lake Como, two villas minutes apart can be worth very different amounts. The micro-area decides — not the postcard view.",
            "about_lead": "I support buyers in Como city, the lake and Brianza. With OMI data and technical checks I help you understand whether the price makes sense before you offer.",
            "wa_text": "Hi Maurizio, I am looking to buy in Como and would like buyer advisory.",
            "zone_placeholder": "e.g. Como centre, Cernobbio, Cantù...",
            "msg_placeholder": "e.g. three-bedroom with lake view, max budget €450,000, max 2nd floor...",
            "market": [
                ("Lake Como", "Lakefront and villages", "Premium market: local and international demand, prices that change town by town."),
                ("Como city", "Centre and districts", "Solid residential demand, strong interest from those working between Como and Milan."),
                ("Como Brianza", "Cantù and belt towns", "More space and links to Milan: different prices from the lake, but serious analysis still matters."),
            ],
            "pain": [
                ("01", "You would pay for the view, not the home", "On the lake it is easy to follow emotion and discover later the price was off-market."),
                ("02", "You compete with outside buyers", "Second homes and international demand: the wrong offer makes you lose the property or overpay."),
                ("03", "You cannot tell lake from belt towns", "Como city, lake and Brianza have different dynamics: you need a zone filter, not a photo filter."),
                ("04", "You worry about planning restrictions", "Lakefront and historic centre: urban planning checks are crucial before the offer."),
            ],
        },
    },
    "varese": {
        "hero_img": "/varese.jpg",
        "datalist_id": "zoneVA",
        "datalist_it": [
            "Varese città", "Busto Arsizio", "Gallarate", "Saronno", "Induno Olona",
            "Luino / Lombardia dei Laghi", "Altra zona provincia Varese",
        ],
        "datalist_en": [
            "Varese city", "Busto Arsizio", "Gallarate", "Saronno", "Induno Olona",
            "Luino / Lake district", "Other area in Varese province",
        ],
        "footer_geo_it": "Varese · Altomilanese · Prealpi · Laghi",
        "footer_geo_en": "Varese · Milan area · Pre-Alps · Lakes",
        "it": {
            "lead": "In provincia di Varese — tra Prealpi, laghi e cintura nord-ovest di Milano — ogni comune ha dinamiche proprie. Chi esce da Milano cerca spazio, ma i prezzi non sono automaticamente più bassi ovunque.",
            "quote": "Tra Varese, Busto e i comuni prealpini, lo stesso trilocale può cambiare valore in modo netto. La micro-zona va letta prima dell'offerta.",
            "about_lead": "Conosco il mercato varesino e l'Altomilanese: ti aiuto a comprare con numeri OMI e verifica tecnica, non con la fretta del portale.",
            "wa_text": "Ciao Maurizio, sto cercando casa in provincia di Varese e vorrei una consulenza acquirente.",
            "zone_placeholder": "Es. Varese, Busto Arsizio, Gallarate...",
            "msg_placeholder": "Es. trilocale vicino stazione, casa con giardino, budget max 350.000 €...",
            "market": [
                ("Varese città", "Centro e colline", "Qualità di vita, verde e domanda stabile da chi lavora tra Varese e Milano."),
                ("Altomilanese", "Busto, Gallarate, Saronno", "Collegamenti rapidi: mercato dinamico con prezzi che cambiano comune per comune."),
                ("Prealpi e laghi", "Luino e nord provincia", "Seconda casa e lifestyle: serve capire se il prezzo è allineato alla zona reale."),
            ],
        },
        "en": {
            "lead": "In the Province of Varese — between the Pre-Alps, lakes and Milan's north-west belt — each town has its own dynamics. Those leaving Milan seek space, but prices are not automatically lower everywhere.",
            "quote": "Between Varese, Busto and pre-alpine towns, the same three-bedroom can shift sharply in value. The micro-area must be read before the offer.",
            "about_lead": "I know the Varese and north-west Milan market: I help you buy with OMI numbers and technical checks, not portal urgency.",
            "wa_text": "Hi Maurizio, I am looking to buy in the Province of Varese and would like buyer advisory.",
            "zone_placeholder": "e.g. Varese, Busto Arsizio, Gallarate...",
            "msg_placeholder": "e.g. three-bedroom near station, home with garden, max budget €350,000...",
            "market": [
                ("Varese city", "Centre and hills", "Quality of life, green surroundings and stable demand from those working between Varese and Milan."),
                ("North-west Milan", "Busto, Gallarate, Saronno", "Fast connections: dynamic market with prices that change town by town."),
                ("Pre-Alps and lakes", "Luino and north province", "Second homes and lifestyle: you need to know if the price fits the real area."),
            ],
        },
    },
    "lecco": {
        "hero_img": "/lecco.jpg",
        "datalist_id": "zoneLC",
        "datalist_it": [
            "Lecco città", "Merate", "Calolziocorte", "Valmadrera", "Ballabio",
            "Valsassina", "Altra zona provincia Lecco",
        ],
        "datalist_en": [
            "Lecco city", "Merate", "Calolziocorte", "Valmadrera", "Ballabio",
            "Valsassina", "Other area in Lecco province",
        ],
        "footer_geo_it": "Lecco · Lago · Brianza · Valsassina",
        "footer_geo_en": "Lecco · Lake · Brianza · Valsassina",
        "it": {
            "lead": "A Lecco e in provincia — tra lago, Brianza e Valsassina — il mercato cambia rapidamente da un comune all'altro. Spazio e natura attirano, ma i prezzi vanno verificati zona per zona.",
            "quote": "Lecco città, lago e Valsassina non sono lo stesso mercato. Comprare senza micro-analisi significa pagare il paesaggio, non il valore.",
            "about_lead": "Ti affianco su Lecco, lago e Brianza lecchese con analisi OMI e controlli tecnici prima dell'offerta.",
            "wa_text": "Ciao Maurizio, sto cercando casa a Lecco e vorrei una consulenza acquirente.",
            "zone_placeholder": "Es. Lecco centro, Merate, Valmadrera...",
            "msg_placeholder": "Es. trilocale Lecco lago, casa in Valsassina, budget max 300.000 €...",
            "market": [
                ("Lecco e lago", "Centro e riviera", "Domanda solida, prezzi sensibili a vista lago e servizi."),
                ("Brianza lecchese", "Merate e cintura", "Chi esce da Milano cerca equilibrio tra spazio e collegamenti."),
                ("Valsassina", "Montagna e borghi", "Qualità di vita e seconda casa: numeri OMI ancora più decisivi."),
            ],
        },
        "en": {
            "lead": "In Lecco and its province — between lake, Brianza and Valsassina — the market shifts quickly from one town to the next. Space and nature attract buyers, but prices must be checked area by area.",
            "quote": "Lecco city, the lake and Valsassina are not the same market. Buying without micro-analysis means paying for the landscape, not the value.",
            "about_lead": "I support you in Lecco, the lake and Brianza with OMI analysis and technical checks before the offer.",
            "wa_text": "Hi Maurizio, I am looking to buy in Lecco and would like buyer advisory.",
            "zone_placeholder": "e.g. Lecco centre, Merate, Valmadrera...",
            "msg_placeholder": "e.g. three-bedroom in Lecco by the lake, home in Valsassina, max budget €300,000...",
            "market": [
                ("Lecco and lake", "Centre and waterfront", "Solid demand, prices sensitive to lake view and services."),
                ("Lecco Brianza", "Merate and belt towns", "Those leaving Milan seek balance between space and connections."),
                ("Valsassina", "Mountains and villages", "Quality of life and second homes: OMI numbers are even more decisive."),
            ],
        },
    },
    "monza": {
        "hero_img": "/monza.jpg",
        "budget": MILANO_BUDGET,
        "datalist_id": "zoneMB",
        "datalist_it": [
            "Monza", "Seregno", "Desio", "Lissone", "Vimercate",
            "Cesano Maderno", "Altra zona Monza Brianza",
        ],
        "datalist_en": [
            "Monza", "Seregno", "Desio", "Lissone", "Vimercate",
            "Cesano Maderno", "Other area in Monza and Brianza",
        ],
        "footer_geo_it": "Monza · Brianza · Seregno · Vimercate",
        "footer_geo_en": "Monza · Brianza · Seregno · Vimercate",
        "it": {
            "lead": "In Monza e Brianza — a due passi da Milano — la domanda è alta e i tempi sono rapidi. È facile pagare troppo per la vicinanza alla città o perdere casa per un'offerta mal calibrata.",
            "quote": "In Brianza il prezzo giusto cambia da Monza a Seregno, da Desio a Vimercate. La micro-zona vale più di dieci annunci scorrevoli.",
            "about_lead": "Seguo acquirenti in Brianza e Monza: analisi OMI, tempismo e verifica tecnica per comprare bene, non in fretta.",
            "wa_text": "Ciao Maurizio, sto cercando casa in Monza e Brianza e vorrei una consulenza acquirente.",
            "zone_placeholder": "Es. Monza, Seregno, Vimercate...",
            "msg_placeholder": "Es. trilocale Monza centro, vicino stazione, budget max 450.000 €...",
            "market": [
                ("Monza", "Centro e ville", "Alta domanda residenziale, forte competizione tra acquirenti."),
                ("Brianza", "Seregno, Desio, Lissone", "Spazio e collegamenti: mercato veloce con prezzi in crescita selettiva."),
                ("Vimercate e est", "Verso Bergamo", "Transizione verso altri mercati lombardi: serve confronto micro-zona per micro-zona."),
            ],
            "pain": [
                ("01", "Paghi il premium Brianza senza saperlo", "Vicino Milano non significa automaticamente prezzo giusto: ogni comune ha la sua curva."),
                ("02", "Perdi casa in pochi giorni", "Mercato rapido: senza numeri arrivi tardi o offri troppo."),
                ("03", "Confondi Monza con la provincia", "Monza città e comuni limitrofi hanno dinamiche diverse — servono filtri precisi."),
                ("04", "Non verifichi prima dell'offerta", "In Brianza, controlli tecnici prima dell'offerta evitano sorprese costose."),
            ],
        },
        "en": {
            "lead": "In Monza and Brianza — minutes from Milan — demand is high and timing is fast. It is easy to overpay for proximity to the city or lose a home with a poorly calibrated offer.",
            "quote": "In Brianza the right price changes from Monza to Seregno, from Desio to Vimercate. The micro-area is worth more than ten scrolling listings.",
            "about_lead": "I support buyers in Monza and Brianza: OMI analysis, timing and technical checks to buy well, not in a hurry.",
            "wa_text": "Hi Maurizio, I am looking to buy in Monza and Brianza and would like buyer advisory.",
            "zone_placeholder": "e.g. Monza, Seregno, Vimercate...",
            "msg_placeholder": "e.g. three-bedroom in Monza centre, near station, max budget €450,000...",
            "market": [
                ("Monza", "Centre and villas", "High residential demand, strong competition among buyers."),
                ("Brianza", "Seregno, Desio, Lissone", "Space and connections: fast market with selective price growth."),
                ("Vimercate and east", "Towards Bergamo", "Transition to other Lombard markets: micro-area comparison is essential."),
            ],
        },
    },
    "sondrio": {
        "hero_img": "/sondrio.jpg",
        "datalist_id": "zoneSO",
        "datalist_it": [
            "Sondrio città", "Tirano", "Morbegno", "Bormio", "Livigno",
            "Valmalenco", "Altra zona provincia Sondrio",
        ],
        "datalist_en": [
            "Sondrio city", "Tirano", "Morbegno", "Bormio", "Livigno",
            "Valmalenco", "Other area in Sondrio province",
        ],
        "footer_geo_it": "Sondrio · Valtellina · Bormio · Livigno",
        "footer_geo_en": "Sondrio · Valtellina · Bormio · Livigno",
        "it": {
            "lead": "In Valtellina e provincia di Sondrio — tra montagna, turismo e residenziale — ogni valle ha regole diverse. Seconda casa e prima casa richiedono analisi diverse, ma sempre basate sui numeri.",
            "quote": "Tra Sondrio, Morbegno e le località turistiche, lo stesso immobile può avere logiche di prezzo opposte. La valle conta più della superficie.",
            "about_lead": "Ti aiuto a comprare in Valtellina con analisi OMI e verifiche tecniche, che cerchi casa abituale o seconda residenza.",
            "wa_text": "Ciao Maurizio, sto cercando casa in provincia di Sondrio e vorrei una consulenza acquirente.",
            "zone_placeholder": "Es. Sondrio, Tirano, Bormio, Livigno...",
            "msg_placeholder": "Es. bilocale Sondrio, chalet Valmalenco, budget max 250.000 €...",
            "market": [
                ("Valtellina centrale", "Sondrio e Morbegno", "Residenziale stabile, prezzi legati a servizi e collegamenti."),
                ("Turismo alpino", "Bormio e Livigno", "Mercato stagionale e premium: analisi OMI ancora più importante."),
                ("Valli laterali", "Valmalenco e Tirano", "Seconda casa e lifestyle: attenzione a vincoli e destinazioni d'uso."),
            ],
            "pain": [
                ("01", "Confondi turismo e residenziale", "A Livigno o Bormio le logiche di prezzo non sono quelle di Sondrio città."),
                ("02", "Sottovaluti vincoli montani", "Destinazioni d'uso e vincoli alpini: da verificare prima dell'offerta."),
                ("03", "Compri emozione montagna", "Vista e chalet possono costare più del valore OMI della micro-zona."),
                ("04", "Non hai referenze locali", "In Valtellina serve chi legge il mercato valle per valle, non annunci generici."),
            ],
        },
        "en": {
            "lead": "In Valtellina and the Province of Sondrio — between mountains, tourism and residential areas — each valley has different rules. Second homes and primary homes need different analysis, but always based on numbers.",
            "quote": "Between Sondrio, Morbegno and tourist towns, the same property can follow opposite price logic. The valley matters more than square metres.",
            "about_lead": "I help you buy in Valtellina with OMI analysis and technical checks, whether you want a primary or second home.",
            "wa_text": "Hi Maurizio, I am looking to buy in the Province of Sondrio and would like buyer advisory.",
            "zone_placeholder": "e.g. Sondrio, Tirano, Bormio, Livigno...",
            "msg_placeholder": "e.g. two-bedroom in Sondrio, chalet in Valmalenco, max budget €250,000...",
            "market": [
                ("Central Valtellina", "Sondrio and Morbegno", "Stable residential market, prices linked to services and connections."),
                ("Alpine tourism", "Bormio and Livigno", "Seasonal premium market: OMI analysis is even more important."),
                ("Side valleys", "Valmalenco and Tirano", "Second homes and lifestyle: watch planning rules and permitted use."),
            ],
        },
    },
    "cremona": {
        "hero_img": "/cremona.jpg",
        "datalist_id": "zoneCR",
        "datalist_it": [
            "Cremona città", "Crema", "Casalmaggiore", "Castelleone", "Pandino",
            "Altra zona provincia Cremona",
        ],
        "datalist_en": [
            "Cremona city", "Crema", "Casalmaggiore", "Castelleone", "Pandino",
            "Other area in Cremona province",
        ],
        "footer_geo_it": "Cremona · Crema · Pianura · Po",
        "footer_geo_en": "Cremona · Crema · Plain · Po Valley",
        "it": {
            "lead": "A Cremona e in provincia — tra capoluogo, pianura e area di Crema — il mercato è più tranquillo di Milano, ma pagare troppo resta possibile se non confronti la micro-zona.",
            "quote": "Cremona città e Crema non seguono la stessa curva di prezzo. Anche in provincia tranquilla, la micro-analisi evita errori costosi.",
            "about_lead": "Ti affianco su Cremona, Crema e pianura con dati OMI e verifica tecnica, per una scelta serena ma non ingenua.",
            "wa_text": "Ciao Maurizio, sto cercando casa a Cremona e vorrei una consulenza acquirente.",
            "zone_placeholder": "Es. Cremona centro, Crema, Castelleone...",
            "msg_placeholder": "Es. trilocale Cremona, casa in campagna, budget max 220.000 €...",
            "market": [
                ("Cremona città", "Centro e quartieri", "Mercato residenziale stabile, prezzi legati a servizi e stato immobile."),
                ("Area Crema", "Est provincia", "Dinamiche proprie rispetto al capoluogo: confronto OMI essenziale."),
                ("Pianura", "Comuni minori", "Più spazio e prezzi accessibili, ma attenzione a documenti e conformità."),
            ],
        },
        "en": {
            "lead": "In Cremona and its province — between the main town, the plain and the Crema area — the market is calmer than Milan, but overpaying is still possible without micro-area comparison.",
            "quote": "Cremona city and Crema do not follow the same price curve. Even in a quieter province, micro-analysis avoids costly mistakes.",
            "about_lead": "I support you in Cremona, Crema and the plain with OMI data and technical checks, for a calm but not naive choice.",
            "wa_text": "Hi Maurizio, I am looking to buy in Cremona and would like buyer advisory.",
            "zone_placeholder": "e.g. Cremona centre, Crema, Castelleone...",
            "msg_placeholder": "e.g. three-bedroom in Cremona, country home, max budget €220,000...",
            "market": [
                ("Cremona city", "Centre and districts", "Stable residential market, prices linked to services and condition."),
                ("Crema area", "East province", "Its own dynamics versus the main town: OMI comparison is essential."),
                ("The plain", "Smaller towns", "More space and accessible prices, but watch documents and compliance."),
            ],
        },
    },
    "lodi": {
        "hero_img": "/lodi.jpg",
        "datalist_id": "zoneLO",
        "datalist_it": [
            "Lodi città", "Codogno", "Casalpusterlengo", "Sant'Angelo Lodigiano",
            "Altra zona provincia Lodi",
        ],
        "datalist_en": [
            "Lodi city", "Codogno", "Casalpusterlengo", "Sant'Angelo Lodigiano",
            "Other area in Lodi province",
        ],
        "footer_geo_it": "Lodi · Pianura · Lodigiano · Po",
        "footer_geo_en": "Lodi · Plain · Lodi area · Po Valley",
        "it": {
            "lead": "A Lodi e in provincia — nel cuore della pianura lodigiana — i prezzi possono sembrare più accessibili, ma difformità, stato immobile e micro-zona fanno comunque la differenza.",
            "quote": "In provincia di Lodi il risparmio iniziale non vale nulla se compri un immobile con problemi tecnici nascosti.",
            "about_lead": "Ti aiuto a comprare nel Lodigiano con analisi OMI e controlli prima dell'offerta, senza sorprese al rogito.",
            "wa_text": "Ciao Maurizio, sto cercando casa a Lodi e vorrei una consulenza acquirente.",
            "zone_placeholder": "Es. Lodi centro, Codogno, Casalpusterlengo...",
            "msg_placeholder": "Es. bilocale Lodi, casa con giardino, budget max 180.000 €...",
            "market": [
                ("Lodi città", "Centro storico", "Mercato compatto, attenzione a stato immobile e servizi."),
                ("Pianura lodigiana", "Comuni medio-piccoli", "Prezzi accessibili, verifica tecnica spesso decisiva."),
                ("Collegamenti", "Verso Milano e Pavia", "Scelte legate a spostamenti: la zona giusta dipende dai tuoi numeri."),
            ],
        },
        "en": {
            "lead": "In Lodi and its province — in the heart of the Lodi plain — prices may look more accessible, but discrepancies, condition and micro-area still make the difference.",
            "quote": "In the Province of Lodi initial savings mean nothing if you buy a property with hidden technical issues.",
            "about_lead": "I help you buy in the Lodi area with OMI analysis and checks before the offer, with no surprises at closing.",
            "wa_text": "Hi Maurizio, I am looking to buy in Lodi and would like buyer advisory.",
            "zone_placeholder": "e.g. Lodi centre, Codogno, Casalpusterlengo...",
            "msg_placeholder": "e.g. two-bedroom in Lodi, home with garden, max budget €180,000...",
            "market": [
                ("Lodi city", "Historic centre", "Compact market, focus on condition and services."),
                ("Lodi plain", "Mid-small towns", "Accessible prices, technical checks often decisive."),
                ("Connections", "Towards Milan and Pavia", "Commute-driven choices: the right area depends on your numbers."),
            ],
        },
    },
    "mantova": {
        "hero_img": "/mantova.jpg",
        "datalist_id": "zoneMN",
        "datalist_it": [
            "Mantova città", "Suzzara", "Virgilio", "Porto Mantovana", "Asola",
            "Altra zona provincia Mantova",
        ],
        "datalist_en": [
            "Mantova city", "Suzzara", "Virgilio", "Porto Mantovana", "Asola",
            "Other area in Mantova province",
        ],
        "footer_geo_it": "Mantova · Mincio · Pianura · Lungo Po",
        "footer_geo_en": "Mantova · Mincio · Plain · Po Valley",
        "it": {
            "lead": "A Mantova e in provincia — tra centro UNESCO, pianura e confine con Veneto ed Emilia — ogni comune ha dinamiche proprie. Un prezzo apparentemente conveniente può nascondere criticità tecniche.",
            "quote": "Mantova città e i comuni della pianura non condividono la stessa domanda. La micro-zona va letta con attenzione.",
            "about_lead": "Seguo acquirenti su Mantova e provincia con analisi OMI e verifica documentale, prima che tu vada in trattativa.",
            "wa_text": "Ciao Maurizio, sto cercando casa a Mantova e vorrei una consulenza acquirente.",
            "zone_placeholder": "Es. Mantova centro, Suzzara, Virgilio...",
            "msg_placeholder": "Es. trilocale Mantova, casa in campagna, budget max 200.000 €...",
            "market": [
                ("Mantova città", "Centro storico", "Appeal culturale e residenziale, prezzi legati a tipologia e posizione."),
                ("Pianura mantovana", "Comuni sparsi", "Più spazio, attenzione a bonifiche e conformità."),
                ("Confini regionali", "Suzzara e sud", "Mercato influenzato anche da Veneto ed Emilia: serve confronto reale."),
            ],
        },
        "en": {
            "lead": "In Mantova and its province — between the UNESCO centre, the plain and the border with Veneto and Emilia — each town has its own dynamics. An apparently convenient price can hide technical issues.",
            "quote": "Mantova city and plain towns do not share the same demand. The micro-area must be read carefully.",
            "about_lead": "I support buyers in Mantova and province with OMI analysis and document checks before you negotiate.",
            "wa_text": "Hi Maurizio, I am looking to buy in Mantova and would like buyer advisory.",
            "zone_placeholder": "e.g. Mantova centre, Suzzara, Virgilio...",
            "msg_placeholder": "e.g. three-bedroom in Mantova, country home, max budget €200,000...",
            "market": [
                ("Mantova city", "Historic centre", "Cultural and residential appeal, prices linked to type and location."),
                ("Mantova plain", "Spread-out towns", "More space, watch land reclamation and compliance."),
                ("Regional borders", "Suzzara and south", "Market influenced by Veneto and Emilia: real comparison needed."),
            ],
        },
    },
    "pavia": {
        "hero_img": "/pavia.jpg",
        "datalist_id": "zonePV",
        "datalist_it": [
            "Pavia città", "Vigevano", "Mortara", "Broni", "Voghera",
            "Oltrepò Pavese", "Altra zona provincia Pavia",
        ],
        "datalist_en": [
            "Pavia city", "Vigevano", "Mortara", "Broni", "Voghera",
            "Oltrepò Pavese", "Other area in Pavia province",
        ],
        "footer_geo_it": "Pavia · Oltrepò · Lomellina · Voghera",
        "footer_geo_en": "Pavia · Oltrepò · Lomellina · Voghera",
        "it": {
            "lead": "A Pavia e in provincia — tra università, Oltrepò e Lomellina — il mercato varia molto da zona a zona. È facile sottovalutare differenze di prezzo tra città, collina e pianura.",
            "quote": "Pavia città, Oltrepò e Lomellina sono tre mercati diversi. Comprare senza micro-analisi significa pagare la zona sbagliata.",
            "about_lead": "Ti affianco su Pavia, Oltrepò e Lomellina con dati OMI e verifica tecnica, per comprare al prezzo giusto.",
            "wa_text": "Ciao Maurizio, sto cercando casa a Pavia e vorrei una consulenza acquirente.",
            "zone_placeholder": "Es. Pavia centro, Vigevano, Oltrepò...",
            "msg_placeholder": "Es. trilocale Pavia, cascina Oltrepò, budget max 250.000 €...",
            "market": [
                ("Pavia città", "Università e centro", "Domanda stabile, mercato influenzato da locazioni e famiglie."),
                ("Oltrepò Pavese", "Collina e borghi", "Seconda casa e lifestyle: prezzi legati a micro-borgo e accessi."),
                ("Lomellina", "Pianura occidentale", "Prezzi più accessibili, verifica tecnica spesso decisiva."),
            ],
        },
        "en": {
            "lead": "In Pavia and its province — between the university city, Oltrepò and Lomellina — the market varies sharply by area. It is easy to underestimate price gaps between city, hills and plain.",
            "quote": "Pavia city, Oltrepò and Lomellina are three different markets. Buying without micro-analysis means paying for the wrong area.",
            "about_lead": "I support you in Pavia, Oltrepò and Lomellina with OMI data and technical checks, to buy at the right price.",
            "wa_text": "Hi Maurizio, I am looking to buy in Pavia and would like buyer advisory.",
            "zone_placeholder": "e.g. Pavia centre, Vigevano, Oltrepò...",
            "msg_placeholder": "e.g. three-bedroom in Pavia, farmhouse in Oltrepò, max budget €250,000...",
            "market": [
                ("Pavia city", "University and centre", "Stable demand, market shaped by rentals and families."),
                ("Oltrepò Pavese", "Hills and villages", "Second homes and lifestyle: prices tied to village and access."),
                ("Lomellina", "Western plain", "More accessible prices, technical checks often decisive."),
            ],
        },
    },
}
