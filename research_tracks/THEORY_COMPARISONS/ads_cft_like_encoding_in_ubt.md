# AdS/CFT-Like Informational Encoding in UBT

**Author**: Ing. David Jaroš  
**Date**: 2026-03-12  
**Status**: Theoretical Analysis — Analogy Document

> © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0

---

## Executive Summary

This document formalizes the structural analogy between the Unified Biquaternion
Theory (UBT) and AdS/CFT-type holographic theories.

**Core claim**: UBT shares an *informational encoding architecture* with holographic
theories in the sense that a higher-dimensional field configuration (bulk-like Θ
dynamics over complex time τ = t + iψ) encodes and constrains the physics observed
in the lower-dimensional real-time sector (the boundary-like 4D spacetime
observable sector).

**What is NOT claimed**: UBT is not claimed to be literal AdS/CFT, to live on
Anti-de Sitter space, or to be dual to a conformal field theory on its boundary.

---

## 1. What Is Shared with AdS/CFT

### 1.1 Information Encoding Across Dimensional Levels

Both AdS/CFT and UBT exhibit a situation in which the full informational content
of a higher-dimensional dynamical system can be read off from data on a
lower-dimensional surface.

| Feature | AdS/CFT | UBT |
|---------|---------|-----|
| Higher-dimensional "bulk" | AdS_{d+1} with gravity | (ℝ⁴ × ℂ_τ) with Θ field |
| Lower-dimensional "boundary" | CFT on ℝ^d (or S^d) | Physical 4D spacetime M⁴ (ψ → 0 slice) |
| Encoding map | GKPW / Witten dictionary | Real-limit projection Θ(q,τ) → Θ(q,t) |
| Geometry from information | Ryu-Takayanagi: S = A/(4G) | Phase entropy ΔS_phase ↔ curvature R |
| Redundancy / code structure | Subregion duality, quantum error correction | Gauge redundancy of Θ modulo SU(3)×SU(2)×U(1) |

### 1.2 Geometry Emerging from Information Constraints

In both frameworks, the geometry of the observable sector is not postulated ab
initio but arises as a consequence of informational constraints encoded in a
richer object:

- **AdS/CFT**: Spacetime geometry (metric, curvature) is encoded in the entanglement
  structure of the boundary CFT (cf. Van Raamsdonk 2010, Maldacena 1997).
- **UBT**: The real metric g_μν and Einstein field equations emerge in the ψ → 0
  limit of the biquaternionic field equation
  ```
  ∇†∇Θ(q,τ) = κ𝒯(q,τ)
  ```
  The GR sector arises as a constrained semiclassical sector of the fuller Θ
  dynamics. The imaginary-time component ψ carries phase-curvature information
  that, when integrated out, produces the effective 4D geometry.

### 1.3 Code Subspace Structure

AdS/CFT holographic quantum error correction (Almheiri–Dong–Harlow 2015,
Pastawski et al. 2015) identifies the bulk effective field theory with a *code
subspace* inside the larger boundary Hilbert space.  UBT has an analogous
structure:

- The full Θ field lives in the extended (q, τ) domain.
- The physically observable sector (Standard Model fields, metric) corresponds to
  the **code subspace** defined by the real projection and the gauge constraints
  (color neutrality D_r + D_g + D_b = Π_color, electroweak gauge fixing, etc.).
- States outside this code subspace represent off-shell or pure-imaginary-time
  excitations that are not directly observable but contribute to renormalization
  and dark-sector corrections.

### 1.4 Bulk-Like vs Boundary-Like Description in UBT

The UBT framework admits a natural split into:

**Bulk-like description** (full complex-time domain):
- Field: Θ(q, τ) ∈ ℍ ⊗ ℂ  (biquaternion, 8 real degrees of freedom)
- Dynamics: `∇†∇Θ = κ𝒯`  in the extended (q, τ) domain
- Contains phase curvature, imaginary-time winding modes, p-adic extensions
- Accessible analytically via complex analysis; directly observable only indirectly

**Boundary-like description** (ψ = Im(τ) → 0 slice):
- Field: Standard Model fields φ, A_μ, ψ_f (Higgs, gauge, fermions) and metric g_μν
- Dynamics: Einstein equations + SM field equations
- Directly observable by experiment
- Constitutes the semiclassical GR+SM sector

The two descriptions are related by the real-limit map:
```
Θ(q, t + i·0) ↦ {g_μν(q,t), A_μ(q,t), φ(q,t), ψ_f(q,t)}
```
This parallels the GKPW dictionary of AdS/CFT without requiring AdS geometry.

---

## 2. What Is Not Claimed

The following claims are **explicitly NOT made** by this document or by UBT in
general:

1. **UBT is not claimed to be literal AdS/CFT.**  
   UBT does not posit Anti-de Sitter boundary conditions, a negative cosmological
   constant, or a dual conformal field theory in the mathematical sense of
   Maldacena (1997).

2. **UBT's boundary is not a CFT.**  
   The ψ → 0 boundary sector is physical 4D Minkowski/curved spacetime with
   Standard Model matter, not a scale-invariant conformal field theory.

3. **No Maldacena conjecture or holographic renormalization group flow is claimed.**  
   While there is a natural RG-like flow as ψ varies (the imaginary-time parameter
   acts as a UV regulator), no exact AdS/CFT duality has been established.

4. **No AdS geometry is required.**  
   UBT works for de Sitter, Minkowski, and general curved backgrounds.  The
   complex time extension τ = t + iψ is independent of the spatial curvature sign.

5. **No string-theoretic embedding is claimed.**  
   UBT does not require string theory, D-branes, or the large-N limit.

6. **No proof of holographic duality in the precise technical sense exists.**  
   The analogy is structural and motivational. It guides research directions but
   is not a proven mathematical theorem.

---

## 3. Bulk-Like vs Boundary-Like Description in UBT

*(This section expands on §1.4 with additional structure.)*

### 3.1 The Complex-Time Fiber as the "Bulk"

In AdS/CFT the extra radial coordinate r of AdS_{d+1} plays the role of the
energy/length scale of the boundary theory. In UBT, the imaginary time coordinate
ψ = Im(τ) plays an analogous role:

| AdS/CFT radial r | UBT imaginary time ψ |
|-----------------|----------------------|
| r → ∞: UV boundary | ψ → 0: classical/observable limit |
| r → 0: deep IR | ψ → ∞: UV / pure-phase sector |
| Bulk-to-boundary propagator | Real projection + mode expansion in ψ |
| Holographic renormalization | Phase-space renormalization in ψ |

This is a structural analogy, not an exact identification.

### 3.2 Field Dictionary

| AdS/CFT bulk field | UBT analog |
|-------------------|-----------|
| Graviton h_μν | Imaginary part Im(Θ) coupling to phase curvature |
| Gauge field A_M | Gauge components of Θ: project onto SU(3)×SU(2)×U(1) generators |
| Scalar Φ | Real part Re(Θ) / Higgs mode |
| Normalizable mode | Physical on-shell states at ψ = 0 |
| Non-normalizable mode | Source terms / boundary conditions at ψ = 0 |

### 3.3 Phase Entropy and Holographic Area

The UBT analogue of the Ryu-Takayanagi formula is the phase entropy formula:

```
ΔS_phase = (ψ₂ - ψ₁) · k_B · ln(dim H_color)
```

which contributes to the effective thermodynamic force producing dark-matter-like
effects (see `consolidation_project/appendix_H2_holography_variational.tex`).
This is structurally analogous to S = A/(4G_N) but is derived from UBT, not from
AdS/CFT.

---

## 4. Code Subspace Analogy

### 4.1 Holographic Quantum Error Correction (AdS/CFT)

In the Almheiri-Dong-Harlow (ADH) framework:
- Boundary Hilbert space H_bdy is large (all CFT states).
- Physical bulk operators are reconstructed from **subregions** of the boundary.
- The code subspace C ⊂ H_bdy encodes low-energy bulk effective field theory.
- Logical operators acting on C are protected against erasure of some boundary
  subregions (analogous to quantum error correction).

### 4.2 UBT Code Subspace

In UBT the analogous structure is:

**Full Hilbert space** H_Θ: All quantum states of the biquaternionic field Θ(q,τ),
including all values of ψ and all excitation modes.

**Code subspace** C_obs ⊂ H_Θ: States satisfying:
1. Real projection: ψ-dependent part in lowest-Fourier mode (semiclassical limit)
2. Color neutrality: D_r + D_g + D_b = Π_color (eliminates u(1) ⊂ u(3))
3. Electroweak gauge fixing and SU(3) Gauss law constraints
4. On-shell condition: ∇†∇Θ|_{ψ=0} = κ𝒯|_{ψ=0}

States in C_obs correspond to **physical observable particles and fields**.
States outside C_obs represent gauge copies, off-shell excitations, and
imaginary-time modes (dark sector, quantum corrections).

**Error-correction analogy**: The gauge constraints of UBT act as **stabilizer
conditions** that protect the physical sector C_obs against unphysical perturbations
(gauge transformations, imaginary-time fluctuations). This is structurally parallel
to quantum error correction in the code-subspace sense.

---

## 5. Geometry from Information Constraints

### 5.1 Entanglement and Geometry (AdS/CFT)

In AdS/CFT, geometry is not fundamental — it emerges from entanglement:
- Disconnected boundary → disconnected bulk (ER = EPR, Maldacena 2013)
- Entanglement entropy ↔ minimal surface area (Ryu-Takayanagi)
- Modular Hamiltonian ↔ bulk geometry near the surface

### 5.2 UBT: Geometry from Phase Constraints

In UBT, observable geometry emerges from phase/information constraints in the
complex-time domain:

1. **Phase winding** (topological): Closed loops in the complex-τ plane contribute
   to vacuum energy and cosmological constant via winding number quantization.

2. **Phase coherence** (local): The condition that Θ(q, τ) be analytic in τ
   (holomorphic) constrains the real-sector metric to satisfy Einstein's equations
   in the semiclassical limit — geometry is a consequence of analyticity.

3. **Information metric**: The Fisher information metric on the space of τ-values
   (parametrizing different semiclassical backgrounds) induces a natural metric on
   the space of classical solutions, analogous to the information-theoretic
   derivation of gravity (Jacobson 1995).

4. **Constraint summary**: The GR sector arises as a constrained semiclassical
   sector of the fuller Θ dynamics. This is the UBT counterpart of "geometry
   from entanglement."

---

## 6. Status Summary

| Claim | Status |
|-------|--------|
| UBT has bulk/boundary split (complex vs real time) | ✅ Established within UBT |
| GR emerges as real limit of Θ dynamics | ✅ Proved (see appendix_R_GR_equivalence.tex) |
| Code subspace structure (gauge constraints) | ✅ Identified |
| Phase entropy analogue of Ryu-Takayanagi | ✅ Derived (appendix_H2) |
| UBT is literal AdS/CFT | ❌ Not claimed |
| UBT dual CFT identified | ❌ Not established |
| Holographic entanglement entropy proven from UBT | 🔶 Conjectural / open |
| Exact bulk reconstruction from boundary data | 🔶 Partial (real-limit projection) |

---

## 7. References

- Maldacena, J. (1997). "The Large N limit of superconformal field theories and
  supergravity." arXiv:hep-th/9711200.
- Almheiri, A., Dong, X., Harlow, D. (2015). "Bulk Locality and Quantum Error
  Correction in AdS/CFT." arXiv:1411.7041.
- Van Raamsdonk, M. (2010). "Building up spacetime with quantum entanglement."
  arXiv:1005.3035.
- Pastawski, F. et al. (2015). "Holographic quantum error-correcting codes."
  arXiv:1503.06237.
- Jaroš, D. — `consolidation_project/appendix_H2_holography_variational.tex`
- Jaroš, D. — `consolidation_project/appendix_R_GR_equivalence.tex`
- Jaroš, D. — `HOLOGRAPHIC_EXTENSION_GUIDE.md`
- Jaroš, D. — `research/moduli_space_ads_vs_physical_ds.tex`
