# Patch notes: holomorphic on-shell rank criterion

Baseline: `unified-biquaternion-theory-master(36).zip`
Date: 2026-07-27

## Purpose

Continue the single canonical chain

`Theta -> E_mu = D_mu Theta / sqrt(N0) -> metric and generalized-Dirac lift`

without reactivating the historical spinor-current tetrad.

## New exact theorem

For real tetrad variables `e in R^16`, nonmetric first-jet variables `z`, and
real constraints `F(e,z)=0`, admissible tetrad variations are

`A = {delta e : F_e delta e lies in im F_z}`.

The metric rank on the equation manifold is exactly the rank of `D_e g`
restricted to `A`.

Consequences:

- if `F_z` is surjective, every tetrad variation lifts to the equation
  manifold and metric rank 10 is preserved;
- if eight independent real constraints act only on the 16 tetrad
  coefficients, the constrained metric rank is at most eight.

This proves the correct criterion and a rank-budget no-go. It does not yet
compute the action-derived holomorphic UBT Jacobian.

## Holomorphy boundary

Under the convention `tau=t+i_c psi`, strict covariant holomorphy gives

`D_psi Psi = i_c D_t Psi`

when the connection preserves the complex-time structure. Therefore
`D_psi Psi` cannot be treated as an independent auxiliary slot in the final
on-shell proof. The next required calculation is the real Jacobian `(F_e,F_z)`
of the actual action-derived equation.

## Hygiene repair

The following accidentally reintroduced active files are removed. Their dated
historical copies remain under
`research_tracks/history/legacy_spinor_current_tetrad_2026-07-26/`.

- `research_tracks/dual_sector_clifford5/dual_sector_cl5_rank_status.md`
- `tools/verify_dual_sector_cl5_rank.py`
- `tests/test_dual_sector_cl5_rank.py`

## Validation

- exact SymPy verifier: passed with no floating tolerances;
- targeted canonical/geometry suite: 78 tests passed;
- standalone proof PDF: built and visually inspected, 5 pages;
- full suite: collection blocked by missing optional package `hypothesis`;
  excluding that file, the run reached 10% without a recorded failure before
  the 300-second execution limit.
