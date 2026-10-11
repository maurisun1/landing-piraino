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

REDIRECTS: dict[str, str] = {}
for c in DROP_CITIES:
    REDIRECTS[f"/de/{c}/"] = f"/{c}/"  # venditori -> pagina IT città
    REDIRECTS[f"/fr/{c}/"] = f"/{c}/"
    REDIRECTS[f"/de/haus-kaufen-{c}/"] = f"/en/buy-home-{c}/"  # acquirenti -> EN città
    REDIRECTS[f"/fr/acheter-maison-{c}/"] = f"/en/buy-home-{c}/"

STUB = """<!doctype html>
<html lang="{lang}">
<head>
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
