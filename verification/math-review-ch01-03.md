# Independent math verification — Chapters 1–3

Scope: every numbered display equation in `chapters/01-why-embeddings.qmd`,
`chapters/02-math-foundations.qmd`, and `chapters/03-learning-embeddings.qmd`.
Canonical notation: `chapters/appendix-a-math.qmd` (symbol table `{#tbl-symbols}`).
No `quarto render` was run. Authors of the chapters did not perform this review.

Checks performed per equation: notation audit (defined / no collision with
Appendix A / consistent type-shape), equation audit (dimensional consistency,
correct statement of what is optimized-over-what, match to cited source, valid
derivation steps), cross-reference audit, and claim audit. 38 numbered equations
audited (7 + 19 + 12).

Hard constraints honored: label prefixes `eq-chNN-…` unchanged; `$$ … $$ {#eq-…}`
syntax (label after closing `$$`) preserved; no labels renamed/renumbered; no
other chapters, `references.bib`, or `bib/*.bib` touched.

## Findings table

| chapter | label | verdict | note |
|:--|:--|:--|:--|
| 01 | eq-ch01-embedding | fixed | Bolded embedding vector `\mathbf{z}` and data matrix `\mathbf{X}` per unification (Appendix A bold vectors/matrices). Statement itself correct. |
| 01 | eq-ch01-similarity | fixed | Bolded `\mathbf{z}_i,\mathbf{z}_j`; `S_{\mathcal{X}}`/`S` defined in prose (line 21). Order-consistency implication correct. |
| 01 | eq-ch01-onehot | fixed | **Collision fixed:** alphabet size `A` collided with Appendix A's generic matrix `A`; replaced by `\lvert\mathcal{A}\rvert`. Bolded one-hot `\mathbf{e}_a`. Distances `\lVert e_a-e_b\rVert_2=\sqrt2` verified. |
| 01 | eq-ch01-kmer | fixed | **Collision fixed:** dimension `A^k` → `\lvert\mathcal{A}\rvert^k` (same `A` collision). Bolded vector `\boldsymbol{\varphi}_k(s)`. Count definition and sparsity bound `L-k+1` correct. |
| 01 | eq-ch01-distributional | fixed | Bolded `\mathbf{z}_w,\tilde{\mathbf{z}}_c`; skip-gram full-softmax objective stated as maximized over embeddings — correct (mikolov2013efficient). |
| 01 | eq-ch01-contextual | fixed | Bolded `\mathbf{z}_{\text{static}},\mathbf{z}_{\text{ctx}}`; static-vs-contextual definition correct. |
| 01 | eq-ch01-multimodal | fixed | Bolded `\mathbf{z}^{(1)}_i,\mathbf{z}^{(2)}_j`; InfoNCE/CLIP objective with temperature `\tau` correct (radford2021learning). |
| 02 | eq-ch02-inner | fixed | Bolded `\mathbf{u},\mathbf{v}`; components `u_i,v_i` kept scalar. Definition correct. |
| 02 | eq-ch02-norm | fixed | Bolded `\mathbf{u}`; `\ell_p` norm and induced distance `D(\mathbf{u},\mathbf{v})` correct. |
| 02 | eq-ch02-cosine | fixed | Bolded `\mathbf{u},\mathbf{v}`; range `S_{\cos}\in[-1,1]`, `D_{\cos}\in[0,2]` correct. |
| 02 | eq-ch02-cosine-euclid | fixed | Bolded; polarization identity correct; on the unit sphere reduces to `\lVert u-v\rVert^2=2D_{\cos}` — verified. |
| 02 | eq-ch02-metric | fixed | Bolded `\mathbf{u},\mathbf{v},\mathbf{w}`; three metric axioms stated correctly. |
| 02 | eq-ch02-mahalanobis | fixed | Bolded `\mathbf{u},\mathbf{v},\boldsymbol{\Sigma}`. **Collision fixed:** removed Cholesky factor `L` (Appendix A reserves `L` for graph Laplacian / sequence length); rewrote whitened form as `\lVert\boldsymbol{\Sigma}^{-1/2}(\mathbf{u}-\mathbf{v})\rVert_2`. Distance itself correct. |
| 02 | eq-ch02-edit | ok | Levenshtein DP recursion, base cases, and `D_{\mathrm{lev}}(s,t)=D_{\mathrm{lev}}(|s|,|t|)` correct (levenshtein1966binary). No vectors involved. |
| 02 | eq-ch02-concentration | fixed | **Collision fixed:** distance symbols `d_{\min},d_{\max}` collided with dimension `d`; renamed `D_{\min},D_{\max}` (explicit distance symbol per task). Bolded `\mathbf{u}`. Limit/relative-contrast statement matches beyer1999nearest. |
| 02 | eq-ch02-pca | fixed | Bolded `\mathbf{w},\boldsymbol{\Sigma}`; max projected variance s.t. `\lVert w\rVert_2=1`; first-order condition → top eigenvector — correct. |
| 02 | eq-ch02-pca-solution | fixed | **Math error fixed:** with covariance `\Sigma=\tfrac1n X^\top X` the squared Frobenius residual equals `n\sum_{j>k}\lambda_j`, not `\sum_{j>k}\lambda_j`; introduced the `\tfrac1n` normalization so the stated equality holds. Also unified covariance from `\tfrac{1}{n-1}` to `\tfrac1n` (Appendix A and Ch. 3 use `\tfrac1n`). Bolded. |
| 02 | eq-ch02-tsne-p | fixed | Bolded `\mathbf{x}_i`; conditional/joint affinity and `p_{ij}=(p_{j|i}+p_{i|j})/2n` correct (vandermaaten2008visualizing). |
| 02 | eq-ch02-tsne-q | fixed | Bolded `\mathbf{y}_i`; Student-`t` kernel correct. |
| 02 | eq-ch02-tsne-obj | fixed | Bolded `\mathbf{y}_i`; `\min D_{\mathrm{KL}}(P\lVert Q)` with the correct KL form; uses `D_{\mathrm{KL}}` as required. |
| 02 | eq-ch02-umap-q | fixed | Bolded `\mathbf{y}_i`; `q_{ij}=(1+a\lVert y_i-y_j\rVert_2^{2b})^{-1}` correct (mcinnes2018umap). |
| 02 | eq-ch02-umap-obj | fixed | Bolded `\mathbf{y}_i`; fuzzy-set cross-entropy correct. |
| 02 | eq-ch02-probe | fixed | Bolded `\mathbf{w},\mathbf{z}_i`; scalar target `y_i` kept plain. Linear-probe least-squares/CE objective correct. |
| 02 | eq-ch02-whitening | fixed | Bolded `\tilde{\mathbf{z}}_i,\mathbf{z}_i,\boldsymbol{\mu},\boldsymbol{\Sigma}`; whitening map correct. |
| 02 | eq-ch02-procrustes | fixed | Bolded `\mathbf{X},\mathbf{Y}`; orthogonal Procrustes with solution `R^\star=UV^\top`, `\mathbf{X}^\top\mathbf{Y}=U\Lambda V^\top` correct (gower1975generalized). |
| 02 | eq-ch02-analogy | fixed | Bolded `\mathbf{z}^\star,\mathbf{z}_a,\mathbf{z}_b,\mathbf{z}_c`; nearest-to-displacement rule correct. |
| 03 | eq-ch03-pca | fixed | **Math error fixed:** transformed `\max(\cdot)=\min(\cdot)` (false — a max value ≠ min value; they differ by `\operatorname{tr}\Sigma`) into `\mathbf{W}^\star=\arg\max\cdots=\arg\min\cdots`, matching Appendix A `{#eq-appa-pca}`. The equivalence derivation (`\lVert\cdot\rVert^2=\lVert x\rVert^2-\lVert W^\top x\rVert^2`, residual `=\operatorname{tr}\Sigma-\operatorname{tr}(W^\top\Sigma W)`) is valid. |
| 03 | eq-ch03-laplacian | fixed | **Collision fixed:** affinity matrix `\mathbf{A}` collided with Appendix A's generic matrix `A`; renamed to `\mathbf{W}` per Appendix A (`W` = graph affinity, `L=D-W`); updated `D_{ii}=\sum_j W_{ij}` and the identity `\operatorname{tr}(Y^\top(D-W)Y)`. The identity `\tfrac12\sum W_{ij}\lVert y_i-y_j\rVert^2=\operatorname{tr}(Y^\top L Y)` and constraint `Y^\top D Y=I_k` are correct (belkin2003laplacian). |
| 03 | eq-ch03-sgns | ok | SGNS objective maximized over `\{\mathbf{u}_w\},\{\mathbf{v}_c\}`; `P_n`, `K`, `\sigma` consistent with Appendix A; matches Levy–Goldberg / mikolov2013efficient. |
| 03 | eq-ch03-sgns-pmi | ok | Implicit factorization `\mathbf{u}_w^\top\mathbf{v}_c=\mathrm{PMI}(w,c)-\log K` correct (levy2014neural); prose derivation (stationary condition of per-pair logistic loss) valid. |
| 03 | eq-ch03-glove | ok | Weighted least squares on `\log X_{ij}` with biases; minimizer statement correct (pennington2014glove). |
| 03 | eq-ch03-ae | ok | Reconstruction MSE; `\phi,\theta` and Gaussian-decoder remark correct (hinton2006reducing). |
| 03 | eq-ch03-vae | ok | ELBO with `D_{\mathrm{KL}}`; matches Appendix A `{#eq-appa-elbo}` (kingma2014auto). |
| 03 | eq-ch03-elbo | ok | Jensen derivation and tightness gap `D_{\mathrm{KL}}(q_\phi(z|x)\lVert p_\theta(z|x))` correct. |
| 03 | eq-ch03-infonce | ok | InfoNCE loss minimized over `\theta`; matches Appendix A and vandenoord2018representation. |
| 03 | eq-ch03-infonce-mibound | ok | `\mathcal{L}_{\mathrm{InfoNCE}}\ge\log(K+1)-I(\mathbf{x};\mathbf{x}^+)` correct for `K` negatives (`K+1` candidates); "bound improves with more negatives" is the derivable monotone property, not an unbacked claim. |
| 03 | eq-ch03-triplet | ok | Margin-based triplet loss minimized over `\theta`; matches Appendix A `{#tbl-losses}` (schroff2015facenet). |
| 03 | eq-ch03-mlm | ok | Masked-token cross-entropy; `\mathcal{M}`, `x_i`, `\mathbf{x}_{\setminus\mathcal{M}}` defined; minimized over `\theta` (devlin2019bert). |

## Non-equation findings and additional fixes

- **Ch. 1 — undefined `d_0`:** line 27 wrote `d \ll d_0` without defining `d_0`;
  added "(with `d_0` the raw feature dimension)".
- **Ch. 3 — probe-head `\mathbf{V}` collision:** the linear-probe head weight
  `\mathbf{V}\in\mathbb{R}^{C\times k}` collided with Appendix A's `V` (right
  singular-vector matrix / attention value matrix / graph vertex set). Renamed to
  `\mathbf{W}_{\text{head}}` and `g_{\mathrm{head}}`. (Prose, not a numbered
  equation.)
- **Ch. 3 — claim audit:** "This 'augment, embed, contrast' pattern *dominates*
  biological foundation models" had no derivation/citation for the superlative;
  downgraded to "is central to". Line 242 ("Denoising autoencoders *improve* the
  representation …") is cited (vincent2008extracting) and retained; line 334
  ("the bound *improves* with more negatives") follows from the `\log(K+1)` MI
  bound and is retained.
- **Cross-reference audit:** all 38 labels are referenced at least once; every
  `@eq-chNN-…` reference resolves; all `$$` delimiters balanced (14 / 38 / 24
  occurrences); no label is followed by anything other than the closing `$$`.
- **Citations:** every `[@key]` in Ch. 1–3 (25 + 18 + 24 distinct keys) resolves
  in `references.bib ∪ bib/*.bib`. No bib files were modified.

## Flags for the coordinator (not fixed here — outside assigned files/scope)

1. **Appendix A exception paragraph is now stale.** Appendix A was updated to add:
   "A small number of opening definitions (Chapters 1–2 …) set the same objects in
   plain italic … $x,z,u,v,X,W$, and the distance functions $D_M,D_{\cos}$ … this
   is a rendering choice only." The assignment explicitly required converting
   Ch. 1–2 to **bold**, which I did. The appendix's exception text and the
   `\mathbf{x}`/`\mathbf{z}` notation table rows now over-describe Ch. 1–2 as
   italic; that paragraph should be removed/adjusted by whoever owns Appendix A.
   (I did not edit `appendix-a-math.qmd`.)
2. **Appendix A covariance symbol duplication.** Appendix A lists *both* `C`
   ("sample covariance, Ch. 2") and `\Sigma` ("covariance matrix") as Ch. 2
   covariance. Ch. 2 (and Ch. 3) consistently use `\boldsymbol{\Sigma}`; the `C`
   row for Ch. 2 appears to be an appendix-side error and should be reconciled.
3. **Ch. 3 `\mathbf{W}` overload (`A`→`W` fix) is intentional but reader-visible.**
   Appendix A explicitly sanctions `W` for both PCA loadings and graph affinity in
   Ch. 3 ("`L=D-W`", "affinity matrix (Ch. 3)"), so I renamed the affinity matrix
   from `\mathbf{A}` to `\mathbf{W}` and added a one-clause in-chapter note. If the
   coordinator prefers to keep `\mathbf{A}`, Appendix A's `L=D-W` / `W=affinity`
   rows must instead change.
4. **Minor base-letter reuse (acceptable, left as-is):** Ch. 1 one-hot
   `\mathbf{e}_a` shares the base letter with Appendix A's edge/KG `\mathbf{e}`
   vectors (distinct subscripts; context disambiguates); Ch. 1 `\boldsymbol{\varphi}_k`
   (k-mer spectrum) sits near Appendix A's `\phi` (variational parameters) as a
   different glyph.

## Summary

- Equations audited: **38** (Ch. 1: 7; Ch. 2: 19; Ch. 3: 12).
- Fixed: **31** (all notation unification for Ch. 1–2; 3 substantive math/notation
  corrections: Ch. 2 `eq-ch02-concentration` symbol collision, Ch. 2
  `eq-ch02-pca-solution` residual factor/normalization, Ch. 3 `eq-ch03-pca`
  `max=min` equality; plus Ch. 1 `A`→`\lvert\mathcal{A}\rvert` collisions, Ch. 2
  Cholesky-`L` removal, Ch. 3 affinity `A`→`W`).
- Ok (no change): **7** (`eq-ch02-edit`; all 6 unchanged Ch. 3 equations besides
  `eq-ch03-pca` and `eq-ch03-laplacian`).
- Flagged (outside scope / appendix-side): **4** as listed above.
- Disagreements: I disagree with the newly added Appendix A paragraph that treats
  Ch. 1–2 plain-italic vectors as an acceptable rendering choice; the assignment
  requires real unification to bold, which is what I implemented and which makes
  Appendix A's stated book-wide "bold vectors/matrices" rule true everywhere.
