# Per-chapter bibliography fragments

Chapter writers **must not** edit `references.bib` directly (parallel writers
would conflict). Instead:

1. Check `references.bib` first — if the citation already exists, reuse its key.
2. If not, create/extend `bib/<chapter-name>.bib` and add the entry there with
   complete metadata: authors, title, venue, year. Add a DOI or stable URL for
   post-2000 work when it can be verified. **Never invent an entry or a DOI.**
3. Reference the fragment from the chapter's YAML so citations resolve:

   ```yaml
   ---
   title: "..."
   bibliography: [../references.bib, ../bib/<chapter-name>.bib]
   ---
   ```

`tools/merge_bib.sh` consolidates all fragments into `references.bib` and
strips the per-chapter `bibliography:` overrides once writing is done.
