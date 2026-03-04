<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# FITTED_PARAMETERS.md — UBT Fitted and Free Parameters

> **Purpose**: Track which parameters in UBT are fitted/semi-empirical (not derived),
> and which have been promoted to fully derived status.
>
> **Maintenance rule (R5):** Update this file on every gap closure.
> - Remove a parameter when it is derived from first principles.
> - Keep a parameter when it remains fitted to data.

This file tracks all parameters in UBT that are either:
- **Fitted** — value chosen to match an experimental result (not predicted)
- **Semi-empirical** — partially derived but with unexplained residual
- **Free** — no derivation; must be input from experiment

Parameters that are **fully derived** from first principles are NOT listed here as active
(they appear in DERIVATION_INDEX.md as "Proven" and in the "Promoted" table below).

---

## How to Read This Register

| Column | Meaning |
|---|---|
| **Parameter** | Symbol and brief description |
| **Domain** | Physics domain where it appears |
| **Formula** | Where the parameter enters |
| **Current Status** | `Fitted` / `Derived` / `Semi-empirical` |
| **Data Used** | What data it was fitted to (if any) |
| **Gap** | Which Gap task addresses this parameter |

---

## Active (Not Yet Derived) Parameters

| Parameter | Domain | Formula | Current Status | Data Used | Gap |
|---|---|---|---|---|---|
| **B̃** (B_base = N_eff^{3/2}) | Fine structure α | V_eff(n) = An² − B̃·n·ln(n) | **Semi-empirical** (OPEN PROBLEM A — three derivation approaches tested; all give HONEST GAP or DEAD END; see `tools/compute_B_KK_sum.py` and `STATUS_ALPHA.md §9`) | SM gauge-boson content (N_eff = 12) | Gap 6 |
| **R factor** (≈ 1.114) | Fine structure α | B = B_base × R | **Semi-empirical** (OPEN PROBLEM B) | SM particle spectrum | Gap 6 |
| **Λ** (cosmological constant) | Cosmology / GR | FRW embedding | Semi-empirical | CMB Planck data | — |
| **Electroweak mixing angle** θ_W | Standard Model | SU(2)×U(1) embedding | **Semi-empirical** | PDG value sin²θ_W = 0.231 | Gap 5 |
| **SU(2)_L coupling** g | Standard Model | Covariant derivative D_μ | **Free** | PDG g ≈ 0.653 | — |
| **U(1)_Y coupling** g' | Standard Model | Covariant derivative D_μ | **Free** | PDG g' ≈ 0.357 | — |
| **ψ-instanton action** S_inst | Lepton masses | m_n ~ exp(S_inst·n)/n! | **Fitted** to muon | S_inst = ln(m_μ/m_e) ≈ 5.33; tau not reproduced | Gap 4 |

Notes on the α derivation:
- Once Problem A (B_base) and Problem B (R) are resolved, both should be **removed** from this table.
- The A kinetic coefficient is normalised to 1.0 by convention and is NOT a free parameter.
- See `STATUS_ALPHA.md §9` for the full derivation strategy.

Notes on lepton masses:
- The naive KK formula is DERIVED and gives ratio 1:2, which is WRONG (mismatch theorem).
- No mechanism with ≤1 free parameter reproduces 1:207:3477.
- All free parameters for lepton masses are pending until the mass generation mechanism is identified.

---

## Promoted: Formerly Fitted, Now Derived

| Parameter | Derived in | Gap | Reference | Date |
|---|---|---|---|---|
| **A** (quadratic coefficient) | KK kinetic energy: A = ℏ²/(2m_field·R_ψ²) | Gap 1 | `Appendix_H_Theta_Phase_Emergence.tex` §H.3a.3 | 2025 |

---

## Multi-Channel Framework for N=137

The effective potential V_eff(n) = An² − B̃·n·ln(n) has a minimum at a specific winding
number n. Within the multi-channel framework, multiple prime channels are stable:

- **Channel family** of prime attractors: n = 131, 137, 139, 149, ...
- **Alternative channels**: n = 199 ranks highest by stability scan; n = 139 is adjacent prime.
- **Our channel**: n = 137 is selected by energy minimisation (V_eff minimum), not stability rank alone.

The "mostly derived" status of V_eff(n) means:
- The An² term is **derived** from KK kinematics (Gap 1, no free parameters).
- The B̃·n·ln(n) term is **semi-empirical**: structure-motivated by one-loop arguments,
  coefficient fitted to SM content (N_eff = 12 gauge bosons).
- The roadmap (Gap 6) is to derive B̃ from first principles.

See `STATUS_ALPHA.md §9` and `validation/validate_B_coefficient.py` for the no-circularity test.

---

## Parameters That Would Be Removed If Derived

| Parameter | Removal condition |
|-----------|-------------------|
| R ≈ 1.114 | Derive R from [D_μ,D_ν] in ℂ⊗ℍ (Option B2) or gravitational dressing (Option B3) |
| B_base = N_eff^{3/2} | Derive from KK mode form factor or gauge-orbit volume. KK sum, zeta regularization, and Weyl gauge-orbit volume all tested in `tools/compute_B_KK_sum.py` — all give HONEST GAP / DEAD END as of 2026-03-04 |
| θ_W | Derive sin²θ_W from extended algebra structure or ψ-circle dynamics |

---

*Full details also in `docs/FITTED_PARAMETERS.md`.*

*Last updated: 2026-03-04. See STATUS_ALPHA.md §9 and docs/PROOFKIT_ALPHA.md §5 for details.*

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*

