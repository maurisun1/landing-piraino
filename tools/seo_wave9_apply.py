#!/usr/bin/env python3
"""Apply SEO wave9 structural fixes (zh unlink, redirects noindex, EN prune, footer VCT)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://mauriziopiraino.it"

VCT = {
    "milano": "https://valorecasatua.it/guide/prezzi-mq-milano/",
    "bergamo": "https://valorecasatua.it/guide/prezzi-mq-bergamo/",
    "brescia": "https://valorecasatua.it/guide/prezzi-mq-brescia/",
    "como": "https://valorecasatua.it/guide/prezzi-mq-como/",
    "varese": "https://valorecasatua.it/guide/prezzi-mq-varese/",
    "lecco": "https://valorecasatua.it/guide/prezzi-mq-lecco/",
    "cremona": "https://valorecasatua.it/guide/prezzi-mq-cremona/",
    "lodi": "https://valorecasatua.it/guide/prezzi-mq-lodi/",
    "mantova": "https://valorecasatua.it/guide/prezzi-mq-mantova/",
    "pavia": "https://valorecasatua.it/guide/prezzi-mq-pavia/",
    "sondrio": "https://valorecasatua.it/guide/prezzi-mq-sondrio/",
    "monza": "https://valorecasatua.it/guide/prezzi-mq-monza-brianza/",
}

EN_NOINDEX = {
    "en/buy-home-cremona",
    "en/buy-home-mantova",
    "en/buy-home-sondrio",
}

CONTEXT_SNIPPETS = {
    "milano": "Se cerchi un riferimento aggiornato sui valori di zona, la lettura completa è sulla <a href=\"{vct}\">guida Milano di ValoreCasaTua</a>.",
    "bergamo": "Per un quadro dei valori di mercato zona per zona puoi consultare la <a href=\"{vct}\">guida Bergamo su ValoreCasaTua</a>.",
    "brescia": "Se vuoi un riferimento sui valori al mq aggiornati della zona, trovi la guida completa su <a href=\"{vct}\">ValoreCasaTua</a>.",
    "como": "Uno sguardo indipendente alle fasce di zona è sulla <a href=\"{vct}\">guida Como di ValoreCasaTua</a>.",
    "varese": "Per approfondire le fasce di zona puoi leggere la <a href=\"{vct}\">guida Varese su ValoreCasaTua</a>.",
    "lecco": "Un riferimento editoriale sulle fasce di zona è nella <a href=\"{vct}\">guida Lecco di ValoreCasaTua</a>.",
    "cremona": "Per i dati di zona aggiornati puoi partire dalla <a href=\"{vct}\">guida Cremona su ValoreCasaTua</a>.",
    "lodi": "Se ti serve un quadro dei valori di zona, c’è la <a href=\"{vct}\">guida Lodi su ValoreCasaTua</a>.",
    "mantova": "Un approfondimento sulle fasce di zona è disponibile nella <a href=\"{vct}\">guida Mantova di ValoreCasaTua</a>.",
    "pavia": "Per orientarti sui valori di zona puoi consultare la <a href=\"{vct}\">guida Pavia su ValoreCasaTua</a>.",
    "sondrio": "Uno sguardo alle fasce di zona è sulla <a href=\"{vct}\">guida Sondrio di ValoreCasaTua</a>.",
    "monza": "Per un riferimento sulle fasce in Brianza vedi la <a href=\"{vct}\">guida Monza e Brianza su ValoreCasaTua</a>.",
}


def write_redirect(path: Path, dest: str, lang: str = "it") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""<!doctype html>
<html lang="{lang}"><head>
<meta charset="utf-8">
<title>Pagina spostata</title>
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="{dest}">
<meta http-equiv="refresh" content="0; url={dest}">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head><body><p>Questa pagina è stata spostata: <a href="{dest}">vai alla nuova pagina</a>.</p></body></html>
""",
        encoding="utf-8",
    )


def strip_zh_links(html: str) -> str:
    # Remove zh lang-option anchors (dropdown)
    html = re.sub(
        r'\s*<a href="/zh/[^"]*" class="lang-option"[^>]*>[\s\S]*?</a>',
        "",
        html,
        flags=re.I,
    )
    # Remove any other /zh/ anchors outside zh pages
    html = re.sub(r'<a\b[^>]*href=["\'][^"\']*/zh/[^"\']*["\'][^>]*>[\s\S]*?</a>', "", html, flags=re.I)
    # Remove zh-Hans hreflang link tags
    html = re.sub(r'\s*<link[^>]+hreflang=["\']zh[^"\']*["\'][^>]*>\s*', "\n", html, flags=re.I)
    return html


def ensure_noindex(html: str) -> str:
    if re.search(r'name=["\']robots["\']', html, re.I):
        return re.sub(
            r'(name=["\']robots["\']\s+content=["\'])([^"\']*)(["\'])',
            r"\1noindex, follow\3",
            html,
            count=1,
            flags=re.I,
        )
    return html.replace(
        "<head>",
        '<head>\n<meta name="robots" content="noindex, follow">',
        1,
    )


def remove_footer_vct_guides(html: str) -> str:
    # Remove footer rows that are pure VCT guide link lists
    html = re.sub(
        r'<p class="footer-geo-row"><span class="footer-geo-label">Guide prezzi OMI:</span>[\s\S]*?</p>\s*',
        "",
        html,
        flags=re.I,
    )
    html = re.sub(
        r'<p class="footer-geo-row"><span class="footer-geo-label">OMI[- ]Preisguides:</span>[\s\S]*?</p>\s*',
        "",
        html,
        flags=re.I,
    )
    html = re.sub(
        r'<p class="footer-geo-row"><span class="footer-geo-label">OMI price guides:</span>[\s\S]*?</p>\s*',
        "",
        html,
        flags=re.I,
    )
    html = re.sub(
        r'<p class="footer-geo-row"><span class="footer-geo-label">Guides prix OMI:</span>[\s\S]*?</p>\s*',
        "",
        html,
        flags=re.I,
    )
    return html


def remove_home_mesh_vct_block(html: str) -> str:
    # Home mesh "Guide prezzi" is a sitewide-style promo; replace with short contextual sentence without link list in footer sense.
    # Keep one contextual link in the intro paragraph only.
    html = re.sub(
        r'<p class="seo-home-mesh-label">Guide prezzi al mq \(OMI\)</p>'
        r'<p class="seo-home-mesh-links">[\s\S]*?</p>',
        '<p class="seo-home-mesh-label">Approfondimenti di mercato</p>'
        '<p class="seo-home-mesh-links">Per i valori di zona aggiornati rimando alle guide editoriali su '
        '<a href="https://valorecasatua.it/guide/">ValoreCasaTua</a>.</p>',
        html,
        count=1,
    )
    return html


def inject_context_link(html: str, city: str) -> str:
    if city not in VCT:
        return html
    vct = VCT[city]
    if "valorecasatua.it/guide/prezzi-mq" in html and "seo-home-mesh" not in html:
        # already has at least one body VCT guide link — OK if not only in footer
        # but after footer strip, ensure one remains in main
        main = re.search(r"<main[\s\S]*?</main>", html, re.I)
        if main and "valorecasatua.it/guide" in main.group(0):
            return html
    snippet = CONTEXT_SNIPPETS.get(city, CONTEXT_SNIPPETS["milano"]).format(vct=vct)
    para = f"<p class=\"vct-context-link\">{snippet}</p>\n"
    # Insert before FAQ or before footer / seo-related
    for marker in (
        '<section id="faq"',
        '<nav class="seo-related"',
        '<section class="buyer-form-section"',
        "<footer",
    ):
        if marker in html:
            return html.replace(marker, para + marker, 1)
    if "</main>" in html:
        return html.replace("</main>", para + "</main>", 1)
    return html


def city_from_path(rel: str) -> str | None:
    for city in VCT:
        if rel in {f"{city}/index.html", f"comprare-casa-{city}/index.html", f"vendere-casa-{city}/index.html"}:
            return city
        if rel == "vendere-casa-milano/index.html":
            return "milano"
        if rel == "comprare-casa-monza/index.html" or rel == "monza/index.html":
            return "monza"
    return None


def fix_index_html_links(html: str) -> str:
    html = html.replace('href="/index.html"', 'href="/"')
    html = html.replace("href='/index.html'", "href='/'")
    return html


def main() -> None:
    # Task 2: standardize guide redirects
    for city, dest in (
        ("milano", VCT["milano"]),
        ("brescia", VCT["brescia"]),
        ("bergamo", VCT["bergamo"]),
    ):
        write_redirect(ROOT / f"guida-prezzi-mq-{city}" / "index.html", dest, "it")
        print("redirect stub", city)

    # Task 2: add noindex to all refresh stubs
    for p in ROOT.rglob("index.html"):
        if any(x in p.parts for x in [".git", "zh"]):
            continue
        t = p.read_text(encoding="utf-8", errors="ignore")
        if re.search(r'http-equiv=["\']refresh["\']', t, re.I):
            t2 = ensure_noindex(t)
            # Align title if empty-ish
            if p.parent.name.startswith("guida-prezzi-mq-"):
                # already rewritten
                continue
            if t2 != t:
                p.write_text(t2, encoding="utf-8")
                print("noindex refresh", p.relative_to(ROOT))

    # Re-write DE/FR refresh stubs that still miss robots after ensure
    for p in list((ROOT / "de").rglob("index.html")) + list((ROOT / "fr").rglob("index.html")):
        t = p.read_text(encoding="utf-8", errors="ignore")
        if re.search(r'http-equiv=["\']refresh["\']', t, re.I) and "noindex" not in t.lower():
            p.write_text(ensure_noindex(t), encoding="utf-8")
            print("force noindex", p.relative_to(ROOT))

    # Task 5: EN noindex provinces
    for rel in EN_NOINDEX:
        p = ROOT / rel / "index.html"
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8")
        t = ensure_noindex(t)
        p.write_text(t, encoding="utf-8")
        print("EN noindex", rel)

    # Walk all non-zh HTML for zh strip, footer VCT, index.html links, context
    for p in ROOT.rglob("*.html"):
        if ".git" in p.parts:
            continue
        rel = p.relative_to(ROOT).as_posix()
        t = p.read_text(encoding="utf-8", errors="ignore")
        orig = t
        if not rel.startswith("zh/"):
            t = strip_zh_links(t)
        t = fix_index_html_links(t)
        t = remove_footer_vct_guides(t)
        if rel == "index.html":
            t = remove_home_mesh_vct_block(t)
        if rel == "vendere-casa/index.html":
            if "valorecasatua.it" not in re.sub(r"<footer[\s\S]*?</footer>", "", t, flags=re.I):
                snip = (
                    '<p class="vct-context-link">Per una stima orientativa e le guide di zona puoi partire da '
                    '<a href="https://valorecasatua.it/">ValoreCasaTua</a> '
                    '(es. <a href="https://valorecasatua.it/guide/prezzi-mq-milano/">Milano</a>).</p>\n'
                )
                t = t.replace("</main>", snip + "</main>", 1) if "</main>" in t else t + snip
        city = city_from_path(rel)
        if city and not re.search(r'http-equiv=["\']refresh["\']', t, re.I):
            t = inject_context_link(t, city)
        if t != orig:
            p.write_text(t, encoding="utf-8")
            print("updated", rel)

    print("done wave9 structural")


if __name__ == "__main__":
    main()
