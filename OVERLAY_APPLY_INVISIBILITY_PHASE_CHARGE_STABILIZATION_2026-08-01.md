<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Apply overlay: invisibility phase-charge finite-scale stabilisation (2026-08-01)

Base expected: `unified-biquaternion-theory-master(41).zip` after the clock-compensator overlay.

## Purpose

This overlay adds the first nontrivial finite-scale stabilisation mechanism for
the speculative Whitney tangential-null shell.  It promotes no canonical UBT
claim and introduces no new fundamental field.

## Main result

The existing Whitney `psi=+/-1` block is given a common collective phase,

\[
\Theta_W\mapsto e^{i\alpha(t)}\Theta_W.
\]

Because this block lies in a totally sharp-null plane, the central visible
metric remains exactly null.  The clock-compensated Hermitian support Gram gives
the phase a positive moment of inertia.  In the minimal reduced model,

\[
E_Q(\chi)=\sigma a_W\chi^2+
\frac{Q_\alpha^2}{2\kappa_\alpha i_W\chi^4}
\]

has the unique strict minimum

\[
\chi_*^6=
\frac{Q_\alpha^2}{\sigma a_W\kappa_\alpha i_W}.
\]

Thus a conserved relative profile-phase charge prevents collapse of the
internal Whitney support scale.

## Status limitation

The theorem is exact only in the stated collective-coordinate reduced action.
The phase kinetic term and exact `U(1)` symmetry are not yet derived from the
UBT master action.  The current shell ansatz also treats the support amplitude
and the exterior radii as independent.  A physical finite-radius theorem
therefore additionally requires a radial bulk equation that locks
`chi = zeta R`.  Full perturbative stability, finite bulk energy, and zero
exterior scattering remain open.

## Validation

Run:

```bash
python tools/verify_invisibility_phase_charge_stabilization.py
pytest -q \
  tests/test_invisibility_phase_charge_stabilization.py \
  tests/test_invisibility_clock_compensator.py \
  tests/test_invisibility_hermitian_support.py \
  tests/test_invisibility_polynomial_action.py \
  tests/test_spherical_null_shell_theta.py \
  tests/test_gr_closure_regressions.py
```

The canonical GR paper is not modified by this overlay.
