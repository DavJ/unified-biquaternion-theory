# Apply overlay: invisibility Hermitian support Gram (2026-08-01)

Base expected: `unified-biquaternion-theory-master(39).zip` after the polynomial-action audit.

## Purpose

This overlay records the exact distinction between zero central visible area
and nonzero internal Hermitian support area for the global Whitney null shell.
It adds a symbolic verifier and regression tests, and opens a noncanonical
support-volume action route without claiming Lorentz-covariant dynamics,
stability, or invisibility.

## Main result

On the inner shell,

\[
dA_\gamma=0,\qquad dA_{\mathsf h}>0,
\]

where

\[
\mathsf h_{\mu\nu}
=\langle\operatorname{ReSc}(E_\mu^\ddagger E_\nu)\rangle_\psi.
\]

The full support Gram is nondegenerate even though the central sharp metric is
degenerate.  A support-volume action is therefore algebraically regular, but
its full Lorentz/gauge covariance and finite-radius stabilisation remain open.

## Validation

Run:

```bash
python tools/verify_invisibility_hermitian_support.py
pytest -q \
  tests/test_invisibility_hermitian_support.py \
  tests/test_invisibility_polynomial_action.py \
  tests/test_spherical_null_shell_theta.py \
  tests/test_biquaternionic_metric_nullity.py \
  tests/test_gr_closure_regressions.py
```

The canonical GR paper is unchanged by this overlay.
