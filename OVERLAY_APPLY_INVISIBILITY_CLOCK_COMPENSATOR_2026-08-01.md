# Apply overlay: invisibility clock-compensated support Gram (2026-08-01)

Base expected: `unified-biquaternion-theory-master(40).zip` after the Hermitian-support overlay.

## Purpose

This overlay narrows the Lorentz-frame covariance gap of the positive internal
support Gram used by the speculative Whitney null-shell track.  It constructs a
Hermitian clock coefficient and compensator from the same `Theta` by projecting
onto the shell's dedicated clock Fourier profile.

## Main result

Under the standard local paravector congruence

\[
E_\mu\mapsto S E_\mu S^\ddagger,
\qquad S\in SL(2,\mathbb C),
\]

the compensated Gram

\[
\mathsf h^{\rm clk}_{\mu\nu}
=\frac12\left\langle\operatorname{ReTr}\left(
E_\mu^\ddagger\widehat{\mathcal N}_\Theta^{-1}
E_\nu\widehat{\mathcal N}_\Theta^{-1}
\right)\right\rangle_\psi
\]

is invariant and positive.  On the explicit Whitney shell,

\[
\mathcal C_\Theta=t\mathbf1,
\qquad
\mathcal N_\Theta=\mathbf1,
\]

so the compensated Gram equals the previously verified Hermitian support Gram.
The same construction gives an invariant scalar clock `T_Theta=t` and a
regular Lorentzian internal support tensor.

## Status limitation

This is an exact conditional theorem for the selected shell clock mode.  The
clock Fourier projector is not yet uniquely derived from the UBT master action,
full `psi`-dependent profile-frame covariance is not proved, and the full paired
left/right bimodule connection remains open.  No on-shell stability or
invisibility claim is made.

## Validation

Run:

```bash
python tools/verify_invisibility_clock_compensator.py
pytest -q \
  tests/test_invisibility_clock_compensator.py \
  tests/test_invisibility_hermitian_support.py \
  tests/test_invisibility_polynomial_action.py \
  tests/test_spherical_null_shell_theta.py \
  tests/test_biquaternionic_metric_nullity.py \
  tests/test_metric_lock.py
```

The canonical GR paper is not modified by this overlay.
