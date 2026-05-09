<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Hecke-Equivariant Path Integral: No-Go Report

**Task**: `construct_or_kill_hecke_equivariant_winding_path_integral`  
**Date**: 2026-05-09  
**Companion file**: `research_tracks/alpha_spectral/hecke_equivariant_path_integral.tex`  
**Predecessor**: `reports/hecke_trace_B_verdict.md`

---

## Verdict

> **CONSTRUCTION INCOMPLETE — NO-GO AT CURRENT LEVEL**
>
> The Hecke-equivariant path-integral decomposition of the UBT winding sector
> at prime level *p* **cannot be completed** from the current UBT action
> S[Θ].  The arithmetic layer is exact.  The physics layer encounters three
> sharp, precisely located obstructions (O1–O3) that block the derivation.
>
> B(p) = (p+1)/3 **remains a conditional modular ansatz**.

---

## Must-answer questions

| # | Question | Answer | Status |
|---|----------|--------|--------|
| Q1 | Does S[Θ] naturally define a modular τ variable? | Complex time τ = t+iψ is formally a complex modulus, but S[Θ] is **not proved** to be SL(2,ℤ)-invariant (Obstruction O1). | **CONDITIONAL** |
| Q2 | Does the p-winding sector transform under Γ₀(p)? | Arithmetically: yes — ℍ_p is closed under Γ₀(p) if SL(2,ℤ) acts on winding modes (proved as arithmetic fact). Physically: the SL(2,ℤ) action on winding modes has **not been derived** (Obstruction O2). | **CONDITIONAL** |
| Q3 | Are there exactly p+1 inequivalent saddles? | Coset count is **exact**: \|Γ₀(p)∖SL(2,ℤ)\| = p+1, bijecting with ℙ¹(𝔽_p). Their physical inequivalence in the path integral is **unproved**. | **CONDITIONAL** |
| Q4 | Are they equal-action? | **No** — not derivable without resolving O1. Equal action requires SL(2,ℤ) invariance of S[Θ]. | **NO-GO** |
| Q5 | Does their contribution multiply the n log n coefficient? | Conditionally yes: if all p+1 saddles are equal-action, the saddle sum contributes a factor p+1 to the free energy, reproducing the B·n log n structure after normalisation. | **CONDITIONAL** |
| Q6 | Does the division by 3 enter through modular area normalisation? | **Yes — unconditionally** (arithmetic): vol(X₀(p))/π = (p+1)/3 follows from vol(SL(2,ℤ)∖ℍ) = π/3. Physics interpretation (path-integral normalised over fundamental domain) is reasonable but not derived from S[Θ]. | **PROVED** (arith); **CONDITIONAL** (physics) |

---

## What was constructed

### 1. Hilbert space of winding states ℋ_p

Defined as the L²-closure of the subspace of winding modes with winding
number n ≡ 0 (mod p):

```
ℋ_p = span̄ { Θ_n | n ≡ 0 (mod p) }
```

This is natural: the quadratic kinetic term in S[Θ] does not mix
modes with p | n and modes with p ∤ n on a symmetric background.

### 2. Arithmetic action of Γ₀(p) on ℋ_p

The subspace ℋ_p is arithmetically closed under Γ₀(p), because the
condition c ≡ 0 (mod p) (defining Γ₀(p)) preserves the sublattice pℤ ⊂ ℤ
of winding numbers. This is an exact, unconditional arithmetic statement.

### 3. Coset identification with ℙ¹(𝔽_p)

The coset space Γ₀(p)∖SL(2,ℤ) is in bijection with ℙ¹(𝔽_p) via
the map (a b; c d) ↦ [c:d] ∈ ℙ¹(𝔽_p).  This gives exactly p+1
coset representatives. **This is exact arithmetic.**

Explicit representatives:
- γ_∞ = (0 -1; 1 0) corresponding to [1:0]
- γ_a = (1 a; 0 1) for a = 0, 1, …, p−1 corresponding to [0:1], [1:1], …, [p−1:1]

### 4. Candidate saddle set indexed by ℙ¹(𝔽_p)

For each coset representative γ_a ∈ SL(2,ℤ), define the a-th saddle
configuration Θ̄_a as the classical solution of the S[Θ] equations of
motion with the complex-time modulus shifted to γ_a · τ.  This gives a
candidate set 𝒮 of p+1 saddles.

### 5. One-loop weights

The one-loop partition function around each saddle is:

```
Z_a^(1) = e^{-S[Θ̄_a]} · (det' ∇†∇|_{Θ̄_a})^{-1/2}
```

If S[Θ] is SL(2,ℤ)-invariant, then all Z_a^(1) are equal and the saddle sum
gives Z_p = (p+1) · e^{-S*} · C_{1-loop}.

### 6. Condition for equal weighting

Equal action of all p+1 saddles holds **if and only if** S[Θ] is
invariant under SL(2,ℤ) acting by τ-reparametrisations. This is a
necessary and sufficient condition (Proposition 5.3 in companion .tex).

### 7. Derivation of normalisation by vol(SL(2,ℤ)∖ℍ) = π/3

The factor 1/3 in B(p) = (p+1)/3 equals vol(SL(2,ℤ)∖ℍ)/π = (π/3)/π = 1/3.
More precisely:

```
B(p) = vol(X₀(p)) / π = [μ(Γ₀(p)) · vol(SL(2,ℤ)∖ℍ)] / π
     = (p+1) · (π/3) / π = (p+1)/3
```

This is **exact** and unconditional. It does not require any UBT-specific assumption.

---

## Exact obstructions

### Obstruction O1 — S[Θ] not proved modular-invariant

**Statement**: The UBT action S[Θ] has not been shown to be invariant
under SL(2,ℤ) acting on the complex-time modulus τ = (t + iψ)/β.

**Where it bites**: Without SL(2,ℤ) invariance, the p+1 candidate
saddles can have different classical actions. The degeneracy factor p+1
does not emerge. All downstream results (Q4, Q5) are blocked.

**What would resolve it**: Prove that ∇†∇ on the complex-time torus is a
modular-covariant operator of definite weight, and that the measure
d⁴x dψ transforms covariantly. An η-function regularisation argument
analogous to the string one-loop amplitude (Polchinski §7) might work.

### Obstruction O2 — SL(2,ℤ) action on winding modes not derived

**Statement**: The physical action of a Möbius transformation
τ → (aτ+b)/(cτ+d) on the Fourier coefficients Θ_n in the winding
expansion has not been computed.

**Where it bites**: Lemma 4.2 (arithmetic compatibility of ℋ_p with Γ₀(p))
is unconditional. But connecting it to a genuine physical equivariance of
the path integral requires the missing computation.

**What would resolve it**: Expand Θ(x,τ) = Σ_n Θ_n(x) e^{2πinτ} in
the Fourier basis and compute how a Möbius transformation reshuffles the
coefficients. Show the induced map on ℋ_p is well-defined and bounded.

### Obstruction O3 — equal-action not derivable (depends on O1)

**Statement**: The claim that all p+1 saddles Θ̄_a are equal-action is
equivalent to SL(2,ℤ) invariance of S[Θ] (O1). Without O1 this is a
no-go.

**Dependency**: O3 resolves automatically once O1 is resolved.

---

## What is exact (unconditional)

| Claim | Proof |
|-------|-------|
| \|Γ₀(p)∖SL(2,ℤ)\| = p+1 | Index formula for congruence subgroups |
| Bijection with ℙ¹(𝔽_p) | Standard modular-forms fact |
| vol(SL(2,ℤ)∖ℍ) = π/3 | Classical result |
| B(p) = (p+1)/3 = vol(X₀(p))/π | Corollary of area formula |
| Denominator 3 = vol(SL(2,ℤ)∖ℍ)·3/π | Exact geometric fact |
| ℋ_p arithmetically closed under Γ₀(p) | Arithmetic of sublattice pℤ |

---

## What remains conditional

| Claim | Condition needed |
|-------|-----------------|
| S[Θ] defines modular τ | O1: prove SL(2,ℤ) invariance of S[Θ] |
| ℋ_p physically transforms under Γ₀(p) | O2: derive SL(2,ℤ) action on winding modes |
| p+1 inequivalent equal-action saddles | O1 + O2 + O3 |
| Saddle sum multiplies n log n by p+1 | Equal-action (O1, O3) |
| B(p) derived from S[Θ] | All of O1–O3 |

---

## Implication for Gap G137-B

Gap G137-B is **not closed** by the present analysis. The canonical
wording remains:

> B(p) = (p+1)/3 is structurally motivated by modular geometry and is
> arithmetically exact, but it is not derived from S[Θ] and therefore
> remains **conditional** until Obstructions O1 and O2 are resolved.

This is consistent with the verdict in `reports/hecke_trace_B_verdict.md`
and strengthens it by identifying the exact obstruction points with precise
proof-level statements.

---

## Internal references

- `research_tracks/alpha_spectral/hecke_equivariant_path_integral.tex` — companion LaTeX document (full proofs)
- `research_tracks/alpha_spectral/hecke_trace_B_derivation_attempt.tex` — predecessor attempt
- `research_tracks/alpha_spectral/b_coefficient_gap_resolution.tex` — synthesis of all B-coefficient routes
- `reports/hecke_trace_B_verdict.md` — verdict on G137-B
- `canonical/alpha/modular_prime_attractor_theorem.tex` — formal prime-attractor theorem
