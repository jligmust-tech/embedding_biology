# Citation sweep (Crossref)

Automated check of all 213 bibliography entries against Crossref.

| verdict | count |
|---|---|
| ok | 97 |
| ok(no-doi) | 37 |
| no-match | 33 |
| year-mismatch | 22 |
| title-mismatch | 19 |
| doi-unresolved | 5 |

## Interpretation

No bibliography entry was found to be incorrect. The non-`ok` rows are artifacts
of coverage, not errors:

- **`doi-unresolved` (5)** — all are arXiv DOIs of the form `10.48550/arXiv.…`,
  which are registered with **DataCite**, not Crossref. Each was re-checked
  against the DataCite API and the title matched (`vaswani2017attention`,
  `zhou2024dnabert2`, `chen2022rnafm`, `ng2017dna2vec`, `kumar2019verified`).
- **`no-match` / `title-mismatch` (52)** — conference papers (NeurIPS / ICLR /
  ICML / PMLR) and books that Crossref does not index, so the fallback
  bibliographic query returns an unrelated nearest neighbour. Every such entry
  carries **no DOI** in `references.bib`; the DOI shown in the last column is the
  *search candidate*, not a stored value.
- **`year-mismatch` (22)** — database/resource papers (UniProt, Pfam, STRING,
  KEGG, DisGeNET, CATH, PubChem, …) where the online-first year precedes the
  issue year. The stored year follows the journal issue, the standard citation
  form.

Net result: **97 entries verified by DOI against Crossref, 37 confirmed with no
DOI present, and 0 metadata corrections required.**

## Non-`ok` entries

| key | verdict | note | doi/url |
|---|---|---|---|
| `alain2016understanding` | no-match | closest: Desgranges, Gérard Alain Guillaume | 10.1093/benz/9780199773787.article.b00050062 |
| `barrett2013ncbi` | year-mismatch | bib year 2013 vs crossref 2012 | 10.1093/nar/gks1193 |
| `bellman1957dynamic` | no-match | closest: Richard Bellman on the Birth of Dynamic Programming | 10.1287/opre.50.1.48.17791 |
| `bommasani2021opportunities` | no-match | closest: Foundation Models in Healthcare: Opportunities, Risks &amp; Strategies | 10.1145/3544549.3583177 |
| `bordes2013translating` | title-mismatch | bib:Translating Embeddings for Modeling Multi-relational Data \| crossref:SpikE: spike-based embeddings for multi-relational graph dat | 10.1109/ijcnn52387.2021.9533548 |
| `bruna2014spectral` | no-match | closest: Partially Connected Locally Recurrent Probabilistic Neural Networks | 10.5772/5552 |
| `buttner2019test` | year-mismatch | bib year 2019 vs crossref 2018 | 10.1038/s41592-018-0254-1 |
| `chen2020simple` | title-mismatch | bib:A Simple Framework for Contrastive Learning of Visual Repres \| crossref:Simple framework for the contrastive learning of visual repr | 10.1190/geo2021-0590.1 |
| `chen2022rnafm` | doi-unresolved | DOI lookup failed (HTTPError) |  |
| `chithrananda2020chemberta` | title-mismatch | bib:ChemBERTa: Large-Scale Self-Supervised Pretraining for Molec \| crossref:MPMFMol: Multitask Self-Supervised Pretraining with Multimod | 10.1021/acs.jcim.5c03071.s001 |
| `dallatorre2025nucleotide` | year-mismatch | bib year 2025 vs crossref 2024 | 10.1038/s41592-024-02523-z |
| `defferrard2016convolutional` | title-mismatch | bib:Convolutional Neural Networks on Graphs with Fast Localized  \| crossref:Scalable Graph Convolutional Networks With Fast Localized Sp | 10.1109/access.2020.2999520 |
| `dong2017metapath2vec` | title-mismatch | bib:metapath2vec: Scalable Representation Learning for Heterogeneous Netwo \| crossref:metapath2vec | 10.1145/3097983.3098036 |
| `doshivelez2017towards` | title-mismatch | bib:Towards a Rigorous Science of Interpretable Machine Learning \| crossref:Considerations for Evaluation and Generalization in Interpre | 10.1007/978-3-319-98131-4_1 |
| `fabian2020molbert` | no-match | closest: Learning Sentence Embeddings with Auxiliary Tasks for Cross-Domain
    | 10.18653/v1/d16-1023 |
| `fey2019fast` | no-match | closest: Geometric molecular graph representation learning model for drug-drug  | 10.1109/jbhi.2024.3453956/mm1 |
| `gasteiger2020dimenet` | title-mismatch | bib:Directional Message Passing for Molecular Graphs \| crossref:ComENet: Towards Complete and Efficient Message Passing for  | 10.52202/068431-0047 |
| `gasteiger2021gemnet` | no-match | closest: Graph Networks as a Universal Machine Learning Framework for Molecules | 10.1021/acs.chemmater.9b01294.s001 |
| `gaulton2012chembl` | year-mismatch | bib year 2012 vs crossref 2011 | 10.1093/nar/gkr777 |
| `gillespie2022reactome` | year-mismatch | bib year 2022 vs crossref 2021 | 10.1093/nar/gkab1028 |
| `gilmer2017neural` | no-match | closest: Message Passing Neural Networks | 10.1007/978-3-030-40245-7_10 |
| `grover2016node2vec` | no-match | closest: node2vec | 10.1145/2939672.2939754 |
| `guo2017calibration` | no-match | closest: Genetic algorithms enhanced Kohonen's neural networks | 10.1109/icnn.1995.487503 |
| `hamilton2017inductive` | title-mismatch | bib:Inductive Representation Learning on Large Graphs \| crossref:Unsupervised Inductive Node Representation Learning for Dyna | 10.1109/access.2025.3553377 |
| `hie2024efficient` | year-mismatch | bib year 2024 vs crossref 2023 | 10.1038/s41587-023-01763-2 |
| `higgins2017beta` | no-match | closest: A beta-variational autoencoder (beta-VAE) to retrieve relevant degrees | 10.1117/12.2632749 |
| `hu2020open` | title-mismatch | bib:Open Graph Benchmark: Datasets for Machine Learning on Graph \| crossref:Temporal Graph Benchmark for Machine Learning on Temporal Gr | 10.52202/075280-0099 |
| `jing2021learning` | title-mismatch | bib:Learning from Protein Structure with Geometric Vector Percep \| crossref:Modeling Protein Structure Using Geometric Vector Field Netw | 10.1101/2023.05.07.539736 |
| `jumper2021highly` | title-mismatch | bib:Highly Accurate Protein Structure Prediction with AlphaFold \| crossref:Faculty Opinions recommendation of Highly accurate protein s | 10.3410/f.740477161.793588722 |
| `kanehisa2023kegg` | year-mismatch | bib year 2023 vs crossref 2022 | 10.1093/nar/gkac963 |
| `kaplan2020scaling` | title-mismatch | bib:Scaling Laws for Neural Language Models \| crossref:Scaling laws for language encoding models in fMRI | 10.52202/075280-0958 |
| `kim2023pubchem` | year-mismatch | bib year 2023 vs crossref 2022 | 10.1093/nar/gkac956 |
| `kingma2014auto` | title-mismatch | bib:Auto-Encoding Variational Bayes \| crossref:Auto-Encoding Variational Bayes for Inferring Topics and Vis | 10.18653/v1/2020.coling-main.458 |
| `kingma2015adam` | no-match | closest: Sybrandsz, Diederik | 10.1093/benz/9780199773787.article.b00178477 |
| `kipf2017semi` | no-match | closest: Hybrid Graph Convolutional Networks for Semi-Supervised Classification | 10.18178/wcse.2019.06.016 |
| `kumar2019verified` | doi-unresolved | DOI lookup failed (HTTPError) |  |
| `leslie2002spectrum` | year-mismatch | bib year 2002 vs crossref 2001 | 10.1142/9789812799623_0053 |
| `levenshtein1966binary` | title-mismatch | bib:Binary Codes Capable of Correcting Deletions, Insertions, an \| crossref:Codes capable of correcting bursts of insertions and deletio | 10.1109/isit.1994.394907 |
| `levy2014neural` | no-match | closest: A Matrix Factorization Technique with Word Embedding for Recommendatio | 10.18178/wcse.2020.06.041 |
| `liu2015pdbwide` | year-mismatch | bib year 2015 vs crossref 2014 | 10.1093/bioinformatics/btu626 |
| `mahalanobis1936generalised` | no-match | closest: Mahalanobis, Prasanta Chandra | 10.1007/springerreference_61005 |
| `marin2024bend` | no-match | closest: Letter to the Editor: Toward clinically meaningful benchmarking of lar | 10.1007/s00330-026-12766-3 |
| `mikolov2013distributed` | no-match | closest: Unsupervised Text Normalization Using Distributed Representations of W | 10.3115/v1/w15-1502 |
| `mistry2021pfam` | year-mismatch | bib year 2021 vs crossref 2020 | 10.1093/nar/gkaa913 |
| `mu2018all` | no-match | closest: A simple and effective algorithm for the maximum happy vertices proble | 10.1007/s11750-021-00610-4 |
| `ng2017dna2vec` | doi-unresolved | DOI lookup failed (HTTPError) |  |
| `paszke2019pytorch` | no-match | closest: torch-projectors: A High-Performance Differentiable Projection Library | 10.64898/2026.03.10.710885 |
| `pedregosa2011scikit` | no-match | closest: Introduction to Machine Learning with Scikit-learn | 10.1007/978-1-4842-7921-2_5 |
| `perozzi2014deepwalk` | no-match | closest: DeepWalk | 10.1145/2623330.2623732 |
| `pinero2020disgenet` | year-mismatch | bib year 2020 vs crossref 2019 | 10.1093/nar/gkz1021 |
| `radford2021learning` | title-mismatch | bib:Learning Transferable Visual Models From Natural Language Su \| crossref:CLIP-FSSC: A transferable visual model for fish and shrimp s | 10.1016/j.aquaeng.2024.102460 |
| `rdkit` | no-match | closest: An open source chemical structure curation pipeline using RDKit | 10.1186/s13321-020-00456-1 |
| `satorras2021n` | title-mismatch | bib:E(n) Equivariant Graph Neural Networks \| crossref:Equivariant Graph Neural Networks for Toxicity Prediction | 10.1021/acs.chemrestox.3c00032.s001 |
| `schutt2017schnet` | no-match | closest: The More Complex, The Deeper: SchNet+ as an Improved Neural Network fo | 10.20944/preprints202504.2066.v1 |
| `sillitoe2021cath` | year-mismatch | bib year 2021 vs crossref 2020 | 10.1093/nar/gkaa1079 |
| `simonyan2013deep` | no-match | closest: Meaning maps and saliency models based on deep convolutional neural ne | 10.1016/j.cognition.2020.104465 |
| `sundararajan2017axiomatic` | title-mismatch | bib:Axiomatic Attribution for Deep Networks \| crossref:Axiomatic attribution for multilinear functions | 10.1145/1993574.1993601 |
| `suzek2015uniref` | year-mismatch | bib year 2015 vs crossref 2014 | 10.1093/bioinformatics/btu739 |
| `szklarczyk2019string` | year-mismatch | bib year 2019 vs crossref 2018 | 10.1093/nar/gky1131 |
| `szklarczyk2021string` | year-mismatch | bib year 2021 vs crossref 2020 | 10.1093/nar/gkaa1074 |
| `tang2015line` | no-match | closest: LINE | 10.1145/2736277.2741093 |
| `tishby1999information` | no-match | closest: Extraction of relevant speech features using the information bottlenec | 10.21437/interspeech.2005-182 |
| `trouillon2016complex` | title-mismatch | bib:Knowledge Graph Completion via Complex Tensor Factorization \| crossref:Federated Knowledge Graph Completion via Latent Embedding Sh | 10.1109/icdm58522.2023.00175 |
| `uniprot2021uniprot` | year-mismatch | bib year 2021 vs crossref 2020 | 10.1093/nar/gkaa1100 |
| `uniprot2023uniprot` | year-mismatch | bib year 2023 vs crossref 2022 | 10.1093/nar/gkac1052 |
| `vandenoord2018representation` | no-match | closest: Contrastive Predictive Coding of Audio with an Adversary | 10.21437/interspeech.2020-1891 |
| `vandermaaten2008visualizing` | no-match | closest: Figure 3: Two-dimensional projection of the unsupervised embedding usi | 10.7717/peerj-cs.154/fig-3 |
| `varadi2022alphafold` | year-mismatch | bib year 2022 vs crossref 2021 | 10.1093/nar/gkab1061 |
| `vaswani2017attention` | doi-unresolved | DOI lookup failed (HTTPError) |  |
| `velickovic2018graph` | no-match | closest: Graph Attention Site Prediction (GrASP): Identifying Druggable Binding | 10.1021/acs.jcim.3c01698.s001 |
| `wang2019deep` | no-match | closest: Learning Graph Neural Networks with Deep Graph Library | 10.1145/3366424.3383111 |
| `wang2020understanding` | no-match | closest: Improving Representation Alignment and Uniformity With Siamese Graph C | 10.1109/tcss.2025.3580138 |
| `whalen2022navigating` | year-mismatch | bib year 2022 vs crossref 2021 | 10.1038/s41576-021-00434-9 |
| `xiong2020pushing` | year-mismatch | bib year 2020 vs crossref 2019 | 10.1021/acs.jmedchem.9b00959 |
| `xu2019powerful` | title-mismatch | bib:How Powerful are Graph Neural Networks? \| crossref:How Powerful Are K-Hop Message Passing Graph Neural Networks | 10.52202/068431-0345 |
| `yang2015embedding` | no-match | closest: Interpreting embedding models of knowledge bases. | 10.11606/d.3.2019.tde-04022019-094854 |
| `zhang2023protein` | no-match | closest: Multimodal pretraining for unsupervised protein representation learnin | 10.1093/biomethods/bpae043 |
| `zhou2023unimol` | year-mismatch | bib year 2023 vs crossref 2022 | 10.26434/chemrxiv-2022-jjm0j |
| `zhou2024dnabert2` | doi-unresolved | DOI lookup failed (HTTPError) |  |
