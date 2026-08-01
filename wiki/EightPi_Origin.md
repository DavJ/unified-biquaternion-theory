<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->
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


# 8π Common Origin

The factor 8π appears in both Einstein's field equations (G_μν = 8πG T_μν)
and the UBT one-loop baseline (B₀ = 8π). Both share a common algebraic ancestor:
dim_ℝ(ℍ) = dim_ℂ(Mat(2,ℂ)) = 4.

**Canonical source**: [`canonical/8pi_common_origin.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/8pi_common_origin.tex)  
**Verification script**: [`tools/verify_8pi_connection.py`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/tools/verify_8pi_connection.py)

---

## Summary

| Appearance of 8π | Origin | Status |
|-----------------|--------|--------|
| G_μν = **8π**G T_μν | 16πG = dim_ℝ(ℍ) × vol(S²) × G = 4 × 4π × G | **Structural** [L0] |
| B₀ = **8π** (one-loop baseline) | B₀ = 2π × dim_ℂ(ℂ⊗ℍ) = 2π × 4 | **Proved** [L1] |

Both factors trace back to the **dimension 4** of the biquaternion algebra —
either as dim_ℝ(ℍ) = 4 (GR) or dim_ℂ(Mat(2,ℂ)) = 4 (QFT coupling).

Numerical verification: ALL PASS — see `tools/verify_8pi_connection.py`.

---

## Derivation Status

<!-- BEGIN GENERATED: eightpi_status -->
_No entries found in DERIVATION_INDEX.md for this section._
<!-- END GENERATED: eightpi_status -->

---

## Unified Theorem Status

The algebraic source of both 8π's is **identified**: both trace to
dim_ℝ(ℍ) = 4 (quaternionic dimension). The conjecture is now formalised
as a **Motivated Conjecture** in `canonical/8pi_common_origin.tex §5`:

- **What is proved**: Both 8π's share the common algebraic ancestor dim_ℝ(ℍ) = 4:
  - G_μν: 8π = (1/2) × dim_ℝ(ℍ) × vol(S²) / (2π)
  - B₀: 8π = 2π × dim_ℂ(ℂ⊗ℍ) = 2π × dim_ℝ(ℍ)
- **What is conjectured**: A single variational argument δS[Θ] produces both,
  with the Einstein–Hilbert coefficient 1/(16πG) arising from the φ-projection
  of S[Θ] onto its real commutative sector.
- **What is blocked**: Rigorous unification requires deriving Newton's constant G
  directly from the normalisation of S[Θ] — a deep [L2] open problem.

## Open Problem

A unified theorem deriving both 8π's from a single source S[Θ] remains open.
This would require deriving the gravitational coupling constant 1/(16πG) directly
from the UBT action functional.

---

## See Also

- [GR Recovery](GR_Recovery) — Einstein equations from UBT
- [Fine Structure Constant α](Alpha_Constant) — B₀ = 8π one-loop baseline
- [Fundamental Objects](Fundamental_Objects) — dim(ℂ⊗ℍ) = 4 algebra

<!-- BEGIN GENERATED: provenance_footer -->
---
> **AI provenance — Tier C (working):** AI assistance may have been used in
> drafting or maintenance. Exhaustive human review is not claimed. See the
> [repository provenance policy](https://github.com/UBT-Institute/unified-biquaternion-theory/blob/master/AI_PROVENANCE.md).
<!-- END GENERATED: provenance_footer -->
