<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# PROOFKIT: Gauge Sector

> **Status**: Layer A/B — Core ontology for U(1); semi-empirical for SU(3) and SU(2)  
> **Claim**: The SM gauge group SU(3) × SU(2) × U(1) is not postulated but emerges from the algebraic automorphism structure of the biquaternionic field Θ(q, τ).

---

## 1. Summary

| Gauge Factor | Origin in UBT | Algebraic Structure | Status |
|---|---|---|---|
| U(1) EM | Complex phase Aut(ℂ) | Complex time ψ-cycle | Proven |
| SU(2) Weak | Quaternion left-action Aut(ℍ)_L | Quaternionic sector | Semi-empirical |
| SU(3) Colour | Octonionic extension G₂ ⊃ SU(3) | Internal phase 3-space | Semi-empirical |

---

## 2. SU(3) Colour Emergence

### Algebraic origin

The biquaternionic field Θ ∈ ℂ ⊗ ℍ has three independent imaginary quaternionic axes:
`i, j, k`.

Each carries an independent complex phase `ψ₁, ψ₂, ψ₃` within the complex-time structure.
The traceless unitary automorphism of this 3-dimensional internal phase space is:

```
SU(3)_colour = { U ∈ U(3) | det U = 1 }
```

The mapping to QCD colour charges:

| Quaternion Axis | Phase | Colour |
|---|---|---|
| i | ψ₁ | Red |
| j | ψ₂ | Green |
| k | ψ₃ | Blue |

### Theta-function realisation

A concrete realisation uses multi-variable theta functions:

```
Θ(x, τ) = Σ_{n ∈ ℤ³} exp( iπ nᵀ Ω(x,τ) n + 2πi nᵀ z(x,τ) ) · Ξ(x,τ)
```

where `Ω ∈ Mat(3×3, ℂ)` is the period matrix (Im Ω > 0) and `z ∈ ℂ³` is the internal
phase coordinate corresponding to the three quaternionic axes.

### Colour gauge connection and Yang–Mills term

The SU(3) colour connection arises from the internal phase geometry:

```
A_μ = 𝒰† ∂_μ 𝒰 − (1/3) tr(𝒰† ∂_μ 𝒰) · 1₃   ∈ su(3)
```

where `𝒰(x, τ) ∈ U(3)` is the unitary phase frame on the internal fiber.

The Yang–Mills field strength:

```
F_{μν} = ∂_μ A_ν − ∂_ν A_μ + [A_μ, A_ν]   ∈ su(3)
```

The Yang–Mills kinetic term in the UBT action:

```
ℒ_YM = − (1/4) tr(F_{μν} F^{μν})
```

emerges from the kinetic term of Θ after projecting onto the SU(3) colour sector.

### Compatibility with GR

The biquaternionic metric `𝒢_{μν} = Sc(Θ† Θ)` is invariant under SU(3) colour rotations.
Therefore the GR metric `g_{μν} = Re(𝒢_{μν})` and Einstein field equations are unaffected
by the colour sector, which acts only on internal phase degrees of freedom.

**References**:  
- [`Appendix_G_Emergent_SU3.tex`](../Appendix_G_Emergent_SU3.tex)  
- [`consolidation_project/appendix_G_internal_color_symmetry.tex`](../consolidation_project/appendix_G_internal_color_symmetry.tex)  
- [`consolidation_project/appendix_E_SM_QCD_embedding.tex`](../consolidation_project/appendix_E_SM_QCD_embedding.tex)

---

## 3. SU(2) Weak Sector

### Algebraic origin

The quaternionic algebra ℍ has automorphism group `Aut(ℍ) = SO(3) ≅ SU(2)/ℤ₂`.

Restricting to **left-handed** quaternionic action gives `SU(2)_L`.

In UBT, the left-chiral projection of the biquaternionic field:

```
Θ_L = ½(1 − γ₅) Θ
```

transforms under `SU(2)_L`, while `Θ_R` is a singlet — reproducing the
chiral structure of the weak interaction.

**References**:  
- [`consolidation_project/appendix_E2_SM_geometry.tex`](../consolidation_project/appendix_E2_SM_geometry.tex)  
- [`QED_SM_FROM_UBT_ANALYSIS.md`](../QED_SM_FROM_UBT_ANALYSIS.md)

---

## 4. U(1) Electromagnetic Sector

### Algebraic origin

The complex factor ℂ in `ℂ ⊗ ℍ` has automorphism group `Aut(ℂ) = U(1)`.

This is the electromagnetic U(1) gauge symmetry. The U(1) gauge field `A_μ` is the
connection on the complex-phase fiber over spacetime.

The winding quantisation of the ψ-cycle gives the coupling constant α
(see [`docs/PROOFKIT_ALPHA.md`](PROOFKIT_ALPHA.md)).

### QED limit

In the `∂_ψ = 0` (constant phase) limit:

```
∇†∇ Θ  →  (i ∂/ − e A/ − m) ψ = 0   [Dirac equation]
∂[μ F^{μν}] = e ψ̄ γ^ν ψ             [Maxwell equation]
```

QED is **exactly recovered** from UBT in this limit.

**References**:  
- [`consolidation_project/appendix_C_electromagnetism_gauge_consolidated.tex`](../consolidation_project/appendix_C_electromagnetism_gauge_consolidated.tex)  
- [`consolidation_project/appendix_D_qed_consolidated.tex`](../consolidation_project/appendix_D_qed_consolidated.tex)

---

## 5. Full Gauge Connection: SM from UBT Geometry

The complete emergence chain:

```
UBT biquaternionic algebra   ℂ ⊗ ℍ  (extended octionically: ℂ ⊗ 𝕆)
        ↓
Automorphism group of internal algebra
        ↓
Aut(ℂ) × Aut(ℍ)_L × [Aut(𝕆) ⊃ G₂ ⊃ SU(3)]
        ↓
  U(1)  ×   SU(2)_L   ×          SU(3)
        ↓
Standard Model gauge group SU(3)_c × SU(2)_L × U(1)_Y
```

**No additional gauge bosons or interactions are assumed.**

**References**:  
- [`QED_SM_FROM_UBT_ANALYSIS.md`](../QED_SM_FROM_UBT_ANALYSIS.md)  
- [`SM_GEOMETRIC_EMERGENCE_DRAFT.md`](../SM_GEOMETRIC_EMERGENCE_DRAFT.md)  
- [`SM_GAUGE_GROUP_RIGOROUS_DERIVATION.md`](../SM_GAUGE_GROUP_RIGOROUS_DERIVATION.md)

---

## 6. Yang–Mills Kinetic Term

The Yang–Mills kinetic term for all gauge factors follows from the
biquaternionic field equation:

```
ℒ_gauge = − (1/4g²) tr(F_{μν}^a F^{aμν})
```

This emerges from the gauge-covariant derivative term in the UBT action:

```
S_UBT ∝ ∫ tr[ (D_μ Θ)† D^μ Θ ] d⁴x dτ
```

after decomposing `D_μ Θ` into spin/gauge/metric components.

---

## 7. Open Questions

1. **Octonionic extension**: SU(3) derivation from `ℂ ⊗ 𝕆` requires non-associativity
   to be handled carefully. The octonionic sector is the main technical challenge.
2. **Electroweak mixing**: The Weinberg angle sin²θ_W is not yet fully derived from UBT.
   Current status: sketch in [`consolidation_project/appendix_K2_fundamental_constants_consolidated.tex`](../consolidation_project/appendix_K2_fundamental_constants_consolidated.tex).
3. **Higgs mechanism**: Mass generation via spontaneous symmetry breaking within UBT
   is under development.

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
