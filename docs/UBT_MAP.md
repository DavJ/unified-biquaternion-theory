<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Unified Biquaternion Theory — One-Page Map

> **Purpose**: Allow a physicist to understand the entire theory in under 2 minutes and jump directly to any proof.

---

## 1. Core Object

The fundamental dynamical object of UBT is the **biquaternionic field**:

```
Θ(q, τ) ∈ ℂ ⊗ ℍ  (or equivalently, Mat(4, ℂ))
```

defined over **complex time**:

```
τ = t + iψ ∈ ℂ
```

where `t` is real (observable) time and `ψ` is the imaginary phase dimension (compact circle, `ψ ~ ψ + 2π`).

The field equation (UBT "T-shirt formula"):

```
∇†∇ Θ(q, τ) = κ 𝒯(q, τ)
```

**Reference axioms**: [`core/AXIOMS.md`](../core/AXIOMS.md) · [`BIQUATERNION_GEOMETRY_LOCK_IN.md`](../BIQUATERNION_GEOMETRY_LOCK_IN.md)

---

## 2. Emergent Geometry

Spacetime geometry is **not postulated** — it emerges from Θ:

```
g_{μν}(x) = Re[ (D_μ Θ)† D_ν Θ ]
```

The underlying biquaternionic metric `𝒢_{μν} = (D_μ Θ)† D_ν Θ ∈ ℂ ⊗ ℍ` is the true fundamental object;
the classical GR metric `g_{μν}` is its real projection.  
There is **no background metric**; all curvature is emergent.

**References**:  
- [`core/AXIOMS.md`](../core/AXIOMS.md) (Axiom C)  
- [`BIQUATERNION_GEOMETRY_LOCK_IN.md`](../BIQUATERNION_GEOMETRY_LOCK_IN.md)  
- [`consolidation_project/appendix_R_GR_equivalence.tex`](../consolidation_project/appendix_R_GR_equivalence.tex)

---

## 3. Recovery of General Relativity

Taking the **real (Hermitian) limit** `ψ → 0` of the UBT field equations yields the
Einstein–Hilbert action and Einstein's field equations exactly:

```
R_{μν} − ½ g_{μν} R = κ T^(Θ)_{μν}
```

The spectral invariants of `Θ` reproduce the Ricci scalar `R` and cosmological constant `Λ`.
UBT **generalises** GR; GR is a classical-limit projection, not a separate assumption.

**References**:  
- [`FORMAL_INVARIANT_EXTRACTION_LAYER0.tex`](../FORMAL_INVARIANT_EXTRACTION_LAYER0.tex)  
- [`Appendix_F_Hermitian_Limit.tex`](../Appendix_F_Hermitian_Limit.tex)  
- [`consolidation_project/appendix_R_GR_equivalence.tex`](../consolidation_project/appendix_R_GR_equivalence.tex)

---

## 4. Emergence of the Standard Model Gauge Sector

The **gauge symmetry group SU(3) × SU(2) × U(1)** is not assumed — it emerges from the
automorphism group of the biquaternionic algebra `ℂ ⊗ ℍ` (extended to octonionic for colour):

| Gauge Factor | Algebraic Origin | Generator Space |
|---|---|---|
| SU(3) colour | Aut(𝕆) = G₂ ⊃ SU(3) | Octonionic extension ℂ ⊗ 𝕆 |
| SU(2) weak  | Aut(ℍ) = SO(3) ≅ SU(2)/ℤ₂ | Quaternionic sector (left action) |
| U(1) EM     | Aut(ℂ) = U(1) | Complex phase of τ |

QED is recovered as the `∂_ψ = 0` (constant phase) limit of the U(1) sector.

**References**:  
- [`Appendix_G_Emergent_SU3.tex`](../Appendix_G_Emergent_SU3.tex)  
- [`QED_SM_FROM_UBT_ANALYSIS.md`](../QED_SM_FROM_UBT_ANALYSIS.md)  
- [`SM_GEOMETRIC_EMERGENCE_DRAFT.md`](../SM_GEOMETRIC_EMERGENCE_DRAFT.md)

---

## 5. Key Physical Predictions

### 5a. Fine Structure Constant α

| Quantity | Value | Status |
|---|---|---|
| Bare (UBT geometric) | α⁻¹ = 137 | Derived from compact ψ-cycle + prime stability |
| Quantum correction | +0.036 | Two-loop vacuum polarisation |
| Predicted | α⁻¹ = 137.036 | |
| Experimental (CODATA 2022) | α⁻¹ = 137.035999177(21) | |
| Agreement | 260 ppm | |

→ **Full derivation**: [`docs/PROOFKIT_ALPHA.md`](PROOFKIT_ALPHA.md)  
→ **Primary tex**: [`unified_biquaternion_theory/solution_P4_fine_structure_constant/alpha_constant_derivation_precise.tex`](../unified_biquaternion_theory/solution_P4_fine_structure_constant/alpha_constant_derivation_precise.tex)

### 5b. Hubble Tension (~8%)

The 8–9% discrepancy between early-universe (H₀ ≈ 67 km/s/Mpc) and late-universe
(H₀ ≈ 73 km/s/Mpc) Hubble measurements is explained as **effective metric latency**:
complex-time phase `ψ` introduces a small systematic offset `δ` between measurement protocols.

| Quantity | Value |
|---|---|
| H₀ early (Planck) | 67.4 km/s/Mpc |
| H₀ late (SH0ES)   | 73.0 km/s/Mpc |
| δ (predicted overhead) | ≈ 0.078 (7.8%) |

→ **Full derivation**: [`docs/PROOFKIT_HUBBLE.md`](PROOFKIT_HUBBLE.md)  
→ **Script**: [`scripts/reproduce_hubble_prediction.py`](../scripts/reproduce_hubble_prediction.py)

### 5c. Electron Mass

UBT derives `m_e ≈ 0.5099 MeV` (0.22% difference from experiment 0.511 MeV) via the fermion mass formula from biquaternionic spectral theory.  
→ **Reference**: [`consolidation_project/appendix_E_m0_derivation_strict.tex`](../appendix_E_m0_derivation_strict.tex)

### 5d. Cosmological Predictions (CMB / Ω_b)

Running baryon density and CMB acoustic peak positions receive calculable UBT corrections.  
→ **Status**: [`STATUS_OBSERVATIONAL.md`](../STATUS_OBSERVATIONAL.md)

---

## 6. Verification Paths

| Claim | Derivation | Script | Status |
|---|---|---|---|
| GR recovery | [`appendix_R_GR_equivalence.tex`](../consolidation_project/appendix_R_GR_equivalence.tex) | — | Analytic |
| SU(3) emergence | [`Appendix_G_Emergent_SU3.tex`](../Appendix_G_Emergent_SU3.tex) | — | Analytic |
| α⁻¹ = 137 (bare) | [`alpha_constant_derivation_precise.tex`](../unified_biquaternion_theory/solution_P4_fine_structure_constant/alpha_constant_derivation_precise.tex) | [`emergent_alpha_calculator.py`](../ARCHIVE/legacy_variants/ubt_with_chronofactor/scripts/emergent_alpha_calculator.py) | Semi-empirical |
| α⁻¹ = 137.036 | [`STATUS_ALPHA.md`](../STATUS_ALPHA.md) | [`alpha_two_loop.py`](../alpha_core_repro/alpha_two_loop.py) | Numeric |
| Hubble tension δ ≈ 8% | [`appendix_HT_hubble_tension_metric_latency.tex`](../speculative_extensions/appendices/appendix_HT_hubble_tension_metric_latency.tex) | [`reproduce_hubble_prediction.py`](../scripts/reproduce_hubble_prediction.py) | Research front |
| Electron mass | [`appendix_E_m0_derivation_strict.tex`](../appendix_E_m0_derivation_strict.tex) | — | Semi-empirical |

---

## Quick Reference: Layer Structure

```
Layer 0/1  Geometry + Biquaternion Dynamics (FROZEN axioms)
    ↓      Emergent metric, gauge group, field equations
Layer B    Semi-empirical observables (α, m_e, Ω_b)
    ↓      Require quantum corrections; ~90% derived
Layer C    Research fronts (Hubble tension, CMB, neutrino masses)
    ↓      Testable hypotheses under active investigation
```

See [`UBT_LAYERED_STRUCTURE.md`](../UBT_LAYERED_STRUCTURE.md) and [`docs/architecture/LAYERS.md`](architecture/LAYERS.md).

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
