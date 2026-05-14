> © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
>
> This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
> 4.0 International License (CC BY-NC-ND 4.0).

# L0 / L1 / L2 — Final Summary

**Task**: `ubt_L0_L1_L2_full_audit`  
**Date**: 2026-05-05  
**Mode**: deep_repo_analysis  
**Epistemic mode**: strict

---

## Critical Finding: Two Incompatible L-Numbering Systems

The repository uses L0/L1/L2 labels in **two distinct, incompatible systems**
that must not be confused:

| System | Notation | Meaning | Source |
|--------|----------|---------|--------|
| **A** Architecture | Layer 0 / L0 | Fundamental field + algebraic invariants | `FORMAL_INVARIANT_EXTRACTION_LAYER0.tex`, `docs/LAYER0_INVARIANT_EXTRACTION_README.md` |
| **A** Architecture | Layer 1 / L1 | Emergent metric, classical GR/QFT limits | `FORMAL_INVARIANT_EXTRACTION_LAYER0.tex`, `docs/architecture/LAYERS.md` |
| **A** Architecture | Layer 2 / L2 | Discretized coding/modulation procedures | `docs/architecture/LAYERS.md`, `gray_vs_hamming_layer2.md` |
| **B** Loop order | [L0] | Tree-level (no loop corrections) | `docs/REPO_LAYERS.md` |
| **B** Loop order | [L1] | One-loop result | `docs/REPO_LAYERS.md`, `ALPHA_PROGRESS_REPORT.md` |
| **B** Loop order | [L2] | Higher-loop / non-perturbative | `docs/REPO_LAYERS.md` |

The bracket notation `[L0]`, `[L1]`, `[L2]` is System B (loop order).
The unbracketed "Layer 0/1/2" or "L0/L1/L2" is System A (architecture).

---

## Exact Definitions

### System A — Architecture Layers

#### L0: Fundamental Biquaternionic Geometry

**Definition** [doc-derived from `FORMAL_INVARIANT_EXTRACTION_LAYER0.tex`]:

```
Domain: Configuration space C_Θ of smooth field sections
  Θ: B^4 × C → B ⊗ S ⊗ G
  B = C ⊗ H (biquaternion algebra, dim_ℝ = 8)
  C = {τ = t + iψ} (complex time)
  S = Spin(3,1) spinor bundle
  G = SU(3) × SU(2) × U(1) gauge fiber

Action: S[Θ] = S_kin + S_pot + S_gauge  (nonlinear functional)

Five L0 invariants:
  I_spec  = Tr[f(D²/Λ²)]         (spectral action, nonlinear)
  I_wind  = n_wind ∈ ℤ           (topological winding, π₃(G/H))
  I_phase = K_ψ ∈ ℤ              (imaginary time periodicity)
  I_curv  = ∫dμ R(q,τ)           (curvature integral)
  I_action = S[Θ]                 (action functional)
```

No free parameters. No discretization. Derived purely from field
structure and symmetries.

---

#### L1: Emergent Physics

**Definition** [doc-derived]:

In **System A architecture**: the layer of emergent metric structure and
classical GR/QFT limits derived from L0 invariants.

```
L1 operators:
  G_μν(Θ)    : variational derivation of metric from Θ  (nonlinear)
  GR_limit   : Θ → R_μν - (1/2)g_μν R = 8πG T_μν  (ψ → 0 limit)
  V_eff(n)   : n² - B·n·ln n  (one-loop effective potential)
  B₀         = 8π (one-loop coefficient: B₀ = 2π N_eff/3, N_eff = 12)
```

In **System B loop order**: [L1] = one-loop results.

```
Examples of [L1]-proved results:
  B₀ = 8π                    [L1] PROVED
  V_eff(n) = n² - B·n·ln n   [L1] PROVED (given B)
  Stationarity: n* ≈ B/(2·(1+ln n*))   [L1] PROVED (given B)
  Prime stability of n*=137  [L1] PROVED
```

---

#### L2: Coding / Discretization / Protocol

**Definition** [doc-derived]:

```
L2 is a collection of discrete operational procedures, NOT a fundamental
physics layer. Three types:

L2S (State layer) — Hamming (8,4,4):
  Input:  {0,1}^8 (8-bit blocks)
  Op:     Parity check H: {0,1}^8 → {0,1}^4  (linear over GF(2))
  Output: Syndrome + P₀ = fraction of syndrome-zero blocks
  Type:   Projection (Π_L2S, idempotent onto codewords)

L2T (Transport layer) — Gray adjacency:
  Input:  Phase symbols ∈ {0,...,N-1}^m
  Op:     A_gray = (1/(m-1)) Σ 1[G^{-1}(s_i) and G^{-1}(s_{i+1}) adjacent]
  Output: Scalar ∈ [0, 1]
  Type:   Mean aggregation (m → 1)

L2 winding scan:
  Input:  n ∈ primes ∩ [101,199]
  Op:     Argmin of V_eff(n) = n² - B·n·ln n
  Output: n* ∈ ℤ
  Type:   Argmin selection
```

**L2 contains 6 additional postulates** not derivable from L0 [doc-derived]:
```
L2.1 Prime restriction on winding numbers — Heuristic
L2.2 Specific choice n=137              — Empirical calibration
L2.3 RS(255,201) with GF(2⁸)           — Engineering choice
L2.4 16 OFDM channels                   — Design parameter
L2.5 Fixed discretization grid          — Computational constraint
L2.6 Prime-gating pattern               — Parametric scan choice
```

---

### System B — Loop Order Labels

```
[L0] = pure biquaternionic geometry (no loop corrections)
       Examples: N_eff = 12 (algebraic), Gray code structure of ℂ⊗ℍ

[L1] = one-loop result
       Examples: B₀ = 8π, V_eff(n), stationarity condition

[L2] = higher-loop or non-perturbative
       (Label defined; no [L2]-proved results present in repo at audit date)
```

---

## Mathematical Form Summary

| Layer | Mathematical form | Type |
|-------|-----------------|------|
| L0: I_spec | Tr[f(D²/Λ²)] | Nonlinear integral functional |
| L0: I_wind | π₃(G/H) homotopy class | Topological integer invariant |
| L1: V_eff | n² - B·n·ln n | Nonlinear scalar function of n |
| L1: GR limit | R_μν - ½g_μν R = 8πG T_μν | PDE limit (ψ → 0) |
| L2S: parity | H·block^T = 0 (mod 2) | Linear filter over GF(2) |
| L2T: adjacency | Σ 1[|G⁻¹(sᵢ) - G⁻¹(sᵢ₊₁)| ≡ 1] / (m-1) | Mean over indicator |
| L2T: Gray code | G(n) = n XOR (n >> 1) | Bijection on {0,...,N-1} |

---

## Dimensional Flow

```
∞-dim field space C_Θ
       │ L0 (integral functionals)
       ▼
5 real invariants (I_spec, I_wind, I_phase, I_curv, I_action)
       │ L1 (variational / perturbative)
       ▼
Scalar physics: n*, V_eff(n*), G_μν, B₀
       │ L2 (discretization / coding)
       ▼
Binary statistics: P₀ ∈ [0,1],  A_gray ∈ [0,1]
```

**All transitions are lossy.** The only reversible step in L2 is the Gray
code bijection G(n) (which maps integer → integer, not a dimension
reduction). [numerically verified]

---

## What L2 Actually Does

1. **L2S (Hamming)**: Filters 8-bit phase blocks through a GF(2) parity
   constraint. Projects onto the 16-codeword subspace of {0,1}^8.
   Observable: P₀ (fraction of syndrome-zero blocks).

2. **L2T (Gray)**: Measures the fraction of consecutive phase-symbol
   transitions that are Gray-adjacent (single-bit changes). Observable:
   A_gray. **This is a statistical test, not a decoder.**

3. **L2 winding scan**: Selects the argmin of V_eff(n) over prime winding
   numbers. Outputs n* (single integer).

**What L2 does NOT do** [doc-derived]:
- Does not prove α = 1/137 from first principles
- Does not project a continuous field onto the "physical state" in the
  sense that would make L2 a fundamental projector
- Does not decode a message from noisy codewords (no encode/decode pipeline)

---

## What Is Missing

| Gap | Status |
|-----|--------|
| L0 → L1 metric derivation (explicit map G_μν from Θ) | Open (in canonical/ appendices but not a closed-form formula) |
| L1 → α first-principles derivation (closed n* = 137) | Open (B_base gap; k=1 not proved) |
| L2 prime constraint derived from topology | Open (no derivation exists) |
| L2 RS(255,201) derived from field dimensions | Open (no derivation exists) |
| L2 → L0 error-free mapping (eliminate heuristic δ terms) | Open |
| System B [L2] proved results | None present at audit date |

---

## Files Produced by This Audit

| File | Content |
|------|---------|
| `research_tracks/L_layers/L_definitions_raw.md` | All L0/L1/L2 occurrences in repo with source citations |
| `research_tracks/L_layers/L_code_analysis.md` | Code-level functions and their I/O |
| `research_tracks/L_layers/L_shapes.md` | Dimensional/space analysis per layer |
| `research_tracks/L_layers/L_math_formulation.md` | Mathematical operator formalization |
| `research_tracks/L_layers/L2_decode_analysis.md` | Decode/projection analysis of L2 |
| `experiments/L_layer_flow_test.py` | Numerical pipeline: Θ → L0 → L1 → L2 |
| `reports/L_layer_numeric.md` | Auto-generated numerical test report |
| `research_tracks/L_layers/L_consistency.md` | UBT interpretation consistency checks |
| `research_tracks/L_layers/L_summary.md` | This file |

---

*Generated by ubt_L0_L1_L2_full_audit, Step 8.*
