<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# DERIVATION_INDEX.md — Canonical UBT Derivation Chain

This index lists the authoritative mathematical/physical derivation chain used
for canonical UBT claims.

For claim-level definitions, see [`docs/UBT_SCOPE_AND_CLAIM_LEVELS.md`](docs/UBT_SCOPE_AND_CLAIM_LEVELS.md).

---

## Canonical Core Chain

### 1) Algebraic foundation

- **Biquaternion algebra** ℂ⊗ℍ and its core structural properties  
  Source: `canonical/algebra/`

### 2) Fundamental field and complex time

- **Θ(q,τ)** as the fundamental field structure
- **Complex time** formulation `τ = t + iψ`
- Lorentz-slice admissibility and involution assumptions explicitly stated

Sources: `canonical/fields/`, `canonical/THEORY/math/fields/`

### 3) Emergent geometry and GR recovery

- Projection-free covariant tetrad from Θ and central anticommutator metric
- Rank-ten/non-degeneracy and Lorentz-signature chain
- Connection reconstruction from tetrad and specified torsion
- Flat affine representers and curved integrability selection
- Conditional effective Einstein/action bridge now explicit; first-principles Hessian/mode/cutoff/measure derivation and Schwarzschild on-shell selection remain open

Sources: `canonical/geometry/`, `canonical/gr_closure/`, `papers/UBT_GR_Submission.tex`

**Covariant-tetrad GR revision (2026-07-16):**
- `canonical/gr_closure/covariant_tetrad_rank_theorem.tex` — central anticommutator metric and exact rank-ten theorem.
- `canonical/geometry/biquaternion_dirac_lift.tex` and `research_tracks/canonical_relation_generalized_dirac/no_extra_variable_rank_theorem.tex` — exact constrained-rank formula, no-extra-field transversality criterion, invertible original-field absorption, and the eight-constraint no-go.
- `canonical/gr_closure/gap_10omega_connection_elimination.tex` — unique reconstruction of every metric-compatible connection from tetrad and specified torsion; Levi-Civita torsion-free corollary.
- `canonical/gr_closure/gap_10i_integrability_selection.tex` — explicit affine Minkowski/constant-tetrad representers; one-sided invertible curved no-go; exact two-sided curvature identity.
- `canonical/gr_closure/gap_10i_paired_connection_audit.tex` — exact reduction of a Lorentz-compatible pair to one spin connection and concurrent-vector no-go for its torsion-free branch.
- `canonical/gr_closure/gap_10i_torsionful_local_representer.tex` — explicit local single-Theta representer for every smooth Lorentzian tetrad using composite metric-compatible contortion; includes a Schwarzschild vacuum-exterior patch.
- `canonical/gr_closure/gap_10t_palatini_torsion_dynamics.tex` — invertible 24-component Cartan torsion map and algebraic torsion elimination in the minimal first-order branch.
- `canonical/gr_closure/gap_10l_psi_symmetry_propagation.tex` — intrinsic Lorentz-slice involution, equivariant fixed-set propagation, and metric invariance under vertical Lorentz/translation-symmetric psi evolution.
- `canonical/gr_closure/gap_10i_augmented_holonomy.tex` — exact augmented-connection/holonomy existence criterion for prescribed `(E,A,B)`.
- `canonical/gr_closure/gap_10d_low_energy_uniqueness.tex` — conditional Palatini field equations and four-dimensional Lovelock uniqueness of the Einstein--Lambda infrared endpoint.
- `tools/verify_covariant_tetrad_rank.py` — exact algebra and rank verification.
- `tools/verify_gap_10omega_connection.py` — Levi-Civita, polar-frame, uniqueness, and contorsion reconstruction checks.
- `tools/verify_gap_10i_integrability.py` — Minkowski representer, one-sided injectivity, and two-sided curvature checks.
- `tools/verify_gap_10i_paired_connection.py` — slice-preserving pair, central cancellation, J-equivariance, and Schwarzschild homothety no-go.
- `tools/verify_remaining_gr_subclosures.py` — exact Cartan rank, Lorentz involution, psi-gauge metric stability, and augmented-curvature checks.
- `tools/verify_canonical_spin_current.py` — direct fixed-background matter current, affine torsion no-go, Lorentz-invariant pairing classification, and the auxiliary affine-stationarity sample.
- `tools/verify_gradient_composite_flatness.py` — exact determinant identity and nonlinear pullback check supporting the exact-gradient flatness no-go.
- Closed/conditional/narrowed: GAP-10K; GAP-10Ω-KIN/GR; GAP-10I-PAIR-KIN and GAP-10I-PAIR-GR (torsion-free no-go), GAP-10I-TORSION-LOCAL (closed locally); GAP-10T-PALATINI and GAP-10T-SPIN (conditional), GAP-10T-FLAT-NOGO, GAP-10T-PAIRING-NOGO, and GAP-10T-GRADIENT-FLATNESS (no-go), with `GAP-10T-JET-AUX` closed, `GAP-10T-JET-CONSTRAINT-SELECTION` closed as a no-go, and full GAP-10T-DYN narrowed; GAP-10L-CONN and GAP-10L-SYM (conditional) with GAP-10L-DYN narrowed; GAP-10I-SR and GAP-10I-PRESCRIBED, GAP-10I-1S (no-go), GAP-10I-2S optional for torsion-free completion and GAP-10I-CURVED local kinematics closed with dynamics/global part narrowed; GAP-10D-PALATINI/UNIQUENESS, GAP-10D-A2-FORM and GAP-10D-SPECTRAL-IR (conditional), GAP-10D-UNDERDETERMINATION (no-go), with GAP-10D narrowed; GAP-10psi-KIN/SYM with GAP-10psi narrowed.
- Still open at full theory level: derivation of the constrained gauge-fixed Hessian and physical mode count, nonminimal curvature coupling, UV scale/regulator from the finalized Theta measure, a non-surjective tetrad-selection principle or induced collective-field construction, global/null-patch continuation, self-consistent curved on-shell selection, physical psi stability, GAP-B-MASTER, and GAP-U2Theta.
- The compact-ψ profile route remains noncanonical under the current Axiom C, but now has a local free-embedding completion candidate: `research_tracks/T1_GR/free_fiber_completion/gap_10r_free_fiber_embedding_completion.tex`. It closes local smooth representability and local vacuum Einstein--Lambda dynamics within the profile-metric architecture; profile selection, canonical-action origin, holomorphic/Jacobi restrictions, matter separation, and global completion remain open.

**GR closure files:**
- `canonical/gr_closure/step1_metric_bridge.tex` — Step 1 — [L1] — Central metric from the covariant Θ tetrad
- `canonical/gr_closure/step2_nondegeneracy.tex` — Step 2 — [L1] — Non-degeneracy
- `canonical/gr_closure/step3_signature_theorem.tex` — Step 3 — [L1] — Lorentzian signature
- `canonical/gr_closure/step3_einstein_with_matter.tex` — Step 5 — [L1] — Einstein equations
- `canonical/gr_closure/linearised_gravity.tex` — ED-2 — [L1 conditional] — Regge-Wheeler after the open covariant-tetrad master bridge
- `canonical/gr_closure/zerilli_derivation.tex` — GAP-Z — [L1] — Zerilli even-parity graviton
- `canonical/gr_closure/schwarzschild_table.tex` — ED-3 — [L1]+[NUM] — Schwarzschild numerical table (Appendix C)
- `canonical/gr_closure/frw_cosmological_solutions.tex` — GAP-C — [L1]+[L1 cond.] — FRW in solution space [L1]; Θ-ansatz [L1 cond. on Friedmann branch only (v55)]; ODE-a auto-consistent [L1]; ODE-f quasi-static $f\propto a^{-3(1+w)}$ [L1 cond. on Friedmann + quasi-static]; ODE-f exact solutions without quasi-static: dust (Si/Ci), radiation (Bessel $J_{1/4}/Y_{1/4}$) [L1 cond. on Friedmann branch only] (NEW v55, Prop prop:ode_f_full_dynamics); g_0i sub-gap [L1 conditional on comoving-frame averaging]

### 4) Gauge and interaction recovery

- SU(3) × SU(2) × U(1) structural recovery tracks
- Chirality and QED-sector derivations where closed
- Explicit open gaps retained (e.g., unresolved Higgs/Yukawa closures)

Sources: `canonical/interactions/`, `canonical/su3_derivation/`, `canonical/chirality/`, `papers/UBT_Gauge_Submission.tex`

**Triqubit error-status closure (2026-07-26):**
- `canonical/interactions/gap_su3_triqubit_qec.tex` — exact projector proof that all single `X_i`/`Y_i` errors are leakage-detectable, compressed `Z_i` operators are non-scalar, and Knill--Laflamme fails for `{I,X_1,X_2,X_3}`.
- `tools/verify_triqubit_qec_status.py` — matrix verifier and explicit `X_1 X_2` witness.
- Status: `GAP-SU3-TRIQUBIT-LEAKAGE: CLOSED [L1]`; `GAP-SU3-TRIQUBIT-QEC: CLOSED AS NO-GO [L1]`. This is a quantum-simulation encoding statement, not evidence for simulation ontology.

**Chirality derivation files:**
- `canonical/chirality/step3_gap_C1_resolution.tex` — Gap C1 Step 3 — [L1] — SU(2)_L acts on left-chiral doublets
- `canonical/chirality/step4_no_wr_derivation.tex` — Gap C1 upgrade — [MC]+[L1 cond.] — SU(2)_R decouples via ψ-parity; all Loopholes 1 [L1 cond.], 2 [L1 cond.], 3 [STD] closed; OP-S4 [L1 conditional]; Rem rem:minimality_anomaly: anomaly-safe (cond. SU(3) colour structure, C2-i CLOSED v55), unitarity deferred EW-2

### 5) α (fine-structure) track with explicit gap discipline

- Canonical route inventory and proof-status discipline
- Conditional/derived results separated from open blockers
- Gaps are explicit and not hidden

Sources: `canonical/alpha/`, `canonical/n_eff/`, `reports/`

research_tracks/T3_ALPHA/mellin_insertion_B.tex | Gap G137-B no-go record |
  [L0]+[L1]+[OBS] | Six routes NO-GO; 3 sub-gaps G137-B-i/ii/iii named [OPEN/MC];
  T3_ALPHA downgraded to STRUCTURAL EVIDENCE 2026-06-11; Alpha NOT DERIVED

research_tracks/T3_ALPHA/integer_137_note.tex | Integer-137 companion note |
  [L1 conditional on B] | Records Thm: n*(B_phenom)=137; Gap G137-B sub-gaps
  stated; N_eff clarification (twist=12 used, not loop=3); alpha NOT DERIVED

research_tracks/EW/hypercharge_from_ubt.tex | Gap C2 Step 1 — fermion hypercharge from ψ-winding and SU(3) colour |
  [L1 cond. on OP-S4 + SU(3) colour structure from UBT] (v55) | $Y=(B-L)/2$ from OP-S4 + SU(3);
  sub-gap C2-i CLOSED [L1 cond. on SU(3) colour structure] (Lem lem:Bq_from_su3 NEW v55);
  sub-gap C2-ii ($U(1)_B$ from ψ-winding) [OPEN/MC] — does not block;
  all 6 SM hypercharge values reproduced algebraically given Lem 2.1; 2026-06-11 v55

research_tracks/EW/weinberg_angle_ew1_rg.tex | EW-1b Weinberg angle via EW1+RG |
  [L1 cond. on OP-S4 + SU(3) + scale closure] (v55) | $\sin^2\theta_W(M_Z)\approx0.231$;
  Corollary prop:sin2_thetaW_corollary added (NEW v55); C2-i conditionality removed

---

## Open Derivation Gaps (Mandatory status discipline)

The following items are explicitly tracked as unresolved unless a full derivation
is added to canonical sources:

- Full UBT quantum field theory closure (Hilbert structure, Born rule,
  measurement map, path-integral closure): **OPEN_GAP**
- Born rule from UBT: **OPEN_GAP**
- Path-integral measure in biquaternionic coordinates: **OPEN_GAP**
- Renormalization group from UBT action: **OPEN_GAP**
- Weak interaction chirality/parity-violation derivation from geometry:
  **CONJECTURE / OPEN_GAP** until SU(2)\_L coupling and closure conditions are derived
- Anomalous magnetic moment prediction from UBT first principles: **OPEN_GAP**

Active scaffolds documenting these gaps:

- `src/ubt/quantum/quantum_scaffold.py`
- `src/ubt/solitons/regularization.py`
- `src/ubt/algebra/chirality.py`
- `src/ubt/observables/physics_observable_bridge.py`
- `docs/quantum_sector_status.md`
- `docs/observable_bridge.md`
- `research_tracks/renormalization/finite_energy_soliton_regularization.md`
- `research_tracks/weak_sector/chirality_and_parity_status.md`

---

## Research-Track (Non-canonical) Scientific Work

The following are scientific but not canonical closure claims:

- numerical diagnostics and reproducibility workflows,
- open alpha routes,
- CMB/Planck and related data-analysis tracks,
- prime-stability and lepton-spectrum active investigations,
- explicit conjectures and unresolved problems.

Primary location: `research_tracks/`

---

## Non-canonical speculative extensions

These extensions are not part of the canonical UBT derivation chain and are not established physical results.

Speculative material is maintained under `speculative_extensions/`, including
consciousness/psychons, ThetaComm-like narratives, afterlife/survival claims,
and metaphysical/simulation-style interpretations.

### GEM compact modes and Gödel-type kinematic target (2026-07-25)

- `research_tracks/gem_compact_modes/gem_compact_modes.tex` —
  `GEM-CM-K1/K2` [L1]: exact averaged `(+n,-n)` current and compact-gradient
  identities; balanced current/flux vanish while gradient energy remains
  positive.
- Same note — `GEM-CM-GA1` [L1]: even-carrier/odd-lift grade audit; no
  independent odd field is added to canonical biquaternionic Theta.
- Same note — `GEM-CM-NG1` [L1]: common infinitesimal Lorentz rotor gives
  `delta g=0` and cannot be a physical light-cone response.
- `tools/verify_gem_compact_modes.py` — exact/numerical regression for compact
  modes, the Lorentz no-go, and the Gödel coframe kinematic target.
- Open: balanced non-zero bivector/spin polarization, canonical action source,
  symmetric metric strain, distinction from standard stress-energy, dynamical
  `R_psi`, Gödel-type solution, and global chronology.
- Historical imaginary-metric/CTC documents remain preserved under
  `speculative_extensions/`; see `research_tracks/gem_compact_modes/LEGACY_MAP.md`.

- `canonical/gr_closure/gap_10t_minimal_one_connection_gr_no_go.tex` — architecture-level exact-GR no-go and completion fork.
- `canonical/gr_closure/gap_10t_split_jet_right_inverse.tex` — explicit local composite Lorentz plus relative-central jet right inverse, keeping physical curvature Levi-Civita; kinematic closure only.
- `canonical/gr_closure/gap_10t_split_jet_auxiliary_completion.tex` — multiplier action, exact lambda=0 theorem, nonpropagation/on-shell decoupling, and surjective-selection no-go.
- `canonical/gr_closure/gap_10d_induced_gravity_endgame.tex` — axiomatic underdetermination theorem and corrected proper-time/Kaluza--Klein induced Einstein coefficient.
- `canonical/gr_closure/gap_10_gr_effective_completion.tex` — complete conditional effective GR branch through two derivatives.
- `tools/verify_gr_endgame_completion.py` — multiplier-rank, proper-time coefficient, self-dual KK constant, and Planck-ratio checks.
