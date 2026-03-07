<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# LMFDB Label Identification — Hecke Forms for Lepton Ratios

**Date**: 2026-03-07  
**Author**: Ing. David Jaroš  
**Status**: **[PENDING full verification — labels are provisional]**  
**Related**: `reports/hecke_lepton/sage_results_2026_03_07.md`

---

> ⚠️ **Epistemic notice**
>
> LMFDB label identification requires online access to
> https://www.lmfdb.org/. The labels given here are **provisional**
> — they represent the best available identification based on the
> level, weight, and Hecke eigenvalue data. Full verification requires
> confirming the a_p values against the LMFDB database entry.
>
> LMFDB label format: `N.k.chi.label`  
> Base URL: `https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/{N}/{k}/`

---

## 1. Set A — Forms at p=137 (STRONG NUMERICAL SUPPORT)

### 1.1 Form k=2, N=76, a₁₃₇ = −11

**LMFDB URL**: https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/76/2/

**Provisional label**: `76.2.a.a` (trivial character χ=1; first newform)

**Key data**:
- Level N = 76 = 4 × 19
- Weight k = 2
- Character: trivial (χ=1)
- Confirmed a₁₃₇ = −11 (from SageMath 2026-03-07)

**Connection to elliptic curves**: By the modularity theorem (Wiles–Taylor),
every weight-2 newform with rational coefficients corresponds to an elliptic
curve over ℚ. If the form 76.2.a.a has rational Fourier coefficients, it
corresponds to an elliptic curve of conductor 76.

The elliptic curve database (Cremona labels) for conductor 76:
- 76a1: y² = x³ + x² − 2x (check whether a₁₃₇ = −11 matches)
- 76b1: further curves

**Verification needed**: Confirm a₁₃₇ = −11 against LMFDB entry for 76.2.a.a.

**CM/RM**: Level 76 = 4×19. The discriminant −19 corresponds to the imaginary
quadratic field ℚ(√−19). A weight-2 newform at N=76 with CM by ℚ(√−19) would
have a_p = 0 for primes inert in ℚ(√−19). At p=137: 137 ≡ 3 (mod 4) but
137 split/inert status in ℚ(√−19) requires checking Legendre symbol (−19/137).
Since 137 ≡ 1 (mod 19) and a₁₃₇ ≠ 0, if CM this form is not CM by ℚ(√−19).

**Status**: Provisional. Verify at LMFDB.

---

### 1.2 Form k=4, N=7, a₁₃₇ = +2274

**LMFDB URL**: https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/7/4/

**Provisional label**: `7.4.a.a` (trivial character; unique newform at this level/weight)

**Key data**:
- Level N = 7 (prime)
- Weight k = 4
- Character: trivial (χ=1)
- Confirmed a₁₃₇ = +2274 (from SageMath 2026-03-07)
- Ramanujan bound: 2 × 137^{3/2} ≈ 3207; observed 2274 < 3207 ✓

**Dimension of S₄(Γ₀(7))**: By the dimension formula,
dim S_k(Γ₀(N)) ≈ (k−1)(N+1)/12 for small levels.
For k=4, N=7: dim ≈ 3×8/12 = 2. The newform space dimension = 2 − (oldforms).
Since N=7 is prime and the only oldforms come from level 1 (trivial),
and dim S₄(SL(2,ℤ)) = 0, all of S₄(Γ₀(7)) is new.
The unique newform 7.4.a.a is the ONLY weight-4 newform at level 7.

**Connection to Klein quartic X(7)**:
The modular curve X(7) = X_full(7) (full level structure) has genus 3 and is
the Klein quartic: x³y + y³z + z³x = 0 (over ℂ). This is distinct from
X₀(7) (Γ₀(7)), which has genus 0.

The connection to X(7) (Klein quartic) is NOT direct via Γ₀(7):
- X₀(7) has genus 0 — no non-trivial 2-forms
- The Klein quartic X(7) is a Γ(7)-quotient

However, the **index** μ(Γ₀(7)) = [SL(2,ℤ) : Γ₀(7)] = 8 = dim_ℝ(ℂ⊗ℍ),
giving a suggestive coincidence with the biquaternionic dimension.

**CM status**: A weight-4 newform with CM by an imaginary quadratic field ℚ(√d)
would have L-function L(s,f) = L(s,ψ)L(s,ψ̄) for a Hecke Grössencharacter ψ.
For N=7 (prime), CM forms are very constrained. The unique newform 7.4.a.a
is **likely non-CM** given that its level equals the conductor of CM only in
special cases. Verify at LMFDB.

**Status**: Provisional. This is the most structurally interesting form
(prime level, unique at its level/weight). High priority for verification.

---

### 1.3 Form k=6, N=208, a₁₃₇ = −38286

**LMFDB URL**: https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/208/6/

**Provisional label**: `208.6.a.?` (trivial character; which newform unclear)

**Key data**:
- Level N = 208 = 16 × 13 = 2⁴ × 13
- Weight k = 6
- Character: trivial (χ=1)
- Confirmed a₁₃₇ = −38286 (from SageMath 2026-03-07)
- Ramanujan bound: 2 × 137^{5/2} ≈ 375,278; observed 38286 ≪ bound ✓

**Dimension**: S₆(Γ₀(208)) has multiple newforms at this level.
The correct form is selected by a₁₃₇ = −38286. Multiple newforms at
N=208 may exist; LMFDB lookup is needed to identify the specific label.

**CM status**: N=208 = 2⁴ × 13. The discriminant −8 (ℚ(√−2)) has conductor
4×2=8; discriminant −52 = −4×13 (ℚ(√−13)) has conductor related to 52.
The CM status requires LMFDB verification.

**Status**: Provisional. Label suffix unknown without LMFDB access.

---

## 2. Set B — Forms at p=139 (NUMERICAL OBSERVATION, mirror sector)

### 2.1 Form k=2, N=195, a₁₃₉ = +15

**LMFDB URL**: https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/195/2/

**Provisional label**: `195.2.a.c` (third newform with trivial character;
corresponds to SageMath index [2] = third newform in the list)

**Key data**:
- Level N = 195 = 3 × 5 × 13 (squarefree)
- Weight k = 2
- Character: trivial (χ=1)
- Confirmed a₁₃₉ = +15 (from SageMath 2026-03-06)
- SageMath index: `CuspForms(Gamma0(195), 2).newforms('a')[2]`

**Connection to elliptic curves**: Weight-2 newforms with rational coefficients
correspond to elliptic curves by modularity. N=195 = 3×5×13 is squarefree,
so the corresponding elliptic curve (if rational) has good reduction at all
primes not dividing 195.

**Status**: Provisional. Third newform at N=195 k=2.

---

### 2.2 Form k=4, N=50, a₁₃₉ = +3100

**LMFDB URL**: https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/50/4/

**Provisional label**: `50.4.a.b` (second newform with trivial character;
SageMath index [1] = second newform)

**Key data**:
- Level N = 50 = 2 × 5²
- Weight k = 4
- Character: trivial (χ=1)
- Confirmed a₁₃₉ = +3100 (from SageMath 2026-03-06)
- Ramanujan bound: 2 × 139^{3/2} ≈ 3282; observed 3100 < 3282 ✓ (close to bound)
- SageMath index: `CuspForms(Gamma0(50), 4).newforms('a')[1]`

**Note**: a₁₃₉ = 3100 is close to the Ramanujan bound of 3282, meaning
this eigenvalue is near-extremal (|λ₁₃₉| ≈ 0.945). This is notable but
not physically motivated without further analysis.

**Status**: Provisional. Second newform at N=50 k=4.

---

### 2.3 Form k=6, N=54, a₁₃₉ = +53009

**LMFDB URL**: https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/54/6/

**Provisional label**: `54.6.a.b` (second newform with trivial character;
SageMath index [1] = second newform)

**Key data**:
- Level N = 54 = 2 × 3³
- Weight k = 6
- Character: trivial (χ=1)
- Confirmed a₁₃₉ = +53009 (from SageMath 2026-03-06)
- Ramanujan bound: 2 × 139^{5/2} ≈ 456,096; observed 53009 ≪ bound ✓
- SageMath index: `CuspForms(Gamma0(54), 6).newforms('a')[1]`

**Status**: Provisional. Second newform at N=54 k=6.

---

## 3. Summary Table

| Set | N | k | LMFDB label (provisional) | a_p at resonance | Resonant p |
|-----|---|---|---------------------------|-----------------|-----------|
| A | 76 | 2 | `76.2.a.a` | −11 | 137 |
| A | 7 | 4 | `7.4.a.a` | +2274 | 137 |
| A | 208 | 6 | `208.6.a.?` | −38286 | 137 |
| B | 195 | 2 | `195.2.a.c` | +15 | 139 |
| B | 50 | 4 | `50.4.a.b` | +3100 | 139 |
| B | 54 | 6 | `54.6.a.b` | +53009 | 139 |

---

## 4. Open Questions for LMFDB Verification

1. **7.4.a.a**: Is this the unique newform at (N=7, k=4)? Does it have CM?
   What is its L-function, and does it factor into Hecke Grössencharacters?

2. **76.2.a.a**: Does this correspond to an elliptic curve of conductor 76?
   Which Cremona label? Is a₁₃₇ = −11 confirmed?

3. **208.6.a.?**: Which index newform has a₁₃₇ = −38286? Is it a₁ or higher?

4. **195.2.a.c**: Does this correspond to an elliptic curve? What is the
   Cremona label for conductor 195?

5. **For all forms**: Are any of the six forms related by a Shimura
   correspondence (weight k ↔ weight k+2 via θ-series lift)?

6. **N=7, k=4 and Klein quartic**: Although X₀(7) has genus 0, the modular
   curve X₁(7) has genus 0 and X(7) (Klein quartic) has genus 3. Is there
   any geometric connection between the form 7.4.a.a and the Klein quartic?

---

## 5. How to Verify

To verify these labels using SageMath (requires internet or LMFDB download):

```sage
# Verify Set A form N=7 k=4
f = CuspForms(Gamma0(7), 4).newforms('a')[0]
print(f"a_137 = {f[137]}")   # should give +2274
print(f"a_139 = {f[139]}")   # Set A blind to 139

# Or using ModularSymbols
M = ModularSymbols(7, 4)
S = M.cuspidal_subspace()
N = S.new_subspace()
forms = N.newforms('a')
```

LMFDB direct lookup:
- https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/7/4/a/a
- https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/76/2/
- https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/208/6/

---

*Document generated: 2026-03-07.  
Labels are provisional pending LMFDB verification.  
Hecke eigenvalues from SageMath via `CuspForms(Gamma0(N), k).newforms('a')`.*
