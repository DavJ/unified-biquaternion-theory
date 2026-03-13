<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Fine Structure Constant (α) — Topic Index

**Status**: **PARTIALLY DERIVED** — structural framework proved; two key quantities remain open  
**Last updated**: 2026-03-10  
**Canonical source**: `STATUS_ALPHA.md`

---

## Quick Answer

The fine structure constant α ≈ 1/137.036 emerges from UBT in three layers:

| Layer | Result | Status |
|-------|--------|--------|
| B₀ = 2π·N_eff/3 = 8π ≈ 25.13 | One-loop baseline | **PROVED [L1]** — zero free parameters |
| B_base = N_eff^{3/2} = 41.57 | Effective coupling strength | **MOTIVATED CONJECTURE** — exponent 3/2 not derived |
| R ≈ 1.114 | Loop correction factor | **OPEN HARD PROBLEM** |
| α⁻¹ = 137 (bare) | Follows from B = 46.3 | **SEMI-EMPIRICAL** |
| α⁻¹ = 137.036 (full) | + two-loop QED correction | **SEMI-EMPIRICAL** |

The theory locates n* = 137 as the unique prime minimum of V_eff(n) (**PROVED [L1]**),
and independently reproduces the two-loop QED running (**PROVED**). The missing piece
is a rigorous first-principles derivation of B_base and R.

---

## Canonical Source (Start Here)

| Document | Role | Status |
|----------|------|--------|
| `STATUS_ALPHA.md` | **CANONICAL** — complete derivation chain with gap inventory | Master reference |

`STATUS_ALPHA.md` is the single authoritative source covering:
- §2 Complex time compactification and Dirac quantisation
- §3 Prime stability constraint and V_eff(n) minimum
- §4 Effective potential one-loop structure
- §5 N_eff = 12 derivation and B₀ = 8π
- §9 B_base landscape of 22 approaches with explicit gap statements

---

## Supporting Files

### Derivation chain files

| Document | Label | Content |
|----------|-------|---------|
| `consolidation_project/N_eff_derivation/step1_mode_decomposition.tex` | **supporting** | N_eff = 12 (Theorem 1.4) |
| `consolidation_project/N_eff_derivation/step2_vacuum_polarization.tex` | **supporting** | B₀ = 8π (Theorem 3.1) |
| `consolidation_project/N_eff_derivation/step3_N_eff_result.tex` | **supporting** | N_eff = 12 result compilation |
| `consolidation_project/N_eff_derivation/verify_N_eff.py` | **supporting** | Numerical verification |
| `consolidation_project/appendix_ALPHA_one_loop_biquat.tex` | **supporting** | One-loop alpha derivation (§B.3 for B_base) |

### B_base approaches (Gaps G1–G3, H1–H3)

The following files document all 22 tested approaches to derive B_base.
All are **supporting** documents; STATUS_ALPHA.md §9 is the canonical summary.

| Document | Label | Approaches |
|----------|-------|-----------|
| `consolidation_project/alpha_derivation/b_base_hausdorff.tex` | **supporting** | A2 (MOTIVATED CONJECTURE: exponent 3/2) |
| `consolidation_project/alpha_derivation/b_base_spinor_approach.tex` | **supporting** | B_base via spinors |
| `consolidation_project/alpha_derivation/b_base_delta_d.tex` | **supporting** | C1–C2 (DEAD END) |
| `consolidation_project/alpha_derivation/b_base_nonpert.tex` | **supporting** | D1–D3 (DEAD END) |
| `consolidation_project/alpha_derivation/b_base_new_directions.tex` | **supporting** | E1–E4 (partial) |
| `consolidation_project/alpha_derivation/b_base_ncg_a4.tex` | **supporting** | F1–F4 (partial) |
| `consolidation_project/alpha_derivation/b_base_g_approaches.tex` | **supporting** | G1–G7 (partial) |
| `consolidation_project/alpha_derivation/b_base_kac_moody_level.tex` | **supporting** | H1–H3: k=1 motivated conjecture |
| `consolidation_project/alpha_derivation/r_factor_geometry.tex` | **supporting** | R-factor geometry (OPEN) |

### R-factor and correction files

| Document | Label | Content |
|----------|-------|---------|
| `tools/explore_r_factor.py` | **supporting** | R-factor numerical exploration |
| `tools/explore_b_exponent.py` | **supporting** | Exponent 3/2 numerical exploration |
| `tools/compute_B_KK_sum.py` | **supporting** | KK sum approach (DEAD END) |
| `tools/compute_B_effective_dimension.py` | **supporting** | Effective dimension (dead end) |

---

## Sandbox / Heuristic Files

| Document | Label | Why Not Canonical |
|----------|-------|-------------------|
| `emergent_alpha_calculations.tex` | **sandbox** | Exploratory; superseded by STATUS_ALPHA.md |
| `emergent_alpha_from_ubt.tex` | **sandbox** | Earlier narrative; superseded |
| `emergent_alpha_executive_summary.tex` | **sandbox** | Old executive summary; STATUS_ALPHA.md is current |
| `appendix_C_geometry_alpha.tex` | **historical** | Earlier geometry approach; documentation only |
| `appendix_C_geometry_alpha_v2.tex` | **historical** | V2 of same; not canonical |
| `alpha_padic_executive_summary.tex` | **sandbox** | p-adic extension; speculative |
| `docs/ALPHA_FROM_ME_ANALYSIS.md` | **supporting** | Matrix element analysis; narrow specific question |
| `docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md` | **supporting** | Stability selection rules; subset of STATUS_ALPHA |
| `reports/alpha_derivation_trace.md` | **historical** | Earlier derivation trace |
| `reports/alpha_audit/alpha_paths.md` | **historical** | Path map superseded by STATUS_ALPHA.md §9 |

---

## Validated Scripts

| Script | Role | Output |
|--------|------|--------|
| `validation/validate_B_coefficient.py` | Non-circularity test | Confirms different N_eff → different n* |
| `alpha_core_repro/alpha_two_loop.py` | Two-loop reproduction | `alpha_core_repro/out/alpha_two_loop_grid.csv` |
| `validate_alpha_renormalization.py` | Renormalisation validation | Quantitative check |

---

## Open Problems Summary

| Gap ID | Description | Current best | Files |
|--------|-------------|--------------|-------|
| G3-k | Kac-Moody level k from S[Θ] | k=1 (MOTIVATED CONJECTURE via H2) | `b_base_kac_moody_level.tex` |
| G-exp | 3/2 exponent in B_base = N_eff^{3/2} | Structural from real Gaussian on Im(ℍ) | `b_base_hausdorff.tex §4` |
| G-R | R ≈ 1.114 correction factor | Best candidate: 1+α(N_eff+π+1/4) ≈ 1.1123 (0.15%) | `r_factor_geometry.tex` |
| G8 | Modular weight of Ẑ(τ) | Open | `b_base_g_approaches.tex` |

---

## DERIVATION_INDEX Cross-Reference

Main entries in `DERIVATION_INDEX.md`, Fine Structure Constant section:
- B₀ = 25.1 — **PROVED [L1]**
- B_base = 41.57 — **MOTIVATED CONJECTURE**
- R ≈ 1.114 — **OPEN HARD PROBLEM**
- α⁻¹ = 137, 137.036 — **SEMI-EMPIRICAL**

---

## What a New Reader Should Do

1. Read `STATUS_ALPHA.md` §§1–5 for the proved results (B₀, V_eff minimum, N_eff=12)
2. Read §9 of `STATUS_ALPHA.md` for the B_base gap landscape
3. For the deepest current approach to B_base, read
   `consolidation_project/alpha_derivation/b_base_hausdorff.tex` (Approach A2)
   and `consolidation_project/alpha_derivation/b_base_kac_moody_level.tex` (Approach H2)
4. For numerical verification, run `validation/validate_B_coefficient.py`
5. Do not use `emergent_alpha_*.tex` files as primary sources — they are superseded by `STATUS_ALPHA.md`
