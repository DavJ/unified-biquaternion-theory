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
- Projected/real-sector admissibility assumptions explicitly stated

Sources: `canonical/fields/`, `canonical/THEORY/math/fields/`

### 3) Emergent geometry and GR recovery

- Derived metric construction from Θ
- Non-degeneracy and Lorentzian-signature chain
- Einstein-equation recovery in admissible real projection
- Schwarzschild-sector recovery and perturbation-sector closure tracking

Sources: `canonical/geometry/`, `canonical/gr_closure/`, `papers/UBT_GR_Submission.tex`

**GR closure files:**
- `canonical/gr_closure/step1_metric_bridge.tex` — Step 1 — [L1] — Metric from Θ
- `canonical/gr_closure/step2_nondegeneracy.tex` — Step 2 — [L1] — Non-degeneracy
- `canonical/gr_closure/step3_signature_theorem.tex` — Step 3 — [L1] — Lorentzian signature
- `canonical/gr_closure/step3_einstein_with_matter.tex` — Step 5 — [L1] — Einstein equations
- `canonical/gr_closure/zerilli_derivation.tex` — GAP-Z — [L1] — Zerilli even-parity graviton
- `canonical/gr_closure/frw_cosmological_solutions.tex` — GAP-C — [L1]+[MC] — FRW in solution space [L1]; Θ-ansatz [MC]; g_0i sub-gap [L1 conditional on comoving-frame averaging]

### 4) Gauge and interaction recovery

- SU(3) × SU(2) × U(1) structural recovery tracks
- Chirality and QED-sector derivations where closed
- Explicit open gaps retained (e.g., unresolved Higgs/Yukawa closures)

Sources: `canonical/interactions/`, `canonical/su3_derivation/`, `canonical/chirality/`, `papers/UBT_Gauge_Submission.tex`

**Chirality derivation files:**
- `canonical/chirality/step3_gap_C1_resolution.tex` — Gap C1 Step 3 — [L1] — SU(2)_L acts on left-chiral doublets
- `canonical/chirality/step4_no_wr_derivation.tex` — Gap C1 upgrade — [MC] — SU(2)_R decouples from n>0 matter via ψ-parity; Loopholes 1 [L1 cond.] and 3 [STD] closed; OP-S4 (Loophole 2) open

### 5) α (fine-structure) track with explicit gap discipline

- Canonical route inventory and proof-status discipline
- Conditional/derived results separated from open blockers
- Gaps are explicit and not hidden

Sources: `canonical/alpha/`, `canonical/n_eff/`, `reports/`

research_tracks/T3_ALPHA/mellin_insertion_B.tex | Gap G137-B no-go record |
  [L0]+[L1]+[OBS] | Six routes NO-GO; 3 sub-gaps G137-B-i/ii/iii named [OPEN/MC];
  T3_ALPHA downgraded to STRUCTURAL EVIDENCE 2026-06-11; Alpha NOT DERIVED

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
