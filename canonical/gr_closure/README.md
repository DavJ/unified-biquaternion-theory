# GR Closure — Canonical Covariant-Tetrad Route

The current canonical route is:

1. `E_mu = D_mu Theta / sqrt(N0)`;
2. restrict the classical sector to the real Lorentz slice;
3. define the metric by the central anticommutator
   `{E_mu,E_nu}_sharp/2 = g_mu_nu 1`;
4. reconstruct every metric-compatible frame connection from tetrad and
   specified torsion: `omega = omega_LC(e) + K(T)`;
5. obtain the torsion-free GR branch by `T=0`;
6. use the two-sided algebra-native derivative
   `D_mu Theta = partial_mu Theta + A_mu Theta - Theta B_mu` for the generic
   curved branch;
7. solve the implicit curved-space integrability problem;
8. derive, rather than assume, torsion dynamics and the Einstein/UBT bridge.

## Authoritative files

- `covariant_tetrad_rank_theorem.tex` — central metric and rank-ten theorem.
- `gap_10omega_connection_elimination.tex` — connection reconstruction from
  tetrad and torsion; Levi-Civita corollary.
- `gap_10i_integrability_selection.tex` — affine Minkowski/constant-tetrad
  representers, one-sided no-go, and two-sided curvature identity.
- `step1_metric_bridge.tex` — canonical Step 1 wrapper.
- `step2_theta_only_closure.tex` — revised GAP-10 ledger.
- `../geometry/biquaternion_tetrad.tex` — tetrad definition.
- `../geometry/biquaternion_connection.tex` — connection, Christoffel relation,
  torsion, and representation selection.
- `../../tools/verify_covariant_tetrad_rank.py` — exact metric/rank checks.
- `../../tools/verify_gap_10omega_connection.py` — connection and contorsion
  checks.
- `../../tools/verify_gap_10i_integrability.py` — affine representer and
  left/right integrability checks.

## Locked status language

- `GAP-10Omega-KIN`: CLOSED.
- `GAP-10Omega-GR`: CLOSED.
- `GAP-10T-DYN`: OPEN.
- `GAP-10I-SR`: CLOSED.
- `GAP-10I-1S`: CLOSED AS NO-GO.
- `GAP-10I-2S`: NARROWED.
- `GAP-10I-CURVED`: OPEN.
- `GAP-10D`: OPEN.

## Noncanonical exploratory branch

The former compact-ψ fiber-average closure files remain in this directory for
comparison and audit history. They must be labelled `EXPLORATORY CANDIDATE
COMPLETION` and must not override the central anticommutator metric or the
covariant-tetrad connection route.
