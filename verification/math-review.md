# Mathematical review log

This is the **index** for the independent math review of the book, per the
protocol in [`outline.qmd`](../outline.qmd). The reviewer was a different agent
from the chapter writer (and from the math-enhancement editor) in every case.

Legend: **ok** = checked, correct · **fixed** = error found and corrected ·
**flagged** = surfaced for a coordinated decision.

## Summary

| Group | File | Equations | ok | fixed | flagged |
|-------|------|:---------:|:--:|:-----:|:-------:|
| Chapters 1–3 | [math-review-ch01-03.md](math-review-ch01-03.md) | 38 | 32 | 6 | 3 |
| Chapters 4–7 | [math-review-ch04-07.md](math-review-ch04-07.md) | 36 | 26 | 7 | 3 |
| Chapters 8–10 | [math-review-ch08-10.md](math-review-ch08-10.md) | 27 | 24 | 3 | 3 |
| Chapters 11–14 | [math-review-ch11-14.md](math-review-ch11-14.md) | 30 | 26 | 4 | 3 |
| Appendices A–B | [math-review-appendices.md](math-review-appendices.md) | 22 | 19 | 3 | 4 |
| **Total** | | **153** | **127** | **23** | **16** |

All 153 numbered equations are referenced at least once, all `@eq-…` references
resolve, and equation labels are globally unique book-wide.

## Substantive corrections made during review

- **Ch3 `eq-ch03-pca`** — `max tr(WᵀΣW)` was equated with `min` reconstruction
  error; the optimal *values* differ by `tr Σ`. Restated as an argmax = argmin
  equivalence (matches Appendix A).
- **Ch2 `eq-ch02-pca-solution`** — residual was off by the `1/n` normalization;
  covariance convention unified to `1/n`.
- **Ch2 `eq-ch02-concentration`** — `d_min, d_max` collided with the dimension
  `d`; renamed `D_min, D_max`.
- **Ch4 `eq-ch04-mismatch`** — prose description of the mismatch kernel was
  corrected (per-k-mer occurrence pairs within Hamming radius, not "pairs that
  agree").
- **Ch4 `eq-ch04-attention`** — removed an incorrect parenthetical about
  singular-vector notation; now links to Appendix A attention.
- **Ch4 `eq-ch04-rc-equiv`** — added the derived consequence `P² = I`.
- **Ch11 `eq-ch11-knn`** — distance symbol `d(·,·) → D(·,·)`.
- **Ch13 `eq-ch13-scaling-law`** — attribution corrected (Kaplan's law has no
  `L_∞` floor; that is the Hoffmann-style extension).
- **Ch14 `eq-ch14-vep-score`** — "rescaling" → "additive shift" of the logits.
- **Ch14 `eq-ch14-kg`** — TransE vectors renamed to `e_h, e_r, e_t` (canonical).
- Plus ~15 notation-collision renames to avoid Appendix A clashes
  (`d_j→δ_j`, `M→Msg`, `A→W`, `C→c`, `∘→⊙`, `V→W_head`, …).

## Citation defects caught by math review

- `meier2021language` pointed to the wrong arXiv id (it resolved to an unrelated
  paper); corrected to the bioRxiv DOI `10.1101/2021.07.09.450648` in
  `references.bib`.

## Cross-cutting reconciliation

The verifiers agreed on a set of book-wide notation rules; the application of
those rules is logged in [notation-consistency.md](notation-consistency.md):

1. Embedding/latent dimension = `d`; rank = `r`; k-mer / k-NN use `k`.
2. Covariance normalization = `1/n` (MLE convention).
3. Generic distance = `D(·,·)`; named distances `d_2`, `d_M`, `d_cos`.
4. `D_KL` for KL divergence, `\mathcal{L}` for loss, `σ` = logistic sigmoid.
5. Bold vectors/matrices book-wide (Appendix A is canonical).
6. Cross-chapter letter overloads documented in Appendix A's symbol table
   unless ambiguous within a single equation.

## Deliverables

- Per-group finding tables (linked above) with chapter | label | verdict | note.
- `notation-consistency.md` — reconciliation decisions and edits.
- `citation-review.md` — citation checks against Crossref/publisher records.
- `bib-conflicts.md` — bibliography entries that differed across fragments.
