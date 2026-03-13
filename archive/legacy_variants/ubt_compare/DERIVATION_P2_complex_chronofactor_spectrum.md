# Complex Chronofactor τ=t+iψ: Spectral Consequences and Links to S_Θ and Σ_Θ

**Author**: UBT Team  
**Date**: February 2026  
**License**: © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0

---

## Abstract

This document provides a rigorous symbolic derivation of how a complex chronofactor τ = t + iψ manifests in spectral properties of the biquaternionic field Θ(τ). We establish the formal mathematical connection between complex-time evolution and the UBT invariants S_Θ = k_B log det(Θ†Θ) (entropy channel) and Σ_Θ = k_B arg det Θ (phase channel). The analysis focuses on linear complex-time flow, eigenmode decomposition, and the emergence of testable discriminators that distinguish real-time evolution from complex-time dynamics.

**Key Results**:
- Complex τ couples growth/decay and oscillation at the eigenmode level
- Phase-entropy coupling emerges through Re/Im mixing in Tr G
- Three discriminators (D1-D3) provide testable signatures

---

## 1. Setup and Assumptions

### 1.1 The Biquaternionic Field

We work with a complex matrix field Θ(τ) where:
- **Θ**: n×n complex matrix field
- **τ = t + iψ**: Complex chronofactor (t = real time, ψ = imaginary/phase component)
- **q**: Spatial coordinates (suppressed when focusing on temporal evolution)

### 1.2 Fundamental Assumptions

**Assumption 1.1** (Regularity): Θ(τ) is holomorphic in a neighborhood of the real axis Im(τ) = 0 for physical time evolution.

**Assumption 1.2** (Positive-Definiteness on Real Slice): For real t with fixed ψ, the Hermitian product O(t) := Θ†(t+iψ) Θ(t+iψ) is positive semidefinite.

**Assumption 1.3** (Linear Flow): The evolution is governed by a time-independent generator G:

```
∂_τ Θ = G Θ
```

where G is a fixed n×n complex matrix (generally non-Hermitian).

### 1.3 UBT Invariants

The theory defines two primary channels:

**Entropy Channel**:
```
S_Θ(τ) = k_B log det(Θ†(τ) Θ(τ)) = 2k_B Re[log det Θ(τ)]
```

**Phase Channel**:
```
Σ_Θ(τ) = k_B arg det Θ(τ) = k_B Im[log det Θ(τ)]
```

where k_B is Boltzmann's constant (set to 1 in natural units for this derivation).

---

## 2. Linear Complex-τ Flow: ∂_τ Θ = G Θ

### 2.1 Formal Solution

The linear flow equation has the formal solution:

**Proposition 2.1** (Exponential Flow):
```
Θ(τ) = exp(τG) Θ_0
```

where Θ_0 = Θ(0) is the initial condition and exp(τG) is the matrix exponential.

### 2.2 Decomposition of Generator

Write the generator G in terms of its real and imaginary parts:

```
G = A + iB
```

where A = Re(G) and B = Im(G) are real n×n matrices.

**Lemma 2.2** (Complex-Time Substitution):

Substituting τ = t + iψ:

```
τG = (t + iψ)(A + iB) = (tA - ψB) + i(tB + ψA)
```

This shows that complex time τ couples the real and imaginary parts of G in a non-trivial way:
- Real part of τG: tA - ψB (combines real-time evolution with imaginary generator)
- Imaginary part of τG: tB + ψA (combines imaginary-time evolution with real generator)

### 2.3 Commutator Analysis

**Theorem 2.3** (Decomposition Conditions):

The matrix exponential simplifies if and only if [A, B] = 0:

**Case 1** (Commuting): If [A, B] = 0, then:
```
exp(τG) = exp(tA - ψB) exp(i(tB + ψA))
```

**Case 2** (Non-Commuting): If [A, B] ≠ 0, use the Baker-Campbell-Hausdorff (BCH) formula:

```
exp(τG) = exp(tA - ψB) exp(i(tB + ψA)) exp(C_BCH)
```

where to first order:
```
C_BCH ≈ (1/2)[tA - ψB, i(tB + ψA)] + O([[[A,B],A],B])
```

Expanding the commutator explicitly:
```
[tA - ψB, i(tB + ψA)] = i[tA - ψB, tB + ψA]
                       = i(t²[A,B] + tψ[A,A] - tψ[B,B] - ψ²[B,A])
```

Using the identities [A,A] = 0, [B,B] = 0, and [B,A] = -[A,B]:
```
[tA - ψB, i(tB + ψA)] = i(t²[A,B] + 0 - 0 - ψ²(-[A,B]))
                       = i(t²[A,B] + ψ²[A,B])
                       = i(t² + ψ²)[A,B]
```

Therefore:
```
C_BCH ≈ (i/2)(t² + ψ²)[A,B] + O([[[A,B],A],B])
```

**Physical Interpretation**: Non-commutativity introduces additional phase factors that depend on both t and ψ quadratically, with the phase correction growing as (t² + ψ²). For small ψ, the correction is order O(ψ²). The positive sign indicates that both real and imaginary time components contribute additively to the non-commutative phase.

**Remark on Higher-Order Terms**: The BCH formula contains higher-order nested commutators such as [[A,B],A] and [[A,B],B]. The leading first-order approximation is valid when ||A||, ||B|| are small or over short complex time intervals where ||τG|| << 1.

---

## 3. Solution Θ(τ) = exp(τG)Θ_0 and Spectral Decomposition of G

### 3.1 Eigendecomposition

Assume G is diagonalizable (extensions to Jordan blocks follow standard matrix theory):

```
G v_k = μ_k v_k,    k = 1, ..., n
```

where:
- **μ_k = α_k + iω_k**: Complex eigenvalues (α_k, ω_k ∈ ℝ)
- **v_k**: Right eigenvectors
- **w_k**: Left eigenvectors (bi-orthogonal: w_k† v_j = δ_kj)

### 3.2 Spectral Representation

**Proposition 3.1** (Spectral Expansion):

```
Θ(τ) = exp(τG) Θ_0 = Σ_k exp(τ μ_k) v_k w_k† Θ_0
```

Each eigenmode k evolves independently with amplitude factor exp(τ μ_k).

### 3.3 Eigenvalue Structure

**Lemma 3.2** (Reality Conditions):

If G is real (B = 0), complex eigenvalues appear in conjugate pairs:
```
μ_k = α_k ± iω_k
```

If G is complex non-Hermitian, eigenvalues can be arbitrary complex numbers.

---

## 4. What Changes When τ is Complex: Growth/Decay + Oscillation (Re/Im Split)

### 4.1 Single Eigenmode Evolution

Consider a single eigenmode with eigenvalue μ = α + iω:

```
exp(τμ) = exp((t + iψ)(α + iω))
        = exp((tα - ψω) + i(tω + ψα))
        = exp(tα - ψω) · exp(i(tω + ψα))
```

**Theorem 4.1** (Mode Amplitude Factor):

The mode amplitude factor decomposes as:

```
|exp(τμ)| = exp(tα - ψω)
arg(exp(τμ)) = tω + ψα
```

**Physical Interpretation**:

1. **Growth/Decay** (Amplitude): |exp(τμ)| = exp(tα - ψω)
   - Real time t couples to Re(μ) = α (standard exponential growth/decay)
   - Imaginary time ψ couples to Im(μ) = ω (modulates amplitude!)
   - A non-zero ψ can turn decay into growth (if ω < 0) or vice versa

2. **Oscillation** (Phase): arg(exp(τμ)) = tω + ψα
   - Real time t couples to Im(μ) = ω (standard oscillation)
   - Imaginary time ψ couples to Re(μ) = α (phase shift!)
   - Growth rate α now contributes to phase accumulation

### 4.2 Key Observation: Cross-Coupling

**Corollary 4.2** (Cross-Coupling Principle):

Complex time τ introduces a fundamental cross-coupling:
- What is "growth" in real time becomes "oscillation" in imaginary time
- What is "oscillation" in real time becomes "growth" in imaginary time

This is the spectral signature of complex chronofactor evolution.

### 4.3 Spectral Broadening

**Proposition 4.3** (Spectral Shift):

For small imaginary time ψ, the effective eigenvalues shift:

```
μ_eff(ψ) ≈ α + iω - ψ(iα + ω) = (α + ψω) + i(ω - ψα)
```

The real part shifts by +ψω (imaginary eigenvalue component).
The imaginary part shifts by -ψα (real eigenvalue component).

**Consequence**: Even if ψ is constant, complex τ causes:
1. Spectral broadening: eigenvalues redistribute
2. Mode mixing: growth rates and frequencies correlate
3. Non-monotonic dynamics: modes can exhibit transient growth

---

## 5. Consequences for O(τ) = Θ†Θ on Real-Time Slice

### 5.1 Evolution Equation for O

Define the observable matrix:
```
O(t, ψ) := Θ†(t + iψ) Θ(t + iψ)
```

**Theorem 5.1** (Real-Time Evolution of O):

Taking ∂_t derivative with ψ fixed:

```
∂_t O = ∂_t(Θ†Θ) = (∂_t Θ†)Θ + Θ†(∂_t Θ)
```

Using ∂_τ Θ = GΘ and ∂_τ Θ† = Θ†G† (chain rule with τ = t + iψ):

```
∂_t Θ = ∂_τ Θ · ∂_t τ = GΘ
∂_t Θ† = (∂_τ Θ†) · ∂_t τ = Θ†G†
```

Therefore:
```
∂_t O = Θ†G†Θ + Θ†GΘ = Θ†(G† + G)Θ
```

Define the Hermitian part of G:
```
Herm(G) := (G + G†)/2
```

Then:
```
∂_t O = 2Θ†Herm(G)Θ
```

**Corollary 5.2** (Conservation Condition):

If Herm(G) = 0 (i.e., G is anti-Hermitian), then ∂_t O = 0 and O is conserved on the real-time slice.

**Physical Interpretation**: Anti-Hermitian generators preserve the norm. This is the spectral manifestation of unitary evolution.

### 5.2 Imaginary-Time Dependence

If ψ varies with t, i.e., ψ = ψ(t), then:

```
dO/dt = ∂_t O + (∂_ψ O)(dψ/dt)
```

Computing ∂_ψ O:
```
∂_ψ Θ = i∂_τ Θ = iGΘ
∂_ψ Θ† = -iΘ†G†
```

Thus:
```
∂_ψ O = -iΘ†G†Θ + iΘ†GΘ = iΘ†(G - G†)Θ
```

Define the anti-Hermitian part:
```
AntiHerm(G) := (G - G†)/(2i)
```

Then:
```
∂_ψ O = 2iΘ†AntiHerm(G)Θ
```

**Theorem 5.3** (Full Time Derivative with Variable ψ):

```
dO/dt = 2Θ†[Herm(G) + i(dψ/dt)AntiHerm(G)]Θ
```

**Physical Consequence**: If ψ(t) varies, the effective generator becomes:
```
G_eff = Herm(G) + i(dψ/dt)AntiHerm(G)
```

This can cause spectral broadening even if G itself is anti-Hermitian!

---

## 6. Determinant Channel: log det Θ and log det(Θ†Θ)

### 6.1 Determinant Evolution

**Theorem 6.1** (Determinant Identity for Linear Flow):

For linear flow ∂_τ Θ = GΘ:

```
det Θ(τ) = det(exp(τG)) det Θ_0 = exp(τ Tr G) det Θ_0
```

Taking logarithm:
```
log det Θ(τ) = τ Tr G + log det Θ_0
```

**Proof**: This follows from det(exp(M)) = exp(Tr M) for any matrix M.

### 6.2 Real and Imaginary Parts

Substituting τ = t + iψ:

```
log det Θ(τ) = (t + iψ) Tr G + log det Θ_0
                = t Tr G + iψ Tr G + log det Θ_0
```

Write Tr G = Tr(A + iB) = Tr A + i Tr B:

```
log det Θ(τ) = t(Tr A + i Tr B) + iψ(Tr A + i Tr B) + log det Θ_0
                = (t Tr A - ψ Tr B) + i(t Tr B + ψ Tr A) + log det Θ_0
```

**Proposition 6.2** (Re/Im Decomposition):

```
Re[log det Θ(τ)] = t Tr A - ψ Tr B + Re[log det Θ_0]
Im[log det Θ(τ)] = t Tr B + ψ Tr A + Im[log det Θ_0]
```

### 6.3 Connection to S_Θ and Σ_Θ

**Theorem 6.3** (UBT Invariant Expressions):

**Entropy Channel**:
```
S_Θ(t, ψ) = k_B log det(Θ†Θ) = 2k_B Re[log det Θ]
           = 2k_B(t Tr A - ψ Tr B + Re[log det Θ_0])
```

**Phase Channel**:
```
Σ_Θ(t, ψ) = k_B Im[log det Θ]
           = k_B(t Tr B + ψ Tr A + Im[log det Θ_0])
```

**Key Observation**: The cross-coupling appears explicitly:
- S_Θ: Real time couples to Tr A, imaginary time couples to Tr B
- Σ_Θ: Real time couples to Tr B, imaginary time couples to Tr A

This is the determinant-level manifestation of the eigenmode cross-coupling from Section 4.

### 6.4 Time Derivatives

**Corollary 6.4** (Evolution Rates):

```
∂_t S_Θ = 2k_B Tr A
∂_ψ S_Θ = -2k_B Tr B

∂_t Σ_Θ = k_B Tr B
∂_ψ Σ_Θ = k_B Tr A
```

**Physical Interpretation**: 
- Tr A controls entropy growth and phase precession rate (with ψ)
- Tr B controls phase precession and entropy reduction (with ψ)

---

## 7. Phase Channel: arg det Θ as Holonomy / Winding Under Im(τ)

### 7.1 Geometric Interpretation

The phase channel Σ_Θ = k_B arg det Θ can be interpreted as a holonomy or winding number in the complex-τ plane.

**Definition 7.1** (Phase Holonomy):

For a closed loop γ in the complex-τ plane:
```
ΔΣ_Θ[γ] = k_B ∮_γ dτ Tr(Θ^{-1} ∂_τ Θ) = k_B ∮_γ dτ Tr G
```

For linear flow, this simplifies to:
```
ΔΣ_Θ[γ] = k_B (Tr G) ∮_γ dτ
```

**Proposition 7.2** (Imaginary-Time Winding):

Consider a loop in the ψ-direction at fixed t: ψ ∈ [0, Δψ]:
```
ΔΣ_Θ = k_B (Tr G) · (iΔψ) = ik_B Δψ Tr G = ik_B Δψ (Tr A + i Tr B)
      = -k_B Δψ Tr B + ik_B Δψ Tr A
```

The real winding is:
```
Re[ΔΣ_Θ] = -k_B Δψ Tr B
```

**Physical Meaning**: The phase accumulation under imaginary-time translation is controlled by Tr B, the imaginary part of the generator trace.

### 7.2 Berry Phase Connection

**Remark 7.3**: This structure is analogous to Berry phase in quantum mechanics, where:
- Berry phase: γ_B = i∮⟨ψ|∇_λ|ψ⟩·dλ
- UBT phase: Σ_Θ = ∮ Tr(Θ^{-1} ∂_τ Θ) dτ

The imaginary time ψ acts as an adiabatic parameter, and Tr G plays the role of the Berry connection.

---

## 8. Non-Hermitian Case: Complex Eigenvalues, Bi-Orthogonal Modes, Pseudospectrum

### 8.1 Non-Normal Matrices

**Definition 8.1** (Non-Normality):

A matrix G is **normal** if [G, G†] = 0. For non-normal G:
- Eigenvalues can be highly sensitive to perturbations
- Eigenvectors are not orthogonal
- Transient growth can occur even if all Re(μ_k) < 0

### 8.2 Bi-Orthogonal Modes

For non-Hermitian G with right eigenvectors {v_k} and left eigenvectors {w_k}:

```
G v_k = μ_k v_k
w_k† G = μ_k w_k†
```

Normalization: w_k† v_j = δ_kj (bi-orthogonality).

**Proposition 8.2** (Modal Expansion):

```
Θ(τ) = Σ_k exp(τ μ_k) v_k (w_k† Θ_0)
```

The expansion coefficients c_k = w_k† Θ_0 depend on the left eigenvectors.

### 8.3 Pseudospectrum

**Definition 8.3** (ε-Pseudospectrum):

The ε-pseudospectrum of G is:
```
σ_ε(G) = {z ∈ ℂ : ||(zI - G)^{-1}|| ≥ 1/ε}
```

**Physical Significance**: Even if eigenvalues suggest stability (Re(μ_k) < 0), the pseudospectrum can extend into Re(z) > 0, indicating potential for transient growth.

**Theorem 8.4** (Transient Amplification):

For non-normal G, there exists t_max such that:
```
||Θ(t_max)|| > ||Θ_0|| exp(max_k Re(μ_k) · t_max)
```

This is transient growth: temporary amplification beyond what eigenvalues predict.

### 8.4 Spectral Abscissa vs. Numerical Abscissa

**Definition 8.5**:
- **Spectral abscissa**: α_spec(G) = max_k Re(μ_k)
- **Numerical abscissa**: α_num(G) = sup_t (1/t) log ||exp(tG)||

For normal matrices: α_spec = α_num.
For non-normal: α_num can be much larger than α_spec.

**Physical Consequence**: Complex-τ evolution with non-normal G can exhibit:
1. Sudden spectral broadening (eigenvalues of O(t) spread rapidly)
2. Non-monotonic entropy evolution
3. Phase-entropy correlation patterns inconsistent with normal (commuting) generators

---

## 9. Diagnostic Invariants and Discriminators (A/B Test Between τ Real vs τ Complex)

### 9.1 Discriminator D1: Phase-Entropy Coupling Coefficient

**Definition 9.1** (Coupling Coefficient):

```
C_ΣS(t) := ∂_t Σ_Θ / ∂_t S_Θ = (k_B Tr B) / (2k_B Tr A) = (Tr B) / (2 Tr A)
```

**Test**:
- **Real τ (ψ = 0)**: C_ΣS is constant, determined solely by G
- **Complex τ (ψ ≠ 0)**: C_ΣS can vary if ψ(t) changes or if G itself depends on ψ

**Prediction**: Observe time-varying C_ΣS(t) as a signature of complex-time evolution.

### 9.2 Discriminator D2: Conservation Test

**Definition 9.2** (Spectral Drift):

Define the eigenvalue variance of O(t):
```
Var_O(t) := Tr(O²(t)) / (Tr O(t))² - 1/n
```

**Test**:
- **Anti-Hermitian G with real τ**: Var_O(t) = constant
- **Complex τ with Herm(G) ≠ 0**: Var_O(t) drifts monotonically or non-monotonically

**Prediction**: Monitor Var_O(t) for unexpected drift:
```
d(Var_O)/dt ≠ 0 implies Herm(G) ≠ 0 or complex-τ effects
```

### 9.3 Discriminator D3: Mode Pairing and Oscillatory Signatures

**Definition 9.3** (Conjugate Mode Correlation):

For complex eigenvalue pair μ = α ± iω, the phase channel exhibits:
```
Σ_Θ(t) ∝ t·ω (oscillatory component)
```

while the entropy channel varies as:
```
S_Θ(t) ∝ t·α (monotonic growth/decay)
```

**Test**:
- **Real τ**: Σ_Θ and S_Θ are uncorrelated (orthogonal channels)
- **Complex τ**: Oscillations in Σ_Θ correlate with features in S_Θ

**Signature**: Look for:
1. Periodic modulation of Σ_Θ with frequency ω
2. Monotonic drift in S_Θ with rate α
3. **Cross-correlation**: When Σ_Θ oscillates, S_Θ may show corresponding fine structure

**Measurement Protocol**:
```
FFT[Σ_Θ(t)] → extract dominant frequency ω_obs
FFT[S_Θ(t)] → check for features at ω_obs (cross-channel leakage)
```

### 9.4 Summary Table of Discriminators

| Discriminator | Observable | Real τ Behavior | Complex τ Signature |
|---------------|------------|-----------------|---------------------|
| D1: C_ΣS | ∂_t Σ_Θ / ∂_t S_Θ | Constant | Time-varying |
| D2: Var_O | Tr(O²)/(Tr O)² | Conserved (if G anti-Herm) | Drifts |
| D3: Mode Pairing | FFT[Σ_Θ] vs FFT[S_Θ] | Uncorrelated | Cross-correlation at ω_k |

---

## Appendix A: 2×2 Worked Example (Closed Form)

### A.1 Setup

Consider a 2×2 generator:
```
G = [α₁  0 ]  + i [0   ω ]  = [ α₁    iω ]
    [0   α₂]      [-ω  0 ]    [-iω   α₂]
```

where α₁, α₂, ω ∈ ℝ.

This represents:
- Diagonal real part: different growth rates for two modes
- Anti-symmetric imaginary part: coupling between modes

### A.2 Eigenvalues

The characteristic polynomial is:
```
det(G - λI) = (α₁ - λ)(α₂ - λ) + ω² = 0
```

Eigenvalues:
```
λ_± = (α₁ + α₂)/2 ± √[(α₁ - α₂)²/4 - ω²]
```

**Case 1**: If (α₁ - α₂)² > 4ω², eigenvalues are real.
**Case 2**: If (α₁ - α₂)² < 4ω², eigenvalues are complex conjugate pair.

### A.3 Complex-Time Evolution

For τ = t + iψ:

```
exp(τG) = exp((t + iψ)G)
```

Using spectral theorem:
```
exp(τG) = Σ_± exp(τλ_±) P_±
```

where P_± are the projection operators onto eigenvectors.

### A.4 Determinant Channel

```
det Θ(τ) = exp(τ Tr G) det Θ₀ = exp(τ(α₁ + α₂)) det Θ₀
```

Thus:
```
S_Θ(τ) = 2k_B Re[τ(α₁ + α₂)] = 2k_B(t(α₁ + α₂) - ψ·0) = 2k_B t(α₁ + α₂)
Σ_Θ(τ) = k_B Im[τ(α₁ + α₂)] = k_B(t·0 + ψ(α₁ + α₂)) = k_B ψ(α₁ + α₂)
```

**Observation**: For this example with purely real trace, S_Θ depends only on t, and Σ_Θ depends only on ψ. The coupling appears in the eigenmode structure, not the determinant.

### A.5 Mode Amplitude Evolution

For an eigenvector v_+ with eigenvalue λ_+ = α_+ + iω_+:

```
|exp(τλ_+)| = exp(tα_+ - ψω_+)
arg(exp(τλ_+)) = tω_+ + ψα_+
```

This explicitly shows the cross-coupling: ψ modulates the amplitude through ω_+.

---

## Appendix B: Relation to Heat-Kernel / Tr log Representation (Symbolic)

### B.1 Heat Kernel Approach

The heat kernel representation relates the determinant to the trace of the evolution operator:

```
log det Θ = Tr log Θ
```

For the flow Θ(τ) = exp(τG)Θ₀:
```
log det Θ(τ) = Tr[log(exp(τG)Θ₀)] = Tr[τG + log Θ₀] = τ Tr G + Tr log Θ₀
```

This reproduces our result from Theorem 6.1.

### B.2 Functional Determinant

In field theory, the functional determinant is often regulated using:
```
det O = exp(Tr log O)
```

For O = Θ†Θ:
```
S_Θ = k_B log det(Θ†Θ) = k_B Tr log(Θ†Θ) = k_B Tr(log Θ† + log Θ)
    = 2k_B Re[Tr log Θ]
```

This connects the entropy channel to the trace logarithm, a standard quantity in quantum field theory.

### B.3 Zeta Function Regularization

For systems with continuous spectra, the determinant can be regulated using the spectral zeta function:
```
ζ_G(s) = Σ_k μ_k^{-s}
```

The regularized determinant is:
```
det_reg G = exp(-ζ_G'(0))
```

This connects the spectral properties (eigenvalues μ_k) to the determinant structure.

---

## Appendix C: Regularization Near det → 0 (Why log → -∞ Appears)

### C.1 Singular Configurations

When det Θ → 0, the matrix becomes singular (non-invertible). This corresponds to:
- At least one eigenvalue λ_k → 0
- The field configuration approaches a lower-dimensional subspace

### C.2 Logarithmic Divergence

As det Θ → 0:
```
log det Θ → -∞
```

This divergence is physical and represents:
1. **Entropy collapse**: S_Θ → -∞ (infinite negative entropy)
2. **Information loss**: The system approaches a zero-volume configuration
3. **Phase singularity**: arg det Θ becomes ill-defined

### C.3 Regularization Strategies

**Strategy 1** (Small Mass): Add a small regularization:
```
Θ_reg = Θ + εI
```

Then:
```
log det Θ_reg = log det(Θ + εI) ≈ log det Θ + ε Tr(Θ^{-1}) + O(ε²)
```

**Strategy 2** (Zeta Regularization): Use the spectral zeta function (Appendix B.3).

**Strategy 3** (Principal Value): Define:
```
S_Θ = k_B lim_{ε→0} [log det(Θ†Θ + ε²I)]
```

### C.4 Physical Interpretation

The divergence log det Θ → -∞ is not a pathology but a physical statement:
- **Black hole analogy**: As matter collapses, entropy of external region diverges (information paradox)
- **Quantum decoherence**: Pure states (det = 0) have infinite negative entropy relative to mixed states
- **Phase transition**: Singular configurations mark phase boundaries in the biquaternionic field space

**Conclusion**: The logarithmic divergence is a feature, not a bug. It encodes critical information about singularities in the field configuration.

---

## Summary and Outlook

### Main Results

1. **Complex-τ couples growth and oscillation**: At the eigenmode level, exp(τμ_k) = exp(tα_k - ψω_k) exp(i(tω_k + ψα_k)) shows explicit mixing of real and imaginary eigenvalue components.

2. **Determinant identities**: log det Θ(τ) = τ Tr G + log det Θ₀ provides exact expressions for S_Θ and Σ_Θ in terms of Tr A and Tr B.

3. **Three discriminators (D1-D3)**: Phase-entropy coupling coefficient, conservation tests, and mode pairing provide testable signatures to distinguish real-time from complex-time evolution.

4. **Non-Hermitian effects**: Pseudospectrum and transient growth explain sudden spectral broadening even without parameter changes.

### Experimental Implications

Measure:
- Time series of S_Θ(t) and Σ_Θ(t)
- Eigenvalue distribution of O(t) = Θ†Θ
- Cross-correlation between phase and entropy channels

Look for:
- Time-varying coupling coefficient C_ΣS
- Unexpected spectral drift in Var_O
- Oscillatory signatures with cross-channel correlations

### Open Questions

1. What determines ψ(t) dynamically in UBT?
2. Can non-Hermitian G be physically measured or inferred?
3. How do quantum corrections modify the linear flow approximation?
4. What is the connection to measurement/decoherence in quantum mechanics?

---

**Document Status**: Complete symbolic derivation  
**Next Steps**: Optional SymPy verification (see `sympy/complex_tau_linear_flow.py`)

---

© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0
