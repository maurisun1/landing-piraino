"""Professional DE/FR buyer content for Lombard province pages."""

from __future__ import annotations

# Province-specific body copy (lead, market, pain, etc.) — not UI labels.
_BLOCKS: dict[str, dict[str, dict]] = {
    "milano": {
        "de": {
            "lead": "Der Mailänder Markt ist schnell und wettbewerbsintensiv: zu viel zu zahlen, zu spät zu kommen oder mit versteckten Mängeln zu kaufen passiert leicht. Meine Aufgabe ist es, Ihnen dabei zu helfen, das zu vermeiden.",
            "quote": "In Mailand ändert sich der richtige Preis von Straße zu Straße. Eine OMI-Mikrozonenanalyse ist mehr wert als zehn zufällige Besichtigungen.",
            "about_lead": "Mailand ist dynamisch und wettbewerbsintensiv. Ich helfe Ihnen zu verstehen, ob eine Immobilie den geforderten Preis wirklich wert ist, mit dem richtigen Timing zu handeln und Probleme nicht erst nach Ihrem Angebot zu entdecken.",
            "wa_text": "Guten Tag Maurizio, ich suche eine Immobilie in Mailand und möchte eine Käuferberatung.",
            "zone_placeholder": "z. B. Navigli, Sesto San Giovanni …",
            "msg_placeholder": "z. B. helle Dreizimmerwohnung mit Balkon, nah Metro, max. 3. OG …",
            "footer_geo": "Mailand · Provinz · Navigli · Isola",
            "market": [
                ("Mailand Stadt", "Zentrale Lagen", "Hohe Nachfrage, schnelle Zeiten: ein falscher Preis ist teuer."),
                ("Provinz", "Gemeinden MI", "Mehr Raum, andere Preise — aber jede Gemeinde hat eigene Dynamiken."),
                ("Investition", "Lage und Infrastruktur", "Metro, Schulen, Aufwertung: der reale Wert liegt nicht nur in den Quadratmetern."),
            ],
            "pain": [
                ("01", "Sie verlieren eine Immobilie innerhalb von Minuten", "Schneller Markt: ohne die richtigen Zahlen kommen Sie zu spät oder zahlen zu viel."),
                ("02", "Sie können den Preis nicht einschätzen", "Inserate und geforderte Preise spiegeln oft nicht den realen Mikrozonenwert wider."),
                ("03", "Sie sind von Anzeigen überflutet", "Hunderte Inserate: Sie brauchen einen seriösen Filter, keine endlosen Portalsuche."),
                ("04", "Sie befürchten Abweichungen oder Auflagen", "In Mailand vermeiden Prüfungen vor dem Angebot kostspielige Fehler beim Notartermin."),
            ],
            "faq_work": "Arbeiten Sie nur in Mailand?",
            "faq_work_a": "Mailand und Provinz stehen im Mittelpunkt, aber ich begleite Käufer auch in Brescia und Bergamo.",
        },
        "fr": {
            "lead": "Le marché milanais est rapide et compétitif : il est facile de payer trop cher, d'arriver trop tard ou d'acheter un bien avec des problèmes cachés. Mon rôle est de vous aider à éviter cela.",
            "quote": "À Milan, le bon prix change d'une rue à l'autre. Une analyse OMI de micro-zone vaut plus que dix visites au hasard.",
            "about_lead": "Milan est dynamique et compétitif. Je vous aide à comprendre si un bien vaut vraiment le prix demandé, à agir au bon moment et à éviter de découvrir des problèmes après votre offre.",
            "wa_text": "Bonjour Maurizio, je cherche un bien à Milan et souhaite un conseil acheteur.",
            "zone_placeholder": "ex. Navigli, Sesto San Giovanni …",
            "msg_placeholder": "ex. trois pièces lumineux avec balcon, proche métro, max 3e étage …",
            "footer_geo": "Milan · Province · Navigli · Isola",
            "market": [
                ("Milan ville", "Zones centrales", "Forte demande, délais rapides : un mauvais prix coûte cher."),
                ("Province", "Communes MI", "Plus d'espace, prix différents — mais chaque commune a ses dynamiques."),
                ("Investissement", "Emplacement et services", "Métro, écoles, rénovation : la valeur réelle ne se résume pas aux m²."),
            ],
            "pain": [
                ("01", "Vous perdez un bien en quelques minutes", "Marché rapide : sans les bons chiffres, vous arrivez trop tard ou payez trop."),
                ("02", "Vous ne savez pas si le prix est juste", "Annonces et prix demandés ne reflètent souvent pas la vraie valeur de la micro-zone."),
                ("03", "Vous êtes submergé par les annonces", "Des centaines d'annonces : il faut un filtre sérieux, pas des heures sur les portails."),
                ("04", "Vous craignez des non-conformités ou contraintes", "À Milan, les contrôles avant l'offre évitent des erreurs coûteuses à la signature."),
            ],
            "faq_work": "Travaillez-vous uniquement à Milan ?",
            "faq_work_a": "Milan et sa province sont au cœur de mon activité, mais j'accompagne aussi des acheteurs à Brescia et Bergame.",
        },
    },
    "bergamo": {
        "de": {
            "lead": "In Bergamo und Provinz — Città Alta, Città Bassa, Täler und Umlandgemeinden — hat jeder Mikromarkt eigene Regeln. Es ist leicht, zu viel zu zahlen oder mit versteckten Mängeln zu kaufen. Meine Aufgabe ist es, Ihnen dabei zu helfen, das zu vermeiden.",
            "quote": "In Bergamo folgen Città Alta und Città Bassa nicht denselben Regeln. Die Mikrozone vor dem Angebot zu kennen, spart Tausende Euro.",
            "about_lead": "RE/MAX-Berater mit Vermessungs-Hintergrund. Ich kenne Bergamo Zentrum, Täler und Provinz — und sage Ihnen, ob der Preis Sinn ergibt, bevor Sie es nach dem Notartermin feststellen.",
            "wa_text": "Guten Tag Maurizio, ich suche eine Immobilie in Bergamo und möchte eine Käuferberatung.",
            "zone_placeholder": "z. B. Città Alta, Seriate, Treviglio …",
            "msg_placeholder": "z. B. Dreizimmer in Città Bassa, Haus im Val Seriana, max. 2. OG …",
            "footer_geo": "Bergamo · Città Alta · Val Seriana · Provinz",
            "market": [
                ("Bergamo Stadt", "Città Alta und Bassa", "Zwei verschiedene Märkte: solide Nachfrage, Preise und Zeiten ändern sich von Straße zu Straße."),
                ("Täler", "Seriana und Brembana", "Lebensqualität und Grün — aber Sie brauchen trotzdem die richtigen Zahlen."),
                ("Provinz", "Gürtel und Ebene", "Dalmine, Seriate, Treviglio: wer aus Mailand kommt, sucht Raum — aber der Wettbewerb bleibt."),
            ],
            "pain": [
                ("01", "Sie befürchten, zu viel zu zahlen", "Sie finden eine Immobilie, die Ihnen gefällt, und wissen nicht, ob der Preis für diese Straße realistisch ist."),
                ("02", "Sie verpassen die Chance wegen eines falschen Angebots", "Wettbewerbsmarkt: ein zu niedriges Angebot schließt Sie aus, ein zu hohes kostet Sie jahrelang."),
                ("03", "Sie haben keine Zeit für Dutzende Inserate", "Portale, Besichtigungen, Verhandlungen: ohne Filter verlieren Sie Wochen mit falschen Objekten."),
                ("04", "Sie befürchten versteckte Probleme", "Abweichungen, Dokumente, Auflagen: sie nach dem Kauf zu entdecken ist zu spät — und teuer."),
            ],
            "faq_work": "Arbeiten Sie nur in Bergamo?",
            "faq_work_a": "Bergamo, Täler und Provinz sind der Schwerpunkt, aber ich begleite Käufer auch in Mailand und Brescia.",
        },
        "fr": {
            "lead": "À Bergame et en province — Città Alta, Città Bassa, vallées et communes de la couronne — chaque micro-marché a ses règles. Il est facile de payer trop cher ou d'acheter avec des problèmes cachés. Mon rôle est de vous aider à éviter cela.",
            "quote": "À Bergame, Città Alta et Città Bassa ne suivent pas les mêmes règles. Connaître la micro-zone avant l'offre vaut des milliers d'euros.",
            "about_lead": "Agent RE/MAX avec formation de géomètre. Je connais Bergame centre, vallées et province — et je vous dis si le prix a du sens avant que vous ne le découvriez après la signature.",
            "wa_text": "Bonjour Maurizio, je cherche un bien à Bergame et souhaite un conseil acheteur.",
            "zone_placeholder": "ex. Città Alta, Seriate, Treviglio …",
            "msg_placeholder": "ex. trois pièces à Città Bassa, maison en Val Seriana, max 2e étage …",
            "footer_geo": "Bergame · Città Alta · Val Seriana · Province",
            "market": [
                ("Bergame ville", "Città Alta et Bassa", "Deux marchés distincts : demande solide, prix et délais qui changent rue par rue."),
                ("Vallées", "Seriana et Brembana", "Qualité de vie et verdure — mais il faut quand même les bons chiffres."),
                ("Province", "Couronne et plaine", "Dalmine, Seriate, Treviglio : plus d'espace que Milan, mais la concurrence reste réelle."),
            ],
            "pain": [
                ("01", "Vous craignez de payer trop cher", "Vous trouvez un bien qui vous plaît sans savoir si le prix est réaliste pour cette rue."),
                ("02", "Vous perdez l'occasion avec une mauvaise offre", "Marché compétitif : une offre trop basse vous élimine, une offre trop haute vous coûte cher pendant des années."),
                ("03", "Vous n'avez pas le temps pour des dizaines d'annonces", "Portails, visites, négociations : sans filtre vous perdez des semaines sur les mauvais biens."),
                ("04", "Vous craignez des problèmes cachés", "Non-conformités, documents, contraintes : les découvrir après l'achat est trop tard — et coûteux."),
            ],
            "faq_work": "Travaillez-vous uniquement à Bergame ?",
            "faq_work_a": "Bergame, ses vallées et sa province sont au centre, mais j'accompagne aussi des acheteurs à Milan et Brescia.",
        },
    },
    "brescia": {
        "de": {
            "lead": "In Brescia und Provinz — vom Zentrum über Franciacorta bis zum Gardasee und Iseosee — hat jede Zone eigene Dynamiken. Es ist leicht, zu viel zu zahlen, eine Chance zu verpassen oder mit versteckten Mängeln zu kaufen.",
            "quote": "In Franciacorta oder am Gardasee können zwei ähnliche Häuser sehr unterschiedliche Werte haben. Die Mikrozone entscheidet — nicht die Emotion des Moments.",
            "about_lead": "Ich begleite Käufer in Brescia Stadt, Franciacorta, an den Seen und in den Tälern. Mit OMI-Daten und technischer Prüfung helfe ich Ihnen, zum richtigen Preis zu kaufen — nicht zum Inseratspreis.",
            "wa_text": "Guten Tag Maurizio, ich suche eine Immobilie in Brescia und möchte eine Käuferberatung.",
            "zone_placeholder": "z. B. Franciacorta, Desenzano, Brescia Zentrum …",
            "msg_placeholder": "z. B. Dreizimmer in Franciacorta, Villa am See, Budget max. 350.000 € …",
            "footer_geo": "Brescia · Franciacorta · Gardasee · Iseosee",
            "market": [
                ("Stadt", "Brescia Zentrum", "Stabile Nachfrage, Preise ändern sich von Viertel zu Viertel."),
                ("Franciacorta", "Hügel und Dörfer", "Premium-Markt: Sie müssen wissen, ob der Preis zur Mikrozone passt."),
                ("Seen", "Garda und Iseo", "Hoher Wettbewerb, auch internationale Käufer — Analyse vor dem Angebot ist entscheidend."),
            ],
            "pain": [
                ("01", "Sie wissen nicht, ob der See-Preis fair ist", "Franciacorta und Garda sind Premium-Märkte: ein echter Vergleich ist nötig, nicht der geforderte Preis."),
                ("02", "Sie konkurrieren mit anderen Käufern", "Ein falsch kalkuliertes Angebot kostet Sie die Immobilie — oder bindet Sie an einen zu hohen Preis."),
                ("03", "Sie suchen in sehr unterschiedlichen Zonen", "Stadt, Hügel, Seen: jede Zone hat eigene Regeln und braucht einen seriösen Filter."),
                ("04", "Sie wollen technische Überraschungen vermeiden", "Vor dem Angebot müssen Sie wissen, ob es urbanistische oder katasterliche Risiken gibt."),
            ],
            "faq_work": "Arbeiten Sie nur in Brescia?",
            "faq_work_a": "Brescia, Franciacorta, Seen und Provinz sind der Schwerpunkt, aber ich begleite Käufer auch in Mailand und Bergamo.",
        },
        "fr": {
            "lead": "À Brescia et en province — du centre à la Franciacorta, du lac de Garde au lac d'Iseo — chaque zone a ses dynamiques. Il est facile de payer trop cher, de rater une opportunité ou d'acheter avec des problèmes cachés.",
            "quote": "En Franciacorta ou sur le lac de Garde, deux maisons similaires peuvent valoir des montants très différents. La micro-zone décide — pas l'émotion du moment.",
            "about_lead": "J'accompagne des acheteurs à Brescia ville, en Franciacorta, sur les lacs et dans les vallées. Avec les données OMI et des contrôles techniques, je vous aide à acheter au bon prix — pas au prix de l'annonce.",
            "wa_text": "Bonjour Maurizio, je cherche un bien à Brescia et souhaite un conseil acheteur.",
            "zone_placeholder": "ex. Franciacorta, Desenzano, centre Brescia …",
            "msg_placeholder": "ex. trois pièces en Franciacorta, villa au lac, budget max 350 000 € …",
            "footer_geo": "Brescia · Franciacorta · Lac de Garde · Lac d'Iseo",
            "market": [
                ("Ville", "Centre Brescia", "Demande stable, prix qui changent quartier par quartier."),
                ("Franciacorta", "Collines et villages", "Marché premium : il faut savoir si le prix correspond à la micro-zone."),
                ("Lacs", "Garde et Iseo", "Forte concurrence, y compris acheteurs internationaux — l'analyse avant l'offre est décisive."),
            ],
            "pain": [
                ("01", "Vous ne savez pas si le prix au lac est juste", "Franciacorta et le Garde sont des marchés premium : il faut une vraie comparaison, pas le prix demandé."),
                ("02", "Vous êtes en concurrence avec d'autres acheteurs", "Une offre mal calibrée vous fait perdre le bien — ou vous engage à un prix trop élevé."),
                ("03", "Vous cherchez dans des zones très différentes", "Ville, collines, lacs : chaque zone a ses règles et nécessite un filtre sérieux."),
                ("04", "Vous voulez éviter les surprises techniques", "Avant l'offre, vous devez connaître les risques urbanistiques ou cadastraux."),
            ],
            "faq_work": "Travaillez-vous uniquement à Brescia ?",
            "faq_work_a": "Brescia, Franciacorta, lacs et province sont au centre, mais j'accompagne aussi des acheteurs à Milan et Bergame.",
        },
    },
}


def get_block(slug: str, lang: str) -> dict | None:
    return _BLOCKS.get(slug, {}).get(lang)


def budget_labels(lang: str, *, milano_budget: bool = False) -> list[tuple[str, str]]:
    if lang == "de":
        if milano_budget:
            return [
                ("", "Möchte ich nicht angeben"),
                ("200000", "Bis 200.000 €"),
                ("200000-350000", "200.000 – 350.000 €"),
                ("350000-500000", "350.000 – 500.000 €"),
                ("500000-800000", "500.000 – 800.000 €"),
                ("800000+", "Über 800.000 €"),
            ]
        return [
            ("", "Möchte ich nicht angeben"),
            ("150000", "Bis 150.000 €"),
            ("150000-250000", "150.000 – 250.000 €"),
            ("250000-400000", "250.000 – 400.000 €"),
            ("400000-600000", "400.000 – 600.000 €"),
            ("600000+", "Über 600.000 €"),
        ]
    if lang == "fr":
        if milano_budget:
            return [
                ("", "Je préfère ne pas indiquer"),
                ("200000", "Jusqu'à 200 000 €"),
                ("200000-350000", "200 000 – 350 000 €"),
                ("350000-500000", "350 000 – 500 000 €"),
                ("500000-800000", "500 000 – 800 000 €"),
                ("800000+", "Plus de 800 000 €"),
            ]
        return [
            ("", "Je préfère ne pas indiquer"),
            ("150000", "Jusqu'à 150 000 €"),
            ("150000-250000", "150 000 – 250 000 €"),
            ("250000-400000", "250 000 – 400 000 €"),
            ("400000-600000", "400 000 – 600 000 €"),
            ("600000+", "Plus de 600 000 €"),
        ]
    return []


def get_new_block(slug: str, lang: str, meta: dict) -> dict:
    """Return province content block for NEW_PROVINCES pages."""
    if lang in ("it", "en"):
        return meta["it" if lang == "it" else "en"]
    en = dict(meta["en"])
    loc = NEW_I18N.get(slug, {}).get(lang)
    if loc:
        en.update(loc)
    if lang == "de":
        en["footer_geo"] = meta.get("footer_geo_en", meta["footer_geo_it"])
    elif lang == "fr":
        en["footer_geo"] = meta.get("footer_geo_en", meta["footer_geo_it"])
    return en


# Professional DE/FR for provinces beyond Milano / Bergamo / Brescia (in _BLOCKS).
NEW_I18N: dict[str, dict[str, dict]] = {
    "como": {
        "de": {
            "lead": "Am Comer See und in der Provinz Como — vom historischen Zentrum bis zur Brianza — hat jede Mikrozone eigene Preise und Zeiten. Es ist leicht, für den See-Charme mehr zu zahlen als der Immobilie wert ist.",
            "quote": "Am Comer See können zwei Villen wenige Minuten entfernt sehr unterschiedliche Werte haben. Die Mikrozone entscheidet — nicht die Postkartenansicht.",
            "about_lead": "Ich begleite Käufer in Como Stadt, am See und in der Brianza. Mit OMI-Daten und technischer Prüfung helfe ich Ihnen, vor dem Angebot zu verstehen, ob der Preis Sinn ergibt.",
            "wa_text": "Guten Tag Maurizio, ich suche eine Immobilie am Comer See und möchte eine Käuferberatung.",
            "zone_placeholder": "z. B. Como Zentrum, Cernobbio, Cantù …",
            "msg_placeholder": "z. B. Dreizimmer mit Seeblick, Budget max. 450.000 €, max. 2. OG …",
            "market": [
                ("Comer See", "Ufer und Dörfer", "Premium-Markt: lokale und internationale Nachfrage, Preise ändern sich von Gemeinde zu Gemeinde."),
                ("Como Stadt", "Zentrum und Viertel", "Solide Wohnnachfrage, starkes Interesse von Pendlern zwischen Como und Mailand."),
                ("Como Brianza", "Cantù und Umland", "Mehr Raum und Anbindung an Mailand: andere Preise als am See — aber seriöse Analyse bleibt wichtig."),
            ],
            "pain": [
                ("01", "Sie zahlen für die Aussicht, nicht für die Immobilie", "Am See lässt man sich leicht von Emotionen leiten und merkt später, dass der Preis nicht marktgerecht war."),
                ("02", "Sie konkurrieren mit externen Käufern", "Zweitwohnsitze und internationale Nachfrage: ein falsches Angebot kostet Sie die Immobilie oder zu viel Geld."),
                ("03", "Sie verwechseln See und Umland", "Como Stadt, See und Brianza haben verschiedene Dynamiken — Sie brauchen einen Zonenfilter, keinen Fotofilter."),
                ("04", "Sie befürchten planungsrechtliche Auflagen", "Uferlage und historisches Zentrum: urbanistische Prüfungen sind vor dem Angebot entscheidend."),
            ],
        },
        "fr": {
            "lead": "À Côme et sur le lac de Côme — du centre historique à la Brianza — chaque micro-zone a ses prix et ses délais. Il est facile de payer pour le charme du lac plus que la valeur réelle du bien.",
            "quote": "Sur le lac de Côme, deux villas à quelques minutes d'écart peuvent valoir des montants très différents. La micro-zone décide — pas la vue carte postale.",
            "about_lead": "J'accompagne des acheteurs à Côme ville, sur le lac et en Brianza. Avec les données OMI et des contrôles techniques, je vous aide à savoir si le prix a du sens avant l'offre.",
            "wa_text": "Bonjour Maurizio, je cherche un bien au lac de Côme et souhaite un conseil acheteur.",
            "zone_placeholder": "ex. centre Côme, Cernobbio, Cantù …",
            "msg_placeholder": "ex. trois pièces avec vue lac, budget max 450 000 €, max 2e étage …",
            "market": [
                ("Lac de Côme", "Rivage et villages", "Marché premium : demande locale et internationale, prix qui changent de commune en commune."),
                ("Côme ville", "Centre et quartiers", "Demande résidentielle solide, fort intérêt des actifs entre Côme et Milan."),
                ("Brianza comasque", "Cantù et couronne", "Plus d'espace et liaisons vers Milan : prix différents du lac, mais analyse sérieuse indispensable."),
            ],
            "pain": [
                ("01", "Vous payez pour la vue, pas pour le bien", "Au lac, l'émotion mène facilement à découvrir trop tard que le prix n'était pas aligné au marché."),
                ("02", "Vous êtes en concurrence avec des acheteurs extérieurs", "Résidences secondaires et demande internationale : une mauvaise offre vous fait perdre le bien ou payer trop."),
                ("03", "Vous confondez lac et couronne", "Côme ville, lac et Brianza ont des dynamiques différentes : il faut un filtre par zone, pas par photo."),
                ("04", "Vous craignez les contraintes urbanistiques", "Rivage et centre historique : les contrôles urbanistiques sont cruciaux avant l'offre."),
            ],
        },
    },
}

try:
    from buyer_provinces_new_i18n_data import NEW_I18N_EXTRA
    NEW_I18N.update(NEW_I18N_EXTRA)
except ImportError:
    pass
