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

# Master(5) connection wording fix — 2026-07-16

Small consistency-only overlay against `unified-biquaternion-theory-master(5).zip`.

Changes:
- names the compatibility equation explicitly as the **tetrad postulate**;
- states that Christoffel symbols and spin/biquaternionic connection are **related but not identical**;
- states explicitly that a componentwise identification such as `Gamma = Re Omega` is **generally incorrect**;
- keeps the canonical and mirrored THEORY files synchronized.

Verification:
- targeted tetrad/Omega/integrability/status tests pass;
- historical fiber test remains skipped by design.
