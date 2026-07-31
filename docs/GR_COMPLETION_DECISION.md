# GR completion architecture decision

**Updated:** 31 July 2026

## Pointwise covariant-tetrad route

The pointwise definition

```text
E_mu = N0^(-1/2) D_mu Theta,
g_mu_nu 1 = {E_mu,E_nu}_sharp / 2
```

remains the current canonical metric readout. Its local metric algebra,
rank-ten theorem, connection reconstruction, and torsion bookkeeping are
valid. However, the minimal torsion-free one-connection realization has an
exact concurrent-vector no-go and cannot be the generic curved-GR endpoint.

The split-jet construction is retained only as a local representation theorem.
Because its auxiliary jet can absorb every prescribed tetrad, it does not
select a physical `E[Theta]` and is not a completion of GR dynamics.

## Compact-psi profile candidate

A distinct noncanonical candidate now has a local closure theorem:

- source:
  `research_tracks/T1_GR/free_fiber_completion/gap_10r_free_fiber_embedding_completion.tex`;
- generated review PDF:
  `docs/pdfs/gap_10r_free_fiber_embedding_completion.pdf`.

It uses the full periodic profile of the same field `Theta(x,psi)` and defines
the metric by the normalized translation-invariant profile pairing. Fourteen
orthonormal Lorentz-slice profiles realize `R^(13,1)`. A local free isometric
embedding therefore lifts to one `Theta(x,psi)`, while free rank ten turns the
Regge--Teitelboim stationarity equation into the complete local vacuum
Einstein--Lambda equation.

This closes local smooth representability and gives exact local vacuum
equivalence **within the adopted profile metric plus the composite
Gauss/Einstein--Hilbert action**. It adds no independent tetrad or connection,
but it does not yet derive that action or the profile readout from the older
UBT master dynamics.

## Canonical boundary

The profile route is not canonical under the current wording of Axiom C,
which selects the pointwise central-anticommutator metric and forbids compact
`psi` averaging. Therefore:

1. the candidate stays under `research_tracks/T1_GR/`;
2. canonical files may describe and audit it, but must not silently present it
   as the active metric axiom;
3. promotion requires an explicit author-approved revision of Axiom C and a
   coordinated update of the canonical action, status files, and GR paper;
4. the fixed-frame derivative has now been promoted to a flat,
   pairing-compatible ambient profile connection in
   `gap_10s_covariant_profile_geometry.tex`; before promotion this ambient
   derivative must be explicitly distinguished from the old pointwise spin-lift
   `D_mu`, and the additional profile directions outside the selected
   fourteen-mode block must be shown auxiliary, gauge, constrained, or
   dynamically suppressed.


## Central complex metric channel

The companion note
`research_tracks/T1_GR/free_fiber_completion/gap_10s_covariant_profile_geometry.tex`
proves that the sharp-symmetrised product is central for arbitrary
biquaternions, not only on the real Lorentz slice.  The natural symmetric
extension is therefore

```text
gamma_mu_nu = g_mu_nu + i h_mu_nu
```

with a central complex coefficient.  The exact classical GR branch is the real
Lorentzian sector.  Quaternion-vector information survives in the
antisymmetric bivector channel `Sigma_mu_nu`; it is not a noncommutative
symmetric metric.

## Remaining obligations after possible promotion

1. Derive the profile readout and the coefficients `kappa` and `Lambda` from the
   older UBT master action rather than inserting an Einstein-equivalent action.
2. Prove dynamic selection and stability of a free profile sector.
3. Establish compatibility with the required holomorphic/Jacobi restrictions.
4. Separate the gravitational and internal/matter equations from one unified
   stationarity condition.
5. Treat null patches, global continuation, topology, and explicit global
   black-hole/cosmological representatives.
6. Reconcile the flat ambient profile connection with canonical UBT notation
   and perform a constraint or perturbative degree-of-freedom audit for the
   full profile space.  Local profile-frame covariance itself is conditionally
   closed by the flat-bundle construction.

## Current decision

Do not develop the split-jet construction as the final exact-GR mechanism.
Keep the pointwise route as the audited canonical baseline and the compact-psi
free-fiber construction as the leading noncanonical completion candidate.
Do not revise Axiom C yet: the fixed-frame covariance objection is now
conditionally closed by a flat ambient profile connection, but the canonical
connection split, extra-profile-mode control, and master-action bridge remain.
