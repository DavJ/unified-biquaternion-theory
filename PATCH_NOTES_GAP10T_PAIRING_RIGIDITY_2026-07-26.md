# UBT differential patch — GAP-10T Lorentz-pairing rigidity

**Patch date:** 2026-07-26  
**Base archive:** `unified-biquaternion-theory-master(22).zip`

This root-relative overlay sharpens the canonical-action audit without adding
new independent fields and without claiming closure of full `GAP-10T-DYN` or
`GAP-10D`.

## Main result

The direct connection current

`tau^mu(M) = <M Theta + Theta M^ddagger, D^mu Theta>`

is exact only for the effective Palatini variation in which the tetrad,
metric, volume form, index raising, and `Theta` are held fixed while the
independent Lorentz connection varies.  The full composite `Theta`-only
variation contains additional induced variations and remains open.

The new exact classification solves

`J_M^T G + G J_M = 0`

for a generic real symmetric bilinear form `G` on the Lorentz slice and all
six `sl(2,C)` generators.  Its solution space is one-dimensional:

`G = c diag(-1,1,1,1)`.

Therefore:

- the `sharp` scalar pairing is the unique nonzero symmetric Lorentz-invariant
  slice pairing up to scale;
- the `ddagger` Hilbert--Schmidt pairing restricts to `2 I_4`, is rotation
  invariant, and fails all three boost-invariance checks;
- the already-proved affine spin-current obstruction persists for every
  nonzero nondegenerate symmetric Lorentz-invariant pairing.

## Verdicts

- `GAP-10T-SPIN`: **CLOSED CONDITIONALLY [L1]**, explicitly scoped to the
  fixed-background effective Palatini variation.
- `GAP-10T-FLAT-NOGO`: **CLOSED AS NO-GO [L1]** in that effective branch.
- `GAP-10T-PAIRING-NOGO`: **CLOSED AS NO-GO [L1]**.
- `GAP-10T-DYN`: **NARROWED**, not closed.  Pairing selection alone is no
  longer an admissible escape route.  The remaining task is the full
  composite variation plus a canonically derived non-minimal torsion
  cancellation or translational/relative-bimodule completion with no
  independent propagating fields.
- `GAP-10D`: unchanged, **NARROWED** to the induced-Palatini/gravitational
  coefficient lemma.

## Validation

- `python tools/verify_canonical_spin_current.py`: **20/20 exact checks PASS**.
- `pytest tests/test_canonical_spin_current.py tests/test_claims_consistency.py`:
  **10 tests PASS**.
- All collectable tests except `tests/test_physics_properties.py` pass in two
  deterministic chunks.  That optional module cannot be collected in this
  environment because the `hypothesis` package is not installed.
- All seven changed standalone TeX roots compile successfully with `latexmk`.
- The updated audit PDF and `UBT_GR_Submission.pdf` were regenerated under
  `docs/pdfs/` and visually inspected after rendering.

## Explicit non-claims

This patch does not derive the Hilbert--Palatini action, Newton's constant or
`Lambda`, does not compute the full composite `Theta`-only Euler--Lagrange
variation, and does not establish a torsion-free canonical UBT branch.
