---
name: notebooklm-wiki-export
description: Convert a documentation repository into a small set of NotebookLM-ready Markdown documents. Use for explicit requests to plan, generate, validate, regenerate, or publish NotebookLM exports. Do not use for normal wiki maintenance.
---

# NotebookLM Wiki Export

## Goal

Create a small set of topic-coherent Markdown reference sources for NotebookLM.

Canonical wiki files remain the source of truth. Generated documents remain export-only derivatives.

Preserve factual meaning, conditions, exceptions, formulas, tables, terminology, and source provenance.

Optimize for NotebookLM retrieval and grounded answers. Human reading flow is secondary.

Do not fix document names, document count, topic grouping, or publishing destination in this skill.

## Authority boundaries

- Read the repository instructions before planning.
- Treat canonical wiki files as input.
- Never use prior exports as canonical input.
- Do not edit canonical content during export.
- Do not edit repository rules without separate authorization.
- Do not publish outside the workspace without authorization.
- Preserve unrelated working-tree changes.

## Scope

Derive these values from the current request and repository:

- Canonical content scope.
- Excluded paths.
- Desired document count.
- Topic boundaries.
- Staging destination.
- Publishing destination.
- Current NotebookLM limits.

If topic grouping changes materially, present the proposed document map and table of contents before generation.

## NotebookLM reference perspective

Treat each output as a model reference source, not a standalone human guide.

Prioritize these qualities in order:

- Canonical correctness and internal consistency.
- Retrieval precision for likely questions.
- Self-contained factual sections.
- Semantic coverage.
- Low duplication and low metadata noise.
- Maintainable provenance.
- Human scanability.

Use descriptive headings that state the subject and scope.

Use descriptive filenames and H1 titles that users can mention in NotebookLM queries.

Keep conditions, units, exceptions, and time sensitivity next to each claim.

Include enough local context for a retrieved section to stand alone.

Do not replace necessary facts with directions to another file.

Repeat minimal context when it prevents a section from depending on another source.

Keep one authoritative home for each fact. Duplicate only the context required to answer a likely query inside another source.

Do not add a table of contents solely for human navigation.

## Inventory

Use deterministic code to collect:

- Canonical Markdown files.
- Headings and document sizes.
- Internal links.
- Source URLs.
- Tables, formulas, thresholds, and exceptions.
- Duplicate topics.
- Conflicting claims.
- Date-sensitive claims.

Map every selected source to one or more proposed outputs.

Do not require each source to appear in only one output.

Create a preflight ledger containing the source map, material conflicts, stale claims, and required user decisions.

Do not begin generation until every material canonical conflict is resolved in the ledger.

## Conflict handling

List each conflict with its source locations.

Separate factual conflicts from differences in scope or context.

Do not blend conflicting claims.

Record the user's resolution in the preflight ledger.

If the resolution changes reusable knowledge, update canonical documentation through its normal workflow before generation.

Canonical edits require separate authorization from export generation.

Record the selected claim and rejected alternatives in the preflight ledger.

For unstable disputed claims, verify against current primary sources.

## Generation

Group content by likely query domain and retrieval context.

Place overview material before detailed procedures.

Create a lossless coverage draft before synthesis.

Use the coverage draft to track retained facts, tables, formulas, thresholds, and exceptions.

Combine duplicate explanations into one authoritative section.

Rewrite mechanical page boundaries into coherent chapters.

Preserve an original boundary when it already represents one answerable subject.

Do not accept the lossless coverage draft as the final export when it still reads like concatenated pages.

Build sections around answerable subjects rather than original file boundaries.

Apply one provenance policy across all outputs.

Keep external evidence near unstable claims and resolved conflicts.

Keep internal source paths in a compact appendix or validation manifest.

Do not prefix every section with internal source-path metadata.

Exclude validation-only manifests from the published NotebookLM source set.

Convert wiki links into explicit context, readable text, or valid output references.

Do not make a necessary answer depend on an output reference.

Add navigation only when it improves semantic orientation without repeating content.

Follow repository language, terminology, and Markdown rules.

## Regeneration comparison

When prior exports exist, generate the candidate from canonical sources before reading prior export content.

Use prior exports only as comparison baselines. Never recover canonical facts from them.

Compare the candidate and baseline across:

- Retrieval precision.
- Grounding clarity.
- Section self-containment.
- Factual density.
- Provenance consistency.
- Canonical reproducibility.
- Semantic preservation.
- Duplicate content.
- Conflicts and stale claims.
- Metadata noise.

Treat size, heading, URL, and duplication counts as diagnostic signals. Do not rank versions from counts alone.

Classify material differences as:

- Canonical content changes.
- Prior export-only decisions.
- Synthesis changes.
- Formatting changes.

List strengths and regressions for both versions.

If a prior export contains a material decision absent from canonical sources, report canonical drift and stop before publishing.

Do not copy the export-only decision into the candidate.

Updating canonical content requires separate authorization and the repository's normal documentation workflow.

## Validation

Use deterministic code for transforms and measurable validation.

Use model judgment only for classification, synthesis, and conflict detection.

### Structural validation

- Every selected source maps to at least one output.
- Every generated document belongs to the approved map.
- Every cross-document reference resolves.
- Export files never become canonical inputs.

### Semantic validation

- Tables remain complete.
- Formulas remain complete.
- Thresholds retain their units and conditions.
- Exceptions remain attached to their rules.
- Resolved conflicts use the approved conclusion.
- Generated text introduces no unsupported claims.
- Material decisions do not exist only in an export.

### Retrieval validation

Create representative questions for every major topic and decision path.

Map each expected answer to one explicit candidate passage.

Reject passages that require hidden context from another file.

If a likely query spans sources, repeat the smallest canonical context needed in the most relevant source.

Reject competing passages that can produce different answers to the same question.

Keep canonical game terms in passages that users can include in queries.

Verify formulas and thresholds by normalized content identity. Do not rely on raw line counts alone.

If authorized NotebookLM access exists, test representative questions in NotebookLM.

Without product access, run static passage mapping and report that live retrieval remains unverified.

### Duplication validation

Detect repeated concepts across outputs.

Allow intentional summaries and cross-references.

Reject competing authoritative explanations.

### Source validation

- Every factual section remains traceable.
- Source URLs are deduplicated.
- Source syntax is valid.
- Current external facts use primary sources.

### Format validation

- Markdown parses cleanly.
- Headings form a usable hierarchy.
- Repository formatting rules pass.
- Manual prose wrapping is absent.
- Unsupported wiki syntax is absent.

Run repository checks required by local instructions.

Apply pass or fail to selected canonical sources and generated artifacts.

Report unrelated pre-existing findings without blocking the export.

### Limit validation

Obtain current limits from official Google sources before assigning pass or fail.

Measure every output with one method.

Report unverified limits instead of assuming them.

## Preview and publishing

Generate inside the repository before external publishing.

Present the artifact list, sizes, topic map, and validation results.

Publish only the artifacts authorized by the user.

Resolve the destination before writing.

Do not delete or overwrite unrelated files.

After publishing, compare source and destination checksums with the same command.

## Acceptance criteria

The export passes only when:

- The user approved the scope and topic map.
- Each file forms a topic-coherent reference source.
- Representative questions map to explicit passages.
- No unresolved canonical drift remains.
- Structural coverage passes.
- Semantic coverage passes.
- Provenance remains usable.
- Cross-document references resolve.
- Current NotebookLM limits pass.
- Selected canonical sources and generated artifacts pass applicable validation.
- Published checksums match when publishing occurred.

## Report

Report:

- Generated artifacts.
- Topic map.
- Preflight ledger result.
- Source coverage.
- Semantic coverage.
- Retrieval coverage and validation mode.
- Conflict resolutions.
- File sizes.
- Validation results.
- Publishing destination.
- Checksum results.
- Unverified claims.

## Stop conditions

Stop before generation when the topic map lacks authorization.

Stop before generation when a material conflict remains unresolved.

Stop before publishing when the destination or overwrite scope is unclear.

Stop after two failed attempts at the same logic error.

Do not report success while any required validation fails.
