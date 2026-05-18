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

### 4) Gauge and interaction recovery

- SU(3) × SU(2) × U(1) structural recovery tracks
- Chirality and QED-sector derivations where closed
- Explicit open gaps retained (e.g., unresolved Higgs/Yukawa closures)

Sources: `canonical/interactions/`, `canonical/su3_derivation/`, `canonical/chirality/`, `papers/UBT_Gauge_Submission.tex`

### 5) α (fine-structure) track with explicit gap discipline

- Canonical route inventory and proof-status discipline
- Conditional/derived results separated from open blockers
- Gaps are explicit and not hidden

Sources: `canonical/alpha/`, `canonical/n_eff/`, `reports/`

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
