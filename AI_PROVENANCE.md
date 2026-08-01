<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: A_attested
ai_assistance: disclosed
human_review: substantive
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: The author has read the substance and accepts editorial responsibility.
UBT-AI-PROVENANCE-END
-->

# AI provenance and editorial responsibility

**Policy version:** 1.0  
**Effective for newly published material:** 2 August 2026  
**Editorially responsible person:** Ing. David Jaroš  
**Tier authority:** [`PROVENANCE_TIERS.yaml`](PROVENANCE_TIERS.yaml)

Unified Biquaternion Theory (UBT) is an author-led research programme developed
with substantial assistance from generative-AI systems. AI assistance has been
used for activities including drafting, editing, code generation, symbolic and
numerical checks, adversarial review, repository maintenance, and preparation
of reproducible research artefacts. The scientific claims remain those of the
author, subject to the claim levels and open gaps recorded in the repository.

This disclosure is intended to make the role of AI legible to readers and
reviewers. It is **not** a statement that an AI system is an author, inventor,
scientific authority, or bearer of legal responsibility. It is also not a legal
certification of compliance with Regulation (EU) 2024/1689.

## Provenance tiers

| Tier | Meaning | Human-review claim |
|---|---|---|
| **A — attested** | The author has read the substance and accepts editorial responsibility. | Substantive human review and editorial control are asserted as of the attestation date in `PROVENANCE_TIERS.yaml`. |
| **B — machine verified** | The material is bound to named source files, tests, or verifier scripts. | Individual line-by-line human review is not asserted. |
| **C — working** | Drafts, research tracks, reports, experiments, and other evolving material. | Exhaustive human review is not claimed. |
| **D — historical** | Material predating systematic AI-assisted development, retained for history. | It is deliberately left unmarked so that old work is not misrepresented as AI-assisted. |

Tier assignment is an editorial decision. Automated tools may report an
unassigned path, but may not elevate a document to Tier A or sign the
attestation on the author's behalf.

## Machine-readable source marking

Current Markdown and LaTeX sources outside excluded and historical paths carry
a structured comment block with this schema:

```text
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: A_attested | B_machine_verified | C_working
ai_assistance: disclosed
human_review: substantive | machine-verified | risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: <tier-specific notice>
UBT-AI-PROVENANCE-END
```

The source marker is generated and checked by
[`tools/apply_provenance_headers.py`](tools/apply_provenance_headers.py). The
map in `PROVENANCE_TIERS.yaml` is the source of truth.

## Publications and PDF metadata

Curated LaTeX publications use [`tex/ubtprovenance.sty`](tex/ubtprovenance.sty)
to add:

1. a visible provenance notice below the title;
2. the provenance tier in PDF Subject/Keywords metadata; and
3. a deterministic-figure provenance macro that explicitly says a plot is not
   AI-generated when it was produced by a named script from named data.

Historical PDFs created before 2 August 2026 are not automatically rewritten.
Newly built curated PDFs should be generated from marked source and should
carry the package notice and metadata.

## Human review and responsibility

For a Tier-A publication, attestation means deliberate review of the substance,
not merely spelling, grammar, or formatting. The author may approve, alter, or
reject AI-proposed text, equations, code, classifications, or conclusions and
holds final editorial responsibility for publication.

Tier B and Tier C must never be cited as though the Tier-A attestation extends
to them. Passing tests establish only the properties encoded by those tests.
They do not establish physical truth, novelty, or completeness.

## Figures

No blanket AI-generated label is applied to repository figures. Deterministic
plots produced by named scripts from named data should use
`\UBTFigureProvenance{script}{data}` in LaTeX. This states that the figure is a
reproducible computational output and **not AI-generated**. Any genuinely
AI-generated or AI-manipulated image must instead be labelled explicitly in its
caption and release metadata.

## AI systems and tools

The project has used multiple AI assistants over time, including OpenAI,
Anthropic, Google, GitHub Copilot, DeepSeek, and locally run models. A tier is
not a quality ranking of a model. It records the repository's review and
verification status for a file. Where model-level traceability is material, it
should be recorded in the relevant commit, patch note, review, or experiment
manifest.

## EU AI Act transparency context

Article 50 of Regulation (EU) 2024/1689 applies from 2 August 2026. The European
Commission's 2026 guidance distinguishes obligations of providers from those
of deployers and recognises substantive human review, editorial control, and
editorial responsibility for certain public-interest text publications. UBT
uses this repository policy as a conservative transparency and audit measure;
it does not rely on a repository banner alone as proof of legal compliance.

Official references:

- Regulation (EU) 2024/1689, Article 50: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- European Commission guidelines: https://digital-strategy.ec.europa.eu/en/policies/guidelines-transparency-ai-generated-content
- European Commission Q&A: https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act
- Code of Practice on Transparency of AI-generated Content: https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content

## Release procedure

Before a public release or submission:

1. update source files;
2. run `python tools/apply_provenance_headers.py --apply` and then `--check`;
3. run `python tools/generate_wiki.py`;
4. rebuild curated PDFs with `tex/` available through `TEXINPUTS`;
5. run the provenance and scientific test suites;
6. refresh the Tier-A signature and attestation date personally;
7. regenerate and verify `SHA256SUMS.txt`.

The pending signature in `PROVENANCE_TIERS.yaml` is intentional until the author
performs that final review.
