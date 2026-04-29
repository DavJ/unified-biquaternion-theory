<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# current_best_model.md — E8 Front: Current Best Model

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Track**: T3_E8 — E8 / Qubit / Torus Research Front  
**Status**: Research front — QUARANTINED from canonical claims  
**Hard rule**: Nothing in this document constitutes a canonical UBT claim
unless explicitly marked DERIVED and cited in `canonical/`.

---

## 1. Research Question

Is the E8 lattice in ℝ⁸ a real mathematical structure arising from UBT,
or is it only an analogy suggested by dimension coincidences?

**Falsification criterion**: The question has a definite answer in either direction.
A useful outcome is either:
- an explicit construction showing E8 arises from UBT dynamics, or
- an explicit no-go showing E8 cannot arise.

---

## 2. Foundation (Derived Facts — Canonical)

These are imported from canonical UBT results and are not specific to E8.

| Fact | Status | Source |
|------|--------|--------|
| dim_ℝ(ℂ⊗ℍ) = 8 | ✅ DERIVED [L0] | Algebra definition |
| Three-qubit Hilbert space (ℂ²)^⊗3 has dim_ℂ = 8 | ✅ DERIVED [L0] | 2³ = 8 |
| N_eff = 12 from algebra mode counting | ✅ DERIVED [L0] | canonical/n_eff/ |
| 12 = 8 × (3/2) — arithmetic identity | ✅ DERIVED [L0] | Number theory |
| ℝ⁸ ≅ ℂ⊗ℍ as real vector spaces | ✅ DERIVED [L0] | Dimension count |
| E8 is the unique (up to isometry) even self-dual lattice in ℝ⁸ | ✅ DERIVED | External: lattice theory |
| E8 achieves the maximal sphere-packing density in ℝ⁸ (π⁴/384) | ✅ DERIVED | External: Viazovska 2016 |
| E8 kissing number = 240 | ✅ DERIVED | External: combinatorics |
| Θ_{E8}(τ) = E₄(τ) = 1 + 240q + ... (weight-4 modular form) | ✅ DERIVED | External: modular forms |

---

## 3. The Current Best Conjectural Model

**Hypothesis (not a theorem)**: The real amplitude subspace of the
three-qubit state (ℂ²)^⊗3, after projecting to a canonical real 8D slice
defined by the S¹_ψ phase structure of UBT, carries the E8 lattice as the
natural information lattice.

### Precise formulation (best current state)

Let:
- H₃q = (ℂ²)^⊗3 be the three-qubit Hilbert space
- V ⊆ H₃q be the real 8D subspace defined by setting all imaginary amplitudes
  to zero: V = span_ℝ{|000⟩, |001⟩, ..., |111⟩}
- T⁸_{E8} = ℝ⁸/E8 be the flat torus with the E8 identification

**Conjecture (C-E8)**: There exists a canonical identification φ: V → ℝ⁸
compatible with the biquaternion algebra action such that the UBT
winding-mode quantization on S¹_ψ is equivalent to winding on T⁸_{E8}.

**Status**: 🔶 CONJECTURAL — dimension coincidence is observed; the canonical
identification φ is not derived from UBT dynamics.

---

## 4. Subtracks and Current Progress

### E8_1 — 3-Qubit to 8D Structure Audit

| Task | Status | Finding |
|------|--------|---------|
| Formalize H = (ℂ²)^⊗3 | ✅ Done | Standard QM; dim_ℂ = 8, dim_ℝ = 16 |
| Distinguish ℂ⁸, ℝ¹⁶, ℂP⁷ | ✅ Done | ℂ⁸ ≠ ℝ¹⁶ ≠ ℂP⁷; E8 lives in ℝ⁸, not these |
| Identify natural real 8D slice V | 🔶 Partial | V = real span of basis states; naturalness requires derivation from UBT |

**Finding**: The real slice V = ℝ⁸ is well-defined but its preferred status
within H₃q requires a dynamical argument (Gap Q7: what selects V over other
real slices?).

### E8_2 — Lattice Feasibility

| Task | Status | Finding |
|------|--------|---------|
| Can E8 lattice arise naturally? | 🔶 Plausible | Optimality argument (packing) is suggestive; not derived from S[Θ] |
| Torus quotient T⁸ = ℝ⁸/E8 | ✅ Well-defined | Standard math; det(Gram) = 1 (self-dual) |
| Candidate coordinates for E8 | 🔶 Partial | Standard root system coordinates available; UBT identification not done |

**Finding**: T⁸_{E8} is well-defined as a mathematical object. Its role as
the UBT information lattice is plausible but unproved.

### E8_3 — Packing to Alpha Relevance

| Task | Status | Finding |
|------|--------|---------|
| Can packing density generate normalization factors? | ❓ Open | Δ_{E8} = π⁴/384 ≈ 0.2537; no connection to α⁻¹ found yet |
| Can theta series create spectral ratios? | 🔶 Plausible | Θ_{E8} = E₄ has coefficient 240; ratio structure unclear |
| Can any E8 result feed current alpha route? | ❓ Open | See relevance_to_alpha.md |

**Finding**: No direct route from E8 packing to α yet identified. The most
promising connection is via Θ_{E8}(τ) = E₄(τ) and its special values.

### E8_4 — Chronofactor Projection

| Task | Status | Finding |
|------|--------|---------|
| Define projection Π: T⁸_{E8} → C_chrono | 🔶 Partial | Linear projection exists mathematically; C_chrono = T² or S² (undecided) |
| Compare to Bloch sphere / phase evolution | 🔶 Partial | Both S² (Bloch) and T² (UBT phase torus) are viable targets |
| Mark conjectural vs derived | ✅ Done | All chronofactor claims are CONJECTURAL in claims_status.md |

**Finding**: Two competing options for C_chrono (T² and S²) are unresolved.
The chronofactor projection is a CONJECTURAL object; its definition requires
a choice not yet determined by UBT dynamics.

---

## 5. Best Available Structural Connection

The strongest current connection between E8 and the alpha derivation is:

1. N_eff = 12 = 8 × (3/2) where 8 = rank(E8) and 3/2 is the proved exponent
   from the heat kernel on Im ℍ ≅ ℝ³.
2. Θ_{E8}(τ) = E₄(τ) = 1 + 240q + 2160q² + ... and the alpha route
   involves V_eff evaluated via modular forms.

**Relationship of these observations**:
- The factorization 12 = 8 × (3/2) is exact but not yet shown to be
  structurally meaningful (as opposed to coincidence).
- The connection between Θ_{E8} and the V_eff partition function requires
  proving that the UBT partition function on S¹_ψ equals Θ_{E8}.

---

## 6. What Would Constitute Progress

| Event | Impact |
|-------|--------|
| Q7 resolved: canonical identification φ: V → ℝ⁸ derived from UBT | Promote C-E8 to DERIVED |
| Θ_{E8} shown to equal the S[Θ] partition function | Major advance; connect to Route A |
| Chronofactor projection uniquely determined | Would make C9 claims precise |
| Explicit no-go for any of the above | Would kill E8 front cleanly |

---

## References

- `research_fronts/e8_torus_quantized_information/claims_status.md` — claim registry
- `research_fronts/e8_torus_quantized_information/e8_torus_chronofactor_paper.md` — extended paper
- `research_fronts/e8_front/no_go_results.md` — no-go results
- `research_fronts/e8_front/relevance_to_alpha.md` — E8 relevance to alpha
