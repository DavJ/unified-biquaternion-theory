> © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
>
> This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
> 4.0 International License (CC BY-NC-ND 4.0).

# L0 / L1 / L2 — Shape / Dimensionality Analysis

**Task**: `ubt_L0_L1_L2_full_audit`  
**Date**: 2026-05-05  
**Mode**: deep_repo_analysis  
**Epistemic mode**: strict

---

## Scope of This Document

This document tracks the input/output spaces and dimensionality at each
layer of the UBT L-architecture (System A: L0 → L1 → L2), based strictly
on what is defined in the repository.

Where code implementations exist, data shapes are extracted from code.
Where only theoretical definitions exist, spaces are described from LaTeX
and Markdown documents.

---

## Layer 0 — Fundamental Field Space

**Source**: `ARCHIVE/archive_legacy/tex/FORMAL_INVARIANT_EXTRACTION_LAYER0.tex` §2  
**type**: [doc]

### Input Space

The Layer-0 input is the configuration space of the biquaternionic field:

```
Θ: B^4 × C → B ⊗ S ⊗ G
```

| Component | Space | Real dimension |
|-----------|-------|----------------|
| Domain: spatial | B^4 = (C ⊗ H)^4 | 4 × 8 = 32 real |
| Domain: time | C = {τ = t + iψ} | 2 real (t, ψ) |
| Codomain: biquaternion | B = C ⊗ H | 8 real |
| Codomain: spinor | S = Spin(3,1) spinor | 4 complex = 8 real |
| Codomain: gauge | G = SU(3)×SU(2)×U(1) | (8+3+1)=12 generators |

**Total field configuration**: infinite-dimensional function space
(smooth sections of the fiber bundle over B^4 × C).

### Output Space

The Layer-0 produces five real-valued invariants:

| Invariant | Output type | Dimension |
|-----------|-------------|-----------|
| I_spec[Θ] = Tr[f(D²/Λ²)] | Real number | ℝ¹ |
| I_wind[Θ] = n_wind | Integer | ℤ |
| I_phase[Θ] = K_ψ | Integer | ℤ |
| I_curv[Θ] = ∫dμ R | Real number | ℝ¹ |
| I_action[Θ] = S[Θ] | Real number | ℝ¹ |

**Transformation type**: integral functionals (linear in f for spectral action;
nonlinear for action functional due to V(Θ) term).

---

## Layer 1 — Emergent Physics

**Source**: `ARCHIVE/archive_legacy/tex/FORMAL_INVARIANT_EXTRACTION_LAYER0.tex` §1.1;  
`docs/architecture/LAYERS.md` §Layer 1  
**type**: [doc]

### Input Space

The input to Layer 1 is the same field Θ and its Layer-0 invariants.

In the language of `docs/architecture/LAYERS.md`, Layer 1 operates on:
- The biquaternionic field structure ℂ⊗ℍ (8-dimensional real algebra)
- The complex time manifold τ = t + iψ ∈ ℂ
- The field equation ∇†∇Θ = κ𝒯 (defining the dynamics)

### Output Space

Layer 1 produces:
- Metric tensor G_μν derived from Θ (dimension: 4×4 symmetric tensor field)
- GR recovery in real limit: R_μν - ½g_μν R = 8πG T_μν
- SM gauge group SU(3)×SU(2)×U(1) from Aut(ℂ⊗ℍ)
- One-loop effective potential V_eff(n) = n² - B·n·ln n (scalar function of integer n)
- One-loop coefficient B₀ = 8π (real number, from N_eff = 12 modes)

**Transformation type**:
- GR limit: nonlinear (metric from field via variational principle)
- Gauge group: algebraic (automorphism group of ℂ⊗ℍ)
- One-loop V_eff: perturbative expansion (loop correction)

**Dimensional reduction (key example)**:

The biquaternion algebra B = C ⊗ H decomposes under SU(2) as:
```
B = 1 ⊕ 3 ⊕ 3̄ ⊕ 1   (dimensions: 1+3+3+1 = 8 ✓)
```
[code-derived from `test_su2_decomposition_1330()` in
`research_tracks/alpha/layer2_coding_alpha_scan.py`]

The N_eff = 12 counting is:
```
N_eff = dim_ℝ(Im ℍ) × N_helicity × N_charge = 3 × 2 × 2 = 12
```
[doc-derived from `ALPHA_PROGRESS_REPORT.md` §2.1]

---

## Layer 2 — Discrete/Coding Layer

**Source**: `docs/architecture/LAYERS.md` §Layer 2;
`research_tracks/gray_transport_layer/gray_vs_hamming_layer2.md`;
`research_tracks/alpha/layer2_coding_alpha_scan.py`  
**type**: [doc + code]

### Sub-layer L2S (Hamming State Layer)

**Input**: 8-symbol phase blocks, each symbol ∈ {0,1} (binary alphabet)

```
Input space: {0,1}^8  (256 possible blocks)
```

**Output**: Syndrome vector s = H·block^T ∈ {0,1}^4; P₀ (scalar ∈ [0,1])

```
Output space: {0,1}^4 (16 possible syndromes)
P₀ ∈ [0,1] (fraction of syndrome-zero blocks)
```

**Transformation type**: linear over GF(2)

```
P_check: {0,1}^8 → {0,1}^4
block → H·block^T  (parity check matrix H)
```

Dimension flow: 8 bits → 4 syndrome bits → scalar P₀

**Code parameters** [code-derived from `generate_hamming_844_codewords()`]:
```
n = 8 (block length)
k = 4 (message bits)
d_min = 4 (minimum Hamming distance)
|codewords| = 2^k = 16
```

### Sub-layer L2T (Gray Transport Layer)

**Input**: Sequence of phase symbols s₁, s₂, ..., s_m where sᵢ ∈ {0, ..., N-1}

```
Input space: {0,...,N-1}^m  (sequences of m symbols, alphabet size N)
Default N = 16 (4-bit) or N = 256 (8-bit)
```

**Input derivation from CMB phases** [code-derived from `phases_to_symbols()` and `alm_to_symbols()`]:
```
Phase domain: [-π, π)  (real phases of complex a_lm coefficients)
Symbol: s = floor(N / (2π) × (phase + π)) ∈ {0,...,N-1}
```

**Output**: A_gray (scalar ∈ [0,1])

```
A_gray = (1/(m-1)) Σᵢ 1[s_{i+1} is Gray-adjacent to sᵢ]
Expected null (i.i.d.): 2/N
```

**Transformation type**: 
- Phase → symbol: deterministic, nonlinear (floor/discretization)
- Symbol → A_gray: aggregation (mean of binary adjacency indicators)

Dimension flow: m complex a_lm → m real phases → m symbols → 1 scalar A_gray

**Gray rank table** [code-derived from `build_gray_order_table(N)`]:
```
Input: integer n ∈ {0,...,N-1}
Gray code: G(n) = n XOR (n >> 1)
gray_rank[G(n)] = n   (inverse lookup)
```

---

## Layer 2 — Winding Number Scan (Layer 2 in System A)

**Input**: Integer winding number n ∈ primes ∩ [101, 199]  
**Output**: V_eff(n) = n² - B·n·ln n (real number)  
**Transformation type**: deterministic analytic function  
**Dimension flow**: ℤ → ℝ (integer → real scalar)

This is the Layer-2 numerical procedure for the α derivation route.
[doc-derived from `docs/INVARIANT_EXTRACTION_SUMMARY.md` and
`ALPHA_PROGRESS_REPORT.md`]

---

## Loop-Order System B — Dimension Flow

**Source**: `docs/REPO_LAYERS.md` §Status Vocabulary  
**type**: [doc]

In System B (perturbative loop order):

| Label | Physical content | Space |
|-------|-----------------|-------|
| [L0] | Tree-level biquaternionic algebra | Algebraic identity (dimension-free) |
| [L1] | One-loop vacuum polarization | Real scalar (B₀ = 8π, N_eff = 12) |
| [L2] | Higher-loop / non-perturbative | Not yet computed in repo |

No dimensional transformation L0 → L1 → L2 is defined in code for System B.
The labels tag derivation status, not executable transformations.

---

## Summary Table

| Layer (System A) | Input | Output | Dim change | Type |
|-----------------|-------|--------|------------|------|
| L0 | Θ ∈ (smooth sections of fiber bundle) | 5 real invariants | ∞-dim → 5 scalars | Integral functional |
| L1 | Θ, L0 invariants | G_μν, gauge group, V_eff | ∞-dim → tensor field + algebra | Variational + perturbative |
| L2S | 8-bit block ∈ {0,1}^8 | Syndrome ∈ {0,1}^4, P₀ ∈ ℝ | 8 → 4 → 1 | Linear over GF(2) |
| L2T | m phase symbols ∈ {0,...,N-1}^m | A_gray ∈ [0,1] | m → 1 | Aggregation |
| L2 (winding) | n ∈ ℤ | V_eff(n) ∈ ℝ | 1 → 1 | Analytic scalar function |

---

*Generated by ubt_L0_L1_L2_full_audit, Step 3.*
