<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->


# neff_geometric_origin.md — Geometric and Information-Theoretic Origin of N_eff

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Track**: T3_ALPHA — Fine Structure Constant  
**Status**: Theory development (workstreams G1, G2 overview, G4)  
**Companion files**:
- `canonical/alpha/chronofactor_projection.md` — G2 detailed construction
- `canonical/alpha/neff_32_alpha_route.tex` — full G5 route
- `ALPHA_STRUCTURAL_ORIGINS.md` — executive summary of all tracks
- `reports/neff_12_dimension_count_audit.md` — N_eff = 12 route audit

---

## Purpose

This document formalizes the geometric and information-theoretic origin of:

1. The three-qubit Hilbert structure as the information sector of the biquaternion algebra  
2. The 8-dimensional state space and its correspondence to the biquaternion real structure  
3. The connection from this 8D structure to N_eff = 12 via the chronofactor projection  
4. The E8/sphere-packing question as an analogy probe (assessed, not claimed)

The organizing principle is:

> **Geometry first, numbers second.**  
> N_eff = 12 must be read from the algebraic structure of ℬ = ℂ⊗ℍ.  
> The 3/2 exponent must be read from a dimensional ratio or spectral scaling law.  
> Neither may be inserted to match α⁻¹ = 137.

---

## 1. Workstream G1: Three-Qubit Hilbert Structure and the 8D Information Sector

### 1.1 Definition of the Three-Qubit Hilbert Space

**Definition G1.1** (Three-Qubit Hilbert Space):  
The three-qubit Hilbert space is
```
ℋ_3q = (ℂ²)^{⊗3} = ℂ² ⊗ ℂ² ⊗ ℂ²
```
with standard basis |abc⟩, a,b,c ∈ {0,1}:
```
|000⟩, |001⟩, |010⟩, |011⟩, |100⟩, |101⟩, |110⟩, |111⟩
```
**dim_ℂ(ℋ_3q) = 8**.

### 1.2 Relation to the Biquaternion Algebra

The biquaternion algebra ℬ = ℂ⊗_ℝ ℍ (see `canonical/fields/biquaternion_algebra.tex`) has:

| Space | Basis over ℝ | dim_ℝ | dim_ℂ |
|-------|-------------|--------|--------|
| ℍ (quaternions) | {1, I, J, K} | 4 | — |
| ℂ (complex plane) | {1, i} | 2 | 1 |
| ℬ = ℂ⊗ℍ | {1, I, J, K, i, iI, iJ, iK} | **8** | 4 |

The real dimension of ℬ is **8**. This matches the *complex* dimension of ℋ_3q.

**Connection**: The three-qubit state space ℋ_3q has dim_ℂ = 8 = dim_ℝ(ℬ). This numerical equality suggests a structural correspondence: the 8 complex dimensions of ℋ_3q map one-to-one (as an ℝ-module) to the 8 real dimensions of ℬ.

**Proof status**: CONJECTURAL — the numerical equality is established; a natural isomorphism
of ℋ_3q ≅ ℬ_ℝ (as real vector spaces only, not as algebras) is straightforward to
construct but does not carry algebraic structure across. See Remark G1.1.

**Remark G1.1** (Limits of the correspondence):  
ℋ_3q over ℂ has dim_ℂ = 8 ≠ dim_ℂ(ℬ) = 4.  
The identification works only at the level of real vector spaces, not complex structures.  
In particular, ℋ_3q is a Hilbert space with inner product, while ℬ is an algebra with product.  
Any statement connecting three-qubit states to biquaternion field modes must specify
which structure is being used.

### 1.3 Physical Interpretation of the Three Qubits

Within UBT, the three qubits can be assigned to three physically distinct binary degrees of freedom arising from the SM gauge structure embedded in ℬ:

| Qubit label | Physical meaning | Algebraic origin in ℬ |
|-------------|-----------------|----------------------|
| q₁ (color parity) | Even/odd color parity of a color triplet state | ℤ₂ subgroup of SU(3)_c |
| q₂ (weak isospin) | Isospin up/down, T₃ = ±1/2 | SU(2)_L subgroup of ℬ |
| q₃ (charge-conjugation) | Particle vs. antiparticle | Complex conjugation automorphism of ℬ |

**Important caveat**: The color degree of freedom is properly a **qutrit** (3 states: r, g, b),
not a qubit. The label "q₁ (color parity)" encodes only the Z₂ parity of the color
state, not its full SU(3) content. The full color sector contributes 3 modes (r, g, b),
not 2.

A more precise "three-qubit" interpretation must either:
- (a) Accept that color is a qutrit and the three-qubit language is an approximation, or
- (b) Use a two-qubit encoding of color: |r⟩ = |00⟩, |g⟩ = |01⟩, |b⟩ = |10⟩ (with |11⟩
  representing a gauge-null direction), giving a 4D color subspace from 2 qubits,
  and the full 8D space = (color-2-qubit) ⊗ (isospin-1-qubit) + residual.

**Assessment (G1)**: The three-qubit language is a useful mnemonic for the three
independent algebraic grading structures of ℬ (quaternion grading × complex grading × 
charge-conjugation grading), but should not be taken as an exact identification with 
a tensor product of spin-1/2 systems unless the algebra isomorphism is fully stated.

**Proof status of dim_ℂ(ℋ_3q) = 8**: DERIVED (standard quantum information theory).  
**Proof status of dim_ℂ(ℋ_3q) = dim_ℝ(ℬ)**: DERIVED (dimension counting).  
**Proof status of structural correspondence**: CONJECTURAL.

### 1.4 Color-Triplet Decomposition of ℋ_3q

The 8-dimensional space ℋ_3q decomposes under color symmetry into sectors:

| Sector | States | Dimension | Physical role |
|--------|--------|-----------|---------------|
| Color singlet | (1/√3)(|100⟩ + |010⟩ + |001⟩) | 1 | Color-neutral |
| Color triplet | |r⟩, |g⟩, |b⟩ (one-hot) | 3 | Quark color charges |
| Complementary | |000⟩, |011⟩, |101⟩, |110⟩, |111⟩ minus singlet | 4 | Mixed |

The one-hot color triplet {|100⟩, |010⟩, |001⟩} generates the 3-dimensional color
sector of the SM. The remaining 5 states carry isospin and baryon structure.

In the biquaternion language:  
- Color sector ↔ Im(ℍ) = span{I, J, K}, dim_ℝ = 3  
- Complex structure ↔ ℂ acting on ℍ, contributing iI, iJ, iK, dim_ℝ = 3 additional  
- Scalar sector ↔ {1, i}, dim_ℝ = 2 (gauge-neutral)

This matches: 3 (colored) + 3 (complex-colored) + 2 (neutral) = 8 = dim_ℝ(ℬ).

### 1.5 Is the Relevant Dimension Complex 8 or Real 16?

The three-qubit Hilbert space ℋ_3q = ℂ^8 has:
- Complex dimension: **8** (this is the "information dimension")
- Real dimension: **16** (this is the full state space over ℝ)

The biquaternion algebra ℬ has:
- Complex dimension: **4** (as a ℂ-algebra)
- Real dimension: **8** (as an ℝ-algebra)

**Which is the relevant "8"?**

The relevant identification is: **dim_ℝ(ℬ) = 8 = dim_ℂ(ℋ_3q)**.

This identifies the 8 **real** information degrees of freedom of ℬ with the 8 **complex**
basis states of ℋ_3q. This is a semi-structural identification: it works as a count
of independent classical (amplitude) degrees of freedom before complexification.

The mode counting that yields N_eff uses dim_ℝ(Im ℍ) = 3 (not dim_ℂ(ℋ_3q) = 8 directly),
then multiplied by helicity × charge = 4, giving N_eff = 12. The bridge from the 8D
information sector to N_eff = 12 goes through the chronofactor projection (Section 2).

---

## 2. Workstream G2 Overview: Chronofactor and the 8D → 12 Transition

**[Full construction in `canonical/alpha/chronofactor_projection.md`]**

### 2.1 The Key Transition

The transition from the 8-dimensional information sector dim_ℝ(ℬ) = 8 to N_eff = 12
proceeds as follows:

```
dim_ℝ(ℬ) = 8
    |
    | Select charged sector: Im ℍ subspace
    | (gauge-active phase directions)
    |
dim_ℝ(Im ℍ) = 3
    |
    | Helicity doubling from complex structure of ℬ
    | N_helicity = 2
    |
    | Charge-conjugation doubling
    | N_charge = 2
    |
N_eff = 3 × 2 × 2 = 12
```

The "chronofactor" accounts for the helicity × charge projection: it contributes
exactly 4 effective degrees of freedom (the 2×2 = 4 factor), transforming the
3-dimensional Im ℍ information sector into the 12 effective charged modes.

### 2.2 Why N_eff ≠ 8

The 8D sector is the total mode count before projection. Not all 8 dimensions
contribute to the one-loop vacuum polarization:
- The 2 gauge-neutral dimensions {1, i} do not couple to the U(1)_EM photon.
- The 3 complex-quaternion dimensions {iI, iJ, iK} do contribute but double the
  Im ℍ count (giving the complex structure factor in the vacuum polarization loop).

After projection: 3 real + 3 complex = 6 charged degrees, × 2 (charge conjugation) = 12.

Alternatively: N_eff = 8 + 4 where 8 = dim_ℝ(ℬ) and 4 = chronofactor modes. But
this decomposition is CONJECTURAL (it requires specifying what the 4 "extra" modes are).
The established decomposition is N_eff = 3 × 2 × 2 = 12 [L0].

---

## 3. Workstream G4: E8 / Sphere-Packing Information-Density Analogy

### 3.1 The E8 Lattice in 8 Dimensions

The E8 lattice is the unique (up to isometry) densest sphere packing in ℝ^8,
proved by Viazovska (2016). Key facts:

| Property | Value |
|----------|-------|
| Dimension | 8 |
| Packing density | π⁴/384 ≈ 0.2537 |
| Kissing number | 240 |
| E8 root system | 240 roots |
| E8 rank | 8 |
| E8 generators (Weyl group) | related to |W(E8)| = 696,729,600 |

The 8 dimensions of E8 match dim_ℝ(ℬ) = 8 = dim_ℂ(ℋ_3q).

### 3.2 Is E8 Algebraically Present in ℬ?

**Assessment**: The biquaternion algebra ℬ = ℂ⊗ℍ ≅ M₂(ℂ) does **not** naturally carry
an E8 lattice or root system. The reasons are:

1. **ℬ is an associative algebra over ℂ**; E8 is an exceptional Lie algebra over ℝ.
   The automorphism group of M₂(ℂ) is PGL(2,ℂ), not related to E8.

2. **The integer lattice of ℬ** (biquaternions with integer coefficients) is related
   to the Hurwitz quaternions, whose root system is D4 (dimension 4), not E8.

3. **E8 appears naturally in** the product ℍ × ℍ (two copies of quaternions over ℤ,
   i.e., the icosian ring), which is an 8-dimensional real space. But ℬ = ℂ⊗ℍ
   is a *different* 8-dimensional space.

4. **No E8 root system has been constructed** within the UBT algebraic framework.

**Status of E8 claim**: The numerical coincidence dim(E8) = dim_ℝ(ℬ) = 8 is noted
but does not constitute a structural connection. The E8 lattice is **not** present
in the canonical UBT algebra.

### 3.3 Sphere-Packing Density as Normalization Factor

**Proposed mechanism**: The Viazovska result that E8 achieves optimal sphere packing
density ρ = π⁴/384 in 8D might provide a non-arbitrary normalization for the
mode-counting effective coupling.

**Assessment**: This requires:
1. Identifying the "spheres" being packed (mode volumes? coherent state areas?)
2. Showing that the packing density factor appears in the one-loop integral
3. Computing whether π⁴/384 ≈ 0.2537 actually enters B_base or N_eff

None of these steps has been completed. The packing density π⁴/384 does not appear
in any current UBT formula for N_eff or B_base.

**Status**: FALSE_LEAD in current state. The E8 connection would require either:
- Constructing an E8 root system from ℬ (no natural construction exists), or
- Proving that mode densities in the 8D information sector are maximized by E8 packing
  (requires a specific inner product on the mode space that has not been defined).

### 3.4 Viazovska/Modular Methods Relevance

The proof of E8 optimality uses modular forms (Viazovska 2016, 2022). The same
modular forms (Jacobi theta functions) appear in UBT's partition function:
```
Ẑ(τ) = ϑ₃(τ)³
```

However, the use of modular forms in the Viazovska proof is technical (they construct
a magic function for the sphere-packing bound), not an intrinsic E8 structure. The
appearance of ϑ₃ in both places is a coincidence of the mathematical toolkit, not
evidence that E8 geometry governs UBT mode counting.

**Status**: ANALOGY only. No theorem connecting E8 packing and UBT mode counts.

---

## 4. Summary Table

| Component | Proposed Origin | Mathematical Definition | Proof Status | Role in α Route |
|-----------|----------------|------------------------|--------------|-----------------|
| three_qubits | Three binary grading structures of ℬ: quaternion / complex / charge-conjugation | ℋ_3q = (ℂ²)^{⊗3}, dim_ℂ = 8 | CONJECTURAL (structural analog, not algebra iso) | Motivates 8D sector as information substrate |
| 8D_information_sector | dim_ℝ(ℬ) = dim_ℂ(ℋ_3q) = 8 | ℬ as real vector space = ℝ^8 | DERIVED (dimension counting) | Supplies 3 charged + 3 complex-charged + 2 neutral directions |
| chronofactor | Imaginary-time compactification S¹_ψ with helicity and charge doubling | 4 = N_helicity × N_charge = 2 × 2 | DERIVED (complex structure of ℬ) | Converts 3 Im ℍ directions into 12 effective modes |
| N_eff_12 | N_phases × N_helicity × N_charge = 3×2×2 from ℬ algebra | N_eff = dim_ℝ(Im ℍ) × 2 × 2 = 12 | DERIVED [L0] (five independent routes) | Enters B₀ = 2πN_eff/3 and B_base = N_eff^{3/2} |
| exponent_3_over_2 | d/2 for d=3=dim_ℝ(Im ℍ); heat-kernel; modular weight of ϑ₃³ | B_base ∝ N_eff^{3/2} | CONJECTURAL [MC→near L0] — three converging mechanisms | Sets B_base ≈ 41.57 → n* near 137 |
| sphere_packing_density | No algebraic construction in ℬ | E8 density π⁴/384 (not present in UBT) | FALSE_LEAD in current state | Not currently in α route |
| projection_factor | Im ℍ → ℂ_τ projection: 3→2 dimensional reduction | Jacobian = dim_ℝ(Im ℍ)/dim_ℝ(ℂ_τ) = 3/2 | CONJECTURAL (geometric motivation without rigorous map) | Candidate source of 3/2 exponent |
| V_eff_alpha_link | n* = α⁻¹_bare from Dirac quantization on S¹_ψ | V_eff(n) = n² − B·n·ln n; min at n* | CONDITIONAL [L1] given B_base | Translates winding spectrum minimum into α⁻¹ |

---

## 5. What This Document Does and Does Not Claim

**Does claim**:
- dim_ℝ(ℬ) = 8 is an exact algebraic fact [L0].
- dim_ℂ(ℋ_3q) = 8 is an exact quantum-information fact [L0].
- The numerical equality is non-trivial and motivates the three-qubit interpretation.
- The dominant color sector (one-hot triplet) maps naturally to Im ℍ.
- N_eff = 12 is derived [L0] from ℬ without using any three-qubit language.

**Does not claim**:
- ℋ_3q ≅ ℬ as algebras (they are not isomorphic as algebras over ℂ).
- E8 lattice structure is present in ℬ.
- Sphere-packing density enters B_base or N_eff.
- The three-qubit picture provides an independent derivation of N_eff = 12.

---

## 6. References

- `canonical/fields/biquaternion_algebra.tex` — ℬ = ℂ⊗ℍ definition
- `canonical/interactions/su3_qubit_encoding.tex` — color/qubit encoding
- `canonical/n_eff/step1_mode_decomposition.tex` — N_eff derivation chain
- `canonical/alpha/chronofactor_projection.md` — chronofactor detailed construction
- `ALPHA_STRUCTURAL_ORIGINS.md` — executive summary of all α tracks
- `reports/neff_12_dimension_count_audit.md` — full N_eff = 12 audit
- `reports/e8_sphere_packing_relevance.md` — E8 detailed analysis
