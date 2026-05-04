<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Continuous Gamma-Entropy Scan: Stationary Points near $1/\alpha$

**Author**: Ing. David Jaroš  
**Date**: 2026-05-04  
**Status**: Computational verification — [L0]  
**Companion files**:
- `canonical/alpha/prime_stability_set.tex` — formal derivation (Section S9)
- `reports/prime_stability_scan.md` — discrete prime-stability tables
- `reports/continuous_gamma_entropy_Vx.png` — plot of $V(x)$ on $[100, 170]$

---

## 1. Problem Statement

Extend the prime-stability potential from integer primes to real $x > 1$ using
the Gamma-function entropy, and determine whether a continuous stationary point
occurs near $x = 1/\alpha \approx 137.036$.

---

## 2. Model

$$V(x;\,B) = x^2 - B\,\ln\Gamma(x+1)$$

with derivatives

$$V'(x;\,B) = 2x - B\,\psi(x+1), \qquad V''(x;\,B) = 2 - B\,\psi^{(1)}(x+1),$$

where $\psi = (\ln\Gamma)'$ is the digamma function and $\psi^{(1)}$ is the
trigamma function.  The parameter $C$ is set to zero (it does not affect
stationarity).

The stationarity condition $V'(x^*; B) = 0$ gives

$$B = \frac{2x^*}{\psi(x^*+1)} \approx \frac{2x^*}{\ln x^*} \quad (x^* \gg 1).$$

---

## 3. Stationary Points for $B = B(p) = (p+1)/3$

For each prime-stable prime $p$ (original leading-entropy model), the table below
gives the continuous minimum $x^*$ of $V(\,\cdot\,; B(p))$ found by
Newton–Raphson on $V'$.

| $p$ | $B(p)$ | $x^*$ | $V'(x^*)$ | $V''(x^*)$ | Nearest prime to $x^*$ |
|----:|-------:|------:|-----------:|-----------:|:-----------------------|
| 127 | 42.667 |  97.900 | $\approx 0$ | 1.566 | 97  |
| 137 | 46.000 | 107.740 | $\approx 0$ | 1.575 | 107 |
| 139 | 46.667 | 109.726 | $\approx 0$ | 1.577 | 109 |
| 151 | 50.667 | 121.755 | $\approx 0$ | 1.586 | 127 |
| 157 | 52.667 | 127.840 | $\approx 0$ | 1.590 | 127 |

**Observation**: Under $B = B(p)$, the continuous minimum lies at roughly
$0.77$–$0.81 \times p$, well below $p$ itself.  The discrete prime-stability of
$p$ is a **lattice effect**: $p$ wins among neighbouring primes even though it is
not the continuous minimiser.

---

## 4. Coupling Required to Place $x^* = 1/\alpha$

Setting $V'(137.036;\, B^*) = 0$:

$$B^* = \frac{2 \times 137.036}{\psi(138.036)} = \frac{274.072}{4.9239} \approx 55.662$$

Verification:

| Quantity | Value |
|----------|------:|
| $\psi(138.036)$ | 4.923888 |
| $B^* = 274.072 / 4.924$ | **55.6617** |
| $V''(137.036;\, B^*)$ | +1.5953 > 0 (minimum ✓) |
| Newton check $x^*$ | 137.036000 |

The discrepancy from the theory coupling is

$$B^* - B(137) = 55.662 - 46.000 = 9.662.$$

This gap reflects the shift from leading-entropy stationarity
($B^* \approx 2p/(\ln p + 1) \approx 46.28$ at $p = 137$) to
Gamma-entropy stationarity ($B^*_\Gamma \approx 2p/\ln p \approx 55.69$).

---

## 5. $V$-Difference Table at $B = B^* = 55.662$

| $p$ | $V(p;\,55.662) - V(x^*;\,55.662)$ |
|----:|----------------------------------:|
| 113 | +453.35 |
| 127 | +79.83  |
| 131 | +28.95  |
| **137** | **+0.001** ← nearest prime |
| 139 | +3.08   |
| 149 | +114.98 |
| 157 | +321.55 |
| 163 | +545.57 |

The prime $p = 137$ lies within $0.001$ units of the continuous minimum, making
it the unambiguous discrete nearest-prime projection.  The next candidate, 139,
is more than **3000× further** in $V$-units.

---

## 6. Scan of $x^*(B)$ over $B \in [40, 60]$

| $B$ | $x^*(B)$ | Nearest prime | $|x^* - p|$ |
|----:|--------:|:-------------:|------------:|
| 40.000 |  90.138 |  89 | 1.138 |
| 42.667 |  97.900 |  97 | 0.900 |
| 44.000 | 101.818 | 101 | 0.818 |
| 46.000 | 107.740 | 107 | 0.740 |
| 46.667 | 109.726 | 109 | 0.727 |
| 48.000 | 113.714 | 113 | 0.714 |
| 50.000 | 119.737 | 113 | 6.737 |
| 50.667 | 121.756 | 127 | 5.244 |
| 52.000 | 125.807 | 127 | 1.193 |
| 52.667 | 127.841 | 127 | 0.841 |
| 54.000 | 131.922 | 131 | 0.922 |
| 55.000 | 134.996 | 137 | 2.004 |
| **55.662** | **137.036** | **137** | **0.036** |
| 56.000 | 138.081 | 139 | 0.919 |
| 58.000 | 144.282 | 149 | 4.718 |
| 60.000 | 150.523 | 151 | 0.477 |

---

## 7. Stationarity Comparison: Leading vs Gamma Model

| $p$ | $B(p)$ | $B^*_\text{lead} = \tfrac{2p}{\ln p+1}$ | $B^*_\Gamma \approx \tfrac{2p}{\ln p}$ | $x^*_\text{lead}$ | $x^*_\Gamma$ (with $B=B(p)$) |
|----:|-------:|---------------------------------------:|--------------------------------------:|------------------:|---------------------------:|
| 127 | 42.667 | 43.462 | 52.392 | 124.201 | 97.900 |
| 131 | 44.000 | 44.594 | 53.699 | 128.899 | 101.818 |
| 137 | 46.000 | 46.284 | 55.650 | 135.989 | 107.740 |
| 139 | 46.667 | 46.845 | 56.297 | 138.364 | 109.726 |
| 149 | 50.000 | 49.634 | 59.513 | 150.319 | 119.737 |
| 151 | 50.667 | 50.189 | 60.152 | 152.726 | 121.755 |
| 157 | 52.667 | 51.847 | 62.062 | 159.976 | 127.840 |

Under the **leading** model: $x^*_\text{lead} \approx p$ (approximately — it
is the near-fixed-point property that makes $p$ prime-stable).  Under the
**Gamma** model: $x^*_\Gamma \approx 0.79\,p$ for the same $B(p)$.

---

## 8. Plot

![V(x) on [100, 170]](continuous_gamma_entropy_Vx.png)

**Top panel** ($B = 46.0 = B(137)$, original leading model): The continuous
minimum sits at $x^* \approx 107.7$, well below 137.  The dashed orange line
marks $x^*$; the dotted vertical lines mark the original stable primes.

**Bottom panel** ($B = B^* \approx 55.662$): The continuous minimum aligns
exactly with $1/\alpha = 137.036$ (dash-dot grey line).  The prime 137 is
indistinguishable from $x^*$ at plot resolution.

---

## 9. Nearest-Prime Projection

| Model | $B$ | $x^*$ | Projects to |
|-------|----:|------:|:-----------:|
| Leading, $B=B(137)=46$ | 46.000 | 135.99 | **137** |
| Gamma, $B=B(137)=46$ | 46.000 | 107.74 | 107 |
| Gamma, $B=B^*=55.662$ | 55.662 | 137.036 | **137** |

Under both the leading model (with $B = B(137)$) and the exact Gamma model (with
the appropriately shifted coupling $B^*$), the nearest-prime projection of the
continuous minimum at or near $1/\alpha$ is $p = \mathbf{137}$, not 139.

---

## 10. Computation Code

```python
import math

def digamma(x):
    """ψ(x) via asymptotic expansion + downward recurrence."""
    if x < 6:
        return digamma(x + 1) - 1.0 / x
    r = math.log(x) - 0.5/x
    x2 = x*x
    r -= 1/(12*x2) - 1/(120*x2*x2) + 1/(252*x2*x2*x2)
    return r

def trigamma(x):
    """ψ'(x)."""
    if x < 6:
        return trigamma(x + 1) + 1.0/(x*x)
    r = 1/x + 0.5/x**2 + 1/(6*x**3) - 1/(30*x**5) + 1/(42*x**7)
    return r

def V(x, B):    return x*x - B * math.lgamma(x + 1)
def Vp(x, B):   return 2*x - B * digamma(x + 1)
def Vpp(x, B):  return 2 - B * trigamma(x + 1)

def find_xstar(B, x0, tol=1e-12):
    x = x0
    for _ in range(300):
        f = Vp(x, B); fp = Vpp(x, B)
        dx = -f/fp; x += dx
        if x < 1: x = 1.01
        if abs(dx) < tol: break
    return x

alpha_inv = 137.036
B_star = 2*alpha_inv / digamma(alpha_inv + 1)   # ≈ 55.662
xstar = find_xstar(B_star, alpha_inv)
print(f"B* = {B_star:.4f},  x* = {xstar:.6f}")
```

---

## 11. Summary

| Question | Answer |
|----------|--------|
| Does $V(x;\,B)$ have a continuous minimum near $x = 137.036$? | **Yes**, for $B = B^* \approx 55.662$ |
| What is the nearest-prime projection of $x^* = 137.036$? | $p = \mathbf{137}$ |
| Is 137 or 139 the nearer prime? | **137** ($V$-gap ratio $\approx 3000:1$) |
| Does $B^*$ equal $B(137) = 46$? | **No** — they differ by 9.66 |
| Why? | Gamma-entropy stationarity is $B^* \approx 2p/\ln p$; leading-model is $2p/(\ln p+1)$ |
| Is the continuous minimum an independent argument for 137? | Only if $B^*$ can be derived from the theory; it is a **numerical coincidence** under the present ansatz |
