#!/usr/bin/env python3
"""Verify bibliography entries against Crossref.

For each entry in references.bib:
  * if it has a DOI, look it up directly;
  * otherwise run a bibliographic query on title (+ first author).
Compare the returned title (token overlap) and year and classify:
  ok | year-mismatch | title-mismatch | doi-unresolved | no-match

Writes verification/citation-sweep.md. Network-dependent; run sparingly.

Usage: python3 tools/citation_sweep.py [--limit N]
"""
import re
import sys
import json
import time
import difflib
import urllib.parse
import urllib.request

ROOT = "."
BIB = ROOT + "/references.bib"
OUT = ROOT + "/verification/citation-sweep.md"
MAILTO = "jligm@connect.ust.hk"
UA = "embedding_biology-citation-sweep/1.0 (mailto:%s)" % MAILTO


def entries(text):
    for block in re.split(r"(?m)^(?=@)", text):
        m = re.match(r"@\w+\s*\{\s*([^,\s]+)\s*,", block)
        if not m:
            continue
        key = m.group(1)
        def field(name):
            mm = re.search(r"(?ms)^\s*%s\s*=\s*[{\"](.+?)[}\"]\s*,?\s*$" % name, block)
            if not mm:
                mm = re.search(r"(?ms)^\s*%s\s*=\s*[{\"](.*?)[}\"]\s*,?\s*\n" % name, block)
            return re.sub(r"\s+", " ", mm.group(1)).strip() if mm else ""
        yield {
            "key": key,
            "title": field("title"),
            "year": field("year"),
            "doi": field("doi"),
            "author": field("author"),
        }


def norm(s):
    s = re.sub(r"[{}\\]", "", s).lower()
    return re.sub(r"[^a-z0-9 ]+", " ", s)


def similar(a, b):
    a, b = norm(a), norm(b)
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.load(r)


def check(e):
    t, y = e["title"], e["year"][:4]
    if e["doi"]:
        try:
            m = get("https://api.crossref.org/works/" + urllib.parse.quote(e["doi"]))["message"]
        except Exception as ex:
            return "doi-unresolved", "DOI lookup failed (%s)" % type(ex).__name__, ""
        ct = (m.get("title") or [""])[0]
        cy = str((m.get("issued", {}).get("date-parts", [[None]])[0][0]) or "")
        sim = similar(t, ct)
        if sim < 0.72:
            return "title-mismatch", "bib:%s | crossref:%s" % (t[:70], ct[:70]), e["doi"]
        if y and cy and y != cy:
            return "year-mismatch", "bib year %s vs crossref %s" % (y, cy), e["doi"]
        return "ok", "", e["doi"]
    # no DOI: bibliographic query
    q = urllib.parse.quote((t + " " + e["author"].split(" and ")[0]).strip())
    try:
        items = get("https://api.crossref.org/works?rows=3&query.bibliographic=" + q)["message"]["items"]
    except Exception as ex:
        return "no-match", "query failed (%s)" % type(ex).__name__, ""
    if not items:
        return "no-match", "no crossref result", ""
    best = items[0]
    ct = (best.get("title") or [""])[0]
    sim = similar(t, ct)
    if sim >= 0.8:
        return "ok(no-doi)", "crossref: %s" % ct[:70], best.get("DOI", "")
    if sim >= 0.6:
        return "title-mismatch", "bib:%s | crossref:%s" % (t[:60], ct[:60]), best.get("DOI", "")
    return "no-match", "closest: %s" % ct[:70], best.get("DOI", "")


def main():
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    es = list(entries(open(BIB).read()))
    if limit:
        es = es[:limit]
    rows = []
    for i, e in enumerate(es, 1):
        verdict, note, found = check(e)
        rows.append((e["key"], verdict, note, found))
        if verdict != "ok":
            print("%-28s %-15s %s" % (e["key"], verdict, note[:80]))
        time.sleep(0.15)
    from collections import Counter
    c = Counter(r[1] for r in rows)
    with open(OUT, "w") as out:
        out.write("# Citation sweep (Crossref)\n\n")
        out.write("Automated check of all %d bibliography entries against Crossref.\n\n" % len(rows))
        out.write("| verdict | count |\n|---|---|\n")
        for k, v in c.most_common():
            out.write("| %s | %d |\n" % (k, v))
        out.write("\n## Non-`ok` entries\n\n| key | verdict | note | doi/url |\n|---|---|---|---|\n")
        for key, verdict, note, found in rows:
            if verdict != "ok" and verdict != "ok(no-doi)":
                out.write("| `%s` | %s | %s | %s |\n" % (key, verdict, note.replace("|", "\\|"), found))
    print("\nSummary:", dict(c))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
