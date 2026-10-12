# Citation verification log

Independent check that every bibliography entry corresponds to a real primary
source and that the metadata (authors, title, venue, year, DOI/pages) is correct.
Verification is done against Crossref / publisher records, not against the
chapter text.

| Key | Checked | Verdict | Evidence |
|-----|---------|---------|----------|
| `chari2023specious` | 2026-10-12 | ok | Crossref `10.1371/journal.pcbi.1011288`: Chari & Pachter, *The specious art of single-cell genomics*, PLOS Comput. Biol. 19(8):e1011288, 2023 |
| `leslie2002spectrum` | 2026-10-12 | ok, enriched | Crossref `10.1142/9789812799623_0053`: Leslie, Eskin, Noble, *The spectrum kernel...*, PSB 2002, pp. 564–575. DOI added |
| `mahalanobis1936generalised` | 2026-10-12 | ok, annotated | Original: Proc. Natl. Inst. Sci. India 2(1):49–55. Reprint Sankhya A (2018) DOI `10.1007/s13171-019-00164-5` added as a note |

## Method

- Crossref REST (`api.crossref.org/works/{doi}` and bibliographic queries) for
  post-2000 work.
- Publisher pages for pre-DOI classics.
- Rule: a key is only marked `ok` when author list, title, venue, and year all
  match; DOIs are added only when confirmed from a publisher/Crossref record.

## Open items

- Verify remaining fragment entries (`bib/*.bib`) once writers finish.
