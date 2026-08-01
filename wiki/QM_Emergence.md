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


# QM Emergence from Complex Time

Quantum mechanics emerges from UBT as a projection of the biquaternionic field
equation ∂_τΘ = □Θ onto the imaginary-time (ψ) sector, without additional postulates.
The Pauli and Dirac structures arise algebraically from ℂ⊗ℍ.

**Canonical source**: [`canonical/qm_emergence/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/canonical/qm_emergence)  
**Step files**: step1–step7 in canonical/qm_emergence/

---

## Key Derivation Chain

| Step | File | Content |
|------|------|---------|
| 1 | [`step1_fpe_check.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qm_emergence/step1_fpe_check.tex) | Biquaternionic FPE structure |
| 2 | [`step2_schrodinger_emergence.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qm_emergence/step2_schrodinger_emergence.tex) | Schrödinger structure from Im sector |
| 3 | [`step3_dirac_emergence.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qm_emergence/step3_dirac_emergence.tex) | Dirac equation from ℂ⊗ℍ⊗ℂ⊗ℍ |
| 4 | [`step4_fpe_equivalence.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qm_emergence/step4_fpe_equivalence.tex) | FPE ↔ Euler–Lagrange equivalence |
| 6 | [`step6_spinorial_subspace.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qm_emergence/step6_spinorial_subspace.tex) | Spinorial subspace identification |
| 7 | [`step7_born_rule.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qm_emergence/step7_born_rule.tex) | Born rule from FPE norm conservation |

---

## Derivation Status

<!-- BEGIN GENERATED: qm_emergence_status -->
_No entries found in DERIVATION_INDEX.md for this section._
<!-- END GENERATED: qm_emergence_status -->

### Open Gaps

| Gap | Description | Status |
|-----|-------------|--------|
| Gap G1 | Derive drift A(Q) = −∇H from S[Θ] | ❌ **Open** |
| Gap G2 | Prove consistency condition on H | ❌ **Open** |
| Gap G3 | Non-commutative FPE ordering | ✅ **Closed [L0] ⭐** — Sc annihilates Im(ℍ); FPE ↔ EL Proved [L0] for ALL sectors (U(1), SU(2), SU(3)); v70 |
| Gap S1 | Derive diffusion coefficient 𝒟_eff = ℏ/(2m) from S[Θ] | ❌ **Open** |
| Gap D1 | Spinorial subspace | ✅ **Closed** |

---

## Three QM Projections

The field equation ∂_TΘ = D∇²Θ has three definitionally equivalent projections:

| Projection | Sector | Resulting Theory |
|------------|--------|-----------------|
| Re(∂_tΘ = □Θ) | Real time t | GR / Klein-Gordon |
| Im(∂_ψΘ = □Θ) | Imaginary time ψ | QM / Schrödinger |
| Full FPE | Both sectors | Statistical mechanics |

These are not emergent from a deeper layer — they are definitionally equivalent
projections of one biquaternionic field equation.

---

## Born Rule

The Born rule |Θ|² = probability density follows from norm conservation under
the FPE without additional postulate:

```
∂_T ∫ |Θ|² dQ = 0   (proved in step7_born_rule.tex)
```

Status: **Proved [L0]**

---

## Open Gaps

| Gap | Description | Priority |
|-----|-------------|----------|
| G1 | Derive drift A(Q) = −∇H from S[Θ] via Euler-Lagrange | HIGH |
| G2 | Prove consistency condition on H for general biquaternionic case | HIGH |
| G3 | Non-commutative FPE ordering — **CLOSED [L0] ⭐** (v70, Sc-projection); FPE ↔ EL Proved [L0] ALL sectors (U(1), SU(2), SU(3)) | CLOSED |
| S1 | Derive diffusion coefficient 𝒟_eff = ℏ/(2m) from S[Θ] | HIGH |

---

## See Also

- [Theta Field](Theta_Field) — ∂_τΘ = □Θ field equation
- [FPE Equivalence](FPE_Equivalence) — QM/GR/stat-mech unification
- [GR Recovery](GR_Recovery) — real-sector projection
- [Mathematical Foundations](Mathematical_Foundations) — ℂ⊗ℍ algebra

<!-- BEGIN GENERATED: provenance_footer -->
---
> **AI provenance — Tier C (working):** AI assistance may have been used in
> drafting or maintenance. Exhaustive human review is not claimed. See the
> [repository provenance policy](https://github.com/UBT-Institute/unified-biquaternion-theory/blob/master/AI_PROVENANCE.md).
<!-- END GENERATED: provenance_footer -->
