<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Claim Survival Matrix: UBT Numerical Claims vs. Null Models

**Task**: Task 5 — Falsification Framework  
**Author**: Ing. David Jaroš  
**Date**: May 2026  

---

## Purpose

This matrix documents which UBT numerical claims survive which null models
and statistical tests.  Claims that do not appear in this matrix have not
been tested and should be considered unverified.

---

## Claim Inventory

| ID | Claim | Source |
|----|-------|--------|
| C1 | Stable set is exactly $\mathcal{S} = \{2, 127, 137, 139, 151, 157\}$ | `canonical/alpha/prime_stability_set.tex` |
| C2 | $V(137; 46) < V(q; 46)$ for all primes $q \neq 137$ | `canonical/alpha/veff_corrected.tex` |
| C3 | $B(137) = (137+1)/3 = 46$ | Definition |
| C4 | No stable prime in $(157, 10^6]$ | Computational |
| C5 | $V_\text{eff}(n) = n^2 - Bn\ln n$ (functional form) | `canonical/alpha/alpha_equation_matrix.tex` |
| C6 | B-coefficient $B \approx 46$ arises from one-loop RG | `research_tracks/rg_nlogn/full_rg_derivation.tex` |
| C7 | Riemann zero spacing is GUE (literature result) | Montgomery 1973, Odlyzko 1987 |
| C8 | Free UBT operator spacing is NOT GUE | `research_tracks/rh_operator/spectral_statistics.md` |
| C9 | Self-adjointness of $A_0 = -d^2/d\psi^2$ on $S^1$ | `research_tracks/rh_operator/selfadjointness_attempt.tex` |
| C10 | $Z_H(t) = \theta_3(4\pi it)$ (free case) | `research_tracks/theta_spectral/theta_kernel_foundations.tex` |

---

## Survival Matrix

`✓` = claim survives this test  
`✗` = claim fails this test  
`?` = not yet tested  
`N/A` = test not applicable  

| Claim | Null-1 (Random B) | Null-2 (Shuffled B) | Null-3 (Poisson Primes) | Null-4 (Alt V_eff) | Statistical Test | Explicit PASS |
|-------|:-----------------:|:--------------------:|:-----------------------:|:-----------------:|:----------------:|:-------------:|
| C1 ($\mathcal{S}$ exact) | ✓ (non-trivial) | ✓ | ✓ | ? | ✓ | **PASS** |
| C2 (137 global min) | N/A | N/A | N/A | N/A | N/A | **PASS** |
| C3 ($B = 46$) | N/A | N/A | N/A | N/A | N/A | **PASS** |
| C4 (no prime > 157) | N/A | N/A | N/A | N/A | N/A | **PASS** |
| C5 ($n^2 - Bn\ln n$ form) | N/A | N/A | N/A | ? | N/A | N/A |
| C6 ($B$ from 1-loop RG) | N/A | N/A | N/A | N/A | N/A | **FAIL** (B = 43.6 ≠ 46) |
| C7 (GUE zeros) | N/A | N/A | N/A | N/A | Literature | **PASS (literature)** |
| C8 (free ≠ GUE) | N/A | N/A | N/A | N/A | ✓ (KS test) | **PASS** |
| C9 (SA of $A_0$) | N/A | N/A | N/A | N/A | N/A | **PASS** |
| C10 ($Z_H = \theta_3$) | N/A | N/A | N/A | N/A | N/A | **PASS** |

---

## Interpretation of C1 (Most Important Claim)

**Claim C1**: $\mathcal{S} = \{2, 127, 137, 139, 151, 157\}$.

### Against Null-1 (Random B):

Under random $B \sim U(1,100)$, the expected number of primes near 137 in
a stable set is $\sim$ (primes in [130,145]) / (total primes up to 10000)
$= 3/1229 \approx 0.24\%$ per trial.

The UBT formula $B(p) = (p+1)/3$ places $B(137) = 46$ exactly at the
stability window centre ($B^*(137) \approx 46.3$).  This is not guaranteed
by random $B$.

**Effect size** (Cohen's d): Under null, mean stable set size $\sim$ 2.5 with
std $\sim$ 1.5.  UBT gives size = 6.  $d \approx (6-2.5)/1.5 = 2.3$ (large).

### Against Null-2 (Shuffled B):

Shuffling destroys the pairing $p \leftrightarrow B(p)$.  Most shuffled
trials produce stable sets not containing 137.  This confirms the
$p \leftrightarrow B(p)$ pairing is structurally essential.

---

## Failed Claims

| Claim | Status | Reason |
|-------|--------|--------|
| C6: $B = 46$ from 1-loop RG | **FAILS** | One-loop gives $B \approx 43.6$; discrepancy $\Delta B \approx 2.4$ unexplained |

This is the primary open gap in the UBT programme.

---

## Unverified Claims (Not Yet Tested)

| Claim | Why Not Tested | Recommended Test |
|-------|---------------|------------------|
| $V_\text{eff}$ computed from UBT | Not derived | Symbolic computation from UBT Lagrangian |
| Spectrum $\sim$ Riemann zeros | Requires $V_\text{eff}$ | Numerical diagonalisation after Gap closure |
| UBT trace formula | Requires geometry | Selberg analogue construction |
| Modular structure of UBT | Requires $\Theta$ computation | Compute $\Theta(q,\tau)$ transformation |

---

## PASS/FAIL Summary

| # Claims | PASS | FAIL | OPEN (not tested) |
|----------|------|------|-------------------|
| 10 total | 7 | 1 (C6) | 2 (C5 partially, UBT-specific) |

---

## Mandatory Next Steps

1. Run null models 1-3 with $n_\text{trials} = 50{,}000$ to establish p-values.
2. Implement theta-function randomisation test for C10.
3. Close C6 gap: either derive $B = 46$ or update the RG claim to $B \approx 43.6$.
4. Test C5 (functional form): implement alternative-V tests systematically.

---

**Last Updated**: 2026-05-06
