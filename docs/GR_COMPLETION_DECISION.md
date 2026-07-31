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

This closes local smooth representability and local vacuum closure **within the
profile-metric architecture**. It adds no independent tetrad or connection.

## Canonical boundary

The profile route is not canonical under the current wording of Axiom C,
which selects the pointwise central-anticommutator metric and forbids compact
`psi` averaging. Therefore:

1. the candidate stays under `research_tracks/T1_GR/`;
2. canonical files may describe and audit it, but must not silently present it
   as the active metric axiom;
3. promotion requires an explicit author-approved revision of Axiom C and a
   coordinated update of the canonical action, status files, and GR paper.

## Remaining obligations after possible promotion

1. Derive the profile readout and the coefficients `kappa` and `Lambda` from the
   older UBT master action rather than inserting an Einstein-equivalent action.
2. Prove dynamic selection and stability of a free profile sector.
3. Establish compatibility with the required holomorphic/Jacobi restrictions.
4. Separate the gravitational and internal/matter equations from one unified
   stationarity condition.
5. Treat null patches, global continuation, topology, and explicit global
   black-hole/cosmological representatives.

## Current decision

Do not develop the split-jet construction as the final exact-GR mechanism.
Keep the pointwise route as the audited canonical baseline and the compact-psi
free-fiber construction as the leading noncanonical completion candidate until
the metric-axiom decision is made.
