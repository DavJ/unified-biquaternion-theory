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

## Prediction 2: \(\Delta N_{\rm eff}\) (CMB-S4)

**Date**: 2026-05-17

UBT KK sector (SU(2) Scherk-Schwarz twist, \(N_{\rm eff}=12\) modes decoupled at
\(T\sim M_{\rm Pl}\)) contributes to the effective number of relativistic
degrees of freedom via the standard relic formula:
\[
  \Delta N_{\rm eff}^{(\rm mode)} =
  \left(\frac{43/4}{g_*(T_{\rm dec})}\right)^{4/3}
  \approx 0.047
  \quad [g_*(T_{\rm dec}) = 106.75].
\]

### Pass/fail criterion

- **PASS:** CMB-S4 detects \(\Delta N_{\rm eff}\) consistent with per-mode prediction.
- **FAIL:** \(\Delta N_{\rm eff} < 0\) or \(\Delta N_{\rm eff} > 1\) would falsify UBT KK sector.
- **STATUS:** [OPEN — total from 12 modes \(\approx 0.562\) in tension with Planck+ACT;
  mode stability analysis pending]

Full calculation: `research_tracks/quantum_ubt/delta_neff_prediction.tex`  
Python tool: `tools/delta_neff_calc.py`

## Scope guardrail

This sheet defines one concrete, parameter-controlled, discriminative observable.
Alpha remains **NOT DERIVED**.
