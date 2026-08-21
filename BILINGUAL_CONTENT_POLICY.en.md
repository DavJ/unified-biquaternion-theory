<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Bilingual content policy / Pravidla dvojjazyčného obsahu

## Normative rule

All active scientific, publication, explanatory, and student-facing prose must
exist in complete English (`en`) and Czech (`cs`) editions. Both editions are
normative. A document change is incomplete until both editions are present in
the same pull request and have passed structural and semantic-equivalence
review.

This is a content-identity rule, not a word-for-word translation rule. Natural
word order and idiom may differ, but the information available to a reader may
not differ.

## Required identity

Every paired edition must preserve exactly the same:

1. ordered section and content-unit structure;
2. equations, symbols, numerical values, units, assumptions, and domains;
3. definitions, lemmas, theorems, proofs, examples, and counterexamples;
4. figures, tables, captions' factual content, and data;
5. citations, links to authorities, labels, and cross-references;
6. claim status, proof level, uncertainty, caveats, warnings, and provenance;
7. conclusions and explicit open questions.

No edition may add or omit a scientific claim, qualification, explanation, or
example. Editorial metadata that is intrinsically language-specific may differ
only when it carries no scientific meaning.

## Source layout

Use ISO language suffixes for paired standalone sources:

```text
path/name.en.md    path/name.cs.md
path/name.en.tex   path/name.cs.tex
```

Each translatable content unit must have the same stable identifier in both
editions. For LaTeX, keep labels identical and place language-neutral equations
or generated tables in shared `*.tex` inputs whenever practical. For Markdown,
use matching explicit anchors or stable bilingual unit markers. Renaming an
identifier is a synchronized change.

Do not create a mixed-language source and call it bilingual. Each rendered
edition must be monolingual apart from proper names, citations, quoted primary
material, conventional symbols, and explicitly identified translation notes.

## Change protocol

Every pull request that changes governed prose must:

1. update both paired sources in the same commit series;
2. state which edition was the translation source;
3. confirm that formal structure and claim/status labels are identical;
4. include rendered or built outputs when the normal workflow produces them;
5. receive explicit human confirmation of semantic equivalence before merge.

Automated checks are mandatory where available and must fail closed on a
missing pair, mismatched identifiers, equations, citations, claim/status
markers, or document structure. Passing automation is necessary but is not
evidence that natural-language meaning is identical.

## Scope and migration

The rule applies to active prose in the repository, including textbooks,
papers, canonical explanations, research-track explanations, public-facing
documentation, reports, and substantive README material.

The following are outside the pairing requirement:

- source code and machine-readable data;
- generated files whose bilingual inputs are governed;
- immutable historical material under `ARCHIVE/`;
- verbatim quotations and deposited primary-source snapshots;
- bibliographic records with no explanatory prose.

Existing unpaired or mixed-language documents are migration debt. They may
remain unchanged temporarily, but they are not a template for new work. A
material edit must migrate the complete document into a pair. A temporary
exception requires a repository-owner-approved entry in a dedicated exception
register containing the exact paths, reason, owner, and expiry date. Exceptions
must never weaken claim-status or provenance requirements.

## Merge gate

A governed bilingual change must not merge unless all of the following are
true:

- both editions exist and build or render successfully;
- structural checks pass;
- the pull request contains the semantic-equivalence declaration;
- a human reviewer explicitly approves semantic equivalence;
- no unresolved bilingual-policy exception remains.

If semantic identity is uncertain, the safe state is to keep the pull request
in draft and not publish either changed edition.
