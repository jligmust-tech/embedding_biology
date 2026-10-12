#!/usr/bin/env python3
"""Normalize cross-references across the book.

1. Remove redundant words before a cross-reference (Quarto already renders
   "@eq-x" as "Equation N"), so "Equation (@eq-x)" -> "(@eq-x)",
   "Table @tbl-x" -> "@tbl-x", "Figure @fig-x" -> "@fig-x".
2. Make equation labels globally unique by prefixing each file's eq- labels
   and references with a per-file tag (ch01..ch14, appa..appc), because Quarto
   requires unique cross-reference identifiers book-wide. Figure/table labels
   are already unique and are left alone.

Run with --check to report only.
"""
import re
import sys
import glob
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def prefix_for(filename):
    base = os.path.basename(filename)
    m = re.match(r"^(\d{2})-", base)
    if m:
        return "ch" + m.group(1)
    if base.startswith("appendix-a"):
        return "appa"
    if base.startswith("appendix-b"):
        return "appb"
    if base.startswith("appendix-c"):
        return "appc"
    return None


PREFIX_WORD_SUBS = [
    (re.compile(r"\bFigures?\s+\(@fig-"), "(@fig-"),
    (re.compile(r"\bTables?\s+\(@tbl-"), "(@tbl-"),
    (re.compile(r"\bEquations?\s+\(@eq-"), "(@eq-"),
    (re.compile(r"\bFigures?\s+@fig-"), "@fig-"),
    (re.compile(r"\bTables?\s+@tbl-"), "@tbl-"),
    (re.compile(r"\bEquations?\s+@eq-"), "@eq-"),
]


def process(text, prefix):
    for pat, repl in PREFIX_WORD_SUBS:
        text = pat.sub(repl, text)

    def lbl(m):
        name = m.group(1)
        if name.startswith(prefix + "-"):
            return m.group(0)
        return "{#eq-%s-%s}" % (prefix, name)

    def ref(m):
        name = m.group(1)
        if name.startswith(prefix + "-"):
            return m.group(0)
        return "@eq-%s-%s" % (prefix, name)

    text = re.sub(r"\{#eq-([A-Za-z0-9_-]+)\}", lbl, text)
    text = re.sub(r"@eq-([A-Za-z0-9_-]+)", ref, text)
    return text


def main():
    check = "--check" in sys.argv
    files = sorted(glob.glob(os.path.join(ROOT, "chapters", "*.qmd")))
    total_sub = 0
    unresolved_report = []
    for f in files:
        prefix = prefix_for(f)
        if not prefix:
            continue
        src = open(f).read()
        out = process(src, prefix)
        # per-file resolution check: every @eq- ref must be defined in this file
        labels = set(re.findall(r"\{#(eq-[A-Za-z0-9_-]+)\}", out))
        refs = set(re.findall(r"@(eq-[A-Za-z0-9_-]+)", out))
        missing = sorted(r for r in refs if r not in labels)
        if missing:
            unresolved_report.append((os.path.basename(f), missing))
        if out != src:
            total_sub += 1
            if not check:
                open(f, "w").write(out)
    print("files changed:", total_sub)
    if unresolved_report:
        print("UNRESOLVED per-file eq refs (need cross-file handling):")
        for name, miss in unresolved_report:
            print("  ", name, miss)
    else:
        print("all @eq- references resolve within their own file")


if __name__ == "__main__":
    main()
