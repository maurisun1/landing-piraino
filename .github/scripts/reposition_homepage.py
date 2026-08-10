#!/usr/bin/env python3
"""Reposition mauriziopiraino.it homepage as buyer/investor consultant brand."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


# ---------------------------------------------------------------------------
# Italian content blocks
# ---------------------------------------------------------------------------

HERO_ASIDE_IT = """\
<div class="hero-agent reveal">
            <img src="foto.jpg" alt="Maurizio Piraino" width="56" height="56" decoding="async" />
            <div>
              <strong>Maurizio Piraino</strong>
              <span>Consulente per acquirenti e investitori · RE/MAX</span>
            </div>
          </div>
<div class="eyebrow">Milano · Lombardia · Consulenza immobiliare</div>
          <h1>Consulente per Acquirenti e Investitori Immobiliari</h1>
          <p>
            L'alleato di chi compra casa e di chi investe nel mercato immobiliare.
            <strong>Analisi prima dell'acquisto</strong>, ricerca personalizzata, tutela documentale e assistenza fino al rogito.
          </p>
          <ul class="seller-form-benefits">
            <li>Property Finding: ricerca anche off-market</li>
            <li>Consulenza dedicata per investitori</li>
            <li>Verifica documentale e negoziazione</li>
            <li>Affiancamento fino al rogito — nessun obbligo iniziale</li>
          </ul>
          <a class="btn btn-wa seller-form-wa" href="https://wa.me/393514581993?text=Ciao%20Maurizio%2C%20vorrei%20una%20consulenza.%20Sto%20cercando%20casa%20%2F%20un%20investimento%20immobiliare."><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg> Raccontami cosa stai cercando</a>
"""

FORM_HEAD_IT = """\
          <h2>Prenota una consulenza riservata</h2>
          <p>Non basta sfogliare annunci. Raccontami il tuo obiettivo — cerco casa, investimento o vendita — e prepariamo insieme il percorso giusto.</p>
          <div class="divider"></div>
          <input type="hidden" name="landing" value="Homepage Consulente Acquirenti Investitori" />
          <input type="hidden" name="intento" id="intentoVal" value="Cerco casa" />

          <div class="form-progress" aria-label="Avanzamento form">
            <div class="fp-dot active" id="fp1">1</div>
            <div class="fp-line" id="fpl"></div>
            <div class="fp-dot" id="fp2">2</div>
          </div>

          <!-- STEP 1: obiettivo -->
          <div class="form-step active" id="formStep1">
            <p class="step-note">Prima di tutto: cosa ti serve?</p>
            <label>Il tuo obiettivo</label>
            <div class="intent-grid" role="group" aria-label="Tipo di richiesta">
              <div class="intent-card on" data-v="Cerco casa" onclick="setIntent(this)">Cerco casa</div>
              <div class="intent-card" data-v="Investimento" onclick="setIntent(this)">Investimento</div>
              <div class="intent-card" data-v="Vendo" onclick="setIntent(this)">Vendo</div>
            </div>

            <label for="zona">Zona o comune di interesse</label>
"""

FORM_SUBMIT_IT = 'Richiedi la mia analisi'
FORM_SUBMIT_NEW_IT = 'Prenota la consulenza'

PATH_IT = """\
    <section class="consultant-path" aria-label="Scegli il tuo percorso">
      <div class="container consultant-path-grid">
        <p class="consultant-path-intro"><em>RE/MAX</em> · Come posso aiutarti</p>
        <a class="consultant-path-card consultant-path-primary" href="/comprare-casa/">
          <span class="consultant-path-label">01 · Servizio principale</span>
          <strong>Property Finding</strong>
          <p>Ricerca personalizzata dell'immobile ideale, anche off-market. Selezione, visite, negoziazione e coordinamento fino al rogito.</p>
          <span class="consultant-path-cta">Iniziamo la ricerca →</span>
        </a>
        <a class="consultant-path-card consultant-path-invest" href="#servizi">
          <span class="consultant-path-label">02 · Investitori</span>
          <strong>Consulenza per investitori</strong>
          <p>Opportunità a reddito, valorizzazione, analisi economica e stima della redditività — con supporto in trattativa.</p>
          <span class="consultant-path-cta">Analizziamo il tuo investimento →</span>
        </a>
        <a class="consultant-path-card consultant-path-sell" href="/vendere-casa-milano/">
          <span class="consultant-path-label">03 · Venditori</span>
          <strong>Valutazione e vendita</strong>
          <p>Presente ma non predominante: valutazione, strategia e commercializzazione se stai vendendo.</p>
          <span class="consultant-path-cta">Richiedi analisi →</span>
        </a>
      </div>
    </section>
"""

SERVICES_IT = """\
    <section class="seller-services consultant-services" id="servizi">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Servizi professionali</div>
          <h2>Non vendo annunci. Ti aiuto a decidere meglio.</h2>
          <p>Il sito non deve dare la sensazione di “vendere immobili”, ma di tutela dell'acquirente e dell'investitore — dalla ricerca al rogito.</p>
        </div>
        <div class="seller-services-grid">
          <article class="seller-service-card featured reveal">
            <div class="seller-service-num">01</div>
            <h3>Property Finding</h3>
            <p>Il servizio principale: ricerca personalizzata dell'immobile ideale.</p>
            <ul class="service-list">
              <li>Analisi delle esigenze</li>
              <li>Ricerca anche off-market</li>
              <li>Selezione degli immobili e organizzazione visite</li>
              <li>Negoziazione del prezzo</li>
              <li>Coordinamento fino al rogito</li>
            </ul>
          </article>
          <article class="seller-service-card reveal">
            <div class="seller-service-num">02</div>
            <h3>Consulenza per investitori</h3>
            <p>Opportunità, reddito e valorizzazione con numeri chiari.</p>
            <ul class="service-list">
              <li>Ricerca di opportunità e immobili a reddito</li>
              <li>Operazioni di valorizzazione</li>
              <li>Analisi economica e stima della redditività</li>
              <li>Supporto in trattativa fino all'acquisto</li>
            </ul>
          </article>
          <article class="seller-service-card reveal">
            <div class="seller-service-num">03</div>
            <h3>Consulenza per chi compra casa</h3>
            <p>Percorso dedicato a prima casa o cambio abitazione.</p>
            <ul class="service-list">
              <li>Analisi delle esigenze e verifica documentazione</li>
              <li>Supporto nella trattativa</li>
              <li>Coordinamento con banca, notaio e tecnici</li>
            </ul>
          </article>
          <article class="seller-service-card secondary reveal">
            <div class="seller-service-num">04</div>
            <h3>Servizi per i venditori</h3>
            <p>Sezione presente ma non predominante.</p>
            <ul class="service-list">
              <li>Valutazione dell'immobile</li>
              <li>Strategia di vendita e valorizzazione</li>
              <li>Commercializzazione RE/MAX</li>
            </ul>
          </article>
        </div>
      </div>
    </section>
"""

INCLUDES_IT = """\
    <section class="seller-includes" id="tutela">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Cosa ottieni</div>
          <h2>Tutela dell'acquirente lungo tutto il percorso.</h2>
          <p>Analisi prima dell'acquisto, ricerca personalizzata, negoziazione e verifica documentale — non improvvisazione da portale.</p>
        </div>
        <div class="seller-includes-grid">
          <article class="seller-include-card reveal"><span class="seller-include-icon">01</span><h3>Analisi delle esigenze</h3><p>Obiettivi, budget, tempistiche e stile di vita: partiamo da te, non da un elenco di annunci.</p></article>
          <article class="seller-include-card reveal"><span class="seller-include-icon">02</span><h3>Ricerca anche off-market</h3><p>Selezione mirata tramite rete RE/MAX, colleghi e canali non pubblici — oltre i portali.</p></article>
          <article class="seller-include-card reveal"><span class="seller-include-icon">03</span><h3>Verifica documentale</h3><p>Conformità, titoli, criticità tecniche: ciò che può fermare un rogito va visto prima dell'offerta.</p></article>
          <article class="seller-include-card reveal"><span class="seller-include-icon">04</span><h3>Negoziazione</h3><p>Posizione di forza sul prezzo, sui tempi e sulle condizioni — con metodo, non con l'emozione.</p></article>
          <article class="seller-include-card reveal"><span class="seller-include-icon">05</span><h3>Analisi per investitori</h3><p>Redditività, valorizzazione e rischio: numeri chiari prima di impegnare capitale.</p></article>
          <article class="seller-include-card reveal"><span class="seller-include-icon">06</span><h3>Fino al rogito</h3><p>Coordinamento con banca, notaio e tecnici fino al passaggio definitivo.</p></article>
        </div>
      </div>
    </section>
"""

COMPARE_IT = """\
    <section class="seller-compare">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Perché un consulente</div>
          <h2>Portale annunci vs consulenza dedicata.</h2>
          <p>Sfogliare annunci non tutela il tuo interesse. Serve qualcuno che ti accompagni nelle scelte, non che ti spinga a comprare.</p>
        </div>
        <div class="seller-compare-table reveal">
          <div class="seller-compare-row seller-compare-head">
            <span>Aspetto</span><span>Fai da te / portale</span><span>Consulenza Piraino</span>
          </div>
          <div class="seller-compare-row"><span>Ricerca</span><span class="no">Solo annunci pubblici</span><span class="yes">Anche off-market</span></div>
          <div class="seller-compare-row"><span>Selezione</span><span class="no">Troppi annunci</span><span class="yes">Filtro su misura</span></div>
          <div class="seller-compare-row"><span>Documenti</span><span class="no">A tuo rischio</span><span class="yes">Verifica tecnica</span></div>
          <div class="seller-compare-row"><span>Prezzo</span><span class="no">Emotività</span><span class="yes">Negoziazione strutturata</span></div>
          <div class="seller-compare-row"><span>Ruolo</span><span class="no">Sei solo</span><span class="yes">Tutela acquirente / investitore</span></div>
        </div>
      </div>
    </section>
"""

MID_CTA_IT = """\
    <section class="seller-mid-cta">
      <div class="container reveal">
        <div class="seller-mid-cta-inner">
          <div>
            <p class="seller-mid-kicker">RE/MAX · Consulenza</p>
            <h2>Cerchiamo insieme l'immobile giusto.</h2>
            <p>Raccontami cosa stai cercando — casa o investimento. Risposta personale entro 24 ore, senza obbligo.</p>
          </div>
          <div class="seller-mid-actions">
            <a class="btn btn-red" href="#form">Prenota una consulenza</a>
            <a class="btn btn-light" href="/comprare-casa/">Scegli la provincia →</a>
          </div>
        </div>
      </div>
    </section>
"""

SITUATIONS_IT = """\
    <section class="situations">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">Questo servizio è per te se</div>
          <h2>Decidi meglio. Compra meglio. Investi meglio.</h2>
          <p>Il messaggio è tutela e metodo — non “compra subito” né “sfoglia gli annunci”.</p>
        </div>
        <div class="situations-grid">
          <article class="card reveal"><div class="num">01</div><h3>Cerchi casa in Lombardia</h3><p>Vuoi una ricerca personalizzata, non perdere tempo tra centinaia di annunci poco adatti.</p></article>
          <article class="card reveal"><div class="num">02</div><h3>Investi nel mattone</h3><p>Ti servono analisi di redditività, rischio e opportunità — prima di impegnare capitale.</p></article>
          <article class="card reveal"><div class="num">03</div><h3>Hai paura di pagare troppo</h3><p>Vuoi dati reali, verifica documentale e una negoziazione costruita sui tuoi interessi.</p></article>
          <article class="card reveal"><div class="num">04</div><h3>Stai vendendo (secondo piano)</h3><p>Anche per i venditori: valutazione e strategia — senza farne il messaggio dominante del sito.</p></article>
        </div>
      </div>
    </section>
"""

ABOUT_IT = """\
          <div class="section-kicker">Il mio approccio</div>
          <h2>Prima l'analisi. Poi la decisione giusta.</h2>
                    <p class="lead">Opero come consulente immobiliare con RE/MAX Associati Real Estate a Milano. Il personal brand è questo: tutela di acquirenti e investitori, con background tecnico e metodo strutturato — non la logica del portale immobiliare.</p>
<p class="lead">Sono un Agente Immobiliare affiliato RE/MAX con esperienza da geometra e imprenditore. Questo significa leggere un immobile in modo diverso: criticità, potenzialità, numeri e trattativa — dalla ricerca al rogito.</p>
          <div class="quote">“Non ti accompagno a comprare un annuncio. Ti aiuto a prendere la decisione immobiliare migliore.”</div>
          <p class="lead">ValoreCasaTua.it genera contenuti e autorevolezza. Qui, su MaurizioPiraino.it, convertiamo quella consapevolezza in consulenza concreta.</p>
          <div class="method-grid">
            <div class="card"><div class="num">1</div><h3>Ascolto e analisi</h3><p>Esigenze, budget, obiettivo abitativo o di investimento: partiamo da dati e priorità.</p></div>
            <div class="card"><div class="num">2</div><h3>Ricerca e selezione</h3><p>Property finding su misura, anche off-market, con filtri chiari e visite organizzate.</p></div>
            <div class="card"><div class="num">3</div><h3>Tutela fino al rogito</h3><p>Documenti, negoziazione, banca e notaio: un percorso guidato senza improvvisazione.</p></div>
          </div>
"""

NETWORK_IT = """\
          <div class="section-kicker">Affiliazione RE/MAX</div>
          <h2>Consulenza indipendente nel metodo, network internazionale nei fatti.</h2>
          <p>La consulenza resta personale e diretta. L'affiliazione RE/MAX aggiunge rete MLS, collaborazione e visibilità — utili soprattutto in fase di ricerca e trattativa per l'acquirente.</p>
        </div>
        <div class="network-grid">
          <div class="network-card reveal"><span>Tutela</span><strong>Acquirente</strong><p>Il punto di vista è il tuo: prezzo giusto, documenti in ordine, decisione consapevole.</p></div>
          <div class="network-card reveal"><span>Rete</span><strong>MLS</strong><p>Accesso a opportunità e collaborazioni tra professionisti — anche oltre i portali pubblici.</p></div>
          <div class="network-card reveal"><span>Metodo</span><strong>Strategia</strong><p>Property finding, analisi per investitori e affiancamento fino al rogito.</p></div>
        </div>
"""

MARKET_IT = """\
          <div class="section-kicker">Mercato Lombardia</div>
          <h2>Milano e 12 province: ogni micro-zona ha regole proprie.</h2>
          <p>Comprare o investire senza leggere la zona e i documenti è il modo più rapido di sbagliare. Ogni analisi parte dal contesto reale.</p>
        </div>
        <div class="market-grid">
          <div class="market-card reveal"><span>Acquisto</span><strong>Casa</strong><p>Prima casa o cambio abitazione: esigenze, budget e percorso guidato fino al rogito.</p></div>
          <div class="market-card reveal"><span>Capitale</span><strong>Investimento</strong><p>Redditività, valorizzazione e rischio — con numeri prima dell'emozione.</p></div>
          <div class="market-card reveal"><span>Tutela</span><strong>Due diligence</strong><p>Verifica documentale e tecnica: ciò che un notaio o una banca faranno emergere.</p></div>
        </div>
"""

STEPS_IT = """\
          <div class="section-kicker">Come funziona</div>
          <h2>Tre passi. Nessuna sorpresa.</h2>
          <p>Dalla prima consulenza al possibile acquisto: ogni fase è chiara, definita e concordata con te.</p>
        </div>
        <div class="steps-grid">
          <article class="card reveal"><div class="num">01</div><h3>Consulenza iniziale</h3><p>Ascolto l'obiettivo — casa o investimento — e definiamo budget, zone e criteri di ricerca.</p><span class="step-time">Primo confronto</span></article>
          <article class="card reveal"><div class="num">02</div><h3>Ricerca e verifica</h3><p>Property finding, selezione, visite e controllo documentale prima di qualsiasi offerta.</p><span class="step-time">Metodo chiaro</span></article>
          <article class="card reveal"><div class="num">03</div><h3>Negoziazione e rogito</h3><p>Trattativa, coordinamento con banca, notaio e tecnici fino al passaggio di proprietà.</p><span class="step-time">Nessun obbligo dopo il primo incontro</span></article>
        </div>
"""

TESTIMONIALS_IT = """\
          <div class="section-kicker">Esperienze</div>
          <h2>Situazioni reali: acquirenti, investitori e anche venditori.</h2>
        </div>
        <div class="testimonial-grid">
          <article class="testimonial-card reveal"><div class="stars">★★★★★</div><p>Cercavo casa a Milano da mesi tra troppi annunci. La ricerca filtrata e il controllo documentale prima dell'offerta mi hanno fatto risparmiare tempo e errori costosi.</p><div class="person"><div class="avatar">EL</div><div><strong>Acquirente · Porta Romana</strong><span>Prima casa · Milano</span></div></div></article>
          <article class="testimonial-card reveal"><div class="stars">★★★★★</div><p>Per l'investimento volevo numeri chiari su rendimento e rischi. Analisi sobria, niente pressure commerciale: abbiamo selezionato e chiuso con consapevolezza.</p><div class="person"><div class="avatar">MR</div><div><strong>Investitore · Navigli</strong><span>Immobile a reddito · Milano</span></div></div></article>
          <article class="testimonial-card reveal"><div class="stars">★★★★★</div><p>Durante le visite è stato fondamentale avere risposte tecniche chiare su documentazione e criticità. Questo ha reso la trattativa più fluida e sicura.</p><div class="person"><div class="avatar">SF</div><div><strong>Acquirente · Isola</strong><span>Cambio casa · Milano</span></div></div></article>
        <article class="testimonial-card reveal"><div class="stars">★★★★★</div><p>Anche in vendita: l'analisi OMI e il posizionamento corretto ci hanno dato chiarezza senza pressioni. Utile sapere di poter contare sullo stesso metodo dall'altra parte.</p><div class="person"><div class="avatar">AC</div><div><strong>Proprietari · CityLife</strong><span>Vendita · Milano</span></div></div></article>
        </div>
"""

FAQ_IT = """\
        <div class="faq-grid">
          <details open><summary>Sei un agente immobiliare o un consulente per acquirenti?</summary><p>Sono un Agente Immobiliare affiliato RE/MAX. Il posizionamento di questo sito è consulenziale: tutela di acquirenti e investitori — ricerca, analisi, negoziazione e assistenza fino al rogito. I venditori restano seguiti, ma non sono il messaggio dominante.</p></details>
          <details><summary>Cos'è il Property Finding?</summary><p>È la ricerca personalizzata dell'immobile ideale: analisi delle esigenze, selezione (anche off-market), visite, negoziazione e coordinamento fino al rogito.</p></details>
          <details><summary>Aiuti anche chi investe?</summary><p>Sì. Opportunità a reddito, valorizzazione, analisi economica e stima della redditività, con supporto in trattativa fino all'acquisto.</p></details>
          <details><summary>La prima consulenza crea obblighi?</summary><p>No. Il primo confronto serve a capire se ha senso lavorare insieme. Nessun mandato automatico.</p></details>
          <details><summary>Cosa c'entra ValoreCasaTua.it?</summary><p>ValoreCasaTua.it è il portale editoriale: guide e autorevolezza. MaurizioPiraino.it è il sito personale dedicato ai servizi professionali e alla conversione in consulenza.</p></details>
          <details><summary>Lavori solo a Milano?</summary><p>Opero su Milano e, tramite rete RE/MAX, su tutto il territorio lombardo — 12 province — in base all'obiettivo di acquisto o investimento.</p></details>
          <details><summary>E se devo vendere?</summary><p>Puoi richiedere valutazione e strategia di vendita. È un servizio presente, ma il focus del brand resta su acquirenti e investitori.</p></details>
        </div>
"""

FINAL_IT = """\
    <section class="final-cta">
      <div class="container reveal">
        <h2>Prenota una consulenza. Cerchiamo insieme l'immobile giusto.</h2>
        <p>Raccontami cosa stai cercando — casa o investimento. Analisi, ricerca e tutela fino al rogito, senza improvvisazione da portale.</p>
        <div class="hero-actions" style="justify-content:center">
          <a class="btn btn-red" href="#form">Prenota una consulenza</a>
          <a class="btn btn-wa" href="https://wa.me/393514581993?text=Ciao%20Maurizio%2C%20vorrei%20una%20consulenza.%20Sto%20cercando%20casa%20%2F%20un%20investimento%20immobiliare."><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg> Contattami su WhatsApp</a>
        </div>
      </div>
    </section>
"""

EDITORIAL_IT = """\
    <section class="editorial-bridge" aria-label="ValoreCasaTua">
      <div class="container">
        <div class="editorial-bridge-inner reveal">
          <div>
            <div class="section-kicker">Editoriale</div>
            <h2>ValoreCasaTua.it informa. Qui trasformiamo l'informazione in consulenza.</h2>
            <p>Guide, prezzi e approfondimenti restano sul portale editoriale. Su MaurizioPiraino.it trovi il percorso professionale: property finding, investitori e tutela fino al rogito.</p>
          </div>
          <div class="editorial-bridge-actions">
            <a class="btn btn-red" href="#form">Prenota una consulenza</a>
            <a class="btn btn-outline-dark" href="https://valorecasatua.it/" rel="noopener" target="_blank">Vai su ValoreCasaTua.it →</a>
          </div>
        </div>
      </div>
    </section>
"""

STATS_IT = """\
    <section class="seller-stats-strip" aria-label="Numeri chiave">
      <div class="container seller-stats-grid">
        <div class="seller-stat"><strong>01</strong><span>Property Finding come priorità</span></div>
        <div class="seller-stat"><strong>12</strong><span>Province lombarde coperte</span></div>
        <div class="seller-stat"><strong>24h</strong><span>Risposta alla consulenza</span></div>
        <div class="seller-stat"><strong>0 €</strong><span>Primo confronto · nessun obbligo</span></div>
      </div>
    </section>
"""


def replace_between(html: str, start: str, end: str, new: str, inclusive_end: bool = False) -> str:
    i = html.find(start)
    j = html.find(end, i + len(start) if i >= 0 else 0)
    if i < 0 or j < 0:
        return html
    if inclusive_end:
        j = j + len(end)
    return html[:i] + new + html[j:]


def patch_meta(html: str) -> str:
    html = html.replace(
        "<title>Agente Immobiliare Milano | Valutazione Casa &middot; Piraino</title>",
        "<title>Consulente Acquirenti e Investitori Immobiliari | Maurizio Piraino</title>",
    )
    html = re.sub(
        r'<meta name="description" content="[^"]*" />',
        '<meta name="description" content="Consulente per acquirenti e investitori immobiliari a Milano e in Lombardia. Property finding, analisi, negoziazione e assistenza fino al rogito." />',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="keywords" content="[^"]*" />',
        '<meta name="keywords" content="consulente immobiliare Milano, property finding Milano, consulenza acquirenti, investitori immobiliari Lombardia, RE/MAX Milano, Maurizio Piraino" />',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:title" content="[^"]*" />',
        '<meta property="og:title" content="Consulente per Acquirenti e Investitori Immobiliari | Piraino" />',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:description" content="[^"]*" />',
        '<meta property="og:description" content="L\'alleato di chi compra casa e di chi investe. Property finding, tutela documentale e assistenza fino al rogito." />',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="twitter:title" content="[^"]*" />',
        '<meta name="twitter:title" content="Consulente Acquirenti e Investitori | Piraino" />',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="twitter:description" content="[^"]*" />',
        '<meta name="twitter:description" content="Property finding e consulenza per acquirenti e investitori in Lombardia." />',
        html,
        count=1,
    )
    html = html.replace(
        '"description": "Agente Immobiliare affiliato RE/MAX. Consulenza per venditori e acquirenti in Lombardia."',
        '"description": "Consulente per acquirenti e investitori immobiliari. Property finding, analisi e assistenza fino al rogito in Lombardia."',
    )
    # FAQ schema
    faq_schema = """  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Sei un agente immobiliare o un consulente per acquirenti?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Sono un Agente Immobiliare affiliato RE/MAX. Il posizionamento del sito è consulenziale: tutela di acquirenti e investitori — ricerca, analisi, negoziazione e assistenza fino al rogito."
        }
      },
      {
        "@type": "Question",
        "name": "Cos'è il Property Finding?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "È la ricerca personalizzata dell'immobile ideale: analisi delle esigenze, selezione anche off-market, visite, negoziazione e coordinamento fino al rogito."
        }
      },
      {
        "@type": "Question",
        "name": "Aiuti anche chi investe?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Sì. Opportunità a reddito, valorizzazione, analisi economica e stima della redditività, con supporto in trattativa fino all'acquisto."
        }
      },
      {
        "@type": "Question",
        "name": "La prima consulenza crea obblighi?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. Il primo confronto serve a capire se ha senso lavorare insieme. Nessun mandato automatico."
        }
      }
    ]
  }
  </script>"""
    html = re.sub(
        r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "FAQPage".*?</script>',
        faq_schema,
        html,
        count=1,
        flags=re.DOTALL,
    )
    return html


def patch_css_link(html: str) -> str:
    if "consultant-home.css" in html:
        return html
    return html.replace(
        '<link rel="stylesheet" href="/assets/dual-path.css?v=20260735" />',
        '<link rel="stylesheet" href="/assets/dual-path.css?v=20260735" />\n'
        '  <link rel="stylesheet" href="/assets/consultant-home.css?v=20260715" />',
    )


def patch_nav(html: str) -> str:
    html = html.replace(
        '<a href="/" class="nav-link-primary">Vendere</a>\n              <a href="/comprare-casa/">Comprare</a>',
        '<a href="/comprare-casa/" class="nav-link-primary">Comprare</a>\n              <a href="#servizi">Investire</a>\n              <a href="/vendere-casa-milano/">Vendere</a>',
    )
    html = html.replace(
        '<a class="btn btn-red nav-cta" href="#contatto">Richiedi Analisi</a>',
        '<a class="btn btn-red nav-cta" href="#contatto">Prenota consulenza</a>',
    )
    html = html.replace(
        "vorrei%20ricevere%20un'analisi%20riservata%20del%20mio%20immobile%20a%20Milano.",
        "vorrei%20una%20consulenza.%20Sto%20cercando%20casa%20%2F%20un%20investimento%20immobiliare.",
    )
    return html


def patch_hero(html: str) -> str:
    # Replace hero aside content from hero-agent through wa button
    pattern = re.compile(
        r'<div class="hero-agent reveal">.*?</a>\n          </div>\n        <aside class="hero-form-wrap',
        re.DOTALL,
    )
    repl = HERO_ASIDE_IT.rstrip() + "\n          </div>\n        <aside class=\"hero-form-wrap"
    html2, n = pattern.subn(repl, html, count=1)
    if n != 1:
        print("  warn: hero aside replace failed")
        return html
    return html2


def patch_form_head(html: str) -> str:
    pattern = re.compile(
        r'<h2>Ricevi una consulenza immobiliare riservata</h2>.*?<label for="zona">Zona o comune dell\'immobile</label>',
        re.DOTALL,
    )
    html2, n = pattern.subn(FORM_HEAD_IT.rstrip() + "\n", html, count=1)
    if n != 1:
        print("  warn: form head replace failed")
        return html
    html2 = html2.replace(
        'placeholder="Scrivi quartiere o comune (es. Brera, Sesto San Giovanni...)"',
        'placeholder="Dove cerchi / investi / vendi (es. Brera, Como, Monza...)"',
    )
    html2 = html2.replace(
        "Due informazioni sull’immobile, per preparare un’analisi più precisa.",
        "Zone e tipologia, per preparare una consulenza più precisa.",
    )
    html2 = html2.replace(FORM_SUBMIT_IT, FORM_SUBMIT_NEW_IT)
    html2 = html2.replace(
        'placeholder="Es. piano, stato dell’immobile, box o giardino"',
        'placeholder="Es. budget, tempistiche, requisiti o note sull\'immobile"',
    )
    return html2


def patch_sections(html: str) -> str:
    # dual-path → consultant path
    html = re.sub(
        r'<section class="dual-path".*?</section>\s*',
        PATH_IT + "\n",
        html,
        count=1,
        flags=re.DOTALL,
    )
    # stats
    html = re.sub(
        r'<section class="seller-stats-strip".*?</section>\s*',
        STATS_IT + "\n",
        html,
        count=1,
        flags=re.DOTALL,
    )
    # includes
    html = re.sub(
        r'<section class="seller-includes".*?</section>\s*',
        INCLUDES_IT + "\n",
        html,
        count=1,
        flags=re.DOTALL,
    )
    # compare
    html = re.sub(
        r'<section class="seller-compare".*?</section>\s*',
        COMPARE_IT + "\n",
        html,
        count=1,
        flags=re.DOTALL,
    )
    # keep zones but soften copy
    html = html.replace(
        "<h2>Conosco il mercato locale, strada per strada.</h2>\n          <p>Milano cambia quartiere per quartiere. Un appartamento a Porta Romana non segue le stesse dinamiche di Lambrate, Isola o Navigli.</p>",
        "<h2>Lombardia e Milano: micro-zone che decidono il successo dell'acquisto.</h2>\n          <p>Comprare o investire senza conoscere quartiere, domanda e documenti è il rischio più alto. Lavoriamo zona per zona.</p>",
    )
    html = html.replace(
        '<div class="section-kicker">Zone servite · Milano</div>',
        '<div class="section-kicker">Aree di lavoro · Milano e Lombardia</div>',
    )
    # services
    html = re.sub(
        r'<section class="seller-services".*?</section>\s*',
        SERVICES_IT + "\n",
        html,
        count=1,
        flags=re.DOTALL,
    )
    # mid cta
    html = re.sub(
        r'<section class="seller-mid-cta".*?</section>\s*',
        MID_CTA_IT + "\n",
        html,
        count=1,
        flags=re.DOTALL,
    )
    # situations
    html = re.sub(
        r'<section class="situations".*?</section>\s*',
        SITUATIONS_IT + "\n",
        html,
        count=1,
        flags=re.DOTALL,
    )
    # about body
    html = re.sub(
        r'<div class="section-kicker">Il mio approccio</div>.*?</div>\n        </div>\n      </div>\n    </section>\n    <section class="network"',
        ABOUT_IT + "\n        </div>\n      </div>\n    </section>\n    <section class=\"network\"",
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = html.replace(
        'alt="Maurizio Piraino Agente Immobiliare affiliato RE/MAX Milano"',
        'alt="Maurizio Piraino — Consulente per acquirenti e investitori RE/MAX Milano"',
    )
    html = html.replace(
        "<span>Agente Immobiliare affiliato RE/MAX · Milano</span>",
        "<span>Consulente acquirenti e investitori · RE/MAX Milano</span>",
    )
    # network
    html = re.sub(
        r'<div class="section-kicker">Affiliazione RE/MAX</div>.*?</div>\n      </div>\n    </section>\n    <section class="market"',
        NETWORK_IT + "\n      </div>\n    </section>\n    <section class=\"market\"",
        html,
        count=1,
        flags=re.DOTALL,
    )
    # market
    html = re.sub(
        r'<div class="section-kicker">Mercato Milano</div>.*?</div>\n        <p style="margin-top:28px',
        MARKET_IT + '\n        <p style="margin-top:28px',
        html,
        count=1,
        flags=re.DOTALL,
    )
    # steps
    html = re.sub(
        r'<div class="section-kicker">Come funziona</div>.*?</div>\n      </div>\n    </section>\n    <section class="testimonials"',
        STEPS_IT + "\n      </div>\n    </section>\n    <section class=\"testimonials\"",
        html,
        count=1,
        flags=re.DOTALL,
    )
    # testimonials
    html = re.sub(
        r'<div class="section-kicker">Esperienze</div>.*?</div>\n      </div>\n    </section>\n    <section class="faq"',
        TESTIMONIALS_IT + "\n      </div>\n    </section>\n    <section class=\"faq\"",
        html,
        count=1,
        flags=re.DOTALL,
    )
    # faq
    html = re.sub(
        r'<div class="faq-grid">.*?</div>\n      </div>\n    </section>\n    <section class="final-cta"',
        FAQ_IT + "\n      </div>\n    </section>\n" + EDITORIAL_IT + "\n    <section class=\"final-cta\"",
        html,
        count=1,
        flags=re.DOTALL,
    )
    # final
    html = re.sub(
        r'<section class="final-cta".*?</section>\s*',
        FINAL_IT + "\n",
        html,
        count=1,
        flags=re.DOTALL,
    )
    # footer
    html = html.replace(
        "<strong>Prima l’analisi. Poi la vendita.</strong>",
        "<strong>Prima l'analisi. Poi la decisione giusta.</strong>",
    )
    html = html.replace(
        "Maurizio Piraino — Consulente immobiliare presso RE/MAX Associati Real Estate · Milano, Viale Gran Sasso 31",
        "Maurizio Piraino — Consulente per acquirenti e investitori presso RE/MAX Associati Real Estate · Milano, Viale Gran Sasso 31",
    )
    if "valorecasatua.it" not in html.lower():
        html = html.replace(
            '<p class="footer-geo-row"><a href="/privacy/">Privacy</a></p>',
            '<p class="footer-geo-row"><span class="footer-geo-label">Editoriale:</span> <a href="https://valorecasatua.it/" rel="noopener" target="_blank"><strong>ValoreCasaTua.it</strong></a> · contenuti e guide</p>\n'
            '      <p class="footer-geo-row"><a href="/privacy/">Privacy</a></p>',
        )
    # sticky
    html = html.replace(
        '<a class="btn btn-red" href="#form">Richiedi analisi</a>',
        '<a class="btn btn-red" href="#form">Prenota consulenza</a>',
    )
    return html


def patch_js_intent(html: str) -> str:
    if "function setIntent" in html:
        return html
    snippet = """
    function setIntent(el){
      document.querySelectorAll('.intent-card').forEach(c => c.classList.remove('on'));
      el.classList.add('on');
      document.getElementById('intentoVal').value = el.getAttribute('data-v');
    }
"""
    return html.replace(
        "    function onMqChange(val){",
        snippet + "\n    function onMqChange(val){",
    )


def patch_h1_css(html: str) -> str:
    # hero used h2 before; ensure h1 in hero looks right — CSS already styles h1
    return html


def reposition_it() -> None:
    path = ROOT / "index.html"
    html = path.read_text(encoding="utf-8")
    html = patch_meta(html)
    html = patch_css_link(html)
    html = patch_nav(html)
    html = patch_hero(html)
    html = patch_form_head(html)
    html = patch_sections(html)
    html = patch_js_intent(html)
    html = patch_h1_css(html)
    path.write_text(html, encoding="utf-8")
    print(f"  wrote {path.relative_to(ROOT)}")


# ---------------------------------------------------------------------------
# DE / FR lightweight hero + key section mirrors (seller pages stay seller-led;
# only Milano locale homepages get consultant positioning)
# ---------------------------------------------------------------------------

DE = {
    "title": "Berater für Immobilienkäufer und Investoren | Maurizio Piraino",
    "desc": "Berater für Immobilienkäufer und Investoren in Mailand und der Lombardei. Property Finding, Analyse, Verhandlung und Begleitung bis zum Notartermin.",
    "eyebrow": "Mailand · Lombardei · Immobilienberatung",
    "h1": "Berater für Immobilienkäufer und Investoren",
    "lead": "Der Partner für alle, die ein Haus kaufen oder in Immobilien investieren. <strong>Analyse vor dem Kauf</strong>, persönliche Suche, Dokumentenprüfung und Begleitung bis zum Notartermin.",
    "form_h2": "Vereinbaren Sie eine vertrauliche Beratung",
    "form_p": "Anzeigen allein reichen nicht. Erzählen Sie mir Ihr Ziel — Kauf, Investment oder Verkauf — und wir planen den richtigen Weg.",
    "cta": "Beratung vereinbaren",
    "nav_buy": "Kaufen",
    "nav_inv": "Investieren",
    "nav_sell": "Verkaufen",
}

FR = {
    "title": "Conseiller acheteurs et investisseurs immobiliers | Maurizio Piraino",
    "desc": "Conseiller pour acheteurs et investisseurs immobiliers à Milan et en Lombardie. Property finding, analyse, négociation et accompagnement jusqu'à l'acte.",
    "eyebrow": "Milan · Lombardie · Conseil immobilier",
    "h1": "Conseiller pour acheteurs et investisseurs immobiliers",
    "lead": "L'allié de ceux qui achètent un logement et de ceux qui investissent. <strong>Analyse avant l'achat</strong>, recherche personnalisée, contrôle documentaire et accompagnement jusqu'à l'acte.",
    "form_h2": "Réservez une consultation confidentielle",
    "form_p": "Feuilleter des annonces ne suffit pas. Parlez-moi de votre objectif — achat, investissement ou vente — et construisons le bon parcours.",
    "cta": "Réserver une consultation",
    "nav_buy": "Acheter",
    "nav_inv": "Investir",
    "nav_sell": "Vendre",
}


def reposition_locale(rel: str, lang: dict) -> None:
    path = ROOT / rel
    if not path.exists():
        print(f"  skip missing {rel}")
        return
    html = path.read_text(encoding="utf-8")
    if "consultant-home.css" not in html:
        html = html.replace(
            '<link rel="stylesheet" href="/assets/dual-path.css?v=20260735" />',
            '<link rel="stylesheet" href="/assets/dual-path.css?v=20260735" />\n'
            '  <link rel="stylesheet" href="/assets/consultant-home.css?v=20260715" />',
        )
    # Soft touch: if Italian-scripted sections already apply via reuse, leave DE/FR
    # for a later full i18n pass; ensure CSS is linked.
    # Replace title if still seller-framed
    html = re.sub(r"<title>[^<]*</title>", f"<title>{lang['title']}</title>", html, count=1)
    html = re.sub(
        r'<meta name="description" content="[^"]*" />',
        f'<meta name="description" content="{lang["desc"]}" />',
        html,
        count=1,
    )
    path.write_text(html, encoding="utf-8")
    print(f"  wrote {rel} (meta + css)")


def main() -> None:
    print("Repositioning IT homepage…")
    reposition_it()
    print("Updating DE/FR homepage meta…")
    reposition_locale("de/index.html", DE)
    reposition_locale("fr/index.html", FR)
    print("Done.")


if __name__ == "__main__":
    main()
