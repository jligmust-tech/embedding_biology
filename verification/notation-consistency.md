# Notation consistency reconciliation — book-wide

Scope: reconcile the cross-cutting notation inconsistencies flagged across the five
independent math reviews (`verification/math-review-ch01-03.md`, `…ch04-07.md`,
`…ch08-10.md`, `…ch11-14.md`, `…appendices.md`) against the canonical conventions
decided by the coordinator. Canonical source of truth: `chapters/appendix-a-math.qmd`
(`{#tbl-symbols}`). Edits are minimal; no `{#eq-…}` label was renamed or renumbered,
the `$$ … $$ {#eq-…}` syntax (label after the closing `$$`) is preserved, no required
section/table/figure/callout was removed, `references.bib` and `bib/*.bib` were not
touched, and no `quarto render` was run.

Verifier decisions already present in the tree (e.g. Ch. 2 `1/n` covariance,
Ch. 3 `A→W`, Ch. 9 `M→T`, Ch. 10 `\circ→\odot`, Ch. 11 `d→D`, Ch. 14 `h,r,t→e_h,e_r,e_t`)
were left intact; this pass only adds the previously-unresolved cross-cutting fixes.

## Conventions applied

### 1. Embedding / latent dimension = `d`
- `chapters/appendix-a-math.qmd`:
  - Definition callout: `f_\theta:\mathcal{X}\to\mathbb{R}^{d}`, image in
    `\mathbb{R}^{d}`, "`d` is the *embedding* (or *latent*) dimension" (dropped the
    now-vacuous `k \le d` clause).
  - Symbol table: `\mathbf{z}`, `\mathbf{z}_i`, `\mathbf{z}^{\text{shared}}_i`,
    `\mathbf{z}^{(m)}_i`, `\mathbf{u},\mathbf{v}`, `\mathbf{e}_h,\mathbf{e}_r,\mathbf{e}_t`,
    `Y`, `f_\theta`, `g_\theta` re-typed to `\mathbb{R}^d` / `n\times d`.
  - `d` row: "embedding (latent) dimension; also the ambient / feature dimension of
    `x` (Ch. 1–3)".
  - `k` row: "k-mer length; k-NN neighbourhood size; top-`k` truncation (PCA
    components, Eckart–Young)" — `k` is no longer the embedding dimension.
- `k` kept for k-mer length (Ch. 4 filter width), k-NN, and top-`k` (PCA/Eckart–Young;
  `\mathbb{R}^{d\times k}`, `X_k`, `\operatorname{rank}(Z)\le k` unchanged).
- `r` remains the matrix rank in SVD / Procrustes / Eckart–Young (`I_r`, `U,V` shapes
  `m\times r`, `n\times r`).

### 2. Covariance normalization = `1/n`
- `chapters/08-single-cell.qmd`: `eq-ch08-covariance` `\Sigma=\frac1{n-1}X_c^\top X_c`
  → `\frac1n`; the gene variance in `eq-ch08-hvg`
  (`\sigma_j^2=\frac1{n-1}\sum_i(\tilde X_{ij}-\bar\mu_j)^2`) → `\frac1n`.
- No other `1/(n-1)` occurrence exists in the book (`rg` over `chapters/`); Ch. 2 and
  Ch. 3 already used `\frac1n`, matching `eq-appa-pca`.

### 3. Generic distance `D(\cdot,\cdot)`; named distances `d_2`, `d_M`, `d_{\cos}`
- `chapters/02-math-foundations.qmd`: renamed the named distances to the canonical
  lowercase forms so they match Appendix A — `D_{\cos}\to d_{\cos}` (all occurrences),
  `D_M\to d_M`, `D_{\mathrm{lev}}\to d_{\mathrm{lev}}`. The generic metric `D(\cdot,\cdot)`
  and the auxiliary `D_{\min},D_{\max}` (generic distance with subscripts) are kept.
- Confirmed by search that no chapter uses a bare `d` as a distance.

### 4. `D_{\mathrm{KL}}`, `\mathcal{L}`, and `\sigma` = logistic sigmoid only
- `D_{\mathrm{KL}}` and `\mathcal{L}` were already canonical throughout.
- Removed `\sigma`-as-generic-activation, which conflicted with the sigmoid meaning and
  appeared in the same equation as the sigmoid gate (the convention-7 "same-equation"
  exception):
  - `chapters/04-dna-rna.qmd` `eq-ch04-cnn-filter`: `\sigma(\cdot)` → `\mathrm{ReLU}`
    (prose: "a pointwise nonlinearity (a rectifier, `\mathrm{ReLU}`)").
  - `chapters/06-protein-structure.qmd` `eq-ch06-gvp`: scalar channel `\sigma` →
    `\mathrm{ReLU}`; the sigmoid gate stays `\sigma^{+}`.
  - `chapters/10-graphs-knowledge.qmd`: `eq-ch10-gcn`, `eq-ch10-sage`, `eq-ch10-rgcn`
    `\sigma` → `\mathrm{ReLU}`; `eq-ch10-gat` `\sigma` → `\mathrm{ELU}`; prose "`\sigma`
    is a nonlinearity" → "`\mathrm{ReLU}` is the element-wise activation".
  - `chapters/13-foundation-models.qmd` `eq-ch13-probe`: replaced the generic
    "link function (logistic … identity)" `\sigma` by an explicit two-case output
    (`\hat y_i=\sigma(\mathbf{w}^\top\mathbf{x}_i+b)` for classification, `=\mathbf{w}^\top\mathbf{x}_i+b`
    for regression), so `\sigma` is used only as the logistic sigmoid.
- `\sigma` now denotes only the logistic sigmoid (Ch. 3, 5, 10, 11, 13) and the
  singular value / standard deviation of Appendix A (documented overload).

### 5. Stale "plain-italic rendering choice" paragraph removed
- `chapters/appendix-a-math.qmd`: deleted the paragraph claiming Chapters 1–2 set
  vectors/matrices in plain italic as "a rendering choice only" (and its
  `k\le d`/ℝ`^k` text). Replaced with a one-line accurate statement: the book-wide
  convention is bold vectors/matrices everywhere, and the letters with more than one
  meaning are listed below.

### 6. Single covariance symbol
- `chapters/appendix-a-math.qmd`: `C` is no longer listed as a covariance. The `C`
  overload bullet and the `{#tbl-symbols}` row now give only the contact map
  (`C_{ij}=\mathbb{1}[D_{ij}<\tau]`, Ch. 6) and continuity `C(k)` (Ch. 12); the bullet
  states explicitly that the covariance matrix is the single symbol `\Sigma`. The
  `\Sigma` bullet/row is the one covariance symbol.

### 7. Cross-chapter overloads documented (not renamed)
Added to the Appendix A overload list and `{#tbl-symbols}`:
- `M` = modalities, with local uses as PSSM matrix (Ch. 5), molecule (Ch. 7), mask set
  (Ch. 4, 13), ECE bins (Ch. 11).
- `A` = generic matrix and adjacency matrix `\mathbf{A}` (Ch. 10); alphabet is
  calligraphic `\mathcal{A}` (Ch. 4, 6); graph affinity stays `W` (Ch. 3).
- `R` = orthogonal alignment `\Omega`/`R`, `R\in SO(3)` (Ch. 6), population risk
  `R(\theta)`, and permutation-invariant readout (Ch. 6–7).
- `P` = t-SNE high-dim affinity, reverse-complement map `\mathbf{P}` (Ch. 4),
  positive-example count (Ch. 11); amino-acid alphabet is `\mathcal{P}` (Ch. 5).
- `V` = right singular vectors, attention value matrix, vertex set (extended to
  Ch. 6), and GVP vector channel (Ch. 6).
- `N` = atoms/residues/nodes, positive/negative counts (Ch. 11), parameter count (Ch. 13).
- `D` = distance function, degree matrix, distance matrix, hash buckets, training
  tokens (Ch. 13).
- `L` = graph Laplacian, sequence length, scaling-law test loss `L(N)` (Ch. 13).
- `σ` = logistic sigmoid; singular value / standard deviation (with the explicit
  statement that it is never a generic activation).
- `\mathbf{z}_v^{(l)}` vs `\mathbf{h}_v^{(l)}` = same node/atom state object (Ch. 10 vs
  Appendix A).
- `k` = k-mer / k-NN / top-`k`, with the dimensionality-reduction chapters (3, 10)
  writing the top-`k` reduced dimension as `k` (a documented local overload of `d`).
- `\phi` = variational/encoder parameters, Ch. 10 message function, Ch. 14 `g_\phi`;
  `\mathbf{u}` = generic vector and Ch. 14 reference window.
- Table rows added/extended accordingly: `A`, `R` (via `R(\theta)` row),
  `C(k)`/`T(k)`, `P,N`, and `L/D/M/N` overload extensions.

### 8. Ch. 8 ZINB vs Ch. 9 NB reconciled
- `chapters/09-multiomics-multimodal.qmd` (where the second one is introduced, in the
  MultiVI paragraph): added one sentence stating that the Ch. 9 negative binomial is
  the non-zero-inflated special case of the Ch. 8 zero-inflated negative binomial, and
  that each model follows the likelihood chosen by its source
  `[@lopez2018deep; @ashuach2023multivi]`. `eq-ch08-zinb` and `eq-ch09-factor-model`
  are unchanged.

### 9. Ch. 6 GVP stated as a simplified exposition
- `chapters/06-protein-structure.qmd`, after `eq-ch06-gvp`: added that the displayed
  form is a simplified exposition and that the full layer of Jing et al. (2021) also
  scales the vector channel by the row-wise vector-norm term `\lVert\mathbf{V}\rVert_2`,
  omitted here for clarity, pointing to `[@jing2021learning]`.

### 10. Ch. 7 random-vs-scaffold split claim supported
- `chapters/07-molecules-chemistry.qmd`: softened "massively overstate" to "can
  substantially overstate" and cited the existing primary keys already used in Ch. 11
  — `[@bemis1996properties; @chuang2018adversarial]` (both present in
  `references.bib`; no new keys or DOIs added).

## Overloads deliberately left as documented (not renamed)
Per convention 7, the following letter reuse is documented in Appendix A rather than
renamed, because it is not ambiguous within any single equation:
`M` (modalities / PSSM / molecule / mask set / ECE bins), `A` (generic matrix /
adjacency / calligraphic alphabet), `R` (rotation / risk / readout), `P` (t-SNE
affinity / RC map / positive count / calligraphic protein alphabet), `V` (singular
vectors / attention value / vertex set / GVP channel), `N` (atoms / counts / parameter
count), `D` (distance / degree / distance matrix / buckets / training tokens), `L`
(Laplacian / sequence length / scaling-law loss), `σ` (sigmoid / singular value / std
dev), `z_v^{(l)}` vs `h_v^{(l)}`, `r` (rank / relation type), `\phi`, `\mathbf{u}`,
`W` (projection / affinity), `g` (genes / decoder / rigid motion), `\tau` (temperature /
contact threshold), `m` (margin / mismatches / Adam moment), `p,q` (densities /
node2vec parameters). Only `σ`'s generic-activation use was renamed (same-equation
ambiguity), and `C`-as-covariance was removed (one covariance symbol).

## Files changed
1. `chapters/appendix-a-math.qmd` — conventions 1, 3 (bullet), 5, 6, 7; typography
   note, definition, overload list, `{#tbl-symbols}`.
2. `chapters/02-math-foundations.qmd` — convention 3 (`D_{\cos},D_M,D_{\mathrm{lev}}`
   → lowercase named distances).
3. `chapters/04-dna-rna.qmd` — convention 4 (`eq-ch04-cnn-filter` σ→ReLU).
4. `chapters/06-protein-structure.qmd` — conventions 4 and 9 (`eq-ch06-gvp`).
5. `chapters/07-molecules-chemistry.qmd` — convention 10 (scaffold-split citation).
6. `chapters/08-single-cell.qmd` — convention 2 (`eq-ch08-covariance`, `eq-ch08-hvg`).
7. `chapters/09-multiomics-multimodal.qmd` — convention 8 (ZINB/NB sentence).
8. `chapters/10-graphs-knowledge.qmd` — convention 4 (GCN/SAGE/GAT/R-GCN activations).
9. `chapters/13-foundation-models.qmd` — convention 4 (`eq-ch13-probe` explicit output).

## Residual notes (not changed)
- Ch. 3 and Ch. 10 still write the *reduced* embedding/latent dimension as `k` with the
  input dimension `d` (`\mathbf{z}\in\mathbb{R}^k`, `f_\phi:\mathbb{R}^d\to\mathbb{R}^k`).
  Rewriting these would invert the dimensionality-reduction narrative and touch
  unassigned files, so it is recorded as a documented local overload of `d` in the
  Appendix A `k` bullet instead.
- The appendix PCA/Eckart–Young displays keep `k` as the top-`k` truncation size
  (`\mathbb{R}^{d\times k}`, `X_k`, `\operatorname{rank}(Z)\le k`), consistent with the
  retained `k` meaning.
- The bib defect `meier2021language` in `bib/frontier-apps.bib` is out of scope
  (`references.bib`/bibs untouched) and remains flagged in the ch11-14 review.
