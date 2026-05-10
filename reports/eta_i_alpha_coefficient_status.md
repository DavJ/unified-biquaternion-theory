<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# eta_i_alpha_coefficient_status.md

**Task**: `prove_or_falsify_eta_i_alpha_coefficient`  
**Author**: Ing. David Jaroš  
**Date**: 2026-05-10  
**Track**: T3_ALPHA  
**Priority**: CRITICAL  
**Hard rules**: No use of α_exp; no use of 137 as derivation input; no exponent tuning.

---

## Formula under investigation

$$B = N_{\rm eff}^{3/2}\,(2\eta(i))^{c/12}
  = 12^{3/2}\!\left(\frac{\Gamma(1/4)}{\pi^{3/4}}\right)^{\!1/4}
  \approx 46.280872$$

---

## Master Verdict

> **OBSERVATION**
>
> The formula `B = 12^(3/2)*(2*eta(i))^(1/4)` is the best-supported
> numerical candidate for the UBT B coefficient.  It is **not proved** from
> the UBT action S[Θ].  Three independent gaps (G-nlogn, G-c3, G-insertion)
> block the PROVED verdict.

---

## Seven Questions — Summary Answers

| # | Question | Answer | Status |
|---|----------|--------|--------|
| Q1 | Does the canonical UBT alpha sector define a T² with τ = i? | Shape stationary point proved (conditional); scale not fixed | CONDITIONAL |
| Q2 | Does the one-loop determinant produce η(i)? | Mathematics: yes. Physical identification: not proved | CONDITIONAL / OPEN |
| Q3 | Does the Weyl anomaly produce exponent c/12? | Mathematics: yes (standard CFT). Physical c = 3: not derived | PROVED (math) / OPEN (physics) |
| Q4 | Is c = 3 uniquely derived from Im(ℍ) phase DoF? | Mode-counting argument only; not from δ²S/δΘ² | OPEN |
| Q5 | Why does the factor multiply B, not just Z? | No mechanism derived; all three sub-routes blocked or speculative | OPEN (Gap G-insertion) |
| Q6 | Can the 0.0066% discrepancy be explained? | Candidate corrections exist; none derived | OPEN |
| Q7 | Is the match a numerical coincidence? | Not a pure coincidence (uniqueness proven); not proved | OBSERVATION |

---

## Status Table (full)

| ID | Claim | Status | Source |
|----|-------|--------|--------|
| A1 | Canonical UBT alpha-sector action S[Θ] defined | PROVED [L0] | canonical/algebra |
| A2 | N_eff = 12 from dim_ℝ(ℂ⊗ℍ) | PROVED [L0] | neff12_derivations.tex |
| A3 | B_base = N_eff^(3/2) as base coefficient | CONDITIONAL [L1] | canonical/alpha |
| A4 | τ = i as shape stationary point of F_1-loop | CONDITIONAL [L1] | self_dual_torus.tex |
| A5 | det'(−ΔT²)|_{τ=i} = (2π)²η(i)⁴ (mathematics) | PROVED [L0] | chowla_selberg.tex |
| A6 | Weyl anomaly exponent c/12 from CFT (mathematics) | PROVED [L0] | CFT textbooks |
| A7 | UBT alpha CFT on T² has c = 3 | OPEN | Gap G-c3 |
| A8 | V_eff(n) = n² − Bn ln n derived from S[Θ] | OPEN | Gap G-nlogn |
| A9 | (2η(i))^(c/12) enters coefficient B (not just Z₀) | OPEN | Gap G-insertion |
| A10 | B_full = 12^(3/2)·(2η(i))^(1/4) proved from S[Θ] | **FAILED** (current) | Gaps A7+A8+A9 open |
| A11 | B_obs ≈ B_req(137) to 0.0066% | **OBSERVATION** | check_eta_alpha_formula.py |
| A12 | (2η(i))^(1/4) is unique best match among ~60 candidates | **OBSERVATION** | verify_b_eta_uniqueness.py |
| A13 | 0.0066% discrepancy explained by controlled correction | OPEN | §Q6 |

---

## Three Blocking Gaps

### Gap G-nlogn: Origin of the n log n form

The exact Coleman–Weinberg effective potential on S¹_ψ is:

```
V_CW(n) = n² − N_eff log(2 sinh(πn))
```

- Minimum at n* ≈ 6π ≈ 19, not 137  
- Large-n behaviour: ~n² − π N_eff n (linear, not n log n)  
- Small-n limit: ~n² − N_eff log n + const (not n log n either)

The n log n form cannot come from the direct CW determinant.  A separate
physical mechanism is required.  Candidate: the Dirichlet divisor sum
∑_{k=1}^n τ(k) ≈ n log n from the number-theoretic winding spectrum.
**Status: OPEN**.

### Gap G-c3: Central charge c = 3 not derived

The exponent 1/4 = c/12 requires c = 3.  Arguments available:
- 3 real phase DoF in Im(ℍ) after SU(2)_L gauge fixing  
- Algebraic relation c = N_eff/4 = 12/4 = 3

Neither derives c from δ²S[Θ]/δΘ² at the winding saddle.
**Status: OPEN**.

### Gap G-insertion: η(i) in B vs. partition-function normalisation

The determinant det'(−ΔT²) = (2π)²|η(i)|⁴ contributes to the one-loop
effective action as an **n-independent** constant.  It does not enter the
n-dependent coefficient B without an additional mechanism.

Sub-routes examined and their outcomes:
| Route | Outcome |
|-------|---------|
| Saddle at τ_n = in | log η(in) ~ −πn/12 (linear in n, not n log n) |
| RG threshold correction | Structurally plausible; not derived from S[Θ] |
| Modular sum-over-saddles | Blocked by Hecke NO-GO obstruction O1 |

**Status: OPEN**.

---

## Numerical Result (computed after derivation attempt)

```
N_eff                  = 12
N_eff^(3/2)            = 41.569219...
η(i)                   = Γ(1/4)/(2π^(3/4)) ≈ 0.768225...
2η(i)                  ≈ 1.536451...
(2η(i))^(1/4)          ≈ 1.113952...
B_obs                  ≈ 46.280872
B_req(137)             = 274/(ln 137 + 1) ≈ 46.283933
Relative deviation     ≈ 0.0066%
Exact exponent x s.t.  B_req = 12^(3/2)·(2η(i))^x: x ≈ 0.25016 ≈ 1/4
```

Verification: `python3 tools/check_eta_alpha_formula.py`

---

## Uniqueness Result

The scan of ~60 standard special values (`tools/verify_b_eta_uniqueness.py`)
confirms that `(2η(i))^(1/4)` is the unique best match:

- Primary deviation: 0.0066%  
- Next best: `(2η(ρ))^(1/4)` at ~0.81%  
- Improvement factor: ~115×

This rules out accidental coincidence at the level of arbitrary special
values, but does not constitute a proof.

---

## Predecessor Documents

| Document | Role |
|----------|------|
| `reports/eta_i_B_insertion_verdict.md` | Predecessor verdict (CONDITIONAL_WITH_EXACT_GAP, 2026-05-09) |
| `reports/alpha_eta_i_rejection.md` | Formal rejection as first-principles B-modifier (2026-05-09) |
| `reports/alpha_current_verdict.md` | Current alpha program status |
| `reports/B_gap_final_verdict.md` | B-gap overall verdict |
| `research_tracks/T3_ALPHA/chowla_selberg_b_derivation.tex` | Chowla–Selberg derivation attempt |
| `research_tracks/T3_ALPHA/cw_determinant_full_derivation.tex` | Exact CW det on S¹_ψ |
| `research_tracks/alpha_spectral/hecke_equivariant_path_integral.tex` | Hecke NO-GO |

---

## Derivation Document

`research_tracks/T3_ALPHA/eta_i_alpha_coefficient_derivation.tex`

---

## Recommended Next Steps

1. **G-c3 (highest priority)**: Compute δ²S[Θ]/δΘ² in the winding background
   and identify the Virasoro central charge.  Time-box: 4 weeks.

2. **G-nlogn**: Investigate whether the Dirichlet divisor-sum
   ∑_{k=1}^n τ(k) ≈ n log n arises from the number-theoretic winding spectrum.

3. **G-insertion**: Compute W_eff[n] on the family of tori T²(τ_n = in),
   T-dual at n = 1, and check whether η(i) appears in the n-dependent part.

4. **Falsification**: Prove S[Θ] is not SL(2,ℤ)-covariant.  If true,
   eliminates the modular absorption mechanism entirely.

---

## Policy

Per `reports/alpha_current_verdict.md` and `canonical/alpha/ALPHA_MASTER_STATUS.md`:

- η(i) is **rejected as a first-principles B-modifier**.
- η(i) may be referenced **only** as a numerical observation or
  partition-function normalisation clue.
- This document and the companion `.tex` file are the **canonical record**
  of the derivation attempt and its outcome.
- **No modification to `canonical/` is warranted at this time.**
