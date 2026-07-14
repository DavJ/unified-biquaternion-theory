# Differential patch: pure UBT GR closure

Date: 2026-07-14

## Purpose

Replace the invalid idea that the non-real part of a scalar trace automatically supplies missing Einstein equations with a rigorous derivation based on the existing complex-time fiber of `Theta(q,tau)`.

## New proof track

- `canonical/gr_closure/pure_ubt_fiber_closure.tex`
- `canonical/gr_closure/PURE_UBT_CLOSURE_STATUS.md`
- `tools/verify_pure_ubt_fiber_closure.py`
- `tests/test_pure_ubt_fiber_closure.py`

## Central result

A single `psi=0` section of a biquaternion-valued field has an eight-real-dimensional value space and only four normal metric-generating directions. This is insufficient for a generic pointwise derivation of all Einstein equations.

The complete existing `psi` profile belongs to an infinite-dimensional function space. With the classical metric defined by normalized `psi` averaging, ten independent normal second-derivative modes can exist. On this explicitly defined fiber-free sector, the pure-Theta gravitational variation implies the Einstein equation.

## Remaining gap

The local kinematic/rank part of GAP-10 is closed for the fiber-completed projection. The remaining gap is the **single-action separation problem**: deriving the direct internal Theta equation and the metric closure equation as independent projections of one canonical UBT stationarity condition, rather than imposing the direct internal equation as an additional on-shell condition.


## Important limitation added after proof audit

The patch does **not** claim that every prescribed GR metric field already has an integrable, holomorphic, on-shell representation by the selected Jacobi-theta sector. Pointwise Lorentzian Gram representability is proved, but neighbourhood/global representability is tracked separately as `GAP-10R`. The compact-fiber average is justified as the unique normalized linear quadratic readout invariant under translations of the canonical compact `S^1_psi` fiber.
