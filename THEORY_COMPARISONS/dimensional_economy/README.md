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

### 5. Three Fermion Generations from ψ-Taylor Modes

UBT identifies the three generations with the lowest ψ-Taylor modes:
Θ(x,t,ψ) = Σₙ ψⁿ Θₙ(x,t).

Three theorems proved (see `st3_complex_time_generations.tex`):

**Theorem 1 — Independence** (Proved [L0]):
The ψ-modes Θ₀, Θ₁, Θ₂, … are kinematically independent — free initial data
in the ψ-direction.  No algebraic relation constrains them.

**Theorem 2 — SU(3) Quantum Numbers** (Proved [L0]):
For U ∈ SU(3) independent of ψ: (UΘ)_n = U·Θₙ.
Every mode transforms in the **same SU(3) representation** as Θ.

**Theorem 3 — ψ-Parity Selection Rule** (Proved [L0]):
Under ψ → -ψ: Θₙ → (-1)ⁿ Θₙ.
ψ-parity forbids mixing between even (Θ₀, Θ₂, …) and odd (Θ₁, Θ₃, …) modes.

Generation identification Θ₀↔e, Θ₁↔μ, Θ₂↔τ is a conjecture; mass ratios open.

### 6. Fine Structure Constant: Proved Components

| Result | Status |
|--------|--------|
| ψ-circle compactification | **Proved [L0]** — unitarity + gauge consistency |
| Dirac quantisation condition | **Proved [L0]** — single-valuedness of Θ |
| N_eff = 12 = 3×2×2 | **Proved [L0]** — SM gauge degrees of freedom |
| B₀ = 2π·N_eff/3 = 8π ≈ 25.13 | **Proved [L1]** — one-loop baseline |
| B_base = N_eff^{3/2} = 41.57 | **Open Hard Problem A** — no derivation |
| α⁻¹ = 137.036 | **Semi-empirical** — B_base required |

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
- `three_generations.py` — ψ-mode independence (Thm 1), SU(3) quantum numbers (Thm 2), ψ-parity (Thm 3)
- `fine_structure.py` — N_eff=12 counting, B₀=2π·N_eff/3, Dirac quantisation, proved summary

### `experiments/`
- `e01_algebra_isomorphism.py` — Interactive demo of ℂ⊗ℍ ≅ Mat(2,ℂ)
- `e02_su2l_derivation.py` — SU(2)_L and U(1)_Y derivation from automorphisms
- `e03_associativity_advantage.py` — UBT associativity vs. octonion failure
- `e04_three_generations.py` — Three fermion generations ψ-mode theorems
- `e05_fine_structure_neff.py` — N_eff=12, B₀, and honest open problems

### `tests/`
- `test_algebra_isomorphism.py` — Pytest suite for the isomorphism
- `test_su2l_generators.py` — Pytest suite for SU(2)_L and U(1)_Y
- `test_associativity.py` — Pytest suite for associativity claims
- `test_three_generations.py` — Pytest suite for ψ-mode theorems
- `test_fine_structure.py` — Pytest suite for N_eff and B₀

---

## Usage

### Run Experiments

```bash
# From repository root:
python -m THEORY_COMPARISONS.dimensional_economy.experiments.e01_algebra_isomorphism
python -m THEORY_COMPARISONS.dimensional_economy.experiments.e02_su2l_derivation
python -m THEORY_COMPARISONS.dimensional_economy.experiments.e03_associativity_advantage
python -m THEORY_COMPARISONS.dimensional_economy.experiments.e04_three_generations
python -m THEORY_COMPARISONS.dimensional_economy.experiments.e05_fine_structure_neff
```

### Run Tests

```bash
pytest THEORY_COMPARISONS/dimensional_economy/tests/
```

**Expected runtime**: Each experiment < 5 seconds.  Full test suite < 5 seconds (106 tests).

---

## Limitations and Disclaimers

This sandbox focuses on the computationally verifiable **proved results**.
The following are implemented and tested:

- ℂ⊗ℍ ≅ Mat(2,ℂ) (algebra) — **proved**
- SU(2)_L and U(1)_Y from automorphisms — **proved**
- ℂ⊗ℍ associativity vs. octonion non-associativity — **proved**
- ψ-mode independence (Theorem 1) — **proved**
- SU(3) quantum numbers preserved (Theorem 2) — **proved**
- ψ-parity selection rule (Theorem 3) — **proved**
- N_eff = 12 = 3×2×2 counting — **proved**
- B₀ = 2π·N_eff/3 = 8π ≈ 25.13 (one-loop) — **proved**

The following remain **open problems** (documented but not proved here):

| Problem | Status |
|---------|--------|
| SU(3)_c from ℂ⊗ℍ alone | Semi-empirical (Track B: octonionic extension) |
| Weinberg angle θ_W | Semi-empirical |
| Lepton mass ratios | Open — Hecke eigenvalue conjecture |
| Higgs mechanism | Open |
| B_base = N_eff^{3/2} | **OPEN PROBLEM A** — DERIVATION_INDEX.md |
| α⁻¹ = 137.036 (full) | Semi-empirical |
| CKM/PMNS mixing matrices | Open |

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

- All five proved-results areas from the problem statement implemented
- 106 tests passing
- Documentation explains each proved result and its limitations
- Open problems honestly documented

---

*© 2026 Ing. David Jaroš — CC BY-NC-ND 4.0*
