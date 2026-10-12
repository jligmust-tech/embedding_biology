# Embeddings in Biology

*A Practical Guide to Representation Learning for Biological Data.*

This repository is a book written in **Quarto** and published with **GitHub
Pages**. It explains how biological entities — DNA/RNA, proteins (sequence and
structure), small molecules, single cells, multi-omics data, and biological
graphs — are turned into vector *embeddings*, and how those embeddings are
learned, evaluated, and interpreted.

## Structure

```
_quarto.yml                     Book configuration
index.qmd                       Preface / landing page
outline.qmd                     Master outline + per-section writing requirements
references.bib                  Shared bibliography (Pandoc [@key] citations)
chapters/                       Chapter sources (*.qmd)
bib/                            Per-chapter bibliography fragments
styles.css                      Custom HTML theme
.github/workflows/publish.yml   Build + deploy to GitHub Pages
```

The **outline and requirements** are committed before the chapters on purpose,
so the plan can be audited and corrected cheaply. Each chapter is written
against its requirement block in `outline.qmd`.

## Writing rules (summary)

- Every named method is cited to its **primary source**.
- Citation keys must resolve in `references.bib` (or a chapter's `bib/*.bib`).
- Each chapter ends with *Key Takeaways* and *Further Reading*.
- Target 2,000–3,500 words per chapter.

See `outline.qmd` for the full acceptance criteria.

## Build locally

Requires [Quarto](https://quarto.org) ≥ 1.4.

```bash
quarto preview     # live preview at http://localhost:xxxx
quarto render      # renders the static site into _book/
```

## Publish

Pushing to `main` triggers `.github/workflows/publish.yml`, which renders the
book and deploys it to GitHub Pages.

> **One-time setup:** if the first workflow run fails at *Configure GitHub Pages*,
> go to **Settings → Pages** and set **Source = GitHub Actions**, then re-run the
> workflow.

## Status

Work in progress. See the [outline](outline.qmd) for chapter-by-chapter status.

## License

To be decided by the repository owner.
