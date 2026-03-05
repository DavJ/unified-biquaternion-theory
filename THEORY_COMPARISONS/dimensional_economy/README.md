# Dimensional Economy and Rigor: UBT vs Competing Theories

## Overview

This sandbox implements and computationally verifies the central claims in
the working document *"UBT vs. Competing Theories: Dimensional Economy and
Rigor"* (Ing. David Jaroš, March 2026).

**Core claim**: Unified Biquaternion Theory (UBT) derives General Relativity
and the Standard Model gauge structure from a single object Θ(x,τ) ∈ ℂ⊗ℍ
with complex time τ = t+iψ — using **fewer extra spatial dimensions than any
competing unified theory**, while maintaining full associativity.

---

## What This Sandbox Proves

### 1. ℂ⊗ℍ ≅ Mat(2,ℂ) — Algebra Isomorphism

The biquaternion algebra ℂ⊗ℍ is isomorphic to the 2×2 complex matrix algebra
Mat(2,ℂ).  The mapping is (standard faithful 2×2 representation):

```
1 ↦ I₂,   i ↦ iσ₂,   j ↦ iσ₁,   k ↦ iσ₃
```

The ordering i↦iσ₂, j↦iσ₁, k↦iσ₃ (rather than sequential σ₁,σ₂,σ₃) is
required so that ij = k holds: (iσ₂)(iσ₁) = -σ₂σ₁ = iσ₃ = k ✓.

Verified:
- `i² = j² = k² = ijk = -1` (all 7 quaternion relations)
- 8 basis elements {I₂, iσ₁, iσ₂, iσ₃, iI₂, -σ₁, -σ₂, -σ₃} are
  ℝ-linearly independent (rank = 8 over ℝ)

### 2. SU(2)_L from Left Action

Generators `T^a = -(i/2)σ^a` represent the left action of ℂ⊗ℍ on itself.
Proved by direct computation:

```
[T^a, T^b] = ε^{abc} T^c     (for all a, b ∈ {1,2,3})
```

All 9 commutator pairs verified symbolically.  Generators are traceless and
anti-Hermitian — no postulates required.

### 3. U(1)_Y from Right Action

Generator `Y = -i I₂` represents the right action Θ → e^{-iθ}Θ.

Proved:
- `exp(θ Y) = e^{-iθ} I₂` (correct finite transformation)
- `Y` anti-Hermitian
- Right action **commutes** with all SU(2)_L left actions

### 4. Associativity Advantage

ℂ⊗ℍ ≅ Mat(2,ℂ) is a **matrix algebra** — associativity is built in.
Proved symbolically: `(AB)C = A(BC)` for all A, B, C ∈ Mat(2,ℂ).

Furey's construction uses octonions 𝕆 (non-associative):
Classic counterexample: `e₁·(e₂·e₄) ≠ (e₁·e₂)·e₄` verified numerically.

---

## Dimensional Inventory

| Theory | Extra spatial dims | Internal algebra dims | Associative? |
|--------|-------------------|-----------------------|--------------|
| String Theory (M-theory) | 6–7 | — | ✅ |
| Kaluza-Klein | 1 | — | ✅ |
| Loop Quantum Gravity | 0 | — | ✅ |
| Furey (ℂ⊗𝕆) | 0 | 8 (octonions) | ❌ |
| Connes (NCG) | 0 | ~4 | ✅ |
| **UBT (ℂ⊗ℍ + complex time)** | **0** | **8** | **✅** |

UBT's one compact imaginary time direction ψ is **not** a spatial dimension —
it is the imaginary part of complex time τ = t+iψ.

---

## Implementation Structure

### `common/`
- `algebra.py` — Pauli matrices, commutator, anti-commutator, Levi-Civita ε

### `dim_economy_core/`
- `biquaternion_algebra.py` — ℂ⊗ℍ ≅ Mat(2,ℂ) isomorphism, basis, dimension table
- `su2l_generators.py` — SU(2)_L generators T^a and commutation relations
- `u1y_generator.py` — U(1)_Y generator Y and commutativity with SU(2)_L
- `associativity.py` — Mat(2,ℂ) associativity proof; octonion non-associativity

### `experiments/`
- `e01_algebra_isomorphism.py` — Interactive demo of ℂ⊗ℍ ≅ Mat(2,ℂ)
- `e02_su2l_derivation.py` — SU(2)_L and U(1)_Y derivation from automorphisms
- `e03_associativity_advantage.py` — UBT associativity vs. octonion failure

### `tests/`
- `test_algebra_isomorphism.py` — Pytest suite for the isomorphism
- `test_su2l_generators.py` — Pytest suite for SU(2)_L and U(1)_Y
- `test_associativity.py` — Pytest suite for associativity claims

---

## Usage

### Run Experiments

```bash
# From repository root:
python -m THEORY_COMPARISONS.dimensional_economy.experiments.e01_algebra_isomorphism
python -m THEORY_COMPARISONS.dimensional_economy.experiments.e02_su2l_derivation
python -m THEORY_COMPARISONS.dimensional_economy.experiments.e03_associativity_advantage
```

### Run Tests

```bash
pytest THEORY_COMPARISONS/dimensional_economy/tests/
```

**Expected runtime**: Each experiment < 5 seconds.  Full test suite < 30 seconds.

---

## Limitations and Disclaimers

This sandbox focuses on the **proved algebraic results**:

- SU(2)_L and U(1)_Y from ℂ⊗ℍ automorphisms (**proved**)
- ℂ⊗ℍ associativity (**proved**)

The following remain **open problems** (not implemented here):

| Problem | Status |
|---------|--------|
| SU(3)_c from ℂ⊗ℍ alone | Semi-empirical (Track B: octonionic extension) |
| Weinberg angle θ_W | Semi-empirical |
| Lepton mass ratios | Open — Hecke eigenvalue conjecture |
| Higgs mechanism | Open |
| B-constant (α numerically) | Open (OPEN PROBLEM A in DERIVATION_INDEX.md) |

See `DERIVATION_INDEX.md` and `STATUS_ALPHA.md` in the repository root for
the complete derivation status.

---

## Connection to Other UBT Documents

- `DERIVATION_INDEX.md` — Master index of all proved/open UBT results
- `consolidation_project/appendix_E2_SM_geometry.tex` — Formal proof of
  SU(2)_L and U(1)_Y from ℂ⊗ℍ (§1 isomorphism, §6 generators)
- `research_tracks/three_generations/` — Three fermion generations mechanism
- `STATUS_ALPHA.md` — Fine structure constant derivation status

---

## References

See `references.md` for detailed citations.

**Key sources**:
- Jaroš, D. (2026). *UBT vs. Competing Theories: Dimensional Economy and Rigor*
- `consolidation_project/appendix_E2_SM_geometry.tex` §1, §6
- Furey, C. (2016). Standard Model Physics from an Algebra? Cambridge PhD thesis.
- Connes, A. & Marcolli, M. (2008). *Noncommutative Geometry, Quantum Fields
  and Motives*. AMS.
- Dixon, G.M. (1994). *Division Algebras: Octonions, Quaternions, Complex Numbers
  and the Algebraic Design of Physics*. Kluwer.

---

## Status

**Current Status**: ✅ **SANDBOX COMPLETE**

- Core algebra modules implemented and verified
- All three experiments demonstrate key claims
- Full pytest suite passes
- Documentation explains each proved result and its limitations

---

*© 2026 Ing. David Jaroš — CC BY-NC-ND 4.0*
