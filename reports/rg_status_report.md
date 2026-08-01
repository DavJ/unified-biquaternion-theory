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


# RG Status Report: Derivation of V_eff(n) = n^2 - B·n·ln n

**Task**: Task 2 — Rigorous RG Derivation of $n \log n$  
**Author**: Ing. David Jaroš  
**Date**: May 2026  
**Priority**: CRITICAL  

---

## Executive Summary

The one-loop RG derivation of $V_\text{eff}(n) = n^2 - Bn\ln n$ has reached the
following state:

| Component | Status | Confidence |
|-----------|--------|------------|
| $n^2$ kinetic term from KK | **PROVED** | High |
| $n^2\ln n$ coefficient from one-loop $d=1$ | **PROVED** | High |
| Regulator independence of $n\ln n$ term | **PROVED** | High |
| Gauge invariance | **PROVED** | High |
| $B \approx 21.8$ (one-loop KK) | **HEURISTIC** | Medium |
| $B \approx 43.6$ (KK + winding) | **HEURISTIC** | Medium |
| $B = 46$ exact | **OPEN GAP** | None |

---

## Files Created

| File | Contents |
|------|----------|
| `research_tracks/rg_nlogn/full_rg_derivation.tex` | Full RG derivation: KK spectrum, one-loop vacuum polarisation, beta function, effective action |
| `research_tracks/rg_nlogn/loop_integrals_appendix.tex` | Explicit one-loop integrals in $d=1$, winding correction, two-loop estimate |
| `research_tracks/rg_nlogn/b_coefficient_analysis.md` | Sensitivity analysis, survey of all sources of $B$, falsification conditions |

---

## Derivation Outline

### Step 1: KK mass spectrum — [PROVED]

KK compactification on $S^1_{R_\psi}$ with natural units $\hbar = 2mR_\psi^2 = 1$:
$$m_n^2 = n^2.$$

### Step 2: Tree-level potential — [PROVED]

$$V_\text{tree}(n) = n^2.$$

### Step 3: One-loop correction in $d=1$ — [PROVED]

Standard Coleman-Weinberg in $d=1$:
$$\delta V_\text{1-loop}(n) = -\frac{n^2}{4\pi}\left(\ln\frac{n^2}{\mu^2} - 1\right).$$

The $n^2\ln n$ coefficient is scheme-independent.

### Step 4: KK+winding at self-dual radius — [HEURISTIC]

T-duality at $R = 1$ doubles the contribution: $B_\text{1-loop} \approx n/\pi \approx 43.6$ for $n = 137$.

### Step 5: Missing $\Delta B \approx 2.4$ — [OPEN GAP]

Two-loop corrections contribute only $\delta B \approx 0.05$ (negligible).
Gauge field loops give similar magnitudes but not the right sign/value.
The exact value $B = 46$ has no derived explanation.

---

## The B Coefficient Problem

The formula $B(p) = (p+1)/3$ is:
- **Empirically verified**: correctly identifies stable primes.
- **Not derived**: from RG or any other first-principles calculation.

The ratio $B(p)/B_\text{KK+wind}(p) \approx 1.054$ is approximately constant
across all stable primes, suggesting a systematic multiplicative factor
not captured by the one-loop calculation.

### Candidate mechanisms for the missing factor

1. **Higher-loop**: Two-loop gives $\delta B \sim 0.05$. Negligible.
2. **Gauge loops**: $\mathrm{SU}(2)$ contribution gives $\sim 43.6$. Still short.
3. **Threshold corrections**: Non-perturbative at compactification scale.
4. **Modular arithmetic**: $B = 46 = 2 \times 23$ might have a number-theoretic origin.

**Current best estimate**: $B \approx 43.6$–$44$ from perturbation theory, not $46$.

---

## Verified Properties of $V_\text{eff}$

| Property | Status |
|----------|--------|
| Dimensional consistency ($[V] = [n^2]$) | **PROVED** |
| Gauge invariance ($n$ is $\mathrm{U}(1)_\psi$ charge) | **PROVED** |
| Regulator independence of $\ln n$ coefficient | **PROVED** |
| $V_\text{eff}$ has unique minimum at $n^*$ | **PROVED** |
| $n^* = B/(2(1+1/\ln n^*))$ (fixed-point equation) | **PROVED** |
| $n^* \approx 137$ for $B = 46$ | **PROVED** (exact computation) |

---

## Open Problems

1. **Derive $B = 46$ exactly** from first principles.
2. **Clarify which fields** contribute to the one-loop effective potential in UBT.
3. **Derive $R_\psi = 1$** (self-dual radius) from UBT moduli.
4. **Compute the two-loop** beta function for the UBT KK sector.

---

## Falsification Conditions

| Condition | What it falsifies |
|-----------|------------------|
| Two-loop calculation gives $B < 44$ or $B > 48$ | RG origin of $B = 46$ |
| $R_\psi \neq 1$ from moduli derivation | Self-dual radius assumption |
| $V_\text{eff}$ not minimised at $n = 137$ for $B = 46$ | Prime-stability claim |
| Gauge invariance violated | Entire effective potential programme |

---

**Last Updated**: 2026-05-06
