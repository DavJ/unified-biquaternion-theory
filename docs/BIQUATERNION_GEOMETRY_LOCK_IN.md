# BIQUATERNION GEOMETRY LOCK-IN
## Unified Biquaternion Theory - Fundamental Geometry Enforcement

**Date**: January 2026  
**Status**: CANONICAL REFERENCE  
**Author**: Ing. David Jaroš

---

## Executive Summary

This document establishes the **absolute precedence** of biquaternionic geometry in the Unified Biquaternion Theory (UBT). All geometric and dynamical structures are defined at the biquaternionic level. General Relativity appears **only as a real (Hermitian) projection**, never as a fundamental axiom.

**Critical principle**: Removing all `Re(...)` operators does NOT invalidate UBT. The theory is fundamentally biquaternionic.

---

## PHASE 1: CORE BIQUATERNIONIC GEOMETRY

### 1. METRIC - Fundamental Biquaternionic Object

**Fundamental Definition:**
```
𝓖_μν(x) ∈ 𝔹 = ℍ ⊗ ℂ
```

The biquaternionic metric is the **ONLY** fundamental metric object.

**Derivation Hierarchy:**
1. Biquaternionic tetrad: `E_μ(x) ∈ 𝔹`
2. Metric from tetrad: `𝓖_μν = Sc(E_μ E_ν†)`
3. Classical metric (derived): `g_μν := Re(𝓖_μν)`

**PROHIBITION:**
❌ **NEVER** introduce `g_μν` without explicit reference to `𝓖_μν`  
❌ **NEVER** write "Let g_μν be the spacetime metric"  
❌ **NEVER** postulate `g_μν` as fundamental

**REQUIRED:**
✅ Always write: `g_μν := Re(𝓖_μν)` (projection)  
✅ Label `g_μν` as "observer-level quantity"  
✅ State "GR limit" or "real projection" when using classical metric

**File location**: `canonical/geometry/biquaternion_metric.tex`

---

### 2. TETRAD - Most Fundamental Object

**Fundamental Definition:**
```
E_μ(x) ∈ 𝔹
```

The biquaternionic tetrad is the **deepest level** of geometric description.

**Metric Definition via Tetrad:**
```
𝓖_μν := Sc(E_μ E_ν†)
```

**PROHIBITION:**
❌ **FORBIDDEN** to introduce metric without tetrad derivation

**REQUIRED:**
✅ All metrics must be derived from tetrads  
✅ State explicitly: `𝓖_μν = Sc(E_μ E_ν†)`

**File location**: `canonical/geometry/biquaternion_tetrad.tex`

---

### 3. CONNECTION - Fundamental Biquaternionic Connection

**Fundamental Definition:**
```
Ω_μ(x) ∈ 𝔹
```

The biquaternionic connection is fundamental. Christoffel symbols are **derived**.

**Compatibility Condition:**
```
∇_μ E_ν = ∂_μ E_ν + Ω_μ ∘ E_ν - Γ^λ_μν E_λ = 0
```

**CRITICAL:** Do NOT simplify commutators `[Ω_μ, Ω_ν]` or assume commutativity.

**Christoffel Symbols (Derived):**
```
Γ^λ_μν = Re(Ω^λ_μν)
```

**PROHIBITION:**
❌ **NEVER** postulate Christoffel symbols independently  
❌ **NEVER** use Levi-Civita connection without stating it's derived  
❌ **NEVER** assume torsion-free as axiom

**REQUIRED:**
✅ Always derive: `Γ^λ_μν := Re(Ω^λ_μν)`  
✅ State "derived from biquaternionic connection"  
✅ Preserve full non-commutative structure

**File location**: `canonical/geometry/biquaternion_connection.tex`

---

### 4. CURVATURE - Biquaternionic Field Strength

**Fundamental Definition:**
```
𝓡_μν = ∂_μ Ω_ν - ∂_ν Ω_μ + [Ω_μ, Ω_ν]
```

The biquaternionic curvature is the field strength of `Ω_μ`.

**Ricci Tensor:**
```
𝓡_νσ = E^μ ⋆ 𝓡_μν ⋆ E_σ
```

**Classical Ricci (Derived):**
```
R_μν := Re(𝓡_μν)
```

**PROHIBITION:**
❌ **NEVER** define Riemann tensor directly from Christoffel symbols as fundamental  
❌ **NEVER** write classical Ricci without stating "GR limit"

**REQUIRED:**
✅ Always: `R_μν := Re(𝓡_μν)`  
✅ Label: "classical Ricci is real projection"  
✅ Define curvature from `Ω_μ` first, then project

**File location**: `canonical/geometry/biquaternion_curvature.tex`

---

### 5. STRESS-ENERGY - Geometric Phase Response

**Fundamental Definition:**
```
𝓣_μν = ⟨D_μΘ, D_νΘ⟩_𝔹 - ½𝓖_μν⟨DΘ, DΘ⟩
```

Stress-energy is a **geometric phase response**, NOT an external matter source.

**Classical Stress-Energy (Derived):**
```
T_μν := Re(𝓣_μν)
```

**CRITICAL PRINCIPLE:**
- Energy-momentum arises from `Θ` field gradients
- There is NO external matter source
- `𝓣_μν` is self-generated from geometry

**PROHIBITION:**
❌ **NEVER** introduce `T_μν` as external matter source  
❌ **NEVER** write "matter source" without clarifying it's geometric  
❌ **NEVER** postulate stress-energy independently of `Θ`

**REQUIRED:**
✅ Always: `T_μν := Re(𝓣_μν)`  
✅ State: "geometric phase response"  
✅ Emphasize: NOT external matter

**File location**: `canonical/geometry/biquaternion_stress_energy.tex`

---

### 6. FIELD EQUATIONS - Biquaternionic Einstein Equations

**Fundamental Equation:**
```
𝓖_μν = κ𝓣_μν
```

where `𝓖_μν = 𝓡_μν - ½𝓖_μν𝓡` is the biquaternionic Einstein tensor.

**Einstein's Equations (GR Limit):**
```
Re(𝓖_μν) = κRe(𝓣_μν)  ⇒  G_μν = 8πG T_μν
```

**PROHIBITION:**
❌ **NEVER** write `G_μν = κT_μν` as the fundamental equation  
❌ **NEVER** state Einstein equations without "after Re(...)"

**REQUIRED:**
✅ State: "Einstein equations arise only after Re(...) projection"  
✅ Label: "GR limit" or "real sector"  
✅ Emphasize: fundamental equation is biquaternionic

**File locations**: 
- `canonical/geometry/biquaternion_metric.tex`
- `canonical/geometry/biquaternion_curvature.tex`

---

## PHASE 2: ENFORCEMENT & CLEANUP

### 7. REMOVE HIDDEN GR ASSUMPTIONS

**Search and Replace Operations:**

| ❌ FORBIDDEN LANGUAGE | ✅ REQUIRED REPLACEMENT |
|----------------------|------------------------|
| "Let g_μν be the spacetime metric" | "The real projection g_μν := Re(𝓖_μν)" |
| "Assume a 4D Lorentzian manifold" | "The real sector of biquaternionic geometry" |
| "standard Einstein equations" | "Einstein equations (GR limit via Re(...))" |
| "Christoffel symbols are..." | "Christoffel symbols Γ^λ_μν := Re(Ω^λ_μν) are derived" |
| "Ricci tensor R_μν" | "Ricci tensor R_μν := Re(𝓡_μν) (real projection)" |
| "matter source T_μν" | "stress-energy T_μν := Re(𝓣_μν) (geometric phase response)" |

**Global Enforcement:**
- Every use of `g_μν` must include derivation from `𝓖_μν`
- Every GR reference must state "real projection" or "GR limit"
- No classical GR equation can be stated without biquaternionic origin

---

### 8. NOTATION CONSISTENCY

**Mandatory Notation Rules:**

1. **Biquaternionic objects**: Gothic script
   - Metric: `𝓖_μν`
   - Connection: `Ω_μ`
   - Curvature: `𝓡_μν`
   - Stress-energy: `𝓣_μν`
   - Einstein tensor: `𝓖_μν`

2. **Classical objects**: Regular script with explicit projection
   - Metric: `g_μν := Re(𝓖_μν)`
   - Christoffel: `Γ^λ_μν := Re(Ω^λ_μν)`
   - Ricci: `R_μν := Re(𝓡_μν)`
   - Stress-energy: `T_μν := Re(𝓣_μν)`
   - Einstein tensor: `G_μν := Re(𝓖_μν)`

3. **Projection operator**: Always explicit
   - Write: `Re(...)` or `text{Re}(...)`
   - Never omit the projection

**PROHIBITION:**
❌ Mixing notation without explanation  
❌ Using `g_μν` without stating `g_μν := Re(𝓖_μν)`  
❌ Implicit projections

---

### 9. Θ → GEOMETRY LINK

**Explicit Coupling Statement:**

The `Θ` field configuration directly determines geometry:
```
𝓖_μν = 𝓖_μν[Θ]
```

**Variation:**
```
δ𝓖_μν ∼ ⟨D_μΘ, δΘ⟩ + ⟨δΘ, D_μΘ⟩
```

**Critical principles:**
- Geometry is NOT background-independent of `Θ`
- `Θ` configurations contribute to `𝓖_μν`
- Stress-energy arises from `Θ` gradients: `𝓣_μν ∼ ⟨D_μΘ, D_νΘ⟩`
- Energy-momentum is geometric, not external

**REQUIRED in all documents:**
✅ State: "`Θ` configurations contribute to geometry"  
✅ Write: `𝓖_μν[Θ]` to show functional dependence  
✅ Emphasize: "stress-energy is geometric phase response"

---

### 10. EXOTIC REGIMES MARKING

**Definition of Exotic Regime:**
```
Im(𝓖_μν) ≠ 0
```

**Required Labeling:**

For all solutions with non-zero imaginary components:

✅ **Mark as:**
- "Physically valid in UBT"
- "Invisible to classical GR observations"
- "Responsible for [specific phenomenon]"

✅ **Physical Phenomena:**
- Pseudo-antigravitational behavior (from phase curvature)
- Metric cloaking (dark matter effects)
- Temporal drift (imaginary time evolution)
- Consciousness coupling (psychon fields)
- Dark energy (negative phase pressure)

**PROHIBITION:**
❌ Calling exotic regimes "violations"  
❌ Treating `Im(𝓖_μν) ≠ 0` as unphysical

**File location**: `canonical/geometry/exotic_regimes.tex`

---

## PHASE 3: AUDIT & LOCK-IN

### 11. GLOBAL AUDIT CHECKLIST

**Verification Requirements:**

✅ **No dynamical equation depends solely on g_μν**
- All dynamics must reference `𝓖_μν`
- Classical equations must be labeled "GR limit"

✅ **No curvature exists without Ω_μ**
- All curvature must derive from `𝓡_μν = ∂_μΩ_ν - ∂_νΩ_μ + [Ω_μ, Ω_ν]`
- Christoffel-based curvature must state "derived"

✅ **No conclusion drawn from Re(...) without labeling**
- Every `Re(...)` must be labeled "real projection", "GR limit", or "observer sector"
- Physical conclusions must reference biquaternionic origin

✅ **Removing Re(...) does not invalidate theory**
- Theory must be internally consistent at biquaternionic level
- Real projection is observational restriction, not theoretical necessity

---

### 12. LOCK-IN STATEMENT

**Standard Lock-In Text** (to be inserted in all major documents):

---

**BIQUATERNION GEOMETRY LOCK-IN:**

All geometric and dynamical structures in this work are defined at the biquaternionic level:

- **Metric**: `𝓖_μν(x) ∈ 𝔹`, derived from tetrads via `𝓖_μν = Sc(E_μ E_ν†)`. Classical metric: `g_μν := Re(𝓖_μν)`.

- **Connection**: `Ω_μ(x) ∈ 𝔹` (fundamental). Christoffel symbols: `Γ^λ_μν := Re(Ω^λ_μν)` (derived).

- **Curvature**: `𝓡_μν = ∂_μΩ_ν - ∂_νΩ_μ + [Ω_μ, Ω_ν]` (fundamental). Ricci tensor: `R_μν := Re(𝓡_μν)` (derived).

- **Stress-energy**: `𝓣_μν = ⟨D_μΘ, D_νΘ⟩_𝔹 - ½𝓖_μν⟨DΘ, DΘ⟩` (geometric phase response). Classical: `T_μν := Re(𝓣_μν)`.

- **Field equations**: `𝓖_μν = κ𝓣_μν` (biquaternionic). Einstein equations arise only after `Re(...)` projection.

Any real-valued spacetime metric, curvature, or stress-energy tensor represents a Hermitian projection corresponding to an observer-restricted sector. No physical conclusion should be interpreted at the level of the real projection alone.

**General Relativity arises as the real projection of fundamental biquaternionic geometry.**

---

**Files updated**:
- `UBT_Main.tex`
- `THEORY_STATUS_DISCLAIMER.tex`
- All documents using geometric structures

---

### 13. FUTURE-PROOFING RULE

**Mandatory for All Future Extensions:**

Any future extension of UBT must:

1. **Define dynamics biquaternionically**
   - New fields: specify biquaternionic structure
   - New interactions: define at `𝔹` level first

2. **Specify GR sector via Re(...)**
   - Explicitly state classical limit
   - Show how projection works

3. **Avoid classical GR objects as axioms**
   - Never introduce `g_μν`, `Γ^λ_μν`, `T_μν` as fundamental
   - Always derive from biquaternionic objects

**Applies to:**
- New appendices
- Phenomenological discussions
- Experimental proposals
- Cosmological models
- Quantum corrections

**Enforcement:**
- Code review must check for violations
- All new documents must include lock-in statement
- Violations must be corrected before merging

---

### 14. FINAL CHECKLIST

**Repository-Wide Verification:**

- [ ] ✅ Removing all `Re(...)` operators does not invalidate theory
- [ ] ✅ No equation relies fundamentally on classical GR objects
- [ ] ✅ Exotic regimes arise naturally from `Im(𝓖_μν) ≠ 0`
- [ ] ✅ GR appears only as restricted observational sector
- [ ] ✅ All documents include lock-in statement
- [ ] ✅ All geometric objects traced to biquaternionic origin
- [ ] ✅ No hidden GR assumptions remain
- [ ] ✅ Notation is consistent throughout
- [ ] ✅ `Θ → geometry` coupling explicitly stated
- [ ] ✅ Stress-energy labeled as geometric, not external source

**If any item fails → refactor until it passes**

---

## CANONICAL FILE STRUCTURE

### Core Biquaternionic Geometry Files

**Primary canonical definitions** (in `canonical/geometry/`):

1. `biquaternion_tetrad.tex` - Fundamental: `E_μ ∈ 𝔹`
2. `biquaternion_metric.tex` - Fundamental: `𝓖_μν ∈ 𝔹`
3. `biquaternion_connection.tex` - Fundamental: `Ω_μ ∈ 𝔹`
4. `biquaternion_curvature.tex` - Fundamental: `𝓡_μν ∈ 𝔹`
5. `biquaternion_stress_energy.tex` - Fundamental: `𝓣_μν ∈ 𝔹`
6. `exotic_regimes.tex` - Physical: `Im(𝓖_μν) ≠ 0` regimes

**Derived classical quantities** (labeled as projections):

7. `metric.tex` - Derived: `g_μν := Re(𝓖_μν)`
8. `curvature.tex` - Derived: `R_μν := Re(𝓡_μν)`
9. `stress_energy.tex` - Derived: `T_μν := Re(𝓣_μν)`

**Hierarchy:**
```
Θ field
  ↓
E_μ (tetrad)
  ↓
𝓖_μν (metric)  ←→  Ω_μ (connection)
  ↓                    ↓
g_μν (projection)   Γ^λ_μν (projection)
  ↓                    ↓
GR observables    Classical curvature
```

---

## IMPLEMENTATION STATUS

### Completed (Phase 1)

✅ Biquaternionic geometry framework established  
✅ Canonical files created with proper structure  
✅ Tetrad formalism implemented  
✅ Connection, curvature, stress-energy defined  
✅ Classical quantities properly derived

### In Progress (Phase 2)

🔄 Enhanced lock-in statements in main documents  
🔄 Notation consistency enforcement  
🔄 Θ → geometry coupling emphasized  
🔄 Exotic regime marking

### Remaining (Phase 3)

⏳ Global audit of all TeX files  
⏳ Search and replace classical GR language  
⏳ Final verification checklist  
⏳ Documentation build and test

---

## REFERENCES

**Primary Documents:**
- `UBT_Main.tex` - Main theory document with lock-in
- `THEORY_STATUS_DISCLAIMER.tex` - Status and lock-in for all documents
- `canonical/README.md` - Canonical framework overview

**Geometry Implementation:**
- `canonical/geometry/` - All canonical geometry definitions

**Related Documents:**
- `BIQUATERNION_GEOMETRY_REFACTOR_SUMMARY.md` - Previous refactor summary
- `CANONICAL_DEFINITIONS.md` - Canonical framework rules
- `UBT_COPILOT_INSTRUCTIONS.md` - Development guidelines

---

## VERSION HISTORY

- **v1.0** (2026-01-08): Initial lock-in document created
- Implements full PHASE 1-3 requirements from geometry refactor task

---

**© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0**

This document is part of the Unified Biquaternion Theory canonical framework and must be referenced in all work involving UBT geometry.
