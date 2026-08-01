<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# July 2026 Gauge and Quantum Honest-Status Audit

**Date:** 2026-07-17  
**Scope:** `canonical/gauge/`, `canonical/su3_derivation/`, and
`canonical/qm_emergence/`  
**Canonical status source:** `CLAIMS_MATRIX.md`

## Executive finding

Two older closure claims were stronger than their mathematics supported.
Neither finding changes the covariant-tetrad GR programme.

1. The involutions select a complex rank-three carrier
   \(V_c\cong\mathbb C^3\), but they do not make \(SU(3)\) a subgroup of the
   complex-algebra automorphism group of \(\mathbb C\otimes\mathbb H\).
2. A diffusion/Fokker--Planck-type equation for an amplitude \(\Theta\) does not
   automatically conserve \(\int\Theta^\dagger\Theta\), so the old Born-rule
   closure is withdrawn.

## Gauge finding

For
\[
U_\theta=\operatorname{diag}(e^{i\theta},e^{-i\theta},1)\in SU(3)
\]
acting on the carrier basis \((I,J,K)\), the mixed relation survives,
\[
(e^{i\theta}I)(e^{-i\theta}J)=K,
\]
but the square relation does not:
\[
(e^{i\theta}I)^2=-e^{2i\theta}\neq-1=I^2
\]
for generic \(\theta\).  Therefore the transformation is not an algebra
automorphism.  The complex-algebra automorphisms of
\(\mathbb C\otimes\mathbb H\cong\operatorname{Mat}(2,\mathbb C)\) are inner,
with group \(\operatorname{PGL}(2,\mathbb C)\).

The honest current statement is:

- Lorentz/spin structure from the biquaternionic algebra: retained.
- Rank-three color carrier from involutions: retained.
- Unitary \(SU(3)\) and Yang--Mills dynamics on that carrier: introduced;
  canonical action origin open as `GAP-SU3-DYN`.

## Quantum finding

For amplitude diffusion
\[
\partial_T\Theta=D\partial_x^2\Theta,
\qquad
\Theta=e^{ikx-Dk^2T},
\]
one has
\[
\int_0^L|\Theta|^2dx=L e^{-2Dk^2T}.
\]
Thus amplitude diffusion is contractive rather than unitary.  Conservation of a
probability density satisfying its own Fokker--Planck equation cannot be
transferred automatically to \(P=\Theta^\dagger\Theta\).

The Born rule and unitary physical evolution remain open and must be derived
from the finalized canonical UBT dynamics.

## Corrections applied

- Legacy gauge status file deprecated.
- SU(3) carrier document made explicitly conditional.
- Minimal Yang--Mills Lagrangian labeled postulated.
- Born-rule document formally retracted while preserving the valid decay
  calculation and audit trail.
- Claim-ledger forbidden wording and recursive regression scans added.
