# Patch notes: GAP-10I torsionful local representer

**Date:** 2026-07-19  
**Baseline:** `unified-biquaternion-theory-master(17).zip`

## Mathematical correction

The prior concurrent-vector obstruction was over-scoped.  It follows from
`D_mu Theta=sqrt(N0)E_mu` only after imposing the torsion-free connection
`Omega=Omega_LC`.  It is therefore a rigorous `K=0` no-go, not a no-go for the
same pure Lorentz left/right pairing with arbitrary metric-compatible
contortion.

## Exact local construction

On a sufficiently small non-null Gaussian patch choose `rho != 0` with
`g^{-1}(d rho,d rho)=epsilon` and define

```text
V^mu = epsilon rho nabla^mu rho,
W_{mu nu} = g_{mu nu} - nabla^LC_mu V_nu,
K_{nu mu rho} = (W_{mu nu} V_rho - V_nu W_{mu rho}) / V^2.
```

Then `K_{nu mu rho}=-K_{rho mu nu}` and therefore `Gamma=Gamma_LC+K` is
metric-compatible.  Exact contraction gives

```text
K^nu_{mu rho} V^rho = W_mu^nu,
nabla^Gamma_mu V^nu = delta_mu^nu.
```

With `Theta=sqrt(N0)V^a u_a`, `A=Omega(e,K)`, and
`B=-Omega(e,K)^ddagger`, the tetrad postulate yields exactly

```text
D_mu Theta = sqrt(N0) E_mu.
```

Thus every smooth Lorentzian tetrad has a local single-Theta representer
without independent `A`, `B`, or a required relative pair.  The construction
also applies on every exterior Schwarzschild patch `r>2M`; it concerns the
vacuum geometry and does not rely on interpreting the source as a physically
exactly nonrotating black hole.

## Honest status

- `GAP-10I-TORSION-LOCAL: CLOSED LOCALLY [L1]`.
- `GAP-10I-PAIR-GR: CLOSED AS A TORSION-FREE NO-GO [L1]`.
- `GAP-10I-2S`: not required for local kinematic representability; retained as
  an optional torsion-free composite/auxiliary route.
- `GAP-10I-CURVED`: local kinematics closed; dynamics/global part narrowed.
- `GAP-10T-DYN`, `GAP-10D`, and `GAP-U2Theta`: not closed.

The theorem does **not** show that the canonical UBT action selects this
contortion, that its induced torsion satisfies phenomenological bounds, that
it is algebraically eliminated by the full field equations, or that one patch
extends through `V^2=0`, Gaussian caustics, horizons, or nontrivial topology.

## New proof, verifier, and test

- `canonical/gr_closure/gap_10i_torsionful_local_representer.tex`
- `tools/verify_gap_10i_torsionful_local_representer.py`
- `tests/test_gap_10i_torsionful_local_representer.py`
- `docs/pdfs/gap_10i_torsionful_local_representer.pdf`

The symbolic verifier checks metric-compatible antisymmetry, exact contraction
`K(V)=W`, the full identity on a non-flat warped Lorentzian metric, and the
Schwarzschild proper-radial Gaussian identities.

## Validation

- 35 targeted architecture, claim-consistency, GR-closure, and publication
  tests passed.
- `verify_gap_10i_paired_connection.py` and
  `verify_gap_10i_torsionful_local_representer.py` both report all implemented
  checks passed.
- 12 affected standalone LaTeX roots compiled with zero build failures.
- The new four-page theorem and the revised GR manuscript were rendered and
  visually checked for clipping, overlaps, and broken glyphs.
- The unrestricted repository suite still has pre-existing failures; its first
  failure, `test_validate_manifest_from_different_cwd`, reproduces unchanged on
  the untouched `(17)` baseline.
