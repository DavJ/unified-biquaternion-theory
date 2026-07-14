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
| Derived metric chain and GR recovery in admissible real projection | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/`, `papers/UBT_GR_Submission.tex` | Steps 1--4 proved; step 5 conditional on GAP-10; GAP-U2: OPEN — mechanism identified (covariantly harmonic U(1)_ψ potential); closure reduced to GAP-U1 normalization; see also GAP-B |
| Regge–Wheeler odd-parity graviton equation recovery | DERIVED_WITH_ASSUMPTIONS | `papers/UBT_GR_Submission.tex`, `canonical/gr_closure/` | Conditional reduction [L1 cond.] given GAP-B (perturbation bridge) |
| Zerilli even-parity graviton equation recovery | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/zerilli_derivation.tex` | Conditional reduction [L1 cond.] given GAP-B; GAP-B remains open |
| Standard-model gauge-structure recovery track (SU(3)×SU(2)×U(1) structural chain) | DERIVED_WITH_ASSUMPTIONS | `canonical/interactions/`, `canonical/su3_derivation/`, `papers/UBT_Gauge_Submission.tex` | Formal chain present; remaining sector-specific closures explicit |
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
