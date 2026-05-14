# Minimal Completion Plan
## Unified Biquaternion Theory — Post-Audit Targeted Actions

**Date:** 2026-03-10  
**Basis:** `copilot_repo_verification_and_gap_report.md` and `claim_evidence_matrix.md`  
**Principle:** Smallest possible change to close each genuine gap. No rederivations.

---

## Prerequisites

This plan is applied **after** verification. The following are NOT on this plan because they are already present:

- GR recovery chain (Steps 1–5) — verified_present
- Action principle — verified_present
- Stress-energy derivation — verified_present
- SU(3) emergence — verified_present
- Three generations — verified_present
- Alpha structural argument (V_eff min at n=137) — verified_present
- N_eff = 12 — verified_present
- Lorentzian signature theorem — verified_present
- Massless photon — verified_present
- QED Lagrangian — verified_present

---

## Tier 1 — Reviewer Navigability (HIGH PRIORITY)

These items do not add new physics. They make the existing proved results traversable for an external reviewer without requiring them to locate 6+ files manually.

### T1.1 — Create `canonical/bridges/` directory and GR chain bridge

**What:** A single LaTeX file that maps the GR recovery chain to its canonical source files, with cross-references and a status annotation for each step.

**Why:** The chain is split across `metric.tex`, `curvature.tex`, `gr_as_limit.tex`, `GR_chain_summary.tex`, `appendix_GR_embedding.tex`, and `stress_energy.tex`. An external reviewer cannot traverse this without guidance.

**File:** `canonical/bridges/GR_chain_bridge.tex`

**Rules:**
- Cross-references only; no new derivations
- Reproduce no equations; only cite and locate
- Mark Step 6 (off-shell) as [L2] open, consistent with `GR_chain_summary.tex`

**Effort:** ~1 hour  
**Blocking:** No other step depends on this

---

### T1.2 — Create `canonical/bridges/QED_limit_bridge.tex`

**What:** A single LaTeX file cross-referencing the QED limit material, the B_base open problem, and the Maxwell limit.

**Why:** The QED limit is in `qed.tex`, `STATUS_ALPHA.md`, and `appendix_GR_embedding.tex`. The B_base gap is documented in `STATUS_ALPHA.md` and `DERIVATION_INDEX.md` but is not explicitly connected to the QED limit claim in one place.

**File:** `canonical/bridges/QED_limit_bridge.tex`

**Content:**
1. Pointer to `qed.tex` for Lagrangian
2. Pointer to `STATUS_ALPHA.md` for running coupling derivation
3. Explicit statement: Maxwell limit follows from QED Lagrangian at φ=const (no new derivation needed)
4. Explicit gap box: B_base = N_eff^(3/2) exponent — Open Hard Problem (do not invent derivation)

**Effort:** ~1 hour  
**Blocking:** No other step depends on this

---

### T1.3 — Create `canonical/bridges/gauge_emergence_bridge.tex`

**What:** A single LaTeX file summarizing the gauge group emergence with precise status labels.

**Why:** `sm_gauge.tex` contains the full derivation but mixes proved and semi-empirical results. A bridge file with explicit status labels per claim (proved / semi-empirical / open) reduces reviewer confusion.

**File:** `canonical/bridges/gauge_emergence_bridge.tex`

**Content:**
1. SU(3)_c from involutions — PROVED [L0] (pointer to Theorems G.A–G.D in `sm_gauge.tex`)
2. SU(2)_L from left action — PROVED [L0]
3. U(1)_Y from right action — PROVED [L0]
4. Weinberg angle θ_W — SEMI-EMPIRICAL (cannot be fixed by ℂ⊗ℍ alone; note open)
5. Chirality (SU(2)_L only) — MOTIVATED (ψ-parity; not fully derived)

**Effort:** ~45 minutes  
**Blocking:** No other step depends on this

---

## Tier 2 — Canonical Completeness (MEDIUM PRIORITY)

### T2.1 — Create `canonical/geometry/connection.tex` stub

**What:** A minimal canonical file defining Christoffel symbols and pointing to their derivation in `curvature.tex`.

**Why:** The canonical geometry directory has `metric.tex`, `curvature.tex`, `stress_energy.tex`, `gr_as_limit.tex` but no `connection.tex`. Christoffel symbols are defined inside `curvature.tex`. This breaks the expected one-file-per-concept structure.

**File:** `canonical/geometry/connection.tex`

**Content (stub — ~30 lines):**
```latex
% Canonical: Levi-Civita connection
% Christoffel symbols Γ^λ_μν are defined in curvature.tex
% This file is a navigational stub
```
Plus the canonical definition and a pointer.

**Effort:** ~20 minutes  
**Blocking:** None

---

### T2.2 — Add disambiguation note to `DERIVATION_INDEX.md`

**What:** A single line or short paragraph distinguishing `B_base` (used in α derivation, value 41.57) from `B_m` (used in the fermion mass formula, value −14.099 MeV).

**Why:** Both symbols are called "B" in their respective derivation chains. Cross-file readers may confuse them, especially since both appear in STATUS_ALPHA.md and STATUS_FERMIONS.md.

**Location:** Under the B_base entry in `DERIVATION_INDEX.md`

**Content:** "Note: B_base (α) and B_m (fermion masses) are distinct objects with different dimensions and physical interpretation."

**Effort:** ~5 minutes  
**Blocking:** None

---

### T2.3 — Add signature convention note to `canonical/geometry/metric.tex`

**What:** A short "Signature conventions" remark noting that some legacy files use (−,+,+,+) while the canonical convention is (+,−,−,−), and that they are physically equivalent (overall sign flip).

**Why:** Prevents reviewer confusion when comparing canonical files with older derivation files.

**Location:** In `canonical/geometry/metric.tex`, under the existing Properties section

**Effort:** ~10 minutes  
**Blocking:** None

---

## Tier 3 — Documentation Only (LOW PRIORITY)

### T3.1 — Update `canonical/README.md` to reference `canonical/bridges/`

After T1.1–T1.3 create the bridges directory, add a line to `canonical/README.md` explaining the bridges subdirectory and when to use it versus the primary canonical files.

**Effort:** ~5 minutes  
**Blocking:** Requires T1.1 to be complete

---

## NOT on this plan (explicitly excluded)

The following are genuine open problems but are **not** addressable by minimal edits. They require original research.

| Open problem | Reason for exclusion |
|---|---|
| B_base = N_eff^(3/2) derivation | 22 approaches exhausted; requires original mathematical insight |
| R ≈ 1.114 geometric origin | 8 approaches exhausted; requires original insight |
| Lepton mass ratios from first principles | KK mismatch is a proved theorem; requires new mechanism |
| Quark theta-function integrals on SU(3) | Estimated 1–2 year calculation |
| Neutrino mass full derivation | Type-I see-saw identified but full calculation not started |
| Weinberg angle from ℂ⊗ℍ | May require additional structure beyond ℂ⊗ℍ |
| Chirality selection proof | Requires formal proof of ψ-parity argument |
| S-matrix / perturbative QFT dynamics | Full QFT formalism development required |
| Off-shell GR closure [L2] | Structural obstruction; requires new mathematical approach |

---

## Completion Checklist

- [ ] T1.1 — `canonical/bridges/GR_chain_bridge.tex` created
- [ ] T1.2 — `canonical/bridges/QED_limit_bridge.tex` created
- [ ] T1.3 — `canonical/bridges/gauge_emergence_bridge.tex` created
- [ ] T2.1 — `canonical/geometry/connection.tex` stub created
- [ ] T2.2 — B_base disambiguation note added to `DERIVATION_INDEX.md`
- [ ] T2.3 — Signature convention note added to `canonical/geometry/metric.tex`
- [ ] T3.1 — `canonical/README.md` updated to reference bridges

---

## Success Criteria

After completing this plan:

1. An external referee can traverse the GR recovery chain in one document (bridge) without reading 6 separate files
2. The QED limit claim is unambiguously bounded: what is proved, what is semi-empirical, and what is open are clearly separated
3. The gauge group emergence status (proved / semi-empirical / open) is visible in one place
4. The canonical geometry directory is complete with a connection.tex file (even if it's a pointer stub)
5. The B_base vs B_m distinction is documented in the derivation index
6. No existing derivation has been weakened, removed, or modified
7. No speculative material has been introduced as canonical

---

*This plan was produced by GitHub Copilot as the smallest-possible completion after a verify-first audit. It adds navigability; it does not change the theory.*
