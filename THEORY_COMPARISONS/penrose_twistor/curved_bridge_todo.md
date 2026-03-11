# Curved Spacetime Bridge Extension: Investigation Plan

**Module**: `THEORY_COMPARISONS/penrose_twistor/`  
**Date**: 2026-03-11  
**Priority**: P2 (after flat-space bridge is rigorously documented)  
**Hard rule**: Do NOT claim nonlinear graviton correspondence without proof.

---

## Overview

The existing penrose_twistor sandbox establishes a structural bridge between UBT and
twistor theory in **flat Minkowski space**.  This document outlines the investigation
needed to extend (or characterize the failure of extension) to **curved spacetime**.

The guiding principle is caution: Penrose's nonlinear graviton construction (1976) is
a non-trivial result requiring anti-self-dual (ASD) Ricci-flat complex metrics.
UBT's emergent metric from the real sector of the biquaternion field is not assumed
ASD; claiming nonlinear graviton correspondence would require proving this.

---

## 1. Background: Twistor Theory in Curved Spacetime

### 1.1 Penrose's Nonlinear Graviton

Penrose (1976) showed that **anti-self-dual (ASD) Ricci-flat complex 4-manifolds** are
in bijective correspondence with deformations of (an open set of) projective twistor space
PT = CP³.

**Precise scope**:
- Applies to Ricci-flat metrics (vacuum Einstein equations, T_μν = 0)
- Applies to anti-self-dual metrics (Weyl curvature satisfies W⁺ = 0)
- Requires working with *complex* spacetime (not Lorentzian)
- Result is local and holomorphic; global statements are more delicate

**Not covered**:
- Metrics with matter (T_μν ≠ 0)
- Lorentzian (real) signature spacetimes directly
- Self-dual or generic (non-ASD) Weyl curvature

### 1.2 Ward Construction

Ward (1977) extended this to gauge fields: ASD Yang–Mills fields on S⁴ ↔ holomorphic
vector bundles over CP³.  A partial extension to the full Yang–Mills case (not just
ASD) remains difficult.

---

## 2. Investigation Topics

### 2.1 Conformal structure of the UBT emergent metric

**Question**: Does the emergent metric g_μν = Re[∂_μΘ ∂_νΘ† / 𝒩] carry a natural
conformal structure compatible with twistor methods?

**Why it matters**: Twistor theory is inherently conformal (it encodes the null cone
structure, invariant under Weyl rescaling g → Ω² g).  If UBT's metric is naturally
defined up to conformal factor, a twistor description could be more natural.

**Note**: The normalization 𝒩[Θ] in the UBT metric definition introduces an
*explicit* conformal factor.  Different choices of 𝒩 give conformally equivalent
metrics.  This suggests the emergent metric lives in a conformal class, which is
exactly the right input for twistor methods.

**Feasibility**: Medium.  Requires writing down the conformal class explicitly and
checking whether it corresponds to a positive-definite or Lorentzian conformal structure.

**Status**: Not started.

---

### 2.2 Null congruences in the UBT metric sector

**Question**: Do null geodesics of the UBT emergent metric form any special families
(congruences with special optical scalars: shear, twist, expansion)?

**Why it matters**: In twistor theory, Penrose's fundamental insight is that null
geodesic congruences correspond to points in twistor space.  If UBT null congruences
have special properties (e.g. shear-free), they might admit a twistor description.

**Shear-free condition**: A null congruence is shear-free if its complex shear scalar
ρ̂ = 0.  The Goldberg–Sachs theorem relates shear-free congruences to the algebraic
special Weyl tensor structure.

**Feasibility**: High for linearized perturbations; difficult for nonlinear.

**Status**: Not started.

---

### 2.3 Anti-self-dual (ASD) sector of UBT metric

**Question**: Is the anti-self-dual part of the Weyl tensor of the UBT emergent
metric nonzero in general?  Is there a natural ASD limit?

**Why it matters**: The nonlinear graviton construction requires W⁺ = 0.

**UBT context**:
- Generic biquaternion fields Θ will produce metrics with both self-dual (W⁺) and
  anti-self-dual (W⁻) Weyl components.
- A UBT "twistor sector" would require identifying field configurations Θ for which
  W⁺ = 0 (or W⁻ = 0 depending on orientation convention).
- Whether such configurations are generic, special, or inconsistent with the UBT
  field equation ∇†∇Θ = κ𝒯 is unknown.

**Feasibility**: Requires explicit metric and curvature computation from UBT field;
technically feasible but computationally intensive.

**Status**: Not started.

---

### 2.4 Real-projected metric and twistor-friendly sectors

**Question**: When the full biquaternion metric 𝒢_μν (complex-valued) is projected
to its real part g_μν = Re(𝒢_μν), does the resulting Lorentzian metric admit any
special structure that simplifies twistor analysis?

**Why it matters**: Standard twistor theory works with complex or Riemannian (positive
definite) metrics directly.  Lorentzian signature requires a separate treatment
(e.g. real twistors, Robinson congruences, ...).

**Possible outcome A**: The real-projected metric is generic Lorentzian with no
special twistor structure → twistor methods do not apply directly to the real sector.

**Possible outcome B**: For specific solutions (e.g. vacuum, ψ = 0 sector), the
real metric has ASD Weyl tensor → nonlinear graviton applies locally.

**Status**: Not started.  Outcome A is expected generically.

---

## 3. Small Non-Committal Experiment (if feasible)

If time permits, the following minimal experiment could provide evidence:

**Experiment**: Compute the self-dual / anti-self-dual decomposition of the Weyl
tensor for the simplest non-trivial UBT metric (e.g. linearized perturbation around
flat Minkowski).

**Input**: The linearized metric perturbation h_μν from UBT, computed from a simple
plane-wave Θ field.

**Output**: Weyl tensor W_μνρσ; its SD/ASD decomposition W = W⁺ + W⁻.

**Expected result**: W⁺ ≠ 0 in general, confirming that the linearized UBT metric
does not automatically lie in the nonlinear graviton sector.

**Location if implemented**: `experiments/e09_weyl_asd_check.py` (to be created)

**Status**: Planned, not implemented.

---

## 4. What NOT to Claim

- **Do NOT** claim that UBT has a nonlinear graviton construction without showing
  ASD Weyl tensor.
- **Do NOT** claim that UBT's curved metric is encoded in twistor space without an
  explicit construction (Penrose's theorem requires Ricci-flat ASD, not general).
- **Do NOT** equate "UBT metric comes from biquaternion field" with "UBT metric is
  encoded by a twistor deformation" — these are different statements.

---

## 5. Current Status Summary

| Topic | Status | Next step |
|-------|--------|-----------|
| Flat-space spinor bridge | ✅ done | See `STATUS.md` |
| Conformal structure of UBT metric | ❓ not started | Analyze 𝒩-dependence |
| Null congruences in UBT | ❓ not started | Compute optical scalars |
| ASD sector of UBT metric | ❓ not started | Need explicit metric |
| Nonlinear graviton claim | ❌ not justified | Requires ASD + Ricci-flat proof |

---

## References

- Penrose, R. (1976). Nonlinear gravitons and curved twistor theory.
  *General Relativity and Gravitation*, 7, 31–52.
- Ward, R.S. (1977). On self-dual gauge fields. *Phys. Lett. A*, 61, 81–82.
- Mason, L. & Woodhouse, N.M.J. (1996). *Integrability, Self-Duality, and Twistor
  Theory*. Oxford UP.
- UBT GR recovery: `canonical/geometry/gr_as_limit.tex`,
  `consolidation_project/GR_closure/`
