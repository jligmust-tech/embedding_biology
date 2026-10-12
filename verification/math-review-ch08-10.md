# Math Review — Chapters 8–10

Independent math verification of `chapters/08-single-cell.qmd`,
`chapters/09-multiomics-multimodal.qmd`, and `chapters/10-graphs-knowledge.qmd`,
against `outline.qmd` (Mathematical rigor; Mathematical verification protocol) and
`chapters/appendix-a-math.qmd` (canonical notation).

Scope: every numbered display equation with a label prefixed `eq-ch08-…`,
`eq-ch09-…`, `eq-ch10-…` (27 total: 7 + 6 + 14). Audit dimensions: notation
(defined, no Appendix A collision, consistent type/shape); equation (dimensional
consistency, what is optimized and over what, match to cited source, validity of
any derivation step); cross-reference (label referenced; every `@eq-`/`@fig-`/
`@tbl-` resolves); claims (unsupported comparative claims derived/cited or
downgraded). Verification was done by re-deriving each nontrivial identity; the
chapter was not authored by the verifier. No `quarto render` was run.

## Findings

| Chapter | Label | Verdict | Note |
|---|---|---|---|
| 8 | `eq-ch08-normalize` | ok | Shifted-log rescaling is well-typed ($X_{ij}/s_i$ dimensionless). The delta-method argument for $\log1p$ as variance-stabilizing is valid: with $\operatorname{Var}[X]=\mu+\mu^2/\theta$, requiring $[f'(\mu)]^2(\mu+\mu^2/\theta)$ constant forces $f'\propto(\mu+\mu^2/\theta)^{-1/2}\to1/\mu$, whose solution is $f=\log$; the $1+\cdot$ shift keeps the map finite at $0$. |
| 8 | `eq-ch08-hvg` | fixed | Two Appendix A collisions removed: dispersion $d_j$ clashed with the latent dimension $d$ used in this chapter and with canonical $d$; the expression-bin function $b(j)$ clashed with the batch covariate $b_i$; the cutoff reused canonical $\tau$ (temperature/contact threshold) and the count reused canonical $k$ (reduced latent dim). Renamed $d_j\to\delta_j$, $b(j)\to\operatorname{bin}(j)$, $\tau\to\zeta$, top-$k\to n_{\mathrm{HVG}}$ (equation and surrounding prose). Math unchanged and correct (within-bin standardized log-dispersion, Seurat convention). |
| 8 | `eq-ch08-covariance` | ok | $\boldsymbol{\Sigma}=\frac1{n-1}\mathbf{X}_c^\top\mathbf{X}_c=\mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^\top$ is a valid $g\times g$ eigendecomposition; projection $\mathbf{Z}=\mathbf{X}_c\mathbf{V}_d$ and the Eckart–Young "best rank-$d$ reconstruction" claim are correct ($\mathbf{Z}\mathbf{V}_d^\top=\mathbf{X}_c\mathbf{V}_d\mathbf{V}_d^\top$). Minor: the scalar prefactor is $1/(n-1)$ here vs $1/n$ in Appendix A (`eq-appa-pca`); eigenvectors, projection, and explained-variance ratio are unaffected, so no downstream error. |
| 8 | `eq-ch08-zinb` | ok | The ZINB pmf is correct ($\pi_{ij}\delta_0+(1-\pi_{ij})\,p_{\mathrm{NB}}$) with NB mean $\mu_{ij}=s_i\rho_{ij}$ and dispersion $\theta_j$; faithful to Lopez et al. 2018 [@lopez2018deep]. Note (not an error): Ch9 calls the MultiVI likelihood "negative binomial" [@ashuach2023multivi] — consistent with each cited source, but a reader may read Ch8's ZINB and Ch9's NB as a contradiction; consider a one-line reconciliation. |
| 8 | `eq-ch08-scvi-likelihood` | ok | Gene-conditional factorization of the observation log-likelihood is the stated scVI independence assumption; sum over $j$ is dimensionally consistent. |
| 8 | `eq-ch08-elbo` | ok | $\mathcal{L}=\mathbb{E}_{q_\phi}[\log p_\theta(\mathbf{x}\mid\mathbf{z})]-D_{\mathrm{KL}}(q_\phi(\mathbf{z}\mid\mathbf{x})\lVert p(\mathbf{z}))$ matches Ch3 `eq-ch03-vae` and Appendix A `eq-appa-elbo` exactly; no cross-chapter contradiction. Maximized over $\theta,\phi$. |
| 8 | `eq-ch08-elbo-gap` | ok | $\log p_\theta(\mathbf{x})-\mathcal{L}=D_{\mathrm{KL}}(q_\phi(\mathbf{z}\mid\mathbf{x})\lVert p_\theta(\mathbf{z}\mid\mathbf{x}))\ge0$: standard identity, correct. The unlabeled Jensen display preceding it is also correct. |
| 9 | `eq-ch09-factor-model` | ok | Shared/private latent factorization matches Appendix A symbols ($\mathbf{z}^{\mathrm{sh}}_i,\mathbf{z}^{(m)}_i,\mathbf{c}_i$); conditional-independence assumption is stated explicitly and licenses the per-modality likelihood. |
| 9 | `eq-ch09-mi-decomp` | ok | $I(\mathbf{x}^{(1)};\mathbf{x}^{(2)})=H(\mathbf{x}^{(1)})-H(\mathbf{x}^{(1)}\mid\mathbf{x}^{(2)})$ is the entropy chain rule; correct. |
| 9 | `eq-ch09-dpi` | ok | With $\mathbf{z}=g(\mathbf{x}^{(1)})$ the triple forms a Markov chain, so $I(\mathbf{z};\mathbf{x}^{(2)})\le I(\mathbf{x}^{(1)};\mathbf{x}^{(2)})$ by the data-processing inequality; valid. |
| 9 | `eq-ch09-infonce` | ok | $B$-way InfoNCE cross-entropy correct; the MI lower bound $I(\mathbf{u};\mathbf{v})\ge\log B-\mathcal{L}$ matches van den Oord et al. [$B$ candidates $= $ Ch3's $K{+}1$], and the stated infimum $\log B-I$ at the optimal density-ratio critic is correct. |
| 9 | `eq-ch09-clip` | ok | Symmetric CLIP loss = mean of the $\mathbf{u}\!\to\!\mathbf{v}$ row-softmax and the $\mathbf{v}\!\to\!\mathbf{u}$ column-softmax cross-entropies; indices and normalization correct. |
| 9 | `eq-ch09-translation` | fixed | Renamed the soft-assignment matrix $M\in\mathbb{R}_{\ge0}^{n_{\mathrm{ref}}\times n_{\mathrm{sp}}}\to T$: $M$ is canonical for the *number of modalities* and is used that way earlier in the same chapter, so reusing it for the mapping matrix was a genuine collision. Objective (maximize $\sum_k\cos((T^\top\mathbf{X}_{\mathrm{ref}})_k,\mathbf{Y}_k)-\lambda\Omega(T)$) and shapes are correct and unchanged. |
| 10 | `eq-ch10-walk-sgns` | ok | Identical to the Chapter 3 SGNS objective (`eq-ch03-sgns`); maximized over per-node vectors; the shifted-PMI factorization claim is consistent with Ch3 `eq-ch03-sgns-pmi`. |
| 10 | `eq-ch10-mp` | ok | GraphNets message-passing update is correctly formed ($\psi$ message, $\bigoplus$ permutation-invariant aggregation, $\phi$ update); the permutation-invariance requirement is correctly justified. |
| 10 | `eq-ch10-spectral` | ok | First-order Chebyshev approximation is correct: $g_\theta(\boldsymbol{\Lambda})\approx\theta_0\mathbf{I}+\theta_1(\boldsymbol{\Lambda}-\mathbf{I})$ with $\lambda_{\max}=2$ (eigenvalues of $\mathbf{L}$ in $[0,2]$), giving $\theta_0\mathbf{x}-\theta_1\mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2}\mathbf{x}$; the step $\theta=\theta_0=-\theta_1$ is valid. Renormalization trick ($\tilde{\mathbf{A}}=\mathbf{A}+\mathbf{I}$) correctly described. |
| 10 | `eq-ch10-gcn` | ok | $\mathbf{Z}^{(l+1)}=\sigma(\tilde{\mathbf{D}}^{-1/2}\tilde{\mathbf{A}}\tilde{\mathbf{D}}^{-1/2}\mathbf{Z}^{(l)}\mathbf{W}^{(l)})$ with $\mathbf{W}^{(l)}\in\mathbb{R}^{d_l\times d_{l+1}}$ is dimensionally consistent and matches Kipf & Welling. See flagged note on $\sigma$ usage. |
| 10 | `eq-ch10-sage` | ok | GraphSAGE concat-then-project update correct; inductive property correctly attributed to a learned feature aggregator. See flagged note on $\sigma$ usage. |
| 10 | `eq-ch10-gat` | ok | Attention $\alpha_{vu}=\operatorname{softmax}_{u}(\mathrm{LeakyReLU}(\mathbf{a}^\top[\mathbf{W}\mathbf{z}_v\Vert\mathbf{W}\mathbf{z}_u]))$ over $\mathcal{N}(v)$, and $\mathbf{z}_v'=\sigma(\sum_u\alpha_{vu}\mathbf{W}\mathbf{z}_u)$, are correct and normalized. |
| 10 | `eq-ch10-rgcn` | ok | R-GCN relation-specific aggregation with $1/c_{v,r}$ normalization plus self-loop term $\mathbf{W}_0^{(l)}\mathbf{z}_v^{(l)}$ is correct; $c_{v,r}$ and $\mathcal{N}_r(v)$ match Appendix A. See flagged note on $\sigma$ usage. |
| 10 | `eq-ch10-kg-loss` | ok | Logistic ranking (negative-sampling) objective, maximized over entity and relation embeddings; corruption distribution $P_n$ matches Appendix A. |
| 10 | `eq-ch10-transe` | ok | $f(h,r,t)=-\lVert\mathbf{e}_h+\mathbf{e}_r-\mathbf{e}_t\rVert_2$ is the standard TransE score. |
| 10 | `eq-ch10-transe-sym` | ok | Symmetric-relation collapse verified: high score for both $(h,r,t)$ and $(t,r,h)$ gives $2\mathbf{e}_r\approx\mathbf{0}$ and $\mathbf{e}_h\approx\mathbf{e}_t$; the one-to-many non-identifiability argument is also correct. |
| 10 | `eq-ch10-rotate` | fixed | Replaced $\circ$ with $\odot$ for the Hadamard product (Appendix A canonicalizes Hadamard as $\odot$; $\circ$ is unlisted and elsewhere denotes function composition). Score $f=-\lVert\mathbf{e}_h\odot\mathbf{e}_r-\mathbf{e}_t\rVert_2$ with unit-modulus $e_r[j]=e^{i\theta_j}$ is correct. Pattern-coverage claims verified: symmetry $\Leftrightarrow\theta_j\in\{0,\pi\}$, antisymmetry $\Leftrightarrow\theta_j\notin\{0,\pi\}$, and phase-additive (hence commutative) composition — all correct. |
| 10 | `eq-ch10-distmult` | ok | $f=\sum_j e_h[j]e_r[j]e_t[j]$ is bilinear and manifestly symmetric in head/tail, $f(h,r,t)=f(t,r,h)$; the inability to rank an antisymmetric relation above its reverse follows. |
| 10 | `eq-ch10-complex` | ok | ComplEx score $\operatorname{Re}\langle\mathbf{e}_h,\mathbf{e}_r,\overline{\mathbf{e}_t}\rangle$ correct. |
| 10 | `eq-ch10-complex-antisym` | ok | Antisymmetry derivation independently re-derived and confirmed: with $a_\ast^{(j)}=\Re e_\ast[j]$, $b_\ast^{(j)}=\Im e_\ast[j]$, $f(h,r,t)-f(t,r,h)=2\sum_j b_r^{(j)}(a_h^{(j)}b_t^{(j)}-a_t^{(j)}b_h^{(j)})$. The real special case ($\Im\equiv0$, i.e. DistMult) is correctly recovered as zero. |

## Cross-reference audit

- All 27 labels are unique (prefixes `eq-ch08-`/`eq-ch09-`/`eq-ch10-` avoid the
  book-wide duplicate names noted elsewhere) and **every label is referenced at
  least once** in its own chapter.
- Every `@eq-…` reference resolves; the sole figure reference
  `@fig-kg-linkpred` resolves to the `{#fig-kg-linkpred}` div. No `@tbl-…`
  references exist in these chapters (their tables are unlabeled), so none are
  dangling.
- All `[@key]` citations used in the three chapters resolve in `references.bib`.

## Flagged notation issues (no equation is mathematically wrong)

| Chapter | Label | Verdict | Note |
|---|---|---|---|
| 8 | (notation, `eq-ch08-covariance`) | flagged | Latent dimension is written $d$ ($\mathbf{z}\in\mathbb{R}^d$, $d\ll g$) whereas Appendix A's table uses $k$ for the reduced/latent dimension. Appendix A's own *Definition* of "embedding" also licenses $d$ as the embedding/latent dimension, so this is ambiguous rather than clearly wrong — coordinator should decide whether to normalize to $k$. |
| 10 | (notation, `eq-ch10-gcn`, `-sage`, `-rgcn`) | flagged | $\sigma$ is declared as the logistic sigmoid at the top of the chapter (correct in `eq-ch10-walk-sgns`/`eq-ch10-kg-loss`) but is then used as a generic activation (ReLU/ELU in the original GCN/SAGE/R-GCN), while Appendix A fixes $\sigma$ as the logistic sigmoid. Standard GNN notation, but an unlisted overload; consider writing the activation explicitly or a note. |
| 10 | (notation, `eq-ch10-mp`, `-gcn`, `-sage`, `-gat`, `-rgcn`) | flagged | Node states are written $\mathbf{z}_v^{(l)}\in\mathbb{R}^{d_l}$; Appendix A provides $\mathbf{h}_v^{(l)}$ for exactly this object. Type/shape agree, so the equations are correct, but the canonical symbol is unused. |

## Claim audit

- Comparative/benefit claims in the three chapters are either derived (TransE
  symmetric failure, DistMult symmetry, ComplEx asymmetry, RotatE coverage, GCN
  locality, InfoNCE MI bound, DPI cap) or cited (`scVI among the strongest
  integration methods` [@luecken2022benchmarking]; foundation-model superiority
  explicitly hedged as "uneven"). No unsupported "improves/outperforms" claim was
  found that required downgrading. Ch10's "shallow embeddings are cheap and strong
  on homogeneous graphs" is descriptive rather than a benchmark claim.

## Summary

- Equations checked: **27** (Ch8: 7, Ch9: 6, Ch10: 14).
- Fixed in place: **3** — `eq-ch08-hvg` (4 notation collisions), `eq-ch09-translation`
  (assignment-matrix/name collision with $M=$ modalities), `eq-ch10-rotate`
  (`\circ`→`\odot` Hadamard).
- Flagged: **3** cross-cutting notation notes ($d$ vs $k$; $\sigma$ as generic
  activation; $\mathbf{z}_v^{(l)}$ vs $\mathbf{h}_v^{(l)}$) plus one reader-facing
  cross-chapter note (Ch8 ZINB vs Ch9 NB).
- No mathematical error (dimensional inconsistency, wrong objective, invalid
  derivation, or contradiction with a cited source) was found; all 27 labeled
  equations are correct. Label prefixes and `$$ … $$ {#eq-…}` syntax were
  preserved; no labels were renamed or renumbered; no other chapter, `references.bib`,
  or `bib/*.bib` was modified.
