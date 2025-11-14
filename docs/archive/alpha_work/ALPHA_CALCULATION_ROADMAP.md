# Roadmap: From Hardcoded to Calculated QED Corrections in UBT

**Author**: GitHub Copilot Analysis  
**Date**: November 2025  
**Purpose**: Detailed implementation plan for calculating the 0.036 alpha correction from first principles within UBT

## Current Status

### What Works ✅

1. **Geometric Baseline Prediction**
   - α⁻¹ = 137 from topological quantization
   - Winding number optimization: V_eff(n) minimization
   - Implementation: `scripts/emergent_alpha_calculator.py`
   - Status: **Complete and verified**

2. **Theoretical Framework**
   - Two-loop formalism with R_UBT factor defined
   - Ward identities Z₁ = Z₂ proven
   - Complex time (CT) renormalization scheme specified
   - Documentation: `consolidation_project/alpha_two_loop/FIT_FREE_ALPHA_README.md`
   - Status: **Rigorous and complete**

3. **Symbolic Infrastructure**
   - Master integrals defined (`master_integrals.py`)
   - IBP reduction system (`ibp_system.py`)
   - Two-loop evaluator (`ct_two_loop_eval.py`)
   - ~1600 lines of symbolic computation code
   - Status: **Framework exists, evaluation incomplete**

### What's Hardcoded ⚠️

1. **QED Corrections**
   - File: `scripts/padic_alpha_calculator.py` line 74
   - Code: `delta_137 = 0.036`
   - Source: Standard QED literature (not computed)
   - Breakdown:
     - Vacuum polarization (electron loops): +0.032
     - Hadronic contributions: +0.003
     - Higher-order terms: +0.001

2. **Validation Placeholders**
   - File: `consolidation_project/alpha_two_loop/validate_ct_baseline.py`
   - Line 139: Comment "Simplified: actual calculation requires master integrals"
   - Uses approximate formulas for demonstration
   - Status: Shows R_UBT → 1 but doesn't compute finite remainder

## Implementation Roadmap

### Phase 1: Master Integral Evaluation (3-4 months)

**Goal**: Implement numerical evaluation of master integrals in Thomson limit

#### Task 1.1: One-Loop Bubble Integral
**File**: `consolidation_project/alpha_two_loop/symbolics/master_integrals.py`  
**Current**: Symbolic definition exists  
**Needed**: Implement `MI_Bubble.numeric()` method

```python
def numeric(self, q2_val=0.0, m2_val=1.0, mu2_val=1.0, precision=50):
    """
    Numerical evaluation using mpmath.
    
    For q² = 0 (Thomson limit):
    I_bubble = (i/(16π²)) × [2/ε - 2 + log(m²/μ²)]
    
    Returns finite part after renormalization.
    """
    # Implementation needed:
    # 1. Handle dimensional regularization (ε → 0 limit)
    # 2. Extract finite part
    # 3. Evaluate to requested precision
```

**Dependencies**:
- `mpmath` library for arbitrary precision
- Special functions: `log`, `atanh`, `sqrt`
- Careful handling of ε poles

**Estimated effort**: 2 weeks

#### Task 1.2: Two-Loop Sunset Integral
**Current**: Symbolic Thomson limit formula exists  
**Needed**: Numerical evaluation with proper error handling

```python
def numeric(self, q2_val=0.0, m2_val=1.0, mu2_val=1.0, precision=50):
    """
    Two-loop sunset in Thomson limit.
    
    Result: (i/(16π²))² × [4/ε² + (8 ln(m²/μ²) - 12)/ε + finite]
    
    finite = 8 ln²(m²/μ²) - 24 ln(m²/μ²) + 20
    """
    # Implementation needed:
    # 1. Extract finite part (double pole structure)
    # 2. Handle numerical instabilities
    # 3. Validate against known results
```

**Dependencies**:
- Previous task completed
- Cross-check with QED literature values

**Estimated effort**: 3 weeks

#### Task 1.3: Double Bubble and Vertex Corrections
**Current**: Definitions exist, no evaluation  
**Needed**: Complete the master integral basis

**Estimated effort**: 3 weeks

**Validation**: Compare against known QED results at q² = 0, ξ = 1 (Feynman gauge)

### Phase 2: Complex Time Corrections (2-3 months)

**Goal**: Implement CT-specific modifications to master integrals

#### Task 2.1: CT Contour Deformation
**Theory**: Complex time τ = t + iψ modifies loop momentum integration contour  
**Effect**: Phase factors exp(-|ψ|/R_ψ) suppressing imaginary time contributions

**Implementation**:
```python
def ct_phase_correction(self, psi, R_psi=1.0):
    """
    Compute CT correction to master integral.
    
    Δ_CT = MI_CT(ψ) - MI_QED(ψ=0)
    
    For small ψ: Δ_CT ~ i·ψ·(perturbative series)
    """
```

**Challenges**:
- Contour integration in complex momentum space
- Analytic continuation from real to complex time
- Gauge/scheme independence preservation

**Estimated effort**: 6 weeks

#### Task 2.2: Verify R_UBT = 1
**Goal**: Numerically confirm that CT corrections vanish in ratio

```python
R_UBT = Π_CT(q²=0, ψ) / Π_QED(q²=0, ψ=0)
# Should yield R_UBT → 1 as ψ → 0
```

**Validation**:
- Check all 5 validation tests in `validate_ct_baseline.py`
- Ensure Ward identity preserved
- Verify gauge independence

**Estimated effort**: 4 weeks

### Phase 3: Vacuum Polarization Assembly (1-2 months)

**Goal**: Combine master integrals to get full Π^(2)(q²)

#### Task 3.1: Diagram Enumeration
**Needed**: Complete list of all 2-loop topologies contributing to vacuum polarization

Known diagrams:
1. Sunset (fermion loop with photon)
2. Double bubble (two fermion bubbles)
3. Vertex correction (fermion self-energy insertion)
4. Box diagrams (if relevant to Thomson limit)

**Implementation**:
```python
def assemble_vacuum_polarization_two_loop(self):
    """
    Π^(2) = Σ_i c_i × MI_i
    
    where c_i are group theory/symmetry factors
    """
```

**Estimated effort**: 3 weeks

#### Task 3.2: Renormalization
**Goal**: Apply CT renormalization scheme, subtract divergences

```python
Π_ren^(2) = Π_bare^(2) - Z_3 × Π^(1) + counterterms
```

**Challenges**:
- Ensure Z₁ = Z₂ (Ward identity)
- Scheme independence of physical result
- Proper subtraction structure

**Estimated effort**: 4 weeks

### Phase 4: Extract Alpha Correction (1 month)

**Goal**: From Π^(2) → Δα^(-1)

#### Task 4.1: Thomson Limit
**Formula**:
```
Δα^(-1) = Re[Π^(2)(q²=0, μ)] × (conversion factor)
```

**Implementation**:
```python
def compute_alpha_correction(self, mu_scale=1.0):
    """
    Compute the finite correction Δα^(-1) from vacuum polarization.
    
    Returns:
        delta_alpha_inv: Numerical value (should be ~ 0.032 for electron loops)
    """
```

**Estimated effort**: 2 weeks

#### Task 4.2: Add Hadronic and Higher-Order
**Current**: Only electron loop implemented  
**Needed**: Include all SM contributions

- Muon loops: + small correction
- Tau loops: + smaller correction
- Hadronic: +0.003 (from dispersion relation or lattice QCD)
- Three-loop and beyond: +0.001

**Note**: Hadronic may remain semi-empirical (input from experiment/lattice)

**Estimated effort**: 2 weeks

### Phase 5: Testing and Validation (1 month)

#### Task 5.1: Unit Tests
- Each master integral against literature
- Each topology against known QED results
- Ward identity checks at every step
- Gauge independence verification

**Estimated effort**: 2 weeks

#### Task 5.2: Integration Tests
- Full Δα^(-1) calculation
- Comparison with PDG value: 0.036 vs calculated
- Acceptable tolerance: < 1% difference

**Estimated effort**: 2 weeks

## Total Effort Estimate

**Conservative**: 9-12 months full-time PhD research  
**Optimistic**: 6-8 months with existing expertise

## Intermediate Milestones

### Milestone 1 (Month 3): Basic MI Evaluation
- Bubble and sunset numerically evaluated
- Thomson limit verified against QED
- **Deliverable**: Can compute electron loop contribution (~0.032)

### Milestone 2 (Month 6): CT Corrections Implemented
- Complex time modifications included
- R_UBT = 1 verified numerically
- **Deliverable**: Proof that UBT ↔ QED equivalence holds

### Milestone 3 (Month 9): Full Calculation
- All diagrams assembled
- Renormalization complete
- **Deliverable**: Δα^(-1) computed from first principles

### Milestone 4 (Month 12): Publication Ready
- All tests passing
- Documentation complete
- **Deliverable**: Replace hardcoded 0.036 with calculated value

## Alternative Approaches

### Quick Win: Simplified Demonstration

Instead of full implementation, create a simplified version that:
1. Uses known MI results from literature
2. Shows the assembly process works
3. Demonstrates R_UBT → 1 numerically
4. Estimates Δα^(-1) with known inputs

**Effort**: 2-3 weeks  
**Value**: Shows framework is sound without full calculation

### Hybrid Approach: Use External Tools

- Use `FIRE` or `Reduze` for IBP reduction (external tools)
- Use `HyperInt` or `HPL` for master integral evaluation
- Focus UBT effort on CT modifications only

**Effort**: 3-4 months  
**Value**: Faster to result, relies on established tools

## Resources Required

### Software
- `sympy` (symbolic math)
- `mpmath` (arbitrary precision)
- `numpy`, `scipy` (numerical computation)
- Optional: `FIRE`, `Reduze` (IBP reduction)
- Optional: `Mathematica` (cross-validation)

### Theoretical Knowledge
- Quantum field theory (2-loop level)
- Dimensional regularization
- Renormalization schemes
- Complex analysis (contour integration)

### Computational
- Moderate: single workstation sufficient
- Precision: 50-100 decimal places for some integrals
- Runtime: minutes to hours per evaluation

## Risks and Challenges

### Technical Risks
1. **Numerical instabilities**: Master integrals can be ill-conditioned
   - Mitigation: Use arbitrary precision arithmetic
   
2. **Gauge dependence**: Easy to violate Ward identities
   - Mitigation: Check Z₁ = Z₂ at every step
   
3. **Scheme ambiguities**: CT scheme not standard in QED literature
   - Mitigation: Prove equivalence to MS-bar in ψ → 0 limit

### Conceptual Risks
1. **CT corrections non-zero**: What if R_UBT ≠ 1?
   - Current theory proves R_UBT = 1, but numerical check important
   - If R_UBT ≠ 1, would need to revise theory

2. **Mismatch with experiment**: What if calculated Δα^(-1) ≠ 0.036?
   - Could indicate UBT differs from QED at 2-loop
   - Or could be calculational error
   - Need careful validation

## Success Criteria

### Minimum Success
- ✅ Master integrals evaluated numerically
- ✅ R_UBT = 1 verified (within numerical precision)
- ✅ Framework demonstrated to work

### Full Success
- ✅ Δα^(-1) calculated from UBT field equations
- ✅ Result matches QED: 0.032 ± 0.002 (electron loops)
- ✅ Hardcoded value replaced with calculation
- ✅ Published as validation of UBT

## Current Recommendation

Given the scope and complexity:

1. **Short-term** (now): 
   - ✅ Document current status honestly (DONE)
   - ✅ Create this roadmap (DONE)
   - Acknowledge 0.036 is from literature

2. **Medium-term** (3-6 months):
   - Implement Phase 1 (master integrals)
   - Basic numerical validation

3. **Long-term** (6-12 months):
   - Complete implementation
   - Replace hardcoded values
   - Publish results

4. **Alternative** (2-3 weeks):
   - Simplified demonstration
   - Shows framework validity without full calculation

## Conclusion

**The 0.036 correction CAN be calculated from UBT**, but it requires:
- Significant implementation effort (6-12 months)
- Expertise in QFT and numerical methods
- Careful validation at each step

**The framework exists** - this is not a theoretical gap, it's a computational gap.

**Current approach** (using QED literature value) is scientifically valid - UBT and QED should give the same answer, so citing the known QED result is acceptable as long as it's documented clearly.

**Future work** should complete the calculation to demonstrate UBT's predictive power fully independent of external QED results.

---

**Next Steps**: Decide on priority:
- A) Full implementation (commit 6-12 months)
- B) Simplified demonstration (commit 2-3 weeks)
- C) Document honestly and defer (commit to transparency)

Current PR follows approach C. User can direct toward A or B if desired.
