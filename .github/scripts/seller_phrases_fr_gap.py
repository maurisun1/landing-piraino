"""French translations for missing seller landing page phrases."""

from __future__ import annotations

_ENTITY_MAP = (
    ("à", "&agrave;"),
    ("è", "&egrave;"),
    ("é", "&eacute;"),
    ("ì", "&igrave;"),
    ("ò", "&ograve;"),
    ("ù", "&ugrave;"),
    ("À", "&Agrave;"),
    ("È", "&Egrave;"),
    ("É", "&Eacute;"),
    ("Ì", "&Igrave;"),
    ("Ò", "&Ograve;"),
    ("Ù", "&Ugrave;"),
    ("â", "&acirc;"),
    ("ê", "&ecirc;"),
    ("î", "&icirc;"),
    ("ô", "&ocirc;"),
    ("û", "&ucirc;"),
    ("Â", "&Acirc;"),
    ("Ê", "&Ecirc;"),
    ("Î", "&Icirc;"),
    ("Ô", "&Ocirc;"),
    ("Û", "&Ucirc;"),
    ("ç", "&ccedil;"),
    ("Ç", "&Ccedil;"),
    ("ë", "&euml;"),
    ("ï", "&iuml;"),
    ("ü", "&uuml;"),
    ("Ë", "&Euml;"),
    ("Ï", "&Iuml;"),
    ("Ü", "&Uuml;"),
    ("’", "&rsquo;"),
    ("«", "&laquo;"),
    ("»", "&raquo;"),
    ("—", "&mdash;"),
    ("·", "&middot;"),
)


def _to_entities(text: str) -> str:
    out = text
    for char, entity in _ENTITY_MAP:
        out = out.replace(char, entity)
    return out


def _expand_entity_variants(
    phrases: list[tuple[str, str]],
) -> list[tuple[str, str]]:
    expanded: list[tuple[str, str]] = []
    seen: set[str] = set()
    for src, dst in phrases:
        for variant_src, variant_dst in (
            (src, dst),
            (_to_entities(src), _to_entities(dst)),
        ):
            if variant_src not in seen:
                seen.add(variant_src)
                expanded.append((variant_src, variant_dst))
    return expanded


_BASE_PHRASES_FR_GAP: list[tuple[str, str]] = [
    (
        "Sono un Agente Immobiliare affiliato RE/MAX con background tecnico e imprenditoriale. Questo significa leggere un immobile in modo diverso: individuare criticità, valorizzare i punti forti e costruire una strategia reale prima ancora della pubblicazione online.",
        "Je suis agent immobilier affilié RE/MAX, avec un parcours technique et entrepreneurial. Cela signifie analyser un bien autrement : identifier les points sensibles, valoriser ses atouts et construire une stratégie réelle avant même sa mise en ligne.",
    ),
    (
        "Le valutazioni online sono utili come punto di partenza, ma non sostituiscono una lettura tecnica e di mercato del singolo immobile.",
        "Les estimations en ligne sont utiles comme point de départ, mais elles ne remplacent pas une lecture technique et de marché de chaque bien.",
    ),
    (
        "Porte aperte organizzate per attrarre più acquirenti qualificati in poche ore, con gestione professionale delle visite.",
        "Portes ouvertes organisées pour attirer davantage d'acheteurs qualifiés en quelques heures, avec une gestion professionnelle des visites.",
    ),
    (
        "Ogni vendita ha criticità diverse. Il primo passo è capire cosa può rallentare, svalutare o valorizzare il tuo immobile.",
        "Chaque vente présente des enjeux différents. La première étape consiste à comprendre ce qui peut ralentir, dévaloriser ou valoriser votre bien.",
    ),
    (
        "La maggior parte degli immobili perde forza nelle prime settimane online non per colpa della casa, ma per una strategia sbagliata. Il mio lavoro è evitare che questo accada.",
        "La plupart des biens perdent de leur élan dès les premières semaines en ligne, non pas à cause du bien lui-même, mais d'une mauvaise stratégie. Mon travail consiste à éviter cela.",
    ),
    (
        "No. L'analisi iniziale non crea obbligo di conferimento incarico. Serve a darti informazioni chiare per decidere meglio.",
        "Non. L'analyse initiale ne crée aucune obligation de mandat. Elle sert à vous donner des informations claires pour mieux décider.",
    ),
    (
        "Opero su Milano e provincia e, tramite RE/MAX, posso coordinarmi anche con colleghi nelle altre province lombarde se il tuo immobile o il tuo obiettivo lo richiede.",
        "J'interviens à Milan et en province et, via RE/MAX, je peux aussi me coordonner avec des collègues dans les autres provinces lombardes si votre bien ou votre objectif l'exige.",
    ),
    (
        "Ti mostro il mercato reale della tua zona, le criticità dell'immobile e la strategia più adatta prima ancora di parlare di incarico.",
        "Je vous montre le marché réel de votre secteur, les points de vigilance du bien et la stratégie la plus adaptée avant même de parler de mandat.",
    ),
    (
        "Ti mostro il mercato reale della tua zona, le criticità dell’immobile e la strategia più adatta prima ancora di parlare di incarico.",
        "Je vous montre le marché réel de votre secteur, les points de vigilance du bien et la stratégie la plus adaptée avant même de parler de mandat.",
    ),
    (
        "È un confronto strutturato sul tuo immobile, sulla micro-zona e sulla strategia di vendita più adatta a Milano.",
        "C'est une analyse structurée de votre bien, de la micro-zone et de la stratégie de vente la plus adaptée à Milan.",
    ),
    (
        "Confronto con immobili comparabili venduti e in vendita nella tua zona, non medie generiche.",
        "Comparaison avec des biens comparables vendus et en vente dans votre secteur, pas avec des moyennes génériques.",
    ),
    (
        "Riferimenti Agenzia delle Entrate integrati con il contesto reale del quartiere o del comune.",
        "Références de l'Agenzia delle Entrate intégrées au contexte réel du quartier ou de la commune.",
    ),
    (
        "Piano, conformità, stato, spazi esterni: ciò che un acquirente farà emergere in trattativa.",
        "Étage, conformité, état, espaces extérieurs : tout ce qu'un acheteur fera ressortir en négociation.",
    ),
    (
        "Quanto potrebbe restare online un immobile posizionato correttamente — o no — nel mercato attuale.",
        "Le temps qu'un bien peut rester en ligne sur le marché actuel selon qu'il soit bien positionné — ou non.",
    ),
    (
        "Visibilità, rete MLS e canali se decidi di procedere — sempre senza obbligo dopo l'analisi.",
        "Visibilité, réseau MLS et canaux de diffusion si vous décidez d'avancer — toujours sans obligation après l'analyse.",
    ),
    (
        "Un appartamento a Porta Romana non segue le stesse dinamiche di Lambrate, Isola o Navigli.",
        "Un appartement à Porta Romana ne suit pas les mêmes dynamiques qu'à Lambrate, Isola ou Navigli.",
    ),
    (
        "Dalla prima analisi alla firma dal notaio: un percorso chiaro, senza improvvisazione.",
        "De la première analyse à la signature chez le notaire : un parcours clair, sans improvisation.",
    ),
    (
        "Studio del mercato locale, comparables, OMI e posizionamento prezzo iniziale.",
        "Étude du marché local, des biens comparables, des données OMI et du positionnement du prix de départ.",
    ),
    (
        "Home staging consigliato, documenti in ordine, presentazione che valorizza i punti di forza.",
        "Home staging conseillé, documents en ordre, présentation qui met en valeur les points forts.",
    ),
    (
        "Foto professionali, portali, rete MLS e visibilità internazionale del brand.",
        "Photos professionnelles, portails, réseau MLS et visibilité internationale de la marque.",
    ),
    (
        "Prima di decidere, vuoi leggere il mercato reale della tua zona e non muoverti a sensazione.",
        "Avant de décider, vous voulez lire le marché réel de votre secteur et ne pas agir à l'intuition.",
    ),
    (
        "Vuoi capire su quali dati si basa il prezzo e distinguere una stima seria da una promessa.",
        "Vous voulez comprendre sur quelles données repose le prix et distinguer une estimation sérieuse d'une simple promesse.",
    ),
    (
        "La mia consulenza rimane personale e diretta. L'affiliazione RE/MAX aggiunge autorevolezza, rete, collaborazione e maggiore visibilità commerciale all'immobile.",
        "Mon conseil reste personnel et direct. L'affiliation RE/MAX apporte crédibilité, réseau, coopération et une visibilité commerciale accrue au bien.",
    ),
    (
        "La mia consulenza rimane personale e diretta. L’affiliazione RE/MAX aggiunge autorevolezza, rete, collaborazione e maggiore visibilità commerciale all’immobile.",
        "Mon conseil reste personnel et direct. L'affiliation RE/MAX apporte crédibilité, réseau, coopération et une visibilité commerciale accrue au bien.",
    ),
    (
        "Il valore non si calcola solo al metro quadro: contano piano, stato, affaccio, contesto e domanda reale.",
        "La valeur ne se calcule pas seulement au mètre carré : l'étage, l'état, l'exposition, l'environnement et la demande réelle comptent aussi.",
    ),
    (
        "Prima dell'annuncio va capito chi è l'acquirente più probabile e cosa lo convince a fare un'offerta.",
        "Avant la mise en vente, il faut comprendre qui est l'acheteur le plus probable et ce qui le convaincra de faire une offre.",
    ),
    (
        "Il momento di lancio, il prezzo iniziale e la comunicazione incidono sulla forza della trattativa.",
        "Le moment du lancement, le prix initial et la communication influencent directement la force de la négociation.",
    ),
    (
        "Dalla prima analisi alla possibile strategia di vendita: ogni fase è chiara, definita e concordata con te.",
        "De la première analyse à l'éventuelle stratégie de vente : chaque étape est claire, définie et validée avec vous.",
    ),
    (
        "Leggo l'immobile, la zona e ti mostro dati, criticità e potenzialità prima di parlare di incarico.",
        "J'analyse le bien et son secteur, puis je vous présente les données, les points de vigilance et le potentiel avant de parler de mandat.",
    ),
    (
        "Leggo l’immobile, la zona e ti mostro dati, criticità e potenzialità prima di parlare di incarico.",
        "J'analyse le bien et son secteur, puis je vous présente les données, les points de vigilance et le potentiel avant de parler de mandat.",
    ),
    (
        "Le stime automatiche non vedono stato interno, piano, affaccio, criticità documentali, domanda reale e concorrenza nella micro-zona.",
        "Les estimations automatiques ne prennent pas en compte l'état intérieur, l'étage, l'exposition, les points de vigilance documentaires, la demande réelle et la concurrence dans la micro-zone.",
    ),
    (
        "Per trasparenza e fiducia. La consulenza resta personale, ma l'affiliazione al network RE/MAX aggiunge riconoscibilità e supporto commerciale.",
        "Par transparence et pour instaurer la confiance. Le conseil reste personnel, mais l'affiliation au réseau RE/MAX apporte notoriété et soutien commercial.",
    ),
    (
        "Di solito entro 24–48 ore lavorative dal modulo. Se serve approfondire documenti o visite, te lo comunico subito con tempi chiari.",
        "En général, sous 24 à 48 heures ouvrées après l'envoi du formulaire. S'il faut approfondir des documents ou organiser une visite, je vous l'indique immédiatement avec des délais clairs.",
    ),
    (
        "Nessun problema. L'analisi resta un asset per te: saprai il valore reale, i tempi di mercato e cosa conviene fare quando deciderai di muoverti.",
        "Aucun problème. L'analyse reste un atout pour vous : vous connaîtrez la valeur réelle, les délais du marché et la meilleure décision à prendre lorsque vous choisirez d'agir.",
    ),
    (
        "Due informazioni sull'immobile, per preparare un'analisi più precisa.",
        "Deux informations sur le bien pour préparer une analyse plus précise.",
    ),
    (
        "Due informazioni sull’immobile, per preparare un’analisi più precisa.",
        "Deux informations sur le bien pour préparer une analyse plus précise.",
    ),
    (
        "Inviando il form acconsenti al trattamento dei dati per essere ricontattato.",
        "En envoyant le formulaire, vous acceptez le traitement de vos données afin d'être recontacté.",
    ),
    (
        "Prima di vendere in provincia di Varese, serve capire davvero quanto vale.",
        "Avant de vendre dans la province de Varèse, il faut connaître la vraie valeur de votre bien.",
    ),
    (
        "Supporto in Verhandlung fino al Notartermin",
        "Accompagnement en négociation jusqu'à l'acte notarié",
    ),
    (
        "Range consigliato, leva trattativa e timing di uscita sul mercato.",
        "Fourchette conseillée, marge de négociation et bon timing de mise sur le marché.",
    ),
    (
        "Gestione offerte, negoziazione e affiancamento fino al passaggio definitivo.",
        "Gestion des offres, négociation et accompagnement jusqu'à la signature définitive.",
    ),
    (
        "Analisi riservata basata su dati reali. Nessun obbligo di incarico, risposta entro 24 ore.",
        "Analyse confidentielle fondée sur des données réelles. Aucune obligation de mandat, réponse sous 24 heures.",
    ),
    (
        "Mesi online, poche visite, offerte basse: spesso il problema non è la casa, ma il posizionamento.",
        "Des mois en ligne, peu de visites, des offres basses : souvent, le problème n'est pas le bien, mais son positionnement.",
    ),
    (
        "“Quando entro in una casa, osservo già quello che un acquirente farà notare durante la trattativa.”",
        "« Quand j'entre dans un bien, j'observe déjà ce qu'un acheteur soulèvera pendant la négociation. »",
    ),
    (
        "Definiamo prezzo, timing, comunicazione e profilo dell'acquirente più adatto.",
        "Nous définissons le prix, le timing, la communication et le profil d'acheteur le plus adapté.",
    ),
    (
        "Se decidi di procedere, ti accompagno in visite, offerte, trattativa e passaggi tecnici.",
        "Si vous décidez d'aller plus loin, je vous accompagne pour les visites, les offres, la négociation et les étapes techniques.",
    ),
    (
        "Se richiedo l'analisi, sono obbligato a darti l'incarico?",
        "Si je demande l'analyse, suis-je obligé de vous confier le mandat ?",
    ),
    (
        "Se richiedo l’analisi, sono obbligato a darti l’incarico?",
        "Si je demande l'analyse, suis-je obligé de vous confier le mandat ?",
    ),
    (
        "Sì. Sapere oggi quanto vale il tuo immobile ti permette di pianificare senza pressione e scegliere il momento migliore.",
        "Oui. Connaître aujourd'hui la valeur de votre bien vous permet de planifier sans pression et de choisir le meilleur moment.",
    ),
    (
        "Dati riservati · Nessun obbligo di incarico · Risposta personale",
        "Données confidentielles · Aucune obligation de mandat · Réponse personnelle",
    ),
    (
        "OMI-Analyse per zona e tipologia",
        "Analyse OMI par zone et typologie",
    ),
    ("Dati OMI ufficiali", "Données OMI officielles"),
    ("Criticità tecniche", "Points de vigilance techniques"),
    ("Tempi di vendita stimati", "Délais de vente estimés"),
    ("Strategia di prezzo", "Stratégie de prix"),
    ("Piano RE/MAX", "Plan RE/MAX"),
    ("Micro-zona e quartiere", "Micro-zone et quartier"),
    ("Media generica", "Moyenne générique"),
    ("Analisi specifica", "Analyse spécifique"),
    ("Stato, piano, affaccio", "État, étage, exposition"),
    ("Non considerati", "Non pris en compte"),
    ("Valutati uno per uno", "Évalués un par un"),
    ("Documenti e conformità", "Documents et conformité"),
    ("Assenti", "Absents"),
    ("Verifica tecnica", "Vérification technique"),
    ("Strategia di vendita", "Stratégie de vente"),
    ("Solo un numero", "Un simple chiffre"),
    ("Piano completo", "Plan complet"),
    ("Obbligo di incarico", "Obligation de mandat"),
    ("Mai, alla prima analisi", "Jamais lors de la première analyse"),
    ("Zone servite · Milano", "Zones couvertes · Milan"),
    ("Milano cambia quartiere per quartiere.", "Milan change d'un quartier à l'autre."),
    (
        "Consulta i valori OMI ufficiali per zona a Milano →",
        "Consultez les valeurs OMI officielles par zone à Milan →",
    ),
    (
        "Consulta i valori OMI per zona a Milano →",
        "Consultez les valeurs OMI par zone à Milan →",
    ),
    ("Analisi e valutazione", "Analyse et évaluation"),
    ("Preparazione immobile", "Préparation du bien"),
    ("Marketing RE/MAX", "Marketing RE/MAX"),
    ("Open House", "Portes ouvertes"),
    ("Vuoi capire se è il momento giusto", "Vous voulez savoir si c'est le bon moment"),
    ("Il tuo immobile è fermo sul mercato", "Votre bien stagne sur le marché"),
    ("Hai ricevuto valutazioni troppo diverse", "Vous avez reçu des estimations trop divergentes"),
    ("Vuoi decidere con dati, non promesse", "Vous voulez décider à partir de données, pas de promesses"),
    (
        "Prima di firmare qualsiasi cosa, vuoi una strategia chiara, riservata e motivata.",
        "Avant de signer quoi que ce soit, vous voulez une stratégie claire, confidentielle et solidement argumentée.",
    ),
    ("Analisi reale", "Analyse réelle"),
    (
        "Confronti concreti, andamento della zona e posizionamento corretto del prezzo.",
        "Comparaisons concrètes, dynamique du secteur et bon positionnement du prix.",
    ),
    ("Strategia personalizzata", "Stratégie personnalisée"),
    (
        "Ogni immobile richiede comunicazione, timing e target differenti.",
        "Chaque bien exige une communication, un timing et une cible différents.",
    ),
    ("Trattativa guidata", "Négociation accompagnée"),
    (
        "Dalla prima visita alla firma dal notaio, senza improvvisazione.",
        "De la première visite à la signature chez le notaire, sans improvisation.",
    ),
    (
        "Un marchio riconoscibile aiuta il proprietario e rassicura molti acquirenti nella fase iniziale.",
        "Une marque reconnue aide le propriétaire et rassure de nombreux acheteurs dès la phase initiale.",
    ),
    (
        "La collaborazione tra professionisti può aumentare le possibilità di intercettare acquirenti qualificati.",
        "La collaboration entre professionnels peut accroître les chances d'attirer des acheteurs qualifiés.",
    ),
    (
        "La differenza resta nel modo in cui l'immobile viene analizzato, posizionato e presentato.",
        "La différence tient à la manière dont le bien est analysé, positionné et présenté.",
    ),
    (
        "Per questo ogni analisi deve essere costruita sulla micro-zona reale.",
        "C'est pourquoi chaque analyse doit être construite à partir de la micro-zone réelle.",
    ),
    ("Nessun obbligo dopo l’analisi", "Aucune obligation après l’analyse"),
    ("Perché non basta una stima online?", "Pourquoi une estimation en ligne ne suffit-elle pas ?"),
    (
        "Perché hai inserito RE/MAX nella pagina?",
        "Pourquoi avoir mentionné RE/MAX sur cette page ?",
    ),
    (
        "Quanto tempo serve per ricevere l'analisi?",
        "Combien de temps faut-il pour recevoir l'analyse ?",
    ),
    (
        "Lavori solo su Milano o anche in provincia?",
        "Travaillez-vous uniquement à Milan ou aussi en province ?",
    ),
    (
        "Cosa succede dopo l'analisi se decido di non vendere?",
        "Que se passe-t-il après l'analyse si je décide de ne pas vendre ?",
    ),
    (
        "Non ho fretta di vendere. Ha senso farlo ora?",
        "Je ne suis pas pressé de vendre. Est-ce utile de le faire maintenant ?",
    ),
    ("Ricevi l’analisi del tuo immobile", "Recevez l’analyse de votre bien"),
    (
        "Agente Immobiliare affiliato RE/MAX · REA BS-639579 · P.IVA 14597560961 · Milano",
        "Agent immobilier affilié RE/MAX · REA BS-639579 · P.IVA 14597560961 · Milan",
    ),
    ("Zona o comune dell'immobile", "Quartier ou commune du bien"),
    ("Zona o comune dell’immobile", "Quartier ou commune du bien"),
    (
        "Scrivi quartiere o comune (es. Brera, Sesto San Giovanni...)",
        "Indiquez le quartier ou la commune (ex. Brera, Sesto San Giovanni...)",
    ),
    ("Tipologia immobile", "Type de bien"),
    (
        "Es. piano, stato dell'immobile, box o giardino",
        "Ex. étage, état du bien, box ou jardin",
    ),
    (
        "Es. piano, stato dell’immobile, box o giardino",
        "Ex. étage, état du bien, box ou jardin",
    ),
    ("Informativa privacy", "Politique de confidentialité"),
    ("Avanzamento form", "Progression du formulaire"),
]


PHRASES_FR_GAP: list[tuple[str, str]] = sorted(
    _expand_entity_variants(_BASE_PHRASES_FR_GAP),
    key=lambda phrase: len(phrase[0]),
    reverse=True,
)
