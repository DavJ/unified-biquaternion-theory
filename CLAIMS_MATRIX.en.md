<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# UBT Claim Status Matrix

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
| Local classical single-Theta Einstein-Lambda recovery from the adopted one-coupling gravity dynamical postulate | PROVED | `canonical/gr_closure/gravity_dynamical_postulate.en.md`, `canonical/gr_closure/gr_recovery_status.yaml`, `research_tracks/action_selection/unimodular_one_constant_gr_closure.en.md`, `canonical/gr_closure/gap_10t_split_jet_right_inverse.tex`, `canonical/gr_closure/gap_10t_palatini_torsion_dynamics.tex` | **Local classical Einstein-Lambda recovery is CLOSED** on regular non-null split-jet patches after adoption of the one-coupling unimodular split-jet Palatini law. `Theta` is the only fundamental physical field; there is no independent tetrad. Surjective algebraic jet variations impose the complete tetrad Einstein equation, the physical connection reduces to Levi-Civita in spinless vacuum, and `kappa` is the sole independent continuous action coupling. `Lambda_0` is not set to zero and is not a second action parameter: `dLambda=0` makes it an integration constant. The affine background-free first-order auxiliary completion is unique within its explicitly declared minimal class up to invertible linear auxiliary redefinitions, sign/orientation and a boundary term. This does not claim that kinematics alone forced the dynamical postulate, nor does it predict the observed numerical value of `Lambda_0` or close the full gauge/matter/quantum action or global/UV completion. |
| Canonical generalized-Dirac constrained metric rank without extra fields | DERIVED_WITH_ASSUMPTIONS | `canonical/geometry/biquaternion_dirac_lift.tex`, `research_tracks/canonical_relation_generalized_dirac/no_extra_variable_rank_theorem.tex`, `tools/verify_no_extra_variable_rank.py` | Exact theorem: `rank(Dg|A)=dim(A+K)-6`; full rank iff `A+K=R^16`. Invertible `F_Psi` preserves pointwise first-jet rank ten using only the value of the original `Theta`; nonzero scalar or scalar-pseudoscalar zero-order blocks are sufficient. Their derivation from the canonical action and local PDE existence remain open. Eight independent real constraints acting only on the tetrad imply rank at most eight. |
| Split-jet auxiliary geometry and variational transmission of the tetrad equation | PROVED | `canonical/gr_closure/gap_10t_split_jet_right_inverse.tex`, `canonical/gr_closure/gap_10t_split_jet_auxiliary_completion.tex`, `research_tracks/action_selection/split_jet_palatii_variational_lift.en.md`, `tools/verify_split_jet_palatii_variational_lift.py` | `GAP-10T-JET-AUX: CLOSED [L1]`; the local right inverse is exact on `X^2 != 0`, the jet variables are algebraic/nonpropagating, and when inserted inside the adopted gravity functional their rank-four variation is surjective onto all tetrad directions. `GAP-10T-JET-CONSTRAINT-SELECTION: CLOSED AS NO-GO [L1]`; the pure surjective constraint by itself cannot select a tetrad. The adopted dynamical functional supplies the missing selector and stationarity imposes the complete tetrad Euler form rather than a projected equation. Global/null-patch continuation is separate. |
| Induced Einstein coefficient from the Theta Hessian (alternative/historical route) | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gap_10d_induced_gravity_endgame.tex`, `canonical/gr_closure/gap_10_gr_effective_completion.tex`, `tools/verify_gr_endgame_completion.py` | `GAP-10D-UNDERDETERMINATION: CLOSED AS NO-GO [L1]`; `GAP-10D-A2-FORM` and `GAP-10D-SPECTRAL-IR` remain conditional statements about a specified Hessian and measure. This route is no longer required for local classical GR closure under the adopted one-coupling dynamical postulate, but remains relevant to quantum/UV derivation and possible computation of effective coefficients. |
| Schwarzschild and Einstein-Lambda solution families in the adopted UBT gravity branch | PROVED | `canonical/gr_closure/gravity_dynamical_postulate.en.md`, `canonical/gr_closure/gr_recovery_status.yaml`, `canonical/geometry/schwarzschild_claim_status.yaml`, `papers/UBT_GR_Submission_canonical_correction.en.tex` | `GAP-U2Theta: CLOSED LOCALLY`. Schwarzschild is included at `Lambda_0=0`; de Sitter, anti-de Sitter and Schwarzschild-de Sitter/Kottler are included for the corresponding constant `Lambda_0`, all through the local split-jet solution-set equivalence. The older direct ansatz in `biquaternionic_vacuum_solutions.tex` remains invalid and superseded. Global horizon-spanning patching is a separate global-completion problem. |
| Regge–Wheeler odd-parity graviton equation recovery | PROVED | `papers/UBT_GR_Submission.tex`, `canonical/gr_closure/gravity_dynamical_postulate.en.md`, `canonical/gr_closure/` | `GAP-B-MASTER: CLOSED FOR CLASSICAL GR PERTURBATIONS`. Linearization of the adopted Einstein branch gives the standard local linearized Einstein system and hence the Regge–Wheeler reduction. A direct UV master-equation derivation remains a stronger full-theory problem, not a blocker for the classical GR theorem. |
| Zerilli even-parity graviton equation recovery | PROVED | `canonical/gr_closure/zerilli_derivation.tex`, `canonical/gr_closure/gravity_dynamical_postulate.en.md` | The standard even-parity reduction follows from the same adopted Einstein branch. A direct UV master-equation derivation is a stronger full-theory problem. |
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
