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
7. use the split-jet right inverse only as a local representation theorem, with
   the physical connection kept Levi--Civita;
8. implement the split-jet relation by an algebraic multiplier sector and prove
   that its multiplier vanishes on shell;
9. derive the two-derivative metric effective action.  The proper-time/KK
   coefficient is known for a specified gauge-fixed Hessian, while its finite
   Newton coupling remains a renormalized/UV input until the finalized UBT
   measure is derived.

## Authoritative files

- `covariant_tetrad_rank_theorem.tex` — central metric and rank-ten theorem.
- `gap_10omega_connection_elimination.tex` — connection reconstruction from
  tetrad and torsion; Levi-Civita corollary.
- `gap_10i_integrability_selection.tex` — affine Minkowski/constant-tetrad
  representers, one-sided no-go, and two-sided curvature identity.
- `gap_10i_paired_connection_audit.tex` — no-new-field Lorentz-pair reduction
  and the concurrent-vector no-go for its torsion-free branch.
- `gap_10i_torsionful_local_representer.tex` — explicit local single-Theta
  representer for arbitrary smooth tetrads using composite metric-compatible
  contortion, including a Schwarzschild vacuum-exterior patch.
- `gap_10t_palatini_torsion_dynamics.tex` — algebraic Cartan torsion equation
  and minimal-branch torsion elimination.
- `gap_10tdyn_10d_canonical_action_audit.tex` — dependency audit, exact direct
  fixed-background spin current, affine flat no-go, Lorentz-invariant pairing
  classification, and the named remaining GAP-10T-DYN/GAP-10D lemmas.
- `gap_10t_composite_flat_admissibility.tex` — proves the stronger exact-gradient
  flatness no-go; affine stationarity is a Jacobian/null-Lagrangian corollary,
  not a surviving curved-GR branch.
- `gap_10t_split_jet_auxiliary_completion.tex` — action-level split-jet
  constraint, proof of algebraic nonpropagation and on-shell decoupling, and
  the surjectivity/selection no-go.
- `gap_10d_induced_gravity_endgame.tex` — curvature-coefficient
  underdetermination theorem and corrected four-dimensional proper-time/KK
  induced-Einstein coefficient.
- `gap_10_gr_effective_completion.tex` — strongest complete result: the
  conditional local Einstein--Lambda effective branch and its exact boundary.
- `gap_10l_psi_symmetry_propagation.tex` — Lorentz-slice and imaginary-time
  symmetry propagation theorems.
- `gap_10i_augmented_holonomy.tex` — exact prescribed-connection integrability
  and augmented-holonomy criterion.
- `gap_10d_low_energy_uniqueness.tex` — conditional Palatini and Lovelock
  endpoint of Einstein dynamics.
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
- `../../tools/verify_gap_10i_paired_connection.py` — exact pair reduction and
  torsion-free Schwarzschild homothety no-go.
- `../../tools/verify_gap_10i_torsionful_local_representer.py` — exact
  composite-contortion and local curved-representer checks.
- `../../tools/verify_remaining_gr_subclosures.py` — Cartan rank, Lorentz
  involution, psi-gauge metric invariance, and augmented-curvature checks.
- `../../tools/verify_canonical_spin_current.py` — exact fixed-background spin
  current, affine obstruction, and Lorentz-invariant pairing classification.
- `../../tools/verify_gr_endgame_completion.py` — exact auxiliary multiplier
  rank, induced coefficient, compact-$\psi$ integral, and self-dual numerical
  checks.

## Locked status language

- `GAP-10Omega-KIN`: CLOSED.
- `GAP-10Omega-GR`: CLOSED.
- `GAP-10T-PALATINI`: CLOSED CONDITIONALLY.
- `GAP-10T-SPIN`: CLOSED CONDITIONALLY; `GAP-10T-FLAT-NOGO` and
  `GAP-10T-PAIRING-NOGO`: CLOSED AS NO-GO.
- `GAP-10T-GRADIENT-FLATNESS`: CLOSED AS NO-GO; exact-gradient tetrads are
  locally flat.
- `GAP-10T-JET-AUX`: CLOSED; the split-jet variables are algebraic and
  decouple on shell on every non-null patch.
- `GAP-10T-JET-CONSTRAINT-SELECTION`: CLOSED AS NO-GO; a surjective pure
  constraint cannot select a physical tetrad from $\Theta$.
- `GAP-10T-DYN`: NARROWED to a non-surjective metric-selection principle or
  the explicitly declared effective-tetrad branch, plus null/global completion.
- `GAP-10I-SR`: CLOSED.
- `GAP-10I-1S`: CLOSED AS NO-GO.
- `GAP-10I-PAIR-KIN`: CLOSED; `GAP-10I-PAIR-GR`: CLOSED AS A
  TORSION-FREE NO-GO.
- `GAP-10I-TORSION-LOCAL`: CLOSED LOCALLY.
- `GAP-10I-2S`: not required for local kinematics; retained as an optional
  torsion-free composite/auxiliary route.
- `GAP-10L-SYM`: CLOSED CONDITIONALLY; `GAP-10L-DYN`: NARROWED.
- `GAP-10I-PRESCRIBED`: CLOSED; `GAP-10I-CURVED`: LOCAL KINEMATICS
  CLOSED, DYNAMICS/GLOBAL PART NARROWED.
- `GAP-10D-PALATINI` and `GAP-10D-UNIQUENESS`: CLOSED CONDITIONALLY.
- `GAP-10D-UNDERDETERMINATION`: CLOSED AS NO-GO; kinematics alone cannot fix
  a Newton coefficient.
- `GAP-10D-A2-FORM` and `GAP-10D-SPECTRAL-IR`: CLOSED CONDITIONALLY for a
  specified gauge-fixed Hessian, mode count, curvature coupling, and UV
  prescription.
- `GAP-10D`: NARROWED to derivation of the constrained measure and the
  renormalized/UV matching data; the conditional GR effective branch is closed.
- `GAP-10psi-KIN`: CLOSED; `GAP-10psi-SYM`: CLOSED CONDITIONALLY;
  `GAP-10psi`: NARROWED.

## Noncanonical profile-completion candidate

The compact-ψ profile files remain noncanonical because the locked Axiom C
forbids fiber averaging. They are no longer described only as a weakly
selective historical route. The 31 July 2026 completion note
`research_tracks/T1_GR/free_fiber_completion/gap_10r_free_fiber_embedding_completion.tex` proves that a local free
isometric embedding in `R^(13,1)` lifts to one `Theta(x,psi)`, gives closure
rank ten, and makes the pure-Theta Gauss action exactly equivalent to local
vacuum Einstein-Lambda dynamics on the free branch.

See `HISTORICAL_FIBER_ROUTE_STATUS.md` for the decision boundary. Promotion
requires an explicit author-approved axiom revision; until then the candidate
must not silently override the pointwise central-anticommutator metric.
