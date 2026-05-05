> © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
>
> This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
> 4.0 International License (CC BY-NC-ND 4.0).

# L0 / L1 / L2 — Mathematical Formalization

**Task**: `ubt_L0_L1_L2_full_audit`  
**Date**: 2026-05-05  
**Mode**: deep_repo_analysis  
**Epistemic mode**: strict

---

## Scope

This document converts the repository definitions of L0, L1, L2 into formal
mathematical operator notation. All expressions are derived strictly from
repository content. Inferred or speculative content is labeled `[inferred]`.

---

## System A — Architecture Hierarchy

### L0: Fundamental Field Layer

**Source**: `ARCHIVE/archive_legacy/tex/FORMAL_INVARIANT_EXTRACTION_LAYER0.tex` §2  
**type**: [doc]

**Domain**:

```
Field configuration space:
  C_Θ = { Θ: B^4 × C → B ⊗ S ⊗ G | Θ smooth }

where:
  B  = C ⊗ H  (biquaternion algebra, dim_ℝ = 8)
  B^4 = (C ⊗ H)^4  (biquaternionic 4-manifold)
  C  = {τ = t + iψ | t,ψ ∈ R}  (complex time)
  S  = Spin(3,1) spinor bundle
  G  = SU(3) × SU(2) × U(1) gauge fiber
```

**L0 action** (Definition 2.3 in tex):

```
L0: C_Θ → R

L0(Θ) = S[Θ] = S_kin[Θ] + S_pot[Θ] + S_gauge[Θ]

where:
  S_kin[Θ]   = (1/2) ∫_{M×C} dμ G^{μν} Tr[(∇_μΘ)†(∇_νΘ)]
  S_pot[Θ]   = -∫_{M×C} dμ (λ/4)(⟨Θ,Θ⟩ - v²)²
  S_gauge[Θ] = -(1/4) ∫_{M×C} dμ Tr[F_{μν}F^{μν}]
```

This is a nonlinear functional due to the quartic potential term.

**L0 invariants** — five projection maps:

```
I_spec  : C_Θ → R    Θ ↦ Tr[f(D²/Λ²)]
I_wind  : C_Θ → Z    Θ ↦ n_wind  (homotopy class π₃(G/H))
I_phase : C_Θ → Z    Θ ↦ K_ψ     (imaginary time periodicity)
I_curv  : C_Θ → R    Θ ↦ ∫dμ R(q,τ)
I_action: C_Θ → R    Θ ↦ S[Θ]
```

**Operator classification**:
- `I_spec`, `I_curv`, `I_action`: **nonlinear** integral functionals
- `I_wind`, `I_phase`: **topological** (homotopy invariants, discrete-valued)
- None of the L0 maps is a simple linear projection

---

### L1: Emergent Metric / Physics Layer

**Source**: `ARCHIVE/archive_legacy/tex/FORMAL_INVARIANT_EXTRACTION_LAYER0.tex` §1.1;
`docs/architecture/LAYERS.md` §Layer 1; `ALPHA_PROGRESS_REPORT.md` §2.2–2.4  
**type**: [doc]

**L1 maps**:

#### L1a — Metric emergence

```
G_μν: C_Θ → Sym²(T*M)   (space of symmetric 2-tensors)
Θ ↦ G_μν derived from Θ via variational principle
```

The precise form of this map is not explicitly given as a closed-form
expression in the repository. The document states that G_μν is "derived
from Θ"; full derivation is in canonical/ appendices. [doc-derived]

#### L1b — GR recovery (real limit)

In the limit ψ → 0 (real time):

```
L1_GR: G_μν ↦ g_μν  (4D Lorentzian metric)

EFE: R_μν - (1/2)g_μν R = 8πG T_μν
```

This is a **limit map** (projection to ψ = 0 subspace), **linear** at
the level of the metric tensor.

#### L1c — One-loop effective potential

**Source**: `ALPHA_PROGRESS_REPORT.md` §2.3 [doc]

```
V_eff: Z → R

V_eff(n) = n² - B·n·ln n
```

This is a **nonlinear** scalar function of integer n. The coefficient B is:

```
B = B₀ + B_higher   (B₀ = 8π, one-loop baseline [L1])
B₀ = 2π N_eff / 3 = 2π × 12 / 3 = 8π
```

#### L1d — Stationarity condition

```
dV_eff/dn = 0  ⟺  2n - B·(1 + ln n) = 0  ⟺  n* ≈ B/2 · (1 + ln n*)
```

This is the L1 equation that selects the attractor winding number n*.

**Operator classification for L1**:
- Metric emergence: nonlinear (variational)
- GR limit: projection (linear restriction to ψ = 0)
- V_eff: nonlinear polynomial-logarithmic scalar function
- Stationarity: transcendental equation (fixed-point condition)

---

### L2: Coding / Discretization Layer

**Source**: `research_tracks/alpha/layer2_coding_alpha_scan.py`;
`research_tracks/gray_transport_layer/gray_vs_hamming_layer2.md`;
`docs/architecture/LAYERS.md` §Layer 2  
**type**: [code + doc]

#### L2S — Hamming State Layer

**Input space**: {0,1}^8 (8-bit binary blocks)

```
H_check: {0,1}^8 → {0,1}^4    (parity check)
block ↦ H·block^T   (mod 2, linear over GF(2))

where H is the 4×8 parity check matrix.
```

**Physical state selector**:

```
Π_L2S: {0,1}^8 → {0,1}
block ↦ 1  if H·block^T = 0 (syndrome-zero)
         0  otherwise
```

This is a **projection** onto the Hamming code subspace. It is linear over GF(2).

**Observable**:

```
P₀ = (1/K) Σ_k Π_L2S(block_k) ∈ [0,1]
```

This aggregation is **linear** (a mean over binary indicators).

#### L2T — Gray Transport Layer

**Input space**: Z_N^m (sequences of m symbols from alphabet Z_N = {0,...,N-1})

**Gray rank map** [code-derived from `build_gray_order_table()`]:

```
G: {0,...,N-1} → {0,...,N-1}    (Gray code bijection)
G(n) = n XOR (n >> 1)          (standard reflected binary Gray code)
```

**Adjacency predicate**:

```
adj: Z_N × Z_N → {0,1}
adj(s, s') = 1  if |G^{-1}(s) - G^{-1}(s')| ≡ 1  (mod N)
             0  otherwise
```

**Observable** [code-derived from `gray_adjacency_score()`]:

```
A_gray: Z_N^m → [0,1]
A_gray(s₁,...,s_m) = (1/(m-1)) Σᵢ adj(sᵢ, s_{i+1})
```

This is a **nonlinear** map (composed of a bijection G and a binary indicator),
but its aggregate output A_gray is linear in the binary adjacency indicators.

**Phase → symbol discretization** [code-derived from `phases_to_symbols()`]:

```
Disc_N: [-π,π) → Z_N
φ ↦ floor(N/(2π) · (φ + π))
```

This is a **nonlinear** map (floor function), implementing a discretization
(quantization to N uniform bins).

#### L2 Winding Number Scan

```
V_eff_L2: P ∩ [101,199] → R    (P = set of primes)
n ↦ n² - B·n·ln n

Argmin selection:
n* = argmin_{n ∈ P ∩ [101,199]} V_eff_L2(n)
```

**Operator classification**:
- Parity check H_check: **linear** over GF(2) (filtering / projection)
- Π_L2S: **projection** onto code subspace (reduces dimension)
- Gray rank G: **bijection** (permutation, no dimension change)
- adj: **nonlinear** (indicator of proximity in permuted order)
- A_gray: **mean aggregation** (dimension reduction: m → 1)
- Disc_N: **nonlinear** (floor/discretization; information-lossy)
- V_eff_L2: **nonlinear scalar** (polynomial-logarithmic, same as L1c)

---

## Summary: L0 → L1 → L2 Operator Chain

```
Configuration space C_Θ                         [L0 domain]
         │
         │  L0: nonlinear integral functionals
         │  (spectral action, winding, phase winding, curvature, action)
         ▼
Five L0 invariants: I_spec, I_wind, I_phase, I_curv, I_action ∈ R or Z   [L0 output]
         │
         │  L1: variational + perturbative calculations
         │  (metric emergence, GR limit, one-loop V_eff)
         ▼
Physics observables: G_μν, n*, B₀, V_eff(n)                              [L1 output]
         │
         │  L2: discretization + coding constraints
         │  (phase binning → symbols → Hamming parity or Gray adjacency)
         ▼
Discrete statistics: P₀, A_gray, n* (prime scan)                          [L2 output]
```

---

## Operator Type Classification (Complete)

| Layer | Operator | Type | Invertible? | Information loss? |
|-------|----------|------|-------------|-------------------|
| L0 | I_spec | Nonlinear integral | No | Yes (many Θ → same I_spec) |
| L0 | I_wind | Topological (homotopy) | No | Yes |
| L0 | I_phase | Topological | No | Yes |
| L0 | I_curv | Nonlinear integral | No | Yes |
| L0 | I_action | Nonlinear functional | No | Yes |
| L1 | G_μν emergence | Nonlinear variational | No | Yes |
| L1 | GR limit (ψ→0) | Projection | No | Yes (drops ψ-component) |
| L1 | V_eff(n) | Nonlinear scalar | No | N/A (scalar domain) |
| L2S | H_check (parity) | Linear / GF(2) | No | Yes (many blocks → same syndrome) |
| L2S | Π_L2S (selector) | Projection | No | Yes |
| L2T | Gray(n) | Bijection | Yes | No |
| L2T | adj(s,s') | Nonlinear indicator | No | Yes |
| L2T | A_gray | Mean aggregation | No | Yes (m → 1) |
| L2T | Disc_N | Floor discretization | No | Yes (lossy quantization) |

---

*Generated by ubt_L0_L1_L2_full_audit, Step 4.*
