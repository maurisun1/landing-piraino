#!/usr/bin/env python3
"""Apply Maurizio-first personal brand + RE/MAX-as-support across i18n pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# --- topbar helpers ---------------------------------------------------------

TOPBAR_RE = re.compile(
    r'(<div class="topbar-tagline">)(.*?)(</div>)',
    re.DOTALL,
)


def fix_topbar_inner(inner: str) -> str:
    s = inner.strip()
    if "<strong>Maurizio Piraino</strong>" in s:
        return s

    # ZH: RE/MAX <strong>顾问</strong> · rest
    m = re.match(r"^RE/MAX\s*<strong>顾问</strong>\s*·\s*(.+)$", s)
    if m:
        return f"<strong>Maurizio Piraino</strong> · {m.group(1)}"

    # PREFIX <strong>RE/MAX</strong> · rest
    m = re.match(r"^(.+?)\s*<strong>RE/MAX</strong>\s*·\s*(.+)$", s)
    if m:
        prefix, rest = m.group(1).strip(), m.group(2).strip()
        # Home-style short role labels → drop prefix (like IT Consulente RE/MAX)
        if prefix in {
            "Berater",
            "Conseiller",
            "Consulente",
            "Agente Immobiliare affiliato",
        }:
            return f"<strong>Maurizio Piraino</strong> · {rest}"
        return f"<strong>Maurizio Piraino</strong> · {prefix} · {rest}"

    # PREFIX <strong>RE/MAX</strong> (no middot rest) e.g. Immobilienberatung · City already has ·
    m = re.match(r"^(.+?)\s*<strong>RE/MAX</strong>\s*$", s)
    if m:
        return f"<strong>Maurizio Piraino</strong> · {m.group(1).strip()}"

    # Any leftover strong RE/MAX inside topbar
    if "RE/MAX" in s and "<strong>" in s:
        s2 = re.sub(r"\s*<strong>RE/MAX</strong>\s*", " ", s)
        s2 = re.sub(r"\s*RE/MAX\s*", " ", s2)
        s2 = re.sub(r"\s*·\s*·\s*", " · ", s2).strip(" ·")
        return f"<strong>Maurizio Piraino</strong> · {s2}"

    return s


def patch_topbars(html: str) -> str:
    def repl(m: re.Match) -> str:
        return m.group(1) + fix_topbar_inner(m.group(2)) + m.group(3)

    return TOPBAR_RE.sub(repl, html)


# --- nav: RE/MAX link → method ---------------------------------------------

NAV_REMAX_REPLACEMENTS = [
    (r'<a href="#remax">RE/MAX</a>', '<a href="#metodo">Il metodo</a>'),
    (r'<a href="#remax">RE/MAX</a>', '<a href="#metodo">Il metodo</a>'),  # noop dup
]


def patch_nav_remax(html: str, lang: str) -> str:
    labels = {
        "it": "Il metodo",
        "en": "The method",
        "de": "Die Methode",
        "fr": "La méthode",
        "zh": "方法",
    }
    label = labels.get(lang, "The method")
    return html.replace('<a href="#remax">RE/MAX</a>', f'<a href="#metodo">{label}</a>')


# --- path intro / mid kicker -----------------------------------------------

def patch_path_and_kickers(html: str, lang: str) -> str:
    intros = {
        "de": (
            '<p class="consultant-path-intro"><em>RE/MAX</em> · Wie kann ich helfen</p>',
            '<p class="consultant-path-intro">Wie kann ich helfen</p>',
        ),
        "fr": (
            '<p class="consultant-path-intro"><em>RE/MAX</em> · Comment puis-je vous aider</p>',
            '<p class="consultant-path-intro">Comment puis-je vous aider</p>',
        ),
        "zh": (
            '<p class="consultant-path-intro"><em>RE/MAX</em> · 我能如何帮助您</p>',
            '<p class="consultant-path-intro">我能如何帮助您</p>',
        ),
    }
    kickers = {
        "de": (
            '<p class="seller-mid-kicker">RE/MAX · Beratung</p>',
            '<p class="seller-mid-kicker">Persönliche Beratung</p>',
        ),
        "fr": (
            '<p class="seller-mid-kicker">RE/MAX · Conseil</p>',
            '<p class="seller-mid-kicker">Conseil personnel</p>',
        ),
        "zh": (
            '<p class="seller-mid-kicker">RE/MAX · 顾问</p>',
            '<p class="seller-mid-kicker">个人顾问</p>',
        ),
    }
    if lang in intros:
        a, b = intros[lang]
        html = html.replace(a, b)
    if lang in kickers:
        a, b = kickers[lang]
        html = html.replace(a, b)
    # Generic dual-path / seller intros that lead with RE/MAX
    html = re.sub(
        r'(<p class="(?:consultant-path-intro|dual-path-intro)"[^>]*>)\s*<em>RE/MAX</em>\s*·\s*',
        r"\1",
        html,
    )
    html = re.sub(
        r'(<p class="seller-mid-kicker">)RE/MAX\s*·\s*',
        r"\1",
        html,
    )
    return html


# --- home hero blocks ------------------------------------------------------

HERO_BLOCKS = {
    "de": """\
<p class="hero-brand-mark reveal">Maurizio Piraino</p>
          <p class="hero-role-line reveal">Berater für Käufer und Investoren · Mailand</p>
          <div class="hero-agent reveal">
            <img src="foto.jpg" alt="Maurizio Piraino" width="64" height="64" decoding="async" />
            <div>
              <strong>Eine Person, eine Methode</strong>
              <span>Affiliierter RE/MAX · Antwort innerhalb von 24h · keine Verpflichtung</span>
            </div>
          </div>
""",
    "fr": """\
<p class="hero-brand-mark reveal">Maurizio Piraino</p>
          <p class="hero-role-line reveal">Conseiller pour acheteurs et investisseurs · Milan</p>
          <div class="hero-agent reveal">
            <img src="foto.jpg" alt="Maurizio Piraino" width="64" height="64" decoding="async" />
            <div>
              <strong>Une personne, une méthode</strong>
              <span>Affilié RE/MAX · réponse sous 24h · sans engagement</span>
            </div>
          </div>
""",
    "zh": """\
<p class="hero-brand-mark reveal">Maurizio Piraino</p>
          <p class="hero-role-line reveal">购房者与投资者顾问 · 米兰</p>
          <div class="hero-agent reveal">
            <img src="/foto.jpg" alt="Maurizio Piraino" width="64" height="64" decoding="async" />
            <div>
              <strong>一人，一套方法</strong>
              <span>RE/MAX 加盟顾问 · 24 小时内回复 · 无委托义务</span>
            </div>
          </div>
""",
}

OLD_HERO_RE = {
    "de": re.compile(
        r'<div class="hero-agent reveal">\s*'
        r'<img src="foto\.jpg" alt="Maurizio Piraino" width="56" height="56"[^/]*/>\s*'
        r"<div>\s*"
        r"<strong>Maurizio Piraino</strong>\s*"
        r"<span>Berater für Käufer und Investoren · RE/MAX</span>\s*"
        r"</div>\s*"
        r"</div>\s*"
        r'<div class="eyebrow">Mailand · Lombardei · RE/MAX-Netzwerk in Italien</div>',
        re.DOTALL,
    ),
    "fr": re.compile(
        r'<div class="hero-agent reveal">\s*'
        r'<img src="foto\.jpg" alt="Maurizio Piraino" width="56" height="56"[^/]*/>\s*'
        r"<div>\s*"
        r"<strong>Maurizio Piraino</strong>\s*"
        r"<span>Conseiller acheteurs et investisseurs · RE/MAX</span>\s*"
        r"</div>\s*"
        r"</div>\s*"
        r'<div class="eyebrow">Milan · Lombardie · réseau RE/MAX en Italie</div>',
        re.DOTALL,
    ),
    "zh": re.compile(
        r'<div class="hero-agent reveal">\s*'
        r'<img src="/foto\.jpg" alt="Maurizio Piraino" width="56" height="56"[^/]*/>\s*'
        r"<div>\s*"
        r"<strong>Maurizio Piraino</strong>\s*"
        r"<span>购房者与投资者顾问 · RE/MAX</span>\s*"
        r"</div>\s*"
        r"</div>\s*"
        r'<div class="eyebrow">米兰 · 买房与卖房 · RE/MAX 意大利网络</div>',
        re.DOTALL,
    ),
}

H1_REPLACEMENTS = {
    "de": (
        "<h1>Berater für Immobilienkäufer und Investoren</h1>",
        "<h1>Kaufen und investieren mit Analyse — nicht nach Gefühl.</h1>",
    ),
    "fr": (
        "<h1>Conseiller pour acheteurs et investisseurs immobiliers</h1>",
        "<h1>Achetez et investissez avec analyse, pas au feeling.</h1>",
    ),
    "zh": (
        "<h1>买房、投资与卖房房地产顾问</h1>",
        "<h1>用分析买房与投资，而不是凭感觉。</h1>",
    ),
}

TITLE_REPLACEMENTS = {
    "de": [
        (
            "<title>Berater für Immobilienkäufer und Investoren | Maurizio Piraino</title>",
            "<title>Maurizio Piraino | Berater für Käufer und Investoren · Mailand</title>",
        ),
        (
            'content="RE/MAX-Immobilienberater Mailand | Immobilienbewertung"',
            'content="Maurizio Piraino | Berater für Käufer und Investoren · Mailand"',
        ),
    ],
    "fr": [
        (
            "<title>Conseiller acheteurs et investisseurs immobiliers | Maurizio Piraino</title>",
            "<title>Maurizio Piraino | Conseiller acheteurs et investisseurs · Milan</title>",
        ),
        (
            'content="Agent immobilier RE/MAX Milan | Estimation immobilière"',
            'content="Maurizio Piraino | Conseiller acheteurs et investisseurs · Milan"',
        ),
    ],
    "zh": [
        (
            "<title>买房与卖房顾问 | Maurizio Piraino</title>",
            "<title>Maurizio Piraino | 购房者与投资者顾问 · 米兰</title>",
        ),
        (
            'content="买房、投资与卖房房地产顾问 | Piraino"',
            'content="Maurizio Piraino | 购房者与投资者顾问 · 米兰"',
        ),
    ],
}


def patch_home_hero(html: str, lang: str) -> str:
    if lang not in OLD_HERO_RE:
        return html
    new = HERO_BLOCKS[lang]
    html2, n = OLD_HERO_RE[lang].subn(new.rstrip() + "\n", html, count=1)
    if n == 0:
        print(f"  WARN: hero block not matched for {lang}")
        return html
    html = html2
    old_h1, new_h1 = H1_REPLACEMENTS[lang]
    html = html.replace(old_h1, new_h1, 1)
    for a, b in TITLE_REPLACEMENTS[lang]:
        html = html.replace(a, b, 1)
    # bump CSS cache
    html = html.replace(
        'consultant-home.css?v=20260735',
        'consultant-home.css?v=20260738',
    )
    html = html.replace(
        'consultant-home.css?v=20260715b',
        'consultant-home.css?v=20260738',
    )
    html = html.replace('site-nav.css?v=20260736', 'site-nav.css?v=20260738')
    return html


# --- EN / buyer Milan hero touch -------------------------------------------

def patch_buyer_milan_en(html: str) -> str:
    if "hero-brand-mark" not in html:
        html = html.replace(
            '<span class="section-kicker" style="color:var(--gold)">Property Finding · Milan</span>',
            '<p class="hero-brand-mark" style="margin-bottom:8px">Maurizio Piraino</p>\n'
            '          <span class="section-kicker" style="color:var(--gold)">Property Finding · Milan</span>',
            1,
        )
    html = html.replace(
        '<div class="buyer-trust-row"><div class="trust"><strong>OMI</strong><span>Price based on official data</span></div><div class="trust"><strong>RE/MAX</strong><span>Access to the MLS network</span></div><div class="trust"><strong>Surveyor</strong><span>Real technical checks</span></div></div>',
        '<div class="buyer-trust-row"><div class="trust"><strong>You</strong><span>Direct contact with me</span></div><div class="trust"><strong>Surveyor</strong><span>Real technical checks</span></div><div class="trust"><strong>RE/MAX</strong><span>Network support</span></div></div>',
        1,
    )
    html = html.replace(
        '<div class="container buyer-stats-grid"><div><strong>OMI</strong><span>Dati ufficiali Agenzia Entrate</span></div><div><strong>24h</strong><span>Risposta alla tua richiesta</span></div><div><strong>✓</strong><span>Nessun obbligo di incarico</span></div><div><strong>RE/MAX</strong><span>Rete internazionale</span></div></div>',
        '<div class="container buyer-stats-grid"><div><strong>Maurizio</strong><span>Direct contact</span></div><div><strong>24h</strong><span>Personal reply</span></div><div><strong>✓</strong><span>No mandate obligation</span></div><div><strong>RE/MAX</strong><span>Network support</span></div></div>',
        1,
    )
    html = html.replace(
        "<h2>Start Property Finding</h2>",
        "<h2>Let's talk</h2>",
        1,
    )
    html = html.replace(
        "<ul class=\"buyer-hero-list\"><li>OMI analysis across Milan and province</li><li>Technical checks before you offer</li><li>Access to the RE/MAX network</li></ul>",
        "<ul class=\"buyer-hero-list\"><li>Micro-area price analysis</li><li>Technical checks before you offer</li><li>RE/MAX network when needed</li></ul>",
        1,
    )
    html = html.replace(
        'consultant-home.css?v=20260715b',
        'consultant-home.css?v=20260738',
    )
    html = html.replace(
        'consultant-home.css?v=20260735',
        'consultant-home.css?v=20260738',
    )
    return html


def patch_buyer_milan_de(html: str) -> str:
    if "hero-brand-mark" not in html:
        html = re.sub(
            r'(<span class="section-kicker"[^>]*>Property Finding · Mailand</span>)',
            r'<p class="hero-brand-mark" style="margin-bottom:8px">Maurizio Piraino</p>\n          \1',
            html,
            count=1,
        )
        # DE may use German kicker
        if "hero-brand-mark" not in html:
            html = re.sub(
                r'(<div class="buyer-hero-pro-copy[^"]*"[^>]*>\s*)',
                r'\1<p class="hero-brand-mark" style="margin-bottom:8px">Maurizio Piraino</p>\n          ',
                html,
                count=1,
            )
    return html


def patch_buyer_milan_fr(html: str) -> str:
    if "hero-brand-mark" not in html:
        html = re.sub(
            r'(<div class="buyer-hero-pro-copy[^"]*"[^>]*>\s*)',
            r'\1<p class="hero-brand-mark" style="margin-bottom:8px">Maurizio Piraino</p>\n          ',
            html,
            count=1,
        )
    return html


def detect_lang(path: Path) -> str:
    parts = path.parts
    for p in parts:
        if p in {"en", "de", "fr", "zh"}:
            return p
    return "it"


def process_file(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    original = html
    lang = detect_lang(path)

    html = patch_topbars(html)
    html = patch_nav_remax(html, lang)
    html = patch_path_and_kickers(html, lang)

    rel = path.relative_to(ROOT).as_posix()
    if rel in {"de/index.html", "fr/index.html", "zh/index.html"}:
        html = patch_home_hero(html, lang)

    if rel == "en/buy-home-milan/index.html":
        html = patch_buyer_milan_en(html)
    if rel == "de/haus-kaufen-milan/index.html":
        html = patch_buyer_milan_de(html)
    if rel == "fr/acheter-maison-milan/index.html":
        html = patch_buyer_milan_fr(html)

    # Soft: bump nav CSS when we touched the file
    if html != original:
        html = html.replace("site-nav.css?v=20260736", "site-nav.css?v=20260738")

    if html != original:
        path.write_text(html, encoding="utf-8")
        return True
    return False


def main() -> None:
    # All HTML under language roots + IT province/buyer pages still RE/MAX-first
    targets: list[Path] = []
    for pattern in (
        "de/**/*.html",
        "fr/**/*.html",
        "zh/**/*.html",
        "en/**/*.html",
        "comprare-casa*/**/index.html",
        "comprare-casa/**/index.html",
        "bergamo/index.html",
        "brescia/index.html",
        "como/index.html",
        "cremona/index.html",
        "lecco/index.html",
        "lodi/index.html",
        "mantova/index.html",
        "monza/index.html",
        "pavia/index.html",
        "sondrio/index.html",
        "varese/index.html",
        "vendere-casa/**/index.html",
        "vendere-casa-*/**/index.html",
    ):
        targets.extend(ROOT.glob(pattern))

    # Deduplicate
    seen = set()
    unique: list[Path] = []
    for p in targets:
        rp = p.resolve()
        if rp in seen or not p.is_file():
            continue
        seen.add(rp)
        unique.append(p)

    changed = []
    for p in sorted(unique):
        if process_file(p):
            changed.append(p.relative_to(ROOT).as_posix())

    print(f"Updated {len(changed)} files")
    for c in changed:
        print(f"  {c}")


if __name__ == "__main__":
    main()
