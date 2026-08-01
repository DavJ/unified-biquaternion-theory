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
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Failed Routes Graveyard — Alpha Derivation from UBT

**Author**: Ing. David Jaroš  
**Updated**: 2026-04-28 (Alpha Breakthrough Mission)  
**Source inventory**: `DERIVATION_INDEX.md`, `ALPHA_PROGRESS_REPORT.md`,
  `research_tracks/T3_ALPHA/`, `experiments/validation/`

---

## Purpose

This document records every approach to deriving α from UBT that has been
attempted and found to fail, be dead ends, or be definitively excluded.

Each entry states: what was tried, why it fails, and what structural lesson
it teaches. Routes are not deleted — they are archived here as negative results.

**Notation**:
- [DEAD END] — No path to α; structural proof that the route cannot work
- [EXCLUDED] — Directly contradicted by experiment
- [CIRCULAR] — The approach uses α as input
- [SCOPE] — Correctly addresses a different question (not a failure per se)
- [RESTATEMENT] — Reduces to an already-known result without new content

---

## Group H: One-Loop Attempts

### H1 — Direct N_eff counting with one-loop anomaly

**Method**: Use the one-loop vacuum polarisation of N_eff = 12 modes on S¹_ψ
to compute the full one-loop B coefficient.

**Result**:
```
B₀ = 2π N_eff / 3 = 8π ≈ 25.133   [PROVED, clean]
n*_prime from B₀ alone: n*_continuous ≈ 2.81 → nearest prime = 3   [not 137]
```

**Why it fails**: The one-loop baseline B₀ = 8π ≈ 25.133 is too small. It gives
n* ≈ 3, not 137. A correction factor B_base/B₀ ≈ 1.65 is needed beyond the
standard one-loop result. The origin of this factor is the central open problem
(Gap G3-k: Kac-Moody level k).

**Structural lesson**: B₀ is the correct one-loop baseline but not the full coefficient.
The WZW level k is an additional factor not captured by the naive one-loop integral.

**Status**: [DEAD END for α] — B₀ is correctly proved as a subsidiary result.

---

### H2 — CS-term absence → k = 1

**Method**: The UBT action S[Θ] has no Chern-Simons term (parity-symmetric).
In 2D CFT, absence of CS term is consistent with the minimal level k=1.
Claim: k=1 follows from parity symmetry.

**Result**: This is a consistency argument, not a proof. Parity symmetry is
necessary but not sufficient for k=1. Many theories without a CS term have k > 1.

**Why it fails**: The logical gap is "consistent with k=1" ≠ "forces k=1". A proof
would need to show that k=1 is the unique value consistent with the full S[Θ]
symmetry structure. No such argument is known.

**Status**: [DEAD END] — Motivation only; no proof.

---

### H3 — Dynkin index computation

**Method**: Compute the Kac-Moody level from the Dynkin index of the representation
of the gauge group on the biquaternion field.

**Result**:
```
For adjoint representation of SU(2):   Dynkin index = 2 × dim(adj) = 6 → k = 6
For fundamental representation:        Dynkin index = 1/2 × dim(fund) = 3/2 → k = 3/2 (non-integer)
```

Neither k = 6 nor k = 3/2 equals k = 1.

**Why it fails**: The Θ field in UBT transforms in a representation of the gauge group
that is neither pure adjoint nor pure fundamental (it is in M₂(ℂ) ≅ adj ⊕ trivial for
SU(2)_L, but the correct decomposition under the full gauge group is not simply one of
the standard representations).

**Status**: [DEAD END] — Both standard representations give k ≠ 1.

---

## Group A: Algebraic/Hausdorff Approaches

### A2 — Hausdorff dimension of Im(ℍ)

**Method**: The effective coefficient should scale as (dim Im(ℍ))^{d/2} where d is
the Hausdorff dimension of Im(ℍ) ≅ ℝ³ (d = 3). This gives the factor:
```
N_eff^{d/2} = 12^{3/2} = B_base
```

**Result**: This is a structural argument that gives the correct form B_base = N_eff^{3/2}.
However, it does not independently derive the exponent d/2 = 3/2 from field theory
principles — it essentially restates the result using the Hausdorff dimension as
a labeling.

**Why it fails**: The derivation of det(S'') (the one-loop determinant of the
Hessian of the action) on Im(ℍ) has not been computed. Without this computation,
the factor 3/2 is motivated but not derived.

**Status**: [PARTIAL/RESTATEMENT] — structural motivation, not a proof.

---

### A3 — Modular weight of ϑ₃³(τ) directly → B_base

**Method**: The modular weight 3/2 of Ẑ(τ) = ϑ₃³(τ) directly encodes B_base =
N_eff^{3/2} via the coincidence of the exponent.

**Result**: The weight 3/2 is a confirmed mathematical fact about ϑ₃. The exponent
3/2 in B_base coincides numerically. However, these are different objects:
- Modular weight = transformation property of ϑ₃³ under SL(2,ℤ)
- B_base exponent = coupling of N_eff modes in the WZW loop correction

**Why it fails**: The coincidence is structural (both involve dim(Im ℍ) = 3 through
different routes) but does not constitute a derivation. The modular weight does not
directly enter the one-loop effective potential formula.

**Status**: [RESTATEMENT] — structural coincidence noted; not a derivation path.

---

## Group B: Coefficient Search Approaches

### B1 — Volume ratios of ℂ⊗ℍ geometry

**Method**: Search for a natural combination of dimensions, volumes, or norms from
the ℂ⊗ℍ algebra that equals B_base ≈ 41.57 or the ratio B_base/B₀ ≈ 1.65.

**Result**: All natural combinations tested:
```
dim_ℝ(ℂ⊗ℍ) = 8
dim_ℝ(Im ℍ) = 3
dim_ℝ(ℂ) = 2
dim(M₂(ℂ)) = 4 (complex)
[8/3] = 2.67, [8/2] = 4, [3/2] = 1.5, [8×3/2] = 12
None produce 41.57 or 1.65 without multiplying by N_eff.
```

**Status**: [DEAD END] — Exhaustive search of small-integer/dimension combinations.

---

### B2 — Algebraic search for R factor

**Method**: Systematic search for an algebraic expression for R = B_full/B_base ≈ 1.114
using UBT-internal constants.

**Best candidate found**:
```
R = 1 + α(N_eff + π + 1/4) ≈ 1 + (0.0073)(12 + 3.14159 + 0.25) ≈ 1.1123
```
Error: 0.15% vs target 1.114.

**Why it fails**: The formula uses α as input → CIRCULAR. All other algebraic
combinations found:
```
1 + 1/(4π) ≈ 1.0796   (3.1% error, no motivation)
1 + √α ≈ 1.0855       (2.6% error, uses α — circular)
1 + π/N_eff ≈ 1.262   (13.3% error)
1 + 1/(N_eff+1) ≈ 1.077  (3.3% error)
```
None are within 1% without using α.

**Status**: [DEAD END] — No non-circular algebraic expression found for R.

---

### B3 — Two-loop β-function on T³×S¹

**Method**: Compute the two-loop β-function of the biquaternion field theory on
the torus T³×S¹_ψ to get the full two-loop correction to B₀.

**Result**:
```
Scalar field content c = 1.91   [wrong by factor ~22]
SU(2) adjoint content c = 7.33  [wrong by factor ~6]
All-mode content c = 44          [close to 41.57 but no natural selection of modes]
```
None give B_base = 41.57 without artificial mode selection.

**Status**: [DEAD END] — Two-loop β-function on the correct geometry does not reproduce B_base.

---

## Group C: Curvature and Geometry Approaches

### C1 — Seeley-DeWitt heat kernel curvature on Im(ℍ)

**Method**: Use the Seeley-DeWitt expansion a₄(D²) on Im(ℍ) ≅ ℝ³ to get a
curvature correction to B₀.

**Result**:
```
Leading correction: ΔB ∝ Λ⁻² → 0 as UV cutoff Λ → ∞
```
The curvature correction vanishes in the UV limit (where B_base is evaluated).

**Status**: [DEAD END] — Heat kernel correction is UV-suppressed, not UV-enhanced.

---

### C2 — Mode pair interference on Im(ℍ)

**Method**: The three phase directions in Im(ℍ) could interfere constructively
to give a factor 3 correction to B₀.

**Result**: The interference factor is exactly 1 (modes are orthogonal in the
Hilbert space) — the three directions contribute additively, which is already
included in N_eff = 12.

**Status**: [DEAD END] — Algebraic identity; restates N_eff counting.

---

## Group D: Dimensional Reduction Approaches

### D1 — Unitarity constraint on Im(ℍ)

**Method**: Require unitarity of the mode expansion to constrain N_eff from 12 to a
smaller value (perhaps the correct effective number for B_base is different from N_eff).

**Result**: Unitarity reduces the effective mode count:
```
N_eff^{unitarity} = 8  (not 12)
B₀(8) = 2π×8/3 = 16.76   [wrong, gives smaller n*]
```
The unitarity reduction goes in the wrong direction.

**Status**: [DEAD END] — Unitarity reduces N_eff, moving n* away from 137.

---

### D2 — Dimensional transmutation on Im(ℍ)

**Method**: Use dimensional transmutation (dynamical scale generation) on Im(ℍ)
to generate the ratio B_base/B₀ ≈ 1.65.

**Result**: Dimensional transmutation introduces R_ψ as a free parameter:
```
B = B₀ × exp(2π/g²)  where g is the coupling — free parameter
```
The ratio B/B₀ is not fixed without specifying g.

**Status**: [DEAD END] — Introduces free parameter.

---

### D3 — Cartan-Killing metric on su(2)

**Method**: Use the Cartan-Killing metric normalization of su(2) to get a correction
to B₀ via the generator normalization.

**Result**: The Cartan-Killing metric on su(2) in the standard basis gives the
normalized Euclidean metric (factor 1/2 per generator). This is already included
in the standard generator convention. No additional correction arises.

**Status**: [DEAD END] — Already accounted for in standard conventions.

---

## Group E: Topological and Index-Theorem Approaches

### E1 — Instantons on SU(2)

**Method**: Instanton contributions to the effective potential could provide the
factor B_base/B₀ > 1 > B₀ correction above the perturbative baseline.

**Result**: Instantons contribute with action S_inst > 0. Their contribution to
the effective potential is proportional to exp(-S_inst) < 1, which would
*reduce* B below B₀, not increase it. The required correction is B_base > B₀,
requiring a negative-action contribution — which is impossible.

**Status**: [DEAD END] — Instantons go in the wrong direction.

---

### E2 — Atiyah-Singer index theorem on Im(ℍ)

**Method**: Use the index of a Dirac operator on Im(ℍ) ≅ ℝ³ (or S³) to get an
integer correction to B₀.

**Result**:
```
im(Im ℍ) is odd-dimensional (dim = 3) → ind(D_{S³}) = 0 for odd-dimensional manifolds
```
The index theorem gives zero for odd-dimensional manifolds. No non-trivial result.

**Status**: [DEAD END] — Index vanishes on odd-dimensional base.

---

### E3 — Holomorphic factorisation of the partition function

**Method**: The partition function Ẑ(τ) = ϑ₃³(τ) could factorize holomorphically
on the torus, allowing a WZW CFT interpretation that fixes k.

**Result**: ϑ₃³(τ) does not factorize into purely holomorphic × anti-holomorphic
parts in general. The Im(ℍ) direction is a real 3-manifold with no natural
complex structure. The Gaussian measure on Im(ℍ) is real, not complex.

**Structural lesson**: This confirms that the exponent 3/2 in B_base has a real
(rather than complex) algebraic origin, consistent with dim_ℝ(Im ℍ)/2 = 3/2.
The real structure does not exclude a WZW interpretation, but makes it harder
to establish.

**Status**: [STRUCTURAL CONFIRMATION] — Confirms the exponent origin; no new path.

---

### E4 — NCG spectral triple (UBT version)

**Method**: Construct a spectral triple (A, H, D) for the biquaternion algebra
ℂ⊗ℍ and compute B_base from the a₄ Seeley-DeWitt coefficient.

**Result**:
```
B_base/N_gen² ≈ 4.619 ≈ 3π/2   [numerical observation, gap (a) open]
```
The ratio 3π/2 is close to the required correction factor, but computing det(S'')
(the spectral-triple Hessian determinant) remains an open sub-problem.

**Status**: [PARTIAL — OPEN SUB-PROBLEM] — Numerical hint, no proof.

---

## Group F: NCG a₄ Coefficient Variants

### F1–F4 — Various NCG a₄ combinations

**Method**: Enumerate all natural combinations of dim(ℍ) = 4, dim(Im ℍ) = 3,
dim(ℂ⊗ℍ) = 8 that could appear in the NCG a₄ spectral coefficient.

**Best candidate**:
```
F4: [dim_ℝ(ℍ) × dim_ℝ(Im ℍ)]^{3/2} = [4 × 3]^{3/2} = 12^{3/2} = 41.57
```

**Why it fails**: This is an algebraic identity that restates B_base = N_eff^{3/2}
in a different notation (using dim(ℍ) × dim(Im ℍ) = 12 = N_eff). It provides no
independent derivation of the exponent 3/2.

**Status**: [RESTATEMENT] — Algebraically identical to B_base = N_eff^{3/2}.

---

## Group G: Other Approaches

### G2 — Weyl anomaly coefficient

**Method**: The Weyl anomaly coefficient of the UBT theory on S⁴ could encode
the ratio B_base/B₀.

**Result**:
```
Weyl anomaly coefficient c̃ = 1/15  [rational, small]
Required exponent to give B_base: ≈ 2.65  [unnatural, not 3/2]
```

**Status**: [DEAD END] — Weyl anomaly coefficient does not reproduce the required ratio.

---

### G4 — Fueter-regular mode count

**Method**: Count the Fueter-regular modes of the biquaternion field on the 4-sphere S⁴.

**Result**:
```
Cumulative Fueter modes at degree d: 650 (d=6), 36 (d=2), 49 (d=3)
None equal 41.57 or give n* = 137.
```

**Status**: [DEAD END] — Fueter mode count does not produce the required coefficient.

---

### G7 — Quaternionic Kähler index on ℂ⊗ℍ over ℍ

**Method**: Compute the quaternionic-Kähler index of the biquaternion bundle
ℂ⊗ℍ over ℍ (as a 4-dimensional quaternionic manifold).

**Result**:
```
ind = 4   (flat quaternionic space; independent of N_eff)
```
The flat-space index is a fixed constant independent of the field content.

**Status**: [DEAD END] — Index is N_eff-independent; cannot reproduce B_base.

---

## Group R: R-Factor Versions (v70–v73)

### R-v70 — Two-scale ratio T³×S¹ correction

**Method**: Compute the ratio of the T³ (spatial) to S¹_ψ (temporal) volumes
to get a modular correction to B₀.

**Result**: Ratio R²_T3/S1 = 1 in the self-dual limit (T-duality fixed point).
No non-trivial correction arises at the self-dual point.

**Status**: [DEAD END]

---

### R-v71 — Modular near τ = i

**Method**: Evaluate the ratio ϑ₃³(τ)/η³(τ) at the special modular point τ = i
to get a numerical correction.

**Result**: ϑ₃(i) = π^{1/4}/Γ(3/4) ≈ 1.0864... This gives a correction factor
close to 1.086, but no natural UBT-internal mechanism produces this specific
modular value as a correction to B₀.

**Status**: [DEAD END] — Numerical coincidence; no structural connection to B_base.

---

### R-v72 — Heat kernel on flat T³

**Method**: Use the heat kernel expansion on flat T³ (the spatial part of the
UBT compactification) to get a finite-size correction to B₀.

**Result**: Finite-size corrections on flat T³ go as exp(-L²/t) for large box
size L and heat-kernel time t. These are exponentially suppressed in the large-L
limit. No power-law correction to B₀ arises from flat T³.

**Status**: [DEAD END] — Corrections are exponentially small in the thermodynamic limit.

---

### R-v73 — ΔB = 3π/2 additive conjecture

**Method**: Propose ΔB = 3π/2 ≈ 4.712 as an additive correction to B₀:
```
B = B₀ + ΔB = 8π + 3π/2 = 19π/2 ≈ 29.8  [too small; gives n* far from 137]
```
Alternatively, as a multiplicative correction: B = B₀ × (1 + 3π/2 / B₀) = B₀ + 3π/2.
This still gives B ≈ 29.8, yielding n* ≈ 24 (prime).

**Origin of 3π/2**: Motivated by the modular weight k_mod = 3/2 and the minimum
Weinberg angle θ_W^{min} = π (both spurious connections).

**Why it fails**: ΔB = 3π/2 as an additive correction gives a B value that does
not yield n* = 137. The additive interpretation is wrong. The multiplicative
R-factor interpretation (R = 1 + ΔB/B_base ≈ 1.113) is numerically closer to
correct, but this approach uses θ_W indirectly in the motivation → PARTIAL CIRC.

**Status**: [DEAD END — confirmed; MC status for additive version; PARTIAL CIRC for R-factor motivation]

---

## Group EW: Electroweak Route Dead Ends

### EW-dead-1 — g = g' at electroweak scale

**Method**: Require equal normalizations of SU(2)_L and U(1)_Y kinetic terms
in the UBT Lagrangian, giving g = g'.

**Result**:
```
g = g' → tan(θ_W) = 1 → θ_W = 45°
→ sin²θ_W = 1/2
→ α = g²/(8π) ≈ 1/97
```

**Why it fails**: **DIRECTLY EXCLUDED BY EXPERIMENT**. The observed value is
sin²θ_W ≈ 0.231 ≠ 0.5. This prediction is wrong by a factor of ~2.

**Status**: [EXCLUDED] — Contradicted by precision electroweak measurements.

---

### EW-dead-2 — Schur lemma → Y normalization

**Method**: Argue that the Schur lemma forces a unique normalization of Y relative
to SU(2)_L generators in M₂(ℂ).

**Result**: The Schur lemma shows that Y ∝ 1 on each SU(2)_L irreducible representation.
This means Y commutes with all SU(2)_L generators. However, it does NOT fix the
*overall normalization* of Y relative to the SU(2)_L generators — only the representation
structure. The ratio g'/g remains free.

**Status**: [DEAD END] — Schur lemma determines representation structure, not coupling ratio.

---

### EW-dead-3 — Canonical norm matching

**Method**: Require that all gauge kinetic terms appear with the same coefficient
(canonical normalization) in the UBT action.

**Result**: This gives -1/(4g²) × Tr[W²] = -1/(4g'²) × Tr[B²], which forces g = g'.
This is the same as EW-dead-1 and is **excluded**.

**Status**: [EXCLUDED] — Same as EW-dead-1.

---

## Summary: Failure Taxonomy

| Failure type | Count | Structural lesson |
|--------------|-------|-------------------|
| DEAD END (structural barrier) | 18 | Gap G3-k (k=1) is a genuine deep problem |
| EXCLUDED (contradicts experiment) | 2 | g = g' is wrong at EW scale; GUT running required |
| CIRCULAR (uses α as input) | 3 | R ≈ 1.114, δ = 0.036, best R-algebraic candidate |
| RESTATEMENT (known result rewritten) | 4 | B_base restated in multiple languages |
| PARTIAL (numerical observation without derivation) | 3 | NCG, Hausdorff, modular |
| SCOPE BOUNDARY (different question answered correctly) | 2 | Coding → charge spectrum; RGE → relay leg |

**Total**: 27+ documented approaches; 1 genuinely untested (modular bootstrap).

---

## Open Route (NOT Graveyard)

### Track A3-bootstrap — Modular Bootstrap for k=1

This is the **one remaining route not yet attempted**. It is NOT in the graveyard.

**Method**: Apply 2D CFT bootstrap crossing symmetry to the 4-point function of
the biquaternion field on T².

**Potential outcome**: If crossing symmetry forces a unique Kac-Moody level k=1
consistent with the UBT field content, Gap G3-k is closed.

**Time-box**: 4 weeks from 2026-04-28.

See `ALPHA_BREAKTHROUGH_REPORT.md §4` and `canonical/alpha/alpha_best_route.tex §9`
for the detailed attack plan.
