<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Canonical Chain Check

This document verifies that the canonical theory backbone is readable and
navigable end-to-end. It does not re-derive the theory; it confirms that
each link in the chain can be followed by a reader starting from first principles.

**Last checked:** March 2026  
**Status:** NAVIGABLE — all links present

---

## The Canonical Theory Chain

### Step 1 — Algebraic Foundations

**Source:** `canonical/algebra/biquaternion_algebra.tex`

The theory starts with the biquaternion algebra ℂ ⊗ ℍ:
- Four basis elements {1, i, j, k} with Hamilton quaternion rules
- Complex coefficients extend the algebra
- Involution structure gives rise to gauge symmetries (see `canonical/algebra/involutions_Z2xZ2xZ2.tex`)

**Key reference:** `canonical/AXIOMS.md` — axioms A–F define the complete
algebraic foundation

**Navigation:** `canonical/algebra/` → `canonical/AXIOMS.md`

---

### Step 2 — Fundamental Field

**Source:** `canonical/fields/theta_field.tex`

The fundamental field Θ(q, τ) is defined over the biquaternion space:
- q ∈ ℂ ⊗ ℍ — biquaternion coordinate
- τ = t + iψ — complex time parameter (real time t, phase ψ)
- Θ takes values in ℂ ⊗ ℍ

The complex time structure is defined in `canonical/fields/biquaternion_time.tex`.

**Navigation:** `canonical/fields/` → `canonical/AXIOMS.md §Axiom B`

---

### Step 3 — Metric Construction

**Source:** `canonical/geometry/biquaternion_metric.tex`

The biquaternionic metric 𝒢_{μν} is constructed from Θ:
- 𝒢_{μν} = D_μΘ†·D_νΘ (schematically)
- g_{μν} := Re(𝒢_{μν}) — classical metric as real projection

This defines the **unique emergent metric** (Axiom C in `canonical/AXIOMS.md`).
No background metric is assumed.

The projection rule g_{μν} := Re(𝒢_{μν}) appears explicitly in
`canonical/geometry/metric.tex` and in `canonical/geometry/phase_projection.tex`.

**Navigation:** `canonical/geometry/` → `canonical/AXIOMS.md §Axiom C`

---

### Step 4 — Curvature

**Source:** `canonical/geometry/biquaternion_curvature.tex`

Curvature tensors are derived from the biquaternionic connection:
- Biquaternionic Riemann tensor ℛ_{μνρσ}
- Ricci tensor ℛ_{μν} = projection of ℛ
- Classical curvature R_{μν} := Re(ℛ_{μν})

See also `canonical/geometry/biquaternion_connection.tex` for the connection.

**Navigation:** `canonical/geometry/curvature.tex`

---

### Step 5 — Stress-Energy and Sector Assumptions

**Source:** `canonical/geometry/biquaternion_stress_energy.tex`

The biquaternionic stress-energy tensor 𝒯_{μν} is constructed from Θ:
- 𝒯_{μν} couples to 𝒢_{μν} through the action
- Classical stress-energy T_{μν} := Re(𝒯_{μν})
- Matter sector follows from QED (φ=const limit): `canonical/qed_phi_const/`

**Navigation:** `canonical/geometry/stress_energy.tex`

---

### Step 6 — GR Limit and Closure

**Source:** `canonical/gr_limit/GR_limit_of_UBT.tex`  
**Summary:** `canonical/gr_closure/GR_chain_summary.tex`

GR is recovered as a sector/limit/projection, not for all Θ:

1. **Exact sector recovery**: On the admissible sector where GR-sector
   conditions C1–C6 hold, the UBT field equations reduce exactly to
   Einstein's field equations.
2. **Low-energy limit**: For φ ≈ const and ψ → 0, UBT recovers GR.
3. **No contradiction**: "UBT contains GR" and "not yet exact full Theta-only
   theorem" are compatible statements.

The conditions for exact GR recovery are defined in:  
`ARCHIVE/archive_legacy/consolidation_project/GR_closure/gr_sector_conditions.tex`

The status of GR recovery levels is documented in:  
`docs/reports/gr_recovery_levels.md`

**Navigation:** `canonical/gr_limit/` → `canonical/gr_closure/` →
`docs/ubt_gr_relationship.md`

---

## Navigation Summary Table

| Concept | Primary Source | Status |
|---------|---------------|--------|
| Biquaternion algebra ℂ⊗ℍ | `canonical/algebra/biquaternion_algebra.tex` | Proven [L0] |
| Complex time τ = t + iψ | `canonical/fields/biquaternion_time.tex` | Proven [L0] |
| Fundamental field Θ(q,τ) | `canonical/fields/theta_field.tex` | Proven [L0] |
| Emergent metric g_{μν} := Re(𝒢_{μν}) | `canonical/geometry/metric.tex` | Proven [L0] |
| Biquaternionic curvature | `canonical/geometry/biquaternion_curvature.tex` | Proven [L0] |
| Biquaternionic stress-energy | `canonical/geometry/biquaternion_stress_energy.tex` | Proven [L0] |
| GR sector conditions | `ARCHIVE/.../gr_sector_conditions.tex` | Proven [L1] |
| GR exact recovery (sector) | `canonical/gr_limit/GR_limit_of_UBT.tex` | Proven [L1] |
| Axioms | `canonical/AXIOMS.md` | Reference |
| GR recovery levels | `docs/reports/gr_recovery_levels.md` | Reference |

---

## Missing or Weak Links

The following gaps exist in the canonical chain but do NOT break its
navigability (they are documented open problems):

1. **Fine structure constant α** — derived numerically from multi-channel
   stability (n=137 is the preferred channel); fully first-principles derivation
   remains an **Open Hard Problem**. See `canonical/THEORY/topic_indexes/alpha_index.md`.

2. **B_base coefficient** — exponent 3/2 from heat kernel [L0]; coefficient
   from Kac-Moody level k=1 is a **Motivated Conjecture [L1]**, not derived.

3. **Fermion mass spectrum** — lepton ratios have structural explanation but
   the precise hierarchy requires instanton-mediated mixing (Open Problem).
   See `docs/reports/lepton_audit/`.

4. **Θ-only termwise separation** — the combined field-metric variation equation
   is the fundamental statement. Termwise separation into ∇†∇Θ = 0 and Einstein
   separately is NOT automatic. See `docs/reports/gr_recovery_levels.md`.

---

## How to Navigate the Canonical Chain

Start at: `canonical/AXIOMS.md`  
Follow through: `canonical/algebra/` → `canonical/fields/` →
`canonical/geometry/` → `canonical/gr_limit/`  
Status authority: `DERIVATION_INDEX.md`  
Layer map: `docs/REPO_LAYERS.md`

---

*This document is a navigation guide, not a derivation.*  
*For proof status, see `DERIVATION_INDEX.md`.*
