# Torn Wiki — Agent Schema (AGENTS.md)

This file is the Schema layer of this llm-wiki. It defines structure, conventions, and workflows for all AI agents operating in this repository.

## Architecture

This wiki uses a three-layer structure:

- sources/: Raw, immutable source material (forum posts, guides, Discord excerpts). Never edited after ingestion.
- wiki pages: LLM-maintained .md files organized by topic directory. These are the living knowledge base.
- AGENTS.md: This file. Governs all agent behavior and wiki conventions.

## Workflows

### Ingest
Triggered when new source material arrives.

1. Save raw source to `sources/` with a descriptive filename (e.g. `sources/2026-06-27-forum-battlestats-ratios.md`).
2. Read and discuss key takeaways.
3. Write or update relevant wiki pages. One source typically touches multiple pages.
4. Add or update `[[wikilink]]` cross-references affected by the change.
5. Append an entry to `log.md`: `## [YYYY-MM-DD] ingest | Source Title`
6. Update `index.md` if new pages were created.

### Query
Triggered when the user asks a question about game content.

1. Search `index.md` to identify relevant pages.
2. Read those pages and synthesize an answer with inline citations (`[[page]]`).
3. If the answer reveals a gap, propose creating a new wiki page.

### Lint
Triggered on demand to health-check the wiki.

1. Scan for contradictions between pages.
2. Find stale claims (content marked with a date that may be outdated).
3. Find orphaned pages (not referenced by any `[[wikilink]]`).
4. Find missing cross-references (page A mentions concept B but does not link `[[B]]`).
5. Report gaps and propose follow-up Ingest or edit tasks.

## File Conventions

### index.md
- Lists all wiki pages with one-line summaries, organized by directory.
- Format per entry: `- [[filename]] — one-line summary`
- Updated during Ingest when new pages are created.

### log.md
- Append-only chronological record of all Ingest operations.
- Entry format: `## [YYYY-MM-DD] ingest | Source Title`
- Body: 2-5 bullet points summarizing what changed.

### sources/
- Filenames: `YYYY-MM-DD-slug.md`
- Content: verbatim or lightly cleaned original text, with a header block:
  ```
  source: <original URL or origin description>
  date: YYYY-MM-DD
  ```
- Never edited after the initial save.

### Wikilinks
- Use `[[filename]]` (without directory prefix) to cross-reference pages.
- If the target filename is ambiguous, use `[[directory/filename]]`.
- Wikilinks appear inline in prose, not as standalone lists.

## Standards

### Terminology and Number Formatting
- See [terminology.md](terminology.md) for canonical game terms and number unit definitions (k/m/b).
- Keep specific game terms in English (e.g., Energy, Nerve, Battlestats, Merits, Cans, SE).
- Do not use Chinese units (億, 萬, 千).

### Markdown Formatting
- Do not use bold (**) or italics (* or _).
- Use headers, lists, tables, and code blocks for structure.

### Language and Style
- Descriptive text: Traditional Chinese (繁體中文).
- Game terms and technical identifiers: English.
- Keep it minimal and direct. Prefer bullet points over long paragraphs.

### Other
- Date format: `YYYY-MM-DD`.
- Edits are surgical. Do not refactor unrelated content.
- Retain original source URLs at the bottom of wiki pages under a `## Sources` section.

## Revision History
- 2026-06-27: Migrated to llm-wiki schema. Added three-layer architecture, Ingest/Query/Lint workflows, index/log/sources conventions, wikilink standard.
- 2026-04-18: Initialized project instructions, integrated terminology and numeric format standards.
