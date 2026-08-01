<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: A_attested
ai_assistance: disclosed
human_review: substantive
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: The author has read the substance and accepts editorial responsibility.
UBT-AI-PROVENANCE-END
-->


# CLAIMS_MATRIX.md — UBT Claim Status Matrix

Allowed statuses:

- **PROVED**
- **DERIVED_WITH_ASSUMPTIONS**
- **NUMERICAL_EVIDENCE**
- **CONJECTURE**
- **OPEN_GAP**
- **SPECULATIVE**

Definitions are governed by [`docs/UBT_SCOPE_AND_CLAIM_LEVELS.md`](docs/UBT_SCOPE_AND_CLAIM_LEVELS.md).

---

## Canonical / Research Claims

| Claim | Status | Primary source | Notes |
|---|---|---|---|
| Covariant-tetrad GR kinematics, connection reconstruction, and conditional dynamical subclosures | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/covariant_tetrad_rank_theorem.tex`, `canonical/gr_closure/gap_10omega_connection_elimination.tex`, `canonical/gr_closure/gap_10i_integrability_selection.tex`, `canonical/gr_closure/gap_10i_paired_connection_audit.tex`, `canonical/gr_closure/gap_10i_torsionful_local_representer.tex`, `canonical/gr_closure/gap_10t_palatini_torsion_dynamics.tex`, `canonical/gr_closure/gap_10l_psi_symmetry_propagation.tex`, `canonical/gr_closure/gap_10i_augmented_holonomy.tex`, `canonical/gr_closure/gap_10d_low_energy_uniqueness.tex`, `canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex`, `canonical/gr_closure/gap_10t_composite_flat_admissibility.tex`, `canonical/gr_closure/gap_10t_dcomposite_linearized.tex`, `canonical/gr_closure/gap_10t_minimal_one_connection_gr_no_go.tex`, `canonical/gr_closure/gap_10t_split_jet_right_inverse.tex`, `canonical/gr_closure/gap_10t_split_jet_auxiliary_completion.tex`, `canonical/gr_closure/gap_10d_induced_gravity_endgame.tex`, `canonical/gr_closure/gap_10_gr_effective_completion.tex`, `papers/UBT_GR_Submission.tex` | Projection-free central metric and rank 10 are proved. Specified tetrad+torsion uniquely reconstruct the metric-compatible connection; the torsion-free GR branch is Levi-Civita. Constant Lorentz tetrads have explicit affine Theta representers. The one-sided invertible curved route is a conditional no-go. Lorentz and metric compatibility reduce the pure pair to one spin connection. With zero torsion that branch is a concurrent-vector no-go for the non-flat Schwarzschild vacuum exterior, but an explicit composite-contortion construction now gives a local single-Theta representer for every smooth Lorentzian tetrad without independent A,B fields. This is `GAP-10I-TORSION-LOCAL: CLOSED LOCALLY [L1]`. Additional exact/conditional subclosures are: invertible Cartan torsion selection in the minimal Palatini branch, `GAP-10T-SPIN: CLOSED CONDITIONALLY` for the exact direct fixed-background tree-level matter spin current of the kinetic term for the pure-pair representative (effective Palatini variation with e, g, the volume form and Theta held fixed; the full composite Theta-only variation is not included), `GAP-10T-FLAT-NOGO: CLOSED AS NO-GO` for that minimal effective branch, `GAP-10T-GRADIENT-FLATNESS: CLOSED AS NO-GO` (for every nondegenerate exact-gradient tetrad $e^a=\mathcal N_0^{-1/2}dY^a$, the induced metric is locally a pullback of Minkowski space, the Levi-Civita curvature and Hilbert--Palatini density vanish identically, and the locked kinetic plus cosmological terms reduce to a Jacobian null Lagrangian; affine stationarity is only an auxiliary corollary, not a surviving curved-GR branch; `canonical/gr_closure/gap_10t_composite_flat_admissibility.tex`), `GAP-10T-DCOMP-WL-SECTOR: CLOSED CONDITIONALLY` (Theta in W_L is a consistent subsector, not a necessary condition), `GAP-10T-DCOMP-LIN-OFFRES: CLOSED CONDITIONALLY` (the frozen real-exponential symbol obeys A^3=qA^2 and the unique driven solution is exactly holonomic off q=1), and `GAP-10T-DCOMP-LIN-REALFREQ: CLOSED AS NO-GO` (for real Fourier covectors det(I-A)=(1-i lambda dot k)^6 never vanishes, so this frozen torsion-free W_L approximation has no nonzero homogeneous real-frequency curved mode); all candidate linearized anholonomy is confined to a six-dimensional real-exponential sector at q=1, while its variable-coefficient/nonlinear assembly remains `GAP-10T-DCOMP-RES: OPEN` (`canonical/gr_closure/gap_10t_dcomposite_linearized.tex`), and `GAP-10T-PAIRING-NOGO: CLOSED AS NO-GO` (the sharp/Minkowski pairing is unique up to scale among real symmetric Lorentz-invariant slice pairings, while the ddagger Hilbert-Schmidt pairing fails boost invariance; therefore pairing selection alone cannot remove the obstruction; `canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex`), symmetry propagation of the Lorentz slice and psi-stable metric sectors, an augmented-holonomy criterion for prescribed curved coefficients, and the conditional Palatini/Lovelock Einstein--Lambda infrared endpoint. The combined representer/no-go audit also closes `GAP-10T-MINIMAL-ONE-CONNECTION-GR` as an architecture-level no-go: the same physical connection cannot simultaneously be torsion-free generic GR and supply universal local single-Theta representability. The split exact-GR kinematic continuation is now explicit: for non-null Lorentz-real X, a composite relative central one-form and orthogonal Lorentz jet tensor give an exact local right inverse while physical curvature remains Levi-Civita (`GAP-10T-JET-KIN: CLOSED LOCALLY`). The split-jet multiplier action closes `GAP-10T-JET-AUX`: its multiplier vanishes on shell, so the jet variables are algebraic, nonpropagating, and do not backreact. Surjectivity simultaneously closes `GAP-10T-JET-CONSTRAINT-SELECTION` as a no-go: the pure constraint cannot select one tetrad from Theta. The GR endgame audit closes `GAP-10D-UNDERDETERMINATION` as a no-go and `GAP-10D-A2-FORM` / `GAP-10D-SPECTRAL-IR` conditionally: a specified gauge-fixed Laplace-type Theta Hessian gives the exact induced coefficient, but the physical mode count, curvature coupling, cutoff identification, and constrained measure remain un-derived. Thus a complete conditional effective GR branch exists, while unconditional single-Theta GR remains open. Fiber averaging is historical/exploratory only. |
| Canonical generalized-Dirac constrained metric rank without extra fields | DERIVED_WITH_ASSUMPTIONS | `canonical/geometry/biquaternion_dirac_lift.tex`, `research_tracks/canonical_relation_generalized_dirac/no_extra_variable_rank_theorem.tex`, `tools/verify_no_extra_variable_rank.py` | Exact theorem: `rank(Dg|A)=dim(A+K)-6`; full rank iff `A+K=R^16`. Invertible `F_Psi` preserves pointwise first-jet rank ten using only the value of the original `Theta`; nonzero scalar or scalar-pseudoscalar zero-order blocks are sufficient. Their derivation from the canonical action and local PDE existence remain open. Eight independent real constraints acting only on the tetrad imply rank at most eight. |
| Split-jet auxiliary action and nonpropagation | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gap_10t_split_jet_auxiliary_completion.tex`, `tools/verify_gr_endgame_completion.py` | `GAP-10T-JET-AUX: CLOSED [L1]`; `GAP-10T-JET-CONSTRAINT-SELECTION: CLOSED AS NO-GO [L1]`; `GAP-10T-JET-DYN: NARROWED`. |
| Induced Einstein coefficient from the Theta Hessian | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gap_10d_induced_gravity_endgame.tex`, `canonical/gr_closure/gap_10_gr_effective_completion.tex`, `tools/verify_gr_endgame_completion.py` | `GAP-10D-UNDERDETERMINATION: CLOSED AS NO-GO [L1]`; `GAP-10D-A2-FORM` and `GAP-10D-SPECTRAL-IR`: CLOSED CONDITIONALLY [L1]. The exact coefficient is fixed once the gauge-fixed Hessian, physical mode count, nonminimal coupling and cutoff are specified; these inputs are not yet derived from the finalized UBT measure, so `GAP-10D: NARROWED`. |
| Regge–Wheeler odd-parity graviton equation recovery | DERIVED_WITH_ASSUMPTIONS | `papers/UBT_GR_Submission.tex`, `canonical/gr_closure/` | Standard GR reduction remains conditional on a canonical on-shell Schwarzschild tetrad and a perturbation bridge from the original UBT master dynamics (`GAP-B-MASTER`). |
| Zerilli even-parity graviton equation recovery | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/zerilli_derivation.tex` | Standard GR reduction remains conditional on the same covariant-tetrad dynamical bridge. |
| Standard-model gauge-structure recovery track (SU(3)×SU(2)×U(1) structural chain) | DERIVED_WITH_ASSUMPTIONS | `canonical/interactions/`, `canonical/su3_derivation/`, `papers/UBT_Gauge_Submission.tex` | Formal chain present; remaining sector-specific closures explicit |
| Triqubit one-hot error status | DERIVED_WITH_ASSUMPTIONS | `canonical/interactions/gap_su3_triqubit_qec.tex`, `tools/verify_triqubit_qec_status.py` | `GAP-SU3-TRIQUBIT-LEAKAGE: CLOSED [L1]`: every single `X_i`/`Y_i` error leaves the color sector. `GAP-SU3-TRIQUBIT-QEC: CLOSED AS NO-GO [L1]`: general `Z_i` errors are undetected logical phases and Knill--Laflamme fails for correction of an unknown single `X_i`. This is useful for a constrained quantum-simulation register and gives no simulation-ontology inference. |
| Hypercharge $Y_Q=1/6$ from topology | L1_FAMILY_CHECK | `canonical/interactions/colour_charge_lattice.tex` | Unique within $Y=n/6$ family via gravitational anomaly $\mathcal{A}_{\rm grav}(n)=n-1=0$ for $n=1$ only. Full uniqueness (outside family) remains OPEN. |
| Three-generation structural route from ψ-winding framework | DERIVED_WITH_ASSUMPTIONS | `canonical/n_eff/`, `canonical/interactions/` | Mechanism documented with explicit assumptions |
| Full α closure from first principles (including blocker derivations) | OPEN_GAP | `canonical/alpha/ALPHA_MASTER_STATUS.md`, `research_tracks/T3_ALPHA/mellin_insertion_B.tex` | 5 routes tested, all NO-GO. $B_{\rm phenom}$ [OBS 0.0066%]. Alpha NOT DERIVED. |
| N_eff-related route support for α track | DERIVED_WITH_ASSUMPTIONS | `canonical/n_eff/` | Must not be overstated as full α proof |
| Numerical reproducibility tracks (diagnostics/validation) | NUMERICAL_EVIDENCE | `research_tracks/`, `tools/`, `experiments/` | Reproducible evidence, not theorem-level proof |
| Full UBT quantum field theory closure (Hilbert/Born/measurement/path-integral completeness) | OPEN_GAP | `src/ubt/quantum/`, `docs/quantum_sector_status.md` | Numerical scaffold exists; derivation chain remains open |
| Born rule derived from UBT | OPEN_GAP | `src/ubt/quantum/quantum_scaffold.py`, `docs/quantum_sector_status.md` | Placeholder only |
| Path-integral measure in biquaternionic coordinates | OPEN_GAP | `src/ubt/quantum/quantum_scaffold.py`, `docs/quantum_sector_status.md` | `NotDerivedPathIntegralKernel` is explicit placeholder |
| Finite-energy soliton regularization | NUMERICAL_EVIDENCE | `src/ubt/solitons/regularization.py`, `research_tracks/renormalization/finite_energy_soliton_regularization.md` | Regularized finite-energy model; full RG derivation open |
| Renormalization group from UBT action | OPEN_GAP | `research_tracks/renormalization/finite_energy_soliton_regularization.md` | No RG-flow derivation claimed |
| UBT derives weak parity violation | CONJECTURE | `src/ubt/algebra/chirality.py`, `research_tracks/weak_sector/chirality_and_parity_status.md` | Chirality algebra scaffold only; no SU(2)_L coupling derivation |
| Anomalous magnetic moment prediction from UBT | OPEN_GAP | `src/ubt/observables/physics_observable_bridge.py`, `docs/observable_bridge.md` | Bridge returns structured open-gap status |

---

## Explicitly Speculative Claims (non-canonical)

Unless a reproducible empirical protocol upgrades them, the following remain **SPECULATIVE**:

| Claim | Status | Location |
|---|---|---|
| consciousness field | SPECULATIVE | `speculative_extensions/consciousness/` |
| psychons as physical particles | SPECULATIVE | `speculative_extensions/consciousness/` |
| afterlife | SPECULATIVE | `speculative_extensions/` |
| survival of consciousness | SPECULATIVE | `speculative_extensions/` |
| communication with deceased consciousness | SPECULATIVE | `speculative_extensions/` |
| ThetaComm | SPECULATIVE | `speculative_extensions/thetacomm/` |
| Biquaternionic metric-null / volume-null invisibility program | SPECULATIVE | `speculative_extensions/invisibility/` |
| soul / immortality | SPECULATIVE | `speculative_extensions/` |
| Matrix / simulation ontology | SPECULATIVE | `speculative_extensions/metaphysics/` (or equivalent speculative path) |
