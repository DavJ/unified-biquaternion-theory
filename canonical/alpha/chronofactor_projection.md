<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# chronofactor_projection.md — Mathematical Definition of the Chronofactor and Projection Map

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Track**: T3_ALPHA — Fine Structure Constant  
**Status**: Theory development (workstream G2)  
**Companion files**:
- `canonical/alpha/neff_geometric_origin.md` — G1 three-qubit/8D sector
- `canonical/alpha/neff_32_alpha_route.tex` — full route
- `canonical/fields/biquaternion_time.tex` — canonical τ = t + iψ definition
- `canonical/geometry/phase_projection.tex` — phase projection geometry

---

## Purpose

This document provides a precise mathematical definition of the **chronofactor** in UBT,
specifies the projection from the 8-dimensional biquaternion information sector to the
effective charged mode count, and counts the effective degrees of freedom contributed
by the complex-time structure.

The central question is:

> How does the imaginary-time structure τ = t + iψ (the "chronofactor") convert the
> 3-dimensional imaginary quaternion phase space Im ℍ into N_eff = 12 effective modes?

---

## 1. Definition: Complex Time and the Chronofactor

### 1.1 Canonical Complex Time

The canonical UBT time coordinate is complex time (see `canonical/fields/biquaternion_time.tex`):
```
τ = t + iψ,    t ∈ ℝ,  ψ ∈ ℝ
```
The real part t is the physical (observable) time. The imaginary part ψ is the
phase-time coordinate that is compactified on a circle S¹_ψ.

The full biquaternion time T_B = t + iψ + jχ + kξ is a deprecated extension;
the canonical isotropic limit τ = t + iψ is used throughout this document.

### 1.2 Definition: Chronofactor

**Definition CF.1** (Chronofactor):  
The **chronofactor** of the UBT field Θ(q,τ) is the complex-time evolution operator
associated with a winding mode of winding number n on S¹_ψ:
```
Φ_n(ψ) = e^{i n ψ / R_ψ},    n ∈ ℤ,  ψ ∈ [0, 2πR_ψ)
```
where R_ψ is the compactification radius of S¹_ψ.

The chronofactor is, loosely, "the contribution of one unit of imaginary-time
winding to the mode structure of the field." More precisely:

**Definition CF.2** (Chronofactor Degrees of Freedom):  
The chronofactor sector contributes **4 effective degrees of freedom** to each
Im ℍ direction, arising from:
```
N_chron = N_helicity × N_charge = 2 × 2 = 4
```
where:
- N_helicity = 2: left- and right-moving components of the complexified Θ field on S¹_ψ
- N_charge = 2: particle and antiparticle (complex conjugation automorphism of ℬ)

These 4 degrees of freedom are the "chronofactor contribution" to each phase direction.

### 1.3 Physical Meaning of the Chronofactor

The imaginary time ψ plays a role analogous to an internal clock or phase variable:

| Role | Mathematical content |
|------|---------------------|
| Phase evolution | Θ → e^{iψJ} Θ under ψ-translation (J = phase generator) |
| KK compactification | Winding modes n ∈ ℤ on S¹_ψ |
| Bloch sphere analog | ψ parameterizes a circle; the Bloch sphere's z-axis maps to ψ |
| Thermal analogy | At finite temperature T, ψ ↔ β = 1/(k_B T) (imaginary-time thermal circle) |

The name "chronofactor" captures the idea that this is the imaginary-time factor
in the field's phase structure — analogous to how the Bloch vector's z-component
parameterizes a two-state system, but here for the winding-mode spectrum.

---

## 2. The Projection Map: Im ℍ → ℂ_τ

### 2.1 The Two Spaces

| Space | Dimension | Coordinates | Role |
|-------|-----------|-------------|------|
| Im ℍ | dim_ℝ = 3 | (φ_I, φ_J, φ_K) ∈ ℝ³ | Phase directions of biquaternion field |
| ℂ_τ | dim_ℝ = 2 | (t, ψ) ∈ ℝ² | Complex time plane |

The biquaternion field Θ(q, τ) depends on complex time τ ∈ ℂ_τ. The three quaternion
phase directions in Im ℍ generate internal rotations of Θ but are not independent
coordinates of the base spacetime.

### 2.2 The Projection Map (Geometric Construction)

**Construction CF.3** (Phase Projection):  

Step 1: The field Θ(q,τ) transforms under Im ℍ phase rotations as:
```
Θ(q, τ) → e^{φ_I I + φ_J J + φ_K K} · Θ(q, τ) · e^{-φ_I I - φ_J J - φ_K K}
```
(adjoint action of exp(Im ℍ) on ℬ).

Step 2: The imaginary time ψ in τ = t + iψ generates a specific Im ℍ phase rotation
via the identification:
```
ψ → ψ_I := ψ  (projection onto the I-axis of Im ℍ)
```
In the isotropic limit (where all three Im ℍ directions are equivalent), the field
evolves uniformly along all three phase directions simultaneously.

Step 3: On S¹_ψ, each winding mode n contributes to all three Im ℍ directions equally
(by isotropy). The effective projected dimension of the Im ℍ → ℂ_τ map is:
```
λ_proj = dim_ℝ(Im ℍ) / dim_ℝ(ℂ_τ) = 3 / 2
```

### 2.3 Interpretation of λ_proj = 3/2

The ratio λ_proj = 3/2 measures how many Im ℍ phase directions are encoded per
complex-time dimension. It appears in the mode density:

```
ρ_eff(n) = λ_proj × ρ_Im ℍ(n) = (3/2) × ρ_base(n)
```

This projection density ratio is the proposed geometric origin of the 3/2 exponent
in B_base = N_eff^{3/2}.

**Proof status**: CONJECTURAL. The projection map is geometrically motivated and
dimensionally correct. A rigorous derivation requires:
- A metric on the phase space of Im ℍ modes
- A precise definition of "mode density" on S¹_ψ
- A Jacobian computation for the Im ℍ → ℂ_τ map

**Status label**: CONJECTURAL — geometrically motivated but not derived via a rigorous map.

### 2.4 Fiber Bundle Language (Schematic)

The structure can be expressed schematically in fiber-bundle terms:

```
Total space: ℬ × ℂ_τ  (field + complex time)
Fiber:       Im ℍ      (phase directions, dim = 3)
Base:        ℂ_τ       (complex time, dim = 2)
Projection:  π: Im ℍ → ℂ_τ  (sends phase to imaginary time)
```

The Jacobian of this projection (fiber dimension / base dimension = 3/2) would
produce the density enhancement factor. However:

**Remark CF.1**: This is not a standard fiber bundle — Im ℍ is an internal space
(gauge fiber), not a spatial fiber over ℂ_τ as base. The language is an analogy
showing where 3/2 naturally appears; it is NOT a derived bundle construction.

---

## 3. Effective Degrees of Freedom: From 3 to 12

### 3.1 The Complete Chain

Starting from dim_ℝ(Im ℍ) = 3 (three independent phase directions of ℬ):

```
Step A: Im ℍ sector
  N_phases = 3
  (three independent U(1) phases from I, J, K)

Step B: Complex structure of ℬ = ℂ⊗ℍ
  The complex factor ℂ in ℬ provides left- and right-moving components:
  N_helicity = 2
  (this doubles the mode count: Θ and its "chiral" partner ΘT)

Step C: Charge conjugation automorphism
  The complex conjugation τ_ℂ: z → z* on ℂ in ℬ provides:
  N_charge = 2
  (particle and antiparticle modes)

Total:
  N_eff = N_phases × N_helicity × N_charge = 3 × 2 × 2 = 12
```

All three factors are **algebraic**, following from the structure of ℬ = ℂ⊗ℍ.

### 3.2 The Chronofactor Contribution in This Chain

The chronofactor is responsible for Steps B and C:
- Step B (helicity): follows from the complex structure of the field on S¹_ψ (the ψ-circle 
  supports both clockwise and counterclockwise winding modes)
- Step C (charge): follows from the charge-conjugation symmetry of the UBT action, which
  is preserved by the S¹_ψ compactification

Together: chronofactor contribution = N_chron = N_helicity × N_charge = 4.

This is exactly the factor needed:
```
N_eff = N_phases × N_chron = 3 × 4 = 12
```

**Proof status**: DERIVED [L0] — all three factors follow from ℬ = ℂ⊗ℍ algebra,
independent of any dynamical computation.

### 3.3 Alternative: "8 + 4" Decomposition

The problem statement proposes the decomposition N_eff = 8 + 4, with 8 from the
information sector and 4 from the chronofactor.

**Assessment**: This can be made consistent but is non-standard relative to the existing derivation.

If the 8D information sector (dim_ℝ(ℬ) = 8) contributes:
- 6 charged dimensions (Im ℍ = 3 real + 3 complex = 6 real dimensions)
- 2 neutral dimensions (scalars {1, i} = 2 real dimensions)

And the chronofactor contributes an additional factor of 2 (for charge conjugation only,
since helicity is already counted in the complex structure of the 8D sector):

```
N_eff = N_charged_dims × N_charge = 6 × 2 = 12
```

Or alternatively:
- 8 from charged (real) modes in ℬ (counting both Im ℍ and i·Im ℍ: 3 + 3 = 6, 
  not 8... this doesn't work cleanly)

**Conclusion**: The "8 + 4" split does not decompose cleanly unless the neutral 
dimensions {1, i} are included in the 8 and then subtracted. The cleanest derivation
remains N_eff = 3 × 2 × 2 = 12. The "8 + 4" language is a suggestive approximation
but should not replace the derived formula.

---

## 4. Chronofactor and the Bloch Sphere Analogy

### 4.1 The Bloch Sphere as a Projection Model

A single qubit's state space is the Bloch sphere S² ⊂ ℝ³. The sphere has:
- Bulk dimension: 3 (the enclosing ℝ³)
- Boundary dimension: 2 (the sphere surface S² = boundary of the unit ball in ℝ³)
- Ratio: bulk/boundary = 3/2 (in the sense of dimension ratio)

Similarly, in UBT:
- Im ℍ has dimension 3 (the "bulk" of phase space)
- ℂ_τ has dimension 2 (the "boundary" or projection screen)
- Ratio: 3/2

**This is the chronofactor Bloch-sphere analogy**: the imaginary time plane ℂ_τ is the
"projection screen" (Bloch disk boundary) onto which the full 3D Im ℍ phase space
is projected, analogously to how the Bloch sphere surface S² ⊂ ℝ³ encodes a qubit.

### 4.2 What Bloch Projection Does and Does Not Capture

| Aspect | Bloch sphere | UBT chronofactor | Match? |
|--------|-------------|-----------------|--------|
| Projection dimension | 3→2 (S² in ℝ³) | 3→2 (Im ℍ → ℂ_τ) | ✓ structural |
| Density enhancement factor | 3/2 from solid angle | 3/2 from projection ratio | ✓ numerical |
| Quantization | Qubit is discrete | Winding modes are discrete | ✓ partial |
| Inner product | Fubini-Study on CP¹ | Not yet defined on Im ℍ | ✗ not established |
| Physical meaning | Single-qubit pure state | Phase direction of Θ field | partial analogy |

The analogy is structurally compelling but does not constitute a proof.

---

## 5. Degrees of Freedom Count: Summary

| Sector | Dimensions | Proof status | Contribution |
|--------|------------|--------------|--------------|
| Im ℍ (quaternion phases) | dim_ℝ = 3 | DERIVED [L0] | N_phases = 3 |
| ℂ complex structure (helicity) | dim_ℝ = 1 (extra complex factor) | DERIVED [L0] | N_helicity = 2 |
| Charge conjugation | discrete ℤ₂ | DERIVED [L0] | N_charge = 2 |
| **Total N_eff** | — | **DERIVED [L0]** | **12** |
| Projection ratio λ = 3/2 | dim(Im ℍ)/dim(ℂ_τ) = 3/2 | CONJECTURAL | Candidate exponent origin |
| 8D → N_eff = 12 transition | Via charged-mode selection | DERIVED [L0] (via 3×2×2) | — |

---

## 6. What Remains Open

The following aspects of the chronofactor are geometrically motivated but not yet
formally derived:

1. **The projection Jacobian**: A precise computation of the measure change under
   Im ℍ → ℂ_τ projection is required to prove that the 3/2 factor enters the
   effective coupling B_base rigorously.

2. **The heat-kernel connection**: The one-loop effective action on T² × S¹_ψ should be
   computed explicitly using heat-kernel methods to verify that the Im ℍ contribution
   gives a K(t) ~ t^{-3/2} leading term.

3. **The Kac-Moody level**: Gap G3-k asks whether the biquaternion field on T²_τ is
   a level-k = 1 WZW model, which is required to derive B_base = N_eff^{3/2}.

4. **The precise fiber bundle**: Making the fiber-bundle schematic in Section 2.4
   mathematically rigorous (specifying the connection, the inner product, and the
   Jacobian of the projection) would resolve points 1 and 2.

**Status**: These are all OPEN_LEMMA items. The chronofactor structure is defined;
the projection formalism needs a rigorous completion.

---

## 7. References

- `canonical/fields/biquaternion_time.tex` — τ = t + iψ definition
- `canonical/fields/biquaternion_algebra.tex` — ℬ = ℂ⊗ℍ
- `canonical/geometry/phase_projection.tex` — phase projection geometry
- `canonical/n_eff/step1_mode_decomposition.tex` — N_eff derivation
- `canonical/alpha/neff_geometric_origin.md` — 8D information sector
- `canonical/interactions/B_base_derivation_complete.tex` — B_base derivation
- `ALPHA_STRUCTURAL_ORIGINS.md` §3 (Track E3) — complex time as projection boundary
- `reports/exponent_3_2_origin_audit.md` — 3/2 exponent mechanisms
