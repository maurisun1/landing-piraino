#!/usr/bin/env python3
"""Riduce DE/FR alle sole aree con domanda estera (Milano, laghi, Brescia/Garda).
Le altre pagine DE/FR diventano stub di redirect (GitHub Pages non supporta 301:
meta refresh 0 + canonical verso la destinazione, che Google tratta come redirect
permanente). Riscrive anche i link interni verso le nuove destinazioni."""
from __future__ import annotations

import html as H
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://mauriziopiraino.it"
DROP_CITIES = ["bergamo", "cremona", "lodi", "mantova", "monza", "pavia", "sondrio"]
# Pagine EN provinciali in noindex: lo stub DE/FR va all'hub EN, non alla città.
BUYER_HUB_CITIES = {"cremona", "mantova", "sondrio"}
# I link <a> verso quelle EN città vanno alla pagina IT acquirenti, non all'hub.
EN_NOINDEX_LINKS = {
    "/en/buy-home-cremona/": "/comprare-casa-cremona/",
    "/en/buy-home-mantova/": "/comprare-casa-mantova/",
    "/en/buy-home-sondrio/": "/comprare-casa-sondrio/",
}

REDIRECTS: dict[str, str] = {}
for c in DROP_CITIES:
    REDIRECTS[f"/de/{c}/"] = f"/{c}/"  # venditori -> pagina IT città
    REDIRECTS[f"/fr/{c}/"] = f"/{c}/"
    buyer = "/en/buy-home/" if c in BUYER_HUB_CITIES else f"/en/buy-home-{c}/"
    REDIRECTS[f"/de/haus-kaufen-{c}/"] = buyer
    REDIRECTS[f"/fr/acheter-maison-{c}/"] = buyer

STUB = """<!doctype html>
<html lang="{lang}">
<head>
<meta name="robots" content="noindex, follow">
<meta charset="utf-8" />
<title>{title}</title>
<link rel="canonical" href="{abs}" />
<meta http-equiv="refresh" content="0; url={abs}" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<script>location.replace({js});</script>
</head>
<body><p><a href="{abs}">{abs}</a></p></body>
</html>
"""


def main() -> None:
    for src, dst in REDIRECTS.items():
        f = ROOT / src.strip("/") / "index.html"
        assert f.is_file(), src
        assert (ROOT / dst.strip("/") / "index.html").is_file(), dst
        lang = src.split("/")[1]
        abs_ = BASE + dst
        f.write_text(
            STUB.format(lang=lang, title=H.escape("→ " + dst), abs=abs_, js=json.dumps(abs_)),
            encoding="utf-8",
        )
    n = 0
    for f in ROOT.glob("**/*.html"):
        rel = "/" + f.parent.relative_to(ROOT).as_posix() + "/"
        if rel in REDIRECTS:
            continue
        t = f.read_text(encoding="utf-8")
        o = t
        for src, dst in REDIRECTS.items():
            t = re.sub(
                r'href=(["\'])(?:' + re.escape(BASE) + r')?' + re.escape(src) + r"\1",
                lambda m, d=dst: f"href={m.group(1)}{d}{m.group(1)}",
                t,
            )
        for src, dst in EN_NOINDEX_LINKS.items():
            t = re.sub(
                r'(<a\b[^>]*\bhref=(["\']))(?:' + re.escape(BASE) + r')?' + re.escape(src) + r"(\2)",
                lambda m, d=dst: m.group(1) + d + m.group(3),
                t,
            )
        # hreflang residui verso pagine rimosse
        for src in REDIRECTS:
            t = re.sub(
                r'[ \t]*<link\s+rel=["\']alternate["\']\s+hreflang=["\'][^"\']+["\']\s+href=["\']'
                + re.escape(BASE + src) + r'["\']\s*/?>\n?',
                "",
                t,
            )
        # selettore lingua: niente bandiera DE/FR se la pagina non ha versione DE/FR
        t = re.sub(
            r'[ \t]*<a href="(?!/(?:de|fr)/)[^"]*" class="lang-option" hreflang="(?:de|fr)"[^>]*>.*?</a>\n?',
            "",
            t,
        )
        if t != o:
            f.write_text(t, encoding="utf-8")
            n += 1
    (ROOT / "seo" / "defr-redirects.json").write_text(
        json.dumps(REDIRECTS, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"stub redirect: {len(REDIRECTS)} | pagine con link aggiornati: {n}")


if __name__ == "__main__":
    main()
