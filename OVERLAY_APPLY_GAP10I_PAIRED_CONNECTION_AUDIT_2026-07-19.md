# UBT GAP-10I paired-connection audit overlay

Date: 2026-07-19
Base archive: `unified-biquaternion-theory-master(16).zip`
Base SHA-256: `64c021a3c928d81c468b930e7b78781746504d0ddcd700467a467c1742ad9462`

Apply by extracting this ZIP into the repository root and allowing replacement of existing files.
No files are deleted by this overlay.

## Scientific status

- Closes `GAP-10I-PAIR-KIN` at L1: Lorentz-slice and metric compatibility reduce the left/right pair to one spin connection, modulo a cancelling common central term.
- Closes `GAP-10I-PAIR-GR` as an L1 no-go: the pure paired branch implies a concurrent/homothetic vector and excludes Schwarzschild with nonzero mass.
- Does **not** close full `GAP-10D`. The remaining exact task is to derive a nontrivial relative bimodule contribution from the canonical action and prove it auxiliary/composite and nonpropagating.

## Validation

Focused repository tests: 15 passed.
Symbolic verifier: all implemented checks passed.
All updated LaTeX targets compiled; rebuilt PDFs are included.
The unrestricted legacy suite has pre-existing failures; its first failure (`test_validate_manifest_from_different_cwd`) reproduces unchanged on the supplied base archive.

## Files

Modified: 34
Added: 5
Deleted: 0
