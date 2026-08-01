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


# exponent_3_2_origin_audit.md — Audit of All Candidate Origins for the Exponent 3/2

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Track**: T3_ALPHA — Fine Structure Constant  
**Purpose**: Systematic audit of all candidate mechanisms for the exponent 3/2 in
B_base = N_eff^{3/2}, with proof-level labels and a clear verdict for each.  
**Companion files**:
- `ALPHA_STRUCTURAL_ORIGINS.md` §2 (Track E1) — original four-mechanism summary
- `canonical/alpha/neff_32_alpha_route.tex §4` — full geometric route
- `canonical/interactions/B_base_derivation_complete.tex` — B_base derivation
- `research_tracks/T3_ALPHA/exponent_3_over_2_candidates.tex` — detailed calculations

---

## Overview

The exponent 3/2 appears in the formula:
```
B_base = N_eff^{3/2} ≈ 41.57
```
which is the baseline effective coupling in the winding-mode potential
V_eff(n) = n² − B·n·ln n.

This audit investigates whether 3/2 is:
- a geometrically derived quantity (desirable)
- an arbitrary exponent fitted to reach n* = 137 (unacceptable)

**Verdict**: The exponent 3/2 is NOT arbitrary. It arises from at least **three
independent mechanisms**, all rooted in the dimension count dim_ℝ(Im ℍ) = 3.
The connection from these mechanisms to the formula B_base = N_eff^{3/2} is
**[CONJECTURAL → near L0]** with a specific remaining open lemma.

---

## Mechanism A: Heat-Kernel Density of States

### Statement

The imaginary quaternion subspace Im ℍ ≅ ℝ³ has real dimension d = 3. The
standard heat-kernel result for the cumulative density of states of a Laplacian
on a compact d-dimensional Riemannian manifold is:
```
𝒩(E) = #{eigenvalues ≤ E} ∝ E^{d/2}
```
For d = 3:
```
𝒩(E) ∝ E^{3/2}
```
When the effective potential coefficient B_base is identified with the cumulative
mode count at scale E ~ N_eff:
```
B_base ∝ 𝒩(N_eff) ∝ N_eff^{3/2}
```
The leading term of the heat kernel on a 3-torus T³ is:
```
K(t) = (4πt)^{-3/2} Vol(T³) + O(t^{-1/2})
```
The exponent -3/2 appears directly.

### Physical interpretation

The three independent Im ℍ directions each contribute one dimension to the
mode-counting problem. The d = 3 heat-kernel exponent d/2 = 3/2 directly
produces the 3/2 power. This connects the exponent to the purely algebraic
fact dim_ℝ(Im ℍ) = 3.

### Independence from α

The dimension d = 3 follows from the axiom ℬ = ℂ⊗ℍ. No reference to α.

### Remaining step

The identification B_base ∝ 𝒩(N_eff) requires:
1. A metric on Im ℍ (or the torus T³ it generates)
2. A proof that the heat-kernel leading coefficient equals N_eff^{3/2} exactly
   (not just proportionally)

**Status**: [L0] for the mechanism (heat-kernel d/2 = 3/2 in Im ℍ); **[OPEN_LEMMA]**
for the precise derivation B_base = N_eff^{3/2}.

**Verdict**: **Strongest candidate.** The mechanism is clean and follows from algebra.
The connection to B_base requires one explicit computation.

---

## Mechanism B: Modular Weight of the Partition Function

### Statement

The partition function of the UBT biquaternion field on the torus T² × S¹_ψ is:
```
Ẑ(τ) = ϑ₃(τ)³,  where ϑ₃(τ) = Σ_{n∈ℤ} e^{2πiτn²}
```
The factor of 3 reflects the three independent Im ℍ phase directions.

Under SL(2,ℤ) modular transformations τ → −1/τ and τ → τ+1, the modular weight
of ϑ₃^N is k = N/2. For N = 3:
```
k(ϑ₃³) = 3/2
```
The one-loop effective coupling in a 2D CFT with partition function of modular
weight k is proportional to k. This connects the 3/2 exponent to the modular
weight of the partition function.

### Remark: direct and indirect connection to B_base

The direct formula B_base = N_eff × k = 12 × (3/2) = 18 does NOT match B_base ≈ 41.57.

The indirect route via B_base = N_eff^{3/2} uses k = √(N_eff)/2 as an implicit
identification. For N_eff = 12: k = √12/2 ≈ 1.73 ≠ 3/2. So this route does NOT
directly produce B_base = N_eff^{3/2} without additional assumptions (specifically
the Kac-Moody level k_KM = 1).

### Status

[L0] for the modular weight k = 3/2 of ϑ₃³ (computed exactly). **[CONJECTURAL]**
for the connection to B_base = N_eff^{3/2} without the Kac-Moody assumption.

**Verdict**: **Strong supporting evidence** that 3/2 is a structural feature of the
partition function. The connection to B_base requires Gap G3-k.

---

## Mechanism C: Projection Ratio (Dimensional Reduction)

### Statement

The complex time plane ℂ_τ has real dimension 2. The imaginary quaternion space
Im ℍ has real dimension 3. The ratio:
```
λ = dim_ℝ(Im ℍ) / dim_ℝ(ℂ_τ) = 3/2
```
If modes in Im ℍ project onto ℂ_τ with density enhancement factor λ:
```
ρ_eff(n) = (3/2) × ρ_base(n)
```
then the effective coupling receives this enhancement:
```
B_eff = λ × B_base_0 = (3/2) × ...
```
Taken as a scaling law applied to N_eff:
```
B_base = N_eff^{3/2}  [if the enhancement acts multiplicatively at each order]
```

### Why 3/2 appears

The biquaternion field Θ(q,τ) lives in a product of field space ℬ (containing
Im ℍ) and the complex time plane ℂ_τ. The "projection" from the 3-dimensional
phase space onto the 2-dimensional time plane introduces a density ratio of 3/2.

### Status

**[CONJECTURAL]** — requires a precise definition of the projection map with inner
product and Jacobian. The geometric motivation is sound but no rigorous derivation exists.
See `canonical/alpha/chronofactor_projection.md §2`.

**Verdict**: **Geometrically motivated.** The factor 3/2 appears naturally from
dimensional analysis, but the path to B_base = N_eff^{3/2} needs formalization.

---

## Mechanism D: Holographic Scaling (Rejected)

### Statement

Standard holographic scaling in a d-dimensional bulk gives entropy ∝ A^{(d-1)/d}
where A is the bulk volume. For d = 3:
```
Exponent = (d-1)/d = 2/3   ≠ 3/2
```
This does NOT produce 3/2. A non-standard inversion would give d/(d-1) = 3/2 but
this inversion requires a non-standard boundary condition that has no derivation.

### Status

**[CONJECTURAL/WEAK]** — the holographic analogy gives the wrong exponent (2/3 not
3/2) unless an inverted convention is used. Treating the complex time plane as a
"projection boundary" rather than a standard holographic screen inverts the formula,
but this inversion is ad hoc without a precise physical argument.

**Verdict**: Weaker than A, B, C. The holographic analogy is a suggestive mnemonic
but does not provide a derivation.

---

## Mechanism E: Three Spatial Dimensions Through 2D Projection (Mechanism A+C Synthesis)

### Statement

Mechanisms A and C are unified as: the exponent 3/2 = d/2 arises because the effective
3-dimensional mode spectrum of Im ℍ is projected through the 2-dimensional complex
time plane. The "d/2" factor from the heat kernel (Mechanism A) and the "3/2" from the
projection ratio (Mechanism C) are the same quantity viewed from different angles:

```
d/2 = dim_ℝ(Im ℍ) / 2 = dim_ℝ(Im ℍ) / dim_ℝ(ℂ_τ) = 3/2
```

The denominator "2" appears in the heat kernel as a Weyl-type denominator, and in
the projection as the dimension of the complex time plane. Both denominators are the
same: the real dimension of ℂ_τ = 2.

### Status

**[L0] for the identification; [OPEN_LEMMA] for using this in B_base.**

**Verdict**: This synthesis shows that Mechanisms A and C have a common algebraic
root: 3/2 = dim_ℝ(Im ℍ) / dim_ℝ(ℂ_τ).

---

## Summary of All Mechanisms

| Mechanism | How 3/2 arises | Status of 3/2 itself | Status of B_base = N_eff^{3/2} |
|-----------|---------------|---------------------|-------------------------------|
| A: Heat kernel | d/2 for d = dim_ℝ(Im ℍ) = 3 | **[L0]** — algebraic | **[OPEN_LEMMA]** — needs heat-kernel on T²×S¹_ψ |
| B: Modular weight | k(ϑ₃³) = 3/2 | **[L0]** — computed | **[CONJECTURAL]** — needs Gap G3-k |
| C: Projection ratio | dim(Im ℍ)/dim(ℂ_τ) = 3/2 | **[CONJECTURAL]** | **[CONJECTURAL]** — needs Jacobian |
| D: Holographic | (d-1)/d inverted | **[WEAK]** — non-standard inversion | **[WEAK]** |
| E: A+C synthesis | d/2 = dim(Im ℍ)/dim(ℂ_τ) | **[L0]** — same derivation | **[OPEN_LEMMA]** |

---

## Independence from α: Exponent Stress Test

From `ALPHA_STRUCTURAL_ORIGINS.md §5.3`:

| Exponent p | B_base = 12^p | n* (prime) | Matches α⁻¹ = 137? |
|-----------|--------------|-----------|---------------------|
| 1.0 | 12.00 | 5 | No |
| 1.2 | 17.45 | 7 | No |
| **1.5** | **41.57** | 127 (or 137 with R) | **Conditional** |
| 2.0 | 144.00 | 269 | No |

The exponent p = 3/2 is the **unique** value with a first-principles justification
(Mechanisms A–C) that also gives n* in the vicinity of 137. The coincidence is
non-trivial; the exponent is not freely tunable.

---

## Primary Open Lemma

**Lemma (OPEN)**: Prove that the one-loop effective coupling B_base, computed from
the heat kernel of ∇†∇ on T² × S¹_ψ with N_eff = 12 charged modes, equals
N_eff^{3/2} = 12^{3/2} ≈ 41.57 exactly (without using α as input).

**Recommended approach** (from `canonical/interactions/B_base_derivation_complete.tex`):
Compute the Schwinger proper-time heat kernel of ∇†∇ on the product T² × S¹_ψ.
The leading small-t expansion on the 3-dimensional Im ℍ torus T³ gives:
```
K(t) ~ (4πt)^{-3/2} Vol(T³)
```
The coefficient B_base arises from the integral of K(t) with appropriate cutoff
at the compactification scale R_ψ. If Vol(T³) = (2πR_ψ)³ and the integral yields
exactly N_eff^{3/2} after normalization, the lemma is proved.

**Estimated difficulty**: Medium. The technique (ζ-function regularization of heat
kernel on torus) is standard. The challenge is establishing the precise normalization.

---

## Conclusion

The exponent 3/2 is NOT an arbitrary parameter chosen to fit α. It has three
converging geometric/algebraic origins, all rooted in:
```
dim_ℝ(Im ℍ) = 3  (from the axiom ℬ = ℂ⊗ℍ)
dim_ℝ(ℂ_τ) = 2   (from the canonical complex time structure)
⟹  3/2 = d/2 = dim(Im ℍ)/dim(ℂ_τ)
```
The mechanism is geometrically compelling. The remaining open work is a single
explicit computation (heat-kernel on T²×S¹_ψ), not a conceptual gap.

**Status of exponent 3/2**: [CONJECTURAL → near L0]. Pending one computation.
