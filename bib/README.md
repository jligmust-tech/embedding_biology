# Per-chapter bibliography fragments

> **Archived.** The per-chapter fragments have been **consolidated into the
> single canonical [`references.bib`](../references.bib)** (213 entries, deduped
> by key; conflicts logged in [`verification/bib-conflicts.md`](../verification/bib-conflicts.md)).
> The chapters now use the project-level bibliography only. The files in
> `bib/fragments/` are retained **for provenance only** and are not read by the
> book build.

The convention used while drafting was: each chapter writer added new entries to
a fragment rather than editing the shared file (to avoid parallel-write
conflicts). Keys resolve via `references.bib`; conflicts are resolved by
[`tools/consolidate_bib.py`](../tools/consolidate_bib.py), which keeps the entry
with the most fields (tie-break: the one carrying a DOI) and records the
difference.

