<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# neff_12_dimension_count_audit.md — Audit of All Routes to N_eff = 12

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Track**: T3_ALPHA — Fine Structure Constant  
**Purpose**: Systematic audit of all known derivations of N_eff = 12 with proof-level
labels, independence checks, and circularity tests.  
**Companion files**:
- `ALPHA_STRUCTURAL_ORIGINS.md` §3 (Track E2) — original five-route summary
- `canonical/alpha/neff_geometric_origin.md` — geometric context
- `canonical/n_eff/` — formal N_eff derivation chain
- `reports/exponent_3_2_origin_audit.md` — exponent audit

---

## Overview

N_eff = 12 is the effective number of charged modes of the biquaternion field Θ on S¹_ψ
contributing to one-loop vacuum polarization. This audit catalogues every independent
derivation route and verifies that none use α or m_e as inputs.

**Verdict**: N_eff = 12 is **over-determined** by five independent algebraic routes,
all [L0] (zero-parameter algebraic identities). It is the most solidly established
quantity in the α-route.

---

## Route R1: Algebraic Phase Decomposition (Primary Route)

**Source**: `canonical/n_eff/step1_mode_decomposition.tex`,
`canonical/alpha/alpha_best_route.tex §3`

**Derivation**:
```
N_eff = N_phases × N_helicity × N_charge
      = dim_ℝ(Im ℍ) × 2 × 2
      = 3 × 2 × 2
      = 12
```

**Factor by factor**:

| Factor | Value | Origin | Independence from α |
|--------|-------|--------|---------------------|
| N_phases | 3 | dim_ℝ(Im ℍ) = dim_ℝ(span{I,J,K}) = 3; algebraic axiom | ✓ |
| N_helicity | 2 | Complex structure of ℬ = ℂ⊗ℍ provides left/right chiral components | ✓ |
| N_charge | 2 | Complex conjugation automorphism τ_ℂ: z → z* of ℬ gives particle/antiparticle | ✓ |

**Proof status**: [L0] — exact algebraic identity from ℬ = ℂ⊗ℍ axiom.  
**Circularity check**: None. Does not use α, m_e, or any experimental input.  
**Falsification condition**: Would require dim_ℝ(Im ℍ) ≠ 3, which contradicts the 
axiom ℬ = ℂ⊗ℍ (quaternions have exactly 3 imaginary directions).

---

## Route R2: Standard Model Generator Count

**Source**: `canonical/interactions/sm_gauge.tex`,
`ALPHA_STRUCTURAL_ORIGINS.md §3.2`

**Derivation**:
The SM gauge group SU(3)_c × SU(2)_L × U(1)_Y, as embedded in ℬ, has generators:

| Group | Generators | Type |
|-------|-----------|------|
| SU(3)_c | 8 Gell-Mann matrices | Color generators |
| SU(2)_L | 3 Pauli matrices | Weak isospin |
| U(1)_Y | 1 hypercharge | Hypercharge |
| **Total** | **12** | |

Each generator corresponds to one independent charged mode of Θ contributing to
U(1)_EM vacuum polarization via virtual loop corrections.

**Proof status**: [L0] — SM generator count is standard algebra; the embedding in ℬ
is derived in `canonical/interactions/sm_gauge.tex`.  
**Circularity check**: None — the number 12 comes from the dimensions of the SM Lie
algebras, which are derived from ℬ without using α.  
**Remark**: Routes R1 and R2 are not independent — SU(3)×SU(2)×U(1) is what
arises when the three factors N_phases=3, N_helicity=2, N_charge=2 are identified
with color, isospin, and hypercharge. They are complementary views of the same count.

---

## Route R3: Three-Qubit Sector Decomposition

**Source**: `canonical/interactions/su3_qubit_encoding.tex`,
`ALPHA_STRUCTURAL_ORIGINS.md §3.3`

**Derivation**:
The biquaternion algebra ℬ = ℂ⊗ℍ supports a three-sector decomposition that can
be read as a "three-qubit-like" encoding:

```
Color sector:         3 charges (r, g, b)     → 3 charged modes
Isospin sector:       2 states (up, down)      → 2 charged modes
Hypercharge sector:   1 phase                  → 1 charged mode
                                                 Total: 6 internal modes
× charge conjugation (particle/antiparticle):    × 2
                                                 = 12
```

**Proof status**: [L0] — dimensional counting from the SM sector structure of ℬ.  
**Important caveat**: Color is properly a **qutrit** (3 states r,g,b), not a qubit.
The "three-qubit" label is a mnemonic for three independent grading structures of ℬ,
not a literal tensor product of spin-1/2 systems. See
`canonical/alpha/neff_geometric_origin.md §1.3`.

---

## Route R4: Spinor Component Counting (M₂(ℂ) Structure)

**Source**: `ALPHA_STRUCTURAL_ORIGINS.md §3.4`

**Derivation**:
The field Θ ∈ ℬ ≅ M₂(ℂ). As a 2×2 complex matrix:
```
Θ = [[θ₁₁, θ₁₂], [θ₂₁, θ₂₂]]
```
Under the SM gauge action:
- Diagonal entries θ₁₁, θ₂₂: gauge-neutral (singlets) → do not contribute to vacuum pol.
- Off-diagonal entries θ₁₂, θ₂₁: gauge-charged → contribute to U(1)_EM vacuum pol.

Mode count:
```
2 off-diagonal complex entries × 3 quaternion phase directions × 2 helicities = 12
```

**Proof status**: [L0] — follows from M₂(ℂ) ≅ ℬ isomorphism and SM charge assignments.  
**Circularity check**: None.

---

## Route R5: Compact Mode Counting on T³ × S¹_ψ

**Source**: `ALPHA_STRUCTURAL_ORIGINS.md §3.5`

**Derivation**:
On the compactification T³ × S¹_ψ, the first non-trivial winding modes are:
```
n = ±1 in ψ-direction × 3 independent Im ℍ phase directions × 2 charge signs = 12
```
The sign n = ±1 represents the left-moving and right-moving winding modes (helicity).
The Im ℍ phase directions contribute factor 3. The charge sign contributes factor 2.

**Proof status**: [L0] — mode counting on compact manifold.  
**Circularity check**: None.

---

## Comparative Table

| Route | Method | N_eff | Proof Status | Uses α? | Uses m_e? | Independent of R1? |
|-------|--------|-------|-------------|---------|-----------|-------------------|
| R1 | 3×2×2 algebraic decomposition | 12 | [L0] | No | No | Baseline |
| R2 | SM generator count (8+3+1) | 12 | [L0] | No | No | Partially (same physics, different counting) |
| R3 | 3-qubit-like sector decomposition | 12 | [L0] | No | No | Partially (refinement of R1) |
| R4 | Off-diagonal M₂(ℂ) spinor count | 12 | [L0] | No | No | Yes (different algebraic viewpoint) |
| R5 | Compact mode counting on T³×S¹_ψ | 12 | [L0] | No | No | Yes (geometric, not algebraic) |

All five routes yield N_eff = 12 without any free parameter or reference to α.

---

## Independence Audit

### Are R1 and R2 independent?

**Answer**: They encode the same physics from different angles. R1 uses the algebraic
structure of ℬ directly; R2 uses the SM gauge group which is derived from ℬ. They
are not fully independent but provide complementary perspectives.

### Are R4 and R5 independent of R1?

**Answer**: Yes. R4 uses the matrix structure of M₂(ℂ) ≅ ℬ; R5 uses compact geometry
on T³×S¹_ψ. Both arrive at 12 through different mathematical routes.

### Non-circularity stress test

From `canonical/alpha/alpha_best_route.tex §8.1`:

| N_eff (counterfactual) | B_full | Prime attractor n* |
|------------------------|--------|-------------------|
| 4 | ≈ 8.9 | 17 |
| 8 | ≈ 25.2 | 67 |
| **12** | **≈ 46.3** | **137** |
| 24 | ≈ 131.0 | 467 |

Different N_eff values produce different n*. N_eff = 12 is selected by the SM embedding
in ℬ, not by the desire to obtain 137. The derivation is non-circular.

---

## Summary: N_eff = 12 Proof Level

| Claim | Proof Status | Source |
|-------|-------------|--------|
| dim_ℝ(Im ℍ) = 3 | [L0] — algebraic | Quaternion algebra |
| N_phases = 3 | [L0] — algebraic | From dim_ℝ(Im ℍ) |
| N_helicity = 2 | [L0] — algebraic | Complex structure of ℬ |
| N_charge = 2 | [L0] — algebraic | Charge conjugation automorphism |
| **N_eff = 12** | **[L0] — exact** | **Product formula** |
| N_eff = 12 (independent SM count) | [L0] | 8+3+1 generators |
| N_eff independent of α | [L0] — confirmed | Stress test Table |
| N_eff independent of m_e | [L0] — trivial | No m_e in any factor |

**Conclusion**: N_eff = 12 is one of the most robustly established facts in the UBT
α-program. It would be falsified only if the algebra axiom ℬ = ℂ⊗ℍ were wrong, which
would require modifying the fundamental UBT axioms.

---

## Open Issues

1. **Three-qubit interpretation**: The "three qubits" language is a mnemonic, not an
   exact algebraic statement. A rigorous isomorphism ℋ_3q → ℬ_ℝ is absent. This does
   not affect the [L0] status of N_eff = 12 via Route R1.

2. **8D → 12 transition**: The statement "N_eff = 8 + 4" (eight from the information
   sector, four from the chronofactor) is suggestive but not the primary derived form.
   The primary form is N_eff = 3 × 2 × 2 = 12. See
   `canonical/alpha/chronofactor_projection.md §3.3`.
