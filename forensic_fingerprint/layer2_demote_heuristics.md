# Layer-2 Heuristics Demoted: Mapping to Layer-0 Invariants

**Document ID**: Deliverable D  
**Date**: February 16, 2026  
**Purpose**: Classify Layer-2 computational procedures as either derived from Layer-0/1 invariants or explicitly labeled as heuristic/engineering choices

---

## Executive Summary

This document provides a comprehensive mapping from Layer-2 discretization procedures (prime-gating, n=137 calibration, RS coding, window choices) to the fundamental Layer-0/1 invariants established in Deliverables A (Dirac operator), B (quantization), and C (RG flow). 

**Key Finding**: Layer-2 introduces **6 additional engineering/heuristic choices** beyond what can be derived from Layer-0 topology and symmetry. We classify each choice, provide mapping equations with error estimates, and outline a plan to either derive or eliminate each heuristic.

---

## 1. Mapping Diagram: Layer-2 → Layer-0 Invariants

```
┌─────────────────────────────────────────────────────────────────┐
│                        LAYER 0/1                                │
│                   (Fundamental Physics)                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  [A] Dirac Operator D = iγ^μ∇_μ                               │
│      → Spectral Invariant: I_spec = Tr[f(D²/Λ²)]              │
│                                                                 │
│  [B] Quantization Conditions                                    │
│      → Phase winding: n_ψ ∈ Z (from π₁(U(1)))                 │
│      → Holonomy: n_hol ∈ Z (from Dirac quantization)          │
│      → Chern class: c₁ ∈ Z (from bundle topology)             │
│                                                                 │
│  [C] RG Flow                                                    │
│      → β-functions: β_κ, β_g, β_λ                              │
│      → Scale dependence: α(μ), H(z)                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                          ↓ ↓ ↓
                    (mapping equations)
                          ↓ ↓ ↓
┌─────────────────────────────────────────────────────────────────┐
│                        LAYER 2                                  │
│              (Discretization & Estimation)                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  [L2.1] Prime-gated scan: n ∈ {2,3,5,7,...,137,...}           │
│         Status: HEURISTIC (not derived from topology)           │
│                                                                 │
│  [L2.2] Calibration n=137 to match α⁻¹                        │
│         Status: EMPIRICAL FIT (not unique minimum)              │
│                                                                 │
│  [L2.3] RS(255,201) error-correcting code                      │
│         Status: ENGINEERING (optimal for GF(2⁸), not derived)   │
│                                                                 │
│  [L2.4] 16 OFDM channels                                        │
│         Status: DESIGN CHOICE (not uniquely determined)         │
│                                                                 │
│  [L2.5] Discretization grid (256 states)                        │
│         Status: COMPUTATIONAL (finite resolution)               │
│                                                                 │
│  [L2.6] Window functions for CMB scans                          │
│         Status: SIGNAL PROCESSING (standard practice)           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Explicit Mapping Equations

### 2.1 Spectral Invariant ↔ Layer-2 Metrics

**Layer-0 Definition** (Deliverable A):
```
I_spec[Θ] = Tr[f(D²/Λ²)]
```

**Layer-2 Estimator**:
```
Î_spec ≈ Σ_n f(λ_n/Λ²) × w_n
```
where:
- `λ_n` are eigenvalues of D² (estimated numerically)
- `w_n` are weights (currently: 1 if n prime, 0 otherwise — **HEURISTIC**)
- Discretization: continuous spectrum → finite sample

**Error Decomposition**:
```
I_spec - Î_spec = δ_disc + δ_finite + δ_prime
```
where:
- `δ_disc` = discretization error (from finite grid)
- `δ_finite` = finite-sample error (incomplete spectrum)
- `δ_prime` = prime-gating bias (**UNQUANTIFIED**)

**Mapping Table**:

| Layer-0 Quantity | Layer-2 Estimator | Error Term | Status |
|-----------------|------------------|-----------|---------|
| I_spec[Θ] | Σ f(λ_n/Λ²) | δ_disc + δ_finite | Controlled |
| Prime restriction | w_n = δ_{n∈P} | δ_prime | **Heuristic** |
| Test function f | f(x) = e^(-x) | Choice-dependent | Assumed |

### 2.2 Winding Number ↔ n=137

**Layer-0 Derivation** (Deliverable B):
```
n_ψ ∈ Z  (from π₁(U(1)))
Allowed: {..., -1, 0, 1, 2, ..., 137, ..., 199, ...}
```

**Layer-2 Selection**:
```
n_ψ = 137  (calibrated to match α⁻¹ ≈ 137.036)
```

**Mapping Equation**:
```
n_ψ = argmin_{n∈P} |α⁻¹(n) - 137.036|
```
where:
- P = primes (**HEURISTIC RESTRICTION**)
- α⁻¹(n) = computed fine-structure constant for winding n

**Derivability**:
- **Derived**: n_ψ ∈ Z (topological quantization)
- **NOT Derived**: n_ψ ∈ P (prime restriction)
- **NOT Derived**: n_ψ = 137 (empirical match)

**Alternative Hypothesis**:
If energy minimization selected n, we'd expect:
```
n_ψ = argmin_{n∈Z} E[n]
E[n] = n²/R_ψ² + V_eff(n)
```
Current analysis: E[0] < E[1] < E[137] ⇒ 137 is **not** energy minimum.

### 2.3 RG Scale ↔ Hubble Tension

**Layer-0 Prediction** (Deliverable C):
```
ΔH₀/H₀ = κ · R_ψ · Λ_RG / M_Pl
```

**Layer-2 Measurement**:
```
ΔH₀/H₀ ≈ 0.08 ± 0.01  (from Planck vs SH0ES)
```

**Fitting**:
```
κ, R_ψ, Λ_RG adjusted to match 0.08
```

**Parameter Count**:
- **Fitted**: κ, R_ψ, Λ_RG (3 parameters)
- **Derived**: Functional form ΔH₀ ∝ R_ψ Λ_RG
- **Fixed**: H₀ ≈ 70 km/s/Mpc (observed)

---

## 3. Comprehensive Classification Table

| ID | Layer-2 Element | Derived from Layer-0? | If Heuristic: Derivation Plan | If Unknown: Research Path |
|----|----------------|----------------------|------------------------------|---------------------------|
| **L2.1** | Prime-gating (n ∈ P) | ❌ **HEURISTIC** | • Investigate stability functional V_eff(n)<br>• Search for anomaly cancellation at primes<br>• Explore representation theory links | • Perform stability sweep n ∈ [1,300]<br>• Check if primes are local minima<br>• Test alternative factorizations |
| **L2.2** | n = 137 calibration | ❌ **EMPIRICAL FIT** | • Derive from RG fixed point?<br>• Connection to SM anomaly cancellation?<br>• Uniqueness theorem? | • Scan RG flow landscape<br>• Check if 137 is UV/IR fixed point<br>• Numerical minimization of action |
| **L2.3** | RS(255,201) code | ❌ **ENGINEERING** | • Derive (255,201) from Hilbert space dimensions<br>• Connect to GF(2⁸) from biquaternionic structure | • Prove GF(2⁸) from B ⊗ H ⊗ G<br>• Show RS is unique MDS code for given params |
| **L2.4** | 16 OFDM channels | ❌ **DESIGN CHOICE** | • Derive 16 from biquaternion components?<br>• Connection to 2⁴ subgroup structure? | • Count independent components of Θ<br>• Check if 16 = dim(representation) |
| **L2.5** | 256-state grid | ✓ **PARTIALLY DERIVED** | • Convergence proof: lim_{N→∞} grid → continuum | • Numerical convergence tests<br>• Compare 128, 256, 512 grids |
| **L2.6** | Window functions | ✓ **STANDARD PRACTICE** | • N/A (signal processing, not physics) | • Document choices for reproducibility |

**Legend**:
- ✓ Derived/Standard
- ❌ Heuristic/Engineering

---

## 4. Error Budget and Estimator Quality

### 4.1 Discretization Error (δ_disc)

**Source**: Finite grid resolution (N_grid = 256)

**Estimate**:
```
δ_disc ~ O(Λ²/N_grid²) ~ (M_Pl²/256²) ~ 10⁻⁴ M_Pl²
```

**Control**: Convergence test with N_grid ∈ {128, 256, 512}

**Status**: **QUANTIFIABLE** (can be reduced by refining grid)

### 4.2 Finite-Sample Error (δ_finite)

**Source**: Incomplete eigenvalue spectrum (only compute first K eigenvalues)

**Estimate**:
```
δ_finite ~ Σ_{n>K} f(λ_n/Λ²) ~ e^(-λ_K/Λ²)
```
For exponential cutoff `f(x) = e^(-x)`.

**Control**: Increase K until convergence

**Status**: **QUANTIFIABLE** (exponentially suppressed for large K)

### 4.3 Prime-Gating Bias (δ_prime)

**Source**: Restricting sum to prime indices

**Estimate**:
```
δ_prime = Σ_{n∈Z\P} f(λ_n/Λ²) × [signal at composite n]
```

**Current Status**: **UNQUANTIFIED** (no proof that composite n contributions vanish)

**Mitigation Path**:
1. Compute I_spec for all n ∈ [1,300]
2. Compare prime-gated vs full sum
3. If |δ_prime| << δ_disc, justify as negligible
4. If |δ_prime| ~ O(1), prime-gating is non-physical

---

## 5. Reproducibility Checklist

To ensure Layer-2 results are reproducible and not artifacts of specific choices:

### 5.1 Seed Control

- [ ] **Random number seeds**: Document all RNG seeds used in Monte Carlo scans
- [ ] **Initial conditions**: Specify Θ(q,τ,t=0) for evolution runs
- [ ] **Grid initialization**: Document mesh construction (uniform vs adaptive)

### 5.2 Sweep Specifications

- [ ] **Parameter ranges**: n ∈ [n_min, n_max], stride, logarithmic vs linear
- [ ] **Convergence criteria**: ε_tol for iterative solvers
- [ ] **Timeout limits**: Maximum wall-clock time for each scan point

### 5.3 Reporting Standards

- [ ] **Error bars**: Propagate δ_disc + δ_finite to all reported quantities
- [ ] **Negative results**: Report when scans find no signal (pre-registration)
- [ ] **Outlier handling**: Document how anomalous points are treated
- [ ] **Version control**: Tag code version used for each published result

### 5.4 Pre-Registration

For falsification-sensitive tests:
- [ ] Register hypothesis before running scan (e.g., "expect peak at n=137")
- [ ] Commit to analysis pipeline before seeing data
- [ ] Public time-stamped deposit (e.g., arXiv, OSF)

**Reference**: See `forensic_fingerprint/pre_registration/` for templates

---

## 6. Plan to Remove or Derive Each Heuristic

### 6.1 Prime-Gating (L2.1)

**Current Status**: Heuristic selection

**Derivation Path A** (Stability):
1. Compute effective potential V_eff(n) for n ∈ [1, 300]
2. Check if V_eff(n) has local minima at primes
3. If yes: Prove stability of prime-winding solitons
4. If no: Abandon prime restriction, use full Z

**Derivation Path B** (Representation Theory):
1. Identify automorphism group G_aut of biquaternionic action
2. Classify irreducible representations
3. Check if irreps are indexed by primes
4. If yes: Prime-gating is representation-theoretic
5. If no: Prime-gating remains heuristic

**Timeline**: 
- Path A: 2-4 weeks (numerical scan)
- Path B: 2-6 months (mathematical analysis)

**Decision Criterion**:
- If neither path succeeds by [DATE], explicitly label prime-gating as **phenomenological ansatz** in publications

### 6.2 Calibration n=137 (L2.2)

**Current Status**: Empirical fit to α⁻¹

**Derivation Path A** (RG Fixed Point):
1. Solve β-function equations β_κ(κ,n) = 0
2. Check if solutions occur at discrete n values
3. If yes: Check if n=137 is among fixed points
4. If no: n=137 remains empirical calibration

**Derivation Path B** (Anomaly Cancellation):
1. Compute quantum anomalies (chiral, gravitational, mixed)
2. Impose anomaly-free condition
3. If condition restricts n to discrete set containing 137: Derived
4. If not: n=137 remains empirical

**Timeline**:
- Path A: 1-2 months (perturbative RG)
- Path B: 3-6 months (anomaly computation)

**Fallback**: If not derivable, clearly state: "n=137 is calibrated to match observed α⁻¹, not predicted a priori"

### 6.3 RS(255,201) Code (L2.3)

**Current Status**: Engineering choice (optimal MDS code for GF(2⁸))

**Derivation Path**:
1. Prove GF(2⁸) structure from B ⊗ H decomposition
2. Show (255,201) emerges from Hilbert space dimensions
3. Derive from information capacity of phase sector?

**Challenge**: Current formulation has no obvious link between coding theory and field theory

**Timeline**: 4-12 months (requires new theoretical development)

**Fallback**: Rename as "RS-optimal lens" (not fundamental ontology)

### 6.4 16 OFDM Channels (L2.4)

**Derivation Path**:
1. Count independent real components of Θ ∈ B ⊗ S ⊗ G
2. If count = 16: Derived from representation
3. If count ≠ 16: Remains design choice

**Quick Check**:
- B = C ⊗ H: 8 real dimensions
- S (Dirac spinor): 4 complex = 8 real
- G (gauge): varies by representation
- Total: Depends on specific representation chosen

**Timeline**: 1 week (combinatorics)

### 6.5 Grid Resolution (L2.5)

**Status**: Computational (not physics)

**No derivation needed**: This is a numerical convergence parameter

**Action**: Perform convergence tests, document in methods section

---

## 7. Relationship to Existing Documentation

This document integrates with:

- **FORMAL_INVARIANT_EXTRACTION_LAYER0.tex**: Provides rigorous invariant definitions
- **LAYER0_INVARIANT_EXTRACTION_README.md**: Executive summary of invariant analysis
- **Deliverable A** (ubt/operators/dirac_like_operator.tex): Defines I_spec
- **Deliverable B** (ubt/quantization/winding_quantization.tex): Derives n_ψ ∈ Z
- **Deliverable C** (ubt/phenomenology/rg_flow_and_scales.tex): Connects to RG scale

**Cross-References**:
- L2.1 (prime-gating) → Deliverable B, Theorem 4.1 (primes not derived)
- L2.2 (n=137) → Deliverable B, Section 5 (empirical calibration)
- L2.3 (RS codes) → Existing: information_probes/RS_OPTIMAL_LENS.md
- Layer-2 stability → forensic_fingerprint/protocols/PROTOCOL_LAYER2_RIGIDITY.md

---

## 8. Summary

### What Layer-2 Provides

Layer-2 is a **numerical estimator** of Layer-0/1 invariants, not a source of additional physics. It provides:

1. **Finite-resolution approximation** to continuous field theory
2. **Computational efficiency** (discrete vs continuous)
3. **Signal processing tools** (window functions, error correction)

### What Layer-2 Does NOT Provide

Layer-2 does **NOT** introduce new fundamental physics. Specifically:

1. Prime restriction is **not topologically required**
2. n=137 is **not uniquely predicted**
3. RS(255,201) is **not geometrically necessary**

### Honest Communication

**Avoid**:
- ❌ "UBT derives α⁻¹=137 from pure geometry"
- ❌ "Prime-gating is topologically enforced"
- ❌ "RS codes are ontologically fundamental"

**Use**:
- ✓ "UBT predicts n_ψ ∈ Z; we calibrate n=137 to match α⁻¹"
- ✓ "Prime-gating is a heuristic scan strategy under investigation"
- ✓ "RS(255,201) provides an optimal information-theoretic lens"

---

## 9. Acceptance Criteria Verification

✅ **Mapping equations**: Section 2 provides I_est ≈ I + δ_disc + δ_finite + δ_prime

✅ **Classification table**: Section 3 categorizes each Layer-2 choice as derived/heuristic/unknown

✅ **Derivation plan**: Section 6 outlines specific paths to derive or eliminate each heuristic

✅ **Reproducibility checklist**: Section 5 specifies seed control, sweep specs, reporting standards

---

## References

1. Deliverable A: `ubt/operators/dirac_like_operator.tex`
2. Deliverable B: `ubt/quantization/winding_quantization.tex`
3. Deliverable C: `ubt/phenomenology/rg_flow_and_scales.tex`
4. Layer-0 Invariant Extraction: `FORMAL_INVARIANT_EXTRACTION_LAYER0.tex`
5. RS Optimal Lens Analysis: `information_probes/RS_OPTIMAL_LENS.md` (if exists)
6. Layer-2 Rigidity Protocol: `forensic_fingerprint/protocols/PROTOCOL_LAYER2_RIGIDITY.md`

---

**Document Version**: 1.0  
**Last Updated**: February 16, 2026  
**Maintainer**: UBT Theory Development  
**License**: CC BY-NC-ND 4.0 (theory), MIT (code)
