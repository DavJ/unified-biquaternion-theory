<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# E8-Torus Information Geometry and Chronofactor Projection in UBT

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Status**: SPECULATIVE RESEARCH FRONT — not canonical theory, not derived  
**Track**: research_fronts/e8_torus_quantized_information  
**Related files**:
- `research_tracks/triqubit_su3_geometry.md` — three-qubit Hilbert-space geometry
- `ALPHA_STRUCTURAL_ORIGINS.md` — N_eff = 12 and exponent 3/2 background
- `research_tracks/T3_ALPHA/neff12_derivations.tex` — five independent N_eff routes
- `research_tracks/T3_ALPHA/exponent_3_over_2_candidates.tex` — exponent origins
- `canonical/algebra/` — biquaternion algebraic structure
- `claims_status.md` — labeled claim registry for this research front

---

## Abstract

The three-qubit Hilbert space H₃q = (ℂ²)^⊗3 has complex dimension 8 and real
amplitude dimension 16. This note investigates whether a toroidal quotient of a
real 8-dimensional information subspace by an E8 lattice — the densest known
sphere packing in ℝ⁸ — provides a geometrically natural information structure
within UBT. The central questions are:

1. Can the 8-dimensional basis of H₃q be associated with a real 8-dimensional
   coordinate space admitting an E8-type lattice structure?
2. Does a chronofactor projection Π: T⁸_E8 → C_chrono extract observed quantum
   dynamics from this 8D torus?
3. Do the gaps between packed spheres in the E8 packing correspond to latent,
   hidden, or transition sectors?
4. Does this structure offer a geometric origin for N_eff and the 3/2 exponent
   appearing in the UBT alpha route?

All four questions remain open. This document formulates them precisely, defines
all required mathematical objects, identifies the construction gaps that must be
closed before any claim can be made canonical, and proposes the next concrete
calculations.

**This paper is a research proposal / theoretical front. No claim in it is
derived. All conjectures are explicitly labeled.**

---

## 1. Motivation

### 1.1 Why Eight Dimensions Appear

The three-qubit Hilbert space arises naturally in UBT through two independent
routes already present in the repository:

- The biquaternion algebra ℂ⊗ℍ has complex dimension 8 (real dimension 16), so a
  single biquaternion field value at a point is an element of a space with
  dim_ℝ = 16 and dim_ℂ = 8.
- The triqubit picture (`research_tracks/triqubit_su3_geometry.md`) gives a
  3-qubit Hilbert space with 8 basis states.

Both routes produce the integer 8 as a natural count. This double occurrence
invites the question: is there a deeper 8-dimensional information structure in
UBT that both are reflecting?

### 1.2 Why E8

The E8 lattice is the unique densest lattice sphere packing in ℝ⁸ (proved by
Viazovska 2016). Among all discrete translation-invariant structures in ℝ⁸, E8
maximises the fraction of volume covered by non-overlapping spheres. If nature
prefers information-dense structures, E8 is the canonical candidate for an
8-dimensional information lattice.

Key properties motivating the choice:

| Property | Value | Significance |
|----------|-------|-------------|
| Dimension | 8 | Matches dim_ℂ(H₃q) and dim_ℂ(ℂ⊗ℍ) |
| Kissing number | 240 | Contacts per sphere; related to root system |
| Packing density | π⁴/384 ≈ 0.2537 | Proved optimal by Viazovska |
| Center density | 1/16 | Normalised contact density |
| Theta series | ∑_{λ∈E8} q^{|λ|²/2} = 1 + 240q + 2160q² + ... | Modular form of weight 4 |
| Automorphism group | Weyl(E8), order 696 729 600 | Symmetry of the lattice |

The theta series of E8 is a weight-4 modular form, directly related to the
Eisenstein series E₄(τ). This connects E8 to modular methods already present
in UBT's theta-route to alpha.

### 1.3 Connection to Existing Alpha Routes

The UBT alpha derivation (see `ALPHA_STRUCTURAL_ORIGINS.md`) uses:

```
B_base = N_eff^{3/2},   N_eff = 12
```

N_eff = 12 arises from the sum of the real dimensions of the complex-time plane
(dim_ℝ ℂ = 2), the imaginary quaternion subspace (dim_ℝ Im ℍ = 3), and the
biquaternion complement (contributing 7, totalling 12 from a specific mode
counting). The exponent 3/2 = dim_ℝ(Im ℍ) / dim_ℝ(ℂ).

The E8 research front proposes a possible alternative geometric origin:
- N_eff may have an 8-dimensional counterpart through the E8 theta series
  coefficients or the kissing number decomposition.
- The exponent 3/2 may arise from projecting the 8D torus onto a 2D or 3D
  chronofactor sector.

Both suggestions are **conjectural** and require explicit calculation before
any claim of derivation.

---

## 2. Relation to Existing UBT Alpha and Theta Routes

### 2.1 Theta Route Summary

The UBT partition function on the imaginary quaternion sector is:

```
Ẑ(τ) = ϑ₃(τ)³
```

where ϑ₃ is the Jacobi theta function. The modular weight k = 3/2 of ϑ₃³
provides the exponent 3/2 via the heat-kernel density of states (Track E1,
`ALPHA_STRUCTURAL_ORIGINS.md §2.2`).

### 2.2 E8 Theta Series

The E8 theta series is:

```
Θ_{E8}(τ) = ∑_{λ ∈ E8} q^{|λ|²/2},   q = e^{2πiτ}
```

This equals the weight-4 Eisenstein series:

```
Θ_{E8}(τ) = E₄(τ) = 1 + 240 ∑_{n=1}^∞ σ₃(n) q^n
```

where σ₃(n) = ∑_{d|n} d³. The leading coefficient 240 is the kissing number
of E8.

**Comparison with UBT theta function**:

| Object | Formula | Weight | Role in UBT |
|--------|---------|--------|-------------|
| ϑ₃(τ)³ | Σ q^{n₁²+n₂²+n₃²} | k = 3/2 | Partition function on Im ℍ |
| Θ_{E8}(τ) | E₄(τ) | k = 4 | Candidate 8D partition function |

The two functions have different modular weights and count different things.
The relationship between ϑ₃³ and Θ_{E8} is a concrete open mathematical
question (see §12, question Q1).

### 2.3 What Must Not Be Claimed

- **Do not** claim that Θ_{E8} replaces ϑ₃³ in the UBT partition function.
- **Do not** claim that the modular weight 4 of E₄ gives the exponent 3/2.
- **Do not** claim that E8 geometry directly yields α without an explicit
  construction of the projection and mode-counting mechanism.

---

## 3. Three-Qubit Hilbert Space and the 8-Dimensional Information Sector

### 3.1 Definition

**Definition 3.1 (Three-qubit Hilbert space)**.
```
H₃q = (ℂ²)^⊗3 = ℂ² ⊗ ℂ² ⊗ ℂ²
```

with standard computational basis:

```
{|q₁q₂q₃⟩ : q_i ∈ {0,1}} = {|000⟩, |001⟩, |010⟩, |011⟩, |100⟩, |101⟩, |110⟩, |111⟩}
```

**Dimensions**:
```
dim_ℂ(H₃q) = 8
dim_ℝ(H₃q) = 16   (treating ℂ as ℝ²)
```

**Status**: ✅ DERIVED — standard definition.

### 3.2 Physical State Space

A pure state is a ray in H₃q. Normalised representatives form S¹⁵ ⊂ ℝ¹⁶.
The projective state space is:

```
CP⁷ = S¹⁵ / U(1)    (dim_ℝ = 14)
```

**Status**: ✅ DERIVED — standard Hilbert-space geometry.

### 3.3 Relation to Biquaternion Algebra

The biquaternion algebra ℂ⊗ℍ has a basis {1, i, j, k, e, ei, ej, ek} over ℝ
with dim_ℝ(ℂ⊗ℍ) = 8 and dim_ℂ(ℂ⊗ℍ) = 4 (over ℂ, using complex coefficients).
As a real vector space, ℂ⊗ℍ ≅ ℝ⁸.

**Important distinction**: The 8 real dimensions of ℂ⊗ℍ and the 8 complex
dimensions of H₃q are different spaces. They share the number 8 but are not
canonically identified without further structure.

**Status**: 🔶 CONJECTURAL that a canonical identification exists. The
coincidence of dimension 8 is the observation motivating this research front;
it is not itself a derivation.

---

## 4. Torus Construction: T⁸ = ℝ⁸ / Λ

### 4.1 General Torus

Given a full-rank lattice Λ ⊂ ℝ⁸ (a discrete subgroup with ℝ⁸/Λ compact),
the quotient

```
T⁸_Λ = ℝ⁸ / Λ
```

is a flat 8-dimensional torus. It is a compact Riemannian manifold with:
- Fundamental domain = the Voronoi cell of Λ
- Volume = |det(B)| where B is the Gram matrix of Λ
- Geodesics = images of straight lines in ℝ⁸

**Status**: ✅ DERIVED — standard differential geometry.

### 4.2 Flat Torus from Coordinate Space

To use this construction for H₃q, one must choose a real coordinate space
associated to the Hilbert space. Two natural candidates exist:

**Option A (Amplitude space)**:
```
ℝ¹⁶ ≅ ℂ⁸ = H₃q
Lattice Λ ⊂ ℝ¹⁶   (16-dimensional lattice, not E8)
```

**Option B (Real 8D slice)**:
Choose a real 8-dimensional subspace V ⊂ H₃q spanned by the 8 computational
basis states (taking real coefficients). Then:

```
V = span_ℝ{|000⟩, ..., |111⟩} ≅ ℝ⁸
Lattice Λ ⊂ V ≅ ℝ⁸   (8-dimensional lattice, candidate for E8)
```

Option B is the natural setting for the E8 construction. It requires a
projection from the full complex Hilbert space to the real basis subspace.

**Status**: ✅ DERIVED that T⁸ = ℝ⁸/Λ is a valid torus for any Λ.
🔶 CONJECTURAL that Option B defines the physically relevant subspace.

---

## 5. Candidate E8 Lattice Choice: Λ = E8

### 5.1 E8 Lattice Definition

The E8 lattice is the unique (up to scaling and rotation) even self-dual lattice
in ℝ⁸. It may be defined as:

```
E8 = {x ∈ ℝ⁸ : all x_i ∈ ℤ or all x_i ∈ ℤ + 1/2, and Σ x_i ≡ 0 mod 2}
```

Key algebraic properties:
```
|E8| = ∞ (it is a lattice, not finite)
Minimum norm: |λ|² = 2 for all non-zero λ ∈ E8
Kissing number: 240 (vectors of norm √2)
Self-dual: E8* = E8
Even: all norms are even integers
```

### 5.2 The E8 Torus

With Λ = E8:

```
T⁸_{E8} = ℝ⁸ / E8
```

Properties:
- Volume of fundamental domain: Vol = √|det(Gram)| = 1 (since E8 is
  self-dual with determinant 1)
- The Voronoi cell is the Gosset polytope 4₂₁
- Spectrum of the Laplacian: eigenvalues are |λ|² for λ ∈ E8* = E8

**Status**: ✅ DERIVED that T⁸_{E8} = ℝ⁸/E8 is a well-defined flat torus.
🔶 CONJECTURAL that this torus is the correct UBT information geometry.

### 5.3 Why E8 and Not Other Lattices

Competing candidates in ℝ⁸:

| Lattice | Kissing number | Packing density | Self-dual |
|---------|---------------|-----------------|-----------|
| E8 | 240 | π⁴/384 (optimal) | Yes |
| D8 | 112 | lower | No |
| ℤ⁸ | 16 | π⁴/384... lower | No |
| Barnes-Wall BW16 | — | — | No (16D) |

E8 is the unique optimal choice in ℝ⁸. If UBT's information geometry optimises
for packing (information density per unit "volume"), E8 is the canonical
candidate. This is a **motivation**, not a derivation.

---

## 6. Difference Between ℂ⁸, ℝ¹⁶, ℂP⁷, and the Real E8 Slice

This section is critical for avoiding conflation errors.

### 6.1 The Chain of Spaces

```
H₃q = ℂ⁸    (complex Hilbert space, dim_ℂ = 8, dim_ℝ = 16)
      |
      | treat ℂ as ℝ²
      ↓
    ℝ¹⁶     (real amplitude space, unreduced)
      |
      | normalize (||ψ|| = 1)
      ↓
    S¹⁵ ⊂ ℝ¹⁶   (unit sphere)
      |
      | quotient by U(1) phase
      ↓
    ℂP⁷     (projective pure state space, dim_ℝ = 14)
```

**Separately**, choosing real coordinates only (all complex amplitudes real):

```
V = {ψ ∈ H₃q : all amplitudes ∈ ℝ} ≅ ℝ⁸    (real 8D subspace)
    |
    | impose E8 lattice structure on ℝ⁸
    ↓
T⁸_{E8} = ℝ⁸/E8   (E8 torus, candidate information space)
```

### 6.2 Key Distinctions

| Space | Dimension | Type | Relation to E8 |
|-------|-----------|------|----------------|
| H₃q = ℂ⁸ | 8 complex = 16 real | Complex Hilbert | None directly |
| ℝ¹⁶ | 16 real | Real amplitude | Too large for E8 |
| S¹⁵ | 15 real | Sphere | None directly |
| ℂP⁷ | 14 real | Complex projective | None directly |
| V = ℝ⁸ | 8 real | Real slice | ✓ Correct domain for E8 |
| T⁸_{E8} | 8 real | Flat torus | ✓ E8 lives here |

**Warning**: CP⁷ is not a flat torus and cannot be identified with T⁸_{E8}.
The E8 construction lives in the real 8D subspace V, not in the full complex
Hilbert space or its projectivisation.

---

## 7. Sphere Packing and Information-Density Interpretation

### 7.1 Sphere Packing

The E8 lattice packing assigns a sphere of radius r = 1/√2 (half the minimum
distance) to each lattice point. These spheres do not overlap. The kissing
number 240 means each sphere touches exactly 240 others.

Packing density:
```
Δ_{E8} = Vol(sphere in ℝ⁸) × (density of lattice points)
        = (π⁴/4! ) × (1/Vol(fundamental domain))
        = π⁴/384 ≈ 0.2537
```

This is the proved maximum for ℝ⁸ (Viazovska 2016).

### 7.2 Information-Density Interpretation

**Conjecture (not derived)**: Each lattice point of E8 represents a distinct
basis state of the 8-dimensional information sector. The sphere around each
lattice point represents the "neighborhood" of that state under small
perturbations. Optimal sphere packing then means:

- Maximum number of distinct states per unit volume of information space.
- Minimum overlap between neighboring states (maximum distinguishability).
- Optimal error-correcting structure: E8 achieves the minimum distance bound
  for codes in ℝ⁸.

This interpretation is consistent with the coding-theory view of E8 as a
self-dual code. The minimum distance √2 corresponds to the minimum Hamming-like
distance between distinct basis states.

**Status**: 🔶 CONJECTURAL — the identification of lattice points with basis
states requires a derivation of the lattice structure from UBT dynamics.

---

## 8. What Lives in the Gaps: Transitions, Syndromes, Latent Sectors, Hidden States

### 8.1 The Gap Structure of E8

The complement of the packed spheres in T⁸_{E8} has volume:
```
Vol(gaps) = Vol(T⁸_{E8}) - 240 × Vol(sphere)
           = 1 - 240 × π⁴/384 / 240 ... (per lattice point fraction)
```

More precisely, the unpacked fraction is 1 - Δ_{E8} ≈ 0.7463 of the torus
volume.

The Voronoi decomposition of T⁸_{E8} divides the torus into fundamental cells.
Points in the interior of a Voronoi cell are closest to exactly one lattice
point. Points on Voronoi boundaries are equidistant from two or more lattice
points.

### 8.2 Proposed Interpretation of Gap Types

The following classification is **speculative and unlabeled** in current UBT:

| Region | Geometry | Conjectured role |
|--------|----------|------------------|
| Lattice points | E8 nodes | Basis states (classical information) |
| Sphere interiors | Balls around nodes | Quantum fluctuations around basis |
| Sphere surfaces | ∂Ball | Transition states (coherent superpositions) |
| Voronoi cell interiors | Between spheres | Latent sector (undecided basis) |
| Voronoi cell boundaries | Equidistant faces | Syndrome states (degenerate) |
| Deep gaps (far from all nodes) | Voronoi vertices | Hidden sector candidates |

**Status**: ❓ OPEN — this classification is a hypothesis. No derivation exists
linking these geometric regions to physical states in UBT.

### 8.3 Connection to Error Correction

E8 is related to the Golay-type codes in the theory of lattices. The deep holes
of E8 (points maximally far from all lattice points, radius = √2 from the nearest
point) sit at the Voronoi vertices. There are 2160 such holes in the E8 Voronoi
cell. If these correspond to "syndrome states" in an error-correcting code
interpretation, then the gap structure has a precise combinatorial meaning.

**Status**: 🔶 CONJECTURAL — the 2160 deep holes of E8 may be meaningful for UBT,
but no derivation exists.

---

## 9. Chronofactor Projection

### 9.1 Definition Attempt

**Definition 9.1 (Chronofactor)**.
The chronofactor in UBT is the complex time coordinate τ = t + iψ, viewed as a
point in the complex time plane ℂ_τ. Periodic identification τ ~ τ + periods
defines a torus structure in the time sector.

In the UBT framework, the S¹_ψ circle (the imaginary time circle) is the
primary dynamical sector for winding modes. The chronofactor projection is a
map from the information space to the dynamical time sector.

**Proposed definition** (not yet derived):

```
Π: T⁸_{E8} → C_chrono
```

where C_chrono is a low-dimensional "chronofactor" space encoding observable
quantum dynamics.

### 9.2 Candidate Target Spaces

**Option A**: Two-torus

```
C_chrono = S¹_t × S¹_ψ = T²
```

This is a 2D torus in real time t and imaginary time ψ. The projection Π would
map the 8D information torus onto the 2D complex time torus.

**Option B**: Bloch sphere

```
C_chrono = S² ≅ ℂP¹   (single-qubit state space)
```

The Bloch sphere is the natural target for a single observable qubit degree of
freedom. The projection Π would identify the "observed" qubit with a specific
equator of T⁸_{E8}.

**Option C**: Product of Bloch spheres

```
C_chrono = S²_t × S²_ψ   (two Bloch spheres for real and imaginary time sectors)
```

### 9.3 Projection Mechanism (Conjectured)

A natural projection from T⁸_{E8} to T² would use the dual lattice and
integrate over 6 of the 8 torus directions:

```
Π: T⁸_{E8} → T²
   x = (x₁,...,x₈) ↦ (Σ aᵢxᵢ mod 1, Σ bᵢxᵢ mod 1)
```

for some coefficient vectors a, b ∈ E8* = E8. The image under such a linear
projection is a subtorus of T⁸_{E8} if a and b generate a primitive sublattice.

**Status**: 🔶 CONJECTURAL — the specific projection vectors (a, b) are not
determined by current UBT theory.

### 9.4 Role of Entanglement and Correlation Tensors

In the three-qubit picture, different 8D basis states carry different
entanglement structures (product states, Bell pairs, GHZ, W, etc.). The
chronofactor projection must be compatible with the entanglement structure.

Specifically: if Π maps entangled states to the same point of C_chrono, then
entanglement represents a "hidden" degree of freedom invisible to the
chronofactor dynamics. If instead Π distinguishes entanglement classes, then the
projected dynamics carries entanglement information.

The correlation tensor of a three-qubit state:
```
T_{ijk} = Tr(ρ σᵢ⊗σⱼ⊗σₖ),   i,j,k ∈ {0,1,2,3}
```

is a natural invariant that could label the fiber of the projection Π.

**Status**: ❓ OPEN — the compatibility of Π with entanglement structure is
not investigated.

---

## 10. Relation to Theta Functions and Viazovska-Style Magic Functions

### 10.1 E8 Theta Series as UBT Partition Function

The E8 theta series:
```
Θ_{E8}(τ) = E₄(τ) = 1 + 240q + 2160q² + 6720q³ + 17520q⁴ + ...
```

is a weight-4 modular form under SL₂(ℤ). The leading coefficient 240 = kissing
number of E8.

If T⁸_{E8} is the UBT information torus, its **Laplace spectrum** is given by
the lattice norms:
```
Spec(-Δ_{T⁸}) = {|λ|² : λ ∈ E8}   with multiplicity = #{λ : |λ|² = k}
```

The generating function of these multiplicities is Θ_{E8}(τ).

A UBT partition function counting states of the information torus would then be:
```
Z_{E8}(τ) = Θ_{E8}(τ) = E₄(τ)
```

This must be compared with the existing UBT partition function ϑ₃(τ)³ (weight
3/2) — they are *different* objects at *different* modular weights.

**Open question Q1**: Is there a map relating ϑ₃(τ)³ and E₄(τ)? Concretely:
does the E8 theta series factorize into products of ϑ functions in a way that
reproduces the UBT Im ℍ partition function?

One known identity:
```
E₄(τ) = ϑ₂(τ)⁸ + ϑ₃(τ)⁸ + ϑ₄(τ)⁸   (Jacobi identity generalisation)
```

This expresses E₄ in terms of eight-fold products of Jacobi theta functions.
The UBT uses ϑ₃³, which is a different combination.

### 10.2 Viazovska's Magic Function

Viazovska's proof of E8 optimality (2016) uses a "magic function" f: ℝ⁸ → ℝ
satisfying:
```
f(0) = f̂(0) = 1,   f(x) ≤ 0 for |x| ≥ √2,   f̂(ξ) ≥ 0 for all ξ
```

This function is constructed from quasi-modular forms (specifically, derivatives
of Eisenstein series). The construction is non-elementary but uses the same
modular form theory that appears in UBT's theta route.

**Possible connection**: If UBT's partition function satisfies analogous
positivity and zero conditions (as required for linear programming bounds on
packing), then the UBT dynamics might automatically select E8 geometry as the
optimal information structure. This is a speculative avenue for deriving rather
than assuming E8.

**Status**: ❓ OPEN — whether UBT's partition function satisfies the Viazovska
magic function conditions is not investigated.

---

## 11. Possible Relation to N_eff = 12 and Exponent 3/2

### 11.1 Current UBT Derivation

From `ALPHA_STRUCTURAL_ORIGINS.md`, N_eff = 12 arises from mode counting in
the UBT field decomposition (five independent routes, all yielding 12, status
Proved [L0]). The exponent 3/2 arises from:

- Heat-kernel density of states of Im ℍ ≅ ℝ³ (dim d = 3, exponent d/2 = 3/2)
- Modular weight of ϑ₃³ (weight k = 3/2)
- Ratio dim_ℝ(Im ℍ) / dim_ℝ(ℂ) = 3/2

### 11.2 E8 Route Candidates (All Conjectural)

**Candidate C1 (Dimensional projection)**:
The E8 torus T⁸_{E8} (dim = 8) projects to C_chrono (dim = 2) via Π, leaving
6 hidden dimensions. The ratio of projected to hidden dimensions:
```
8/2 = 4   or   8/6 = 4/3
```
Neither immediately gives 3/2. However, if C_chrono = ℝ³ (a 3-dimensional
chronofactor, e.g., Bloch sphere coordinates), then:
```
8/3 ≈ 2.67   (not 3/2)
projected/total = 3/8
```
Still not 3/2 directly.

**Candidate C2 (Root system)**:
The E8 root system has 240 roots. The ratio of independent Cartan directions
(rank = 8) to the dimension of a single qubit (dim = 2):
```
8/2 = 4,   rank/dim_qubit = 4   (not 3/2)
```

**Candidate C3 (Theta series weight)**:
The E8 theta series Θ_{E8} has modular weight k = 4. If the projection
reduces to the 3-qubit (= 3 Im ℍ directions) sector, the weight reduces by
the fiber dimension:
```
k_{projected} = k_{E8} − k_{fiber} = 4 − k_{fiber}
```
Requiring k_{projected} = 3/2 gives k_{fiber} = 5/2. This is an ad-hoc
condition without derivation.

**Candidate C4 (N_eff from E8)**:
The E8 lattice has 8 independent directions (rank 8). If each contributes
3/2 modes (from 3D thermal structure), the effective mode count is:
```
N_eff^{candidate} = 8 × (3/2) = 12
```

This is intriguing: N_eff = 12 = 8 × (3/2). Whether this factorization has
physical meaning, or is numerical coincidence, is an **open question**.

**Status**: ❓ OPEN — all four candidates are numerical observations without
derivation. Candidate C4 is the most suggestive and should be investigated
first.

---

## 12. Quantization Depth

### 12.1 Three Qubits = 8 Basis States ≠ 8-Bit Numerical Precision

The three-qubit system has **8 basis states** (|000⟩ through |111⟩). This is
a **state-space dimension**, not a bit-depth.

**8-bit numerical quantization** means representing a continuous variable with
256 = 2⁸ discrete levels. These are entirely different concepts:

| Concept | Description | Value for 3 qubits |
|---------|-------------|-------------------|
| Basis dimension | Number of orthogonal basis states | 8 |
| Phase resolution | Granularity of quantum phases | Continuous in ℂ |
| Bit depth (encoding) | Number of bits to index a basis state | 3 |
| Classical simulation depth | Bits to represent an amplitude | 64 (double), 128, etc. |

A three-qubit system **does not have 8-bit numerical precision**. It has 3 bits
of classical label space and 15 real parameters for the full state in ℂP⁷.

### 12.2 Quantization Mechanisms Available to UBT

If UBT's universe-simulator interpretation is taken seriously, the relevant
quantization is not bit-depth but geometric quantization of the information
torus. Several natural quantization mechanisms exist:

**Mechanism 1: Basis-dimension quantization**  
The Hilbert space has 8 basis states. Information is quantized to multiples of
one basis state. This is the standard quantum-mechanical discretization.

**Mechanism 2: Phase-grid quantization**  
Complex amplitudes take values in a discrete phase grid. For E8, the natural
phase grid is determined by the angles between E8 root vectors (multiples of
π/6, π/4, π/3 appear in the E8 root system).

**Mechanism 3: Error-correcting code quantization**  
The E8 lattice is the root lattice of an error-correcting code. States are
quantized to the nearest codeword. Errors smaller than the minimum distance
√2 are correctable.

**Mechanism 4: Action-bound quantization**  
The Bekenstein-Hawking bound limits the information per unit area. For the
E8 torus with unit volume, the Bekenstein bound gives a maximum entropy:
```
S_max ∝ A^{(n-1)/n}   (holographic scaling in n dimensions)
```
For n = 8: S_max ∝ A^{7/8}. Quantization then follows from discretizing
this entropy.

**Mechanism 5: Holographic boundary capacity**  
If T⁸_{E8} has a holographic dual on its 7-dimensional boundary ∂T⁸, the
boundary degrees of freedom determine the bulk quantization. The boundary
of the 8D torus is the 7-sphere S⁷, which has a known cohomology structure
related to the octonions.

**Status**: ❓ OPEN — UBT does not yet specify which quantization mechanism
is fundamental. This section identifies the candidates for investigation.

### 12.3 Which Mechanism Does UBT Prefer?

The current UBT alpha route uses winding-number quantization on S¹_ψ:
```
n ∈ ℤ   (winding number on S¹_ψ)
```

This is Mechanism 1 (basis-dimension quantization in the time sector). Extending
this to the E8 information torus would give winding numbers on T⁸_{E8}:
```
n ∈ E8   (lattice winding vectors)
```

The minimum non-zero winding has norm |n|² = 2, corresponding to the minimum
E8 vector length. This suggests the "quantum of information" in the E8 picture
is the minimum E8 root vector, with 240 equivalent choices.

**Status**: 🔶 CONJECTURAL — this extension of winding-mode quantization to
E8 is plausible but not derived from UBT field equations.

---

## 13. Testable Mathematical Questions

The following questions are **mathematically precise** and can be investigated
without further conceptual development:

**Q1**: Does the E8 theta series Θ_{E8}(τ) = E₄(τ) factor into products of
Jacobi theta functions in a way that contains ϑ₃(τ)³ as a sub-factor? What
is the precise relation:
```
E₄(τ) = f(ϑ₂, ϑ₃, ϑ₄)?
```

**Q2**: Is there a natural linear map Π: ℝ⁸ → ℝ³ that takes E8 lattice points
to the fcc lattice (which is the densest in ℝ³), making the projection
Π: T⁸_{E8} → T³_{fcc} a lattice homomorphism?

**Q3**: Does N_eff = 12 = 8 × (3/2) have a combinatorial interpretation in
terms of E8 root system data (e.g., rank, Coxeter number h = 30, Weyl group
order, etc.)?

**Q4**: What is the spectrum of the chronofactor projection Π: T⁸_{E8} → T²
under the L² decomposition? Do the eigenvalues of the projected Laplacian
reproduce the UBT winding-mode spectrum?

**Q5**: Is the Viazovska magic function f_{E8}: ℝ⁸ → ℝ related to the UBT
partition function by a linear integral transform? Specifically:
```
Z_{UBT}(τ) = ∫_{ℝ⁸} f_{E8}(x) K(x, τ) d⁸x
```
for some kernel K?

**Q6**: What are the deep holes of the E8 packing within T⁸_{E8}? Do their
240 + 2160 = 2400 representative points (roots + deep holes) correspond to
any known physical sector count in UBT?

**Q7**: Does a real 8D slice V ⊂ H₃q have a canonical definition within UBT
field theory (e.g., as the fixed-point set of a real structure / anti-linear
involution), or is the choice of V arbitrary?

---

## 14. Failure Modes

The following are the most likely ways this research front could fail:

**F1 (Dimensional mismatch)**: The UBT information space may not be 8-dimensional
in the relevant sense. If the natural information structure is 16-real (full ℂ⁸)
or 14-real (ℂP⁷), then E8 (which requires exactly ℝ⁸) is inapplicable.

**F2 (No canonical real slice)**: The choice V ≅ ℝ⁸ ⊂ H₃q may be arbitrary
(not singled out by any UBT dynamics or symmetry), making the E8 construction
basis-dependent and unphysical.

**F3 (Wrong lattice)**: Even if the information space is genuinely ℝ⁸, the
physical lattice may not be E8. Alternative dense lattices in ℝ⁸ (D8, E8 rescaled,
or other) might be more consistent with UBT dynamics.

**F4 (Chronofactor not projective)**: The chronofactor may not admit a linear
projection from T⁸_{E8}. If the time dynamics is non-linear or involves
curvature, a flat torus projection misses essential physics.

**F5 (N_eff = 12 coincidence)**: The equation 12 = 8 × (3/2) may be numerological
coincidence with no structural meaning. Checking whether other lattice dimensions
(d = 4 with E4, d = 16 with Λ_{16}, d = 24 with Leech) also produce interesting
products with existing UBT parameters is the required test.

**F6 (Modular weight conflict)**: The E8 theta series has modular weight 4,
while the UBT partition function uses weight 3/2. If these cannot be reconciled,
the modular form connection fails.

---

## 15. Status: Speculative Research Front

This document is classified as **speculative research front** within the UBT
project. The following table summarizes the claim status of all principal
assertions. See `claims_status.md` for the complete registry.

| Claim | Status |
|-------|--------|
| dim_ℂ((ℂ²)^⊗3) = 8 | ✅ DERIVED |
| T⁸ = ℝ⁸/Λ is a valid flat torus for any full-rank Λ | ✅ DERIVED |
| E8 is the densest sphere packing in ℝ⁸ (Viazovska 2016) | ✅ DERIVED (external) |
| T⁸_{E8} = ℝ⁸/E8 is a well-defined flat torus | ✅ DERIVED |
| The real 8D slice V ⊂ H₃q is the correct domain for E8 | 🔶 CONJECTURAL |
| E8 is the correct UBT information lattice | 🔶 CONJECTURAL |
| Chronofactor projection Π: T⁸_{E8} → C_chrono exists | 🔶 CONJECTURAL |
| Gaps correspond to hidden/latent/transition sectors | 🔶 CONJECTURAL |
| N_eff = 12 arises from 8D E8 sector plus projection | ❓ OPEN |
| Exponent 3/2 arises from E8 projection | ❓ OPEN |
| E8 theta series reproduces UBT partition function | ❓ OPEN |
| Alpha is derivable from E8 geometry | ❌ NOT CLAIMED |

The classification **NOT CLAIMED** is distinct from OPEN: alpha derivation from
E8 is not an objective of this research front. The front investigates information
geometry; any connection to alpha, if it exists, would be a secondary consequence
of the deeper structural result.

---

## References

- Viazovska, M.S. (2016). "The sphere packing problem in dimension 8."
  *Annals of Mathematics* 185(3), 991–1015.
  arXiv:1603.04246.

- Conway, J.H. & Sloane, N.J.A. (1999). *Sphere Packings, Lattices and Groups.*
  3rd ed. Springer.

- Cohn, H. & Kumar, A. (2009). "Optimality and uniqueness of the Leech lattice
  among lattices." *Annals of Mathematics* 170(3), 1003–1050.

- Serre, J.-P. (1973). *A Course in Arithmetic*. Springer.
  (Modular forms, Eisenstein series, lattice theta functions.)

- Penrose, R. (2004). *The Road to Reality*. Vintage.
  (General background on spinors, Hopf fibrations, and physical geometry.)

- Jaroš, D. (2026). `ALPHA_STRUCTURAL_ORIGINS.md` — N_eff = 12 and exponent
  3/2 derivations. (This repository.)

- Jaroš, D. (2026). `research_tracks/triqubit_su3_geometry.md` — Three-qubit
  Hilbert-space geometry and SU(3). (This repository.)

- Jaroš, D. (2026). `research_tracks/T3_ALPHA/neff12_derivations.tex` —
  Five independent routes to N_eff = 12. (This repository.)

---

*Status: SPECULATIVE RESEARCH FRONT — not canonical, not peer-reviewed.*  
*All conjectures are explicitly labeled. No numerology. No overclaiming.*  
*Next step: address mathematical questions Q1, Q4, Q7 before any further conjecture.*  
*License: CC BY-NC-ND 4.0 — © 2026 Ing. David Jaroš*
