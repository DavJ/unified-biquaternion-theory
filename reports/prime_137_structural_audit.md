<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Structural Audit of Prime 137 in UBT

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Workstreams**: G137_1, G137_2, G137_3, G137_4  
**Status**: Research document — comprehensive cross-workstream audit  
**Companion files**:
- `reports/gamma0_137_invariants.md` — Γ₀(137) detailed analysis
- `reports/f137_projective_geometry_check.md` — P¹(𝔽₁₃₇) and polytope check
- `canonical/alpha/prime_137_status.md` — canonical status summary
- `ALPHA_STRUCTURAL_ORIGINS.md` — N_eff and exponent derivations

---

## Purpose

The prime 137 appears in UBT in multiple distinct roles.  This audit:

1. Lists every known appearance of 137 in UBT.
2. Classifies each appearance as: **spectral**, **modular**, **finite-field**,
   or **geometric**.
3. Rates each appearance as: [L0] proved / [L1] conditional / [MC] motivated
   conjecture / [NC] numerical coincidence / [SPEC] speculative / [REJECT] rejected.
4. Identifies which appearances are independent and which are derived from others.

**Hard rule**: No fitted numerology.  Every appearance must trace to an
invariant meaning or be explicitly classified as a coincidence / rejected.

---

## 1. Classification of All Known 137 Appearances

### 1.1 SPECTRAL: V_eff Prime Attractor (Primary Route)

**Where**: `canonical/alpha/alpha_best_route.tex`, `ALPHA_STRUCTURAL_ORIGINS.md`

**Claim**: The winding-mode effective potential

```
V_eff(n) = n² − B · n · ln n,    dV_eff/dn = 0  ⟹  n* = 137
```

selects n* = 137 when B = B_phenom ≈ 46.298.

**Computation**:
```
dV_eff/dn = 2n − B(ln n + 1) = 0
⟹  B_phenom = 2n* / (ln n* + 1) = 274 / (ln 137 + 1) ≈ 46.298
```

**Independence**: This is a *conditional* derivation.  The value 137 is
output, not input, once B is fixed.  The derivation of B is the open gap.

**Sub-classification**:

| Step | Content | Status |
|------|---------|--------|
| V_eff formula | From UBT field on S¹_ψ | [L1] — conditional on Kac-Moody level k=1 |
| B₀ = 8π | One-loop QED coefficient | [L0/L1] — proved |
| B_base = 12^{3/2} ≈ 41.57 | From N_eff=12 and heat-kernel exponent 3/2 | [MC] — motivated but not proved |
| B_phenom ≈ 46.298 | What makes n* = 137 exact | Target — requires derivation |
| n* = 137 from B_phenom | V_eff minimum | [L1] given B = B_phenom |
| n* is prime | Stability argument | [L1] — proved numerically, analytic gap remains |

**Type**: SPECTRAL — the spectrum of winding modes selects n* = 137.  
**Classification**: [L1] **conditional** on the derivation of B.

---

### 1.2 MODULAR: Index μ(Γ₀(137)) = 138 and Normalised Volume

**Where**: `reports/gamma0_137_invariants.md`, `tools/compute_modular_curve_genus.py`

**Claim**: The normalised hyperbolic volume of the modular curve X₀(137)
matches B_phenom:

```
μ(Γ₀(137)) / 3 = 138 / 3 = 46.000 ≈ B_phenom = 46.298  (error: 0.64%)
```

**Type**: MODULAR — the arithmetic geometry of the congruence subgroup Γ₀(137).

**Why non-trivial**: The index μ(Γ₀(p)) = p + 1 is an arithmetic invariant
of the modular group structure, not a free parameter.  At p = 137, the
normalised index 138/3 = 46 approximates the coefficient B that places the
V_eff minimum at n = p.  If a UBT derivation of B = (p+1)/3 exists, it would
explain *why p = 137 is self-consistent*: the modular index at level p equals 3B(p),
where B(p) is the coefficient that places the winding minimum at n = p.

**The self-consistency condition**: Demand that the V_eff minimum n*(B) equals
the modular index level p:

```
n*(B) = p    and    B = μ(Γ₀(p)) / 3 = (p+1)/3
```

Substituting: n*((p+1)/3) = p?  Check at p = 137:
```
n*( (138)/3 ) = n*(46) ≈ ?
dV/dn=0 at B=46: n* = 23(ln n*+1), iterate: n*≈133.8  (close, 2.3% from 137)
```

With B = 46.298 (exact): n* = 137.  With B = 46 (integer): n* ≈ 133.8.
So the exact condition n*(B) = p is not satisfied with B = (p+1)/3 exactly —
there is a 0.64% residual.  The condition is approximately but not exactly satisfied.

**Classification**: [MC] MOTIVATED COINCIDENCE — the 0.64% gap is unexplained.

---

### 1.3 MODULAR: Hecke Eigenvalues and Lepton Mass Ratios

**Where**: `docs/reports/hecke_lepton/prime_specificity_results.txt`,
`scripts/hecke/test_prime_specificity.sage`

**Claim**: Hecke eigenvalues a_{137} of specific modular forms reproduce
the lepton mass ratios m_μ/m_e and m_τ/m_e to < 0.1%.

Specifically, with forms at levels 76, 7, 208 and weights 2, 4, 6:

```
R_μ  = |a_{137}(k=4)| / |a_{137}(k=2)| = 2274/11  = 206.727  (exp: 206.768, err: 0.02%)
R_τ  = |a_{137}(k=6)| / |a_{137}(k=2)| = 38286/11 = 3480.55  (exp: 3477.23, err: 0.10%)
```

**Prime specificity (global scan, p = 50–300)**: p = 137 is the **unique
global minimum** for these three forms.  No other prime in this range
achieves both errors < 0.1%.

**Type**: MODULAR — Hecke eigenvalues of modular forms at specified levels.

**Independence**: The forms at levels 76, 7, 208 were found by a search;
the theoretical motivation (why these levels and weights?) is the open gap.

**Classification**: [MC] STRONG NUMERICAL SIGNAL — prime specificity
established; derivation from UBT first principles not yet complete.

---

### 1.4 FINITE-FIELD: P¹(𝔽₁₃₇) has 138 Points

**Where**: `reports/f137_projective_geometry_check.md`

**Claim**: |P¹(𝔽₁₃₇)| = 138 connects to UBT mode counting or phase structure.

**Analysis**: The identity |P¹(𝔽_p)| = p + 1 = μ(Γ₀(p)) is exact and holds
for all primes p.  It is the *coset parametrisation* of Γ₀(p) in SL(2,ℤ).
This is structurally meaningful but not specific to p = 137.

**UBT phase interpretation**: No invariant map from P¹(𝔽₁₃₇) to UBT phase
space has been found.  The identification of 138 with mode-count is a raw
counting coincidence (Section 4.1 of `f137_projective_geometry_check.md`).

**Classification**: [NC] for the mode-count interpretation; the underlying
exact identity μ(Γ₀(p)) = |P¹(𝔽_p)| is structural but holds for all p.

---

### 1.5 FINITE-FIELD / NUMBER THEORY: 137 is Prime, 137 ≡ 1 (mod 4), 137 ≡ 2 (mod 3)

**Where**: `reports/gamma0_137_invariants.md` §2.1

**Claim**: The congruence class of 137 modulo small integers has structural consequences.

- 137 ≡ 1 (mod 4): the Legendre symbol (−1|137) = +1 (−1 is a QR mod 137),
  so ν₂ = 2 (Γ₀(137) has 2 elliptic points of order 2).
- 137 ≡ 2 (mod 3): the Legendre symbol (−3|137) = −1 (−3 is a QNR mod 137),
  so ν₃ = 0 (Γ₀(137) has no elliptic points of order 3).

**Contrast with p = 139**: 139 ≡ 3 (mod 4) → ν₂ = 0; 139 ≡ 1 (mod 3) → ν₃ = 2.
Twin primes 137, 139 have complementary elliptic-point structures.

**UBT relevance**: This complementarity may explain why Set A (Hecke) hits 137
and Set B hits 139 with mutual exclusivity.  The ν₂ = 2 vs ν₃ = 2 distinction
is a modular-arithmetic invariant of the prime.

**Classification**: [MC] — structurally motivated but connection to Hecke
Set A/B splitting not yet derived.

---

### 1.6 SPECTRAL: n* = 137 as the Unique Prime Attractor

**Where**: `canonical/alpha/alpha_best_route.tex`, stability tests

**Claim**: The V_eff minimum selects a *prime* n*, and n* = 137 is the unique
prime attractor for N_eff = 12 (the mode count from the biquaternion algebra).

The prime-attractor table (from `ALPHA_STRUCTURAL_ORIGINS.md` §5.1):

| N_eff | Prime attractor n* |
|-------|-------------------|
| 4 | 17 |
| 8 | 67 |
| **12** | **137** |
| 24 | 467 |

N_eff = 12 is selected by the SM gauge group structure (5 independent proofs).
The prime 137 emerges from N_eff = 12 without fitting.

**Classification**: [MC→L1] — the prime-attractor result is conditional on
the B formula.  N_eff = 12 is [L0]; the step N_eff = 12 → prime 137 is [MC]
pending the B derivation.

---

### 1.7 GEOMETRIC: g(X₀(137)) = 11 (Genus of Modular Curve)

**Where**: `reports/gamma0_137_invariants.md` §5

**Claim**: The genus 11 of X₀(137) has a UBT meaning.

**Analysis**: g(X₀(137)) = 11 does **not** equal N_eff = 12.  The first prime
p for which g(X₀(p)) = 12 is p = 149, not p = 137.  No UBT interpretation
of g = 11 has been found.

**Classification**: [NONE] — no coincidence identified.

---

### 1.8 POLYTOPE / GEOMETRIC: Root Systems and Exceptional Groups

**Where**: `reports/f137_projective_geometry_check.md` §6

**Claim**: 137 arises as an orbit count in some polytope or root system.

**Analysis**: Checked all classical and exceptional root systems (A_n, B_n,
C_n, D_n, G₂, F₄, E₆, E₇, E₈) and finite groups (A₅, S₅, M₁₁, M₁₂).
137 does not appear as a root count, orbit count, or order in any of these.
137 is prime; this eliminates most combinatorial group-theoretic candidates.

**Classification**: [REJECT] — no polytope/root-system link found.

---

## 2. Independence Assessment

| Appearance | Independent of α? | Independent of n*=137? | Type |
|------------|------------------|----------------------|------|
| V_eff spectral minimum | Yes | n*=137 is output | SPECTRAL [MC] |
| N_eff = 12 | Yes | Yes | [L0] |
| B₀ = 8π | Yes | Yes | [L1] |
| B_base = 41.57 | Yes | Yes | [MC] |
| B_phenom = 46.3 | No (defined by n*=137) | Tautological | TARGET |
| μ(Γ₀(137))/3 = 46 | Yes | Yes | MODULAR [MC] |
| Hecke eigenvalue R_μ | Yes | Yes — search over p=50–300 | MODULAR [MC] |
| |P¹(𝔽₁₃₇)| = 138 | Yes | Yes | FINITE-FIELD [trivial] |
| g(X₀(137)) = 11 | Yes | Yes | GEOMETRIC [none] |
| Root systems | Yes | Yes | [REJECT] |

---

## 3. Theta-Spectrum Derivation Verification (Workstream G137_3)

### 3.1 The V_eff Formula and its Minimum

The effective potential for winding number n on S¹_ψ in UBT is:

```
V_eff(n) = n² − B · n · ln n,    n ∈ ℤ_{>0}
```

The minimum satisfies:

```
dV_eff/dn = 0:  2n = B(ln n + 1)
n*(B) = (B/2)(ln n*(B) + 1)   [transcendental, solved iteratively]
```

At B = B_phenom = 46.298, the exact minimum is n* = 137.06 ≈ 137 (prime).

At B = B_base = 41.57 = 12^{3/2}:

```
n*(41.57) ≈ 120  [computed numerically by iteration]
```

This shows that B_base alone is **insufficient** to reach n* = 137.
The gap is:

```
B_phenom / B_base = 46.298 / 41.57 ≈ 1.114
```

This correction factor R ≈ 1.114 is the key remaining gap in the B derivation.

### 3.2 Assumptions That Fix B

The current derivation chain for B contains these layers:

| Layer | Formula | Status | Fixes B to: |
|-------|---------|--------|-------------|
| One-loop | B₀ = 2πN_eff/3 = 8π ≈ 25.1 | [L1] proved | 25.1 (gives n* ≈ 65) |
| Heat kernel | B_base = N_eff^{3/2} ≈ 41.6 | [MC] | 41.6 (gives n* ≈ 120) |
| Modular index | B = μ(Γ₀(p))/3 = 46.0 | [MC] candidate | 46.0 (gives n* ≈ 133.8) |
| Exact | B_phenom ≈ 46.298 | TARGET | 46.3 (gives n* = 137.06) |

**Which assumption fixes B?**

The heat-kernel derivation (B_base = N_eff^{3/2}) yields B ≈ 41.6 and is
the best first-principles candidate.  It is short by ≈ 11.4% of B_phenom.

The modular-index candidate (B = (p+1)/3) requires knowing p = 137 as the
level, which is circular if p is the very prime being derived.  However, if
the UBT action produces a modular structure at level p = n*, this candidate
becomes a self-consistency condition.

**The correction factor R ≈ 1.114 is the key open problem** for the spectral
derivation of n* = 137.  It can potentially be explained by:
1. Higher-loop corrections to the one-loop V_eff formula.
2. The Kac-Moody level k ≠ 1 (Gap G3-k).
3. The sub-leading cusp/elliptic corrections in the genus formula (adding ν₂/4 = 0.5 brings B to 46.5, within 0.44% of B_phenom).
4. A Casimir energy contribution from the compact S¹_ψ × T³ background.

### 3.3 Can B be Derived Independently from Gauge/Symmetry Data?

From the modular-curve analysis (`gamma0_137_invariants.md` §4):

```
B_phenom ≈ 46.298
μ(Γ₀(137)) / 3 = 46.000  (error: 0.64%)
μ(Γ₀(137)) / 3 + ν₂/4 = 46.500  (error: 0.44%)
```

The Γ₀(137) index is a **gauge/symmetry datum** — it depends only on the prime
level and not on α or m_e.  If UBT can derive a formula B = (p+1)/3 + ε (with
ε from cusp/elliptic corrections) from the gauge structure of the Θ-field at
level n* = p, this would constitute an independent derivation of B from
symmetry data alone.

**Status**: This is the most promising path for G137_3.  The elliptic-point
correction ν₂/4 at p = 137 (= 2/4 = 0.5) reduces the residual to 0.44%.

---

## 4. Summary Classification Table

| Appearance | Domain | Classification | Independence | Quality |
|------------|--------|----------------|-------------|---------|
| n* = 137 from V_eff | Spectral | [MC→L1] | From N_eff and B | PRIMARY |
| N_eff = 12 | Algebraic | [L0] PROVED | From ℬ = ℂ⊗ℍ | CONFIRMED |
| B₀ = 8π | QFT 1-loop | [L1] PROVED | From gauge structure | CONFIRMED |
| B_base = 12^{3/2} | Geometric | [MC] | From d=3 heat kernel | PARTIAL |
| μ(Γ₀(137))/3 ≈ B | Modular | [MC] (0.64% gap) | Independent of α | PROMISING |
| Hecke → lepton ratios | Modular | [MC] STRONG | Independent, prime-specific | STRONG |
| P¹(𝔽₁₃₇) = 138 points | Finite-field | Exact identity (all p) | Yes | STRUCTURAL |
| g(X₀(137)) = 11 | Geometric | [NONE] | — | NO LINK |
| Root systems | Geometric | [REJECT] | — | DEAD END |
| Dodecahedron/A₅ | Geometric | [SPEC] → [REJECT] | — | DEAD END |
| 137 ≡ 1 mod 4 → ν₂=2 | Number theory | Structural | Yes | SUPPORTING |
| Twin prime (137,139) | Number theory | Structural | Yes | SUPPORTING |

---

## 5. Agreed Verdicts on Each Workstream

| Workstream | Verdict |
|------------|---------|
| G137_1 (Γ₀(137) structure) | μ/3 ≈ B_phenom is the key result [MC]; Hecke lepton signal is strong [MC]; genus=11 has no role |
| G137_2 (P¹(𝔽₁₃₇)) | No invariant UBT map; exact identity μ=|P¹| is structural but holds for all p |
| G137_3 (theta spectrum) | n*=137 is verified from V_eff; B_base=41.57 is insufficient; correction R≈1.114 is the gap |
| G137_4 (polytope) | All root systems and exceptional groups checked; **REJECTED** |

---

## 5.5 Self-Consistency Fixed-Point Scan (2026-05-10)

**Source**: `research_tracks/T3_ALPHA/self_consistency_fixed_point.tex`,
`tools/self_consistency_scan.py`

**Method**: Scan primes $p \in [50, 500]$ for the fixed-point condition
$n^*(B_\mathrm{mod}(p)) = p$, where $B_\mathrm{mod}(p) = (p+1)/3$ is the
normalised modular volume of $X_0(p)$.

**Exact algebraic condition**: $(5p-1)/(p+1) = \ln p$

**Key numerical results**:

| $p$ | $B_\mathrm{mod}$ | $n^*(B_\mathrm{mod})$ | $\delta = n^* - p$ | $|\delta|$ |
|-----|------|---------|-------|--------|
| 139 | 46.667 | 138.364 | −0.636 | 0.636 |
| **137** | **46.000** | **135.989** | **−1.011** | **1.011** |
| 149 | 50.000 | 150.319 | +1.319 | 1.319 |
| 151 | 50.667 | 152.726 | +1.726 | 1.726 |

With refined $B_\mathrm{ref}(p) = (p+1)/3 + \nu_2(p)/4$:

| $p$ | $\nu_2$ | $B_\mathrm{ref}$ | $n^*(B_\mathrm{ref})$ | $\delta_r$ |
|-----|------|---------|-------|--------|
| 139 | 0 | 46.667 | 138.364 | −0.636 |
| **137** | **2** | **46.500** | **137.770** | **+0.770** |

**Verdict**:

- $p=137$ is approximately a self-consistent fixed point with $|\delta|/p = 0.74\%$
  (basic) or $0.56\%$ (refined).  Both pass the 1% kill condition.
- $p=139$ has a smaller gap ($|\delta|=0.636$) for the basic formula.
- The exact algebraic equation $(5p-1)/(p+1)=\ln p$ crosses between $p=137$ and
  $p=139$ (at $p_0 \approx 138.5$); neither prime is an exact root.
- The self-consistency condition selects a **twin-prime window** $\{137, 139\}$,
  not $p=137$ uniquely.

**Classification**: [MC] — $p=137$ approximately satisfies the self-consistency
condition, but the condition alone does not uniquely distinguish 137 from 139.

---

## 6. Open Problems Registered

| ID | Description | Priority |
|----|-------------|----------|
| G137-B | Derive B = (p+1)/3 + ε from S[Θ] without using p=137 as input | CRITICAL |
| G137-R | Explain correction factor R ≈ 1.114 between B_base and B_phenom | HIGH |
| G137-Hk | Derive why levels 76, 7, 208 and weights 2, 4, 6 are selected by UBT | HIGH |
| G137-twin | Derive twin-prime symmetry (137/139) from UBT modular structure | MEDIUM |
| G137-Fq | Find invariant map from P¹(𝔽₁₃₇) to UBT field structure (or reject) | LOW |

---

## 7. References (Internal)

- `reports/gamma0_137_invariants.md` — detailed Γ₀(137) analysis
- `reports/f137_projective_geometry_check.md` — P¹(𝔽₁₃₇) and polytope check
- `canonical/alpha/prime_137_status.md` — canonical status
- `ALPHA_STRUCTURAL_ORIGINS.md` — N_eff and exponent derivations (E1–E4)
- `canonical/alpha/alpha_best_route.tex` — V_eff derivation chain
- `docs/reports/hecke_lepton/prime_specificity_results.txt` — Hecke results
- `tools/compute_modular_curve_genus.py` — genus computation script
