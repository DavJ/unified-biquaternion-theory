<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# QUANTUM_ROADMAP.md — UBT Quantum Development Roadmap

**Author**: Ing. David Jaroš  
**Date**: 2026-05-18  
**Status**: PLANNING DOCUMENT — not a claims document  
**Supersedes**: `docs/QUANTUM_CORRECTIONS_ROADMAP.md` (marked legacy/superseded)  
**Relates to**: `research_tracks/quantum_ubt/GAP_Q_scope.md`, `docs/quantum_sector_status.md`

---

## Preamble and Claim-Level Discipline

UBT is currently a **classical field theory**.  
The fundamental field Θ(q,τ) ∈ ℂ⊗ℍ and the field equations ∇†∇Θ = κ𝒯  
are classical Euler-Lagrange equations.

**No quantum closure claim is made in this document.**  
Every milestone below carries an explicit status label drawn from
[`CLAIMS_MATRIX.md`](../CLAIMS_MATRIX.md):

| Label | Meaning |
|---|---|
| **PROVED** | Rigorous derivation in canonical sources |
| **DERIVED_WITH_ASSUMPTIONS** | Derivation present; assumptions explicitly stated |
| **NUMERICAL_EVIDENCE** | Reproducible numerical result; not a theorem |
| **CONJECTURE** | Plausible but unproven |
| **OPEN_GAP** | Required; no derivation available |
| **SPECULATIVE** | Exploratory only; not part of canonical claim set |

---

## Current State (2026-05-18)

### What exists

| Item | Status | Source |
|---|---|---|
| Numerical Theta-state evolution scaffold | NUMERICAL_EVIDENCE | `src/ubt/quantum/quantum_scaffold.py` |
| Reproducible stochastic evolution proxy | NUMERICAL_EVIDENCE | `src/ubt/quantum/quantum_scaffold.py` |
| Soliton energy regularization scaffold | NUMERICAL_EVIDENCE | `src/ubt/solitons/regularization.py` |
| Chirality and parity algebra scaffold | DERIVED_WITH_ASSUMPTIONS | `src/ubt/algebra/chirality.py` |
| Observable bridge scaffold | OPEN_GAP (placeholder) | `src/ubt/observables/physics_observable_bridge.py` |
| GAP-Q problem scoping | SCOPING_DOC | `research_tracks/quantum_ubt/GAP_Q_scope.md` |
| One-loop effective potential for winding modes | DERIVED_WITH_ASSUMPTIONS | `canonical/n_eff/` |
| Free propagator identification (KG structure) | CONJECTURE | `research_tracks/quantum_ubt/GAP_Q_scope.md §2.2` |
| SM gauge-fixing and FP ghost procedure applicability | CONJECTURE | `research_tracks/quantum_ubt/GAP_Q_scope.md §3` |

### What is explicitly missing

| Gap | Status | Blocker |
|---|---|---|
| Path-integral measure 𝒟Θ for ℂ⊗ℍ-valued field | OPEN_GAP | Non-standard field space; no standard reference applies |
| Canonical commutation relations from UBT action | OPEN_GAP | No Hamiltonian formulation available |
| Hilbert-space inner product for UBT states | OPEN_GAP | Depends on canonical commutation relations |
| Born rule derivation from UBT | OPEN_GAP | Depends on Hilbert-space structure |
| Mapping from Θ energy density to probability amplitude | OPEN_GAP | Depends on Born rule |
| Gravity-Θ interaction vertices | OPEN_GAP | Non-polynomial coupling; non-perturbative regime |
| UV completeness / renormalisability proof | OPEN_GAP | Full 5D theory is non-renormalisable by power-counting |
| One-loop SM Feynman rules recovery from UBT | OPEN_GAP | Classical recovery proved; quantum recovery not attempted |
| Anomaly cancellation from UBT first principles | OPEN_GAP | Depends on fermion hypercharge closure (C2 gap in ROADMAP.md) |

---

## Roadmap Phases

### Phase 0 — Scaffold and gap-mapping ✅ DONE

**Goal**: Establish reproducible numerical scaffolding and document all open derivation gaps  
**Completion criterion**: Tests pass; all gaps labeled; no gap hidden

**Deliverables** (all complete):

- [x] `src/ubt/quantum/quantum_scaffold.py` — deterministic and stochastic evolution scaffold
- [x] `src/ubt/solitons/regularization.py` — finite-energy regularization scaffold
- [x] `src/ubt/algebra/chirality.py` — Clifford/chirality algebra scaffold
- [x] `src/ubt/observables/physics_observable_bridge.py` — observable bridge scaffold
- [x] `docs/quantum_sector_status.md` — gap inventory
- [x] `research_tracks/renormalization/finite_energy_soliton_regularization.md`
- [x] `research_tracks/weak_sector/chirality_and_parity_status.md`
- [x] `CLAIMS_MATRIX.md` — all quantum claims labeled OPEN_GAP or CONJECTURE
- [x] `DERIVATION_INDEX.md` — quantum open gaps enumerated
- [x] Tests: quantum scaffold, soliton regularization, chirality, observable bridge

**Test suite entry point**:

```bash
PYTHONPATH=. python3 -m pytest tests/test_quantum_scaffold.py \
    tests/test_soliton_regularization.py \
    tests/test_chirality_scaffold.py \
    tests/test_observable_bridge.py -v
```

---

### Phase 1 — Tractable near-term quantum calculations

**Goal**: Execute the quantum computations identified as accessible in
`research_tracks/quantum_ubt/GAP_Q_scope.md §5` without claiming full quantum closure.

**Priority**: High — these do not require full GAP-Q resolution.  
**Entry gate**: Phase 0 complete ✅

**Milestone 1.1 — One-loop beta function for U(1)_Y**

- Compute the one-loop beta function β₀ for U(1)_Y from the UBT effective action.
- Compare with SM value β₀ = 41/6.
- Status target: **DERIVED_WITH_ASSUMPTIONS** (assumptions: KK-truncation, 4D effective theory limit).
- Deliverable: `research_tracks/quantum_ubt/ubt_u1y_beta_function.tex`
- Exit criterion: explicit agreement with SM value under stated KK assumptions;
  discrepancy (if any) documented as a gap, not suppressed.

**Milestone 1.2 — Anomaly cancellation check**

- Verify that the UBT fermion content (three generations, SM representations)
  satisfies SM anomaly cancellation conditions.
- Status target: **DERIVED_WITH_ASSUMPTIONS** (assumes fermion content = SM;
  hypercharge assignments C2 gap still open).
- Deliverable: `research_tracks/quantum_ubt/anomaly_cancellation_check.tex`
- Exit criterion: explicit pass/fail for each anomaly condition; C2 gap clearly noted.

**Milestone 1.3 — Heat kernel / Seeley-DeWitt B₂ coefficient**

- Compute the one-loop effective action via heat kernel expansion.
- This is the B_base computation referenced in the T3_ALPHA track.
- Status target: **DERIVED_WITH_ASSUMPTIONS**.
- Deliverable: `research_tracks/quantum_ubt/seeley_dewitt_b2_ubt.tex`
- Exit criterion: explicit agreement with known SM heat kernel in the real limit;
  UBT-specific correction terms isolated and labeled as conjectural until verified.

**Milestone 1.4 — Free propagator explicit derivation**

- Extract the Θ field propagator ⟨Θ(x)Θ†(y)⟩₀ from the kinetic term of S[Θ].
- Identify momentum-space structure (Klein-Gordon with Mat(2,ℂ) matrix structure).
- Status target: **DERIVED_WITH_ASSUMPTIONS** (quadratic expansion around classical solution).
- Deliverable: extend `research_tracks/quantum_ubt/GAP_Q_scope.md §2.2`
  or new file `research_tracks/quantum_ubt/ubt_free_propagator.tex`.
- Exit criterion: momentum-space propagator written down with full index structure;
  comparison to SM scalar propagator explicit; gravity-Θ non-polynomial vertices
  explicitly deferred as OPEN_GAP.

---

### Phase 2 — Foundation derivations (medium-term, multi-year)

**Goal**: Derive the minimum formal structures needed for a rigorous quantum UBT.  
**Entry gate**: Phase 1 milestones closed.  
**Status of all items in this phase**: **OPEN_GAP** until individually closed.

**Milestone 2.1 — Hamiltonian formulation of UBT**

- Construct the Hamiltonian H[Θ] from the canonical action S[Θ].
- Identify conjugate momenta Π = δS/δ(∂_τΘ).
- Required for: canonical commutation relations.
- Challenge: complex-time coordinate τ = t + iψ complicates Legendre transform.
- Exit criterion: H[Θ] written explicitly; equal-time Poisson brackets stated.

**Milestone 2.2 — Canonical commutation relations**

- Promote Poisson brackets to commutators: [Θ, Π] = iℏδ³(x−y).
- Requires: Milestone 2.1.
- Challenge: ℂ⊗ℍ-valued fields require careful specification of
  which components commute; no standard reference.
- Exit criterion: explicit commutation relations written; representation
  on a Hilbert space identified or proved non-existent.

**Milestone 2.3 — Hilbert-space inner product**

- Define ⟨ψ₁|ψ₂⟩ on the space of UBT states.
- Required for: Born rule, probability interpretation.
- Challenge: inner product must be positive-definite; UBT field values are
  complex — standard L² inner product may not be positive on the full space.
- Exit criterion: inner product written down; positivity condition verified
  or counterexample produced.

**Milestone 2.4 — Born rule derivation**

- Derive Prob(outcome A) = |⟨A|ψ⟩|² (or its UBT analogue) from UBT structure.
- Requires: Milestones 2.2, 2.3.
- This is the hardest foundational step. No known shortcut.
- Exit criterion: explicit derivation or formal reduction to standard QM Born rule
  under stated assumptions; assumptions recorded in CLAIMS_MATRIX.md.

**Milestone 2.5 — Path-integral measure 𝒟Θ**

- Define 𝒟Θ rigorously for Θ: M⁴ × S¹_ψ → Mat(2,ℂ).
- Minimum requirements: Gaussian measure on L²(M⁴ × S¹_ψ, Mat(2,ℂ));
  gauge-fixing for SM local symmetry; Faddeev-Popov ghosts.
- Challenge: ℂ⊗ℍ symmetry may require non-standard ghost sector.
- Exit criterion: partition function Z = ∫𝒟Θ exp(iS[Θ]/ℏ) written in
  gauge-fixed form with explicit ghost action; UV regularization stated.

---

### Phase 3 — Full quantum-UBT closure (long-term)

**Goal**: Full quantum field theory of UBT including UV completeness,
Standard Model Feynman rule recovery at one loop, and observable predictions.

**Entry gate**: Phase 2 milestones closed.  
**Status**: **OPEN_GAP** for all items. Multi-year research programme.

**Milestone 3.1 — UV completeness / renormalisability proof**

- Determine whether UBT is (a) perturbatively renormalisable, (b) UV-complete
  via asymptotic safety, or (c) UV-incomplete (formally dead-end result).
- Power-counting note: full 5D UBT is non-renormalisable by power-counting
  ([g²] = −1 in mass units for 5D Yang-Mills). Asymptotic safety or
  string embedding required for UV completeness.
- Exit criterion: formal classification with proof; asymptotic-safety route
  (if pursued) requires non-perturbative functional RG analysis.

**Milestone 3.2 — One-loop SM Feynman rules recovery**

- Show that in the KK limit the UBT one-loop effective action reduces
  to the SM one-loop effective action.
- Requires: Milestone 2.5, Milestone 3.1 (at least 4D effective-theory regime).
- Exit criterion: explicit matching condition between UBT and SM one-loop
  contributions for at least one gauge-boson process; Appelquist-Carazzone
  decoupling of KK modes demonstrated.

**Milestone 3.3 — Gravity-Θ vertex renormalisability**

- Analyse UV behaviour of gravity-Θ vertices arising from the
  metric construction g_μν = Re[Tr(∂_μΘ · ∂_νΘ†)]/𝒩.
- These vertices are non-polynomial and likely UV-problematic.
- Exit criterion: power-counting done; divergence structure mapped;
  counterterm set identified or formal dead-end stated.

**Milestone 3.4 — Observable prediction promotion**

- Promote at least one entry in `src/ubt/observables/physics_observable_bridge.py`
  from OPEN_GAP to a genuine prediction.
- Requires: Milestones 2.4, 3.1, and the relevant Phase 1 milestone.
- Exit criterion: `ObservableResult.value` is non-None, `status` is DERIVED_WITH_ASSUMPTIONS
  or better, with no target-observable fitting in the derivation.

---

### Parallel Track R — Renormalization and soliton energy

**Goal**: Close the RG derivation gap opened by the finite-energy soliton scaffold.  
**Entry gate**: None (independent of Phases 1–3). Can proceed in parallel.

| Milestone | Status | Deliverable |
|---|---|---|
| R.1 Derive RG flow equations from S[Θ] (functional RG) | OPEN_GAP | `research_tracks/renormalization/ubt_functional_rg.tex` |
| R.2 Show cutoff-independence of physical soliton energy | OPEN_GAP | Update `research_tracks/renormalization/finite_energy_soliton_regularization.md` |
| R.3 Identify physical vs numerical regulator | OPEN_GAP | Clarify `SolitonRegularizationConfig.cutoff_length` role |

---

### Parallel Track W — Weak-sector chirality

**Goal**: Derive SU(2)_L coupling from UBT geometry, resolving CONJECTURE status.  
**Entry gate**: Phase 1.1 (beta function) useful; not strictly blocking.

| Milestone | Status | Deliverable |
|---|---|---|
| W.1 Derive SU(2)_L coupling constant from UBT structure | OPEN_GAP | `research_tracks/weak_sector/su2l_coupling_derivation.tex` |
| W.2 Hypercharge assignment derivation | OPEN_GAP | Depends on gap C2 from ROADMAP.md §5 |
| W.3 Anomaly cancellation from first principles | OPEN_GAP | Depends on W.2 |
| W.4 W/Z mass mechanism derivation | OPEN_GAP | Separate paper; post-W.1 |
| W.5 CPT theorem from UBT action | OPEN_GAP | `research_tracks/weak_sector/cpt_proof.tex` |

---

## Claim gates: what must be true before status upgrades

### Before any claim "UBT quantum field theory is closed"

All of the following must be satisfied:

- [ ] Hilbert-space inner product defined and positive-definite (Milestone 2.3)
- [ ] Born rule derived from UBT (Milestone 2.4)
- [ ] Path-integral measure 𝒟Θ rigorously defined (Milestone 2.5)
- [ ] UV completeness or renormalisability proved (Milestone 3.1)
- [ ] SM Feynman rules recovered at one loop (Milestone 3.2)
- [ ] All results recorded in CLAIMS_MATRIX.md

### Before any observable can be marked as a UBT prediction

- [ ] Derivation path from UBT action to the observable is explicit
- [ ] No fitting to the target observable in the derivation
- [ ] Uncertainty budget and sensitivity analysis complete
- [ ] Reproducible implementation and passing tests
- [ ] Value and comparison target are explicitly separated in `physics_observable_bridge.py`

See also: [`docs/observable_bridge.md`](observable_bridge.md).

---

## What is NOT on this roadmap

The following are explicitly excluded from quantum-UBT development:

- Consciousness / psychons — **SPECULATIVE**, outside canonical physics
- ThetaComm — **SPECULATIVE**, outside canonical physics
- Afterlife / survival-of-consciousness claims — **SPECULATIVE**
- Any quantum calculation that requires fixing free parameters to match data
  (those belong in `research_tracks/`, labeled NUMERICAL_EVIDENCE at best)
- Quantum gravity (full) — beyond scope; see ROADMAP.md §Phase 4
  note on GAP-Q as "very long term"

---

## Document relationships

| Document | Role |
|---|---|
| `ROADMAP.md` (root) | Top-level programme roadmap; GAP-Q is "very long term" in Phase 4 |
| `research_tracks/quantum_ubt/GAP_Q_scope.md` | Detailed scoping of the quantisation problem |
| `docs/quantum_sector_status.md` | Current scaffold implementation status |
| `CLAIMS_MATRIX.md` | Authoritative claim-level registry |
| `DERIVATION_INDEX.md` | Canonical derivation chain with open gaps |
| `src/ubt/quantum/quantum_scaffold.py` | Code scaffold with explicit TODO markers |
| `docs/QUANTUM_ROADMAP.md` (this file) | Forward-looking development plan |

---

## Update policy

This document is updated when:

1. A milestone changes status (closed / killed / downgraded)
2. A new gap is identified and scoped
3. ROADMAP.md Phase 4 priorities change

Previous versions are preserved in git history. No version is deleted.

---

*This is a planning document. No result herein constitutes a claim of UBT physics
at any proof level. All proof-status changes must be recorded in CLAIMS_MATRIX.md.*
