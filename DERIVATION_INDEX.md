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
- Open Einstein/action bridge and Schwarzschild on-shell selection

Sources: `canonical/geometry/`, `canonical/gr_closure/`, `papers/UBT_GR_Submission.tex`

**Covariant-tetrad GR revision (2026-07-16):**
- `canonical/gr_closure/covariant_tetrad_rank_theorem.tex` — central anticommutator metric and exact rank-ten theorem.
- `canonical/gr_closure/gap_10omega_connection_elimination.tex` — unique reconstruction of every metric-compatible connection from tetrad and specified torsion; Levi-Civita torsion-free corollary.
- `canonical/gr_closure/gap_10i_integrability_selection.tex` — explicit affine Minkowski/constant-tetrad representers; one-sided invertible curved no-go; exact two-sided curvature identity.
- `tools/verify_covariant_tetrad_rank.py` — exact algebra and rank verification.
- `tools/verify_gap_10omega_connection.py` — Levi-Civita, polar-frame, uniqueness, and contorsion reconstruction checks.
- `tools/verify_gap_10i_integrability.py` — Minkowski representer, one-sided injectivity, and two-sided curvature checks.
- Closed/narrowed: GAP-10K, GAP-10Ω-KIN, GAP-10Ω-GR, GAP-10L-CONN, GAP-10I-SR, GAP-10I-1S (no-go), GAP-10I-2S (narrowed).
- Open: GAP-10T-DYN, GAP-10L-DYN, GAP-10I-CURVED, GAP-10D, GAP-10ψ, GAP-B-MASTER, GAP-U2Θ.
- The earlier compact-ψ fiber-average closure is retained as a noncanonical exploratory branch.

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
