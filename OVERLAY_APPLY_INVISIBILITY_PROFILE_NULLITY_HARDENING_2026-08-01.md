# Apply note — invisibility profile-nullity hardening

This repository-root-relative overlay hardens the speculative invisibility
track. It does not modify Axiom C and does not make an engineering claim.

## Changes

- proves the pointwise Witt-index obstruction: a completely metric-null jet in
  one copy of `C tensor H` has rank at most two;
- records an exact UBT-specific escape in the full `psi`-profile space;
- adds four independent Fourier-profile jets with zero averaged central metric
  and nonzero averaged biquaternionic bivector channel;
- adds exact verifier and regression checks;
- keeps action, integrability, stability, and scattering claims open.

## Verify

```bash
python tools/verify_biquaternionic_metric_nullity.py
pytest -q tests/test_biquaternionic_metric_nullity.py
```
