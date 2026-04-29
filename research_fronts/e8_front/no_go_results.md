<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# no_go_results.md — E8 Front: No-Go Results

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Track**: T3_E8 — E8 / Qubit / Torus Research Front  
**Purpose**: Explicit registry of what has been ruled out or falsified in
the E8 front. A clean no-go is as valuable as a positive result.

---

## Summary Table

| ID | Claim tested | Status | Method | Strength |
|----|-------------|--------|--------|---------|
| NG-1 | E8 lattice lives in ℂ⁸ | ❌ NO-GO | E8 is defined over ℝ; ℂ⁸ has dim_ℝ = 16; no ℝ⁸ ≅ ℂ⁸ | DERIVED |
| NG-2 | E8 torus T⁸_{E8} identified with ℂP⁷ | ❌ NO-GO | ℂP⁷ is curved (non-zero curvature); T⁸_{E8} is flat | DERIVED |
| NG-3 | 3-qubit basis dimension 8 = 8-bit precision | ❌ NO-GO | 2³ = 8 (basis states); 2⁸ = 256 (numerical precision) — distinct concepts | DERIVED |
| NG-4 | E8 directly gives α⁻¹ = 137.036 (numerical coincidence hunt) | ❌ NO-GO | Systematic search: no combination of E8 invariants found | NUMERICAL |
| NG-5 | ℂP⁷ is the UBT information space | ❌ NO-GO | ℂP⁷ is phase space of pure states; not a lattice; packing irrelevant | DERIVED |
| NG-6 | E8 replaces the UBT partition function ϑ₃(τ)³ | ❌ NO-GO | Different modular weights (4 vs 3/2); coexistence hypothesis remains, not replacement | DERIVED |
| NG-7 | Quantization in 8D is equivalent to three-qubit quantization | 🔶 OPEN (partial no-go) | The statement requires a precise identification φ: V → ℝ⁸; this is unproved (Gap Q7) but not ruled out | PARTIAL |

---

## Detailed No-Go Statements

### NG-1: E8 Cannot Live in ℂ⁸

**Claim tested**: There exists an identification of the E8 lattice with a
sublattice of ℂ⁸.

**No-go argument**:
- The E8 lattice is an even self-dual lattice in ℝ⁸.
- ℂ⁸ = ℝ¹⁶ as a real vector space.
- An even self-dual lattice in ℝ¹⁶ has a different classification
  (includes D₁₆ and E₈ × E₈ as distinct possibilities).
- There is no canonical identification of ℝ⁸ with a subspace of ℂ⁸
  that preserves the E8 lattice structure.
- The relevant real 8D space is V = span_ℝ{|000⟩, ..., |111⟩} ⊂ H₃q,
  which is a real subspace, not a complex one.

**Conclusion**: E8 requires ℝ⁸, not ℂ⁸. This restricts the E8 construction
to the real slice V of the three-qubit space.

---

### NG-2: T⁸_{E8} ≠ ℂP⁷

**Claim tested**: The E8 torus can be identified with the projective state
space ℂP⁷ = S¹⁵/U(1).

**No-go argument**:
- ℂP⁷ is a complex projective space with Fubini-Study metric of constant
  positive holomorphic sectional curvature.
- T⁸_{E8} = ℝ⁸/E8 is a flat torus: its curvature tensor is identically zero.
- A flat space cannot be isometric to a positively curved space.
- Therefore T⁸_{E8} ≇ ℂP⁷ as Riemannian manifolds.

**Conclusion**: The E8 torus construction requires a separate real slice,
not the full quantum state space ℂP⁷.

---

### NG-3: Dimension 8 (Qubit States) ≠ 8-Bit Precision

**Claim tested**: The 8D nature of the three-qubit system has something to
do with 8-bit numerical precision (256 levels).

**No-go argument**:
- (ℂ²)^⊗3 has dim_ℂ = 2³ = 8 basis states.
- 8-bit numerical precision encodes 2⁸ = 256 discrete levels per variable.
- These are distinct notions: basis count vs precision quantization.
- The E8 connection uses dim = 8 in the sense of basis states,
  which is a property of the three-qubit Hilbert space, not a precision claim.

**Conclusion**: No connection between E8 and 8-bit precision. This is a
conceptual confusion to avoid.

---

### NG-4: No Direct E8 → α⁻¹ = 137.036

**Claim tested**: Some combination of E8 invariants (kissing number 240,
packing density π⁴/384, lattice determinant 1, theta series coefficients)
directly yields α⁻¹ = 137.036.

**Numerical search results**:

| Expression | Value | Matches α⁻¹ = 137.036? |
|------------|-------|------------------------|
| 240/√(2π) | ≈ 95.8 | No |
| 240 × π⁴/384 | ≈ 61.2 | No |
| (384/π⁴)^(1/2) × 137 | Forced fit | ❌ Fitted — disqualified |
| θ_{E8}(i) = E₄(i) | = 1 + 240e^{-2π} + ... ≈ 1.00000... | No |
| rank(E8) × N_eff/2 | 8 × 6 = 48 | No |
| 240 - 137 | 103 | No (no motivation) |
| √(240 × 137) / π | ≈ 57.8 | No |

**Conclusion**: No combination of the basic E8 invariants yields 137.036
without fitting. This is a **definitive no-go for direct numerical coincidences**.

**Surviving connection**: The indirect route via Θ_{E8}(τ) = E₄(τ) and
its relation to the V_eff partition function remains OPEN (Gap A-2).

---

### NG-5: ℂP⁷ Is Not the UBT Information Space

**Claim tested**: The quantum state space ℂP⁷ = {unit vectors in ℂ⁸}/U(1)
is the natural UBT information geometry.

**No-go argument**:
- ℂP⁷ is the space of pure states of a three-qubit system.
- UBT's information geometry is based on winding modes on the ψ-circle S¹_ψ.
- The ψ-circle compactification gives a lattice structure (integer winding numbers),
  not a projective state space.
- Generalizing to 8D torus structures requires the real slice V, not ℂP⁷.

**Conclusion**: ℂP⁷ is a valid mathematical object but not the correct space
for the E8 lattice construction.

---

### NG-6: E8 Does Not Replace ϑ₃(τ)³

**Claim tested**: The E8 theta series Θ_{E8}(τ) = E₄(τ) replaces the
existing UBT partition function ϑ₃(τ)³ in the alpha derivation.

**No-go argument**:
- ϑ₃(τ)³ has modular weight 3/2 under SL₂(ℤ) — this arises from the
  three-dimensional imaginary quaternion sector Im ℍ ≅ ℝ³.
- E₄(τ) = Θ_{E8}(τ) has modular weight 4 — this arises from the 8D E8 lattice.
- These are different modular forms with different transformation properties.
- They cannot be equal as modular forms (different weights).

**What can be true**: E₄(τ) and ϑ₃(τ)³ can both appear in the UBT partition
function, summing over different sectors. The relationship between them
(e.g., via modular identities) is an open mathematical question (Gap Q1).

**Conclusion**: NG-6 is a definitive no-go for replacement; coexistence
hypothesis remains open.

---

## Active Partial No-Goes (Not Yet Definitive)

| Claim | Status | Current evidence |
|-------|--------|-----------------|
| E8 lattice is the unique UBT information lattice | Not yet a no-go; not proved | C5.5 in claims_status.md: CONJECTURAL |
| Chronofactor projection is unique | Not yet a no-go; multiple options exist | C9.1–C9.7 in claims_status.md |
| Packing density → coupling constant | No concrete mechanism found; not definitively ruled out | Ongoing — NG-4 is suggestive |

---

## Implications for Research Direction

The no-go results sharpen the target: E8 must be sought via:
1. The real slice V = span_ℝ(computational basis), not via ℂ⁸ or ℂP⁷.
2. Indirect connections through modular forms (Θ_{E8} = E₄), not direct numerics.
3. Potential factorization 12 = 8 × (3/2) as a structural relation, not a numerical coincidence hunt.

---

## References

- `research_fronts/e8_torus_quantized_information/claims_status.md`
- `research_fronts/e8_front/current_best_model.md`
- `research_fronts/e8_front/relevance_to_alpha.md`
