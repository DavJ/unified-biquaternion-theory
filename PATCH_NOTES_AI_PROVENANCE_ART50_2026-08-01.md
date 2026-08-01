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

# Patch notes — AI provenance / Article 50 transparency layer

**Date:** 2026-08-01  
**Scope:** provenance disclosure, editorial tiers, machine-readable metadata,
release verification, and curated PDF rebuilds.  
**Scientific content:** no new physical theorem or claim-level elevation.

## Purpose

The repository now records substantial generative-AI assistance without
misrepresenting AI systems as authors or delegating scientific responsibility.
The policy is intentionally conservative for material newly published from
2 August 2026, when Article 50 of Regulation (EU) 2024/1689 becomes applicable.
It is a transparency and audit mechanism, not a legal-compliance certificate.

## Delivered

- `AI_PROVENANCE.md` and author-controlled `PROVENANCE_TIERS.yaml`.
- Idempotent Markdown/LaTeX source markers for active A/B/C material.
- Historical D-tier sources remain unmarked.
- Visible notices plus PDF Subject/Keywords metadata in fourteen curated PDFs.
- Deterministic-figure provenance macro that does not mislabel computational
  plots as AI-generated.
- Idempotent Tier-C footer in generated wiki pages.
- Zenodo metadata disclosure and repository-agent rules.
- Regression tests, PDF verifier, checksum regeneration, and integrity checks.

## Author-only release gate

The tier map ships with a pending signature. Only Ing. David Jaroš may attest
that he has substantively reviewed all Tier-A material and accepts editorial
responsibility. Automated agents must not complete this step.

## Verification boundary

Focused provenance, checksum, hard-coded-constant, and GR regression gates are
run by the apply script. A complete scientific suite should also be run in the
project environment with all dependencies, including Hypothesis, installed.
