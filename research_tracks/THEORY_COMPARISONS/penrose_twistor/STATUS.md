# UBT ↔ Twistor Bridge: Formal Status Register

**Module**: `THEORY_COMPARISONS/penrose_twistor/`  
**Date**: 2026-03-11  
**Author**: UBT Research Team  
**Hard rule**: Do NOT upgrade a result from a lower status tier to a higher one without
providing an explicit isomorphism proof or peer-reviewed reference.

---

## Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ **proved** | Algebraically or computationally verified with explicit proof |
| 🔬 **computationally_verified** | Numerically/symbolically checked; proof sketch present |
| 🔶 **indicated** | Consistent with, but not classified; requires more structure |
| ❓ **open** | Not resolved; exact answer unknown |
| ❌ **dead_end** | Shown not to hold; kept for record |

---

## Section 1 — Proved

These results have explicit algebraic proofs or exhaustive symbolic verifications.

### 1.1 Sigma matrices derived from UBT biquaternion basis

**Claim**: The 2×2 complex matrices {σ₀, σ₁, σ₂, σ₃} satisfying det(x^μ σ_μ) = Minkowski
interval can be derived from the UBT biquaternion basis {**1**, **i**, **j**, **k**} without
importing Pauli matrices externally.

**Status**: ✅ **proved**  
**Proof file**: `twistor_core/ubt_generators.py` — `get_biquaternion_basis_2x2()`,
`get_sigma_matrices()`, `verify_clifford_relations()`, `verify_determinant_minkowski_form()`  
**Test coverage**: `tests/test_ubt_generators_clifford.py` (all 15 tests pass)  
**Assumptions**: Standard 2×2 complex matrix representation; quaternion basis element
ordering fixed as {**1**, σ₁, σ₂, σ₃} with $\sigma_i^2 = I$.

---

### 1.2 det(X) = Minkowski interval

**Claim**: For X = x^μ σ_μ (Hermitian 2×2 matrix), det(X) = (x⁰)² − (x¹)² − (x²)² − (x³)²

**Status**: ✅ **proved** (symbolic)  
**Proof file**: `twistor_core/ubt_generators.py` — `verify_determinant_minkowski_form()`  
**Test coverage**: `tests/test_ubt_generators_clifford.py::test_det_equals_minkowski_interval`

---

### 1.3 Bijection x ↔ X is well-defined and invertible

**Claim**: The map Minkowski₄ → Herm₂(ℂ) defined by x ↦ X = x^μ σ_μ is a ℝ-linear
bijection with explicit inverse X ↦ x^μ = ½ Tr(σ^μ X).

**Status**: ✅ **proved**  
**Proof file**: `twistor_core/minkowski_spinor.py` — `x_to_X()`, `X_to_x()`  
**Test coverage**: `tests/test_spinor_roundtrip.py` (roundtrip: x → X → x, generic and null vectors)

---

### 1.4 Null vectors ↔ rank-1 Hermitian matrices

**Claim**: x^μ is null (s² = 0) if and only if X = x^μ σ_μ has rank 1 (det X = 0).

**Status**: ✅ **proved**  
**Proof file**: `twistor_core/minkowski_spinor.py`  
**Test coverage**: `tests/test_light_cone.py`

---

### 1.5 Incidence relation ω^A = i X^{AA'} π_{A'} is flat-space consistent

**Claim**: Given X ∈ Herm₂(ℂ) and π_{A'} ≠ 0, the assignment ω^A = iXπ defines a
valid twistor Z^α = (ω, π) ∈ ℂ⁴ that encodes the spacetime point via the standard
flat-space incidence relation.

**Status**: ✅ **proved** (flat, constant X)  
**Scope**: **flat Minkowski space only** — curvature corrections are not included.  
**What is NOT preserved**: The imaginary time coordinate ψ in τ = t + iψ is not
carried through the incidence relation (see Section 3 — Open Questions).  
**Failure modes**: π = 0 (degenerate twistor); non-Hermitian X (not a real spacetime point).  
**Proof file**: `twistor_core/twistor.py` — `Twistor.from_X_and_pi()`  
**Test coverage**: `tests/test_incidence.py`

---

### 1.6 SU(2,2) Hermitian form H is well-defined and preserved

**Claim**: H = [[0, I₂], [I₂, 0]] defines an indefinite Hermitian form of signature (2,2)
on ℂ⁴, and the group SU(2,2) = {U ∈ GL(4,ℂ) : U† H U = H, det U = 1} is non-trivial.

**Status**: ✅ **proved**  
**Proof file**: `twistor_core/su22.py` — `get_su22_hermitian_form()`, `is_su22()`  
**Test coverage**: `tests/test_su22.py`

---

### 1.7 SU(2,2) action on twistor space

**Claim**: Z ↦ UZ (matrix multiplication) for U ∈ SU(2,2) preserves the indefinite inner
product ⟨Z₁, Z₂⟩_H = Z₁† H Z₂.

**Status**: ✅ **proved**  
**Test coverage**: `tests/test_su22_conformal.py`

---

## Section 2 — Computationally Verified

These results have been checked numerically or by symbolic computation, but a fully
self-contained analytic proof or peer-reviewed classification is not yet in place.

### 2.1 Conformal (Möbius) action on X-space

**Claim**: For block-decomposition U = [[A, B], [C, D]] ∈ SU(2,2), the formula
X' = (AX + B)(CX + D)⁻¹ gives a well-defined transformation on Hermitian 2×2
matrices, corresponding to a conformal Möbius map on Minkowski spacetime.

**Status**: 🔬 **computationally_verified** (numerical, multiple random U, X)  
**Preserved form**: det(X) (light-cone structure) preserved up to a positive real conformal factor.  
**Lorentz vs full conformal**: The Lorentz subgroup SO(1,3) ≅ SL(2,ℂ) acts as a
linear map X ↦ L X L†; the full conformal group action is non-linear (fractional linear).  
**Caveat**: Degenerate cases (CX + D non-invertible) correspond to conformal infinity
and are not covered by this formula.  
**Proof file**: `twistor_core/conformal.py` — `transform_X()`  
**Experiment**: `experiments/e06_su22_conformal_actions.py`  
**Test coverage**: `tests/test_su22_conformal.py`

---

### 2.2 UBT generator closure yields dimension-15 algebra

**Claim**: Starting from 8 UBT-side generators embedded in 4×4 matrices, iterative
commutator closure converges to a 15-dimensional Lie algebra with non-degenerate
Killing form.

**Status**: 🔬 **computationally_verified** (symbolic with sympy)  
**Dimension growth**: [8, 14, 15, 15] (converged)  
**Killing form signature**: (8, 7, 0) — non-compact, rank 15, semisimple.  
**Proof file**: `twistor_core/lie_audit.py`; `experiments/e08_lie_algebra_audit.py`  
**Output**: `reports/e08_commutator_table.csv`, `reports/e08_summary.md`  
**Test coverage**: `tests/test_e08_lie_algebra_audit.py`

---

## Section 3 — Indicated but Not Classified

These are results that are numerically consistent with a claim but whose full classification
requires additional structure (explicit isomorphism, Cartan invariant match, etc.).

### 3.1 UBT-generated algebra is a strong candidate for su(2,2)

**Claim**: The 15-dimensional Lie algebra with Killing signature (8, 7, 0) derived from
UBT generators (Section 2.2) is isomorphic to the real Lie algebra su(2,2).

**Status**: 🔶 **indicated** — NOT proved  
**Evidence for**:
- Dimension matches: 15 = dim su(2,2) ✓
- Non-compact signature: (8, 7, 0) consistent with su(2,2) ✓
- Semisimple: Yes ✓
- Real form of sl(4,ℂ): consistent ✓

**Missing for a proof**:
- Explicit generator-by-generator isomorphism to a standard su(2,2) basis
- Cartan decomposition and verification of root system (type A₃ real form)
- Comparison of Dynkin diagram against known non-compact real forms of A₃
- Alternatively: a rank-2 Cartan subalgebra check with the correct eigenvalues

**Upgrade criterion**: Exhibit a Lie algebra isomorphism φ: (our algebra) → su(2,2)
satisfying φ([X,Y]) = [φ(X), φ(Y)] for all generators.

**⚠ Do not write "proved" or "exact recovery" for this result.**

---

## Section 4 — Open Questions

### 4.1 Mapping of UBT phase ψ (complex time) to twistor geometry

**Status**: ❓ **open**  
**Description**: In UBT, time is complex: τ = t + iψ.  In twistor theory, complexified
spacetime arises from choosing ω^A, π_{A'} ∈ ℂ without reality constraints.  The question
is: what is the precise geometric role of ψ in twistor (or spinor-conformal) geometry?

**Candidates investigated** (see `tau_phase_mapping.md`):
- ψ as an internal U(1) phase in the field Θ
- ψ as a fiber coordinate over twistor space
- ψ as a projective phase (Z ~ λZ with |λ| ≠ 1)
- ψ as an extra circle coordinate over complexified spacetime

**None of these are confirmed.** See `tau_phase_mapping.md` for details.

---

### 4.2 Extension to curved spacetime

**Status**: ❓ **open**  
**Description**: This module works in flat Minkowski space.  Penrose's nonlinear graviton
construction extends twistors to anti-self-dual (ASD) vacuum metrics.  Whether and how
UBT's emergent curved metric admits a twistor-compatible structure is unknown.

**See**: `curved_bridge_todo.md` for investigation plan.

---

### 4.3 Conformal invariance of UBT field equations

**Status**: ❓ **open** (expected negative)  
**Description**: Twistor theory is naturally conformal; UBT field equations involve mass
terms and a running fine-structure constant, both of which break strict conformal
invariance.  Whether a conformal limit exists and whether it maps to a twistor field theory
is open.

---

## Section 5 — Dead Ends

*(None recorded yet.  Will be populated as negative results accumulate.)*

---

## Change Log

| Date | Change | Author |
|------|--------|--------|
| 2026-03-11 | Initial STATUS.md created from sandbox results | UBT Research Team |
