# Roadmap: From Experimental Calibration to First-Principles Calculation

**Purpose:** Transform current experimental-calibration code into genuine first-principles UBT derivations  
**Status:** Detailed implementation plan  
**Priority:** CRITICAL (addresses core credibility of UBT)

## Current Situation

| Constant | Theory Status | Code Status | Action Required |
|----------|---------------|-------------|-----------------|
| α⁻¹ | Framework complete, R_UBT=1 proven | Hardcoded 0.035999 | Implement 2-loop integrals |
| m_e | Framework exists, anchor proposed | Hardcoded 0.51099895 | Determine M_Θ, compute texture |
| m_μ, m_τ | Framework exists | NOT_IMPLEMENTED | Complete after m_e |

## Phase 1: Fix Alpha Derivation (3-6 months)

### Task 1.1: Implement Two-Loop Master Integrals

**Goal:** Replace hardcoded `delta_ct = 0.035999` with actual calculation

**Files to create/modify:**
- `alpha_core_repro/master_integrals_ct.py` (NEW)
- `alpha_core_repro/alpha_two_loop.py` (MODIFY)

**Dependencies:**
- Install: SymPy for symbolic manipulation
- Install: mpmath for high-precision numerics
- Optional: pySecDec or FIESTA for automated integration

**Steps:**

1. **Identify required integrals**
   ```python
   # Two-loop vacuum polarization in CT scheme
   # Requires 3 master integrals:
   # - I_1(q², m, ψ): One-loop bubble
   # - I_2(q², m, ψ): Two-loop sunrise
   # - I_3(q², m, ψ): Two-loop vertex
   ```

2. **Implement CT propagators**
   ```python
   def fermion_propagator_ct(k, m, psi):
       """
       Fermion propagator in complex time.
       k: 4-momentum
       m: mass
       psi: imaginary time parameter
       """
       k_tau = complexify_momentum(k, psi)
       return 1 / (k_tau.slash() - m + i*epsilon)
   ```

3. **Evaluate master integrals**
   ```python
   def compute_master_integral_I1(q2, m, psi):
       """
       One-loop bubble: ∫ d^4k/(2π)^4 1/[(k²-m²)((k+q)²-m²)]
       """
       # Use dimensional regularization
       # Evaluate in CT scheme with complex time
       # Extract finite part
       pass
   ```

4. **Thomson limit extraction**
   ```python
   def compute_delta_ct(p, psi=0):
       N_eff = 12
       R_psi = 1
       B = (2 * pi * N_eff) / (3 * R_psi)
       
       # Evaluate at q² = 0 (Thomson limit)
       I1 = compute_master_integral_I1(q2=0, m=0, psi=psi)
       I2 = compute_master_integral_I2(q2=0, m=0, psi=psi)
       I3 = compute_master_integral_I3(q2=0, m=0, psi=psi)
       
       # Combine with R_UBT = 1
       delta_ct = (B / (2*pi)) * (I1 + I2 + I3)
       
       # Scale running for other primes
       if p != 137:
           delta_ct += beta_function_correction(p, 137)
       
       return delta_ct
   ```

**Validation:**
```python
# Test 1: QED limit
assert abs(compute_delta_ct(137, psi=0) - 0.035999) < 1e-4

# Test 2: Complex time dependence
delta_psi = compute_delta_ct(137, psi=0.1)
# Should reduce continuously to QED

# Test 3: Gauge independence
delta_xi1 = compute_delta_ct(137, gauge_param=1.0)
delta_xi2 = compute_delta_ct(137, gauge_param=2.0)
assert abs(delta_xi1 - delta_xi2) < 1e-10
```

**Expected outcome:**
- `compute_delta_ct(137)` returns ~0.035999 from calculation
- Remove hardcoded value
- Match experiment as validation, not input

**Difficulty:** HIGH (PhD-level QFT)  
**Time estimate:** 2-3 months for experienced physicist

### Task 1.2: Derive Pipeline Function F(B)

**Goal:** Connect geometric B = 8π to numerical α⁻¹

**Theoretical work:**
1. Review beta function in CT scheme
2. Connect B parameter to charge renormalization
3. Derive relation B → α⁻¹ explicitly

**Code implementation:**
```python
def alpha_from_geometric_B(B, p=137):
    """
    Derive α⁻¹ from geometric parameter B.
    
    Based on: α⁻¹ = p + Δ_CT where Δ_CT = F(B)
    """
    # Solve: dα⁻¹/d(ln μ) = B/(2π)
    # With boundary condition from topology
    # Returns α at scale μ = p
    pass
```

**Expected outcome:**
- Mathematical derivation in LaTeX document
- Implementation in Python
- Verification: B = 8π → α⁻¹ ≈ 137.036

**Difficulty:** MEDIUM-HIGH  
**Time estimate:** 1-2 months

### Task 1.3: Update Documentation

**Files to update:**
- `CALCULATION_STATUS_ANALYSIS.md`
- `PYTHON_SCRIPTS_REPORT.md`
- `alpha_core_repro/README.md`
- `consolidation_project/alpha_two_loop/FIT_FREE_ALPHA_README.md`

**Changes:**
- ✅ "Fully derived from first principles" (when complete)
- ✅ "No fitted parameters"
- ✅ "Experimental match as validation"

## Phase 2: Determine Electron Mass Scale (4-8 months)

### Task 2.1: Choose and Implement Absolute Scale Anchor

**Goal:** Determine M_Θ from geometry (no experimental input)

**Option A: Geometric Normalization** (PREFERRED)

```python
def compute_absolute_scale_M_theta():
    """
    Determine absolute fermion mass scale from geometric normalization.
    
    Based on: Y₀ = Λ_H_C / √R_ψ
    """
    # 1. Determine characteristic scale from Hermitian slice
    Lambda_HC = compute_characteristic_scale_hermitian_slice()
    
    # 2. Use same R_ψ as in alpha derivation
    R_psi = 1  # From geometric normalization
    
    # 3. Compute Yukawa scale
    Y_0 = Lambda_HC / sqrt(R_psi)
    
    # 4. Effective Higgs vev in UBT
    v_eff = compute_effective_higgs_vev()
    
    # 5. Overall mass scale
    M_theta = Y_0 * v_eff
    
    return M_theta
```

**Requirements:**
- Derive Λ_H_C from biquaternion geometry
- Connect to same normalization used for N_eff, R_ψ
- Prove no free parameters introduced

**Option B: Topological Constraint**

```python
def compute_M_theta_topological():
    """
    Use topological invariants (Hopfion winding) to fix scale.
    """
    # Based on winding number and geometric radius
    pass
```

**Expected outcome:**
- M_Θ ~ O(100 GeV) from geometry
- Links to same geometric structure as α
- No fitted parameters

**Difficulty:** HIGH (requires new theoretical work)  
**Time estimate:** 3-4 months

### Task 2.2: Compute Yukawa Texture Coefficients

**Goal:** Calculate a₁, a₂, a₃ from Θ-field geometry

**Implementation:**
```python
def compute_yukawa_texture_electron():
    """
    Compute electron Yukawa coupling from Θ-field invariants.
    
    Based on: Y_e[Θ, ∇Θ, R(Θ)]
    """
    # 1. Set up Θ-field on Hermitian slice
    theta_field = initialize_theta_field_HC()
    
    # 2. Compute invariants
    inv1 = theta_field.scalar_invariant()
    inv2 = theta_field.gradient_invariant()
    inv3 = theta_field.curvature_invariant()
    
    # 3. Form Yukawa operator
    Y_e = a1 * inv1 + a2 * inv2 + a3 * inv3
    
    # 4. Coefficients from action minimization
    a1, a2, a3 = minimize_theta_action()
    
    return Y_e
```

**Expected outcome:**
- Y_e (dimensionless) ~ O(10⁻⁶) for electron
- Ratios Y_μ/Y_e, Y_τ/Y_e from texture
- Match experimental mass ratios

**Difficulty:** VERY HIGH  
**Time estimate:** 2-4 months

### Task 2.3: Implement Full Mass Calculation

**Goal:** Replace hardcoded m_e = 0.51099895 with calculation

```python
def compute_electron_mass_from_UBT():
    """
    Complete first-principles electron mass calculation.
    """
    # 1. Absolute scale
    M_theta = compute_absolute_scale_M_theta()
    
    # 2. Yukawa texture
    Y_e = compute_yukawa_texture_electron()
    
    # 3. Tree-level mass
    m_e_tree = M_theta * Y_e
    
    # 4. RG evolution (using already-derived α)
    alpha_func = lambda mu: alpha_from_geometric_B(B=8*pi, mu=mu)
    m_e_msbar = RG_evolve(m_e_tree, alpha_func, mu_from=M_theta, mu_to=m_e_tree)
    
    # 5. MSbar → Pole conversion (this already works)
    from ubt_masses.qed import pole_from_msbar_lepton
    alpha_e = alpha_func(m_e_msbar)
    m_e_pole = pole_from_msbar_lepton(m_e_msbar, m_e_msbar, alpha_e)
    
    return m_e_pole
```

**Expected outcome:**
```python
m_e_calc = compute_electron_mass_from_UBT()
# m_e_calc ≈ 0.510999 MeV (from first principles)
# Compare with experiment: 0.51099895 MeV
# Difference < 0.01% validates theory
```

**Validation:**
- Match experimental value within error budget
- No fitted parameters
- Acyclic dependencies (verified in Appendix E2)

**Difficulty:** VERY HIGH  
**Time estimate:** 1-2 months (after tasks 2.1, 2.2 complete)

## Phase 3: Extend to Muon and Tau (2-3 months)

### Task 3.1: Implement Same Framework

```python
def compute_muon_mass_from_UBT():
    M_theta = compute_absolute_scale_M_theta()  # Same as electron
    Y_mu = compute_yukawa_texture_muon()  # Different texture
    return M_theta * Y_mu  # + RG evolution
```

**Expected outcome:**
- m_μ ≈ 105.658 MeV from first principles
- Mass ratio m_μ/m_e ≈ 207 from texture (not fitted)

### Task 3.2: Implement Tau

```python
def compute_tau_mass_from_UBT():
    M_theta = compute_absolute_scale_M_theta()  # Same
    Y_tau = compute_yukawa_texture_tau()  # Different texture
    return M_theta * Y_tau  # + RG evolution
```

**Expected outcome:**
- m_τ ≈ 1776.86 MeV from first principles
- All three leptons from unified framework

## Timeline Summary

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| 1.1 Two-loop integrals | 2-3 months | α from calculation |
| 1.2 Pipeline function | 1-2 months | B → α⁻¹ derivation |
| 1.3 Documentation | 2 weeks | Updated claims |
| 2.1 Absolute scale | 3-4 months | M_Θ determined |
| 2.2 Yukawa texture | 2-4 months | Y_e calculated |
| 2.3 Electron mass | 1-2 months | m_e from UBT |
| 3.1-3.2 Muon/Tau | 2-3 months | Complete leptons |
| **TOTAL** | **12-18 months** | **Full first-principles UBT** |

## Resources Required

### Personnel:
- 1 theoretical physicist (QFT, 2-loop calculations)
- 1 numerical physicist (high-precision integration)
- 1 programmer (Python, symbolic math)
- Part-time: geometry/topology expert for M_Θ

### Software:
- SymPy (free)
- mpmath (free)
- Optional: Mathematica or FORM for cross-validation
- Optional: pySecDec or FIESTA for automation

### Literature:
- QED two-loop calculations (Jegerlehner 2017)
- Master integral techniques (Tarasov 1997)
- Dimensional regularization (Collins 1984)
- Complex time field theory (custom, develop as needed)

## Success Criteria

### Alpha:
- [ ] `compute_delta_ct(137)` returns value from calculation
- [ ] Matches experiment: |calc - 0.035999| < 1e-4
- [ ] No hardcoded experimental values
- [ ] All validation tests pass
- [ ] Peer-reviewed publication possible

### Electron Mass:
- [ ] `compute_electron_mass_from_UBT()` returns value from calculation
- [ ] Matches experiment: |calc - 0.51099895| < 0.0001 MeV
- [ ] M_Θ derived from geometry (no free parameters)
- [ ] Yukawa coefficients from first principles
- [ ] Peer-reviewed publication possible

### Overall UBT Credibility:
- [ ] Can claim "fit-free first-principles derivation" honestly
- [ ] Experimental values used for validation, not input
- [ ] Clear documentation of theory vs. code status
- [ ] Academic community acceptance

## Alternative: Document Current State Honestly

**If full implementation is not feasible:**

1. **Update all documentation** to say:
   - "Experimental calibration" (current)
   - "Theoretical framework complete"
   - "Numerical implementation in progress"

2. **Keep current code** but label clearly:
   ```python
   # TEMPORARY: Experimental calibration
   # TODO: Replace with first-principles calculation
   delta_ct = 0.035999000  # CODATA 2022 target
   ```

3. **Maintain scientific integrity:**
   - Don't claim "fit-free" until actually implemented
   - Be transparent about gaps
   - Focus on theoretical framework completeness

**This is acceptable IF properly documented.**

## Conclusion

UBT CAN derive α and m_e from first principles - the theoretical framework exists and is rigorous. The gap is COMPUTATIONAL, not THEORETICAL.

**Recommendation:** Prioritize Phase 1 (alpha) as it's more straightforward and would validate the UBT approach.

**Critical:** Update documentation NOW to reflect current state honestly, then implement calculations to match the theory.
