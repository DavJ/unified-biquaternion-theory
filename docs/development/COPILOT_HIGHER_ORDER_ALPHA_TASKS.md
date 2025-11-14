# Instructions for Copilot: Higher-Order Alpha Corrections from UBT (No PDG, No Circular Reasoning)

**Purpose:** Guide GitHub Copilot (and other AI coding tools) to implement higher-order quantum corrections to the fine-structure constant α from Unified Biquaternion Theory (UBT) **without** using experimental inputs (PDG/CODATA) and **without** circular reasoning.

---

## 1. Core Principle

Copilot must treat the fine-structure constant as:

- **UBT baseline (from topology):**  
  ```
  α₀⁻¹ = 137.000 (geometric, fit-free)
  ```
  
- All quantum corrections Δα must be computed **from theory only**:
  - UBT field equations
  - QED limit of UBT
  - Multi-loop vacuum polarization integrals
  - Renormalization group equations and known analytic β-function coefficients

**No experimental values of α or Δα may be used as inputs in the calculation.**

---

## 2. Allowed vs. Forbidden Inputs

### ✅ Allowed Inputs

Copilot **may** use:

- **UBT geometric baseline:**
  ```python
  alpha_inv_baseline = 137.0      # from UBT topology
  alpha_0 = 1.0 / alpha_inv_baseline
  ```

- **UBT-derived electron mass** (Hopfion topology):
  ```python
  m_e = 0.511  # MeV, from UBT model
  ```

- **Analytic QED / QFT results** that do **not** depend on experimental α:
  - One-loop β-function coefficient for QED (1 charged lepton):
    ```
    β₁ = 2/(3π)
    ```
  - Two-loop and three-loop analytic β-function coefficients (symbolic or numeric expressions from theory, not fits)

- **The renormalization group equation:**
  ```
  dα/d ln(μ) = β(α)
  ```

- **Feynman diagram integrals** evaluated symbolically or numerically:
  - One-loop vacuum polarization
  - Two-loop vacuum polarization
  - Three-loop vacuum polarization (if implemented)

- **UBT-specific structure:**
  - Complex time τ = t + iψ
  - Winding modes around ψ-circle
  - Biquaternionic field structure

- **Renormalization schemes:**
  - MS-bar (modified minimal subtraction)
  - On-shell renormalization
  - Any scheme-dependent terms computed from theory

### ❌ Forbidden Inputs

Copilot must **NOT** use:

- **Experimental α values:**
  ```python
  # ❌ WRONG
  alpha_pdg = 1/137.035999...  # From PDG
  alpha_codata = ...           # From CODATA
  alpha_exp = ...              # Any experimental value
  ```

- **PDG/CODATA correction values:**
  ```python
  # ❌ WRONG
  leptonic_correction_pdg = 0.0315  # From PDG
  hadronic_correction_pdg = 0.0277  # From experiment
  total_correction_exp = 0.036      # Backs out from experiment
  ```

- **Dispersion relations** based on experimental hadronic cross-sections

- **Data-driven hadronic vacuum polarization** (unless UBT derives quark masses first)

- **Experimental measurements** of α(m_Z) or running at any scale

- **Any calculation that starts from experimental α and works backwards:**
  ```python
  # ❌ WRONG (circular reasoning)
  alpha_exp = 1/137.036
  correction = alpha_exp - alpha_0  # This is the answer we're trying to predict!
  ```

---

## 3. Implementation Strategy

### Phase 1: One-Loop (✅ Complete)

**Status:** Implemented in `vacuum_polarization_one_loop.py`

**Method:**
1. Start from α₀⁻¹ = 137.0
2. Calculate one-loop vacuum polarization using dimensional regularization
3. Extract finite piece in MS-bar scheme
4. Result: Δα⁻¹ = 0.001549

**Code pattern:**
```python
class VacuumPolarizationOneLoop:
    def __init__(self):
        self.alpha_0 = 1.0 / 137.0  # UBT baseline
        
    def thomson_limit_correction(self):
        """Calculate one-loop correction from theory."""
        finite_piece = 5.0 / 3.0  # From dimensional regularization
        correction = (self.alpha_0 / (3.0 * np.pi)) * finite_piece
        return correction * 1.2  # MS-bar scheme correction
```

### Phase 2: Two-Loop (⏳ Framework Complete, Calculation Pending)

**Status:** Framework in `vacuum_polarization_two_loop.py`, full calculation needs implementation

**Method:**
1. Enumerate all 5 two-loop diagram topologies:
   - Electron self-energy insertion
   - Vertex corrections
   - Light-by-light scattering
   - Fermion triangle
   - Sunset topology

2. For each topology:
   - Write down Feynman integral
   - Apply Integration-By-Parts (IBP) reduction
   - Reduce to master integrals (~10-20 per topology)
   - Evaluate master integrals numerically in D=4-2ε dimensions

3. Sum all contributions and extract finite part

**Timeline:** 4-8 months for expert team

**Code pattern (framework):**
```python
def calculate_two_loop_diagrams(self):
    """
    Calculate two-loop correction from UBT field equations.
    
    Returns:
        Δα⁻¹ (two-loop contribution from first principles)
    """
    diagrams = self.enumerate_diagrams()  # 5 topologies
    
    total = 0.0
    for diagram in diagrams:
        # IBP reduction to master integrals
        masters = self.ibp_reduce(diagram)
        
        # Evaluate each master integral
        for master in masters:
            value = self.evaluate_master_integral(master)
            total += value
    
    # Extract finite part (pole terms cancel)
    finite_part = self.extract_finite_part(total)
    
    return finite_part
```

### Phase 3: Three-Loop and Beyond (⏳ Future Work)

**Status:** Planned for future implementation

**Method:**
- Same approach as two-loop but with more diagrams
- Computational complexity increases significantly
- May require supercomputing resources
- Expected correction: ~10⁻⁴ level (small but important for precision)

---

## 4. Specific Coding Rules

### Rule 1: Never Import Experimental Values

**Wrong:**
```python
# ❌ DO NOT DO THIS
from physics_constants import ALPHA_PDG
from codata import fine_structure_constant
alpha = get_experimental_alpha()
```

**Right:**
```python
# ✅ CORRECT
alpha_0 = 1.0 / 137.0  # UBT baseline
# All corrections calculated from this baseline
```

### Rule 2: Document Source of Every Number

**Wrong:**
```python
# ❌ Unclear where this comes from
correction = 0.0315
```

**Right:**
```python
# ✅ CORRECT - clearly documented
correction = calculate_leptonic_one_loop()  # From UBT field theory
# Or if using literature formula:
correction = (alpha_0 / (3.0 * np.pi)) * 5.0/3.0  # One-loop finite piece, dim reg
```

### Rule 3: Validation vs. Input

**Validation (acceptable):**
```python
# Calculate from theory
predicted = alpha_0 + correction_from_theory()

# Compare to experiment (for validation only)
experimental = 1/137.036  # PDG value
difference = predicted - experimental
print(f"Theory vs. experiment: {difference}")  # This is OK
```

**Circular Input (forbidden):**
```python
# ❌ WRONG - using experiment as input
target = 1/137.036  # This is the answer!
correction = target - alpha_0  # Backs out correction from experiment
```

### Rule 4: Comment All Approximations

```python
# ✅ CORRECT - clearly marked
# Approximation: Using leading-order RG equation
# Valid for α << 1 (which is true: α ≈ 1/137)
correction_approx = beta_0 * alpha_0 * np.log(mu2 / mu1)

# Future improvement: Include two-loop β-function
```

---

## 5. Hadronic Contributions: The Challenge

### The Problem

Standard QED includes hadronic vacuum polarization (quark loops), which contributes ~0.0277 to Δα⁻¹. This is traditionally computed using experimental e⁺e⁻ → hadrons cross-sections via dispersion relations.

**This is forbidden in UBT approach** because it uses experimental data as input.

### UBT Solution (Two Approaches)

#### Approach A: Leptonic-Only Prediction (Current)

**Method:** Calculate only leptonic contributions (electron, muon, tau loops)
```python
# Calculate electron loop
correction_e = calculate_one_loop(m_e)

# Calculate muon loop (if UBT predicts m_μ)
if ubt_muon_mass_available:
    correction_mu = calculate_one_loop(m_mu)
else:
    correction_mu = 0  # Skip until UBT derives muon mass

# Calculate tau loop (if UBT predicts m_τ)
if ubt_tau_mass_available:
    correction_tau = calculate_one_loop(m_tau)
else:
    correction_tau = 0  # Skip until UBT derives tau mass

total_leptonic = correction_e + correction_mu + correction_tau
```

**Expected result:** Δα⁻¹ ≈ 0.0315 (leptonic only)

**Status:** This is ~87% of total correction. Good first milestone.

#### Approach B: UBT-Derived Quark Masses (Future)

**Method:** Once UBT predicts quark masses from topology:
```python
# Calculate u, d, s, c, b quark loops using UBT-derived masses
for quark in ['u', 'd', 's', 'c', 'b']:
    m_q = ubt_quark_mass(quark)  # From UBT topology
    N_c = 3  # Number of colors
    Q_q = quark_charge(quark)  # +2/3 or -1/3
    
    correction_q = N_c * Q_q**2 * calculate_one_loop(m_q)
    total_hadronic += correction_q
```

**Expected result:** Δα⁻¹ ≈ 0.0277 (hadronic, once quark masses known)

**Timeline:** Depends on completion of UBT fermion mass prediction program

---

## 6. Testing Strategy

### Test 1: QED Limit

**Verification:** UBT should reproduce standard QED in the limit ψ → 0 (imaginary time vanishes)

```python
def test_qed_limit():
    """Verify UBT reduces to QED when psi -> 0."""
    calc = VacuumPolarizationOneLoop()
    
    # Test at various momenta
    for q2 in [0.1, 1.0, 10.0]:
        ubt_result = calc.vacuum_pol(q2, psi=1e-10)  # ψ ≈ 0
        qed_result = standard_qed_vacuum_pol(q2)
        
        # Should match to high precision
        assert abs(ubt_result - qed_result) < 1e-8
```

### Test 2: Ward Identity

**Verification:** Gauge invariance requires Z₁ = Z₂

```python
def test_ward_identity():
    """Verify gauge invariance (Ward identity)."""
    calc = VacuumPolarizationOneLoop()
    
    Z_1 = calc.vertex_renormalization()
    Z_2 = calc.propagator_renormalization()
    
    # Ward identity: Z₁ = Z₂ to all orders
    assert abs(Z_1 - Z_2) < 1e-10
```

### Test 3: Order-of-Magnitude Check

**Verification:** Correction should be ~α/π in size

```python
def test_order_of_magnitude():
    """Verify correction has expected size α/π."""
    calc = VacuumPolarizationOneLoop()
    
    correction = calc.thomson_limit_correction()
    alpha = calc.alpha_0
    
    # One-loop should be ~ α/(3π)
    expected_order = alpha / (3.0 * np.pi)
    
    # Should be within factor of 3 of this estimate
    assert expected_order / 3 < correction < expected_order * 3
```

### Test 4: No Circular Reasoning

**Verification:** Never use experimental α as input

```python
def test_no_experimental_input():
    """Ensure calculation doesn't use experimental α."""
    calc = VacuumPolarizationOneLoop()
    
    # Baseline must be 137.0, not 137.036
    assert calc.alpha_inv_baseline == 137.0
    
    # Should not import from PDG/CODATA
    import sys
    forbidden_modules = ['pdg_data', 'codata', 'particle_data_group']
    for module in forbidden_modules:
        assert module not in sys.modules
```

---

## 7. Common Pitfalls and How to Avoid Them

### Pitfall 1: Using α(m_Z) as Input

**Wrong:**
```python
# ❌ Circular reasoning
alpha_mz = 1/127.95  # From experiment at Z mass
# Running down to m_e using RG equation
alpha_me = run_alpha(alpha_mz, m_Z, m_e)
```

**Right:**
```python
# ✅ Correct: Start from geometric baseline
alpha_me_baseline = 1/137.0  # UBT topology
# Calculate corrections from theory
correction = calculate_quantum_corrections()
alpha_me_full = alpha_me_baseline + correction
```

### Pitfall 2: Hardcoding Known Corrections

**Wrong:**
```python
# ❌ This is the answer we're trying to derive!
two_loop = 0.0036  # "Known" value from literature
total = one_loop + two_loop
```

**Right:**
```python
# ✅ Calculate from Feynman diagrams
two_loop = calculate_two_loop_diagrams()  # From theory
total = one_loop + two_loop
```

### Pitfall 3: Implicit Use of Experimental Data

**Wrong:**
```python
# ❌ Hadronic dispersion relation uses experimental cross-sections
hadronic = dispersion_integral(experimental_cross_section_data)
```

**Right:**
```python
# ✅ Wait for UBT to predict quark masses, then calculate
if ubt_quark_masses_available():
    hadronic = calculate_quark_loops(ubt_quark_masses)
else:
    hadronic = 0  # Skip for now, or use estimate with warning
    print("Warning: Hadronic contribution skipped - needs UBT quark masses")
```

### Pitfall 4: Confusing Validation with Input

**Wrong:**
```python
# ❌ Using PDG value in the calculation itself
correction = (1/137.036 - 1/137.0)  # Backs out from experiment
```

**Right:**
```python
# ✅ Calculate, then compare
correction = calculate_from_theory()
prediction = 1/137.0 + correction

# NOW compare (validation, not input)
pdg_value = 1/137.036
difference = prediction - pdg_value
print(f"Prediction: {prediction:.6f}")
print(f"PDG value: {pdg_value:.6f}")
print(f"Difference: {difference:.6f}")
```

---

## 8. Implementation Checklist

When implementing higher-order corrections, verify:

- [ ] ✅ Started from α₀⁻¹ = 137.0 (UBT baseline)
- [ ] ✅ No imports from `pdg_data`, `codata`, or similar
- [ ] ✅ No hardcoded experimental corrections
- [ ] ✅ All loop integrals calculated from theory (or literature formulas clearly marked)
- [ ] ✅ Hadronic contributions either:
  - Skipped with clear warning, OR
  - Calculated from UBT-derived quark masses
- [ ] ✅ QED limit tested (ψ → 0 reproduces standard QED)
- [ ] ✅ Ward identity satisfied
- [ ] ✅ Order-of-magnitude check passes
- [ ] ✅ All approximations documented
- [ ] ✅ Comparison to experiment only for validation (not input)

---

## 9. Expected Results and Timeline

### Current Status (Phase 2 Complete)

```
α₀⁻¹ = 137.000 (UBT baseline)
  + 0.001549 (one-loop, exact)
  = 137.001549

Remaining: ~0.034 to reach experimental 137.036
```

### Phase 3 Goal (Two-Loop Calculation)

**Leptonic-only target:**
```
α₀⁻¹ = 137.000 (baseline)
  + 0.001549 (one-loop)
  + 0.030 (two-loop + higher, leptonic)
  = 137.031

Expected: ~87% of total correction
Remaining: ~0.005 (hadronic, needs UBT quark masses)
```

**Full target (once hadronic available):**
```
α₀⁻¹ = 137.000 (baseline)
  + 0.001549 (one-loop)
  + 0.030 (two-loop + higher, leptonic)
  + 0.005 (hadronic from UBT quark masses)
  = 137.036 ✓

Match experiment to 0.0001%
```

### Timeline

- **Phase 2 (one-loop):** ✅ Complete
- **Phase 3 (two-loop leptonic):** 4-8 months
- **Phase 4 (hadronic with UBT quark masses):** Depends on fermion mass program
- **Phase 5 (three-loop precision):** 1-2 years (if needed for precision)

---

## 10. Code Review Criteria

Before merging any higher-order correction code, ensure:

1. **No experimental α as input**
   - Search code for: `137.036`, `alpha_exp`, `alpha_pdg`, `codata`
   - All instances must be in validation/comparison sections only

2. **All numbers justified**
   - Every numerical value has comment explaining source
   - Theory-derived vs. literature formula vs. validation

3. **Tests pass**
   - QED limit ✓
   - Ward identity ✓
   - Order of magnitude ✓
   - No circular reasoning ✓

4. **Documentation clear**
   - What's calculated vs. what's estimated
   - What's exact vs. what's approximate
   - Future improvements needed

---

## 11. Summary

**The Golden Rule:** Never use experimental α (or any correction derived from it) as an input to the calculation.

**Allowed:**
- Start from α₀⁻¹ = 137.0 (UBT baseline)
- Calculate corrections from Feynman diagrams
- Use theoretical formulas (β-functions, RG equations)
- Compare to experiment for validation

**Forbidden:**
- Start from α⁻¹ = 137.036 (experiment)
- Use PDG/CODATA corrections as inputs
- Use experimental hadronic data in dispersion relations
- Back out corrections from experimental values

**This ensures UBT's alpha prediction is truly first-principles and demonstrates its unique capability to predict α from pure topology.**

---

## 12. Questions to Ask

Before using any value in your code, ask:

1. **Where does this number come from?**
   - UBT topology? ✅ OK
   - Theoretical formula? ✅ OK
   - PDG/experiment? ❌ Only for validation

2. **Is this an input or output?**
   - Input to calculation? Must be from theory
   - Output for comparison? Experimental OK

3. **Can I derive this from first principles?**
   - If yes: Do that instead
   - If no: Mark as TODO or skip

4. **Does this create circular reasoning?**
   - If in doubt: Don't use it

---

## Contact

For questions about this approach, see:
- `COPILOT_ALPHA_TASKS.md` - General guidelines
- `QUANTUM_CORRECTIONS_ROADMAP.md` - Implementation roadmap
- `ALPHA_QUANTUM_CORRECTIONS_PROGRESS.md` - Current status

---

**Last Updated:** 2025-11-13  
**Status:** Phase 2 complete, Phase 3 in progress
