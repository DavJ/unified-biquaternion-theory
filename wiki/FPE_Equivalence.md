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


# FPE Equivalence — QM / GR / Statistical Mechanics Unification

The Fokker–Planck Equation (FPE) and Euler–Lagrange equation derived from the
UBT action S[Θ] are algebraically equivalent under conditions C1 and C2. This
provides a single origin for quantum mechanics, general relativity, and statistical
mechanics as projections of one field equation.

**Canonical source**: [`canonical/qm_emergence/step4_fpe_equivalence.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qm_emergence/step4_fpe_equivalence.tex)  
**Verification script**: [`tools/verify_fpe_equivalence.py`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/tools/verify_fpe_equivalence.py)

---

## Summary

**Strongest unification result in UBT**: QM, GR, and statistical mechanics are
definitionally equivalent projections of ∂_TΘ = D∇²Θ.

The equivalence holds under:
- **C1**: ∇²H = 0 (Hamiltonian is harmonic)
- **C2**: ∇H ⊥ ∇Θ (Hamiltonian gradient orthogonal to field gradient)

Numerical verification: ALL CHECKS PASSED — see `tools/verify_fpe_equivalence.py`.

---

## Derivation Status

<!-- BEGIN GENERATED: fpe_status -->
_No entries found in DERIVATION_INDEX.md for this section._
<!-- END GENERATED: fpe_status -->

---

## The Three Projections

```
∂_TΘ = D∇²Θ  (single biquaternionic field equation)
    ├── Re(∂_tΘ = □Θ)  →  GR / Klein-Gordon
    ├── Im(∂_ψΘ = □Θ)  →  QM / Schrödinger
    └── Full FPE        →  Statistical mechanics (by construction)
```

---

## Supporting Files

| File | Content |
|------|---------|
| [`step4_fpe_equivalence.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qm_emergence/step4_fpe_equivalence.tex) | Main FPE ↔ E-L proof |
| [`step1_fpe_check.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qm_emergence/step1_fpe_check.tex) | FPE structure check |
| [`step7_born_rule.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qm_emergence/step7_born_rule.tex) | Norm conservation / Born rule |

---

## See Also

- [QM Emergence](QM_Emergence) — full QM emergence derivation chain
- [GR Recovery](GR_Recovery) — GR as real-sector limit
- [Theta Field](Theta_Field) — field equation structure

<!-- BEGIN GENERATED: provenance_footer -->
---
> **AI provenance — Tier C (working):** AI assistance may have been used in
> drafting or maintenance. Exhaustive human review is not claimed. See the
> [repository provenance policy](https://github.com/UBT-Institute/unified-biquaternion-theory/blob/master/AI_PROVENANCE.md).
<!-- END GENERATED: provenance_footer -->
