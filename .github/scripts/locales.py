"""Central locale routing for mauriziopiraino.it."""

from __future__ import annotations

LANGS = ("it", "en", "de", "fr")

LANG_LABELS = {
    "it": "IT",
    "en": "EN",
    "de": "DE",
    "fr": "FR",
}

LANG_NAMES = {
    "it": "Italiano",
    "en": "English",
    "de": "Deutsch",
    "fr": "Français",
}

SWITCHER_ARIA = {
    "it": "Seleziona lingua",
    "en": "Choose language",
    "de": "Sprache wählen",
    "fr": "Choisir la langue",
}

# Compact SVG flags (3:2 ratio)
FLAGS = {
    "it": (
        '<svg class="lang-flag" viewBox="0 0 18 12" aria-hidden="true">'
        '<rect width="6" height="12" fill="#009246"/>'
        '<rect x="6" width="6" height="12" fill="#fff"/>'
        '<rect x="12" width="6" height="12" fill="#CE2B37"/>'
        "</svg>"
    ),
    "en": (
        '<svg class="lang-flag" viewBox="0 0 18 12" aria-hidden="true">'
        '<rect width="18" height="12" fill="#012169"/>'
        '<path fill="#fff" d="M0 0l18 12M18 0L0 12" stroke="#fff" stroke-width="2.2"/>'
        '<path fill="none" stroke="#C8102E" stroke-width="1.2" d="M0 0l18 12M18 0L0 12"/>'
        '<path fill="#fff" d="M8 0h2v12H8zM0 5h18v2H0z"/>'
        '<path fill="#C8102E" d="M9 0h1v12H9zM0 5.5h18v1H0z"/>'
        "</svg>"
    ),
    "de": (
        '<svg class="lang-flag" viewBox="0 0 18 12" aria-hidden="true">'
        '<rect width="18" height="4" fill="#000"/>'
        '<rect y="4" width="18" height="4" fill="#DD0000"/>'
        '<rect y="8" width="18" height="4" fill="#FFCE00"/>'
        "</svg>"
    ),
    "fr": (
        '<svg class="lang-flag" viewBox="0 0 18 12" aria-hidden="true">'
        '<rect width="6" height="12" fill="#002395"/>'
        '<rect x="6" width="6" height="12" fill="#fff"/>'
        '<rect x="12" width="6" height="12" fill="#ED2939"/>'
        "</svg>"
    ),
}

OG_LOCALE = {
    "it": "it_IT",
    "en": "en_GB",
    "de": "de_DE",
    "fr": "fr_FR",
}

HTML_LANG = {
    "it": "it",
    "en": "en",
    "de": "de",
    "fr": "fr",
}

CITY_EN = {
    "milano": "milan",
    "monza": "monza",
    "bergamo": "bergamo",
    "brescia": "brescia",
    "como": "como",
    "varese": "varese",
    "lecco": "lecco",
    "sondrio": "sondrio",
    "cremona": "cremona",
    "lodi": "lodi",
    "mantova": "mantova",
    "pavia": "pavia",
}

CITY_LABELS_EN = {
    "milan": "Milan", "bergamo": "Bergamo", "brescia": "Brescia", "como": "Como",
    "varese": "Varese", "lecco": "Lecco", "monza": "Monza and Brianza",
    "sondrio": "Sondrio", "cremona": "Cremona", "lodi": "Lodi", "mantova": "Mantova", "pavia": "Pavia",
}
CITY_LABELS_DE = {
    "milan": "Mailand", "bergamo": "Bergamo", "brescia": "Brescia", "como": "Como",
    "varese": "Varese", "lecco": "Lecco", "monza": "Monza und Brianza",
    "sondrio": "Sondrio", "cremona": "Cremona", "lodi": "Lodi", "mantova": "Mantova", "pavia": "Pavia",
}
CITY_LABELS_FR = {
    "milan": "Milan", "bergamo": "Bergame", "brescia": "Bresse", "como": "Côme",
    "varese": "Varèse", "lecco": "Lecco", "monza": "Monza et Brianza",
    "sondrio": "Sondrio", "cremona": "Crémone", "lodi": "Lodi", "mantova": "Mantoue", "pavia": "Pavie",
}


def en_slug(slug: str) -> str:
    return CITY_EN.get(slug, slug)


def city_label(slug: str, lang: str) -> str:
    if lang == "it":
        from buyer_provinces import LOMBARD_PROVINCES
        for s, it_name, _en in LOMBARD_PROVINCES:
            if s == slug:
                return it_name
        return slug.title()
    es = en_slug(slug)
    table = {"en": CITY_LABELS_EN, "de": CITY_LABELS_DE, "fr": CITY_LABELS_FR}[lang]
    return table.get(es, es.title())


def buyer_hub_url(lang: str) -> str:
    return {
        "it": "/comprare-casa/",
        "en": "/en/buy-home/",
        "de": "/de/haus-kaufen/",
        "fr": "/fr/acheter-maison/",
    }[lang]


def seller_hub_url(lang: str) -> str:
    return {
        "it": "/vendere-casa/",
        "en": "/vendere-casa/",  # no EN seller hub yet — share IT hub
        "de": "/de/haus-verkaufen/",
        "fr": "/fr/vendre-maison/",
    }[lang]


def buyer_province_url(slug: str, lang: str) -> str:
    es = en_slug(slug)
    if lang == "it":
        return "/comprare-casa-milano/" if slug == "milano" else f"/comprare-casa-{slug}/"
    if lang == "en":
        return f"/en/buy-home-{es}/"
    if lang == "de":
        return f"/de/haus-kaufen-{es}/"
    if lang == "fr":
        return f"/fr/acheter-maison-{es}/"
    raise ValueError(lang)


def seller_url(slug: str, lang: str) -> str:
    if lang == "it":
        return "/" if slug == "milano" else f"/{slug}/"
    if lang == "de":
        return "/de/" if slug == "milano" else f"/de/{slug}/"
    if lang == "fr":
        return "/fr/" if slug == "milano" else f"/fr/{slug}/"
    # No dedicated EN seller pages — link to EN buyer for same province.
    return buyer_province_url(slug, "en")


def buyer_page_path(slug: str, lang: str) -> str:
    url = buyer_province_url(slug, lang)
    return url.strip("/") + "/index.html"


def seller_page_path(slug: str, lang: str) -> str:
    if lang == "it":
        return "index.html" if slug == "milano" else f"{slug}/index.html"
    if lang in ("de", "fr"):
        prefix = lang
        return f"{prefix}/index.html" if slug == "milano" else f"{prefix}/{slug}/index.html"
    raise ValueError(f"No seller page path for lang={lang}")


def buyer_hub_path(lang: str) -> str:
    return buyer_hub_url(lang).strip("/") + "/index.html"


def alternate_urls(slug: str, *, hub: bool = False) -> dict[str, str]:
    base = "https://mauriziopiraino.it"
    if hub:
        return {lang: f"{base}{buyer_hub_url(lang)}" for lang in LANGS}
    return {lang: f"{base}{buyer_province_url(slug, lang)}" for lang in LANGS}


def render_lang_links(current: str, urls: dict[str, str], *, aria_lang: str = "it") -> str:
    aria = SWITCHER_ARIA.get(aria_lang, SWITCHER_ARIA["en"])
    parts = [f'<div class="lang-switcher" role="group" aria-label="{aria}">']
    for lang in LANGS:
        label = LANG_LABELS[lang]
        name = LANG_NAMES[lang]
        flag = FLAGS[lang]
        if lang == current:
            parts.append(
                f'<span class="lang-option lang-option-active" aria-current="true" title="{name}">'
                f'{flag}<span class="lang-code">{label}</span></span>'
            )
        else:
            parts.append(
                f'<a href="{urls[lang]}" class="lang-option" hreflang="{lang}" title="{name}">'
                f'{flag}<span class="lang-code">{label}</span></a>'
            )
    parts.append("</div>")
    return "\n            ".join(parts)


def seller_lang_urls(slug: str) -> dict[str, str]:
    return {
        "it": seller_url(slug, "it"),
        "en": buyer_province_url(slug, "en"),
        "de": seller_url(slug, "de"),
        "fr": seller_url(slug, "fr"),
    }


def buyer_lang_urls(slug: str) -> dict[str, str]:
    return {lang: buyer_province_url(slug, lang) for lang in LANGS}


def hub_lang_urls() -> dict[str, str]:
    return {lang: buyer_hub_url(lang) for lang in LANGS}
