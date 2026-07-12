"""Brescia-specific DE/FR phrase replacements for seller landing pages."""

from __future__ import annotations

_ENTITY_MAP = (
    ("À", "&Agrave;"),
    ("à", "&agrave;"),
    ("È", "&Egrave;"),
    ("è", "&egrave;"),
    ("É", "&Eacute;"),
    ("é", "&eacute;"),
    ("Ì", "&Igrave;"),
    ("ì", "&igrave;"),
    ("Ò", "&Ograve;"),
    ("ò", "&ograve;"),
    ("Ù", "&Ugrave;"),
    ("ù", "&ugrave;"),
    ("—", "&mdash;"),
    ("·", "&middot;"),
)


def _to_entities(text: str) -> str:
    out = text
    for char, ent in _ENTITY_MAP:
        out = out.replace(char, ent)
    return out


def _expand_and_sort(phrases: list[tuple[str, str]]) -> list[tuple[str, str]]:
    expanded: list[tuple[str, str]] = []
    seen: set[str] = set()
    for src, dst in phrases:
        for variant_src, variant_dst in (
            (src, dst),
            (_to_entities(src), _to_entities(dst)),
        ):
            if variant_src in seen:
                continue
            seen.add(variant_src)
            expanded.append((variant_src, variant_dst))
    return sorted(expanded, key=lambda pair: len(pair[0]), reverse=True)


_PHRASES_BRESCIA_DE_BASE: list[tuple[str, str]] = [
    (
        "Ogni zona ha dinamiche diverse — dal centro città alla Franciacorta, dal Lago di Garda al Lago d'Iseo. <strong>Un prezzo sbagliato può costarti mesi sul mercato</strong> o migliaia di euro nella trattativa. Prima della vendita, servono dati reali, metodo e posizionamento corretto.",
        "Jede Zone hat eigene Dynamiken — von der Innenstadt bis zur Franciacorta, vom Gardasee bis zum Iseosee. <strong>Ein falscher Preis kann Sie Monate auf dem Markt kosten</strong> oder in der Verhandlung Tausende Euro. Vor dem Verkauf brauchen Sie reale Daten, Methode und die richtige Positionierung.",
    ),
    (
        "Sono un Agente Immobiliare affiliato RE/MAX con background da geometra e imprenditore. Conosco le specificità di ogni zona del territorio bresciano — dalle dinamiche del centro città alle residenze di pregio in Franciacorta, fino agli immobili fronte lago sul Garda e sull'Iseo.",
        "Als RE/MAX-Immobilienberater mit Hintergrund als Vermessungsingenieur und Unternehmer kenne ich die Besonderheiten jeder Zone im Raum Brescia — von den Dynamiken der Innenstadt über hochwertige Residenzen in der Franciacorta bis zu Seeufer-Immobilien am Gardasee und am Iseosee.",
    ),
    (
        "Un appartamento in centro Brescia non segue le stesse dinamiche di una villa in Franciacorta o di un immobile fronte lago sul Garda o sull'Iseo. Per questo ogni analisi deve essere costruita sulla zona reale dell'immobile.",
        "Eine Wohnung im Zentrum von Brescia folgt nicht denselben Dynamiken wie eine Villa in der Franciacorta oder eine Uferimmobilie am Gardasee oder Iseosee. Deshalb muss jede Analyse auf der tatsächlichen Lage der Immobilie aufbauen.",
    ),
    (
        "Le stime automatiche non vedono stato interno, piano, affaccio, criticità documentali e domanda reale della zona. Sul Lago di Garda o in Franciacorta questo è ancora più rilevante, dove la componente internazionale incide significativamente.",
        "Automatische Schätzungen berücksichtigen weder Innenzustand, Etage, Ausrichtung, dokumentarische Risiken noch die reale Nachfrage der Zone. Am Gardasee oder in der Franciacorta ist das noch wichtiger, weil die internationale Komponente erheblich ins Gewicht fällt.",
    ),
    (
        "Sì. Opero su tutto il territorio bresciano — Brescia città, provincia, Franciacorta, Lago di Garda e Lago d'Iseo. Ogni zona ha dinamiche proprie e richiede un'analisi specifica.",
        "Ja. Ich arbeite im gesamten Raum Brescia — in Brescia Stadt, der Provinz, der Franciacorta, am Gardasee und am Iseosee. Jede Zone hat eigene Dynamiken und verlangt eine spezifische Analyse.",
    ),
    (
        "Avevo una villa in Franciacorta difficile da posizionare — né prima casa né immobile da investimento classico. L'analisi del mercato locale e l'identificazione del profilo acquirente giusto hanno fatto la differenza. Venduta al prezzo richiesto.",
        "Ich hatte eine Villa in der Franciacorta, die schwer zu positionieren war — weder klassische Erstwohnung noch typisches Investmentobjekt. Die Analyse des lokalen Marktes und die Identifikation des richtigen Käuferprofils haben den Unterschied gemacht. Zum gewünschten Preis verkauft.",
    ),
    (
        "Il mio appartamento sul Lago di Garda riceveva solo offerte da acquirenti non qualificati. Con un riposizionamento mirato e la selezione degli acquirenti giusti, abbiamo chiuso in due mesi con un risultato superiore alle aspettative.",
        "Meine Wohnung am Gardasee erhielt nur Angebote von nicht qualifizierten Käufern. Mit einer gezielten Neupositionierung und der Auswahl der richtigen Interessenten konnten wir in zwei Monaten mit einem Ergebnis über den Erwartungen abschließen.",
    ),
    (
        "Dovevo vendere l'appartamento di famiglia a Brescia senza avere tempo per gestire visite e trattative. Ha gestito tutto — documentazione, acquirenti, trattativa e rogito — con professionalità e precisione in ogni fase.",
        "Ich musste die Familienwohnung in Brescia verkaufen, ohne Zeit für Besichtigungen und Verhandlungen zu haben. Er hat alles übernommen — Unterlagen, Käufer, Verhandlung und Notartermin — mit Professionalität und Präzision in jeder Phase.",
    ),
    (
        "Prima di vendere casa a Brescia, in Franciacorta o sui laghi, serve capire davvero quanto vale.",
        "Bevor Sie in Brescia, in der Franciacorta oder an den Seen verkaufen, müssen Sie den realen Wert Ihrer Immobilie kennen.",
    ),
    (
        "La mia consulenza rimane personale e diretta. L'affiliazione RE/MAX aggiunge autorità, rete e maggiore visibilità — anche per acquirenti internazionali interessati ai laghi e alla Franciacorta.",
        "Meine Beratung bleibt persönlich und direkt. Die RE/MAX-Affiliation verleiht Autorität, Netzwerk und mehr Sichtbarkeit — auch für internationale Käufer, die sich für die Seen und die Franciacorta interessieren.",
    ),
    (
        "Agente Immobiliare affiliato RE/MAX · REA BS-639579 · P.IVA 14597560961 · Brescia · Franciacorta · Lago di Garda · Lago d'Iseo",
        "RE/MAX-Immobilienberater · REA BS-639579 · USt-IdNr. 14597560961 · Brescia · Franciacorta · Gardasee · Iseosee",
    ),
    (
        "Vendere casa a Brescia, in Franciacorta o sui laghi? Analisi immobiliare riservata su dati reali, prima di parlare di incarico.",
        "Haus verkaufen in Brescia, in der Franciacorta oder an den Seen? Vertrauliche Immobilienanalyse auf Basis realer Daten, bevor wir über ein Mandat sprechen.",
    ),
    (
        "agente immobiliare Brescia, agente RE/MAX Brescia, valutazione casa Brescia, vendere casa Brescia, agente immobiliare Franciacorta, agente immobiliare Lago di Garda, agente immobiliare Lago Iseo, valutazione immobile Brescia, Maurizio Piraino immobiliare",
        "Immobilienberater Brescia, RE/MAX-Immobilienberater Brescia, Immobilienbewertung Brescia, Haus verkaufen Brescia, Immobilienberater Franciacorta, Immobilienberater Gardasee, Immobilienberater Iseosee, Immobilienbewertung Brescia, Maurizio Piraino Immobilien",
    ),
    (
        "Vuoi vendere casa a Brescia, Franciacorta o sui laghi? Ricevi un'analisi immobiliare riservata basata su dati reali e strategia di vendita.",
        "Möchten Sie in Brescia, in der Franciacorta oder an den Seen verkaufen? Erhalten Sie eine vertrauliche Immobilienanalyse auf Basis realer Daten und einer klaren Verkaufsstrategie.",
    ),
    (
        "Analisi immobiliare riservata per vendere casa a Brescia, Franciacorta, Lago di Garda e Lago d'Iseo.",
        "Vertrauliche Immobilienanalyse für den Verkauf in Brescia, der Franciacorta, am Gardasee und am Iseosee.",
    ),
    (
        "Agente Immobiliare affiliato RE/MAX Brescia | Valutazione Casa",
        "RE/MAX-Immobilienberater Brescia | Immobilienbewertung",
    ),
    (
        "Agente Immobiliare Brescia | Valutazione Casa · Piraino",
        "Immobilienberater Brescia | Immobilienbewertung · Piraino",
    ),
    (
        "\"Ogni zona del bresciano ha il suo mercato. Vendere sul Lago di Garda è diverso dal vendere in città — e io conosco entrambe le dinamiche.\"",
        "\"Jede Zone im Raum Brescia hat ihren eigenen Markt. Am Gardasee zu verkaufen ist etwas anderes als in der Stadt zu verkaufen — und ich kenne beide Dynamiken.\"",
    ),
    (
        "Ogni vendita ha criticità diverse. Il primo passo è capire cosa può rallentare, svalutare o valorizzare il tuo immobile nel territorio bresciano.",
        "Jeder Verkauf hat andere Herausforderungen. Der erste Schritt besteht darin zu verstehen, was Ihre Immobilie im Raum Brescia verlangsamen, entwerten oder aufwerten kann.",
    ),
    (
        "Prima di decidere, vuoi leggere il mercato reale della tua zona — Brescia, Franciacorta o laghi — e non muoverti a sensazione.",
        "Bevor Sie entscheiden, möchten Sie den realen Markt Ihrer Zone — Brescia, Franciacorta oder die Seen — verstehen und nicht nach Gefühl handeln.",
    ),
    (
        "Prima di firmare qualsiasi cosa, vuoi una strategia chiara, riservata e costruita sulla realtà del mercato bresciano.",
        "Bevor Sie etwas unterschreiben, möchten Sie eine klare, vertrauliche Strategie, die auf der Realität des Marktes in Brescia aufbaut.",
    ),
    (
        "Dalla prima analisi alla possibile strategia di vendita: ogni fase è chiara, definita e concordata con te — ovunque si trovi il tuo immobile nel territorio bresciano.",
        "Von der ersten Analyse bis zur möglichen Verkaufsstrategie ist jede Phase klar, definiert und mit Ihnen abgestimmt — wo auch immer sich Ihre Immobilie im Raum Brescia befindet.",
    ),
    (
        "Opero su Brescia città e provincia e, tramite RE/MAX, posso coordinarmi anche con colleghi nelle altre province lombarde se il tuo immobile o il tuo obiettivo lo richiede.",
        "Ich arbeite in Brescia Stadt und Provinz und kann mich über RE/MAX auch mit Kollegen in anderen lombardischen Provinzen abstimmen, wenn Ihre Immobilie oder Ihr Ziel es erfordert.",
    ),
    (
        "Operi anche in provincia, sui laghi e in Franciacorta?",
        "Arbeiten Sie auch in der Provinz, an den Seen und in der Franciacorta?",
    ),
    (
        "Lavori solo su Brescia o anche in provincia?",
        "Arbeiten Sie nur in Brescia oder auch in der Provinz?",
    ),
    (
        "Valutazione su città, Franciacorta e laghi. Nessun obbligo di incarico.",
        "Bewertung für Stadt, Franciacorta und Seen. Keine Verpflichtung zum Mandat.",
    ),
    (
        "Comprare a Brescia con metodo: laghi, colline e città.",
        "In Brescia mit Methode kaufen: Seen, Hügelland und Stadt.",
    ),
    (
        "È un confronto strutturato sul tuo immobile, sulla micro-zona e sulla strategia di vendita più adatta a Brescia.",
        "Es ist ein strukturierter Vergleich Ihrer Immobilie, der Mikrozone und der für Brescia passendsten Verkaufsstrategie.",
    ),
    (
        "Brescia centro, la Franciacorta, il Garda bresciano e le valli hanno domanda, prezzi e tempi di vendita completamente diversi.",
        "Das Zentrum von Brescia, die Franciacorta, das brescianische Gardaseegebiet und die Täler haben völlig unterschiedliche Nachfrage-, Preis- und Verkaufszeiten.",
    ),
    (
        "Confronti zona per zona — Brescia, Franciacorta, Garda, Iseo — e posizionamento corretto del prezzo.",
        "Vergleiche Zone für Zone — Brescia, Franciacorta, Gardasee, Iseosee — und korrekte Preispositionierung.",
    ),
    (
        "Un marchio riconoscibile rassicura i proprietari e gli acquirenti — inclusi quelli stranieri interessati al Lago di Garda.",
        "Eine wiedererkennbare Marke schafft Vertrauen bei Eigentümern und Käufern — auch bei internationalen Interessenten am Gardasee.",
    ),
    (
        "Agente Immobiliare affiliato RE/MAX · Brescia e Provincia",
        "RE/MAX-Immobilienberater · Brescia und Provinz",
    ),
    (
        "Maurizio Piraino Agente Immobiliare affiliato RE/MAX Brescia",
        "Maurizio Piraino RE/MAX-Immobilienberater Brescia",
    ),
    (
        "Brescia · Franciacorta · Lago di Garda · Lago d'Iseo",
        "Brescia · Franciacorta · Gardasee · Iseosee",
    ),
    (
        "· Brescia · Franciacorta · Laghi",
        "· Brescia · Franciacorta · Seen",
    ),
    (
        "Lago di Garda bresciano",
        "Brescianischer Gardasee",
    ),
    (
        "Altra zona provincia Brescia",
        "Andere Zone in der Provinz Brescia",
    ),
    (
        "Bassa bresciana",
        "Brescianer Tiefebene",
    ),
    (
        "Brescia città",
        "Brescia Stadt",
    ),
    (
        "Brescia Città",
        "Brescia Stadt",
    ),
    (
        "Centro storico",
        "Altstadt",
    ),
    (
        "Valle Trompia",
        "Val Trompia",
    ),
    (
        "Valle Camonica",
        "Val Camonica",
    ),
    (
        "Comprare a Brescia →",
        "In Brescia kaufen →",
    ),
    (
        "Consulta i valori OMI ufficiali per zona a Brescia →",
        "Offizielle OMI-Werte nach Zone in Brescia →",
    ),
    (
        "Mercato Bresciano",
        "Markt Brescia",
    ),
    (
        "Proprietà Franciacorta",
        "Immobilie in der Franciacorta",
    ),
    (
        "Franciacorta · Provincia di Brescia",
        "Franciacorta · Provinz Brescia",
    ),
    (
        "Appartamento Lago di Garda",
        "Wohnung am Gardasee",
    ),
    (
        "Desenzano · Lago di Garda",
        "Desenzano · Gardasee",
    ),
    (
        "Appartamento Brescia",
        "Wohnung in Brescia",
    ),
    (
        "Brescia Centro",
        "Zentrum Brescia",
    ),
    (
        "Laghi Garda · Iseo",
        "Gardasee · Iseosee",
    ),
    (
        "Lago di Garda",
        "Gardasee",
    ),
    (
        "Lago d'Iseo",
        "Iseosee",
    ),
    (
        "Provincia di Brescia",
        "Provinz Brescia",
    ),
    (
        "Provincia BS",
        "Provinz BS",
    ),
]


_PHRASES_BRESCIA_FR_BASE: list[tuple[str, str]] = [
    (
        "Ogni zona ha dinamiche diverse — dal centro città alla Franciacorta, dal Lago di Garda al Lago d'Iseo. <strong>Un prezzo sbagliato può costarti mesi sul mercato</strong> o migliaia di euro nella trattativa. Prima della vendita, servono dati reali, metodo e posizionamento corretto.",
        "Chaque zone a ses propres dynamiques — du centre-ville à la Franciacorta, du lac de Garde au lac d'Iseo. <strong>Un mauvais prix peut vous coûter des mois sur le marché</strong> ou des milliers d'euros en négociation. Avant de vendre, il faut des données réelles, une méthode et le bon positionnement.",
    ),
    (
        "Sono un Agente Immobiliare affiliato RE/MAX con background da geometra e imprenditore. Conosco le specificità di ogni zona del territorio bresciano — dalle dinamiche del centro città alle residenze di pregio in Franciacorta, fino agli immobili fronte lago sul Garda e sull'Iseo.",
        "Agent immobilier RE/MAX avec un parcours de géomètre et d'entrepreneur, je connais les spécificités de chaque zone du territoire de Brescia — des dynamiques du centre-ville aux résidences de prestige en Franciacorta, jusqu'aux biens en bord de lac sur le lac de Garde et le lac d'Iseo.",
    ),
    (
        "Un appartamento in centro Brescia non segue le stesse dinamiche di una villa in Franciacorta o di un immobile fronte lago sul Garda o sull'Iseo. Per questo ogni analisi deve essere costruita sulla zona reale dell'immobile.",
        "Un appartement dans le centre de Brescia ne suit pas les mêmes dynamiques qu'une villa en Franciacorta ou qu'un bien en bord de lac sur le lac de Garde ou le lac d'Iseo. Chaque analyse doit donc être construite sur la zone réelle du bien.",
    ),
    (
        "Le stime automatiche non vedono stato interno, piano, affaccio, criticità documentali e domanda reale della zona. Sul Lago di Garda o in Franciacorta questo è ancora più rilevante, dove la componente internazionale incide significativamente.",
        "Les estimations automatiques ne voient ni l'état intérieur, ni l'étage, ni l'exposition, ni les risques documentaires, ni la demande réelle de la zone. Sur le lac de Garde ou en Franciacorta, c'est encore plus déterminant, où la composante internationale pèse fortement.",
    ),
    (
        "Sì. Opero su tutto il territorio bresciano — Brescia città, provincia, Franciacorta, Lago di Garda e Lago d'Iseo. Ogni zona ha dinamiche proprie e richiede un'analisi specifica.",
        "Oui. J'interviens sur tout le territoire de Brescia — Brescia ville, province, Franciacorta, lac de Garde et lac d'Iseo. Chaque zone a ses propres dynamiques et exige une analyse spécifique.",
    ),
    (
        "Avevo una villa in Franciacorta difficile da posizionare — né prima casa né immobile da investimento classico. L'analisi del mercato locale e l'identificazione del profilo acquirente giusto hanno fatto la differenza. Venduta al prezzo richiesto.",
        "J'avais une villa en Franciacorta difficile à positionner — ni résidence principale, ni bien d'investissement classique. L'analyse du marché local et l'identification du bon profil d'acheteur ont fait la différence. Vendue au prix demandé.",
    ),
    (
        "Il mio appartamento sul Lago di Garda riceveva solo offerte da acquirenti non qualificati. Con un riposizionamento mirato e la selezione degli acquirenti giusti, abbiamo chiuso in due mesi con un risultato superiore alle aspettative.",
        "Mon appartement sur le lac de Garde ne recevait que des offres d'acquéreurs non qualifiés. Avec un repositionnement ciblé et une sélection plus précise des bons acheteurs, nous avons conclu en deux mois avec un résultat supérieur aux attentes.",
    ),
    (
        "Dovevo vendere l'appartamento di famiglia a Brescia senza avere tempo per gestire visite e trattative. Ha gestito tutto — documentazione, acquirenti, trattativa e rogito — con professionalità e precisione in ogni fase.",
        "Je devais vendre l'appartement familial à Brescia sans avoir le temps de gérer visites et négociations. Il a tout pris en charge — documentation, acheteurs, négociation et acte — avec professionnalisme et précision à chaque étape.",
    ),
    (
        "Prima di vendere casa a Brescia, in Franciacorta o sui laghi, serve capire davvero quanto vale.",
        "Avant de vendre à Brescia, en Franciacorta ou sur les lacs, il faut connaître la vraie valeur de votre bien.",
    ),
    (
        "La mia consulenza rimane personale e diretta. L'affiliazione RE/MAX aggiunge autorità, rete e maggiore visibilità — anche per acquirenti internazionali interessati ai laghi e alla Franciacorta.",
        "Mon accompagnement reste personnel et direct. L'affiliation RE/MAX apporte autorité, réseau et visibilité accrue — y compris auprès d'acheteurs internationaux intéressés par les lacs et la Franciacorta.",
    ),
    (
        "Agente Immobiliare affiliato RE/MAX · REA BS-639579 · P.IVA 14597560961 · Brescia · Franciacorta · Lago di Garda · Lago d'Iseo",
        "Agent immobilier RE/MAX · REA BS-639579 · P.IVA 14597560961 · Brescia · Franciacorta · lac de Garde · lac d'Iseo",
    ),
    (
        "Vendere casa a Brescia, in Franciacorta o sui laghi? Analisi immobiliare riservata su dati reali, prima di parlare di incarico.",
        "Vendre à Brescia, en Franciacorta ou sur les lacs ? Analyse immobilière confidentielle fondée sur des données réelles, avant de parler de mandat.",
    ),
    (
        "agente immobiliare Brescia, agente RE/MAX Brescia, valutazione casa Brescia, vendere casa Brescia, agente immobiliare Franciacorta, agente immobiliare Lago di Garda, agente immobiliare Lago Iseo, valutazione immobile Brescia, Maurizio Piraino immobiliare",
        "agent immobilier Brescia, agent RE/MAX Brescia, estimation immobilière Brescia, vendre maison Brescia, agent immobilier Franciacorta, agent immobilier lac de Garde, agent immobilier lac d'Iseo, estimation bien Brescia, Maurizio Piraino immobilier",
    ),
    (
        "Vuoi vendere casa a Brescia, Franciacorta o sui laghi? Ricevi un'analisi immobiliare riservata basata su dati reali e strategia di vendita.",
        "Vous souhaitez vendre à Brescia, en Franciacorta ou sur les lacs ? Recevez une analyse immobilière confidentielle basée sur des données réelles et une vraie stratégie de vente.",
    ),
    (
        "Analisi immobiliare riservata per vendere casa a Brescia, Franciacorta, Lago di Garda e Lago d'Iseo.",
        "Analyse immobilière confidentielle pour vendre à Brescia, en Franciacorta, sur le lac de Garde et le lac d'Iseo.",
    ),
    (
        "Agente Immobiliare affiliato RE/MAX Brescia | Valutazione Casa",
        "Agent immobilier RE/MAX Brescia | Estimation immobilière",
    ),
    (
        "Agente Immobiliare Brescia | Valutazione Casa · Piraino",
        "Agent immobilier Brescia | Estimation immobilière · Piraino",
    ),
    (
        "\"Ogni zona del bresciano ha il suo mercato. Vendere sul Lago di Garda è diverso dal vendere in città — e io conosco entrambe le dinamiche.\"",
        "\"Chaque zone autour de Brescia a son propre marché. Vendre sur le lac de Garde est différent de vendre en ville — et je maîtrise parfaitement ces deux dynamiques.\"",
    ),
    (
        "Ogni vendita ha criticità diverse. Il primo passo è capire cosa può rallentare, svalutare o valorizzare il tuo immobile nel territorio bresciano.",
        "Chaque vente présente des enjeux différents. La première étape consiste à comprendre ce qui peut ralentir, dévaloriser ou valoriser votre bien sur le territoire de Brescia.",
    ),
    (
        "Prima di decidere, vuoi leggere il mercato reale della tua zona — Brescia, Franciacorta o laghi — e non muoverti a sensazione.",
        "Avant de décider, vous voulez lire le marché réel de votre zone — Brescia, Franciacorta ou les lacs — et ne pas avancer à l'intuition.",
    ),
    (
        "Prima di firmare qualsiasi cosa, vuoi una strategia chiara, riservata e costruita sulla realtà del mercato bresciano.",
        "Avant de signer quoi que ce soit, vous voulez une stratégie claire, confidentielle et construite sur la réalité du marché de Brescia.",
    ),
    (
        "Dalla prima analisi alla possibile strategia di vendita: ogni fase è chiara, definita e concordata con te — ovunque si trovi il tuo immobile nel territorio bresciano.",
        "De la première analyse à la stratégie de vente éventuelle, chaque phase est claire, définie et convenue avec vous — où que se trouve votre bien sur le territoire de Brescia.",
    ),
    (
        "Opero su Brescia città e provincia e, tramite RE/MAX, posso coordinarmi anche con colleghi nelle altre province lombarde se il tuo immobile o il tuo obiettivo lo richiede.",
        "J'interviens à Brescia ville et en province et, via RE/MAX, je peux aussi me coordonner avec des collègues des autres provinces lombardes si votre bien ou votre objectif l'exige.",
    ),
    (
        "Operi anche in provincia, sui laghi e in Franciacorta?",
        "Intervenez-vous aussi en province, sur les lacs et en Franciacorta ?",
    ),
    (
        "Lavori solo su Brescia o anche in provincia?",
        "Travaillez-vous seulement sur Brescia ou aussi en province ?",
    ),
    (
        "Valutazione su città, Franciacorta e laghi. Nessun obbligo di incarico.",
        "Évaluation sur la ville, la Franciacorta et les lacs. Aucune obligation de mandat.",
    ),
    (
        "Comprare a Brescia con metodo: laghi, colline e città.",
        "Acheter à Brescia avec méthode : lacs, collines et ville.",
    ),
    (
        "È un confronto strutturato sul tuo immobile, sulla micro-zona e sulla strategia di vendita più adatta a Brescia.",
        "C'est une comparaison structurée de votre bien, de la micro-zone et de la stratégie de vente la plus adaptée à Brescia.",
    ),
    (
        "Brescia centro, la Franciacorta, il Garda bresciano e le valli hanno domanda, prezzi e tempi di vendita completamente diversi.",
        "Le centre de Brescia, la Franciacorta, la rive bresciane du lac de Garde et les vallées ont des demandes, des niveaux de prix et des délais de vente complètement différents.",
    ),
    (
        "Confronti zona per zona — Brescia, Franciacorta, Garda, Iseo — e posizionamento corretto del prezzo.",
        "Comparaisons zone par zone — Brescia, Franciacorta, lac de Garde, lac d'Iseo — et juste positionnement du prix.",
    ),
    (
        "Un marchio riconoscibile rassicura i proprietari e gli acquirenti — inclusi quelli stranieri interessati al Lago di Garda.",
        "Une marque reconnaissable rassure propriétaires et acheteurs — y compris les acquéreurs étrangers intéressés par le lac de Garde.",
    ),
    (
        "Agente Immobiliare affiliato RE/MAX · Brescia e Provincia",
        "Agent immobilier RE/MAX · Brescia et province",
    ),
    (
        "Maurizio Piraino Agente Immobiliare affiliato RE/MAX Brescia",
        "Maurizio Piraino agent immobilier RE/MAX Brescia",
    ),
    (
        "Brescia · Franciacorta · Lago di Garda · Lago d'Iseo",
        "Brescia · Franciacorta · lac de Garde · lac d'Iseo",
    ),
    (
        "· Brescia · Franciacorta · Laghi",
        "· Brescia · Franciacorta · Lacs",
    ),
    (
        "Lago di Garda bresciano",
        "lac de Garde côté Brescia",
    ),
    (
        "Altra zona provincia Brescia",
        "Autre secteur de la province de Brescia",
    ),
    (
        "Bassa bresciana",
        "plaine bresciane",
    ),
    (
        "Brescia città",
        "Brescia ville",
    ),
    (
        "Brescia Città",
        "Brescia ville",
    ),
    (
        "Centro storico",
        "Centre historique",
    ),
    (
        "Valle Trompia",
        "Val Trompia",
    ),
    (
        "Valle Camonica",
        "Val Camonica",
    ),
    (
        "Comprare a Brescia →",
        "Acheter à Brescia →",
    ),
    (
        "Consulta i valori OMI ufficiali per zona a Brescia →",
        "Consultez les valeurs OMI officielles par zone à Brescia →",
    ),
    (
        "Mercato Bresciano",
        "Marché de Brescia",
    ),
    (
        "Proprietà Franciacorta",
        "Propriété en Franciacorta",
    ),
    (
        "Franciacorta · Provincia di Brescia",
        "Franciacorta · province de Brescia",
    ),
    (
        "Appartamento Lago di Garda",
        "Appartement sur le lac de Garde",
    ),
    (
        "Desenzano · Lago di Garda",
        "Desenzano · lac de Garde",
    ),
    (
        "Appartamento Brescia",
        "Appartement à Brescia",
    ),
    (
        "Brescia Centro",
        "Centre de Brescia",
    ),
    (
        "Laghi Garda · Iseo",
        "lac de Garde · lac d'Iseo",
    ),
    (
        "Lago di Garda",
        "lac de Garde",
    ),
    (
        "Lago d'Iseo",
        "lac d'Iseo",
    ),
    (
        "Provincia di Brescia",
        "province de Brescia",
    ),
    (
        "Provincia BS",
        "Province BS",
    ),
]


PHRASES_BRESCIA_DE: list[tuple[str, str]] = _expand_and_sort(_PHRASES_BRESCIA_DE_BASE)
PHRASES_BRESCIA_FR: list[tuple[str, str]] = _expand_and_sort(_PHRASES_BRESCIA_FR_BASE)
