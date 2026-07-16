# Patch notes — v10.3.0 GR subclosures candidate

**Baseline:** `unified-biquaternion-theory-master (1)(2).zip`  
**Date:** 2026-07-16  
**Architecture:** frozen covariant-tetrad route; no metric/fiber/projection pivot.

## Purpose

Close every sharply defined GR subproblem that can be closed from the current
architecture without pretending that the fundamental UBT action or general
curved solution has already been derived.

## New theorem notes

1. `canonical/gr_closure/gap_10t_paladini_torsion_dynamics.tex`
   - minimal Hilbert--Palatini/Einstein--Cartan branch;
   - exact connection variation;
   - pointwise Cartan torsion map rank 24/24;
   - zero spin current -> `T=0`; specified current -> unique contorsion;
   - `GAP-10T-PALATINI: CLOSED CONDITIONALLY`; full `GAP-10T-DYN: NARROWED`.

2. `canonical/gr_closure/gap_10l_psi_symmetry_propagation.tex`
   - intrinsic involution `J(X)=-conj(X^sharp)` with fixed set `W_L`;
   - unique equivariant evolution preserves the Lorentz slice;
   - a psi-flow tangent to a Lorentz gauge orbit leaves `g_mu_nu` invariant;
   - translation-symmetric unique evolution preserves psi-independent data;
   - `GAP-10L-SYM` and `GAP-10psi-SYM` conditionally closed; full gaps narrowed.

3. `canonical/gr_closure/gap_10i_augmented_holonomy.tex`
   - converts the prescribed inhomogeneous two-sided Theta equation into
     homogeneous parallel transport of `(Theta,1)`;
   - exact existence/path-independence criterion: augmented holonomy fixes the
     initial augmented vector;
   - `GAP-10I-PRESCRIBED: CLOSED`; self-consistent `GAP-10I-CURVED: NARROWED`.

4. `canonical/gr_closure/gap_10d_low_energy_uniqueness.tex`
   - minimal first-order action yields Cartan plus Einstein--Lambda equations;
   - four-dimensional Lovelock assumptions uniquely select
     `a G_mu_nu + b g_mu_nu`;
   - `GAP-10D-PALATINI/UNIQUENESS: CLOSED CONDITIONALLY`; full `GAP-10D: NARROWED`.

## Exact verifier

`tools/verify_remaining_gr_subclosures.py` checks:

- Cartan torsion map rank 24/24;
- Lorentz-slice involution and fixed set;
- psi Lorentz-gauge metric invariance;
- augmented-curvature/compatibility identity.

It explicitly does **not** test the action origin, PDE well-posedness, Lovelock
theorem itself, or a self-consistent curved UBT solution.

## Documentation and agent discipline

All active status surfaces, the main GR paper, canonical action, Czech and
English student explanations, and Copilot/agent instructions were synchronized.
Agents are forbidden to promote conditional Palatini/Lovelock or prescribed-
coefficient holonomy results to an unconditional derivation from UBT.

## Remaining gaps

- fundamental selection of the low-energy action and spin current;
- self-consistent curved on-shell existence, regularity and global continuation;
- full dynamic Lorentz/psi stability beyond sufficient symmetry conditions;
- perturbation bridge `GAP-B-MASTER`;
- canonical Schwarzschild tetrad/lapse selection `GAP-U2Theta`.

## Validation target

The overlay must pass the four exact GR verifiers, targeted status/architecture
tests, and compilation of the four new papers plus the canonical, GR and
student documents.
