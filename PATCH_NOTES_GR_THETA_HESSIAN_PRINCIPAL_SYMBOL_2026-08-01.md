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

# GR Theta-Hessian principal-symbol decision

## Purpose

This patch performs the cheapest safe decision test for the induced-gravity
route without modifying the signed Tier-A claims ledger.

## Results

1. The fixed-background quadratic Theta kinetic operator has scalar principal
   symbol after the internal pairing index is raised:
   `sigma_2(H)^A_B = g^{mu nu} k_mu k_nu delta^A_B`.
2. The same kinetic scalar collapses to a volume term when the metric is locked
   to the same covariant jet. Therefore its full composite Hessian is not the
   fixed-background Hessian.
3. The six-dimensional `q=1` D-composite sector is a finite-scale singularity
   of `I-A(s,lambda)`. It is not conic under `s -> c s`, so it is not a
   principal-symbol bundle and cannot be inserted directly as six heat-kernel
   fields.
4. The remaining first-principles calculation is the complete gauge-fixed
   composite Theta-only Hessian and its physical/ghost quotient.

## Claim boundary

The patch does not derive the Einstein coefficient, Newton's constant, a
physical mode count, or unconditional GR. The new diagnostic subgap labels are
B-tier machine-verified statements and require substantive human review before
promotion into the signed Tier-A ledger.

## Verification

- `tools/verify_theta_hessian_principal_symbol.py`
- `tests/test_theta_hessian_principal_symbol.py`
- existing D-composite and GR-endgame regression tests
- curated PDF provenance verification
- repository SHA-256 integrity verification
