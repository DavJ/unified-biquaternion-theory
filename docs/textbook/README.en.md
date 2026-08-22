<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# UBT textbook

This directory publishes one textbook in two synchronized editions. The only
book entry points are `main.en.tex` and `main.cs.tex`; both load the shared,
language-neutral layout in `main.tex` and their corresponding `.en.tex` or
`.cs.tex` content files.

## Language and parity contract

Every active prose source must have an English/Czech pair. Both files must
carry identical mathematics, equations, labels, references, citations,
numbers, claim statuses, and section structure. Translation-only differences
are allowed; scientific additions or deletions must be applied to both files
in the same change. CI checks mechanical parity, while a human reviewer remains
responsible for semantic equivalence.

## Official build

From the repository root, run:

```bash
make -C docs/textbook verify
```

The command produces exactly two official files:

```text
build/textbook/public/UBT_Textbook_EN.pdf
build/textbook/public/UBT_Textbook_CS.pdf
```

`make -C docs/textbook publish` copies the same pair to `docs/pdfs/`.
Supplementary student papers remain separate documents and are not alternative
textbook editions.

## Scientific and provenance rules

- `docs/textbook/SOURCE_MAP.md` identifies the live sources governing the book.
- `ARCHIVE/**` remains historical and is never included in the live textbook.
- Classical results, controlled UBT bridges, and new or open UBT claims must
  remain visibly distinct.
- Paper derivations follow `docs/DERIVATION_VERIFICATION_POLICY.md`.
- AI-assisted content follows `ubt-ai-provenance/v1`; this directory remains
  Tier `C_working` until the responsible human editor changes its status.
