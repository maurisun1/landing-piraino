"""Professional DE/FR translations for seller landing pages."""

from __future__ import annotations

import json
import re
from urllib.parse import quote

from buyer_provinces import LOMBARD_PROVINCES
from locales import buyer_hub_url, buyer_province_url, city_label, seller_url
from seller_localize import SELLER_LOCALIZE
from seller_localize_i18n import get_localize_block
from seller_phrases_bergamo import PHRASES_BERGAMO_DE, PHRASES_BERGAMO_FR
from seller_phrases_brescia import PHRASES_BRESCIA_DE, PHRASES_BRESCIA_FR
from seller_phrases_fr_gap import PHRASES_FR_GAP
from seller_province_templates import apply_province_all

# Full-phrase replacements only — never single-word swaps.
PHRASES_DE: list[tuple[str, str]] = [
    ("Prima di vendere casa a Milano, serve capire davvero quanto vale.",
     "Bevor Sie in Mailand verkaufen, müssen Sie den realen Wert Ihrer Immobilie kennen."),
    ("Prima di vendere in provincia di Varese, serve capire davvero quanto vale.",
     "Bevor Sie in der Provinz Varese verkaufen, müssen Sie den realen Wert Ihrer Immobilie kennen."),
    ("A Milano, vendere bene non è fortuna. È strategia.",
     "In Mailand ist gut verkaufen kein Glück — es ist Strategie."),
    ("A Bergamo e provincia, vendere bene non è fortuna. È strategia.",
     "In Bergamo und Provinz ist gut verkaufen kein Glück — es ist Strategie."),
    ("A Brescia e provincia, vendere bene non è fortuna. È strategia.",
     "In Brescia und Provinz ist gut verkaufen kein Glück — es ist Strategie."),
    ("Le domande che ricevo più spesso.", "Die häufigsten Fragen."),
    ("Situazioni reali affrontate con metodo e strategia.", "Reale Verkaufssituationen — mit Methode und Strategie."),
    ("Personal brand forte, supportato da un network internazionale.",
     "Persönliche Beratung, gestützt von einem internationalen Netzwerk."),
    ("Prima l'analisi. Poi la vendita.", "Zuerst die Analyse. Dann der Verkauf."),
    ("Prima l’analisi. Poi la vendita.", "Zuerst die Analyse. Dann der Verkauf."),
    ("Chi vende bene parte prima degli altri.", "Wer gut verkauft, beginnt früher als die anderen."),
    ("Scopri quanto vale davvero il tuo immobile.", "Erfahren Sie den realen Wert Ihrer Immobilie."),
    ("Tutto ciò che serve per vendere con metodo.",
     "Alles, was Sie für einen strukturierten Verkauf brauchen."),
    ("Conosco il mercato locale, strada per strada.",
     "Ich kenne den lokalen Markt — Straße für Straße."),
    ("Stima automatica vs analisi professionale.",
     "Automatische Schätzung vs. professionelle Analyse."),
    ("L'analisi riservata non è una stima automatica.",
     "Die vertrauliche Analyse ist keine automatische Schätzung."),
    ("Milano · Analisi immobiliare riservata", "Mailand · Vertrauliche Immobilienanalyse"),
    ("Ricevi una consulenza immobiliare riservata",
     "Erhalten Sie eine vertrauliche Immobilienberatung"),
    ("Nessuna stima automatica. Solo analisi reale basata sul mercato della tua zona.",
     "Keine automatische Schätzung. Nur eine echte Analyse auf Basis Ihres lokalen Marktes."),
    ("Ogni quartiere ha dinamiche diverse. <strong>Un prezzo sbagliato può costarti mesi sul mercato</strong> o migliaia di euro nella trattativa. Prima della vendita, servono dati reali, metodo e posizionamento corretto.",
     "Jedes Viertel hat eigene Dynamiken. <strong>Ein falscher Preis kann Sie Monate auf dem Markt kosten</strong> oder in der Verhandlung Tausende Euro. Vor dem Verkauf brauchen Sie echte Daten, Methode und die richtige Positionierung."),
    ("Risposta entro 24 ore, nessun obbligo di incarico",
     "Antwort innerhalb von 24 Stunden, keine Verpflichtung zum Mandat"),
    ("OMI-Analyse per zona e tipologia", "OMI-Analyse nach Zone und Objekttyp"),
    ("Posizionamento prezzo basato su dati reali",
     "Preispositionierung auf Basis realer Daten"),
    ("Supporto in trattativa fino al rogito",
     "Begleitung in der Verhandlung bis zum Notartermin"),
    ("Supporto in Verhandlung fino al Notartermin",
     "Begleitung in der Verhandlung bis zum Notartermin"),
    ("Scrivimi su WhatsApp", "Schreiben Sie mir auf WhatsApp"),
    ("Contattami su WhatsApp", "Kontaktieren Sie mich per WhatsApp"),
    ("Scegli il tuo percorso", "Wählen Sie Ihren Weg"),
    ("Vuoi vendere", "Sie möchten verkaufen"),
    ("Analisi del tuo immobile", "Analyse Ihrer Immobilie"),
    ("Valutazione riservata su dati OMI e micro-zona. Nessun obbligo di incarico.",
     "Vertrauliche Bewertung auf OMI-Daten und Mikrozonen-Basis. Keine Verpflichtung zum Mandat."),
    ("Richiedi analisi →", "Analyse anfordern →"),
    ("Richiedi l'analisi gratuita", "Kostenlose Analyse anfordern"),
    ("Richiedi analisi", "Analyse anfordern"),
    ("Richiedi Analisi", "Analyse anfordern"),
    ("Cerchi casa", "Sie suchen eine Immobilie"),
    ("Consulenza acquirente", "Käuferberatung"),
    ("Milano e 12 province lombarde. Non pagare l'emozione del momento.",
     "Mailand und 12 Provinzen der Lombardei. Zahlen Sie nicht für die Emotion des Moments."),
    ("Comprare a Milano →", "In Mailand kaufen →"),
    ("Stai cercando casa? →", "Suchen Sie eine Immobilie? →"),
    ("Paesi con RE/MAX nel mondo", "Länder mit RE/MAX weltweit"),
    ("Province lombarde seguite", "Betreute Provinzen der Lombardei"),
    ("Provincia MI", "Provinz MI"),
    ("Risposta alla tua richiesta", "Antwort auf Ihre Anfrage"),
    ("Analisi iniziale · nessun obbligo", "Erstanalyse · keine Verpflichtung"),
    ("Cosa ricevi", "Was Sie erhalten"),
    ("È un confronto strutturato sul tuo immobile, sulla micro-zona e sulla strategia di vendita più adatta a Milano.",
     "Es ist ein strukturierter Vergleich Ihrer Immobilie, der Mikrozone und der für Mailand passendsten Verkaufsstrategie."),
    ("Valore di mercato reale", "Realer Marktwert"),
    ("Confronto con immobili comparabili venduti e in vendita nella tua zona, non medie generiche.",
     "Vergleich mit verkauften und angebotenen Vergleichsobjekten in Ihrer Zone — keine generischen Durchschnittswerte."),
    ("Dati OMI ufficiali", "Offizielle OMI-Daten"),
    ("Riferimenti Agenzia delle Entrate integrati con il contesto reale del quartiere o del comune.",
     "Referenzwerte der Steuerbehörde, integriert mit dem realen Kontext des Viertels oder der Gemeinde."),
    ("Criticità tecniche", "Technische Risiken"),
    ("Piano, conformità, stato, spazi esterni: ciò che un acquirente farà emergere in trattativa.",
     "Etage, Konformität, Zustand, Außenbereiche: was ein Käufer in der Verhandlung anspricht."),
    ("Tempi di vendita stimati", "Geschätzte Verkaufsdauer"),
    ("Quanto potrebbe restare online un immobile posizionato correttamente — o no — nel mercato attuale.",
     "Wie lange eine Immobilie im aktuellen Markt online bleiben könnte — bei richtiger oder falscher Positionierung."),
    ("Strategia di prezzo", "Preisstrategie"),
    ("Range consigliato, leva trattativa e timing di uscita sul mercato.",
     "Empfohlene Spanne, Verhandlungsspielraum und optimaler Marktstart."),
    ("Piano RE/MAX", "RE/MAX-Plan"),
    ("Visibilità, rete MLS e canali se decidi di procedere — sempre senza obbligo dopo l'analisi.",
     "Sichtbarkeit, MLS-Netzwerk und Kanäle, wenn Sie fortfahren — stets ohne Verpflichtung nach der Analyse."),
    ("Perché non basta online", "Warum Online allein nicht reicht"),
    ("Le valutazioni online sono utili come punto di partenza, ma non sostituiscono una lettura tecnica e di mercato del singolo immobile.",
     "Online-Schätzungen sind ein guter Ausgangspunkt, ersetzen aber keine technische und marktbezogene Bewertung der einzelnen Immobilie."),
    ("Criterio", "Kriterium"),
    ("Stima online", "Online-Schätzung"),
    ("Analisi RE/MAX", "RE/MAX-Analyse"),
    ("Micro-zona e quartiere", "Mikrozone und Viertel"),
    ("Media generica", "Generischer Durchschnitt"),
    ("Analisi specifica", "Spezifische Analyse"),
    ("Stato, piano, affaccio", "Zustand, Etage, Ausrichtung"),
    ("Non considerati", "Nicht berücksichtigt"),
    ("Valutati uno per uno", "Einzeln bewertet"),
    ("Documenti e conformità", "Dokumente und Konformität"),
    ("Assenti", "Fehlend"),
    ("Verifica tecnica", "Technische Prüfung"),
    ("Strategia di vendita", "Verkaufsstrategie"),
    ("Solo un numero", "Nur eine Zahl"),
    ("Piano completo", "Vollständiger Plan"),
    ("Obbligo di incarico", "Verpflichtung zum Mandat"),
    ("Mai, alla prima analisi", "Nie bei der Erstanalyse"),
    ("Zone servite · Milano", "Betreute Zonen · Mailand"),
    ("Milano cambia quartiere per quartiere.",
     "Mailand ändert sich von Viertel zu Viertel."),
    ("Un appartamento a Porta Romana non segue le stesse dinamiche di Lambrate, Isola o Navigli.",
     "Eine Wohnung in Porta Romana folgt nicht denselben Dynamiken wie in Lambrate, Isola oder Navigli."),
    ("Consulta i valori OMI ufficiali per zona a Milano →",
     "Offizielle OMI-Werte nach Zone in Mailand →"),
    ("Consulta i valori OMI per zona a Milano →",
     "OMI-Werte nach Zone in Mailand →"),
    ("Servizi", "Leistungen"),
    ("Dalla prima analisi alla firma dal notaio: un percorso chiaro, senza improvvisazione.",
     "Von der Erstanalyse bis zur notariellen Beurkundung: ein klarer Weg ohne Improvisation."),
    ("Analisi e valutazione", "Analyse und Bewertung"),
    ("Studio del mercato locale, comparables, OMI e posizionamento prezzo iniziale.",
     "Studium des lokalen Marktes, Vergleichsobjekte, OMI und initiale Preispositionierung."),
    ("Preparazione immobile", "Objektvorbereitung"),
    ("Home staging consigliato, documenti in ordine, presentazione che valorizza i punti di forza.",
     "Empfohlenes Home Staging, ordentliche Dokumente, Präsentation der Stärken."),
    ("Marketing RE/MAX", "RE/MAX-Marketing"),
    ("Foto professionali, portali, rete MLS e visibilità internazionale del brand.",
     "Professionelle Fotos, Portale, MLS-Netzwerk und internationale Markenpräsenz."),
    ("Open House", "Open House"),
    ("Porte aperte organizzate per attrarre più acquirenti qualificati in poche ore, con gestione professionale delle visite.",
     "Organisierte Tage der offenen Tür, um in wenigen Stunden mehr qualifizierte Käufer anzuziehen."),
    ("Trattativa e rogito", "Verhandlung und Notartermin"),
    ("Gestione offerte, negoziazione e affiancamento fino al passaggio definitivo.",
     "Angebotsmanagement, Verhandlung und Begleitung bis zum endgültigen Abschluss."),
    ("Analisi riservata basata su dati reali. Nessun obbligo di incarico, risposta entro 24 ore.",
     "Vertrauliche Analyse auf realen Daten. Keine Verpflichtung zum Mandat, Antwort innerhalb von 24 Stunden."),
    ("Questo servizio è per te se", "Dieser Service ist für Sie, wenn"),
    ("Ogni vendita ha criticità diverse. Il primo passo è capire cosa può rallentare, svalutare o valorizzare il tuo immobile.",
     "Jeder Verkauf hat andere Herausforderungen. Der erste Schritt: verstehen, was Ihre Immobilie verzögern, entwerten oder aufwerten kann."),
    ("Vuoi capire se è il momento giusto",
     "Sie möchten wissen, ob der Zeitpunkt stimmt"),
    ("Prima di decidere, vuoi leggere il mercato reale della tua zona e non muoverti a sensazione.",
     "Bevor Sie entscheiden, möchten Sie den realen Markt Ihrer Zone lesen — nicht nach Gefühl handeln."),
    ("Il tuo immobile è fermo sul mercato",
     "Ihre Immobilie steht am Markt fest"),
    ("Mesi online, poche visite, offerte basse: spesso il problema non è la casa, ma il posizionamento.",
     "Monate online, wenige Besichtigungen, niedrige Angebote: oft liegt es nicht an der Immobilie, sondern an der Positionierung."),
    ("Hai ricevuto valutazioni troppo diverse",
     "Sie haben sehr unterschiedliche Bewertungen erhalten"),
    ("Vuoi capire su quali dati si basa il prezzo e distinguere una stima seria da una promessa.",
     "Sie möchten verstehen, worauf der Preis basiert, und eine seriöse Schätzung von einer leeren Zusage unterscheiden."),
    ("Vuoi decidere con dati, non promesse",
     "Sie möchten mit Daten entscheiden, nicht mit Versprechen"),
    ("Prima di firmare qualsiasi cosa, vuoi una strategia chiara, riservata e motivata.",
     "Bevor Sie etwas unterschreiben, möchten Sie eine klare, vertrauliche und fundierte Strategie."),
    ("Il mio approccio", "Mein Ansatz"),
    ("Opero come consulente immobiliare con RE/MAX Associati Real Estate a Milano, agenzia con oltre 25 anni di attività sul mercato e tra le prime 30 RE/MAX in Italia. Questo mi permette di unire un metodo consulenziale personale alla forza di una rete internazionale.",
     "Ich arbeite als Immobilienberater mit RE/MAX Associati Real Estate in Mailand — einer Agentur mit über 25 Jahren Markterfahrung und unter den Top-30-RE/MAX-Büros in Italien. So verbinde ich persönliche Beratung mit der Stärke eines internationalen Netzwerks."),
    ("Sono un Agente Immobiliare affiliato RE/MAX con background tecnico e imprenditoriale. Questo significa leggere un immobile in modo diverso: individuare criticità, valorizzare i punti forti e costruire una strategia reale prima ancora della pubblicazione online.",
     "Als RE/MAX-Immobilienberater mit technischem und unternehmerischem Hintergrund lese ich Immobilien anders: Risiken erkennen, Stärken hervorheben und eine echte Strategie — noch vor der Online-Veröffentlichung."),
    ("“Quando entro in una casa, osservo già quello che un acquirente farà notare durante la trattativa.”",
     "„Wenn ich eine Immobilie betrete, sehe ich bereits, was ein Käufer in der Verhandlung ansprechen wird.“"),
    ("La maggior parte degli immobili perde forza nelle prime settimane online non per colpa della casa, ma per una strategia sbagliata. Il mio lavoro è evitare che questo accada.",
     "Die meisten Immobilien verlieren in den ersten Wochen online an Kraft — nicht wegen der Immobilie, sondern wegen einer falschen Strategie. Meine Aufgabe ist es, das zu verhindern."),
    ("Analisi reale", "Echte Analyse"),
    ("Confronti concreti, andamento della zona e posizionamento corretto del prezzo.",
     "Konkrete Vergleiche, Entwicklung der Zone und korrekte Preispositionierung."),
    ("Strategia personalizzata", "Individuelle Strategie"),
    ("Ogni immobile richiede comunicazione, timing e target differenti.",
     "Jede Immobilie braucht andere Kommunikation, Timing und Zielgruppe."),
    ("Trattativa guidata", "Geführte Verhandlung"),
    ("Dalla prima visita alla firma dal notaio, senza improvvisazione.",
     "Von der ersten Besichtigung bis zur notariellen Beurkundung — ohne Improvisation."),
    ("Affiliazione RE/MAX", "RE/MAX-Affiliation"),
    ("La mia consulenza rimane personale e diretta. L'affiliazione RE/MAX aggiunge autorevolezza, rete, collaborazione e maggiore visibilità commerciale all'immobile.",
     "Meine Beratung bleibt persönlich und direkt. Die RE/MAX-Affiliation verleiht Autorität, Netzwerk, Zusammenarbeit und mehr kommerzielle Sichtbarkeit."),
    ("La mia consulenza rimane personale e diretta. L’affiliazione RE/MAX aggiunge autorevolezza, rete, collaborazione e maggiore visibilità commerciale all’immobile.",
     "Meine Beratung bleibt persönlich und direkt. Die RE/MAX-Affiliation verleiht Autorität, Netzwerk, Zusammenarbeit und mehr kommerzielle Sichtbarkeit."),
    ("Un marchio riconoscibile aiuta il proprietario e rassicura molti acquirenti nella fase iniziale.",
     "Eine bekannte Marke hilft dem Eigentümer und beruhigt viele Käufer in der Anfangsphase."),
    ("La collaborazione tra professionisti può aumentare le possibilità di intercettare acquirenti qualificati.",
     "Die Zusammenarbeit zwischen Profis kann die Chancen erhöhen, qualifizierte Käufer zu erreichen."),
    ("La differenza resta nel modo in cui l'immobile viene analizzato, posizionato e presentato.",
     "Der Unterschied liegt darin, wie die Immobilie analysiert, positioniert und präsentiert wird."),
    ("Mercato Milano", "Markt Mailand"),
    ("Per questo ogni analisi deve essere costruita sulla micro-zona reale.",
     "Deshalb muss jede Analyse auf der realen Mikrozone basieren."),
    ("Il valore non si calcola solo al metro quadro: contano piano, stato, affaccio, contesto e domanda reale.",
     "Der Wert ergibt sich nicht nur aus dem Quadratmeterpreis: Etage, Zustand, Ausrichtung, Kontext und reale Nachfrage zählen."),
    ("Prima dell'annuncio va capito chi è l'acquirente più probabile e cosa lo convince a fare un'offerta.",
     "Vor der Anzeige muss klar sein, wer der wahrscheinlichste Käufer ist und was ihn zum Angebot bewegt."),
    ("Il momento di lancio, il prezzo iniziale e la comunicazione incidono sulla forza della trattativa.",
     "Startzeitpunkt, Anfangspreis und Kommunikation beeinflussen die Verhandlungsstärke."),
    ("Come funziona", "So funktioniert es"),
    ("Tre passi. Nessuna sorpresa.", "Drei Schritte. Keine Überraschungen."),
    ("Dalla prima analisi alla possibile strategia di vendita: ogni fase è chiara, definita e concordata con te.",
     "Von der Erstanalyse bis zur möglichen Verkaufsstrategie: jede Phase ist klar, definiert und mit Ihnen abgestimmt."),
    ("Analisi immobiliare riservata", "Vertrauliche Immobilienanalyse"),
    ("Leggo l'immobile, la zona e ti mostro dati, criticità e potenzialità prima di parlare di incarico.",
     "Ich lese die Immobilie und die Zone und zeige Ihnen Daten, Risiken und Potenziale — bevor wir über ein Mandat sprechen."),
    ("Leggo l’immobile, la zona e ti mostro dati, criticità e potenzialità prima di parlare di incarico.",
     "Ich lese die Immobilie und die Zone und zeige Ihnen Daten, Risiken und Potenziale — bevor wir über ein Mandat sprechen."),
    ("Strategia e posizionamento", "Strategie und Positionierung"),
    ("Definiamo prezzo, timing, comunicazione e profilo dell'acquirente più adatto.",
     "Wir definieren Preis, Timing, Kommunikation und das passende Käuferprofil."),
    ("Eventuale vendita guidata", "Ggf. geführter Verkauf"),
    ("Se decidi di procedere, ti accompagno in visite, offerte, trattativa e passaggi tecnici.",
     "Wenn Sie fortfahren, begleite ich Sie bei Besichtigungen, Angeboten, Verhandlung und technischen Schritten."),
    ("Primo confronto", "Erstes Gespräch"),
    ("Metodo chiaro", "Klare Methode"),
    ("Nessun obbligo dopo l'analisi", "Keine Verpflichtung nach der Analyse"),
    ("Nessun obbligo dopo l’analisi", "Keine Verpflichtung nach der Analyse"),
    ("Esperienze", "Erfahrungen"),
    ("Se richiedo l'analisi, sono obbligato a darti l'incarico?",
     "Bin ich verpflichtet, Ihnen ein Mandat zu erteilen, wenn ich die Analyse anfordere?"),
    ("Se richiedo l’analisi, sono obbligato a darti l’incarico?",
     "Bin ich verpflichtet, Ihnen ein Mandat zu erteilen, wenn ich die Analyse anfordere?"),
    ("No. L'analisi iniziale non crea obbligo di conferimento incarico. Serve a darti informazioni chiare per decidere meglio.",
     "Nein. Die Erstanalyse begründet keine Verpflichtung zur Beauftragung. Sie gibt Ihnen klare Informationen für eine bessere Entscheidung."),
    ("Perché non basta una stima online?",
     "Warum reicht eine Online-Schätzung nicht?"),
    ("Le stime automatiche non vedono stato interno, piano, affaccio, criticità documentali, domanda reale e concorrenza nella micro-zona.",
     "Automatische Schätzungen berücksichtigen weder Innenzustand, Etage, Ausrichtung, dokumentarische Risiken, reale Nachfrage noch die Konkurrenz in der Mikrozone."),
    ("Perché hai inserito RE/MAX nella pagina?",
     "Warum ist RE/MAX auf dieser Seite erwähnt?"),
    ("Per trasparenza e fiducia. La consulenza resta personale, ma l'affiliazione al network RE/MAX aggiunge riconoscibilità e supporto commerciale.",
     "Aus Transparenz und Vertrauen. Die Beratung bleibt persönlich, die RE/MAX-Affiliation verleiht aber Wiedererkennung und kommerzielle Unterstützung."),
    ("Quanto tempo serve per ricevere l'analisi?",
     "Wie lange dauert es, die Analyse zu erhalten?"),
    ("Di solito entro 24–48 ore lavorative dal modulo. Se serve approfondire documenti o visite, te lo comunico subito con tempi chiari.",
     "In der Regel innerhalb von 24–48 Werktunden nach dem Formular. Bei Bedarf an Dokumenten oder Besichtigungen teile ich Ihnen sofort klare Fristen mit."),
    ("Lavori solo su Milano o anche in provincia?",
     "Arbeiten Sie nur in Mailand oder auch in der Provinz?"),
    ("Opero su Milano e provincia e, tramite RE/MAX, posso coordinarmi anche con colleghi nelle altre province lombarde se il tuo immobile o il tuo obiettivo lo richiede.",
     "Ich arbeite in Mailand und Provinz und kann über RE/MAX auch mit Kollegen in anderen Provinzen der Lombardei koordinieren, wenn Ihre Immobilie oder Ihr Ziel es erfordert."),
    ("Cosa succede dopo l'analisi se decido di non vendere?",
     "Was passiert nach der Analyse, wenn ich mich gegen einen Verkauf entscheide?"),
    ("Nessun problema. L'analisi resta un asset per te: saprai il valore reale, i tempi di mercato e cosa conviene fare quando deciderai di muoverti.",
     "Kein Problem. Die Analyse bleibt ein Vorteil für Sie: Sie kennen den realen Wert, die Marktzeiten und was sich lohnt, wenn Sie sich bewegen."),
    ("Non ho fretta di vendere. Ha senso farlo ora?",
     "Ich habe es nicht eilig zu verkaufen. Lohnt sich eine Analyse jetzt?"),
    ("Sì. Sapere oggi quanto vale il tuo immobile ti permette di pianificare senza pressione e scegliere il momento migliore.",
     "Ja. Den heutigen Wert Ihrer Immobilie zu kennen, ermöglicht Planung ohne Druck und die Wahl des besten Zeitpunkts."),
    ("Ti mostro il mercato reale della tua zona, le criticità dell'immobile e la strategia più adatta prima ancora di parlare di incarico.",
     "Ich zeige Ihnen den realen Markt Ihrer Zone, die Risiken der Immobilie und die passende Strategie — bevor wir über ein Mandat sprechen."),
    ("Ti mostro il mercato reale della tua zona, le criticità dell’immobile e la strategia più adatta prima ancora di parlare di incarico.",
     "Ich zeige Ihnen den realen Markt Ihrer Zone, die Risiken der Immobilie und die passende Strategie — bevor wir über ein Mandat sprechen."),
    ("Ricevi l'analisi del tuo immobile", "Erhalten Sie die Analyse Ihrer Immobilie"),
    ("Ricevi l’analisi del tuo immobile", "Erhalten Sie die Analyse Ihrer Immobilie"),
    ("Maurizio Piraino — Consulente immobiliare presso RE/MAX Associati Real Estate · Milano, Viale Gran Sasso 31",
     "Maurizio Piraino — Immobilienberater bei RE/MAX Associati Real Estate · Mailand, Viale Gran Sasso 31"),
    ("Agente Immobiliare affiliato RE/MAX · REA BS-639579 · P.IVA 14597560961 · Milano",
     "RE/MAX-Immobilienberater · REA BS-639579 · USt-IdNr. 14597560961 · Mailand"),
    ("La consulenza iniziale non costituisce obbligo di conferimento incarico.",
     "Die Erstberatung begründet keine Verpflichtung zur Beauftragung."),
    ("Sedi operative:", "Standorte:"),
    ("Guide prezzi OMI:", "OMI-Preisguides:"),
    ("Vuoi comprare?", "Möchten Sie kaufen?"),
    ("Tutte le province lombarde (12)", "Alle 12 Provinzen der Lombardei"),
    ("Due informazioni sull'immobile, per preparare un'analisi più precisa.",
     "Zwei Angaben zur Immobilie für eine präzisere Analyse."),
    ("Due informazioni sull’immobile, per preparare un’analisi più precisa.",
     "Zwei Angaben zur Immobilie für eine präzisere Analyse."),
    ("Zona o comune dell'immobile", "Zone oder Gemeinde der Immobilie"),
    ("Zona o comune dell’immobile", "Zone oder Gemeinde der Immobilie"),
    ("Scrivi quartiere o comune (es. Brera, Sesto San Giovanni...)",
     "Stadtteil oder Gemeinde eingeben (z. B. Brera, Sesto San Giovanni …)"),
    ("Tipologia immobile", "Objekttyp"),
    ("Es. piano, stato dell'immobile, box o giardino",
     "z. B. Etage, Zustand, Garage oder Garten"),
    ("Es. piano, stato dell’immobile, box o giardino",
     "z. B. Etage, Zustand, Garage oder Garten"),
    ("Dati riservati · Nessun obbligo di incarico · Risposta personale",
     "Vertrauliche Daten · Keine Verpflichtung zum Mandat · Persönliche Antwort"),
    ("Inviando il form acconsenti al trattamento dei dati per essere ricontattato.",
     "Mit dem Absenden stimmen Sie der Datenverarbeitung zur Kontaktaufnahme zu."),
    ("Informativa privacy", "Datenschutzerklärung"),
    ("Avanzamento form", "Formularfortschritt"),
    ("Azioni rapide", "Schnellaktionen"),
    ("Salta al contenuto", "Zum Inhalt springen"),
    ("Apri menu", "Menü öffnen"),
    ("Menu principale", "Hauptmenü"),
    ("Agente Immobiliare affiliato RE/MAX", "RE/MAX-Immobilienberater"),
    ("Agente Immobiliare affiliato RE/MAX · Milano", "RE/MAX-Immobilienberater · Mailand"),
    ("Approccio strategico", "Strategischer Ansatz"),
    ("Geometra", "Vermessungsingenieur"),
    ("Consulenza immobiliare", "Immobilienberatung"),
    ("Consulenza vendita", "Verkäuferberatung"),
    ("Percorso", "Weg"),
    ("Vendere", "Verkaufen"),
    ("Comprare", "Kaufen"),
    ("Chi sono", "Über mich"),
    ("Domande frequenti", "Häufige Fragen"),
    ("Mercato", "Markt"),
    ("Pronto a vendere", "Bereit zu verkaufen"),
    ("Richiedi una consulenza", "Beratung anfordern"),
    ("Analisi OMI", "OMI-Analyse"),
    ("micro-zona", "Mikrozone"),
    ("Micro-zona", "Mikrozone"),
    ("Agenzia delle Entrate", "Italienische Steuerbehörde"),
    ("Agenzia Entrate", "Italienische Steuerbehörde"),
    ("Rete internazionale", "Internationales Netzwerk"),
    ("Risposta entro 24h", "Antwort innerhalb von 24h"),
    ("Nessun obbligo di incarico", "Keine Verpflichtung zum Mandat"),
    ("Prima l'analisi. Poi la scelta giusta.", "Zuerst die Analyse. Dann die richtige Wahl."),
]

PHRASES_FR: list[tuple[str, str]] = [
    ("Prima di vendere casa a Milano, serve capire davvero quanto vale.",
     "Avant de vendre à Milan, il faut connaître la vraie valeur de votre bien."),
    ("A Milano, vendere bene non è fortuna. È strategia.",
     "À Milan, bien vendre n'est pas une question de chance — c'est une stratégie."),
    ("A Bergamo e provincia, vendere bene non è fortuna. È strategia.",
     "À Bergame et en province, bien vendre n'est pas une question de chance — c'est une stratégie."),
    ("A Brescia e provincia, vendere bene non è fortuna. È strategia.",
     "À Brescia et en province, bien vendre n'est pas une question de chance — c'est une stratégie."),
    ("Le domande che ricevo più spesso.", "Les questions les plus fréquentes."),
    ("Situazioni reali affrontate con metodo e strategia.", "Des situations réelles, traitées avec méthode et stratégie."),
    ("Personal brand forte, supportato da un network internazionale.",
     "Une approche personnelle, soutenue par un réseau international."),
    ("Prima l'analisi. Poi la vendita.", "D'abord l'analyse. Ensuite la vente."),
    ("Prima l’analisi. Poi la vendita.", "D'abord l'analyse. Ensuite la vente."),
    ("Chi vende bene parte prima degli altri.", "Ceux qui vendent bien commencent avant les autres."),
    ("Scopri quanto vale davvero il tuo immobile.", "Découvrez la vraie valeur de votre bien."),
    ("Tutto ciò che serve per vendere con metodo.",
     "Tout ce qu'il faut pour vendre avec méthode."),
    ("Conosco il mercato locale, strada per strada.",
     "Je connais le marché local — rue par rue."),
    ("Stima automatica vs analisi professionale.",
     "Estimation automatique vs analyse professionnelle."),
    ("L'analisi riservata non è una stima automatica.",
     "L'analyse confidentielle n'est pas une estimation automatique."),
    ("Milano · Analisi immobiliare riservata", "Milan · Analyse immobilière confidentielle"),
    ("Ricevi una consulenza immobiliare riservata",
     "Recevez une consultation immobilière confidentielle"),
    ("Nessuna stima automatica. Solo analisi reale basata sul mercato della tua zona.",
     "Pas d'estimation automatique. Une analyse réelle basée sur votre marché local."),
    ("Ogni quartiere ha dinamiche diverse. <strong>Un prezzo sbagliato può costarti mesi sul mercato</strong> o migliaia di euro nella trattativa. Prima della vendita, servono dati reali, metodo e posizionamento corretto.",
     "Chaque quartier a ses dynamiques. <strong>Un mauvais prix peut vous coûter des mois sur le marché</strong> ou des milliers d'euros en négociation. Avant de vendre, il faut des données réelles, une méthode et un positionnement juste."),
    ("Risposta entro 24 ore, nessun obbligo di incarico",
     "Réponse sous 24 heures, aucune obligation de mandat"),
    ("Analisi OMI per zona e tipologia", "Analyse OMI par zone et type de bien"),
    ("Posizionamento prezzo basato su dati reali",
     "Positionnement du prix basé sur des données réelles"),
    ("Supporto in trattativa fino al rogito",
     "Accompagnement en négociation jusqu'à l'acte notarié"),
    ("Scrivimi su WhatsApp", "Écrivez-moi sur WhatsApp"),
    ("Contattami su WhatsApp", "Contactez-moi sur WhatsApp"),
    ("Scegli il tuo percorso", "Choisissez votre parcours"),
    ("Vuoi vendere", "Vous vendez"),
    ("Analisi del tuo immobile", "Analyse de votre bien"),
    ("Valutazione riservata su dati OMI e micro-zona. Nessun obbligo di incarico.",
     "Évaluation confidentielle sur données OMI et micro-zone. Aucune obligation de mandat."),
    ("Richiedi analisi →", "Demander une analyse →"),
    ("Richiedi l'analisi gratuita", "Demander l'analyse gratuite"),
    ("Richiedi analisi", "Demander une analyse"),
    ("Richiedi Analisi", "Demander une analyse"),
    ("Cerchi casa", "Vous cherchez un bien"),
    ("Consulenza acquirente", "Conseil acheteurs"),
    ("Milano e 12 province lombarde. Non pagare l'emozione del momento.",
     "Milan et 12 provinces lombardes. Ne payez pas l'émotion du moment."),
    ("Comprare a Milano →", "Acheter à Milan →"),
    ("Stai cercando casa? →", "Vous cherchez un bien ? →"),
    ("Paesi con RE/MAX nel mondo", "Pays avec RE/MAX dans le monde"),
    ("Province lombarde seguite", "Provinces lombardes couvertes"),
    ("Provincia MI", "Province MI"),
    ("Risposta alla tua richiesta", "Réponse à votre demande"),
    ("Analisi iniziale · nessun obbligo", "Analyse initiale · sans obligation"),
    ("Cosa ricevi", "Ce que vous recevez"),
    ("Perché non basta online", "Pourquoi le web ne suffit pas"),
    ("Come funziona", "Comment ça marche"),
    ("Tre passi. Nessuna sorpresa.", "Trois étapes. Sans surprise."),
    ("Esperienze", "Expériences"),
    ("Il mio approccio", "Mon approche"),
    ("Affiliazione RE/MAX", "Affiliation RE/MAX"),
    ("Mercato Milano", "Marché Milan"),
    ("Servizi", "Services"),
    ("Questo servizio è per te se", "Ce service est pour vous si"),
    ("Sedi operative:", "Bureaux :"),
    ("Guide prezzi OMI:", "Guides prix OMI :"),
    ("Vuoi comprare?", "Vous souhaitez acheter ?"),
    ("Tutte le province lombarde (12)", "Les 12 provinces lombardes"),
    ("Salta al contenuto", "Aller au contenu"),
    ("Apri menu", "Ouvrir le menu"),
    ("Menu principale", "Menu principal"),
    ("Agente Immobiliare affiliato RE/MAX", "Agent immobilier RE/MAX"),
    ("Agente Immobiliare affiliato RE/MAX · Milano", "Agent immobilier RE/MAX · Milan"),
    ("Approccio strategico", "Approche stratégique"),
    ("Geometra", "Géomètre"),
    ("Consulenza immobiliare", "Conseil immobilier"),
    ("Consulenza vendita", "Conseil vendeur"),
    ("Percorso", "Parcours"),
    ("Vendere", "Vendre"),
    ("Comprare", "Acheter"),
    ("Chi sono", "Qui je suis"),
    ("Domande frequenti", "Questions fréquentes"),
    ("Mercato", "Marché"),
    ("Pronto a vendere", "Prêt à vendre"),
    ("Richiedi una consulenza", "Demander un conseil"),
    ("Analisi OMI", "Analyse OMI"),
    ("micro-zona", "micro-zone"),
    ("Micro-zona", "Micro-zone"),
    ("Agenzia delle Entrate", "Agence des Entrées"),
    ("Agenzia Entrate", "Agence des Entrées"),
    ("Rete internazionale", "Réseau international"),
    ("Risposta entro 24h", "Réponse sous 24h"),
    ("Nessun obbligo di incarico", "Aucune obligation de mandat"),
    ("Prima l'analisi. Poi la scelta giusta.", "D'abord l'analyse. Ensuite le bon choix."),
    ("Opero come consulente immobiliare con RE/MAX Associati Real Estate a Milano, agenzia con oltre 25 anni di attività sul mercato e tra le prime 30 RE/MAX in Italia. Questo mi permette di unire un metodo consulenziale personale alla forza di una rete internazionale.",
     "J'opère comme consultant immobilier avec RE/MAX Associati Real Estate à Milan, une agence avec plus de 25 ans d'activité sur le marché et parmi les 30 premières RE/MAX en Italie. Cela me permet d'allier une approche conseil personnelle à la force d'un réseau international."),
    ("Maurizio Piraino — Consulente immobiliare presso RE/MAX Associati Real Estate · Milano, Viale Gran Sasso 31",
     "Maurizio Piraino — Consultant immobilier chez RE/MAX Associati Real Estate · Milan, Viale Gran Sasso 31"),
    ("La consulenza iniziale non costituisce obbligo di conferimento incarico.",
     "La consultation initiale ne crée aucune obligation de mandat."),
    ("Azioni rapide", "Actions rapides"),
    ("Trattativa e rogito", "Négociation et acte notarié"),
    ("Eventuale vendita guidata", "Vente accompagnée le cas échéant"),
    ("Ricevi l'analisi del tuo immobile", "Recevez l'analyse de votre bien"),
    ("Ricevi l'analisi del tuo immobile", "Recevez l'analyse de votre bien"),
    ("Analisi immobiliare riservata", "Analyse immobilière confidentielle"),
    ("Strategia e posizionamento", "Stratégie et positionnement"),
    ("Primo confronto", "Premier échange"),
    ("Metodo chiaro", "Méthode claire"),
    ("Nessun obbligo dopo l'analisi", "Aucune obligation après l'analyse"),
    ("Nessun obbligo dopo l'analisi", "Aucune obligation après l'analyse"),
    ("Valore di mercato reale", "Valeur marchande réelle"),
    ("Criterio", "Critère"),
    ("Stima online", "Estimation en ligne"),
    ("Analisi RE/MAX", "Analyse RE/MAX"),
]

META_DE = {
    "milano": {
        "title": "Immobilienberater Mailand | Immobilienbewertung · Piraino",
        "desc": "Möchten Sie in Mailand verkaufen? Vertrauliche Immobilienanalyse auf realen Daten und Mikrozonen-Basis — bevor wir über ein Mandat sprechen. Zuerst die Analyse, dann der Verkauf.",
        "og_title": "RE/MAX-Immobilienberater Mailand | Immobilienbewertung",
        "og_desc": "Möchten Sie in Mailand verkaufen? Erhalten Sie eine vertrauliche Analyse auf realen Daten, Mikrozonen und Verkaufsstrategie.",
    },
}
META_FR = {
    "milano": {
        "title": "Agent immobilier Milan | Estimation immobilière · Piraino",
        "desc": "Vous souhaitez vendre à Milan ? Analyse immobilière confidentielle sur données réelles et micro-zone — avant tout mandat. D'abord l'analyse, ensuite la vente.",
        "og_title": "Agent immobilier RE/MAX Milan | Estimation immobilière",
        "og_desc": "Vous souhaitez vendre à Milan ? Recevez une analyse confidentielle basée sur des données réelles, la micro-zone et une stratégie de vente.",
    },
}


_ENTITY_MAP = (
    ("À", "&Agrave;"), ("à", "&agrave;"),
    ("È", "&Egrave;"), ("è", "&egrave;"),
    ("É", "&Eacute;"), ("é", "&eacute;"),
    ("Ì", "&Igrave;"), ("ì", "&igrave;"),
    ("Ò", "&Ograve;"), ("ò", "&ograve;"),
    ("Ù", "&Ugrave;"), ("ù", "&ugrave;"),
    ("—", "&mdash;"), ("·", "&middot;"),
)

_CURVY_APOSTROPHES = (
    ("\u2019", "'"),
    ("\u2018", "'"),
)


def _to_entities(text: str) -> str:
    out = text
    for char, ent in _ENTITY_MAP:
        out = out.replace(char, ent)
    return out


def _merge_phrases(*lists: list[tuple[str, str]]) -> list[tuple[str, str]]:
    seen: set[str] = set()
    merged: list[tuple[str, str]] = []
    for phrases in lists:
        for src, dst in phrases:
            if src in seen:
                continue
            seen.add(src)
            merged.append((src, dst))
    return merged


def _text_variants(text: str) -> list[str]:
    seen: set[str] = set()
    variants = [text, _to_entities(text)]
    for cur, repl in _CURVY_APOSTROPHES:
        for base in list(variants):
            if cur in base:
                variants.append(base.replace(cur, repl))
            if repl in base:
                variants.append(base.replace(repl, cur))
    out: list[str] = []
    for v in variants:
        if v not in seen:
            seen.add(v)
            out.append(v)
    return out


def _expand_entity_variants(phrases: list[tuple[str, str]]) -> list[tuple[str, str]]:
    extra: list[tuple[str, str]] = []
    seen: set[str] = set()
    for src, dst in phrases:
        for variant_src in _text_variants(src):
            variant_dst = _to_entities(dst) if "&" in variant_src else dst
            if variant_src not in seen:
                seen.add(variant_src)
                extra.append((variant_src, variant_dst))
    return extra


def _sorted_phrases(phrases: list[tuple[str, str]]) -> list[tuple[str, str]]:
    return sorted(phrases, key=lambda p: len(p[0]), reverse=True)


def _phrases_for(lang: str) -> list[tuple[str, str]]:
    if lang == "de":
        base = _merge_phrases(PHRASES_DE, PHRASES_BERGAMO_DE, PHRASES_BRESCIA_DE)
    else:
        base = _merge_phrases(PHRASES_FR, PHRASES_BERGAMO_FR, PHRASES_BRESCIA_FR, PHRASES_FR_GAP)
    return _expand_entity_variants(base)


def _apply_phrases(html: str, phrases: list[tuple[str, str]]) -> str:
    for src, dst in _sorted_phrases(phrases):
        if src and src in html:
            html = html.replace(src, dst)
    return html


def _apply_localize(html: str, lang: str, slug: str) -> str:
    it_data = SELLER_LOCALIZE.get(slug)
    loc_data = get_localize_block(slug, lang)
    if not it_data or not loc_data:
        return html
    for key, it_val in it_data.items():
        loc_val = loc_data.get(key)
        if loc_val is None:
            continue
        if key == "testimonials" and isinstance(it_val, list) and isinstance(loc_val, list):
            for it_tup, loc_tup in zip(it_val, loc_val):
                for it_part, loc_part in zip(it_tup, loc_tup):
                    if it_part and it_part in html:
                        html = html.replace(it_part, loc_part)
        elif isinstance(it_val, str) and isinstance(loc_val, str) and it_val in html:
            html = html.replace(it_val, loc_val)
    return html


def _apply_province_templates(html: str, lang: str, slug: str) -> str:
    city_it = city_label(slug, "it")
    city = city_label(slug, lang)
    if lang == "de":
        pairs = [
            (
                f"Opero su {city_it} e provincia, con attenzione alle micro-zone e alle dinamiche locali del mercato immobiliare.",
                f"Ich arbeite in {city} und Provinz mit Fokus auf Mikrozonen und lokale Marktdynamiken.",
            ),
            (
                f"Opero su {city_it} città e provincia e, tramite RE/MAX, posso coordinarmi anche con colleghi nelle altre province lombarde se il tuo immobile o il tuo obiettivo lo richiede.",
                f"Ich arbeite in {city} und Provinz und kann über RE/MAX auch mit Kollegen in anderen Provinzen der Lombardei koordinieren, wenn Ihre Immobilie oder Ihr Ziel es erfordert.",
            ),
            (
                f"Opero su {city_it} e provincia e, tramite RE/MAX, posso coordinarmi anche con colleghi nelle altre province lombarde se il tuo immobile o il tuo obiettivo lo richiede.",
                f"Ich arbeite in {city} und Provinz und kann über RE/MAX auch mit Kollegen in anderen Provinzen der Lombardei koordinieren, wenn Ihre Immobilie oder Ihr Ziel es erfordert.",
            ),
            (
                f"Definiamo prezzo, timing, comunicazione e profilo dell'acquirente più adatto alla tua zona specifica — {city_it} e provincia.",
                f"Wir definieren Preis, Timing, Kommunikation und das passende Käuferprofil für Ihre konkrete Zone — {city} und Provinz.",
            ),
            (
                "Ogni vendita ha criticità diverse. Il primo passo è capire cosa può rallentare, svalutare o valorizzare il tuo immobile.",
                "Jeder Verkauf hat andere Herausforderungen. Der erste Schritt: verstehen, was Ihre Immobilie verzögern, entwerten oder aufwerten kann.",
            ),
            (
                "Eravamo indecisi se vendere ora o aspettare. L'analisi sui dati OMI e sulle compravendite recenti in zona ci ha dato chiarezza senza pressioni commerciali.",
                "Wir waren unsicher, ob wir jetzt verkaufen oder warten sollten. Die Analyse auf OMI-Daten und jüngsten Transaktionen in der Zone gab uns Klarheit ohne Verkaufsdruck.",
            ),
            (
                "Durante le visite è stato fondamentale avere risposte tecniche chiare su documentazione, stato dell'immobile e strategia di vendita. Questo ha reso la trattativa più fluida.",
                "Bei Besichtigungen waren klare technische Antworten zu Dokumentation, Zustand und Verkaufsstrategie entscheidend. Das machte die Verhandlung reibungsloser.",
            ),
            (
                "Prima della pubblicazione sono state individuate alcune criticità che avrebbero potuto rallentare la trattativa. Risolverle in anticipo ha migliorato la presentazione e il risultato finale.",
                "Vor der Veröffentlichung wurden Schwachstellen erkannt, die die Verhandlung verzögert hätten. Die frühzeitige Lösung verbesserte Präsentation und Endergebnis.",
            ),
            (
                "Prima della pubblicazione sono state individuate alcune criticità che avrebbero potuto rallentare la trattativa. Risolverle in anticipo ha migliorato la presentazione dell'immobile.",
                "Vor der Veröffentlichung wurden Schwachstellen erkannt, die die Verhandlung verzögert hätten. Die frühzeitige Lösung verbesserte die Präsentation der Immobilie.",
            ),
            (
                "Per trasparenza e fiducia. La consulenza resta personale, ma l'affiliazione al network RE/MAX aggiunge riconoscibilità e supporto commerciale.",
                "Aus Transparenz und Vertrauen. Die Beratung bleibt persönlich, die RE/MAX-Affiliation verleiht aber Wiedererkennung und kommerzielle Unterstützung.",
            ),
            (
                "Per trasparenza e fiducia. La consulenza resta personale, ma l'affiliazione al network RE/MAX aggiunge riconoscibilità e supporto commerciale.",
                "Aus Transparenz und Vertrauen. Die Beratung bleibt persönlich, die RE/MAX-Affiliation verleiht aber Wiedererkennung und kommerzielle Unterstützung.",
            ),
            (
                f"Lavori solo su {city_it} o anche in provincia?",
                f"Arbeiten Sie nur in {city} oder auch in der Provinz?",
            ),
            (
                f"A {city_it} ogni comune e quartiere ha dinamiche proprie che incidono in modo significativo sul valore reale.",
                f"In {city} hat jede Gemeinde und jedes Viertel eigene Dynamiken, die den realen Wert erheblich beeinflussen.",
            ),
            (
                f"Le stime automatiche non vedono stato interno, piano, affaccio, criticità documentali e domanda reale della zona. A {city_it} ogni comune e quartiere ha dinamiche proprie che incidono in modo significativo sul valore reale.",
                f"Automatische Schätzungen berücksichtigen weder Innenzustand, Etage, Ausrichtung, dokumentarische Risiken noch die reale Nachfrage. In {city} beeinflussen Gemeinde und Viertel den Wert erheblich.",
            ),
            (
                f"Mesi online, poche visite, offerte basse: spesso il problema non è la casa, ma il posizionamento sbagliato per quella zona — che a {city_it} cambia significativamente da una micro-zona all'altra.",
                f"Monate online, wenige Besichtigungen, niedrige Angebote: oft liegt es nicht an der Immobilie, sondern an der falschen Positionierung — in {city} ändert sich der Markt von Mikrozone zu Mikrozone.",
            ),
            (
                f"Dalla prima analisi alla possibile strategia di vendita: ogni fase è chiara, definita e concordata con te — ovunque si trovi il tuo immobile a {city_it} e in provincia.",
                f"Von der Erstanalyse bis zur möglichen Verkaufsstrategie: jede Phase ist klar, definiert und mit Ihnen abgestimmt — wo auch immer Ihre Immobilie in {city} und Provinz liegt.",
            ),
            (
                f"Prima di vendere casa a {city_it} o in provincia, serve capire davvero quanto vale.",
                f"Bevor Sie in {city} oder in der Provinz verkaufen, müssen Sie den realen Wert kennen.",
            ),
            (
                f"È un confronto strutturato sul tuo immobile, sulla micro-zona e sulla strategia di vendita più adatta a {city_it}.",
                f"Es ist ein strukturierter Vergleich Ihrer Immobilie, der Mikrozone und der für {city} passendsten Verkaufsstrategie.",
            ),
            (
                f"Valutazione riservata su {city_it} e provincia. Nessun obbligo di incarico.",
                f"Vertrauliche Bewertung in {city} und Provinz. Keine Verpflichtung zum Mandat.",
            ),
            (
                "Sì. Sapere oggi quanto vale il tuo immobile ti permette di pianificare senza pressione, scegliere il momento migliore e non farti trovare impreparato quando decidi di procedere.",
                "Ja. Den heutigen Wert Ihrer Immobilie zu kennen ermöglicht Planung ohne Druck, die Wahl des besten Zeitpunkts — und Sie sind vorbereitet, wenn Sie verkaufen möchten.",
            ),
            (
                f"La maggior parte degli agenti tratta tutto allo stesso modo. Io costruisco una strategia su misura per la zona specifica del tuo immobile, prima ancora di pubblicare la prima foto.",
                "Die meisten Makler behandeln alles gleich. Ich entwickle eine maßgeschneiderte Strategie für die konkrete Zone Ihrer Immobilie — noch bevor das erste Foto veröffentlicht wird.",
            ),
            (
                "Agente Immobiliare affiliato RE/MAX. Consulenza per venditori e acquirenti in Lombardia.",
                "RE/MAX-Immobilienberater. Beratung für Verkäufer und Käufer in der Lombardei.",
            ),
        ]
    else:
        pairs = [
            (
                f"Opero su {city_it} e provincia, con attenzione alle micro-zone e alle dinamiche locali del mercato immobiliare.",
                f"J'interviens à {city} et en province, en tenant compte des micro-zones et des dynamiques locales du marché.",
            ),
            (
                f"Opero su {city_it} città e provincia e, tramite RE/MAX, posso coordinarmi anche con colleghi nelle altre province lombarde se il tuo immobile o il tuo obiettivo lo richiede.",
                f"J'interviens à {city} et en province et, via RE/MAX, je peux coordonner avec des collègues dans d'autres provinces lombardes si votre bien ou votre objectif l'exige.",
            ),
            (
                f"Opero su {city_it} e provincia e, tramite RE/MAX, posso coordinarmi anche con colleghi nelle altre province lombarde se il tuo immobile o il tuo obiettivo lo richiede.",
                f"J'interviens à {city} et en province et, via RE/MAX, je peux coordonner avec des collègues dans d'autres provinces lombardes si votre bien ou votre objectif l'exige.",
            ),
            (
                f"Definiamo prezzo, timing, comunicazione e profilo dell'acquirente più adatto alla tua zona specifica — {city_it} e provincia.",
                f"Nous définissons le prix, le timing, la communication et le profil acheteur adapté à votre zone — {city} et province.",
            ),
            (
                "Ogni vendita ha criticità diverse. Il primo passo è capire cosa può rallentare, svalutare o valorizzare il tuo immobile.",
                "Chaque vente a ses propres enjeux. La première étape : comprendre ce qui peut ralentir, dévaloriser ou valoriser votre bien.",
            ),
            (
                "Eravamo indecisi se vendere ora o aspettare. L'analisi sui dati OMI e sulle compravendite recenti in zona ci ha dato chiarezza senza pressioni commerciali.",
                "Nous hésitions à vendre maintenant ou à attendre. L'analyse des données OMI et des transactions récentes dans la zone nous a éclairés sans pression commerciale.",
            ),
            (
                "Durante le visite è stato fondamentale avere risposte tecniche chiare su documentazione, stato dell'immobile e strategia di vendita. Questo ha reso la trattativa più fluida.",
                "Lors des visites, des réponses techniques claires sur la documentation, l'état du bien et la stratégie de vente ont été essentielles. La négociation s'est déroulée plus facilement.",
            ),
            (
                "Prima della pubblicazione sono state individuate alcune criticità che avrebbero potuto rallentare la trattativa. Risolverle in anticipo ha migliorato la presentazione dell'immobile.",
                "Avant la publication, des points sensibles susceptibles de ralentir la négociation ont été identifiés. Les résoudre à l'avance a amélioré la présentation du bien.",
            ),
            (
                "Prima della pubblicazione sono state individuate alcune criticità che avrebbero potuto rallentare la trattativa. Risolverle in anticipo ha migliorato la presentazione e il risultato finale.",
                "Avant la publication, des points sensibles susceptibles de ralentir la négociation ont été identifiés. Les résoudre à l'avance a amélioré la présentation et le résultat final.",
            ),
            (
                "Per trasparenza e fiducia. La consulenza resta personale, ma l'affiliazione al network RE/MAX aggiunge riconoscibilità e supporto commerciale.",
                "Par transparence et confiance. Le conseil reste personnel, mais l'affiliation au réseau RE/MAX apporte reconnaissance et soutien commercial.",
            ),
            (
                f"Lavori solo su {city_it} o anche in provincia?",
                f"Intervenez-vous uniquement à {city} ou aussi en province ?",
            ),
            (
                f"A {city_it} ogni comune e quartiere ha dinamiche proprie che incidono in modo significativo sul valore reale.",
                f"À {city}, chaque commune et quartier a ses propres dynamiques qui influencent significativement la valeur réelle.",
            ),
            (
                f"Le stime automatiche non vedono stato interno, piano, affaccio, criticità documentali e domanda reale della zona. A {city_it} ogni comune e quartiere ha dinamiche proprie che incidono in modo significativo sul valore reale.",
                f"Les estimations automatiques ne voient ni l'état intérieur, l'étage, l'exposition, les risques documentaires ni la demande réelle. À {city}, commune et quartier influencent fortement la valeur.",
            ),
            (
                f"Mesi online, poche visite, offerte basse: spesso il problema non è la casa, ma il posizionamento sbagliato per quella zona — che a {city_it} cambia significativamente da una micro-zona all'altra.",
                f"Mois en ligne, peu de visites, offres basses : souvent le problème n'est pas le bien, mais un mauvais positionnement — à {city}, le marché change nettement d'une micro-zone à l'autre.",
            ),
            (
                f"Dalla prima analisi alla possibile strategia di vendita: ogni fase è chiara, definita e concordata con te — ovunque si trovi il tuo immobile a {city_it} e in provincia.",
                f"De la première analyse à la stratégie de vente : chaque étape est claire, définie et convenue avec vous — où que se trouve votre bien à {city} et en province.",
            ),
            (
                f"Prima di vendere casa a {city_it} o in provincia, serve capire davvero quanto vale.",
                f"Avant de vendre à {city} ou en province, il faut connaître la vraie valeur.",
            ),
            (
                f"È un confronto strutturato sul tuo immobile, sulla micro-zona e sulla strategia di vendita più adatta a {city_it}.",
                f"C'est une analyse structurée de votre bien, de la micro-zone et de la stratégie de vente la plus adaptée à {city}.",
            ),
            (
                f"Valutazione riservata su {city_it} e provincia. Nessun obbligo di incarico.",
                f"Évaluation confidentielle à {city} et en province. Aucune obligation de mandat.",
            ),
            (
                "Sì. Sapere oggi quanto vale il tuo immobile ti permette di pianificare senza pressione, scegliere il momento migliore e non farti trovare impreparato quando decidi di procedere.",
                "Oui. Connaître aujourd'hui la valeur de votre bien permet de planifier sans pression, de choisir le bon moment — et d'être prêt quand vous décidez de vendre.",
            ),
            (
                f"La maggior parte degli agenti tratta tutto allo stesso modo. Io costruisco una strategia su misura per la zona specifica del tuo immobile, prima ancora di pubblicare la prima foto.",
                "La plupart des agents traitent tout de la même façon. Je construis une stratégie sur mesure pour la zone de votre bien — avant même la première photo.",
            ),
            (
                "Agente Immobiliare affiliato RE/MAX. Consulenza per venditori e acquirenti in Lombardia.",
                "Agent immobilier RE/MAX. Conseil pour vendeurs et acheteurs en Lombardie.",
            ),
        ]
    return _apply_phrases(html, _expand_entity_variants(pairs))


def _fix_wa_urls(html: str, lang: str, slug: str) -> str:
    city = city_label(slug, lang)
    if lang == "de":
        msg = f"Hallo Maurizio, ich möchte eine vertrauliche Analyse meiner Immobilie in {city} erhalten."
    else:
        msg = f"Bonjour Maurizio, je souhaite recevoir une analyse confidentielle de mon bien à {city}."
    encoded = quote(msg)
    html = re.sub(
        r'href="https://wa\.me/393514581993\?text=[^"]*"',
        f'href="https://wa.me/393514581993?text={encoded}"',
        html,
    )
    return html


def _fix_schema(html: str, lang: str) -> str:
    locale = "de-DE" if lang == "de" else "fr-FR"
    html = html.replace('"inLanguage": "it-IT"', f'"inLanguage": "{locale}"')
    html = html.replace('"inLanguage":"it-IT"', f'"inLanguage":"{locale}"')
    if lang == "de":
        html = html.replace("Lombardia", "Lombardei")
        html = html.replace("Consulenza per venditori e acquirenti in Lombardia.", "Beratung für Verkäufer und Käufer in der Lombardei.")
    else:
        html = html.replace("Consulenza per venditori e acquirenti in Lombardia.", "Conseil pour vendeurs et acheteurs en Lombardie.")
    return html


def _fix_titles(html: str, lang: str, slug: str) -> str:
    city = city_label(slug, lang)
    if lang == "de":
        title = f"Immobilienberater {city} | Immobilienbewertung &middot; Piraino"
        og_title = f"RE/MAX-Immobilienberater {city} | Immobilienbewertung"
        html = re.sub(r"<title>[^<]+</title>", f"<title>{title}</title>", html, count=1)
        html = re.sub(
            r'<meta property="og:title" content="[^"]+" */>',
            f'<meta property="og:title" content="{og_title}" />',
            html,
            count=1,
        )
        html = re.sub(
            r'<meta name="twitter:title" content="[^"]+" */>',
            f'<meta name="twitter:title" content="{og_title}" />',
            html,
            count=1,
        )
    else:
        title = f"Agent immobilier {city} | Estimation immobilière &middot; Piraino"
        og_title = f"Agent immobilier RE/MAX {city} | Estimation immobilière"
        html = re.sub(r"<title>[^<]+</title>", f"<title>{title}</title>", html, count=1)
        html = re.sub(
            r'<meta property="og:title" content="[^"]+" */>',
            f'<meta property="og:title" content="{og_title}" />',
            html,
            count=1,
        )
        html = re.sub(
            r'<meta name="twitter:title" content="[^"]+" */>',
            f'<meta name="twitter:title" content="{og_title}" />',
            html,
            count=1,
        )
    return html


def _fix_links(html: str, lang: str, slug: str) -> str:
    buy = buyer_province_url(slug, lang)
    hub = buyer_hub_url(lang)
    html = html.replace(f'href="/comprare-casa-{slug}/"', f'href="{buy}"')
    if slug == "milano":
        html = html.replace('href="/comprare-casa-milano/"', f'href="{buy}"')
        html = html.replace('href="/comprare-casa-milan/"', f'href="{buy}"')
    html = html.replace('href="/comprare-casa/"', f'href="{hub}"')
    # Dual-path buy CTA text per city
    city = city_label(slug, lang)
    if lang == "de":
        html = re.sub(
            r'Comprare a [^<]+ →',
            f"In {city} kaufen →",
            html,
        )
        html = re.sub(
            r'<span class="dual-path-cta">Comprare a [^<]+ →</span>',
            f'<span class="dual-path-cta">In {city} kaufen →</span>',
            html,
        )
    elif lang == "fr":
        html = re.sub(
            r'Comprare a [^<]+ →',
            f"Acheter à {city} →",
            html,
        )
    return html


def _fix_meta(html: str, lang: str, slug: str) -> str:
    city = city_label(slug, lang)
    canonical = f"https://mauriziopiraino.it{seller_url(slug, lang)}"
    html = re.sub(r'<html lang="[^"]+"', f'<html lang="{lang}"', html, count=1)
    html = re.sub(r'<link rel="canonical" href="[^"]+" */>', f'<link rel="canonical" href="{canonical}" />', html, count=1)
    html = re.sub(r'<meta property="og:url" content="[^"]+" */>', f'<meta property="og:url" content="{canonical}" />', html, count=1)
    html = re.sub(r'content="it_IT"', f'content="{lang}_{"DE" if lang == "de" else "FR"}"', html, count=1)
    if lang == "de":
        html = re.sub(
            r'<meta name="twitter:description" content="[^"]+" */>',
            f'<meta name="twitter:description" content="Vertrauliche Immobilienanalyse zum Verkauf in {city} — mit Methode, realen Daten und Strategie." />',
            html,
            count=1,
        )
    elif lang == "fr":
        html = re.sub(
            r'<meta name="twitter:description" content="[^"]+" */>',
            f'<meta name="twitter:description" content="Analyse immobilière confidentielle pour vendre à {city} — méthode, données réelles et stratégie." />',
            html,
            count=1,
        )

    meta_pack = (META_DE if lang == "de" else META_FR).get(slug)
    if meta_pack:
        html = re.sub(r"<title>[^<]+</title>", f"<title>{meta_pack['title']}</title>", html, count=1)
        html = re.sub(
            r'<meta name="description" content="[^"]+" */>',
            f'<meta name="description" content="{meta_pack["desc"]}" />',
            html,
            count=1,
        )
        html = re.sub(
            r'<meta property="og:title" content="[^"]+" */>',
            f'<meta property="og:title" content="{meta_pack["og_title"]}" />',
            html,
            count=1,
        )
        html = re.sub(
            r'<meta property="og:description" content="[^"]+" */>',
            f'<meta property="og:description" content="{meta_pack["og_desc"]}" />',
            html,
            count=1,
        )
    else:
        if lang == "de":
            html = re.sub(
                r'<meta name="description" content="[^"]+" */>',
                f'<meta name="description" content="Möchten Sie in {city} verkaufen? Vertrauliche Analyse auf realen Daten und Mikrozonen-Basis — bevor wir über ein Mandat sprechen." />',
                html,
                count=1,
            )
            html = re.sub(
                r'<meta property="og:description" content="[^"]+" */>',
                f'<meta property="og:description" content="Möchten Sie in {city} verkaufen? Vertrauliche Analyse auf realen Daten, Mikrozonen und Verkaufsstrategie." />',
                html,
                count=1,
            )
        else:
            html = re.sub(
                r'<meta name="description" content="[^"]+" */>',
                f'<meta name="description" content="Vous souhaitez vendre à {city} ? Analyse confidentielle sur données réelles et micro-zone — avant tout mandat." />',
                html,
                count=1,
            )
            html = re.sub(
                r'<meta property="og:description" content="[^"]+" */>',
                f'<meta property="og:description" content="Vous souhaitez vendre à {city} ? Analyse confidentielle basée sur des données réelles, la micro-zone et une stratégie de vente." />',
                html,
                count=1,
            )
    return html


def _replace_cities(html: str, lang: str) -> str:
    """Replace Italian city names with localized labels (longest first)."""
    pairs = sorted(
        ((it_name, city_label(slug, lang)) for slug, it_name, _en in LOMBARD_PROVINCES),
        key=lambda x: len(x[0]),
        reverse=True,
    )
    for it_name, loc in pairs:
        if it_name != loc:
            html = html.replace(it_name, loc)
    return html


def apply_seller_locale(html: str, lang: str, slug: str) -> str:
    phrases = _phrases_for(lang)
    html = _apply_localize(html, lang, slug)
    html = _apply_phrases(html, phrases)
    html = _apply_province_templates(html, lang, slug)
    html = apply_province_all(html, lang, slug)
    html = _replace_cities(html, lang)
    html = _apply_phrases(html, phrases)
    html = _apply_province_templates(html, lang, slug)
    html = apply_province_all(html, lang, slug)
    html = _fix_links(html, lang, slug)
    html = _fix_meta(html, lang, slug)
    html = _fix_titles(html, lang, slug)
    html = _fix_wa_urls(html, lang, slug)
    html = _fix_schema(html, lang)
    return html
