#!/usr/bin/env python3
"""Slim ZH home + create dedicated EN home at /en/ + wire hreflang/nav."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Reuse section helpers from slim_to_85
import sys

sys.path.insert(0, str(ROOT / "scripts"))
from slim_to_85 import (  # type: ignore
    remove_sections_by_class,
    replace_section_class,
)


def slim_zh() -> None:
    path = ROOT / "zh/index.html"
    html = path.read_text(encoding="utf-8")

    html = remove_sections_by_class(
        html,
        [
            "seller-stats-strip",
            "seller-includes",
            "seller-compare",
            "seller-zones",
            "seller-mid-cta",
            "network",
            "market",
            "steps",
        ],
    )

    # hero benefits
    html = re.sub(
        r"<ul class=\"seller-form-benefits\">.*?</ul>",
        """<ul class="seller-form-benefits">
            <li>量身专属寻盘</li>
            <li>出价前数字清晰</li>
            <li>陪同至过户</li>
          </ul>""",
        html,
        count=1,
        flags=re.S,
    )

    pb_strip = """
    <section class="pb-strip" aria-label="要点">
      <div class="container pb-strip-grid">
        <div><strong>Maurizio</strong><span>直接对接，非呼叫中心</span></div>
        <div><strong>方法</strong><span>先分析，再决策</span></div>
        <div><strong>网络</strong><span>RE/MAX 作支持，不抢主角</span></div>
        <div><strong>24h</strong><span>个人回复</span></div>
      </div>
    </section>
"""
    if 'class="pb-strip"' not in html:
        html = html.replace(
            '<section class="consultant-path"',
            pb_strip.strip() + '\n\n    <section class="consultant-path"',
            1,
        )

    about = """
    <section class="about pb-about" id="metodo">
      <div class="container about-grid">
        <div class="portrait-card reveal">
          <img src="/foto.jpg" loading="lazy" decoding="async" alt="Maurizio Piraino — 米兰房地产顾问" />
          <div class="portrait-info">
            <strong>Maurizio Piraino</strong>
            <span>购房者与投资者顾问 · 米兰</span>
            <div class="badges">
              <div class="badge">REA BS-639579</div>
              <div class="badge">测量师</div>
              <div class="badge">RE/MAX Associati</div>
            </div>
          </div>
        </div>
        <div class="reveal">
          <div class="section-kicker">关于我</div>
          <h2>以您为中心。方法由我负责。</h2>
          <p class="lead">我在米兰与伦巴第为购房者与投资者提供顾问服务。RE/MAX 加盟带来网络与工具：责任与沟通始终是个人的。</p>
          <div class="quote">“我不带您去买一则广告。我帮您做出更好的决定。”</div>
          <div class="method-grid pb-method">
            <div class="card"><div class="num">1</div><h3>倾听</h3><p>目标、预算、时间——从您开始。</p></div>
            <div class="card"><div class="num">2</div><h3>寻盘</h3><p>精准筛选，含非公开盘源。</p></div>
            <div class="card"><div class="num">3</div><h3>保障</h3><p>文件、报价、过户——没有意外。</p></div>
          </div>
        </div>
      </div>
    </section>
"""
    services = """
    <section class="seller-services consultant-services pb-services" id="servizi">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">服务</div>
          <h2>从寻盘到过户，守护购房者与投资者。</h2>
          <p>需要时，也把同一套方法用于卖房。</p>
        </div>
        <div class="seller-services-grid">
          <article class="seller-service-card featured reveal">
            <div class="seller-service-num">01</div>
            <h3>专属寻盘</h3>
            <p>个性化搜索、带看、谈判与过户协调。</p>
          </article>
          <article class="seller-service-card reveal">
            <div class="seller-service-num">02</div>
            <h3>投资者</h3>
            <p>收益与增值机会，回报分析清晰。</p>
          </article>
          <article class="seller-service-card reveal">
            <div class="seller-service-num">03</div>
            <h3>自住房</h3>
            <p>首套房或换房：文件核查与谈判支持。</p>
          </article>
          <article class="seller-service-card secondary reveal">
            <div class="seller-service-num">04</div>
            <h3>您要卖房</h3>
            <p>分析、策略与销售方案。<a href="/zh/chu-shou-milan/" style="color:inherit;text-decoration:underline">了解更多 →</a></p>
          </article>
        </div>
        <div class="seller-compare-table reveal pb-compare">
          <div class="seller-compare-row seller-compare-head">
            <span>方面</span><span>独自 / 门户</span><span>与我合作</span>
          </div>
          <div class="seller-compare-row"><span>寻盘</span><span class="no">仅公开广告</span><span class="yes">含非公开盘源</span></div>
          <div class="seller-compare-row"><span>文件</span><span class="no">自行承担风险</span><span class="yes">出价前核查</span></div>
          <div class="seller-compare-row"><span>价格</span><span class="no">凭感觉</span><span class="yes">结构化谈判</span></div>
        </div>
      </div>
    </section>
"""
    situations = """
    <section class="situations pb-situations">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">如果您是这样的人</div>
          <h2>保障与方法，而不是刷不完的广告。</h2>
        </div>
        <div class="situations-grid pb-situations-grid">
          <article class="card reveal"><div class="num">01</div><h3>您在找房</h3><p>要的是精准筛选，不是数月无效浏览。</p></article>
          <article class="card reveal"><div class="num">02</div><h3>您在投资</h3><p>先要回报与风险数字，再投入资金。</p></article>
          <article class="card reveal"><div class="num">03</div><h3>担心买贵</h3><p>要数据、文件与站在您这边的谈判。</p></article>
        </div>
      </div>
    </section>
"""
    testimonials = """
    <section class="testimonials" id="recensioni">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">客户体验</div>
          <h2>和我一起做决定的人，不是靠运气。</h2>
        </div>
        <div class="testimonial-grid pb-testimonials">
          <article class="testimonial-card reveal"><div class="stars">★★★★★</div><p>在米兰找了好几个月。筛选寻盘与出价前文件核查，帮我省下时间和昂贵错误。</p><div class="person"><div class="avatar">EL</div><div><strong>购房者 · Porta Romana</strong><span>首套房 · 米兰</span></div></div></article>
          <article class="testimonial-card reveal"><div class="stars">★★★★★</div><p>投资要数字清楚。分析冷静、没有压力：筛选并完成交易，心里有数。</p><div class="person"><div class="avatar">MR</div><div><strong>投资者 · Navigli</strong><span>收益型房产 · 米兰</span></div></div></article>
          <article class="testimonial-card reveal"><div class="stars">★★★★★</div><p>带看时对文件与风险答复清楚。谈判更有把握。</p><div class="person"><div class="avatar">SF</div><div><strong>购房者 · Isola</strong><span>换房 · 米兰</span></div></div></article>
        </div>
      </div>
    </section>
"""
    faq = """
    <section class="faq pb-faq">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-kicker">FAQ</div>
          <h2>常见问题</h2>
        </div>
        <div class="faq-grid">
          <details open><summary>您是经纪人还是购房顾问？</summary><p>我是 Maurizio Piraino，RE/MAX 加盟房产经纪人。以顾问身份服务购房者与投资者，也以同一方法服务卖房客户。</p></details>
          <details><summary>什么是专属寻盘？</summary><p>个性化找房：需求分析、含非公开盘源筛选、带看、谈判与过户协调。</p></details>
          <details><summary>首次咨询有委托义务吗？</summary><p>没有。第一次沟通只是判断是否适合合作。</p></details>
          <details><summary>如果我要卖房呢？</summary><p>可申请私密分析：真实价值、销售阻碍与呈现方式。<a href="/zh/chu-shou-milan/">卖房页面 →</a></p></details>
          <details><summary>与 ValoreCasaTua.it 有何关系？</summary><p>ValoreCasaTua 是内容门户（指南与报价）。这里是我本人与专业服务。</p></details>
        </div>
      </div>
    </section>
"""
    editorial = """
    <section class="editorial-bridge" aria-label="ValoreCasaTua">
      <div class="container">
        <div class="editorial-bridge-inner reveal">
          <div>
            <div class="section-kicker">两个角色，互不混淆</div>
            <h2>我负责闭环。ValoreCasaTua 负责信息。</h2>
            <p>指南与每平米价格留在内容门户。这里与我合作：寻盘、投资，以及需要时的卖房。</p>
          </div>
          <div class="editorial-bridge-actions">
            <a class="btn btn-red" href="#form">预约咨询</a>
            <a class="btn btn-outline-dark" href="https://valorecasatua.it/" rel="noopener" target="_blank">ValoreCasaTua.it →</a>
          </div>
        </div>
      </div>
    </section>
"""
    final = """
    <section class="final-cta">
      <div class="container reveal">
        <h2>聊聊吧。一起找到合适的房产。</h2>
        <p>自住或投资：分析、寻盘与过户保障——由我一人对接。</p>
        <div class="hero-actions" style="justify-content:center">
          <a class="btn btn-red" href="#form">预约咨询</a>
          <a class="btn btn-wa" href="https://wa.me/393514581993?text=%E4%BD%A0%E5%A5%BD%20Maurizio%EF%BC%8C%E6%88%91%E6%83%B3%E5%92%A8%E8%AF%A2。">WhatsApp</a>
        </div>
      </div>
    </section>
"""
    engage = """
    <section class="pb-engage-band" aria-label="下一步">
      <div class="container reveal">
        <div class="pb-engage-inner">
          <div>
            <p class="seller-mid-kicker">下一步</p>
            <h2>告诉我您在找什么。</h2>
            <p>自住或投资：24 小时内个人回复，无委托义务。</p>
          </div>
          <div class="seller-mid-actions">
            <a class="btn btn-red" href="#form">预约咨询</a>
            <a class="btn btn-light" href="https://wa.me/393514581993?text=%E4%BD%A0%E5%A5%BD%20Maurizio%EF%BC%8C%E6%88%91%E6%83%B3%E5%92%A8%E8%AF%A2。">WhatsApp</a>
          </div>
        </div>
      </div>
    </section>
"""

    html = replace_section_class(html, "about", about)
    html = replace_section_class(html, "seller-services", services)
    html = replace_section_class(html, "situations", situations)
    html = replace_section_class(html, "testimonials", testimonials)
    html = replace_section_class(html, "faq", faq)
    # editorial may already exist
    if 'class="editorial-bridge"' in html:
        html = replace_section_class(html, "editorial-bridge", editorial)
    html = replace_section_class(html, "final-cta", final)

    # reorder: after path → about, services, situations, engage, testimonials...
    # Extract and reorder like DE
    def extract(html: str, *, sid=None, cls=None):
        if sid:
            pat = re.compile(rf'<section\b[^>]*\bid="{re.escape(sid)}"[^>]*>', re.I)
        else:
            pat = re.compile(
                rf'<section\b[^>]*\bclass="[^"]*{re.escape(cls)}[^"]*"[^>]*>', re.I
            )
        m = pat.search(html)
        if not m:
            return None, html
        start = m.start()
        i = m.end()
        depth = 1
        while depth and i < len(html):
            no = html.find("<section", i)
            nc = html.find("</section>", i)
            if nc == -1:
                break
            if no != -1 and no < nc:
                depth += 1
                i = no + 8
            else:
                depth -= 1
                i = nc + len("</section>")
        return html[start:i], html[:start] + html[i:]

    about_b, html = extract(html, sid="metodo")
    services_b, html = extract(html, sid="servizi")
    situations_b, html = extract(html, cls="situations")
    # remove old engage if any then insert clean stack after path
    if "pb-engage-band" in html:
        _, html = extract(html, cls="pb-engage-band")

    m = re.search(r'<section\b[^>]*class="[^"]*consultant-path[^"]*"[^>]*>', html)
    if m and about_b and services_b and situations_b:
        start = m.start()
        i = m.end()
        depth = 1
        while depth and i < len(html):
            no = html.find("<section", i)
            nc = html.find("</section>", i)
            if nc == -1:
                break
            if no != -1 and no < nc:
                depth += 1
                i = no + 8
            else:
                depth -= 1
                i = nc + len("</section>")
        insert = (
            "\n\n"
            + about_b.strip()
            + "\n\n"
            + services_b.strip()
            + "\n\n"
            + situations_b.strip()
            + "\n\n"
            + engage.strip()
            + "\n"
        )
        html = html[:i] + insert + html[i:]

    # SEO polish ZH
    html = html.replace(
        "<title>Maurizio Piraino | 购房者与投资者顾问 · 米兰</title>",
        "<title>Maurizio Piraino | 购房者与投资者顾问 · 米兰</title>",
    )
    if 'property="og:locale"' not in html:
        html = html.replace(
            '<meta property="og:type" content="website" />',
            '<meta property="og:type" content="website" />\n'
            '  <meta property="og:locale" content="zh_CN" />\n'
            '  <meta property="og:site_name" content="Maurizio Piraino" />',
            1,
        )
    html = html.replace(
        'consultant-home.css?v=20260740', 'consultant-home.css?v=20260742'
    )
    if "site-polish-v10.css" not in html:
        html = html.replace(
            "</head>",
            '  <link rel="stylesheet" href="/assets/site-polish-v10.css?v=20260742" />\n</head>',
            1,
        )
    else:
        html = html.replace(
            "site-polish-v10.css?v=20260741", "site-polish-v10.css?v=20260742"
        )
        html = html.replace(
            "site-polish-v10.css?v=20260740", "site-polish-v10.css?v=20260742"
        )

    # path sell copy
    html = html.replace(
        "<p>存在但不占主导：估价、策略与营销。</p>",
        "<p>私密分析、定价策略与销售方案。</p>",
    )

    path.write_text(html, encoding="utf-8")
    print("ZH sections:", html.count("<section"))


def create_en_home() -> None:
    """Clone slim DE home and translate to English."""
    src = (ROOT / "de/index.html").read_text(encoding="utf-8")
    html = src

    # lang + urls
    html = html.replace('<html lang="de">', '<html lang="en">')
    html = html.replace("https://mauriziopiraino.it/de/", "https://mauriziopiraino.it/en/")
    html = html.replace('content="de_DE"', 'content="en_US"')
    html = html.replace('"inLanguage": "de-DE"', '"inLanguage": "en-GB"')
    html = html.replace("/de/haus-kaufen/", "/en/buy-home/")
    html = html.replace("/de/haus-kaufen-milan/", "/en/buy-home-milan/")
    html = html.replace("/de/haus-verkaufen-milan/", "/vendere-casa-milano/")
    html = html.replace('href="/de/"', 'href="/en/"')

    # hreflang block: ensure en present
    if 'hreflang="en"' not in html.split("</head>")[0]:
        html = html.replace(
            '<link rel="alternate" hreflang="it" href="https://mauriziopiraino.it/" />',
            '<link rel="alternate" hreflang="it" href="https://mauriziopiraino.it/" />\n'
            '<link rel="alternate" hreflang="en" href="https://mauriziopiraino.it/en/" />',
            1,
        )

    # Lang switcher: DE active → EN active
    # Replace active DE span with link, and EN link with active span
    de_active = re.search(
        r'<span class="lang-option lang-option-active"[^>]*title="Deutsch".*?</span>',
        html,
        re.S,
    )
    en_link = re.search(
        r'<a href="/en/[^"]*" class="lang-option" hreflang="en"[^>]*>.*?</a>',
        html,
        re.S,
    )
    if de_active and en_link:
        de_span = de_active.group(0)
        en_a = en_link.group(0)
        de_as_link = (
            '<a href="/de/" class="lang-option" hreflang="de" title="Deutsch">'
            + re.sub(r'^<span[^>]*>', '', de_span).replace("</span>", "")
            + "</a>"
        )
        # simplify: rebuild EN active
        en_active = (
            '<span class="lang-option lang-option-active" aria-current="true" title="English">'
            '<svg class="lang-flag" viewBox="0 0 18 12" aria-hidden="true">'
            '<rect width="18" height="12" fill="#012169"/>'
            '<path fill="#fff" d="M0 0l18 12M18 0L0 12" stroke="#fff" stroke-width="2.2"/>'
            '<path fill="none" stroke="#C8102E" stroke-width="1.2" d="M0 0l18 12M18 0L0 12"/>'
            '<path fill="#fff" d="M8 0h2v12H8zM0 5h18v2H0z"/>'
            '<path fill="#C8102E" d="M9 0h1v12H9zM0 5.5h18v1H0z"/></svg>'
            '<span class="lang-code">EN</span></span>'
        )
        html = html.replace(de_span, de_as_link, 1)
        html = html.replace(en_a, en_active, 1)

    # Also fix any remaining buy-home-milan lang self-links in switcher pointing wrong
    html = html.replace('href="/en/buy-home-milan/"', 'href="/en/"')

    replacements = [
        (
            "<title>Maurizio Piraino | Berater für Käufer und Investoren · Mailand</title>",
            "<title>Maurizio Piraino | Buyer & investor advisory · Milan</title>",
        ),
        (
            'content="Berater für Immobilienkäufer und Investoren in Mailand und der Lombardei. Über das RE/MAX-Netzwerk auch in ganz Italien. Property Finding, Analyse und Begleitung bis zum Notartermin."',
            'content="Maurizio Piraino — buyer and investor advisory in Milan and Lombardy. Property finding, analysis and support to completion. RE/MAX in support — reply within 24h."',
        ),
        (
            'content="Maurizio Piraino | Berater für Käufer und Investoren · Mailand"',
            'content="Maurizio Piraino | Buyer & investor advisory · Milan"',
        ),
        (
            'content="Möchten Sie in Mailand verkaufen? Erhalten Sie eine vertrauliche Analyse auf realen Daten, Mikrozonen und Verkaufsstrategie."',
            'content="Find the right property in Milan with analysis, protection and method. Property finding for buyers and investors."',
        ),
        (
            'content="RE/MAX-Immobilienberater Mailand | Immobilienbewertung"',
            'content="Maurizio Piraino | Buyer & investor advisory · Milan"',
        ),
        (
            'content="Vertrauliche Immobilienanalyse zum Verkauf in Mailand — mit Methode, realen Daten und Strategie."',
            'content="Property finding and advisory for buyers and investors in Milan. Analysis first — then the right decision."',
        ),
        ("Zum Inhalt springen", "Skip to content"),
        (
            "<strong>Maurizio Piraino</strong> · Käufer und Investoren",
            "<strong>Maurizio Piraino</strong> · Buyers and investors",
        ),
        ("Menü öffnen", "Open menu"),
        ("Hauptmenü", "Main menu"),
        (">Weg<", ">Path<"),
        (">Kaufen<", ">Buy<"),
        (">Investieren<", ">Invest<"),
        (">Verkaufen<", ">Sell<"),
        (">Über mich<", ">About me<"),
        (">Die Methode<", ">The method<"),
        (">Info<", ">About<"),
        ("Sprache wählen", "Choose language"),
        ("Beratung vereinbaren", "Book a consultation"),
        (
            "Berater für Käufer und Investoren · Mailand",
            "Advisor for buyers and investors · Milan",
        ),
        ("Eine Person, eine Methode", "One person, one method"),
        (
            "Affiliierter RE/MAX · Antwort innerhalb von 24h · keine Verpflichtung",
            "RE/MAX affiliate · reply within 24h · no obligation",
        ),
        (
            "Kaufen und investieren mit Analyse — nicht nach Gefühl.",
            "Buy and invest with analysis — not by gut feeling.",
        ),
        (
            "Der Partner für alle, die ein Haus kaufen oder in Immobilien investieren. <strong>Analyse vor dem Kauf</strong>, persönliche Suche, Dokumentenprüfung und Begleitung bis zum Notartermin.",
            "Your ally when buying a home or investing in property. <strong>Analysis before you buy</strong>, personalised search, document checks and support through to completion.",
        ),
        ("Property Finding auf Maß", "Tailored Property Finding"),
        ("Klare Zahlen vor dem Angebot", "Clear numbers before you offer"),
        ("Begleitung bis zum Notartermin", "Support through to completion"),
        ("Erzählen Sie mir, was Sie suchen", "Tell me what you are looking for"),
        ("Vereinbaren Sie eine vertrauliche Beratung", "Book a confidential consultation"),
        (
            "Anzeigen allein reichen nicht. Erzählen Sie mir Ihr Ziel — Kauf, Investment oder Verkauf.",
            "Listings alone are not enough. Tell me your goal — buy, invest or sell.",
        ),
        ("Antwort innerhalb von 24h", "Reply within 24h"),
        ("Keine Mandatsverpflichtung", "No mandate obligation"),
        ("Direkter Ansprechpartner", "Direct contact"),
        ("Zusicherungen", "Assurances"),
        ("Formularfortschritt", "Form progress"),
        ("Zuerst: was brauchen Sie?", "First: what do you need?"),
        (">Ihr Ziel<", ">Your goal<"),
        ('data-v="Kauf"', 'data-v="Buy"'),
        (">Kauf<", ">Buy<"),
        ('data-v="Investment"', 'data-v="Invest"'),
        # Investment label already English-ish
        ('data-v="Verkauf"', 'data-v="Sell"'),
        (">Verkauf<", ">Sell<"),
        ("Zone oder Gemeinde der Immobilie", "Area or municipality"),
        (
            "Stadtteil oder Gemeinde eingeben (z. B. Brera, Sesto San Giovanni …)",
            "Enter neighbourhood or town (e.g. Brera, Como, Monza…)",
        ),
        ("Kurzüberblick", "At a glance"),
        ("Direkter Ansprechpartner, kein Callcenter", "Direct contact, not a call centre"),
        (">Methode<", ">Method<"),
        ("Analyse vor Emotion", "Analysis before emotion"),
        (">Netzwerk<", ">Network<"),
        (
            "RE/MAX als Unterstützung, nicht im Zentrum",
            "RE/MAX in support, not centre stage",
        ),
        ("Persönliche Antwort", "Personal reply"),
        ("Wählen Sie Ihren Weg", "Choose your path"),
        ("Wie kann ich helfen", "How can I help"),
        ("01 · Hauptservice", "01 · Main service"),
        (
            "Persönliche Immobiliensuche — auch off-market. Auswahl, Besichtigungen, Verhandlung und Begleitung bis zum Notartermin.",
            "Personalised property search — including off-market. Selection, viewings, negotiation and support to completion.",
        ),
        ("Suche starten →", "Start the search →"),
        ("02 · Investoren", "02 · Investors"),
        ("Beratung für Investoren", "Investor advisory"),
        (
            "Renditeobjekte, Wertsteigerung, Wirtschaftlichkeitsanalyse — mit Verhandlungsunterstützung.",
            "Yield opportunities, value-add and return analysis — with negotiation support.",
        ),
        ("Investment analysieren →", "Analyse the investment →"),
        ("03 · Verkäufer", "03 · Sellers"),
        ("Bewertung und Verkauf", "Valuation and sale"),
        (
            "Vertrauliche Analyse, Preisstrategie und Verkaufsplan.",
            "Confidential analysis, pricing strategy and sale plan.",
        ),
        ("Analyse anfordern →", "Request analysis →"),
        (
            "Immobilienberater in Mailand",
            "real estate advisor in Milan",
        ),
        (
            "Berater für Käufer und Investoren · Mailand",
            "Advisor for buyers and investors · Milan",
        ),
        ("Vermessungsingenieur", "Surveyor"),
        (">Über mich<", ">About me<"),
        (
            "Der Bezugspunkt sind Sie. Die Methode ist meine.",
            "You are the reference point. The method is mine.",
        ),
        (
            "Ich arbeite in Mailand und der Lombardei als Berater für Käufer und Investoren. Die RE/MAX-Affiliation gibt mir Netzwerk und Werkzeuge: Verantwortung und Beziehung bleiben persönlich.",
            "I work in Milan and Lombardy as an advisor for buyers and investors. RE/MAX affiliation gives me network and tools: responsibility and the relationship stay personal.",
        ),
        (
            "„Ich begleite Sie nicht beim Kauf einer Anzeige. Ich helfe bei der besten Entscheidung.“",
            "“I don’t take you to buy a listing. I help you make the best decision.”",
        ),
        (">Zuhören<", ">Listen<"),
        ("Ziel, Budget, Timing — wir starten bei Ihnen.", "Goal, budget, timing — we start with you."),
        (">Suche<", ">Search<"),
        (
            "Gezielte Auswahl, auch außerhalb der Portale.",
            "Targeted selection, including off-portal.",
        ),
        (">Schutz<", ">Protection<"),
        (
            "Dokumente, Angebot, Notar — ohne Überraschungen.",
            "Documents, offer, notary — no surprises.",
        ),
        (">Leistungen<", ">Services<"),
        (
            "Ich schütze Käufer und Investoren — von der Suche bis zum Notar.",
            "I protect buyers and investors — from search to completion.",
        ),
        (
            "Und bringe dieselbe Methode zu Verkäufern, wenn nötig.",
            "And I bring the same method to sellers when needed.",
        ),
        (
            "Persönliche Suche, Besichtigungen, Verhandlung und Koordination bis zum Notartermin.",
            "Personalised search, viewings, negotiation and coordination to completion.",
        ),
        (">Investoren<", ">Investors<"),
        (
            "Renditeobjekte und Wertsteigerung mit klarer Wirtschaftlichkeitsanalyse.",
            "Yield and value-add opportunities with clear return analysis.",
        ),
        (">Immobilienkäufer<", ">Home buyers<"),
        (
            "Ersterwerb oder Wechsel: Dokumentenprüfung und Verhandlungsunterstützung.",
            "First home or move: document checks and negotiation support.",
        ),
        (">Sie verkaufen<", ">You are selling<"),
        (
            'Maximum ohne Unterverkauf: Analyse, Strategie und Verkaufsplan. <a href="/vendere-casa-milano/" style="color:inherit;text-decoration:underline">Mehr erfahren →</a>',
            'Maximise without underselling: analysis, strategy and sale plan. <a href="/vendere-casa-milano/" style="color:inherit;text-decoration:underline">Learn more →</a>',
        ),
        (">Aspekt<", ">Aspect<"),
        (">Allein / Portal<", ">Alone / portal<"),
        (">Mit mir<", ">With me<"),
        (">Nur öffentliche Anzeigen<", ">Public listings only<"),
        (">Auch off-market<", ">Also off-market<"),
        (">Dokumente<", ">Documents<"),
        (">Auf eigenes Risiko<", ">At your risk<"),
        (">Prüfung vor dem Angebot<", ">Checks before the offer<"),
        (">Preis<", ">Price<"),
        (">Emotion<", ">Emotion<"),
        (">Strukturierte Verhandlung<", ">Structured negotiation<"),
        (
            "Dieser Weg ist für Sie, wenn",
            "This path is for you if",
        ),
        (
            "Schutz und Methode — keine Anzeigen zum Durchscrollen.",
            "Protection and method — not endless scrolling of listings.",
        ),
        (">Sie suchen ein Zuhause<", ">You are looking for a home<"),
        (
            "Gefilterte Suche statt Monate mit falschen Anzeigen.",
            "Filtered search instead of months of wrong listings.",
        ),
        (">Sie investieren<", ">You invest<"),
        (
            "Zahlen zu Rendite und Risiko, bevor Kapital gebunden wird.",
            "Numbers on yield and risk before capital is committed.",
        ),
        (">Sie fürchten, zu viel zu zahlen<", ">You fear overpaying<"),
        (
            "Daten, Dokumente und eine Verhandlung in Ihrem Interesse.",
            "Data, documents and a negotiation built around your interests.",
        ),
        ("Nächster Schritt", "Next step"),
        (
            "Erzählen Sie mir, was Sie suchen.",
            "Tell me what you are looking for.",
        ),
        (
            "Wohnen oder Investment: persönliche Antwort innerhalb von 24 Stunden — ohne Verpflichtung.",
            "Home or investment: personal reply within 24 hours — no obligation.",
        ),
        (">Erfahrungen<", ">Experiences<"),
        (
            "Wer mit mir entschieden hat — nicht zufällig.",
            "Those who decided with me — not by chance.",
        ),
        (
            "Monatelange Suche in Mailand. Gefilterte Recherche und Dokumentenprüfung vor dem Angebot haben Zeit und teure Fehler gespart.",
            "Months searching in Milan. Filtered research and document checks before the offer saved time and costly mistakes.",
        ),
        ("Käuferin · Porta Romana", "Buyer · Porta Romana"),
        ("Ersterwerb · Mailand", "First home · Milan"),
        (
            "Für das Investment wollte ich klare Zahlen. Sachliche Analyse, kein Druck: Auswahl und Abschluss mit Bewusstsein.",
            "For the investment I wanted clear numbers. Sober analysis, no pressure: selection and closing with clarity.",
        ),
        ("Investor · Navigli", "Investor · Navigli"),
        ("Renditeobjekt · Mailand", "Yield property · Milan"),
        (
            "Bei Besichtigungen klare technische Antworten zu Dokumenten und Risiken. Die Verhandlung war sicherer.",
            "Clear technical answers on documents and risks during viewings. Negotiation felt safer.",
        ),
        ("Wohnungswechsel · Mailand", "Home move · Milan"),
        (">Häufige Fragen<", ">Frequently asked questions<"),
        (
            "Sind Sie Makler oder Käuferberater?",
            "Are you an agent or a buyer’s advisor?",
        ),
        (
            "Ich bin Maurizio Piraino, RE/MAX-Immobilienberater. Ich begleite Käufer und Investoren — und auch Verkäufer, mit derselben Methode.",
            "I am Maurizio Piraino, a RE/MAX-affiliated real estate advisor. I support buyers and investors — and sellers too, with the same method.",
        ),
        ("Was ist Property Finding?", "What is Property Finding?"),
        (
            "Die persönliche Immobiliensuche: Bedarf, Auswahl auch off-market, Besichtigungen, Verhandlung und Koordination bis zum Notar.",
            "Personalised property search: needs, selection including off-market, viewings, negotiation and coordination to completion.",
        ),
        (
            "Verpflichtet die Erstberatung?",
            "Does the first consultation create obligations?",
        ),
        (
            "Nein. Das erste Gespräch dient dazu zu klären, ob eine Zusammenarbeit Sinn ergibt.",
            "No. The first conversation is to see whether working together makes sense.",
        ),
        ("Und wenn ich verkaufen muss?", "What if I need to sell?"),
        (
            'Fordern Sie eine vertrauliche Analyse an: realer Wert, Verkaufshemmnisse und Präsentation. <a href="/vendere-casa-milano/">Zur Verkaufsseite →</a>',
            'Request a confidential analysis: real value, sale blockers and presentation. <a href="/vendere-casa-milano/">Go to the sale page →</a>',
        ),
        (
            "Was hat ValoreCasaTua.it damit zu tun?",
            "How does ValoreCasaTua.it fit in?",
        ),
        (
            "ValoreCasaTua ist das redaktionelle Portal (Guides und Preise). Hier finden Sie mich und die professionellen Leistungen.",
            "ValoreCasaTua is the editorial portal (guides and prices). Here you find me and the professional services.",
        ),
        ("Zwei Rollen, null Verwirrung", "Two roles, zero confusion"),
        (
            "Ich schließe den Weg ab. ValoreCasaTua informiert.",
            "I close the journey. ValoreCasaTua informs.",
        ),
        (
            "Guides und Quadratmeterpreise bleiben auf dem redaktionellen Portal. Hier arbeiten Sie mit mir: Property Finding, Investoren und Verkauf bei Bedarf.",
            "Guides and price-per-sqm stay on the editorial portal. Here you work with me: Property Finding, investors and sale when needed.",
        ),
        (
            "Sprechen wir darüber. Suchen wir gemeinsam die richtige Immobilie.",
            "Let’s talk. Let’s find the right property together.",
        ),
        (
            "Wohnen oder Investment: Analyse, Suche und Schutz bis zum Notar — mit mir als einzigem Ansprechpartner.",
            "Home or investment: analysis, search and protection to completion — with me as your single contact.",
        ),
        (
            "Zuerst die Analyse. Dann die richtige Entscheidung.",
            "Analysis first. Then the right decision.",
        ),
        (
            "Immobilienberater bei RE/MAX Associati Real Estate · Mailand, Viale Gran Sasso 31",
            "Real estate advisor at RE/MAX Associati Real Estate · Milan, Viale Gran Sasso 31",
        ),
        (
            "RE/MAX-Immobilienberater · REA BS-639579 · USt-IdNr. 14597560961 · Mailand<br><small>Die Erstberatung begründet keine Verpflichtung zur Beauftragung.</small>",
            "RE/MAX-affiliated real estate advisor · REA BS-639579 · VAT 14597560961 · Milan<br><small>The initial consultation does not create any mandate obligation.</small>",
        ),
        ("Operative Basis:", "Operating base:"),
        (">Mailand<", ">Milan<"),
        ("außerhalb der Region über RE/MAX-Netzwerk", "outside the region via RE/MAX network"),
        ("OMI-Preisguides:", "OMI price guides:"),
        ("Möchten Sie kaufen?", "Want to buy?"),
        ("Alle 12 Provinzen der Lombardei", "All 12 Lombardy provinces"),
        ("Schnellaktionen", "Quick actions"),
        ("Datenschutzerklärung", "Privacy policy"),
        (
            "Mit dem Absenden stimmen Sie der Datenverarbeitung zur Kontaktaufnahme zu.",
            "By submitting you agree to data processing for contact purposes.",
        ),
        ("Vertrauliche Daten · Keine Verpflichtung zum Mandat · Persönliche Antwort", "Confidential data · No mandate obligation · Personal reply"),
        ("Mailand", "Milan"),
        ("Lombardei", "Lombardy"),
    ]

    for a, b in replacements:
        html = html.replace(a, b)

    # Website schema name
    html = html.replace(
        '"name": "Maurizio Piraino — RE/MAX"',
        '"name": "Maurizio Piraino"',
    )

    # skip-link already done
    # nav brand href should stay /
    # Fix foto path - DE uses foto.jpg relative; EN is in /en/ so need /foto.jpg
    html = html.replace('src="foto.jpg"', 'src="/foto.jpg"')

    # landing hidden
    html = html.replace(
        'value="Landing Mailand RE/MAX Premium"',
        'value="EN Homepage · Buyer Investor Advisory"',
    )

    out = ROOT / "en/index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("EN home written, sections:", html.count("<section"))


def wire_en_links() -> None:
    """Point hreflang and lang switchers to /en/ on key pages."""
    targets = []
    for pattern in [
        "index.html",
        "de/index.html",
        "fr/index.html",
        "zh/index.html",
        "en/index.html",
        "comprare-casa-milano/index.html",
        "vendere-casa-milano/index.html",
        "en/buy-home-milan/index.html",
        "en/buy-home/index.html",
        "de/haus-kaufen-milan/index.html",
        "fr/acheter-maison-milan/index.html",
        "zh/mai-fang-milan/index.html",
    ]:
        p = ROOT / pattern
        if p.exists():
            targets.append(p)

    # also all html with buy-home-milan lang link
    for p in ROOT.rglob("*.html"):
        if p not in targets:
            t = p.read_text(encoding="utf-8", errors="ignore")
            if 'hreflang="en"' in t or "/en/buy-home-milan/" in t:
                targets.append(p)

    seen = set()
    for p in targets:
        rp = p.resolve()
        if rp in seen:
            continue
        seen.add(rp)
        html = p.read_text(encoding="utf-8")
        orig = html

        # hreflang en → /en/
        html = re.sub(
            r'(<link rel="alternate" hreflang="en" href=")https://mauriziopiraino\.it/en/[^"]*(")',
            r"\1https://mauriziopiraino.it/en/\2",
            html,
        )
        if 'hreflang="en"' not in html.split("</head>")[0] and "rel=\"canonical\"" in html:
            # insert after it alternate if present
            html = re.sub(
                r'(<link rel="alternate" hreflang="it" href="[^"]+" />)',
                r'\1\n<link rel="alternate" hreflang="en" href="https://mauriziopiraino.it/en/" />',
                html,
                count=1,
            )

        # lang switcher EN option → /en/ (but not when already on a buy-home page that wants city - for homes and hubs use /en/)
        html = re.sub(
            r'<a href="/en/buy-home-milan/" class="lang-option" hreflang="en"',
            '<a href="/en/" class="lang-option" hreflang="en"',
            html,
        )
        # brand link on EN pages to /en/
        if p.as_posix().startswith(str(ROOT / "en")) or "en/" in p.relative_to(ROOT).as_posix():
            # Keep brand as / for site root OR /en/ - use /en/ for EN section brand
            html = re.sub(
                r'(<a class="brand" href=")(/)(">)',
                r"\1/en/\3",
                html,
                count=1,
            )

        if html != orig:
            p.write_text(html, encoding="utf-8")
            print("wired", p.relative_to(ROOT))


def main() -> None:
    print("=== Slim ZH ===")
    slim_zh()
    print("=== Create EN home ===")
    create_en_home()
    print("=== Wire EN links ===")
    wire_en_links()
    # sanity
    for rel in ["zh/index.html", "en/index.html"]:
        t = (ROOT / rel).read_text(encoding="utf-8")
        print(
            rel,
            "sections",
            t.count("<section"),
            "polish",
            "site-polish-v10" in t,
            "engage",
            "pb-engage-band" in t,
            "brand",
            "hero-brand-mark" in t,
        )


if __name__ == "__main__":
    main()
