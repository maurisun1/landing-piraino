#!/usr/bin/env python3
"""Audit DE/FR noindex pages for completeness; optionally reindex complete ones."""
from __future__ import annotations

import argparse
import html as H
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IT_ONLY = re.compile(
    r"\b(vendere|comprare|valutazione|immobile|immobili|consulenza|richiedi|proprietà|"
    r"appartamento|senza obbligo|nessun obbligo|acquirenti|investitori|"
    r"prenota|scrivimi|analisi riservata|incarico)\b",
    re.I,
)


def analyze(path: Path) -> dict:
    t = path.read_text(encoding="utf-8", errors="ignore")
    robots_m = re.search(r'name=["\']robots["\'][^>]*content=["\']([^"\']+)', t)
    robots = robots_m.group(1) if robots_m else ""
    title_m = re.search(r"<title>([^<]+)", t)
    title = title_m.group(1) if title_m else ""
    h1_m = re.search(r"<h1[^>]*>([\s\S]*?)</h1>", t)
    h1 = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h1_m.group(1) if h1_m else "")).strip()
    desc_m = re.search(r'name=["\']description["\'][^>]*content=["\']([^"\']*)', t)
    desc = H.unescape(desc_m.group(1)) if desc_m else ""
    main = re.search(r"<main[\s\S]*?</main>", t, re.I)
    body = main.group(0) if main else t
    body = re.sub(r"<script[\s\S]*?</script>", " ", body, flags=re.I)
    body = re.sub(r"<style[\s\S]*?</style>", " ", body, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", body)
    words = re.findall(r"[\wàèéìòùäöüßâêîôûç']+", text, flags=re.I)
    it_hits = IT_ONLY.findall(text)
    reasons = []
    if len(words) < 700:
        reasons.append(f"words={len(words)}<700")
    if len(it_hits) > 5:
        reasons.append(f"IT tokens={len(it_hits)}")
    if len(desc) < 120:
        reasons.append(f"desc_len={len(desc)}<120")
    if not h1:
        reasons.append("missing H1")
    if re.search(r"\b(Vendere|Comprare|Consulente)\b", title):
        reasons.append("IT title")
    return {
        "path": "/" + path.parent.relative_to(ROOT).as_posix() + "/",
        "file": str(path.relative_to(ROOT)),
        "robots": robots,
        "words": len(words),
        "title": title,
        "title_len": len(title),
        "h1": h1,
        "desc": desc,
        "desc_len": len(desc),
        "it_hits": len(it_hits),
        "it_samples": sorted(set(x.lower() for x in it_hits))[:8],
        "complete": not reasons,
        "missing": reasons,
    }


def set_robots(path: Path, value: str) -> bool:
    text = path.read_text(encoding="utf-8")
    new, n = re.subn(
        r'(<meta\s+name=["\']robots["\']\s+content=["\'])([^"\']*)(["\'])',
        rf"\g<1>{value}\g<3>",
        text,
        count=1,
        flags=re.I,
    )
    if n == 0:
        return False
    path.write_text(new, encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reindex-complete", action="store_true")
    ap.add_argument("--json-out", type=Path, default=None)
    args = ap.parse_args()

    rows = []
    for lang in ("de", "fr"):
        for path in sorted((ROOT / lang).rglob("index.html")):
            row = analyze(path)
            if "noindex" not in row["robots"].lower():
                continue
            rows.append(row)

    complete = [r for r in rows if r["complete"]]
    incomplete = [r for r in rows if not r["complete"]]

    print(f"DE/FR noindex: {len(rows)} | complete={len(complete)} | incomplete={len(incomplete)}")
    print("\n=== COMPLETE (eligible for index) ===")
    for r in complete:
        print(f"{r['path']}\twords={r['words']}\ttitle={r['title_len']}\tdesc={r['desc_len']}\tit={r['it_hits']}")
    print("\n=== INCOMPLETE (keep noindex) ===")
    for r in incomplete:
        print(f"{r['path']}\twords={r['words']}\tdesc={r['desc_len']}\tmissing={'; '.join(r['missing'])}")

    if args.reindex_complete:
        for r in complete:
            ok = set_robots(ROOT / r["file"], "index, follow")
            print(("reindexed" if ok else "FAILED"), r["path"])

    if args.json_out:
        args.json_out.write_text(json.dumps({"complete": complete, "incomplete": incomplete}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
