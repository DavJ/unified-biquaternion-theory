<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# FITTED_PARAMETERS.md — UBT Fitted and Free Parameters

This file tracks all parameters in UBT that are either:
- **Fitted** — value chosen to match an experimental result (not predicted)
- **Semi-empirical** — partially derived but with unexplained residual
- **Free** — no derivation; must be input from experiment

Parameters that are **fully derived** from first principles are NOT listed here
(they appear in DERIVATION_INDEX.md as "Proven").

---

## Fine Structure Constant Derivation

| Parameter | Symbol | Value | Status | To be resolved by |
|-----------|--------|-------|--------|-------------------|
| B_base formula | B_base = N_eff^{3/2} | 41.57 (for N_eff=12) | **OPEN PROBLEM A** — no derivation | KK mode form factor or gauge-orbit volume argument |
| Correction factor | R | ≈ 1.114 | **OPEN PROBLEM B** — no derivation | NC correction from [D_μ,D_ν] or gravitational dressing |
| Full B coefficient | B = B_base × R | ≈ 46.3 | **Semi-empirical** | Requires A and B resolution |

Note: Once both Problem A and Problem B are resolved, R should be **removed**
from this table (or kept with a proven value). Until then, R remains here
as a free parameter.

The A kinetic coefficient is normalised to 1.0 by convention and is NOT a free parameter.

---

## Electroweak Sector

| Parameter | Symbol | Value | Status | Notes |
|-----------|--------|-------|--------|-------|
| Weinberg angle | θ_W | sin²θ_W ≈ 0.231 | **Free (experimental input)** | Cannot be fixed by ℂ⊗ℍ geometry alone (see appendix_E2_SM_geometry.tex §6) |
| SU(2)_L coupling | g | ≈ 0.653 | **Free** | Not predicted from biquaternionic geometry |
| U(1)_Y coupling | g' | ≈ 0.357 | **Free** | Not predicted from biquaternionic geometry |

---

## Lepton Mass Sector (Three Generations)

| Parameter | Symbol | Value | Status | Notes |
|-----------|--------|-------|--------|-------|
| ψ-instanton action | S_inst | ≈ 5.33 | **Fitted** to muon mass ratio | S_inst = ln(m_μ/m_e) ≈ 5.33; tau not reproduced |
| Mass generation mechanism | — | — | **OPEN HARD PROBLEM** | Options A/B/C all fail; see st3_complex_time_generations.tex §7 |

The naive KK formula is DERIVED and gives ratio 1:2, which is WRONG.
No mechanism with ≤1 free parameter reproduces 1:207:3477.
All free parameters for lepton masses are pending until the mass generation
mechanism is identified.

---

## Parameters That Would Be Removed If Derived

The following parameters could be removed from this table (upgraded to "Proven")
if the indicated derivation is completed:

| Parameter | Removal condition |
|-----------|-------------------|
| R ≈ 1.114 | Derive R from [D_μ,D_ν] in ℂ⊗ℍ (Option B2) or gravitational dressing (Option B3) |
| B_base = N_eff^{3/2} | Derive from KK mode form factor or gauge-orbit volume |
| θ_W | Derive sin²θ_W from extended algebra structure or ψ-circle dynamics |

---

*Last updated: 2026-03-04. See STATUS_ALPHA.md §9 and docs/PROOFKIT_ALPHA.md §5 for details.*
