<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

### Derivation
N_eff = 12 KK modes [L1], decoupled at T_dec ~ M_Pl
g*(T_Pl) = 106.75 (SM) + 2 (grav) + 24 (KK scalars)
         + 60 (KK gravitons) + 36 (KK gauge) + 21 (KK fermions)
         = 249.75 [NUM]

ΔN_eff = 12 × (43/4) × (3.909/249.75)^(4/3) ≈ 0.477 [NUM]

### Status
- ΔN_eff ≈ 0.477 for g*=250: [CONDITIONAL TENSION with Planck 0.28]
- ΔN_eff ≈ 0.247 for g*=427 (extended): [CONDITIONAL OK]
- g*(T_Pl) derivation: [OPEN]
- CMB-S4 sensitivity: σ ≈ 0.03 (2027+)

### Fail criterion
If ΔN_eff < 0 or ΔN_eff > 1 (future CMB): UBT KK sector excluded.

---

## Prediction 1: Proton decay τ_p (channel p → e⁺π⁰)

### Derivation (exact)
Parameters:
- M_GUT = 2×10¹⁶ GeV [CONDITIONAL on UBT EW-1b]
- α_GUT = 1/40 (SU(5) unification coupling)
- m_p = 0.938 GeV

Proton lifetime from dimension-6 operators:
```
τ_p [GeV⁻¹] = M_GUT⁴ / (α_GUT² × m_p⁵)
             = (2×10¹⁶)⁴ / ((1/40)² × (0.938)⁵)
             = 3.526×10⁶⁸ GeV⁻¹

τ_p [s] = 3.526×10⁶⁸ × ħ = 3.526×10⁶⁸ × 6.582×10⁻²⁵ s·GeV
        = 2.32×10⁴⁴ s

τ_p [years] = 2.32×10⁴⁴ / (3.156×10⁷) ≈ 7.4×10³⁶ years
```

### Status
- τ_p ~ 7.4×10³⁶ years [CONDITIONAL on M_GUT]
- Super-Kamiokande lower bound: τ_p > 1.6×10³⁴ years [EXP]
- **CONSISTENT** (UBT prediction above experimental limit)
- Hyper-Kamiokande sensitivity (2027+): ~10³⁵ years

### Fail criterion
τ_p < 10³⁴ years (future experiment) → M_GUT < 2×10¹⁶ GeV
→ UBT EW-1b conditional result excluded.

### Note
The standard SU(5) prediction gives τ_p ~ 10³¹ years (excluded by
Super-K). UBT predicts longer lifetime due to higher M_GUT.

---

## Scope guardrail

This sheet defines one concrete, parameter-controlled, discriminative observable.
Alpha remains **NOT DERIVED**.
