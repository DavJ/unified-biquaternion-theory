# Patch notes — alpha non-zero electroweak minimum closure

Adds:

- `research_tracks/T3_ALPHA/theta0_nonzero_minimum_theorem.tex`
- `docs/reports/alpha_nonzero_ew_minimum_closure.md`

Updates:

- `research_tracks/T3_ALPHA/alpha_derivation_complete.tex`
- `research_tracks/T3_ALPHA/theta0_electroweak_vacuum_orbit_theorem.tex`

The new theorem proves that if the projected UBT electroweak potential has the
stable symmetry-breaking form

```math
V_EW = V0 - mu_EW^2 Phi^dagger Phi + lambda_EW (Phi^dagger Phi)^2,
lambda_EW > 0,
mu_EW^2 > 0,
```

then the vacuum is non-zero and satisfies

```math
Phi^dagger Phi = mu_EW^2/(2 lambda_EW) = v^2/2.
```

Combined with the previous Theta0 vacuum-orbit theorem, EM projection theorem,
and compact-U(1) modular identification, this closes the low-energy
electroweak part of the alpha proof condition.

Remaining UV condition:

```math
derive mu_EW^2 > 0 from canonical S[Theta].
```

This patch intentionally keeps that condition explicit and does not claim a
full UV Higgs-sector derivation.
