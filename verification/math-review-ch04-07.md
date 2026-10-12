# Math review — Chapters 4–7 (independent verification)

Scope: `chapters/04-dna-rna.qmd`, `chapters/05-proteins-sequence.qmd`,
`chapters/06-protein-structure.qmd`, `chapters/07-molecules-chemistry.qmd`.

Method: every numbered display equation with an `eq-ch04-…`…`eq-ch07-…` label was
audited for (1) notation (defined at first use, no collision with Appendix A,
consistent type/shape), (2) equation validity (dimensional consistency; what is
optimized/specified and over what; match to the cited source; derivation steps),
(3) cross-references (`@eq-`/`@fig-`/`@tbl-` resolve; every label referenced), and
(4) claims (`improves/outperforms` derived or cited, else downgraded). Labels were
preserved, the `$$ … $$ {#eq-…}` syntax was preserved (label after the closing
`$$`), and no label was renamed or renumbered. No `quarto render` was run.

**Totals: 36 numbered equations checked — 26 ok, 7 fixed, 3 flagged** (plus
notation/claim flags recorded below).

## Findings table

| Chapter | Label | Verdict | Note |
|---|---|---|---|
| 4 | eq-ch04-onehot | ok | $O\in\{0,1\}^{L\times4}$, row sums $1$; equidistance $\lVert u-v\rVert_2^2=2$ for distinct one-hots is correct, so all base pairs are equidistant. |
| 4 | eq-ch04-kmer-profile | ok | $\phi_k(s)\in\mathbb{N}^{4^k}$; dimension $4^k$ and sparsity $\lVert\phi_k(s)\rVert_0\le L-k+1\ll 4^k$ correct (window $s_{i:i+k-1}$ spans exactly $k$ symbols, count has $L-k+1$ terms). |
| 4 | eq-ch04-kmer-hash | ok | $\psi_B$ is a linear pooling of $\phi_k$; collision law $\Pr=1/B$ and expected colliding pairs $\binom{N_{\mathrm{obs}}}{2}/B$ for distinct observed k-mers meant as a uniform-hash expectation; halving claim correct. |
| 4 | eq-ch04-mismatch | **fixed** | Feature map and Hamming-ball size $\sum_{j=0}^m\binom{k}{j}3^j$ correct, but prose said the kernel "counts pairs … that agree within Hamming radius $m$". The inner product actually counts, per k-mer $u$, occurrence pairs each within radius $m$ of $u$; such a pair contributes only when the two windows differ in $\le 2m$ positions (Hamming balls intersect iff distance $\le 2m$). Prose corrected. |
| 4 | eq-ch04-cnn-filter | ok | $W_f\in\mathbb{R}^{k\times4}$, $H\in\mathbb{R}^{(L-k+1)\times F}$; pre-activation equals $\langle W_f,O_{j:j+k-1}\rangle$. |
| 4 | eq-ch04-attention | **fixed** | Equation correct and matches `@eq-appa-attention`. The trailing parenthetical claimed $K,V$ were "unrelated to the singular-vector notation of Appendix A", which is wrong: Appendix A's singular-vector matrices are $U,V$, and its attention equation already uses the same $Q,K,V$. Replaced with a pointer to `@eq-appa-attention`. |
| 4 | eq-ch04-mlm-dna | ok | Masked NLL, minimized over $\theta$ on corpus $\mathcal{D}$; masking set is calligraphic $\mathcal{M}$, distinct from the PSSM $M$ of Ch. 5. |
| 4 | eq-ch04-dna-embed | ok | Pooled encoder output; $f_\theta$ matches Appendix A. |
| 4 | eq-ch04-rc-equiv | **fixed** | Equivariance "up to a fixed invertible $\mathbf{P}$" is stated correctly; added the derived consequence that, since $\mathrm{rc}$ is an involution, applying the equation twice forces $\mathbf{P}^2=\mathbf{I}$ on the image, so $\mathbf{P}$ is itself an involution (reversal permutation / identity both satisfy this). |
| 5 | eq-ch05-pssm | **flagged** | Log-odds $M_{i,a}=\log(p_{i,a}/q_a)$ with $M\in\mathbb{R}^{L\times20}$ is correct (positive iff enriched) and matches PSI-BLAST's convention. Notation: the symbol $M$ collides with Appendix A's $M$ = "number of modalities"; it is not listed among the sanctioned overloads. Recommend renaming (e.g. $\mathbf{M}\!\to\!$ PSSM-specific letter) or adding $M$ to the Appendix A overload list. |
| 5 | eq-ch05-protvec | ok | Pooled 3-mers $f(s)=\frac1n\sum_j v_{w_j}\in\mathbb{R}^{100}$; order-invariance stated correctly; $20^3=8000$ correct. |
| 5 | eq-ch05-ar-loss | ok | Autoregressive NLL with softmax head $W_{\mathrm{out}}\in\mathbb{R}^{20\times d}$, minimized over $\theta$; matches the UniRep mLSTM objective. |
| 5 | eq-ch05-mlm-protein | ok | Masked NLL over corpus $\mathcal{D}$, categorical over the 20 residues; masking set calligraphic $\mathcal{M}$ avoids the PSSM $M$. |
| 5 | eq-ch05-mut-effect | ok | Telescoping verified: for an autoregressive model $\log p_\theta(s')-\log p_\theta(s)=\sum_{i=j}^{L}\log\frac{p_\theta(s'_i\mid s'_{<i})}{p_\theta(s_i\mid s_{<i})}$ because $s'_{<j}=s_{<j}$ cancels the prefix terms; reduction to the single-position log-ratio holds when later conditionals are unchanged. |
| 5 | eq-ch05-protein-embed | ok | Pooled contextual embedding $f_\theta(s)\in\mathbb{R}^d$. |
| 5 | eq-ch05-probe | ok | Binary cross-entropy probe; convex in $(\mathbf{w},b)$ for fixed features, so the optimum is unique — correct. |
| 6 | eq-ch06-distance-matrix | ok | $D_{ij}=\lVert\mathbf{x}_i-\mathbf{x}_j\rVert_2$, consistent with Appendix A's Ch. 6 overload of $D$. |
| 6 | eq-ch06-distance-invariance | ok | Translation cancels and $\lVert R y\rVert_2=\lVert y\rVert_2$; matches $\mathbf{R}\in SO(3)$ invariance. |
| 6 | eq-ch06-contact-map | ok | $C_{ij}=\mathbb{1}[D_{ij}<\tau]$ with $\tau>0$; matches Appendix A's Ch. 6 overload of $C$. |
| 6 | eq-ch06-graph | ok | Edge rule from $D$ alone; edge set therefore rigid-motion invariant. |
| 6 | eq-ch06-permutation-invariance | ok | Permutation-invariant readout definition is correct. |
| 6 | eq-ch06-invariance | ok | Scalar invariance $f(RP+\mathbf{1}_N t^\top)=f(P)$ correct. |
| 6 | eq-ch06-equivariance | ok | Coordinate equivariance $f(RP+\mathbf{1}_N t^\top)=R f(P)+\mathbf{1}_N t^\top$ is a genuine $SE(3)$ group action; shapes consistent ($f(P)\in\mathbb{R}^{N\times3}$). |
| 6 | eq-ch06-invariant-scalarization | ok | Norms and inner products invariant under $R$; correct. |
| 6 | eq-ch06-gvp | **flagged** | Shapes ($W_m\!\in\!\mathbb{R}^{m\times n}$, $W_\mu\!\in\!\mathbb{R}^{\mu\times n}$, $W_\nu\!\in\!\mathbb{R}^{\mu\times\nu}$) and the equivariance argument (gate depends only on invariant $\mathbf{s}$; $W_\nu(RV)=R(W_\nu V)$) are correct. However the scalar update omits the row-wise vector-norm term $\lVert V\rVert_2$ used in the cited GVP (Jing et al. 2021); it is a valid simplified/special form, not the full layer. Flagged for fidelity to the source. |
| 6 | eq-ch06-egnn-message | ok | Message built from invariant squared distance and optional edge attributes; correct. |
| 6 | eq-ch06-egnn-update | **fixed** | Update formulas correct (translation-invariant because displacements are coordinate differences; rotation-equivariant). The normalization constant was denoted $C$, colliding with the contact map $C$ defined earlier in the same chapter. Renamed the constant to $c$ (equation and prose) to remove the within-chapter collision with the Appendix-A-fixed contact-map symbol. |
| 6 | eq-ch06-gearnet-edge | ok | Distances and bond angles are rigid-motion invariant; correct. |
| 6 | eq-ch06-inverse-folding | ok | ProteinMPNN random-order autoregressive NLL, $\pi\sim\mathrm{Unif}(S_N)$, over encoder+decoder $\theta$; geometric inputs invariant, so $p_\theta(\mathbf{a}\mid RP+\mathbf{1}_N t^\top)=p_\theta(\mathbf{a}\mid P)$. |
| 7 | eq-ch07-ecfp-label | ok | Morgan/ECFP label recursion over an *unordered* neighbor multiset; atom-permutation invariant. |
| 7 | eq-ch07-ecfp | **fixed** | Bitwise-OR hashing correct; sparsity $n(R+1)\le b$ and birthday collision $\binom{m}{2}/b$ correct. Molecule symbol $M$ was used before it was defined; added "For a molecule $M$" at first use. (See notation flag: molecule $M$ still overloads Appendix A's $M$.) |
| 7 | eq-ch07-tanimoto | ok | For binary vectors $\langle u,v\rangle$ = #shared bits, $\lVert u\rVert_1+\lVert v\rVert_1-\langle u,v\rangle$ = #union bits; so $T$ = intersection/union $\in[0,1]$. Correct. |
| 7 | eq-ch07-mpnn | **fixed** | MPNN update correct; message function was denoted $M$, colliding with the molecule $M$ used in the same chapter. Renamed the message function to $\mathrm{Msg}$ (equation and prose). |
| 7 | eq-ch07-mol-readout | ok | Permutation-invariant readout; correct. |
| 7 | eq-ch07-dmpnn | **fixed** | D-MPNN update and the exclusion $k\in\mathcal{N}(i)\setminus\{j\}$ (removing the reverse edge $j\to i$) are correct; message function renamed $M\to\mathrm{Msg}$ as above. |
| 7 | eq-ch07-mol-prediction | ok | Empirical risk over $\mathcal{D}=\{(M,y_M)\}$, minimized over encoder $\theta$ and head $\phi$; QSPR squared error / QSAR cross-entropy correctly instantiated; $\theta=\varnothing$ for fingerprints. (Molecule $M$ overload flagged.) |

## Notation audit

Central symbols are fixed in [Appendix A](../chapters/appendix-a-math.qmd). Symbols
introduced or reinterpreted by Chapters 4–7:

| Symbol | Meaning in Ch. 4–7 | First defined | Consistent with Appendix A? |
|---|---|---|---|
| $\mathcal{A}$ | DNA alphabet (Ch. 4); 20-letter amino-acid alphabet (Ch. 6) | Ch. 4 eq-ch04-onehot | **Flag**: cross-chapter overload of $\mathcal{A}$; Ch. 5 uses $\mathcal{P}$ for the protein alphabet, so Ch. 6 and Ch. 5 disagree. Not listed in Appendix A. |
| $\boldsymbol{\phi}_k,\ \psi_B$ | k-mer profile / hashed sketch | Ch. 4 eq-ch04-kmer-profile, eq-ch04-kmer-hash | new, internally consistent. |
| $\mathbf{O}$ | one-hot matrix $\{0,1\}^{L\times4}$ | Ch. 4 eq-ch04-onehot | new. |
| $\mathbf{K}$ | attention key matrix | Ch. 4 eq-ch04-attention | ok: Appendix A already defines $Q,K,V$ in `@eq-appa-attention`; distinct from integer $K$ (negatives/classes). |
| $\mathbf{P}$ | fixed invertible RC map (Ch. 4) | Ch. 4 eq-ch04-rc-equiv | **Flag**: overloads Ch. 6's coordinate matrix $\mathbf{P}$ and Appendix A's t-SNE affinities $P,Q$. |
| $\mathbf{S}\in\mathcal{P}^{N\times L}$ | multiple sequence alignment (Ch. 5) | Ch. 5 prose | new; unused after definition (minor). |
| $M\in\mathbb{R}^{L\times20}$ | PSSM log-odds matrix (Ch. 5) | Ch. 5 eq-ch05-pssm | **Flag**: collides with Appendix A's $M$ = number of modalities. |
| $M$ | molecule (Ch. 7) | Ch. 7 eq-ch07-ecfp (now defined at first use) | **Flag**: collides with Appendix A's $M$ = number of modalities. |
| $\mathrm{Msg}$ | learned message function (Ch. 7) | Ch. 7 eq-ch07-mpnn | **Fixed**: introduced to replace the message-function $M$, which collided with the molecule $M$. Not in Appendix A (which assigns the Ch. 10 message function to $\phi$); $\phi$ is already the head-parameter symbol in eq-ch07-mol-prediction. |
| $C$ vs $c$ | contact map (Ch. 6); normalization constant (Ch. 6) | Ch. 6 eq-ch06-contact-map / eq-ch06-egnn-update | **Fixed**: EGNN constant renamed $C\to c$ so the Ch. 6 contact-map $C$ (Appendix-A-fixed) is unambiguous. |
| $R$ | permutation-invariant readout (Ch. 6, Ch. 7) | Ch. 6 eq-ch06-permutation-invariance | **Flag**: overloads Appendix A's $R\in SO(3)$ rotation (Ch. 6) and risk $R(\theta)$; within Ch. 6 it coexists with the rotation matrix $\mathbf{R}$. Renaming the readout would need cross-chapter agreement, so left as a flag. |
| $\mathcal{V},\mathcal{E}$ | vertex/edge sets (Ch. 6, Ch. 7) | Ch. 6 eq-ch06-graph | minor style difference from Appendix A's plain $V,E$ in $G=(V,E)$. |

No symbol was found to have inconsistent type/shape within an equation: all
displayed shapes are mutually consistent (verified for k-mer, hashing, CNN,
attention, PSSM, ProtVec, GVP, EGNN, ECFP and Tanimoto).

## Cross-reference audit

- All 36 `eq-ch04-…`…`eq-ch07-…` labels are defined exactly once and are unique
  book-wide (no collisions with other chapters or Appendix A).
- Every one of the 36 labels is referenced at least once — in-file, and several
  also from `appendix-c-glossary.qmd`. No dangling `@eq-` reference.
- `@fig-`/`@tbl-` targets resolve: `fig-tokenization`, `tbl-dna-models` (Ch. 4),
  `fig-plm-transfer`, `tbl-plm-models` (Ch. 5), `fig-coord-graph`, `tbl-equivariance`
  (Ch. 6), `fig-mol-graph`, `tbl-fingerprint-learned` (Ch. 7) are each defined once
  and referenced.
- All Pandoc citation keys used in Ch. 4–7 resolve in `references.bib` ∪
  `bib/*.bib`. The `$$ … $$ {#eq-…}` syntax (label after closing `$$`) holds for
  every display; `$$` delimiters are balanced (Ch. 4: 18, Ch. 5: 14, Ch. 6: 26,
  Ch. 7: 14).
- The new `@eq-appa-attention` reference in Ch. 4 resolves (Appendix A defines it)
  and follows the existing book convention of cross-file references (e.g. the
  glossary cites `@eq-appa-kl`, `@eq-appa-mi`).

## Claim audit

- **Ch. 5 (fixed).** "a linear probe … is usually more **robust than** fine-tuning"
  was an unbacked comparative claim. Downgraded to the underlying mechanism (the
  probe has far fewer trainable parameters, so it can overfit less with few labels,
  while fine-tuning can recover more capacity with many labels).
- **Ch. 7 (flagged).** "Random splits massively overstate performance relative to
  *scaffold* splits" has no direct citation (it points to Ch. 11). Recommend citing a
  primary source on scaffold splitting (e.g. MoleculeNet) or marking it as a
  reporting convention.
- Confirmed supported/hedged claims: gapped k-mers "improved regulatory-sequence
  prediction … [@ghandi2014enhanced]"; DNABERT "$k=6$ gave the best downstream
  performance … [@ji2021dnabert]"; DNABERT-2 "improving efficiency and
  cross-species transfer [@zhou2024dnabert2]"; Chemprop/D-MPNN "matches or exceeds
  … although the size of the advantage depends on the dataset [@yang2019analyzing]";
  ChemBERTa "competitive property predictors [@chithrananda2020chemberta]"; MolBERT
  "improving robustness … [@fabian2020molbert]"; ESM-2 "improves monotonically on
  structure prediction [@lin2023evolutionary]"; Ankh "fewer parameters and less
  compute … [@elnaggar2023ankh]". All carry a primary citation or are explicitly
  attributed/hedged.

## Special-attention items (confirmed correct)

- k-mer dimension/sparsity (Ch. 4): $4^k$ features, $\lVert\phi_k\rVert_0\le L-k+1$ — correct.
- One-hot equidistance (Ch. 4): $\lVert u-v\rVert_2^2=2$ — correct.
- Hashing collision bound (Ch. 4): $\binom{N_{\mathrm{obs}}}{2}/B$ — correct.
- Attention/softmax (Ch. 4): scaled dot-product with $\sqrt{d_k}$, softmax over keys — correct.
- Reverse-complement equivariance (Ch. 4): correct; involution consequence added.
- PSSM log-odds (Ch. 5): $M_{i,a}=\log(p_{i,a}/q_a)$ — correct.
- Mutation log-ratio telescoping (Ch. 5): verified.
- Rotation/translation invariance, permutation invariance, GVP/EGNN equivariance (Ch. 6): all correct (GVP flagged only as a simplification vs source).
- Inverse-folding objective (Ch. 6): ProteinMPNN random-order NLL — correct.
- ECFP hashing and Tanimoto (Ch. 7): correct.
- MPNN/D-MPNN updates (Ch. 7): correct; message function renamed for clarity.

## Unresolved / author attention

1. Symbol overloads not editable from Ch. 4–7 alone: $M$ (Ch. 5 PSSM, Ch. 7
   molecule) vs Appendix A's $M$ (number of modalities); $\mathcal{A}$ (Ch. 4 DNA,
   Ch. 6 protein) vs Ch. 5's $\mathcal{P}$; $R$ readout vs Appendix A's rotation/risk;
   $\mathbf{P}$ (Ch. 4 RC map) vs Ch. 6 coordinates. Resolve by adding these to the
   Appendix A overload list or renaming in a coordinated pass.
2. Ch. 6 GVP equation is the simplified form (no vector-norm term); decide whether to
   present the full Jing et al. (2021) layer or label it as simplified.
3. Ch. 7 scaffold-split claim needs a citation.
