# Patch notes: GAP-10I paired-connection audit

**Date:** 2026-07-19  
**Baseline:** `unified-biquaternion-theory-master(16).zip`

## Result

This patch closes two sharply scoped subgaps without claiming closure of the
full Einstein/action bridge.

1. **GAP-10I-PAIR-KIN — CLOSED [L1].** Lorentz-slice and metric compatibility
   force the pure no-new-field representative
   
   `A_mu = Omega_mu`, `B_mu = -Omega_mu^ddagger`,
   
   modulo a common central one-form that cancels identically. Thus the pure
   branch does not introduce two new gravitational fields.
2. **GAP-10I-PAIR-GR — CLOSED AS NO-GO [L1].** In the torsion-free branch,
   `D_mu Theta = sqrt(N0) E_mu` then implies a concurrent vector
   `nabla_mu V^nu = delta_mu^nu`. Consequently the metric admits a proper
   homothety and `R^rho_{ sigma mu nu} V^sigma = 0`. Schwarzschild with
   nonzero mass violates this condition.

## Exact remaining gap

The general bimodule derivative remains structurally possible, but the
canonical action must derive a nontrivial relative component

`A_mu = Omega_mu + P_mu`, `B_mu = -Omega_mu^ddagger + Q_mu`,

and prove that `P_mu X - X Q_mu` is composite or auxiliary and carries no new
propagating degree of freedom. A common central constant, central one-form, or
scalar potential parameter cannot evade the no-go because it cancels from the
derivative.

Therefore **GAP-10I-2S/CURVED remains NARROWED** and **GAP-10D remains
NARROWED**, not closed.

## New proof and verifier

- `canonical/gr_closure/gap_10i_paired_connection_audit.tex`
- `tools/verify_gap_10i_paired_connection.py`
- `tests/test_gap_10i_paired_connection.py`

The verifier checks the necessity and sufficiency of the slice-preserving pair,
central cancellation, metric-dilation removal, involution equivariance, and
the Schwarzschild homothety contradiction.

## Validation

The overlay was validated with the paired-connection verifier, targeted GR and
claim-consistency tests, repository sanity checks, and LaTeX compilation of the
new audit and revised GR manuscript. See the final overlay manifest for exact
file hashes.
