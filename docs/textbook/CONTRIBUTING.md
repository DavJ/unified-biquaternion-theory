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

# Contributing to the UBT Textbook
**Goal:** engineer-friendly overview. Keep core vs. proofs vs. speculative strictly separated.
- Reuse main paper content via `\input{../../...}` to avoid divergence.
- Style: short intros per chapter + `\input{}` of canonical sources.
- PRs: add small, focused improvements; include a quick build check (`latexmk -pdf`).
