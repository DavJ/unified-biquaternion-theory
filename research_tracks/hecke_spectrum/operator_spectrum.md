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

# Operator / Spectrum Connection — UBT Hecke ΔV

## Do ΔV values behave like eigenvalues?

The ΔV spectrum has 6 values corresponding to the 6 stable primes.
A Hilbert–Pólya interpretation requires eigenvalues of a self-adjoint
operator.  This requires at minimum that the spectrum be real (satisfied)
and that spacing statistics deviate from Poisson (uncorrelated levels).

## Nearest-neighbour spacings

| Pair (pᵢ, pᵢ₊₁) | |ΔV(pᵢ₊₁) − ΔV(pᵢ)| | s_norm |
|------------------|----------------------|--------|
| (2, 127) | 10122.6488 | 2.9491 |
| (127, 137) | 2116.6847 | 0.6167 |
| (137, 139) | 450.5678 | 0.1313 |
| (139, 151) | 2897.2480 | 0.8441 |
| (151, 157) | 1574.8755 | 0.4588 |

Mean spacing   : 3432.4050
Std dev        : 3438.5649

## Comparison to Poisson and Wigner-Dyson (GOE)

| s_norm | Poisson p(s) | Wigner-Dyson p(s) |
|--------|-------------|-------------------|
| 2.949 | 0.0524 | 0.0050 |
| 0.617 | 0.5397 | 0.7186 |
| 0.131 | 0.8770 | 0.2034 |
| 0.844 | 0.4299 | 0.7577 |
| 0.459 | 0.6320 | 0.6109 |

## Comparison to Riemann zeta zeros

The non-trivial zeros of ζ(s) on the critical line are known to follow
Wigner-Dyson (GUE) statistics.  Our sample (5 spacings from 6 primes)
is too small for a statistically meaningful comparison.

## Conclusion

- The ΔV spectrum is real, monotone in p (for primes > 2), and shows
  irregular spacing, which is neither clearly Poisson nor Wigner-Dyson.
- The sample size is insufficient for formal spectral classification.
  Reliable nearest-neighbour spacing statistics typically require N ≥ 50
  eigenvalues; the current set of 6 primes yields only 5 spacings.
- A proto Hilbert–Pólya structure cannot be confirmed or excluded from
  this data alone.
- Extension to all primes up to ~1000 (roughly 170 primes) would be
  required for a statistically meaningful test against Poisson or
  Wigner-Dyson distributions.
