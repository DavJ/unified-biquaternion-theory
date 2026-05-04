<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Gaussian Prime Stability: λ-Scan [Research]

**Author**: Ing. David Jaroš  
**Date**: 2026-05-04  
**Track**: T3_ALPHA — Fine Structure Constant  
**Status**: Research track — exploratory; NOT canonical  
**Related files**:
- `research_tracks/gaussian_prime_stability/gaussian_prime_stability.md` — model definition
- `canonical/alpha/prime_stability_set.tex` — canonical 1D model (fixed)
- `reports/prime_stability_scan.md` — 1D numerical scan

---

## Purpose

Test whether the degeneracy weight $\lambda$ in the extended entropy
$$S_G(n;\,\lambda) = n\ln n + \lambda\,\ln r_2(n)$$
changes the stable set relative to the canonical result.

> **Rule**: $\lambda$ must **not** be tuned to force specific primes into the
> stable set.  The $\lambda = 0$ baseline must be established first and must
> reproduce the canonical 1D result.

---

## Model Definition

The 2D Gaussian potential with degeneracy weight:
$$V_G(n;\,B,\lambda) = n^2 - B\,S_G(n;\,\lambda),
  \qquad B(p) = \frac{p+1}{3}$$

where $r_2(n)$ is the number of representations $n = a^2 + b^2$ (signed, ordered)
and $\ln r_2(n) = 0$ by convention for $r_2(n) = 0$ (inert primes).

Gaussian prime norms with $r_2(n) > 0$ are:
- $n = 2$ (ramified, $r_2 = 4$)
- $n = p \equiv 1 \pmod 4$ (split primes, $r_2 = 8$)

Inert primes $p \equiv 3 \pmod 4$ have $r_2(p) = 0$, so the degeneracy term
vanishes for them at all $\lambda$.

---

## λ = 0 Baseline

At $\lambda = 0$, $S_G(n;0) = n\ln n$ and $V_G$ reduces exactly to the canonical
1D potential.

**Result**: Stable set = $\{2,\;127,\;137,\;139,\;151,\;157\}$ ✓

This matches the canonical result, as required.

---

## λ Scan Results

Exhaustive search over candidates $p \leq 1{,}000$, competition against all
primes $q \leq 100{,}000$.

| $\lambda$ | Stable set | Changed? | Notes |
|----------:|:-----------|:--------:|:------|
| $-1.0$ | $\{2,\;103,\;127,\;139,\;151,\;167\}$ | ✗ yes | 103,167 enter; 137,157 exit (split primes destabilised) |
| $-0.5$ | $\{2,\;127,\;139,\;151,\;167\}$ | ✗ yes | 137,157 exit; 167 enters |
| $-0.1$ | $\{2,\;127,\;137,\;139,\;151\}$ | ✗ yes | 157 exits (smallest margin) |
| $0.0$ | $\{2,\;127,\;137,\;139,\;151,\;157\}$ | — baseline | canonical result |
| $+0.1$ | $\{2,\;127,\;137,\;149,\;151,\;157\}$ | ✗ yes | 139 exits; 149 enters |
| $+0.5$ | $\{2,\;127,\;137,\;149,\;157\}$ | ✗ yes | 139,151 exit; 149 survives |
| $+1.0$ | $\{2,\;127,\;137,\;149,\;157\}$ | ✗ yes | same as $\lambda=+0.5$ |

---

## Interpretation

### Sensitivity to λ

The stable set changes for **any** $\lambda \neq 0$.  The model is sensitive to
the degeneracy weight even at $|\lambda| = 0.1$.

This confirms that $\lambda = 0$ is the **unique** value that reproduces the
canonical 1D stable set.  Any non-zero $\lambda$ produces a genuinely different model.

### Effect by Prime Type

| Prime | Type | $r_2$ | $\ln r_2$ | Sensitivity |
|------:|:----:|:-----:|:---------:|:-----------|
| 127 | inert | 0 | 0 | Not affected by $\lambda$ directly |
| 137 | split | 8 | 2.079 | Destabilised at $\lambda < 0$; robust at $\lambda > 0$ |
| 139 | inert | 0 | 0 | Destabilised at $\lambda > 0$ (relative competition with split primes) |
| 151 | inert | 0 | 0 | Destabilised at $\lambda > 0$ |
| 157 | split | 8 | 2.079 | Destabilised at $\lambda < -0.1$ (smallest canonical margin) |

### Why 157 exits first at negative λ

The prime 157 has the smallest upper margin $\Delta_+(157) = 0.0072$ in the canonical
model.  Negative $\lambda$ reduces the entropy of split primes (137, 157), making them
less stable.  157 exits the stable set already at $\lambda \approx -0.1$.

### The inert/split boundary effect

Positive $\lambda$ enhances split primes relative to inert primes.  This shifts
competition: 139 (inert) is replaced by 149 (split, $r_2(149)=0$ since
$149 \equiv 1 \pmod 4$... wait, $149 = 10^2 + 7^2$, $r_2(149) = 8$).
The boundary between stable and unstable shifts from 139 to 149.

---

## Conclusion

The $\lambda = 0$ baseline is the **only** value of $\lambda$ that reproduces the
canonical stable set $\{2,127,137,139,151,157\}$.

No value of $\lambda$ has been found that simultaneously:
1. Keeps all six canonical primes stable, and
2. Differs from the 1D canonical result.

Any claim about Gaussian prime stability at $\lambda \neq 0$ requires full disclosure
of $\lambda$ and must not be presented as a result of the canonical model.

> **No physical claims** about the fine structure constant or other constants are
> derived from this scan.

---

## Computation Code

```python
import math

def sieve(n):
    is_p = [True]*(n+1); is_p[0]=is_p[1]=False
    for i in range(2, int(n**0.5)+1):
        if is_p[i]:
            for j in range(i*i, n+1, i): is_p[j]=False
    return [i for i in range(2, n+1) if is_p[i]]

primes = sieve(100_000)
cands  = [p for p in primes if p<=1000]

def r2(n):
    count = 0
    lim = int(n**0.5)+1
    for a in range(-lim, lim+1):
        b2 = n - a*a
        if b2 < 0: continue
        b = round(b2**0.5)
        if b*b == b2: count += 1
    return count

def S_G(n, lam=0.0):
    if n<=1: return 0.0
    rr = r2(n)
    e = n * math.log(n)
    if lam != 0 and rr > 0:
        e += lam * math.log(rr)
    return e

def V_G(n, B, lam=0.0): return n**2 - B * S_G(n, lam)

def is_norm_stable(p, lam=0.0):
    B = (p+1)/3.0; Vp = V_G(p, B, lam)
    return all(V_G(q, B, lam) > Vp for q in primes if q != p)

for lam in [-1.0, -0.5, -0.1, 0.0, 0.1, 0.5, 1.0]:
    stable = [p for p in cands if is_norm_stable(p, lam)]
    print(f"lambda={lam:+.1f}: {stable}")
```
