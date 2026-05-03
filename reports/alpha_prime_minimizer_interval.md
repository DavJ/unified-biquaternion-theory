<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Alpha Prime Minimizer — Stability Interval Report

**Author**: Ing. David Jaroš  
**Date**: 2026-05-03  
**Status**: Computational verification — [L0]  
**Companion files**:
- `canonical/alpha/modular_prime_attractor_theorem.tex` — formal theorem
- `reports/alpha_old_formula_cleanup.md` — removed erroneous formulas

---

## 1. Purpose

Find the interval $[B_{\mathrm{low}},\, B_{\mathrm{high}}]$ such that $q = 137$
is the unique discrete prime minimiser of

$$V(q;\,B) = q^2 - B\,q\ln q$$

over all primes $q$, and verify that $B = 46 = \mu(\Gamma_0(137))/3$ lies inside
that interval.

---

## 2. Condition for q = 137 to be the Prime Minimiser

$V(137;\,B) < V(q;\,B)$ for all primes $q \neq 137$ iff

$$137^2 - q^2 < B\,(137\ln 137 - q\ln q)  \quad \forall\; q \text{ prime}, q \neq 137.$$

Note: $f(x) = x\ln x$ is strictly increasing for $x > e^{-1}$, so:
- For $q < 137$: both $137^2 - q^2 > 0$ and $137\ln 137 - q\ln q > 0$
  → lower bound: $B > (137^2 - q^2)/(137\ln 137 - q\ln q) =: B_{\min}(q)$
- For $q > 137$: both $137^2 - q^2 < 0$ and $137\ln 137 - q\ln q < 0$
  → upper bound: $B < (137^2 - q^2)/(137\ln 137 - q\ln q) =: B_{\max}(q)$

Therefore:
$$B \in (B_{\mathrm{low}},\, B_{\mathrm{high}}) \;\text{ where }\;
  B_{\mathrm{low}} = \max_{q < 137,\, q\text{ prime}} B_{\min}(q), \quad
  B_{\mathrm{high}} = \min_{q > 137,\, q\text{ prime}} B_{\max}(q).$$

---

## 3. Numerical Results

### 3.1 Tightest lower bounds (q < 137)

| Prime q | B_min(q) | Note |
|---------|----------|------|
| 131 | **45.441010** | tightest — sets B_low |
| 127 | 44.878400 | |
| 113 | 42.905392 | |
| 109 | 42.340670 | |
| 107 | 42.058161 | |

### 3.2 Tightest upper bounds (q > 137)

| Prime q | B_max(q) | Note |
|---------|----------|------|
| 139 | **46.564636** | tightest — sets B_high |
| 149 | 47.820... | |
| 151 | 47.983... | |

### 3.3 Stability interval

$$\boxed{B_{\mathrm{low}} = 45.441, \quad B_{\mathrm{high}} = 46.565}$$

The interval is set by the nearest primes: 131 (below) and 139 (above).

---

## 4. Verification: B = 46 Lies Inside the Interval

$$45.441 < 46 < 46.565 \quad \checkmark$$

B = 46 lies **1.232 units above B_low** and **0.565 units below B_high**.

### 4.1 V-differences at B = 46

| Prime q | V(q;46) − V(137;46) |
|---------|---------------------|
| 113 | +432.758 |
| 127 | +65.979 |
| 131 | +19.781 |
| **137** | **0** (minimum) |
| 139 | +6.693 |
| 149 | +140.672 |

All non-137 primes have V(q;46) > V(137;46). ✓

### 4.2 V-differences at B = 46.284 (exact stationarity value)

| Prime q | V(q;46.284) − V(137;46.284) |
|---------|-----------------------------|
| 113 | +472.473 |
| 127 | +82.685 |
| 131 | +29.831 |
| **137** | **0** (minimum) |
| 139 | +3.327 |
| 149 | +120.351 |

B = 46.284 also lies inside the interval (45.441 < 46.284 < 46.565). ✓

---

## 5. Physical B Values and Interval Membership

| B value | Source | In interval? |
|---------|--------|-------------|
| 8π ≈ 25.133 | B₀ one-loop baseline [L1] | No |
| N_eff^{3/2} ≈ 41.569 | B_base conjectural [MC] | No |
| **μ(Γ₀(137))/3 = 46** | Modular invariant [L0] | **Yes ✓** |
| 46.284 | Exact stationarity constraint [PHENOM] | Yes ✓ |
| 46.298 | B_phenom back-solved [PHENOM] | Yes ✓ |

---

## 6. Conclusion

- **B = 46** (the modular value $\mu(\Gamma_0(137))/3$) lies inside the prime-stability
  interval $(45.441,\, 46.565)$ for the discrete prime minimiser at $q = 137$.
- This is a **[L0] computational proof**: every prime in the interval gives
  $V(137;\,46) < V(q;\,46)$.
- The closeness of B = 46 to B_high = 46.565 (margin 0.565) means 139 is the
  nearest competitor. The next serious competitor is 131 on the lower side
  (margin 0.559 from B_low).
- The identification $B = \mu(\Gamma_0(137))/3$ from $S[\Theta]$ is Gap G-Bmod
  (**[Open]**).

---

## 7. Computation Code

```python
import math

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True

primes = [p for p in range(2, 10000) if is_prime(p)]
ln137 = math.log(137)

thresholds_below, thresholds_above = [], []
for q in primes:
    if q == 137: continue
    lnq = math.log(q)
    num = 137**2 - q**2
    den = 137 * ln137 - q * lnq
    if abs(den) < 1e-12: continue
    threshold = num / den
    if q < 137:
        thresholds_below.append((q, threshold))
    else:
        thresholds_above.append((q, threshold))

B_low = max(t for q, t in thresholds_below)   # 45.441010 (q=131)
B_high = min(t for q, t in thresholds_above)  # 46.564636 (q=139)
```
