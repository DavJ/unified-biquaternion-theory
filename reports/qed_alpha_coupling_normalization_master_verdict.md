<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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


# qed_alpha_coupling_normalization_master_verdict.md

**Task**: `fix_or_reject_U1_coupling_normalization`  
**Priority**: CRITICAL  
**Mode**: physics-first, no numerology  
**Date**: 2026-05-10  
**Scope**: Targets 1–6, full chain audit

---

## Status table

| Item | Status | Notes |
|---|---|---|
| U(1) generator normalization | **DERIVED** | Tr(T²) = 1/2 from biquaternion algebra |
| Charge unit q_Θ = 1 | **DERIVED** | Right-phase period in Mat(2,ℂ) |
| Integer charge quantization | **CONDITIONAL** | Requires flux convention Φ₀ = 2π |
| Quark fractional charges | **CONDITIONAL** | Requires SM hypercharge assignment |
| e₅ parent coupling | **NO-GO** | Field rescaling removes it; no fixer found |
| R_ψ compact scale | **NO-GO** | Scale modulus is a flat direction |
| e₄ four-dimensional coupling | **CONDITIONAL** | Blocked by e₅ and R_ψ being NO-GO |
| α value | **NO-GO** | Blocked by e₅ and R_ψ |
| RG running direction | **DERIVED** | α⁻¹ decreasing with μ, b_em > 0 |
| Prime consistency (137, 127) | **OBSERVED CONSISTENCY** | After-the-fact comparison only |

---

## Exact derivation chain

```
S[Θ]
  │
  ├─ Biquaternion algebra B = C ⊗ H ≅ Mat(2,C)
  │    ↓
  ├─ Automorphism group: [GL(2,C) × GL(2,C)] / Z₂
  │    ↓
  ├─ U(1)_EM = right-phase action: T_EM = (1/2)I₂
  │    Tr(T_EM²) = 1/2   [DERIVED]
  │    q_Θ = 1            [DERIVED]
  │
  ├─ Compactification on M₄ × S¹_ψ
  │    ↓
  │    e₄² = e₅² / (2π R_ψ)  [structure DERIVED; values BLOCKED]
  │              │        │
  │              │        └─ R_ψ = ?  [NO-GO: scale modulus free]
  │              └─ e₅ = ?    [NO-GO: field-rescaling removes it]
  │
  └─ α = e₄² / (4π)     [NO-GO: e₅ and R_ψ both free]
```

---

## Free parameters remaining

| Parameter | Reason for being free |
|---|---|
| e₅ (5D coupling) | Absorbed by 𝒜_M = e₅ A_M rescaling; no independent fixing |
| R_ψ (compact radius) | Scale modulus is flat in all examined free energies |
| θ_W (Weinberg angle) | Ratio g'/g not fixed by B = C ⊗ H |
| Y_r (hypercharge assignments) | SM input; not derived from biquaternion algebra |

---

## Failed assumptions

| Claim | Why it fails |
|---|---|
| T-duality fixes R_ψ | Requires string length ℓ_s as external input |
| Spectral free energy fixes R_ψ | Fixes only shape R_t/R_ψ = 1, not absolute scale |
| Holonomy / winding quantization fixes e₅ | Quantizes e₅·Φ product; Φ is a free Wilson line modulus |
| Chern class quantization fixes e₅ | Quantizes e₅·B·R²; not e₅ alone |
| Trace normalization fixes absolute coupling | Fixes relative gauge sector normalization only |
| Modular covariance fixes volume | Constrains spectrum, not overall volume |

---

## What is established (positive results)

1. **QED sector emergence**: DERIVED. Starting from S[Θ], UBT generates the
   U(1) gauge sector with canonical kinetic form `-1/(4e²) F²`.

2. **Generator normalization**: DERIVED. The U(1)_EM generator is
   `T_EM = (1/2)I₂` with `Tr(T_EM²) = 1/2`, matching the standard
   hypercharge normalization.

3. **Unit charge**: DERIVED. The fundamental field Θ carries unit charge
   `q_Θ = 1` under the right-phase action.

4. **RG running direction**: DERIVED. The beta function is positive
   (`b_em > 0`), giving `dα⁻¹/d ln μ < 0` — coupling grows with energy.

5. **Shape modulus**: CONDITIONAL. The spectral free energy gives a
   stationary shape point `R_t = R_ψ` under isotropic normalization.

---

## Next possible routes if α remains free

**Route A — Gravitational-electromagnetic unification:**  
Derive a condition relating `e₅²` to the 5D Newton constant `G₅` and a
fundamental length scale. Schematically:
```
e₅² ~ G₅ / ℓ_Planck  →  fixes e₅ if G₅ and ℓ_Planck are fixed by UBT
```

**Route B — Dynamical moduli stabilization:**  
Add a potential term `V(R_ψ)` to S[Θ] that breaks the moduli symmetry
`R_ψ → λ R_ψ` and selects a specific vacuum value. This requires new
physics beyond the current canonical action.

**Route C — Topological quantization of the full action:**  
Identify a topological invariant (e.g., instanton number on the compact
manifold) that fixes the product `e₅²/(2π R_ψ)` without free parameters.
This would require a compact internal manifold with quantized flux and
a non-trivial instanton structure.

**Route D — GUT embedding:**  
Derive the full GUT group from the biquaternion involution structure
(SU(3)_c is already established). If SU(5) or SO(10) emerges, the
GUT-normalized coupling at the unification scale could fix e₄ at low
energies via RG running — but this requires the GUT scale to be derived.

---

## Hard-rule compliance

- Alpha, 137, 127, B=46, and measured e² not used as derivation input. ✓
- Prime stability not used as derivation mechanism. ✓
- No new alpha routes introduced. ✓
- No constant fitting performed. ✓
- Work confined to research_tracks/qed_alpha_derivation/ and reports/. ✓
- canonical/ unchanged. ✓
- All claims labeled with verdict class. ✓

---

## Mandatory final sentence

> **"Alpha remains a free normalization in the current UBT formulation."**
