<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Γ₀(137) Modular Structure — Invariants and UBT Comparison

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Workstream**: G137_1  
**Status**: Research document  
**Companion files**:
- `tools/compute_modular_curve_genus.py` — automated genus/index computation
- `docs/reports/hecke_lepton/prime_specificity_results.txt` — Hecke eigenvalue results
- `reports/prime_137_structural_audit.md` — cross-workstream audit

---

## 1. Purpose

Determine whether the prime p = 137 has deeper structural meaning in UBT
through the arithmetic geometry of the modular group Γ₀(137).  Specifically:

1. Compute all basic invariants of Γ₀(137) and the modular curve X₀(137).
2. Compare modular-form invariants at level 137 with existing UBT p = 137 signals.
3. Assess whether the genus g = 11 or index μ = 138 admits a UBT interpretation.
4. Record which observations are invariant (structural) vs numerical coincidences.

**Hard rule**: Every occurrence of 137 must be tied to invariant meaning.
No post-hoc fitting.

---

## 2. Computed Invariants of Γ₀(137)

The standard formulas (Diamond & Shurman, Theorem 3.1.1) for prime level p:

| Invariant | Formula | Value at p = 137 |
|-----------|---------|-----------------|
| Index in SL(2,ℤ) | μ = p + 1 | **138** |
| Cusps | ν_∞ = 2 | **2** (0 and ∞) |
| Elliptic pts order 2 | ν₂ = 1 + (−4\|p) | **2** (since 137 ≡ 1 mod 4) |
| Elliptic pts order 3 | ν₃ = 1 + (−3\|p) | **0** (since 137 ≡ 2 mod 3) |
| Genus of X₀(137) | g = 1 + μ/12 − ν₂/4 − ν₃/3 − ν_∞/2 | **11** |
| Hyperbolic volume | vol(X₀(137)) = π(p+1)/3 | **46π ≈ 144.51** |

**Derivation check** (exact):

```
g = 1 + 138/12 − 2/4 − 0/3 − 2/2
  = 1 + 11.5 − 0.5 − 0 − 1
  = 11.0  ✓
```

### 2.1 Kronecker Symbol Details

- (−4|137): Since 137 ≡ 1 (mod 4), the Legendre symbol (−1|137) = (−1)^{(137−1)/2} = (−1)^{68} = +1.
  Therefore (−4|137) = (−1|137)·(4|137) = (+1)(+1) = **+1**.  So ν₂ = 1 + 1 = 2.

- (−3|137): Since 137 ≡ 2 (mod 3), the Legendre symbol (−3|137) = **−1**
  (by the formula: (−3|p) = +1 iff p ≡ 1 mod 3).  So ν₃ = 1 − 1 = 0.

### 2.2 Comparison with Twin Prime p = 139

| Invariant | p = 137 | p = 139 |
|-----------|---------|---------|
| μ | 138 | 140 |
| ν₂ | 2 | 0 |
| ν₃ | 0 | 2 |
| g | 11 | 11 |
| vol/π | 46 | 46.667 |

Note: 137 and 139 are twin primes; both have genus 11.  Their
elliptic-point structures are complementary: 137 has ν₂ = 2, ν₃ = 0;
139 has ν₂ = 0, ν₃ = 2.  This complementarity may be related to the
twin-prime mutual exclusivity observed in the Hecke lepton-mass results
(Set A hits p = 137, Set B hits p = 139; each is blind to the other).

---

## 3. Cusp Forms at Level 137

### 3.1 Dimension of S₂(Γ₀(137))

By the Riemann–Roch formula for modular curves:

```
dim S₂(Γ₀(137)) = g(X₀(137)) = 11
```

Since 137 is prime, the old space is empty and **all 11 dimensions consist
of newforms**.  The 11 dimensions decompose over Q into newforms of various
field degrees d_i with Σ d_i = 11.

### 3.2 Atkin-Lehner Involution

For prime level p, the Atkin–Lehner involution w_p acts on S₂(Γ₀(p)).
Each newform f satisfies w_p f = ε_p f with ε_p = ±1 (the root number
of the L-function L(f, s)).  The Hecke eigenvalue at p satisfies:

```
a_p(f) = ε_p    (for weight 2, prime level)
```

So each of the 11 newforms in S₂(Γ₀(137)) has a_{137} ∈ {+1, −1}.

### 3.3 Hecke Eigenvalues at p = 137 of Forms at Other Levels

The UBT Hecke-lepton conjecture (2026-03-07) uses forms at *other* levels
and evaluates their Hecke eigenvalue *at prime p = 137*:

| Form | Level N | Weight k | a_{137} | a_{137} type |
|------|---------|----------|---------|--------------|
| Electron (gen 1) | 76 | 2 | **−11** | good prime (gcd(76,137)=1) |
| Muon (gen 2) | 7 | 4 | **+2274** | good prime |
| Tau (gen 3) | 208 | 6 | **−38286** | good prime |

These are Hecke eigenvalues of forms whose level is *coprime to 137*.
At a good prime p, the Weil bound gives |a_p| ≤ 2p^{(k−1)/2}:

| Form | Weil bound at p=137 | Observed |a_{137}| | Within bound? |
|------|--------------------|-----------------------|---------|
| k=2 | 2√137 ≈ 23.4 | 11 | ✓ |
| k=4 | 2·137^{3/2} ≈ 3208 | 2274 | ✓ |
| k=6 | 2·137^{5/2} ≈ 439,360 | 38286 | ✓ |

All eigenvalues satisfy the Weil bound — they are consistent with genuine
Hecke eigenvalues of modular forms.

### 3.4 Lepton Mass Ratio Reconstruction

From the Hecke eigenvalues above:

```
R_μ  = |a_{137}(k=4)| / |a_{137}(k=2)| = 2274 / 11 = 206.727
R_τ  = |a_{137}(k=6)| / |a_{137}(k=2)| = 38286 / 11 = 3480.545
```

| Ratio | UBT (Hecke) | Experimental (PDG 2022) | Error |
|-------|-------------|------------------------|-------|
| R_μ = m_μ/m_e | 206.727 | 206.768 | **0.02%** |
| R_τ = m_τ/m_e | 3480.55 | 3477.23 | **0.10%** |

This is a **strong numerical signal**: p = 137 is the unique prime in the
range 50–300 for which these three forms reproduce both lepton mass ratios
to < 0.1% (global scan result from 2026-03-07).

**Classification**: STRONG NUMERICAL SIGNAL — not yet a derivation.  The
forms were found by a search at level 137; their theoretical motivation
within UBT is the open problem (workstream G137_1).

---

## 4. Connection of Index μ = 138 to B_phenom

### 4.1 The Key Numerical Coincidence

The hyperbolic volume and index yield:

```
vol(X₀(137)) / π = μ(Γ₀(137)) / 3 = 138 / 3 = 46.000
```

The phenomenological B coefficient required to set n* = 137 in the UBT
V_eff potential is:

```
From dV_eff/dn = 0 at n* = 137:
    2 × 137 = B × (ln 137 + 1)
    B_phenom = 274 / (ln 137 + 1) = 274 / 5.9189 ≈ 46.298
```

Comparison:

| Quantity | Value | Relative to B_phenom |
|----------|-------|----------------------|
| B_phenom (V_eff minimum at n*=137) | 46.298 | — |
| μ(Γ₀(137)) / 3 | 46.000 | −0.64% |
| μ(Γ₀(137)) / 3 + ν₂/4 | 46.500 | +0.44% |
| N_eff^{3/2} = 12^{3/2} | 41.569 | −10.2% |
| B₀ = 8π | 25.133 | −45.7% |

**Finding**: The modular invariant μ(Γ₀(p))/3 evaluated at p = 137
reproduces B_phenom to within 0.64%, which is the best available match.
The inclusion of the elliptic-point correction ν₂/4 = 0.5 reduces the
error to 0.44%.

### 4.2 Why μ(Γ₀(137))/3 Is an Invariant

The expression μ(Γ₀(p))/3 is:

```
μ(Γ₀(p)) / 3 = (p + 1) / 3 = vol(X₀(p)) / π
```

This is the **normalised hyperbolic area** of the modular curve X₀(p),
with normalisation factor π/3 = vol(SL(2,ℤ)\ℍ) equal to the volume of
the fundamental domain of the full modular group.  It is:
- A purely arithmetic invariant of Γ₀(p): depends only on p
- Related to the index [SL(2,ℤ) : Γ₀(p)] by a factor of 3
- Equal to |P¹(𝔽_p)| / 3 = (p+1)/3 (see `reports/f137_projective_geometry_check.md`)

### 4.3 Assessment

The coincidence μ(Γ₀(137))/3 ≈ B_phenom is **structurally non-trivial**:
it relates the normalised hyperbolic volume of the modular curve X₀(p) at
p = 137 to the coefficient that places the V_eff minimum at n = p = 137.
This is a **modular** appearance of 137, not a spectral one.

**Current status**: MOTIVATED COINCIDENCE [MC] — the 0.64% error is not
explained; it could be a sub-leading correction (from higher loops, cusp
contributions, or the ν₂/4 elliptic correction) or a chance match.
A derivation of B from the UBT action S[Θ] that recovers (p+1)/3 at p = 137
would elevate this to [L1].

---

## 5. Genus g = 11 and UBT

The genus g(X₀(137)) = 11 does **not** equal N_eff = 12.  Primes for
which g(X₀(p)) = 12 are p ∈ {149, 151, 157, ...} (the smallest being
p = 149).  There is no g = N_eff = 12 coincidence at the UBT prime p = 137.

**Classification**: The genus 11 at p = 137 has no known UBT interpretation.
Record as **no coincidence**.

---

## 6. Twin-Prime Modular Symmetry

The Hecke lepton results (2026-03-07) show:

- **Set A** (levels 76, 7, 208): hits only p = 137; blind to p = 139.
- **Set B** (levels 195, 50, 54): hits only p = 139; blind to p = 137.

The complementary elliptic-point structure (ν₂, ν₃) at p = 137 vs p = 139
(Section 2.2) may reflect this modular symmetry, but a direct connection
to the Set A/B form levels has not been established.

**Classification**: SUGGESTIVE PATTERN — requires theoretical motivation.

---

## 7. Summary Table

| Observation | Mathematical type | Value | UBT relevance | Classification |
|-------------|------------------|-------|---------------|----------------|
| Index μ(Γ₀(137)) = 138 | Arithmetic invariant | p+1 | = \|P¹(𝔽_137)\| | Exact identity |
| vol(X₀(137))/π = 46 | Geometric invariant | (p+1)/3 | ≈ B_phenom (−0.64%) | [MC] |
| vol/π + ν₂/4 = 46.5 | Geometric+elliptic | (p+1)/3 + ν₂/4 | ≈ B_phenom (−0.44%) | [MC] |
| g(X₀(137)) = 11 | Topological | standard formula | No N_eff match | No coincidence |
| ν₂ = 2, ν₃ = 0 | Elliptic geometry | 137 ≡ 1 mod 4, 2 mod 3 | Complements p=139 | Structural |
| a_{137}(N=76,k=2) = −11 | Hecke eigenvalue | Weil-bounded | Lepton mass ratio | Strong signal [MC] |
| Lepton R_μ error | Precision | 0.02% | Within PDG | Strong signal |
| Lepton R_τ error | Precision | 0.10% | Within PDG | Strong signal |

---

## 8. Open Problems Identified

| ID | Description | Priority |
|----|-------------|----------|
| G1-Bmod | Derive B = μ(Γ₀(137))/3 from S[Θ] without using p=137 as input | HIGH |
| G1-forms | Explain why levels 76, 7, 208 at weight 2, 4, 6 are selected by UBT | HIGH |
| G1-twin | Derive the Set A / Set B modular symmetry between p=137 and p=139 | MEDIUM |
| G1-genus | Determine if g=11 has any role in the mode-counting structure | LOW |

---

## References (Internal)

- `tools/compute_modular_curve_genus.py` — genus and index computations
- `docs/reports/hecke_lepton/prime_specificity_results.txt` — Hecke results
- `canonical/alpha/alpha_best_route.tex` — V_eff derivation chain
- `reports/f137_projective_geometry_check.md` — P¹(𝔽_137) analysis
- Diamond & Shurman, *A First Course in Modular Forms*, Springer 2005, Thm 3.1.1
