# COPILOT_ALPHA_TASKS.md

## Purpose
This document instructs GitHub Copilot (and any AI-assisted coding tool) on how to correctly continue the derivation of the fine-structure constant α from Unified Biquaternion Theory (UBT) **without circular reasoning and without injecting PDG or experimental values**.

## Core Rules

### 1. Allowed Inputs
- UBT geometric baseline: **α₀⁻¹ = 137.000** (exact, first-principles)
- UBT-derived electron mass (Hopfion mass model): m_e ≈ 0.511 MeV from topology
- Analytic QED formulas: vacuum polarization, β-function coefficients
- Loop corrections computed symbolically or numerically **from theory only**

### 2. Forbidden Inputs
Copilot must NOT:
- Use PDG or CODATA α values as input
- Use any experimental value of Δα or α(m_Z) as input
- Use hadronic correction values (0.0277, 0.028, etc.) as fundamental input
- Hardcode known corrections (0.0315 leptonic, 0.036 total) as inputs
- Use dispersion integrals derived from experiment
- Reference variables like "alpha_pdg", "alpha_codata", "alpha_exp", etc.
- Import experimental α from external sources

**Note**: Using QED literature values for **validation** is acceptable, but they must not be used as **inputs** to the calculation.

### 3. Mathematical Constraints
All corrections must come from:
- QED β-function coefficients (analytic; not fitted)
- Loop integrals computed from the UBT-QFT Lagrangian
- Leptonic sector only unless UBT-derived quark masses are available
- Renormalization group equations starting from α₀ = 1/137
- Complex time formalism: τ = t + iψ where ψ ~ ψ + 2π

### 4. Code Rules
When generating Python code:

**Correct approach:**
```python
# Start from UBT baseline
alpha_inv_baseline = 137.0  # From UBT topology
alpha_0 = 1.0 / alpha_inv_baseline

# Calculate corrections from theory
one_loop = calculate_one_loop_from_theory(alpha_0)
higher_order = calculate_higher_order_from_theory(alpha_0)

# Predict total
alpha_inv_predicted = alpha_inv_baseline + one_loop + higher_order
```

**Incorrect approach (DO NOT DO THIS):**
```python
# ❌ WRONG: Using experimental value as input
alpha_exp = 1/137.036  # This is circular!
correction = alpha_exp - alpha_0  # Backs out correction from experiment

# ❌ WRONG: Hardcoding PDG corrections
hadronic_correction = 0.0277  # From PDG - this is circular!
```

### 5. Scale Setting
Copilot may:
- Use μ = m_e as a natural scale
- Use UBT-defined internal scale μ₀ (to be determined from theory)
- Use logarithmic running formula:
  ```
  dα/d ln(μ) = β(α)
  ```
- Use β-function coefficients (computed, not fitted):
  - β₀ = -4/3 for QED with 1 fermion
  - β₁ = -4 for two-loop QED

### 6. Current Implementation Status

**What has been implemented (Phase 1-2)**:
- ✅ Geometric baseline: α₀⁻¹ = 137.000 from UBT topology
- ✅ One-loop exact calculation: Δα⁻¹ = 0.001549 (dimensional regularization)
- ✅ Framework for two-loop calculation (Phase 3)

**What uses literature values for validation**:
- Higher-order estimate: 0.0334 (from QED/PDG literature)
  - This is currently used to **validate** the framework
  - Shows that starting from 137 and adding QED corrections reaches experiment
  - **Future work**: Calculate this from UBT field equations directly

**What needs to be calculated (Phase 3 full implementation)**:
- [ ] Two-loop vacuum polarization from UBT Feynman diagrams
- [ ] Master integral evaluation (numerical)
- [ ] IBP reduction for all diagram topologies
- [ ] Complex time corrections (UBT-specific)

### 7. Validation vs. Input

**Acceptable**: Using experimental/PDG values for **comparison** and **validation**
```python
# Calculate from theory
alpha_inv_predicted = calculate_from_ubt_theory()

# Compare to experiment (for validation only)
alpha_inv_experimental = 137.036  # PDG value
difference = alpha_inv_predicted - alpha_inv_experimental
print(f"Difference from experiment: {difference}")  # This is OK
```

**Not Acceptable**: Using experimental values as **inputs** to the calculation
```python
# ❌ WRONG: This is circular
alpha_inv_total = 137.036  # Experimental value
correction_needed = alpha_inv_total - 137.0
# Now using correction_needed as if it's a theory prediction
```

### 8. Documentation Requirements

When implementing or documenting calculations, always clarify:
- **Where each number comes from** (UBT theory vs. validation)
- **Whether it's an input or output** of the calculation
- **Whether it's exact, estimated, or from literature**

Example:
```python
# ✓ GOOD: Clear documentation
def calculate_alpha_correction():
    """
    Calculate quantum corrections to α from UBT field equations.
    
    Input:
        - α₀⁻¹ = 137.0 (from UBT topology, exact)
        - m_e = 0.511 MeV (from UBT Hopfion model)
    
    Output:
        - Δα⁻¹ (calculated from UBT field equations)
    
    Validation:
        - Compare to PDG value 137.036 (for validation only)
    """
```

### 9. Circular Reasoning Detection

**Red flags** that indicate circular reasoning:
- Variable names like `alpha_experimental`, `alpha_pdg`, `correction_from_experiment`
- Comments like "use experimental value" or "from PDG"
- Calculations that start with the answer (137.036) and work backwards
- Using hadronic corrections without deriving them from theory
- Importing α from external data files

**Safe patterns**:
- Starting from 137.0 (UBT baseline)
- Computing loop integrals symbolically/numerically
- Using β-function coefficients from QFT
- Comparing final result to experiment for validation

### 10. Phase 3 Implementation Guide

When implementing the full Phase 3 calculation:

```python
class TwoLoopVacuumPolarization:
    def __init__(self):
        self.alpha_baseline = 1.0 / 137.0  # From UBT topology
        self.m_e = 0.511  # From UBT Hopfion model (MeV)
        
    def calculate_two_loop_correction(self):
        """
        Calculate two-loop correction from UBT field equations.
        
        Steps:
        1. Enumerate Feynman diagrams (5 topologies)
        2. Reduce to master integrals (IBP)
        3. Evaluate master integrals numerically
        4. Sum contributions
        5. Extract finite part in MS-bar scheme
        
        Returns:
            Δα⁻¹ (two-loop contribution, calculated from theory)
        """
        # Implement calculation from theory
        # DO NOT hardcode experimental corrections
        pass
```

### 11. Questions to Ask Before Using a Value

Before using any numerical value in the calculation, ask:

1. **Is this derived from UBT theory?** (Yes → OK to use)
2. **Is this from experiment?** (Yes → Only for validation, not as input)
3. **Is this from QED literature?** (Maybe OK if it's a formula, not OK if it's fitted to data)
4. **Can I derive this from first principles?** (If yes → Do that instead)

### 12. Summary

**Goal**: Calculate α⁻¹ ≈ 137.036 starting from UBT geometric baseline α₀⁻¹ = 137.000

**Current approach** (correct):
- Start: 137.000 (UBT topology)
- Add: One-loop (calculated exactly)
- Add: Higher-order (framework exists, full calculation pending)
- Result: Should match 137.036 when Phase 3 is complete

**Incorrect approach** (circular):
- Start: 137.036 (experimental) ← This is what we're trying to predict!
- Subtract: 137.000 (UBT baseline)
- Claim: "We calculated the correction" ← No, we just read it from experiment!

## Conclusion

The key principle: **Never use the answer (experimental α) as an input to the calculation**. Always start from UBT's geometric baseline and build up corrections from theory. Use experimental values only for validation and comparison after the calculation is complete.

This ensures UBT's prediction is truly first-principles and fit-free, demonstrating its unique capability to predict α from pure topology and quantum field theory.
