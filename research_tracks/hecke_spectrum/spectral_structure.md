<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Spectral Structure — UBT Hecke Frequency Spectrum

Analysis of the musical-model frequency ratios against standard
temperaments.  p₀ = 137 is the reference (0 cents).

## Cents deviations and temperament proximity

| p   | cents  | nearest 12-TET (¢) | Δ12-TET (¢) | nearest 24-TET (¢) | Δ24-TET (¢) |
|-----|--------|---------------------|-------------|---------------------|-------------|
| 2 | +1200.0 | +600 | +600.0 | +600 | +600.0 |
| 127 | +276.2 | +300 | -23.8 | +300 | -23.8 |
| 137 | +0.0 | +0 | +0.0 | +0 | +0.0 |
| 139 | -64.9 | -100 | +35.1 | -50 | -14.9 |
| 151 | -553.2 | -600 | +46.8 | -550 | -3.2 |
| 157 | -890.7 | -600 | -290.7 | -600 | -290.7 |

## Log-spacing analysis (consecutive differences in ln(f))

Mean Δln(f) = -0.2415
Variance    = 0.027497
Std dev     = 0.1658

A small variance relative to the mean would indicate log-linear spacing.

## Clustering

Primes 137, 139 are a twin-prime pair and their cents separation is 64.9 ¢ (< 1 semitone).
Primes 151, 157 are also close and cluster within 337.5 ¢ of each other.

## Is the spectrum harmonic?

The frequency ratios do NOT fall on simple integer ratios (harmonic series).
The spectrum is approximately log-monotone in p but not log-linear
(variance / mean² ≈ 0.471).

## Is the spectrum log-linear?

Approximate log-linearity would require constant Δln(f).  The observed standard deviation of 0.1658 compared to
mean -0.2415 gives a coefficient of variation 0.69.
Conclusion: the spectrum is monotone but not strictly log-linear.
