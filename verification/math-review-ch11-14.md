# Math review — Chapters 11–14 (independent verifier)

Scope: every numbered display equation in
`chapters/11-evaluation-pitfalls.qmd`, `chapters/12-interpretability-visualization.qmd`,
`chapters/13-foundation-models.qmd`, `chapters/14-applications.qmd`
(labels `eq-ch11-…` … `eq-ch14-…`). Canonical symbols per `chapters/appendix-a-math.qmd`.
Each equation was audited for (1) notation, (2) dimensional/derivation correctness and what is
optimised over what, (3) cross-references, (4) claims. HARD constraints respected: label
prefixes kept, `$$ … $$ {#eq-…}` syntax kept, no labels renamed/renumbered, no other chapters or
`references.bib` / `bib/*.bib` touched.

**Contents:** 30 numbered equations (Ch11: 9, Ch12: 7, Ch13: 7, Ch14: 7).
**Verdicts:** 26 ok, 4 fixed, 0 flagged at the equation level (chapter-level flags listed below).
All 30 labels are referenced at least once; all `@eq-…` references resolve in-file; all
`[@key]` citations used by these equations resolve in `references.bib` ∪ `bib/*.bib`.

## Findings

| Chapter | Label | Verdict | Note |
|---|---|---|---|
| 11 | eq-ch11-linear-probe | ok | $\ell_2$-regularised logistic probe; shapes $\mathbf{w}\in\mathbb{R}^d$, $b\in\mathbb{R}$ consistent with Appendix A ($\sigma$, $\lambda$); states correctly that only $(\mathbf{w},b)$ are fit with the encoder frozen. |
| 11 | eq-ch11-probing-bound | ok | Fano $H(Y\mid\hat Y)\le H_b(P_e)+P_e\log(K-1)$ plus DPI $Y\to\mathbf{x}\to\hat Y$ yields the stated MI lower bound; binary case $K=2$ correctly drops the last term. One-sidedness correctly stated. |
| 11 | eq-ch11-knn | fixed | Renamed the distance $d(\cdot,\cdot)\to D(\cdot,\cdot)$ (and "choice of $d$"$\to$"choice of $D$"): lowercase $d$ was used for the embedding dimension in the same sentence and collides with Appendix A, where $D$ is the distance function. |
| 11 | eq-ch11-silhouette | ok | $s(i)=(b(i)-a(i))/\max\{a(i),b(i)\}$, $S\in[-1,1]$ standard; signs/interpretation correct. |
| 11 | eq-ch11-homology-split | ok | Condition ($c(i)\neq c(j)$ across folds) is exactly "no cluster straddles a fold"; random split = identity clustering, correctly noted. |
| 11 | eq-ch11-precision-recall | ok | Prec/Rec(=TPR)/FPR definitions correct; the $\mathrm{Prec}=1$ empty-positive convention is stated. |
| 11 | eq-ch11-auprc | ok | Step-sum equals average precision under the stated step-interpolation convention; the bare integral $\int_0^1\mathrm{Prec}(r)\,dr$ differs from AP under trapezoidal interpolation (minor, convention-dependent — no change). |
| 11 | eq-ch11-ece | ok | Standard binned ECE; the two bias arguments (within-bin cancellation of over/under-confidence; $M$-dependent plug-in bias/variance) are correct and cited [@kumar2019verified]. |
| 11 | eq-ch11-alignment-uniformity | ok | Matches Wang & Isola alignment ($\alpha=2$) and uniformity ($t=2$); interpretation of low loss = close positives / spread features correct. |
| 12 | eq-ch12-trustworthiness | ok | Matches Venna–Kaski normalisation $2/(nk(2n-3k-1))$ and rank convention (rank 1 = nearest); $T\in[0,1]$, $=1$ on exact neighbour-set agreement. |
| 12 | eq-ch12-continuity | ok | Correct dual of trustworthiness using projection ranks $\hat r(i,j)$ and $N_k(i)\setminus\hat N_k(i)$. |
| 12 | eq-ch12-probe | ok | Same linear-probe objective as Ch11; notation consistent (no Appendix A collision). |
| 12 | eq-ch12-probe-selectivity | ok | Selectivity $=\mathrm{acc}_{\mathrm{real}}-\mathrm{acc}_{\mathrm{ctrl}}$ (Hewitt–Liang-style); "must be positive and large vs sampling error" correctly stated, cited [@belinkov2022probing]. |
| 12 | eq-ch12-saliency | ok | $\mathbf{S}=\nabla_{\mathbf{x}}g$, $\mathbf{M}=\mathbf{x}\odot\nabla_{\mathbf{x}}g$; Hadamard product per Appendix A. |
| 12 | eq-ch12-integrated-gradients | ok | Correct straight-path IG; completeness $\sum_j\mathrm{IG}_j(\mathbf{x})=g(\mathbf{x})-g(\mathbf{x}')$ holds (verified by the fundamental theorem of calculus along the path). |
| 12 | eq-ch12-latent-direction | ok | Mean-difference direction + unit projection; held-out validation and confounder caveat present. |
| 13 | eq-ch13-probe | ok | Linear probe over $d+1$ parameters; convexity claim correct for logistic+cross-entropy and identity+squared error. |
| 13 | eq-ch13-mlm | ok | Masked NL objective: sum over masked positions of $-\log p_\theta(x_i\mid x_{\setminus M})$; what is optimised (expectation over corpus and mask set) stated. |
| 13 | eq-ch13-ar | ok | Left-to-right NLL $-\sum_t\log p_\theta(x_t\mid x_{<t})$; correct. |
| 13 | eq-ch13-scaling-law | fixed | Equation unchanged, but its attribution was wrong: Kaplan et al. (Eq. 1.1/3.1, arXiv:2001.08361) report $L(N)=(N_c/N)^{\alpha_N}$ with **no** additive floor; the irreducible-loss floor $L_\infty$ is the Hoffmann-style extension ($L(N,D)=E+A/N^\alpha+B/D^\beta$). Prose now attributes the power law to Kaplan and the floor to Hoffmann et al. |
| 13 | eq-ch13-scaling-fit | ok | $\log(L-L_\infty)=\alpha_N\log N_c-\alpha_N\log N$ derived correctly from the closed form; $\alpha_N$ = negative slope of $\log(L-L_\infty)$ vs $\log N$. |
| 13 | eq-ch13-compute | ok | $2ND$ forward + $2\times$ backward $=6ND$; matches Kaplan's $C\approx 6NBS$ with $D=BS$ training tokens. Correct. |
| 13 | eq-ch13-compute-optimal | ok | $\arg\min_{N,D:\,6ND\le C}L(N,D)$; constraint mirrors eq-ch13-compute; the $C^{a},C^{b}$ exponents are explicitly labelled "reported". |
| 14 | eq-ch14-vep-score | fixed | Masked-marginal LLR correct; softmax normalizer cancels giving $z_{a_i'}-z_{a_i}$ (verified). Adjacent claim text changed "invariant to context-dependent **rescaling** of the logits"$\to$"**additive shift**": the normalizer is an additive constant in logit space, so the ratio is invariant to a shift, not to a multiplicative rescaling. (Bib URL defect flagged below.) |
| 14 | eq-ch14-vep-reg | ok | $\Delta s_{\mathrm{reg}}=g_\phi(\mathbf{u}')-g_\phi(\mathbf{u})$; scalar, sign = direction, correctly stated. |
| 14 | eq-ch14-qsar | ok | Squared-error regression; equivalence to Gaussian-noise MLE (Appendix A) correct; classification replacement noted. |
| 14 | eq-ch14-ef | ok | $\mathrm{EF}_k=(\#\text{actives in top }k/k)/(A/T)$; equals 1 for random ranking (verified); applicable only when $A/T<1$. |
| 14 | eq-ch14-kg | fixed | Renamed TransE vectors $\mathbf{h},\mathbf{r},\mathbf{t}\to\mathbf{e}_h,\mathbf{e}_r,\mathbf{e}_t$ to match Appendix A's canonical KG-embedding symbols (and to avoid colliding with $\mathbf{h}_v^{(l)}$, the hidden representation). Score $f_r(h,t)=-\lVert\mathbf{e}_h+\mathbf{e}_r-\mathbf{e}_t\rVert_2$ correct. |
| 14 | eq-ch14-case-score | ok | Identical to eq-ch14-vep-score, correctly cross-referenced and fixed as the single ranked quantity. |
| 14 | eq-ch14-metrics | ok | $\mathrm{AUROC}=P(s^+>s^-)+\tfrac12P(s^+{=}s^-)$ (tie-corrected) and $\rho_s=1-6\sum d_i^2/(n(n^2-1))$ (no-ties form, tie-corrected form noted); both rank-based, so calibration-invariant — correct. |

## Chapter-level flags (not equation-level)

1. **Notation overloads absent from the Appendix A canonical table.** Appendix A states its
   overload list is exhaustive, but these chapters introduce locally-defined symbols whose
   meanings are not listed there. Recommend the coordinator add them to Appendix A (I may not
   edit the appendix):
   - Ch13: $N$ = non-embedding parameter count (Appendix A: number of atoms/residues/nodes);
     $D$ = training tokens (Appendix A: distance function / degree matrix / distance matrix / hash
     buckets); $L$ = test loss (Appendix A: graph Laplacian / sequence length);
     $M$ = random mask-index set (Appendix A: number of modalities).
   - Ch11: $P,N$ = number of positive/negative examples (used in eq-ch11-precision-recall and
     eq-ch11-auprc); $M$ = number of ECE bins. These are standard but are not in Appendix A.
   - Ch12: $C(k)$ = continuity and $T(k)$ = trustworthiness collide with Appendix A's $C$
     (covariance / contact map); standard in the visualisation literature, but unlisted.
   - Ch14: $\phi$ reused for the regulatory model parameters $g_\phi$ (Appendix A: variational /
     encoder parameters; message function); $\mathbf{u}$ reused for the reference sequence window
     (Appendix A: generic vectors).
   These are documented overloads, not mathematical errors; the preferred fix is an Appendix A
   update, not a rename.

2. **Citation defect in `bib/frontier-apps.bib` (cannot fix — bib files are out of scope).**
   `meier2021language` has `url = https://arxiv.org/abs/2107.07455`, but that arXiv record is
   Malinin et al., *Shifts: A Dataset of Real Distributional Shift* — not Meier et al. I verified
   there is no arXiv record for the Meier title, and the correct stable identifier is the bioRxiv
   DOI **10.1101/2021.07.09.450648** (title/authors confirmed via Crossref). This key backs the
   masked-marginal claim in eq-ch14-vep-score. Suggest replacing the URL with
   `https://doi.org/10.1101/2021.07.09.450648`.

3. **Non-math formatting observation.** `13-foundation-models.qmd:5` and
   `14-applications.qmd:5` each begin with a body-level H1 that duplicates the YAML `title:`;
   Ch11/Ch12 do not. Out of the equation scope, so left unchanged, but flagged for a consistency
   pass.

## Claim audit summary

Every "improves/outperforms/rival/beats" claim in these four chapters is either cited or hedged as
"reported". No unsupported superiority claim required downgrading at the equation level. A
dangling referent ("this sample-efficiency argument", `13-foundation-models.qmd:214`) has no
antecedent in the chapter; it is descriptive prose, not an equation claim, so it was left for the
prose editor.
