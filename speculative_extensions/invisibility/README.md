# Invisibility / biquaternionic null-geometry track

**Status:** SPECULATIVE / NON-CANONICAL / ACTIVE RESEARCH PROGRAM  
**Rebased:** 2026-08-01

This directory preserves David Jaroš's 2013--2015 geometric-invisibility
research intuition and restates it in the current covariant-tetrad language.
It does **not** claim that an invisibility device exists or that UBT already
provides an engineering design.

## Current geometric hierarchy

The canonical tetrad is

\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta.
\]

The full unsymmetrised biquaternionic bilinear is

\[
\mathfrak G_{\mu\nu}:=E_\mu^\sharp E_\nu
=\gamma_{\mu\nu}\mathbf 1+\Sigma_{\mu\nu},
\]

where

\[
\gamma_{\mu\nu}\mathbf 1
=\tfrac12(\mathfrak G_{\mu\nu}+\mathfrak G_{\nu\mu}),
\qquad
\Sigma_{\mu\nu}
=\tfrac12(\mathfrak G_{\mu\nu}-\mathfrak G_{\nu\mu}).
\]

- `gamma_mu_nu` is symmetric and central (generally complex).
- On the classical Lorentz slice it becomes the real GR metric `g_mu_nu`.
- `Sigma_mu_nu` is antisymmetric and genuinely biquaternionic.
- The full `mathfrak G_mu_nu` is retained; the GR metric is only its central
  symmetric projection.

The canonical GR documents reserve the word **metric** for the central
symmetric object because it has an ordinary determinant, inverse, signature,
and Levi--Civita connection. This track asks whether the full
`mathfrak G_mu_nu` admits a broader metric interpretation relevant to null or
invisible phases.

## Why the biquaternionic part disappears from ordinary `ds^2`

For commuting real coordinate differentials,

\[
\mathfrak G_{\mu\nu}\,dx^\mu dx^\nu
=\gamma_{\mu\nu}\,dx^\mu dx^\nu\,\mathbf1,
\]

because `Sigma_mu_nu` is antisymmetric while `dx^mu dx^nu` is symmetric.
Thus the biquaternionic information has not vanished from the geometry; it is
invisible to the ordinary quadratic line element.

A genuinely biquaternionic interval would therefore require at least one of:

1. an ordered or noncommutative differential calculus;
2. a separate oriented-area/two-form observable carrying `Sigma_mu_nu`;
3. a different noncentral Hermitian metric candidate with a well-defined
   determinant, inverse, covariance, and GR limit.

None of these is canonical yet.

## Active hypotheses

The track distinguishes three nullity notions:

1. **curve-null:** `gamma(v,v)=0` for a particular tangent vector;
2. **volume-null:** `det(gamma)=0`;
3. **metric-null but algebra-active:** `gamma_mu_nu=0` while
   `Sigma_mu_nu != 0`.

Only the latter two are candidates for a genuinely hidden geometric phase.
Neither by itself proves physical invisibility. Operational invisibility also
requires the visible-sector mixing and exterior scattering/back-reaction to
vanish.

A pointwise `gamma_mu_nu=0` jet in one copy of `C tensor H` has rank at most
two, because the central complex bilinear has Witt index two.  The full
`psi`-profile space escapes this finite-dimensional obstruction: four
independent Fourier profiles can have zero averaged central metric while the
averaged `Sigma` channel remains nonzero.  This profile witness is algebraic,
not yet an on-shell spacetime or device.

For a spherical shell the two-direction pointwise limit is not an obstruction:
the tangent plane of `S^2` is two-dimensional. The dedicated shell candidate
therefore imposes `gamma_AB=0` only for `A,B in {theta,phi}` at the inner
boundary while retaining `Sigma_theta_phi != 0`.

## Files

- `BIQUATERNIONIC_METRIC_NULLITY_PROGRAM.md` — current research statement,
  algebraic witness, action questions, and falsification criteria.
- `PROFILE_METRIC_NULL_WITNESS.md` — exact pointwise rank obstruction and
  rank-four profile-space algebraic witness.
- `SPHERICAL_TANGENTIAL_NULL_SHELL.md` — explicit spherical candidate with
  a central-metrically null angular surface and nonzero `Sigma_theta_phi`.
- `STATUS_REBASE_2026-08-01.md` — relationship of the older ST-1--ST-5 files to
  the current central-anticommutator architecture.
- `st1_...` through `st5_...` — historical speculative analyses retained for
  provenance; they are not current canonical derivations.

## Promotion barrier

Nothing in this directory may be promoted until all of the following are
provided:

- a covariant definition of the proposed full metric/volume object;
- a well-defined action at degeneracy;
- an explicit nontrivial on-shell solution;
- a visible-sector coupling theorem;
- exterior scattering and stability calculations;
- a falsifiable laboratory or astronomical signature.
