# Copilot Task List — v20 Blockers and Final Polish
_Date: 2025-11-06_0731_

> **Goal:** Make UBT ready for an OSF/Zenodo release by unifying the α/B derivation, proving acyclicity of dependencies, and tightening SU(3) exposition — without changing core UBT principles.

---

## 1) Unify the B derivation (blocking)
**Files:** `consolidation_project/appendix_ALPHA_one_loop_biquat.tex`, `ALPHA_SYMBOLIC_B_DERIVATION.md`  
**Deliverable:** One continuous symbolic chain from Θ‑action to `B≈46.3` with no “placeholder” coefficients.

**Exact steps:**
1. In `appendix_ALPHA_one_loop_biquat.tex`:
   - Replace mixed narrative with a **numbered derivation**:  
     (i) Θ‑action in biquaternion time with compactification `ψ ~ ψ + 2π` and UV cut‑off `Λ=1/R_ψ`  
     (ii) One‑loop vacuum polarization `Π(μ; R_ψ)` in the compact direction (show integral limits and gauge-fixing)  
     (iii) Extract β‑function `d(1/α)/d ln μ = B/(2π)`  
     (iv) Derive `B = B(R_ψ, N_eff, 𝓡)` where `N_eff=12` from mode counting and `𝓡` is the 2‑loop renorm factor
   - Include the **winding‑mode integral** explicitly with all pre‑factors (2π, volume factors).

2. In `ALPHA_SYMBOLIC_B_DERIVATION.md`:
   - Mirror the same chain in prose, with a **boxed final formula** for `B`.
   - Provide a short **SymPy pseudocode** block (we will supply a full script separately).

3. Update `FITTED_PARAMETERS.md`:
   - Move `B` to **Derived** once the above is merged.  
   - Clearly mark `Λ=1/R_ψ` and `N_eff=12` as **geometric/mode-count inputs**, not fit.

---

## 2) Prove α–mₑ acyclicity (blocking)
**Files:** `consolidation_project/appendix_E2_fermion_masses.tex`, `consolidation_project/appendix_E3_neutrino_masses.tex`, `README.md`

**Tasks:**
- Insert a **dependency DAG figure** (TikZ or ASCII) in README and in E2 intro:  
  `Topology + Loop  →  α(μ)  →  SM renorm (g_i(μ))  →  Yukawa/texture  →  m_e`  
- Grep entire repo to ensure **α is not used upstream** when defining the mass texture.  
- Add a 1‑paragraph **“Dependency Hygiene”** note to E2 stating α is upstream, mₑ downstream.

---

## 3) SU(3) explicit mapping (important polish)
**Files:** `consolidation_project/appendix_G_internal_color_symmetry.tex`

**Tasks:**
- Add explicit Gell‑Mann matrices `λ₁..λ₈`, the commutation table, and `f^{abc}`.  
- Provide the explicit map from the **internal biquaternion phase manifold** to the **Cartan subalgebra** (T₃,T₈).  
- One **Worked Example**: derive a sample color gauge potential from a specified internal phase configuration and show why **non‑Abelian self‑terms** do not enter the **U(1)-only α** derivation.

---

## 4) Documentation edits (quick wins)
- `B_CONSTANT_DERIVATION_SUMMARY.md`: replace “in agreement with empirical value” by “implied by the unified derivation with `Λ=1/R_ψ`, `N_eff=12`, `𝓡`”.  
- `SPECULATIVE_VS_EMPIRICAL.md`: confirm F2 (psychons) is labeled **speculative** and not included by `ubt_core_main.tex` nor `ubt_2_main.tex`.  
- Regenerate PDFs via CI and ensure no unresolved references.

---

## 5) SymPy check (to be added by us after merge)
- We will add `tools/symbolic/alpha_B_check.py` that reproduces the final B value from the explicit integrals and prints the numeric decomposition:  
  `B = B_winding × 𝓡 → 25.1 × 1.84 = 46.2` (example).

---

### Definition of Done
- Build passes; PDFs updated  
- Single α/B chain present and internally consistent  
- Dependency DAG included; no α–mₑ cycles  
- SU(3) appendix contains explicit matrices and mapping  
- `FITTED_PARAMETERS.md` reclassified accordingly  
- Green light for **OSF/Zenodo release**

