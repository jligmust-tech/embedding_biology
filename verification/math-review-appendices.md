# Math review — Appendices A and B

**Scope.** Independent verification of `chapters/appendix-a-math.qmd` (canonical
notation source) and `chapters/appendix-b-tools-data.qmd`, per the "Mathematical
rigor" and "Mathematical verification protocol" requirements in `outline.qmd`.
The reviewer did not write these appendices. Label prefixes and the display
syntax `$$ … $$ {#eq-…}` are preserved; no labels were renamed, renumbered, or
removed; no chapters and no `references.bib` were touched.

**Method.** Each numbered equation was checked for (a) dimensional
consistency, (b) correctness of the stated objective (what is optimized, over
what), and (c) agreement with the standard reference (SVD, Eckart–Young, PCA,
orthogonal Procrustes, entropy, cross-entropy, KL, mutual information, ELBO,
softmax, scaled dot-product attention, SGD, Adam). The canonical symbol table
`{#tbl-symbols}` was checked row by row for correct meaning/type and internal
contradiction. Every `{#eq-…}` label was checked for at least one resolving
reference.

**Verdict legend.** `ok` = checked, correct · `fixed` = error found and
corrected in place · `flagged` = unresolved, needs author attention.

## Findings

| File | Label | Verdict | Note |
|:---|:---|:---|:---|
| appendix-a-math.qmd | eq-appa-inner-product | ok | $\langle x,y\rangle=x^\top y=\sum_i x_i y_i$, $x,y\in\mathbb{R}^d$; correct. |
| appendix-a-math.qmd | eq-appa-norm | ok | $\ell_p$ norm and its $p=2$ case $\lVert x\rVert_2=\sqrt{\langle x,x\rangle}$; correct; $\ell_1,\ell_\infty$ cases stated correctly. |
| appendix-a-math.qmd | eq-appa-cosine | ok | $\cos\in[-1,1]$ and $d_{\cos}=1-\cos$; correct, invariant to magnitude as stated. |
| appendix-a-math.qmd | eq-appa-euclidean | ok | $\lVert x-y\rVert_2$; correct. |
| appendix-a-math.qmd | eq-appa-mahalanobis | ok | $\sqrt{(x-y)^\top\Sigma^{-1}(x-y)}$, $\Sigma=\mathrm{Cov}[x]\succ0$; correct. |
| appendix-a-math.qmd | eq-appa-svd | ok | Thin SVD $X=U\,\mathrm{diag}(\sigma_1..\sigma_r)V^\top$, $U^\top U=V^\top V=I_r$, $\sigma_1\ge..\ge\sigma_r>0$; correct for $\operatorname{rank}(X)=r$. |
| appendix-a-math.qmd | eq-appa-eckart-young | ok | $X_k=\sum_{i\le k}\sigma_i u_i v_i^\top=\arg\min_{\operatorname{rank}(Z)\le k}\lVert X-Z\rVert_F$, residual $\sum_{i>k}\sigma_i^2$; correct (Eckart–Young–Mirsky). |
| appendix-a-math.qmd | eq-appa-pca | flagged | Equations correct (max $W^\top\Sigma W$ ⇔ min $n^{-1}\sum_i\lVert x_i-WW^\top x_i\rVert^2$, $Z=XW$). Convention flag: this appendix defines $\Sigma=\tfrac1n X^\top X$, while Chapter 2 uses $\tfrac{1}{n-1}X^\top X$; the two normalizations must be reconciled (see Flags). |
| appendix-a-math.qmd | eq-appa-procrustes | ok | $\Omega^\star=\arg\min_{\Omega^\top\Omega=I}\lVert X\Omega-Y\rVert_F^2=UV^\top$ with $X^\top Y=U\,\mathrm{diag}(\sigma)V^\top$; correct. |
| appendix-a-math.qmd | eq-appa-elbo | ok | $\mathbb{E}_{q_\phi}[\log p_\theta(x\mid z)]-D_{\mathrm{KL}}(q_\phi\lVert p(z))\le\log p_\theta(x)$; correct, bound tight at $q_\phi=p_\theta(z\mid x)$. |
| appendix-a-math.qmd | eq-appa-entropy | ok | $H(p)=-\sum_x p\log p=\mathbb{E}_p[-\log p]$; correct. |
| appendix-a-math.qmd | eq-appa-cross-entropy | ok | $H(p,q)=-\sum_x p\log q=H(p)+D_{\mathrm{KL}}(p\lVert q)$; correct, minimized at $q=p$. |
| appendix-a-math.qmd | eq-appa-kl | ok | $D_{\mathrm{KL}}(p\lVert q)=\sum_x p\log\frac{p}{q}\ge0$; correct, asymmetric (not a metric) as stated. |
| appendix-a-math.qmd | eq-appa-mi | ok | $I(X;Y)=\sum p(x,y)\log\frac{p(x,y)}{p(x)p(y)}=D_{\mathrm{KL}}(p(x,y)\lVert p(x)p(y))\ge0$; correct. |
| appendix-a-math.qmd | eq-appa-infonce | ok | Positive over positive+$K$ negatives with temperature $\tau$; correct InfoNCE; the "lower bound on MI" claim is standard. |
| appendix-a-math.qmd | eq-appa-risk | ok | $R_\lambda=\frac1n\sum_i\ell(f_\theta(x_i),y_i)+\lambda\rho(\theta)$, $\hat\theta=\arg\min$; correct, $\lambda\ge0$. |
| appendix-a-math.qmd | eq-appa-softmax | ok | $\mathrm{softmax}(z)_i=e^{z_i}/\sum_j e^{z_j}$; correct. |
| appendix-a-math.qmd | eq-appa-attention | ok | $\mathrm{softmax}(QK^\top/\sqrt{d_k})V$; correct scaled dot-product attention; $\sqrt{d_k}$ rationale correct. |
| appendix-a-math.qmd | eq-appa-sgd | ok | $\theta_{t+1}=\theta_t-\eta\nabla_\theta\hat R(\theta_t)$; correct. |
| appendix-a-math.qmd | eq-appa-adam | ok | $m_t,v_t$ updates, bias correction $\hat m_t=m_t/(1-\beta_1^t)$, $\hat v_t=v_t/(1-\beta_2^t)$, update $\theta_{t+1}=\theta_t-\eta\,\hat m_t/(\sqrt{\hat v_t}+\epsilon)$; correct; defaults $0.9/0.999/10^{-8}$ correct. |
| appendix-b-tools-data.qmd | eq-appb-split | ok | $\mathcal{D}=\mathcal{D}_{\text{train}}\sqcup\mathcal{D}_{\text{val}}\sqcup\mathcal{D}_{\text{test}}$ with pairwise-disjoint blocks; correct and consistent with Appendix A ($\mathcal{D}$ = dataset). |
| appendix-b-tools-data.qmd | eq-appb-leakage | ok | Test empirical risk and $\mathrm{gap}=R(\theta)-\hat R_{\text{test}}(\theta)$; correct, and $\mathrm{gap}>0$ is consistent with optimistic (leaked) test risk. Label names the split-risk/gap relation, not merely KL-style leakage — content is right. |
| appendix-a-math.qmd | tbl-symbols (`{#tbl-symbols}`) | fixed | Removed a duplicated `$L$` row (graph Laplacian listed twice, lines 89 and 108); all remaining rows define one meaning per type. Corrected `$d$` row to "ambient / feature dimension" so it no longer conflicts with `$k$` as the embedding/latent dimension. |
| appendix-a-math.qmd | Definition callout (Embedding) | fixed | Prose contradicted the table: it said the image $f_\theta(x)$ "is written $\mathbf{x}$" and "$d$ is the embedding dimension", while the table (`$z=f_\theta(x)\in\mathbb{R}^k$`, `$f_\theta:\mathcal{X}\to\mathbb{R}^k$`) and Chapters 3–12 use $z$ and $k$. Reconciled to the table. |
| appendix-a-math.qmd | Typography & overloads note | fixed | Note falsely claimed "Chapters 2, 3, and 6–10 typeset vectors/matrices in plain italic". The book-wide convention is **bold** (Ch. 3–14 use `\mathbf` heavily); plain italic is confined to opening Chapters 1–2 and the metric summary. Rewrote the note and added the missing `d`, `V`, `Σ` disambiguations (see below). |
| appendix-a-math.qmd | tbl-metrics (`{#tbl-metrics}`) | ok | Rows consistent with eq-appa-euclidean/cosine/mahalanobis; "squared Euclidean is not a metric" and "alignment score is a similarity, not a metric" correct. |
| appendix-a-math.qmd | tbl-distributions (`{#tbl-distributions}`) | ok | Support/use pairings correct (Gaussian, Bernoulli, categorical, Poisson, negative binomial). |
| appendix-a-math.qmd | tbl-losses (`{#tbl-losses}`) | ok | MSE, BCE, softmax cross-entropy, triplet (hinge with margin $m$), InfoNCE; forms and "optimizes" column correct. |

## Errors fixed

1. **Typography note (main error).** The note asserted that Chapters 2, 3 and
   6–10 set vectors/matrices in plain italic. `\mathbf`-usage counts show the
   opposite: the book-wide convention is bold (e.g. Ch. 3: 189, Ch. 6: 195,
   Ch. 10: 135 uses), with plain italic confined to the opening definitions of
   Chapters 1–2 (and the metric summary). The note is rewritten to state the
   bold convention, treat plain italic as a same-object rendering variant, and
   disambiguate the reused letters (full text below).
2. **Duplicated canonical symbol.** `$L$` had two rows in `{#tbl-symbols}`
   (graph Laplacian listed at line 89 and again at line 108). Removed the
   redundant row; the surviving row already covers both meanings
   (sequence length, and $L=D-W$).
3. **Definition-callout contradiction.** "The image $f_\theta(x)$ is written
   $\mathbf{x}$, and $d$ is the embedding dimension" contradicted the table
   ($\mathbf{z}=f_\theta(\mathbf{x})\in\mathbb{R}^k$; $f_\theta:\mathcal{X}\to
   \mathbb{R}^k$). Corrected to $\mathbf{z}$ and $k$, and the following
   sentence ("$\mathbf{x}_i$ denotes the embedding of entity $i$") corrected so
   $\mathbf{x}_i$ is the feature vector and $\mathbf{z}_i=f_\theta(\mathbf{x}_i)$
   the embedding, matching the table.

## Flags (unresolved — author attention)

1. **Embedding dimension across chapters.** After reconciling Appendix A to the
   table ($\mathbf{z}\in\mathbb{R}^k$, embedding dimension $k$), Chapters 1,
   13 and 14 still write the same object at the full dimension $d$ (Chapter 1 as
   $z\in\mathbb{R}^d$; Chapters 13–14 as $x\in\mathbb{R}^d$). These chapters
   were out of scope for edits and should be aligned to the canonical appendix.
2. **Covariance normalization.** Appendix A's @eq-appa-pca uses
   $\Sigma=\tfrac1n X^\top X$; Chapter 2 uses $\tfrac{1}{n-1}X^\top X$. Both are
   legitimate estimators (MLE vs unbiased) but the canonical source should pick
   one convention.
3. **Graph-matrix shape typing.** `{#tbl-symbols}` types $W$, $D$ and $L$ as
   $n\times n$ while $N$ is defined as "number of atoms, residues, or nodes in
   one structure/graph"; Chapter 3 uses $n$ for vertices, but Chapters 6 and 10
   count per-graph units as $N$. The shape column should read $N\times N$ (or
   note that $n=N$ for graphs).
4. **Symbol `R`.** The table gives `$\Omega$ ($R$)` as the orthogonal
   alignment/rotation matrix, `$R\in SO(3)$` as a 3D rotation, and `$R(\theta)$`
   as the population risk — three meanings under one letter. Not among the
   letters requested for disambiguation, but worth a table note.

Cross-reference audit: all 22 equation labels in the appendices
(20 `eq-appa-*`, 2 `eq-appb-*`) resolve to at least one reference; no dangling
labels. No equations were found to be dimensionally inconsistent.

## Corrected "Typography and overloads" note

> **Typography and overloads.** The book-wide convention is **bold for vectors
> and matrices**: a vector is $\mathbf{x}$ and a matrix is $\mathbf{X}$; scalars
> are italic lowercase ($d$, $n$, $k$), and sets and spaces are calligraphic
> ($\mathcal{X}$, $\mathcal{D}$). A small number of opening definitions
> (Chapters 1–2 and the metric summary) set the same objects in plain italic
> under the same names — $x$, $z$, $u$, $v$, $X$, $W$, and the distance
> functions $D_M, D_{\cos}$ — so this is a rendering choice only: a plain-italic
> symbol and its bold counterpart denote exactly the same object with the same
> type, and $z$ and $\mathbf{z}$, $X$ and $\mathbf{X}$ are interchangeable.
> Likewise the embedding is written $\mathbf{z}=f_\theta(\mathbf{x})\in\mathbb{R}^{k}$
> in most chapters, whereas Chapters 1, 13, and 14 use the full dimension $d$
> for the same object (Chapter 1 writes it $z$, Chapters 13–14 write it $x$); in
> all cases $k\le d$. Apart from these typographic variants no chapter redefines
> a canonical symbol. The letters that do carry more than one meaning are listed
> below; context always resolves them:
>
> - $d$: the ambient / feature dimension of an object, $x\in\mathbb{R}^{d}$
>   (this appendix, Chapters 1–2), versus the lowercase distance functions
>   $d_2$, $d_M$, $d_{\cos}$ (this appendix) and the component dimensions $d_k$
>   (attention key), $d_l$ (layer), $d_e$ (edge). The reduced embedding dimension
>   is $k$.
> - $D$: a distance function / metric $D(\cdot,\cdot)$ (Chapters 1–2); the graph
>   degree matrix $D_{ii}=\sum_j W_{ij}$ (Chapter 3); the pairwise distance
>   matrix $D_{ij}=\lVert \mathbf{x}_i-\mathbf{x}_j\rVert_2$ (Chapter 6); a
>   number of hash buckets (Chapter 4). A data set is the calligraphic
>   $\mathcal{D}$, never $D$.
> - $\Sigma$: a covariance matrix (this appendix, Chapters 2–3). It never
>   denotes summation — sums use the operator $\sum$ — and singular values are
>   the scalars $\sigma_i$, so $\Sigma$, $\sum$, and $\sigma$ do not collide.
> - $V$: the right singular-vector matrix (this appendix); the value matrix in
>   attention, $Q, K, V$ (this appendix, Chapter 10); and the vertex set $V$ of a
>   graph $G=(V,E)$ (Chapter 10). The surrounding operation — SVD, attention, or
>   graph — fixes which is meant.
> - $C$: a sample covariance matrix (Chapter 2); a contact map
>   $C_{ij}=\mathbb{1}[D_{ij}<\tau]$ (Chapter 6).
> - $L$: the graph Laplacian $L=D-W$ (Chapter 3); a sequence length
>   (Chapter 4). The training objective is the calligraphic $\mathcal{L}$ and a
>   per-example loss is $\ell$, so $L$ is never a loss.
> - $m$: a margin (triplet loss, Chapter 3); a number of allowed mismatches
>   (Chapter 4); an Adam first-moment estimate $m_t$ (this appendix). The number
>   of modalities is the distinct uppercase $M$.
> - $p, q$: probability mass / density functions $p(\cdot), q(\cdot)$ (this
>   appendix); the node2vec return and in-out walk parameters (Chapter 3). The
>   t-SNE affinity distributions are the distinct uppercase $P, Q$, and the
>   variational posterior is $q_\phi(\mathbf{z}\mid\mathbf{x})$.
> - $W$: a projection / weight matrix (Chapters 3, 10); a graph affinity matrix
>   $W_{ij}\ge 0$ (Chapter 3).
> - $g$: the number of genes (Chapter 8); the decoder $g_\theta$ (this
>   appendix); a rigid motion $g\cdot x$ of 3D coordinates (Chapter 6).
> - $\tau$: a temperature (contrastive objectives, Chapters 3, 9); a contact
>   threshold (Chapter 6).
> - $\sigma$: the logistic sigmoid $\sigma(\cdot)$ (Chapters 3, 10); a singular
>   value $\sigma_i$ or a standard deviation (this appendix).
