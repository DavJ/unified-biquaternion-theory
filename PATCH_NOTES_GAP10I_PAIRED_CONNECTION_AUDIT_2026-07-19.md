<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Patch notes: GAP-10I paired-connection audit

> **Superseded scope note (19 July 2026):** the concurrent-vector no-go below is valid only for the torsion-free (`K=0`) generated-tetrad branch. The later `GAP-10I-TORSION-LOCAL` theorem constructs a local composite-contortion representer for every smooth Lorentzian tetrad, so a relative pair is not required for local kinematics.

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
2. **GAP-10I-PAIR-GR — CLOSED AS A TORSION-FREE NO-GO [L1].** In the torsion-free branch,
   `D_mu Theta = sqrt(N0) E_mu` then implies a concurrent vector
   `nabla_mu V^nu = delta_mu^nu`. Consequently the metric admits a proper
   homothety and `R^rho_{ sigma mu nu} V^sigma = 0`. Schwarzschild with
   nonzero mass violates this condition.

## Exact remaining gap (superseded refinement)

The original audit correctly showed that a common central constant, central
one-form, or scalar potential parameter cannot evade the **torsion-free**
concurrent-vector obstruction.  It initially identified a relative pair

`A_mu = Omega_mu + P_mu`, `B_mu = -Omega_mu^ddagger + Q_mu`

as the remaining route.  The companion `GAP-10I-TORSION-LOCAL` theorem later
proved that this route is optional: explicit composite metric-compatible
contortion already provides local curved representability inside the single
connection pairing.

The remaining gap is therefore dynamical/global rather than local kinematic:
derive the selected torsion/current from the canonical action, prove physical
admissibility and nonpropagation where required, and establish global
continuation and Einstein dynamics.

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
