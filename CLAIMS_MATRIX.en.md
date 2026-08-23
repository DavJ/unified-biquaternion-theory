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
| Covariant-tetrad GR kinematics and **conditional effective GR recovery** | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gr_recovery_completion.en.tex`, `canonical/gr_closure/gr_recovery_status.yaml`, `canonical/gr_closure/gap_10_gr_effective_completion.tex`, `canonical/gr_closure/gap_10t_split_jet_right_inverse.tex`, `canonical/gr_closure/gap_10t_split_jet_auxiliary_completion.tex`, `canonical/gr_closure/gap_10d_induced_gravity_endgame.tex`, `papers/UBT_GR_Submission.tex` | **GR recovery is CLOSED CONDITIONALLY** at the local four-dimensional infrared effective level. Projection-free central metric and rank 10 are proved; the physical connection is Levi–Civita in the recovered branch; split-jet auxiliaries are algebraic/nonpropagating and vanish from the on-shell metric/spin equations; and the assumed/induced two-derivative effective action yields Einstein–Lambda. Every smooth local Einstein tetrad has a split-jet representative, so Schwarzschild including its lapse is recovered without using the invalid historical direct-Theta ansatz. Linearization of this recovered branch gives the standard Regge–Wheeler/Zerilli sectors. This does **not** claim unconditional microscopic single-Theta derivation, prediction of Newton's constant, UV psi stability, or global/null-patch completion; those are stronger nonblocking fundamental/UV research questions. `gr_chain` therefore remains `DERIVED_WITH_ASSUMPTIONS`, not `PROVED`. |
| Canonical generalized-Dirac constrained metric rank without extra fields | DERIVED_WITH_ASSUMPTIONS | `canonical/geometry/biquaternion_dirac_lift.tex`, `research_tracks/canonical_relation_generalized_dirac/no_extra_variable_rank_theorem.tex`, `tools/verify_no_extra_variable_rank.py` | Exact theorem: `rank(Dg|A)=dim(A+K)-6`; full rank iff `A+K=R^16`. Invertible `F_Psi` preserves pointwise first-jet rank ten using only the value of the original `Theta`; nonzero scalar or scalar-pseudoscalar zero-order blocks are sufficient. Their derivation from the canonical action and local PDE existence remain open. Eight independent real constraints acting only on the tetrad imply rank at most eight. |
| Split-jet auxiliary action and nonpropagation | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gap_10t_split_jet_auxiliary_completion.tex`, `tools/verify_gr_endgame_completion.py` | `GAP-10T-JET-AUX: CLOSED [L1]`; `GAP-10T-JET-CONSTRAINT-SELECTION: CLOSED AS NO-GO [L1]`; `GAP-10T-JET-DYN: CLOSED CONDITIONALLY FOR GR RECOVERY`, while microscopic origin of the effective selector and global/measure completion remain open. |
| Induced Einstein coefficient from the Theta Hessian | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gap_10d_induced_gravity_endgame.tex`, `canonical/gr_closure/gap_10_gr_effective_completion.tex`, `tools/verify_gr_endgame_completion.py` | `GAP-10D-UNDERDETERMINATION: CLOSED AS NO-GO [L1]`; `GAP-10D-A2-FORM` and `GAP-10D-SPECTRAL-IR`: CLOSED CONDITIONALLY [L1]. A finite positive renormalized Einstein coefficient suffices for GR recovery, so `GAP-10D` is **CLOSED CONDITIONALLY FOR GR RECOVERY**. The composite Hessian, physical mode count, nonminimal coupling, cutoff identification, and constrained measure remain open for a first-principles numerical prediction of `G`, not for conditional GR recovery. |
| Schwarzschild solution in UBT GR branch | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gr_recovery_completion.en.tex`, `canonical/geometry/schwarzschild_claim_status.yaml`, `papers/UBT_GR_Submission_canonical_correction.en.tex` | `GAP-U2Theta: CLOSED CONDITIONALLY FOR GR RECOVERY`. The complete Schwarzschild tetrad/lapse is recovered as a vacuum Einstein solution and lifted locally by the split-jet right inverse with on-shell-decoupled auxiliaries. The older `biquaternionic_vacuum_solutions.tex` direct ansatz is explicitly invalid as a canonical derivation and remains superseded. Microscopic direct branch selection and global horizon-spanning patching remain open fundamental questions. |
| Regge–Wheeler odd-parity graviton equation recovery | DERIVED_WITH_ASSUMPTIONS | `papers/UBT_GR_Submission.tex`, `canonical/gr_closure/gr_recovery_completion.en.tex`, `canonical/gr_closure/` | `GAP-B-MASTER: CLOSED CONDITIONALLY FOR EFFECTIVE GR PERTURBATIONS`: linearization of the recovered Einstein branch gives the standard linearized Einstein system and hence the Regge–Wheeler reduction. Direct derivation from the microscopic UBT master equation remains a stronger nonblocking fundamental-completion problem. |
| Zerilli even-parity graviton equation recovery | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/zerilli_derivation.tex`, `canonical/gr_closure/gr_recovery_completion.en.tex` | Standard even-parity reduction follows from the same conditionally recovered Einstein branch; direct microscopic master-equation derivation remains open as a stronger nonblocking question. |
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
