#!/usr/bin/env bash
# Consolidate per-chapter bibliography fragments into references.bib.
# Deduplicates by citation key (first definition wins), preserves references.bib.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MAIN="$ROOT/references.bib"
TMP="$(mktemp)"

# Collect keys already present in the main bibliography.
awk -F'[{,]' '/^@/{print $2}' "$MAIN" | sort -u > "$TMP.known"

shopt -s nullglob
for f in "$ROOT"/bib/*.bib; do
  [ "$(basename "$f")" = "README.md" ] && continue
  python3 - "$f" "$MAIN" "$TMP.known" <<'PY'
import re, sys
frag, main, known_path = sys.argv[1], sys.argv[2], sys.argv[3]
known = set(open(known_path).read().split())
text = open(frag).read()
entries = re.split(r'(?m)^(?=@)', text)
kept = []
for e in entries:
    m = re.match(r'@\w+\{([^,]+),', e)
    if not m:
        continue
    key = m.group(1).strip()
    if key in known:
        continue
    kept.append(e.rstrip() + "\n")
    known.add(key)
if kept:
    with open(main, "a") as out:
        out.write("\n% ---- merged from %s ----\n" % frag.split('/')[-1])
        out.write("\n".join(kept))
    open(known_path, "w").write("\n".join(sorted(known)))
    print("merged %d entr%s from %s" % (len(kept), "y" if len(kept)==1 else "ies", frag))
PY
done

echo "Done. Review references.bib and remove any 'merged from' comments you dislike."
