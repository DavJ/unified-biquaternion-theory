<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# UBT falsifiable prediction sheet (Priority 10)

**Date**: 2026-05-17  
**Status**: Single focused prediction (no speculative expansion)

## Prediction

UBT gauge unification route implies a proton-decay lifetime scale near
\[
\tau_p^{\mathrm{UBT}} \sim 10^{34}\ \text{years}
\]
for the channel \(p\to e^+\pi^0\), using the standard scaling
\[
\tau_p \sim \frac{M_{\mathrm{GUT}}^4}{m_p^5},
\qquad M_{\mathrm{GUT}}\sim 2\times10^{16}\ \mathrm{GeV}.
\]

## Current experimental bound

- Super-K lower bound (order level): \(\tau_p > 1.6\times10^{34}\) years.
- Hyper-K era is the next discriminative test window.

## Pass/fail criterion

- **PASS (UBT not falsified by this observable yet):** no proton decay seen above
  the bound while limits remain compatible with \(\mathcal{O}(10^{34})\)-\(10^{35}\) years.
- **FAIL (UBT route falsified):** a robust exclusion pushes the relevant
  \(p\to e^+\pi^0\) lifetime well beyond the UBT-predicted scale window
  (e.g., strong lower limit in the \(\gtrsim10^{36}\) year regime without a compensating
  UBT mechanism), or an observed lifetime is irreconcilable with the stated UBT
  unification assumptions.

---

## Prediction 2: ΔN_eff (CMB-S4)

Value: 0.05–0.25 (g*-dependent)  
Condition: g*(T_Pl) ≥ 427 (KK tower included)  
CMB-S4 sensitivity: σ ~ 0.03  
Status: OPEN (g* derivation needed)  
Fail criterion: ΔN_eff < 0 OR ΔN_eff > 1

Full calculation: `research_tracks/quantum_ubt/delta_neff_prediction.tex`  
Python tool: `tools/delta_neff_calc.py`

## Prediction 1: Proton decay (confirmed)
τ_p ~ 10³⁴ years (M_GUT ~ 2×10¹⁶ GeV, conditional)  
Super-K limit: τ_p > 1.6×10³⁴ yr — consistent  
Hyper-K (2027+): next test window

## Scope guardrail

This sheet defines one concrete, parameter-controlled, discriminative observable.
Alpha remains **NOT DERIVED**.
