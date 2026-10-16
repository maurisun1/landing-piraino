#!/usr/bin/env python3
"""Build FAQPage JSON-LD from the FAQ the visitor can read.

Visible source of truth: every <details> that is not the language switcher.
The question is the <summary> text; the answer is the rest of the <details>,
with tags removed and whitespace collapsed. Schema questions that are not on
the page are dropped. Pages with visible FAQ and no FAQPage get one. Pages
with no visible FAQ lose any FAQPage node.

Run without flags to rewrite HTML. `--check` exits 1 when schema and visible
FAQ differ (used in CI). There is no HTML rewrite at deploy time: GitHub Pages
serves the files this script writes.
"""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_RE = re.compile(
    r'(<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)',
    re.I | re.S,
)
SKIP_PREFIXES = (".github/", "tools/", "seo/")


def norm(text: str) -> str:
    return " ".join(text.split())


class FAQExtractor(HTMLParser):
    """Collect non-language-switcher <details> in document order."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.faqs: list[tuple[str, str]] = []
        self._depth = 0
        self._is_faq = False
        self._in_summary = False
        self._summary_depth = 0
        self._summary: list[str] = []
        self._answer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k: (v or "") for k, v in attrs}
        if tag == "details" and self._depth == 0:
            classes = attr.get("class", "").split()
            self._is_faq = "lang-switcher" not in classes
            self._summary = []
            self._answer = []
            self._in_summary = False
            self._summary_depth = 0
            self._depth = 1
            return
        if self._depth == 0:
            return
        self._depth += 1
        if tag == "summary" and not self._in_summary and not self._summary:
            self._in_summary = True
            self._summary_depth = self._depth
        elif self._is_faq and not self._in_summary and tag == "br":
            self._answer.append(" ")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if self._depth == 0:
            return
        if tag == "summary" and self._in_summary and self._depth == self._summary_depth:
            self._in_summary = False
            self._summary_depth = 0
        if tag == "details" and self._depth == 1:
            if self._is_faq:
                question = norm("".join(self._summary))
                answer = norm("".join(self._answer))
                if question:
                    self.faqs.append((question, answer))
            self._depth = 0
            self._is_faq = False
            return
        self._depth -= 1

    def handle_data(self, data: str) -> None:
        if self._depth == 0 or not self._is_faq:
            return
        if self._in_summary:
            self._summary.append(data)
        else:
            self._answer.append(data)


def visible_faqs(html: str) -> list[tuple[str, str]]:
    parser = FAQExtractor()
    parser.feed(html)
    parser.close()
    return parser.faqs


def is_faq(node: object) -> bool:
    if not isinstance(node, dict):
        return False
    kind = node.get("@type")
    if kind == "FAQPage":
        return True
    return isinstance(kind, list) and "FAQPage" in kind


def entities_from(faqs: list[tuple[str, str]]) -> list[dict]:
    return [
        {
            "@type": "Question",
            "name": question,
            "acceptedAnswer": {"@type": "Answer", "text": answer},
        }
        for question, answer in faqs
    ]


def schema_faqs(data: object) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []

    def walk(node: object) -> None:
        if isinstance(node, dict):
            if is_faq(node):
                for q in node.get("mainEntity") or []:
                    if not isinstance(q, dict):
                        continue
                    ans = q.get("acceptedAnswer") or {}
                    text = ans.get("text", "") if isinstance(ans, dict) else ""
                    found.append((norm(str(q.get("name", ""))), norm(str(text))))
                return
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(data)
    return found


def iter_faq_spans(raw: str):
    decoder = json.JSONDecoder()
    index = 0
    while True:
        start = raw.find("{", index)
        if start < 0:
            return
        try:
            obj, end = decoder.raw_decode(raw, start)
        except json.JSONDecodeError:
            index = start + 1
            continue
        if is_faq(obj):
            yield start, end, obj
        index = start + 1


def render_faq(obj: dict, span: str) -> str:
    """Re-serialize one FAQPage object, matching the span's existing style."""
    ensure_ascii = "\\u" in span
    pretty = re.match(r"\{\n( +)\"", span)
    if pretty:
        extra = max(0, len(pretty.group(1)) - 2)
        dumped = json.dumps(obj, ensure_ascii=ensure_ascii, indent=2)
        if extra:
            dumped = "\n".join(
                line if i == 0 else (" " * extra) + line
                for i, line in enumerate(dumped.split("\n"))
            )
        return dumped
    if "\n" not in span:
        spaced = re.search(r'": ', span) is not None
        separators = (", ", ": ") if spaced else (",", ":")
        return json.dumps(obj, ensure_ascii=ensure_ascii, separators=separators)

    q_indent_m = re.search(r'\n( *)\{"@type":"Question"', span)
    q_indent = q_indent_m.group(1) if q_indent_m else ""
    close_m = re.search(r"\n( *)\]\}", span)
    close_indent = close_m.group(1) if close_m else ""
    questions = [
        json.dumps(q, ensure_ascii=ensure_ascii, separators=(",", ":"))
        for q in obj.get("mainEntity") or []
    ]
    head = {k: v for k, v in obj.items() if k != "mainEntity"}
    head_json = json.dumps(head, ensure_ascii=ensure_ascii, separators=(",", ":"))
    if head_json == "{}":
        prefix = '{"mainEntity":[\n'
    else:
        prefix = head_json[:-1] + ',"mainEntity":[\n'
    body = (",\n" + q_indent).join(questions)
    return prefix + q_indent + body + "\n" + close_indent + "]}"


def replace_faq_object(raw: str, faqs: list[tuple[str, str]]) -> str:
    spans = list(iter_faq_spans(raw))
    if not spans:
        return raw
    start, end, obj = spans[0]
    if schema_faqs(obj) == faqs:
        return raw
    updated = dict(obj)
    updated["mainEntity"] = entities_from(faqs)
    rendered = render_faq(updated, raw[start:end])
    # Re-parse so a style mismatch cannot ship invalid JSON.
    json.loads(rendered)
    return raw[:start] + rendered + raw[end:]


def new_faq_script(faqs: list[tuple[str, str]]) -> str:
    payload = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities_from(faqs),
    }
    body = json.dumps(payload, ensure_ascii=False, indent=2)
    return '<script type="application/ld+json">\n' + body + "\n</script>\n"


def drop_faq_nodes(data: object) -> object | None:
    if isinstance(data, dict):
        if is_faq(data):
            return None
        if isinstance(data.get("@graph"), list):
            graph = [n for n in data["@graph"] if not is_faq(n)]
            if not graph:
                return None
            data = dict(data)
            data["@graph"] = graph
        return data
    if isinstance(data, list):
        kept = [n for item in data if (n := drop_faq_nodes(item)) is not None]
        return kept
    return data


def render_script_body(data: object, raw: str) -> str:
    ensure_ascii = "\\u" in raw
    stripped = raw.strip()
    if "\n" not in stripped:
        spaced = re.search(r'": ', stripped) is not None
        separators = (", ", ": ") if spaced else (",", ":")
        return json.dumps(data, ensure_ascii=ensure_ascii, separators=separators)
    pretty = re.match(r"\{\n( +)\"", stripped)
    extra = max(0, len(pretty.group(1)) - 2) if pretty else 0
    dumped = json.dumps(data, ensure_ascii=ensure_ascii, indent=2)
    if extra:
        dumped = "\n".join(
            line if i == 0 else (" " * extra) + line
            for i, line in enumerate(dumped.split("\n"))
        )
    leading = raw[: len(raw) - len(raw.lstrip())]
    trailing = raw[len(raw.rstrip()) :]
    return leading + dumped + trailing


def sync_html(html: str) -> str:
    faqs = visible_faqs(html)
    matches = list(SCRIPT_RE.finditer(html))
    faq_match = None
    for match in matches:
        if "FAQPage" in match.group(2):
            faq_match = match
            break

    if faqs:
        if faq_match is None:
            block = new_faq_script(faqs)
            if "</head>" not in html:
                raise ValueError("page has visible FAQ but no </head>")
            return html.replace("</head>", block + "</head>", 1)
        inner = faq_match.group(2)
        new_inner = replace_faq_object(inner, faqs)
        if new_inner == inner:
            return html
        return html[: faq_match.start(2)] + new_inner + html[faq_match.end(2) :]

    if faq_match is None:
        return html
    inner = faq_match.group(2)
    try:
        data = json.loads(inner)
    except json.JSONDecodeError:
        return html
    kept = drop_faq_nodes(data)
    if kept is None:
        start = faq_match.start()
        end = faq_match.end()
        # Drop a single trailing newline left by the removed script.
        if end < len(html) and html[end] == "\n":
            end += 1
        return html[:start] + html[end:]
    new_inner = render_script_body(kept, inner)
    return html[: faq_match.start(2)] + new_inner + html[faq_match.end(2) :]


def page_paths() -> list[Path]:
    pages = []
    for path in sorted(ROOT.rglob("index.html")):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(SKIP_PREFIXES):
            continue
        pages.append(path)
    return pages


def schema_in(html: str) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for match in SCRIPT_RE.finditer(html):
        if "FAQPage" not in match.group(2):
            continue
        try:
            data = json.loads(match.group(2))
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid FAQPage JSON: {exc}") from exc
        found.extend(schema_faqs(data))
    return found


def check_page(path: Path) -> list[str]:
    html = path.read_text(encoding="utf-8")
    visible = visible_faqs(html)
    try:
        schema = schema_in(html)
    except ValueError as exc:
        return [f"{path.relative_to(ROOT)}: {exc}"]
    if visible == schema:
        return []
    rel = path.relative_to(ROOT).as_posix()
    lines = [f"{rel}: visible {len(visible)} vs schema {len(schema)}"]
    vq = [q for q, _ in visible]
    sq = [q for q, _ in schema]
    for q in sq:
        if q not in vq:
            lines.append(f"  schema only: {q}")
    for q in vq:
        if q not in sq:
            lines.append(f"  visible only: {q}")
    return lines


def main(argv: list[str]) -> int:
    check = "--check" in argv
    problems: list[str] = []
    changed = 0
    for path in page_paths():
        html = path.read_text(encoding="utf-8")
        try:
            updated = sync_html(html)
        except ValueError as exc:
            problems.append(f"{path.relative_to(ROOT)}: {exc}")
            continue
        if check:
            if updated != html:
                problems.extend(check_page(path) or [f"{path.relative_to(ROOT)}: FAQ schema out of date"])
            continue
        if updated != html:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            # The rewrite must satisfy the check on the file just written.
            problems.extend(check_page(path))
    if problems:
        print("\n".join(problems))
        return 1
    if check:
        print(f"FAQ schema matches visible FAQ on {len(page_paths())} pages")
    else:
        print(f"updated {changed} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
