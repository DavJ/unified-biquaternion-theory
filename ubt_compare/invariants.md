# UBT Comparison: Shared Invariants

These invariants are candidates for A/B comparison between the two formulations.

## Invariants to Compare

| Invariant | Symbol | Description |
|---|---|---|
| Field determinant | det Θ | Complex determinant of the biquaternionic field matrix |
| Log-trace | Tr(log Θ) | Trace of the matrix logarithm of Θ |
| Log-det (real part) | Re(log det Θ) | Real part of the complex log-determinant |
| Log-det (imaginary part) | Im(log det Θ) | Imaginary part; encodes phase winding |
| Hermitian product | Θ†Θ | Positive semi-definite; encodes amplitude geometry |
| Unitary decomposition | U in Θ = U·H | Unitary factor from polar decomposition |
| Hermitian decomposition | H in Θ = U·H | Hermitian (positive) factor from polar decomposition |

## What Must Match Across Formulations

For the two theories to make compatible physical predictions in the classical/observational
sector, the following invariants must agree (within numerical precision) when evaluated
at the same physical configuration:

- `Re(det Θ)` in the metric projection limit (real sector)
- `Θ†Θ` at low-energy / long-wavelength limit
- The unitary factor U at tree level (gauge structure)

## What Is Allowed to Differ

The following invariants may legitimately differ between the formulations; a measured
difference here is diagnostic rather than a contradiction:

- `Im(log det Θ)` — phase winding; chronofactor formulation has an extra winding mode
- `Tr(log Θ)` off-shell — chronofactor generates an extra imaginary-time contribution
- Short-wavelength / UV structure of `Θ†Θ`

## Measurement Protocol

For each candidate observable O:

1. Compute O in `ubt_with_chronofactor` formulation.
2. Compute O in `ubt_no_chronofactor` formulation.
3. Record |O_with - O_no| / max(|O_with|, |O_no|, ε).
4. Flag if relative difference > threshold (default: 1e-6 for "must match" invariants).

Implement scripts for this in `scripts/`.
