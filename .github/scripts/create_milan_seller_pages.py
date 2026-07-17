#!/usr/bin/env python3
"""Restore Milan seller landings at dedicated URLs (homepage is now buyer/investor)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
# Pre-reposition seller Milan pages (before consultant homepage rewrite)
SRC_COMMIT = "81e82ed"

PAGES = {
    "it": {
        "src": "index.html",
        "dest": "vendere-casa-milano/index.html",
        "url": "/vendere-casa-milano/",
        "canonical": "https://mauriziopiraino.it/vendere-casa-milano/",
        "langs": {
            "it": "/vendere-casa-milano/",
            "de": "/de/haus-verkaufen-milan/",
            "fr": "/fr/vendre-maison-milan/",
        },
        "foto": "/foto.jpg",
    },
    "de": {
        "src": "de/index.html",
        "dest": "de/haus-verkaufen-milan/index.html",
        "url": "/de/haus-verkaufen-milan/",
        "canonical": "https://mauriziopiraino.it/de/haus-verkaufen-milan/",
        "langs": {
            "it": "/vendere-casa-milano/",
            "de": "/de/haus-verkaufen-milan/",
            "fr": "/fr/vendre-maison-milan/",
        },
        "foto": "/foto.jpg",
    },
    "fr": {
        "src": "fr/index.html",
        "dest": "fr/vendre-maison-milan/index.html",
        "url": "/fr/vendre-maison-milan/",
        "canonical": "https://mauriziopiraino.it/fr/vendre-maison-milan/",
        "langs": {
            "it": "/vendere-casa-milano/",
            "de": "/de/haus-verkaufen-milan/",
            "fr": "/fr/vendre-maison-milan/",
        },
        "foto": "/foto.jpg",
    },
}


def _run_git_show(path: str) -> str:
    import subprocess

    return subprocess.check_output(
        ["git", "show", f"{SRC_COMMIT}:{path}"],
        cwd=ROOT,
        text=True,
    )


def _patch_meta(html: str, cfg: dict) -> str:
    html = re.sub(
        r'<link rel="canonical" href="[^"]+"\s*/?>',
        f'<link rel="canonical" href="{cfg["canonical"]}" />',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:url" content="[^"]+"\s*/?>',
        f'<meta property="og:url" content="{cfg["canonical"]}" />',
        html,
        count=1,
    )
    # Replace hreflang block (drop EN seller which never existed)
    html = re.sub(
        r'(?:<link rel="alternate" hreflang="[^"]+" href="[^"]+"\s*/?>\s*)+',
        "".join(
            f'<link rel="alternate" hreflang="{lang}" href="https://mauriziopiraino.it{url}" />\n'
            for lang, url in cfg["langs"].items()
        )
        + f'<link rel="alternate" hreflang="x-default" href="https://mauriziopiraino.it{cfg["langs"]["it"]}" />\n',
        html,
        count=1,
    )
    return html


def _fix_asset_paths(html: str, cfg: dict) -> str:
    html = html.replace('src="foto.jpg"', f'src="{cfg["foto"]}"')
    html = html.replace("url('milano.jpg')", "url('/milano.jpg')")
    html = html.replace('href="milano.jpg"', 'href="/milano.jpg"')
    # Brand home stays site root (consultant home)
    return html


def main() -> None:
    for lang, cfg in PAGES.items():
        html = _run_git_show(cfg["src"])
        html = _patch_meta(html, cfg)
        html = _fix_asset_paths(html, cfg)
        dest = ROOT / cfg["dest"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding="utf-8")
        print(f"Wrote {cfg['dest']}")


if __name__ == "__main__":
    main()
