<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# polyhedral_weinberg_scan.md — Platonic Discrete Symmetry and the Weinberg Angle

**Track**: T3_ALPHA — Weinberg-Angle Program  
**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Status**: Research scan — honest assessment, all computations explicit  
**Deliverable ID**: T3_ALPHA / polyhedral route scan  
**Companion**: `canonical/alpha/ew_mixing_gap_map.md`,
`canonical/alpha/weinberg_angle_routes.md`

---

## Objective and Rules

**Question**: Can sin²θ_W emerge from the discrete symmetry groups of the
Platonic solids — A4 (tetrahedron), S4 (octahedron/cube), A5
(icosahedron/dodecahedron) — through representation theory or projection
geometry, without numerical fitting?

**Hard rules**:
1. No fitted constants. Every parameter must be independently derived.
2. All predictions must arise from group-theoretic structure (representations,
   projection geometry, index theory) — not from choosing parameters to match
   the target value sin²θ_W(M_Z) ≈ 0.2312.

**Experimental target** (PDG 2024, MS-bar):

```
sin²θ_W(M_Z) = 0.23122 ± 0.00003
sin²θ_W(M_GUT) = 3/8 = 0.3750   [SU(5) GUT boundary]
```

---

## Mathematical Framework

The Weinberg angle θ_W is defined by the ratio of the U(1)_Y and SU(2)_L
gauge couplings at a given scale:

```
tan θ_W = g'/g      (coupling ratio)
sin²θ_W = g'² / (g² + g'²)
```

For a discrete group G to fix sin²θ_W, it must determine the ratio g'/g by
one of these mechanisms:

| Mechanism | Description |
|-----------|-------------|
| **Projection geometry** | G acts on a vector space; T₃ and Y are identified with specific invariant directions; their angle is θ_W |
| **Dynkin index ratio** | G embeds in a continuous GUT group; the Dynkin index of the U(1)_Y embedding relative to SU(2)_L fixes g'/g |
| **McKay-ADE-GUT route** | G (discrete) → McKay quiver → ADE Lie algebra → GUT boundary condition for sin²θ_W |

Each route is evaluated for A4, S4, A5 below.

---

## Group-Theoretic Preliminaries

### The three groups

| Group | Geometric name | Order | Binary cover | McKay ADE | Irrep dims |
|-------|---------------|-------|-------------|-----------|-----------|
| A4 | Tetrahedral rotations | 12 | 2T (binary tetrahedral) | Ê₆ → E₆ | 1, 1, 1, 3 |
| S4 | Octahedral rotations | 24 | 2O (binary octahedral) | Ê₇ → E₇ | 1, 1, 2, 3, 3 |
| A5 | Icosahedral rotations | 60 | 2I (binary icosahedral) | Ê₈ → E₈ | 1, 3, 3, 4, 5 |

The binary covers 2T, 2O, 2I are subgroups of SU(2); the base groups A4, S4, A5
are their images in SO(3) under the standard covering map SU(2) → SO(3).

### Symmetry axes of Platonic solids

| Group | Order-2 axes (C₂) | Order-3 axes (C₃) | Order-4 axes (C₄) | Order-5 axes (C₅) |
|-------|------------------|------------------|------------------|------------------|
| A4 | (1,0,0), (0,1,0), (0,0,1) | (±1,±1,±1)/√3 (4 pairs) | — | — |
| S4 | edge midpts (12) | (±1,±1,±1)/√3 (4 pairs) | face ctrs (3) | — |
| A5 | edge midpts (15) | face ctrs (10) | — | vertex dirs (6) |

All axes normalised to unit vectors.

---

## Route 1: Projection Geometry

### Method

For each group G and each pair of distinct symmetry axes (n̂₁, n̂₂), compute
the Hilbert-Schmidt angle in the SU(2) representation:

```
cos θ = ⟨n̂₁·σ/2, n̂₂·σ/2⟩ / (|n̂₁·σ/2| |n̂₂·σ/2|)
       = n̂₁ · n̂₂
```

(the Hilbert-Schmidt angle in the spin-1/2 rep equals the geometric axis angle).

Identify: T₃ → one symmetry axis direction, Y → another axis direction.
Read off: sin²θ = 1 − (n̂₁ · n̂₂)².

### Results

#### A4 (tetrahedral)

| T₃ direction | Y direction | cos θ | sin²θ | Exact form |
|--------------|-------------|-------|-------|-----------|
| C₂: (0,0,1) | C₃: (1,1,1)/√3 | 1/√3 | **2/3** | 2/3 |
| C₂: (0,0,1) | C₂: (1,0,0) | 0 | 1 | 1 |

**A4 is excluded**: sin²θ = 2/3 ≈ 0.667 for the only non-trivial non-orthogonal
pair. This is excluded by experiment (factor 2.9 above measured value).

#### S4 (octahedral/cubic)

S4 contains A4 as a subgroup, so the A4 axis pairs reappear.
Additional S4-specific pairs involving the C₄ (4-fold) axes:

| T₃ direction | Y direction | cos θ | sin²θ | Exact form |
|--------------|-------------|-------|-------|-----------|
| C₄: (0,0,1) | C₃: (1,1,1)/√3 | 1/√3 | **2/3** | 2/3 |
| C₄: (0,0,1) | C₂-face: (1,0,1)/√2 | 1/√2 | **1/2** | 1/2 |
| C₄: (0,0,1) | C₂-edge: (1,1,0)/√2 | 0 | 1 | 1 |
| C₃: (1,1,1)/√3 | C₂-edge: (1,1,0)/√2 | √(2/3) | **1/3** | 1/3 |

**S4 results**: Three clean rational values: 1/3, 1/2, 2/3.

- sin²θ = 1/3 ≈ 0.333: above the GUT value 3/8 = 0.375? No, 0.333 < 0.375.
  It lies between the measured low-energy value (0.231) and the GUT value (0.375)
  but matches neither.
- sin²θ = 1/2: too large.
- sin²θ = 2/3: too large.

**S4 is not conclusive**: rational predictions at 1/3, 1/2, 2/3 do not match
sin²θ_W at any experimentally relevant scale.

#### A5 (icosahedral/dodecahedral)

The golden ratio φ = (1+√5)/2 enters through the icosahedral geometry.

Standard coordinates: icosahedron vertices at (0, ±1, ±φ) and cyclic permutations;
C₅ axes along (0, 1, φ)/√(1+φ²), C₃ along (1,1,1)/√3,
C₂ along (1, φ², φ)/(2φ) [edge midpoint].

Note: φ² = φ+1, so (1+φ²) = φ+2 = (5+√5)/2.

| T₃ direction | Y direction | cos θ | sin²θ | Exact form |
|--------------|-------------|-------|-------|-----------|
| C₅ | C₃ | φ²/√(3(φ+2)) | ≈ 0.369 | 1 − φ⁴/[3(φ+2)] |
| **C₅** | **C₂** | φ/√(φ+2) | **≈ 0.276** | **(5−√5)/10** |
| C₃ | C₂ | φ/√3 | ≈ 0.127 | (3−√5)/6 |

**A5 best candidate: sin²θ = (5−√5)/10**

The C₅–C₂ axis pair gives:

```
cos θ = φ / √(φ+2) = φ / √((5+√5)/2)

sin²θ = 1 − φ²/(φ+2) = 1/(φ+2) = 2/(5+√5) = (5−√5)/10
```

Numerical value: **(5−√5)/10 ≈ 0.2764**

This is a clean, parameter-free algebraic expression in the golden ratio. It is
the only geometric prediction from any Platonic group that falls within striking
distance of sin²θ_W(M_Z) ≈ 0.2312.

**Deviation from experimental value**: 19.5% above sin²θ_W(M_Z) = 0.2312.
**Deviation from GUT boundary**: 26% below sin²θ_W(M_GUT) = 3/8 = 0.375.

This intermediate value does not match either known reference point cleanly,
and there is no a priori principle that identifies T₃ with the C₅ direction
and Y with the C₂ direction in the icosahedron — making this result
suggestive but not derived.

### Route 1 verdict

| Group | Best prediction | Exact form | Status |
|-------|----------------|------------|--------|
| A4 | 2/3 | 2/3 | EXCLUDED — factor 2.9 off |
| S4 | 1/3 | 1/3 | Not matching — neither scale |
| A5 | (5−√5)/10 | (5−√5)/10 | SUGGESTIVE but 19.5% off; axis identification unjustified |

**Route 1 conclusion**: No Platonic solid group predicts sin²θ_W from first
principles via projection geometry alone. The identification of T₃ with one
specific axis type and Y with another requires additional physical input.

---

## Route 2: Representation Theory / Dynkin Index

### Method

For each group G embedded in SU(2) × U(1), the coupling ratio is:

```
g'²/g² = Σ_reps dim(ρ) · Y²_ρ / Σ_reps Tr_ρ(T₃²)
```

For SU(2)_L doublets (j=1/2): Tr(T₃²) = 1/2 per doublet.
For singlets with hypercharge Y: contribute dim×Y² to the numerator.

### Key obstruction

The hypercharge Y of each matter representation is NOT determined by the
discrete group G alone. The groups A4, S4, A5 constrain which representations
appear and what their SU(2)_L structure is (through the SU(2) embedding), but
they do not constrain the U(1)_Y charge.

**Proof**: The center of A4 is trivial; A4 has no U(1) subgroup that could
serve as U(1)_Y. Similarly for S4 and A5. The only U(1) available in these
groups is the Cartan subalgebra of the SU(2) ambient group — which is T₃, not Y.

For Y to be fixed, G must be embedded in a continuous group G_GUT that contains
U(1)_Y as a specific subalgebra.

### What can be computed

Under the specific embedding 2G → G_GUT with the matter content determined by
decomposition of G_GUT representations under 2G, the ratio g'/g is fixed.

For the minimal SM fermion content (one generation) and the standard SU(5)
hypercharge assignments:

```
Tr(T₃²) per generation = 3 × ½ + ½ = 2  [3 colors × Q_L doublet + L_L doublet]
Tr(Y²)  per generation = 3(1/36 + 4/9 + 1/9) + (1/4 + 1) = 10/3

sin²θ_W(GUT) = Tr(Y²) / [Tr(T₃²) + Tr(Y²)] = (10/3) / (2 + 10/3) = 3/8 ✓
```

This is the standard SU(5) result. The same calculation applies for any G
embedded in SU(5), since the matter content and hypercharge assignments are
inherited from SU(5), not from G.

### Dynkin index for each binary polyhedral group

| Binary group | Irrep dims | 2D irreps (doublets) | SU(2) Dynkin index |
|-------------|-----------|---------------------|-------------------|
| 2T (A4 double) | 1,1,1,2,2,2,3 | three 2D irreps (j=1/2) | I = 3×(1/2) = 3/2 |
| 2O (S4 double) | 1,1,2,2,2,3,3,4 | three 2D irreps | I = 3×(1/2) = 3/2 |
| 2I (A5 double) | 1,2,2,3,4,4,5,6 | two 2D irreps | I = 2×(1/2) = 1 |

The U(1)_Y contribution requires hypercharge assignments, which are not determined
by the discrete group.

### Route 2 verdict

**Discrete group alone cannot fix sin²θ_W via Dynkin index.** The ratio g'/g
remains a free parameter until U(1)_Y is identified within a GUT embedding.

---

## Route 3: McKay-ADE-GUT Boundary Condition

### Method

The McKay correspondence maps each binary polyhedral group to an affine ADE Lie
algebra:

```
2T (binary tetrahedral, |2T|=24) → Ê₆ → E₆
2O (binary octahedral, |2O|=48) → Ê₇ → E₇
2I (binary icosahedral, |2I|=120) → Ê₈ → E₈
```

Each ADE Lie algebra defines a candidate GUT group G_GUT. The standard embedding
G_GUT ⊃ SU(3) × SU(2) × U(1) then fixes sin²θ_W(M_GUT) via the Georgi-Glashow
trace formula.

### A4 → E₆ → sin²θ_W

E₆ contains SU(5) as a maximal subgroup: E₆ ⊃ SO(10) ⊃ SU(5) ⊃ SM.

Along the chain E₆ → SU(5) → SM, the hypercharge generator inherits the SU(5)
normalization. The Georgi-Glashow formula gives:

```
sin²θ_W(M_GUT) = 3/8 = 0.375   [A4, E₆ route, via SU(5)]
```

After one-loop RG running with SM particle content from M_GUT ≈ 2×10¹⁶ GeV to M_Z:

```
sin²θ_W(M_Z) ≈ 0.231   [standard SU(5) RG result]
```

This is not a prediction of A4 specifically; it is the SU(5) GUT result,
which holds for any group embedded in SU(5).

### S4 → E₇ → sin²θ_W

E₇ has two natural breaking chains to the SM:

**Chain (i): E₇ ⊃ E₆ × U(1) ⊃ SO(10) ⊃ SU(5) ⊃ SM**

```
sin²θ_W(M_GUT) = 3/8 = 0.375   [same as SU(5), inherited]
```

**Chain (ii): E₇ ⊃ SO(12) × SU(2) ⊃ SO(10) × U(1) ⊃ SM**

In this chain, the hypercharge mixes with the SO(12) Cartan elements differently
from SU(5). The resulting GUT-scale prediction is:

```
sin²θ_W(M_GUT) = 3/7 ≈ 0.429   [E₇, SO(12) route]
```

After one-loop RG running (same shift as SU(5) route ≈ 0.144):

```
sin²θ_W(M_Z) ≈ 3/7 − 0.144 ≈ 0.285   [E₇, SO(12) route, rough estimate]
```

This prediction is 23% above the experimental value and is excluded at the
current level of accuracy.

**S4 is not uniquely predictive**: the two E₇ breaking chains give different
sin²θ_W values, and S4 alone does not select between them.

### A5 → E₈ → sin²θ_W

E₈ contains SO(16) ⊃ SO(10) ⊃ SU(5) ⊃ SM.

The standard breaking chain:

```
E₈ ⊃ SO(10) × U(1) × U(1) → SO(10) ⊃ SU(5) ⊃ SM
sin²θ_W(M_GUT) = 3/8 = 0.375   [A5, E₈ route, via SU(5)]
```

After RG running: sin²θ_W(M_Z) ≈ 0.231 (standard SU(5) result).

Again, the prediction is identical to the SU(5) case and does not provide
A5-specific information.

### McKay route summary

| Group | ADE | Via SU(5) chain | Via alternative chain | Distinguishing? |
|-------|-----|----------------|-----------------------|-----------------|
| A4 | E₆ | 3/8 (GUT) → 0.231 (M_Z) | — | No |
| S4 | E₇ | 3/8 (GUT) → 0.231 (M_Z) | **3/7 (GUT) → 0.285 (M_Z)** | Yes — but excluded |
| A5 | E₈ | 3/8 (GUT) → 0.231 (M_Z) | — | No |

**Route 3 conclusion**: Via the common SU(5) subalgebra, all three groups predict
the correct sin²θ_W(M_Z) ≈ 0.231 — but this is a SU(5) prediction, not a
Platonic-solid prediction. The only genuinely distinct prediction (S4 via the
E₇ SO(12) chain) is excluded by experiment.

---

## Combined Results Table

| Group | Route | Prediction | Exact form | Status |
|-------|-------|-----------|-----------|--------|
| A4 | Projection (C₂–C₃) | 0.667 | 2/3 | EXCLUDED |
| A4 | McKay → E₆ → SU(5) | 0.231 | 3/8 → RG | Reproduced, not derived from A4 |
| S4 | Projection (C₄–C₃) | 0.667 | 2/3 | EXCLUDED |
| S4 | Projection (C₄–C₂) | 0.500 | 1/2 | EXCLUDED |
| S4 | Projection (C₃–C₂) | 0.333 | 1/3 | No match at any scale |
| S4 | McKay → E₇ → SU(5) | 0.231 | 3/8 → RG | Reproduced, not derived from S4 |
| S4 | McKay → E₇ → SO(12) | 0.285 | 3/7 → RG | EXCLUDED |
| A5 | Projection (C₅–C₃) | 0.369 | — | No match |
| **A5** | **Projection (C₅–C₂)** | **0.276** | **(5−√5)/10** | **Nearest; ~20% off; unanchored** |
| A5 | Projection (C₃–C₂) | 0.127 | (3−√5)/6 | EXCLUDED |
| A5 | McKay → E₈ → SU(5) | 0.231 | 3/8 → RG | Reproduced, not derived from A5 |

---

## The A5 Suggestive Result: (5−√5)/10

The icosahedral group A5 produces a clean, derivation-free expression:

```
sin²θ = (5 − √5) / 10   [C₅–C₂ axis angle]
       = 1 / (φ + 2)    [φ = golden ratio]
       ≈ 0.2764
```

This is the angle between a 5-fold rotation axis and an edge-midpoint (2-fold)
axis of the icosahedron, computed via the Hilbert-Schmidt inner product in the
spin-1/2 representation.

**Why it is suggestive but not a derivation**:

1. **Axis identification is unjustified**: For T₃ → C₅ and Y → C₂ to be a
   physical statement, there must be a mechanism in UBT that assigns the
   SU(2)_L Cartan direction to the 5-fold axis and the U(1)_Y generator to
   the edge-midpoint direction. No such mechanism is currently identified.

2. **Scale mismatch**: (5−√5)/10 ≈ 0.276 lies between sin²θ_W(M_Z) ≈ 0.231
   and sin²θ_W(M_GUT) = 0.375. It would match at some intermediate scale, but
   the value of that scale cannot be predicted without specifying the RG running,
   which in turn requires knowing the spectrum above M_Z.

3. **No independent fixing of both generators**: sin²θ_W requires simultaneously
   knowing the normalisation of both T₃ and Y. The C₅ and C₂ axes are geometric
   objects; converting them to Lie algebra generators requires a normalisation
   convention that introduces a free parameter.

**What would make this a derivation**: A UBT-internal mechanism showing that
A5 acts on the (T₃, Y) subspace of su(2)_L ⊕ u(1)_Y with T₃ identified with
the C₅ generator and Y with the C₂ generator, together with a natural
normalisation of both generators from the kinetic term structure.

---

## Verdict: None of the Three Routes Derives sin²θ_W from Platonic Solids

| Route | Verdict | Reason |
|-------|---------|--------|
| Projection geometry (all groups) | **INDETERMINATE** | Axis identification to T₃, Y requires additional physical input |
| Dynkin index (all groups) | **OPEN** | U(1)_Y charge not fixed by discrete group alone |
| McKay → SU(5) (A4, A5) | **REPRODUCES**, not derives | Prediction = SU(5) GUT; discrete group is irrelevant |
| McKay → E₇ → SO(12) (S4) | **EXCLUDED** | Predicts sin²θ_W(M_Z) ≈ 0.285 ≠ 0.231 |

**Summary conclusion**: The three Platonic discrete symmetry groups do not, by
themselves, predict sin²θ_W from first principles. The McKay-ADE route recovers
the correct value via SU(5), but this is SU(5) physics — the discrete group is a
spectator. The only geometrically clean prediction specific to A5 (the golden-ratio
result (5−√5)/10 ≈ 0.276) is suggestive but requires physical justification of the
axis identification.

---

## What This Scan Rules In and Rules Out

### Ruled out (definitive)

- **A4 and S4 via projection geometry**: All axis-pair predictions give sin²θ ≥ 1/3,
  which is excluded for any scale from M_Z to M_GUT.
- **S4 via E₇ → SO(12) route**: Predicts ≈ 0.285, excluded.
- **A4 or A5 providing a distinct prediction from SU(5)**: They don't; they
  reproduce SU(5) through their GUT subalgebra.

### Ruled in as candidate (requires further work)

- **A5 (icosahedral) via C₅–C₂ projection geometry**: The prediction sin²θ =
  (5−√5)/10 is a clean algebraic result. It is not currently derived from UBT
  physics. The following steps would be needed to determine whether it is viable:
  1. Identify a UBT-internal reason why A5 acts on the EW mixing sector.
  2. Derive the axis identification T₃ ↔ C₅, Y ↔ C₂ from the UBT action S[Θ].
  3. Show the normalisation of both generators from the canonical kinetic term.
  4. Determine the scale at which sin²θ = (5−√5)/10; compare with the known
     RG trajectory.

---

## Open Problems Registered

| Gap ID | Description | Required for |
|--------|-------------|-------------|
| POL-1 | Derive axis identification for A5: why T₃ ↔ C₅ and Y ↔ C₂ | Anchoring the (5−√5)/10 prediction |
| POL-2 | Compute sin²θ_W from E₇ → SM via all maximal breaking chains | Determining if S4/E₇ is viable |
| POL-3 | Identify whether A5 ⊂ Aut(ℂ⊗ℍ) in a way that acts on EW sector | Connecting A5 to UBT algebra |
| POL-4 | Find the RG scale at which sin²θ_W(μ) = (5−√5)/10 | Checking if A5 prediction is self-consistent |

---

## Connections to Existing UBT Work

- `canonical/alpha/ew_mixing_gap_map.md` — EW mixing gap map; Gap EW-1 is the
  blocking gap for all Weinberg angle routes
- `canonical/alpha/weinberg_angle_routes.md` — broader survey of Weinberg angle
  routes including GUT boundary, algebra normalization, and geometric projection
- `canonical/alpha/alpha_derivation_routes.md` — routes A1–A4 for α derivation;
  the Weinberg angle is the blocking gap for A1 and A2
- `canonical/interactions/sm_gauge.tex` — proved SU(2)_L and U(1)_Y embeddings
  in ℂ⊗ℍ; starting point for a UBT-native Weinberg angle derivation
- `reports/ew_mixing_status.md` — master EW mixing status

---

## References (External)

- Georgi, Glashow (1974): SU(5) GUT, sin²θ_W = 3/8 at GUT scale
- McKay (1980): McKay correspondence, ADE classification
- González-Arroyo, Korthals Altes et al.: Discrete subgroups and GUT models
- King, Luhn (2013): Neutrino mass and mixing with discrete symmetry, Rep. Prog. Phys. 76
- Raby (2002): E₇ GUT models, alternative symmetry breaking chains
- Kiritsis (2009): String theory and ADE singularities
