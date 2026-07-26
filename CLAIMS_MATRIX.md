<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

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
| Covariant-tetrad GR kinematics, connection reconstruction, and conditional dynamical subclosures | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/covariant_tetrad_rank_theorem.tex`, `canonical/gr_closure/gap_10omega_connection_elimination.tex`, `canonical/gr_closure/gap_10i_integrability_selection.tex`, `canonical/gr_closure/gap_10i_paired_connection_audit.tex`, `canonical/gr_closure/gap_10i_torsionful_local_representer.tex`, `canonical/gr_closure/gap_10t_palatini_torsion_dynamics.tex`, `canonical/gr_closure/gap_10l_psi_symmetry_propagation.tex`, `canonical/gr_closure/gap_10i_augmented_holonomy.tex`, `canonical/gr_closure/gap_10d_low_energy_uniqueness.tex`, `canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex`, `canonical/gr_closure/gap_10t_composite_flat_admissibility.tex`, `canonical/gr_closure/gap_10t_dcomposite_linearized.tex`, `papers/UBT_GR_Submission.tex` | Projection-free central metric and rank 10 are proved. Specified tetrad+torsion uniquely reconstruct the metric-compatible connection; the torsion-free GR branch is Levi-Civita. Constant Lorentz tetrads have explicit affine Theta representers. The one-sided invertible curved route is a conditional no-go. Lorentz and metric compatibility reduce the pure pair to one spin connection. With zero torsion that branch is a concurrent-vector no-go for the non-flat Schwarzschild vacuum exterior, but an explicit composite-contortion construction now gives a local single-Theta representer for every smooth Lorentzian tetrad without independent A,B fields. This is `GAP-10I-TORSION-LOCAL: CLOSED LOCALLY [L1]`. Additional exact/conditional subclosures are: invertible Cartan torsion selection in the minimal Palatini branch, `GAP-10T-SPIN: CLOSED CONDITIONALLY` for the exact direct fixed-background tree-level matter spin current of the kinetic term for the pure-pair representative (effective Palatini variation with e, g, the volume form and Theta held fixed; the full composite Theta-only variation is not included), `GAP-10T-FLAT-NOGO: CLOSED AS NO-GO` for that minimal effective branch, `GAP-10T-GRADIENT-FLATNESS: CLOSED AS NO-GO` (for every nondegenerate exact-gradient tetrad $e^a=\mathcal N_0^{-1/2}dY^a$, the induced metric is locally a pullback of Minkowski space, the Levi-Civita curvature and Hilbert--Palatini density vanish identically, and the locked kinetic plus cosmological terms reduce to a Jacobian null Lagrangian; affine stationarity is only an auxiliary corollary, not a surviving curved-GR branch; `canonical/gr_closure/gap_10t_composite_flat_admissibility.tex`), `GAP-10T-DCOMP-SECTOR: CLOSED` and `GAP-10T-DCOMP-LIN-OFFRES: CLOSED CONDITIONALLY` (linearized frozen-coefficient D-composite analysis: symbol identity A^3 = q A^2, off-resonance solutions exactly holonomic; all linearized anholonomy confined to a six-dimensional resonant sector, `GAP-10T-DCOMP-RES: OPEN`; `canonical/gr_closure/gap_10t_dcomposite_linearized.tex`), and `GAP-10T-PAIRING-NOGO: CLOSED AS NO-GO` (the sharp/Minkowski pairing is unique up to scale among real symmetric Lorentz-invariant slice pairings, while the ddagger Hilbert-Schmidt pairing fails boost invariance; therefore pairing selection alone cannot remove the obstruction; `canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex`), symmetry propagation of the Lorentz slice and psi-stable metric sectors, an augmented-holonomy criterion for prescribed curved coefficients, and the conditional Palatini/Lovelock Einstein--Lambda infrared endpoint. The full canonical action origin, dynamical selection and physical admissibility of the composite torsion (or of an optional torsion-free relative bimodule component), global continuation, and master-equation perturbation bridge remain unresolved. Fiber averaging is historical/exploratory only. |
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
| soul / immortality | SPECULATIVE | `speculative_extensions/` |
| Matrix / simulation ontology | SPECULATIVE | `speculative_extensions/metaphysics/` (or equivalent speculative path) |
