# Validation Report — UBT Hecke Frequency Spectrum

## Model A — Musical (440 Hz base)

| p   | Expected (Hz) | Computed (Hz) | Deviation (Hz) | Error (%) |
|-----|--------------|--------------|----------------|-----------|
| 127 | 422 | 516.09 | +94.09 | +22.30% |
| 137 | 440 | 440.00 | +0.00 | +0.00% |
| 139 | 447 | 423.80 | -23.20 | -5.19% |
| 151 | 484 | 319.65 | -164.35 | -33.96% |
| 157 | 506 | 263.03 | -242.97 | -48.02% |

## Model B — Biological (40 Hz base)

| p   | Expected (Hz) | Computed (Hz) | Deviation (Hz) | Error (%) |
|-----|--------------|--------------|----------------|-----------|
| 127 | 38 | 46.92 | +8.92 | +23.47% |
| 137 | 40 | 40.00 | +0.00 | +0.00% |
| 139 | 41 | 38.53 | -2.47 | -6.03% |
| 151 | 44 | 29.06 | -14.94 | -33.96% |
| 157 | 46 | 23.91 | -22.09 | -48.02% |

## Notes

Expected values in the problem statement are marked as approximate (~).
Deviations reflect differences between the exact V(p, p) computation
and the rounded reference values.

## Discrepancy Analysis

The expected values and the literal computation diverge significantly because:

1. **Sign convention**: In V(q, p) = q² − ((p+1)/3)·q·ln(q), the potential
   is *more negative* for larger p (the linear term dominates for large q = p).
   Therefore V(p) decreases as p increases, making ΔV(p) = V(p) − V(p₀) < 0
   for p > p₀.  The expected values assume ΔV > 0 for p > p₀, which corresponds
   to a reversed-sign convention: ΔV_alt(p) = V(p₀) − V(p).

2. **Evaluation point**: The expected values match closely (within ~3%) the
   formula V evaluated at the *fixed coordinate q = p₀* rather than q = p:
       V(q = p₀, p) = p₀² − ((p+1)/3)·p₀·ln(p₀)
   This is linear in p, giving ΔV_alt(p) = ((p₀+1)/3 − (p+1)/3)·p₀·ln(p₀)
   = (p₀ − p)/3 · p₀·ln(p₀), which is proportional to (p₀ − p).

3. **Numerical comparison with the alternative formula** (V at q = p₀, reversed sign):

| p   | ΔV_alt_norm | f_alt_musical (Hz) | Expected (Hz) | Match? |
|-----|------------|-------------------|---------------|--------|
| 127 | −0.074     | ~407              | ~422          | partial |
| 137 | 0.000      | 440.00            | 440           | ✓      |
| 139 | +0.015     | ~447              | ~447          | ✓      |
| 151 | +0.104     | ~486              | ~484          | ✓      |
| 157 | +0.148     | ~505              | ~506          | ✓      |

Primes p ≥ 139 match the expected values within ~2 Hz under the alternative
convention.  Prime p = 127 remains discrepant (~15 Hz), suggesting the
approximate expected values were generated with yet another rounding or an
inconsistent formula.

**Conclusion**: The literal formula (q = p) is used throughout this analysis.
The expected values in the task specification appear to have been estimated
using a linearised approximation with a reversed-sign convention.  The
validated figures in the tables above reflect the mathematically exact result
of the stated potential.
