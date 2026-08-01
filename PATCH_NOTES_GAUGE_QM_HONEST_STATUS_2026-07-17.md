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

# Patch Notes — Gauge and QM Honest-Status Correction

**Date:** 2026-07-17  
**Overlay type:** differential root overlay  
**Mathematical scope:** gauge carrier status and Born-rule/unitarity status only

## Changed files

- `canonical/gauge/GAUGE_MASTER_STATUS.md`
- `canonical/su3_derivation/su3_from_involutions.tex`
- `canonical/qm_emergence/step7_born_rule.tex`
- `docs/notes/symmetry_from_automorphisms.tex`
- `CLAIMS.yaml`
- `tests/test_claims_consistency.py`
- `CHANGELOG.md`

## Added file

- `reviews/gauge_qm_honest_status_audit_2026-07-17.md`
- `reports/gauge_qm_honest_status_validation_2026-07-17.md`

## New authoritative statuses

- `GAP-SU3-DYN: OPEN`: the involutions select a complex rank-three carrier;
  the unitary/Yang--Mills dynamics on it must still be derived from canonical
  UBT.
- Born rule / unitarity: `OPEN_GAP`; the former diffusion-based proof is
  retracted.

## Non-goals

This patch does not change the frozen covariant-tetrad GR architecture, the GR
subclosure mathematics, or the historical development record.
