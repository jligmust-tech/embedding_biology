#!/usr/bin/env python3
"""Lightweight integrity checks for the book. Exits non-zero on failure.

Checks:
  1. every citation key `[@key]` resolves in references.bib
  2. every cross-reference `@eq-…`/`@fig-…`/`@tbl-…` resolves to a defined label
  3. all cross-reference labels are globally unique (Quarto requirement)
  4. no leftover TODO / placeholder text
  5. references.bib has balanced braces and no duplicate keys
"""
import re
import sys
import glob
import os
import collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

errors = []
warnings = []

# --- bibliography ---------------------------------------------------------
bib_text = open("references.bib").read()
bib_keys = re.findall(r"(?m)^@\w+\{\s*([^,\s]+)\s*,", bib_text)
bib_set = set(bib_keys)
if len(bib_keys) != len(bib_set):
    dups = [k for k, c in collections.Counter(bib_keys).items() if c > 1]
    errors.append("references.bib has duplicate keys: %s" % dups)
if bib_text.count("{") != bib_text.count("}"):
    errors.append("references.bib has unbalanced braces")

# --- sources --------------------------------------------------------------
files = ["index.qmd"] + sorted(glob.glob("chapters/*.qmd"))
labels = collections.defaultdict(list)
refs = collections.defaultdict(list)
used_keys = set()

for f in files:
    txt = open(f).read()
    if re.search(r"TODO|Placeholder|<!-- *PLACEHOLDER", txt):
        errors.append("%s contains TODO/placeholder text" % f)
    for m in re.finditer(r"\{#((?:eq|fig|tbl|sec)-[A-Za-z0-9_-]+)(?=[\s}])", txt):
        labels[m.group(1)].append(f)
    # strip code so examples like [@key] inside backticks are ignored
    stripped = re.sub(r"`[^`]*`", "", txt)
    stripped = re.sub(r"```.*?```", "", stripped, flags=re.S)
    for m in re.finditer(r"@([A-Za-z][A-Za-z0-9_-]+)", stripped):
        name = m.group(1)
        if name.split("-")[0] in ("eq", "fig", "tbl", "sec"):
            refs[name].append(f)
        else:
            used_keys.add(name)
            if name not in bib_set:
                errors.append("%s cites unknown key @%s" % (f, name))

for name, where in labels.items():
    if len(where) > 1:
        errors.append("label #%s defined in multiple files: %s" % (name, where))
for name, where in refs.items():
    if name not in labels:
        errors.append("dangling reference @%s in %s" % (name, sorted(set(where))))

unused = sorted(bib_set - used_keys)
if unused:
    warnings.append("%d bibliography entries never cited: %s" % (len(unused), unused[:10]))

# --- report ---------------------------------------------------------------
print("files checked:", len(files))
print("bibliography keys:", len(bib_set), "| cited:", len(used_keys & bib_set))
print("cross-ref labels:", len(labels), "| references:", len(refs))
for w in warnings:
    print("WARN:", w)
for e in errors:
    print("ERROR:", e)
print("OK" if not errors else "FAILED (%d errors)" % len(errors))
sys.exit(1 if errors else 0)
