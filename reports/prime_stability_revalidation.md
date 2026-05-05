<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Prime Stability Revalidation: V vs V\_ren [Numerical]

**Author**: Ing. David Jaroš  
**Date**: 2026-05-05 (updated from 2026-05-04)  
**Status**: Numerical revalidation — [L0]  
**Related files**:
- `canonical/alpha/prime_stability_set.tex` — formal derivation
- `reports/prime_stability_scan.md` — full scan and Gamma sanity check

---

## Purpose

Confirm that the canonical stable set $\mathcal{S} = \{2,127,137,139,151,157\}$
is identical under:

1. **Canonical potential** $V(q;B) = q^2 - B\,q\ln q$
2. **Renormalised potential** $V_{\text{ren}}(q;B) = q^2 - B\,S_{\text{ren}}(q)$,
   where $S_{\text{ren}}(q) = \ln\Gamma(q+1) + q - \tfrac{1}{2}\ln(2\pi q)$

The renormalised entropy satisfies $S_{\text{ren}}(q) = q\ln q + O(q^{-1})$,
so this is a consistency check, not a model change.

**Scope**: Candidates $p \leq 10{,}000$; competition against all primes $q \leq 100{,}000$.

---

## Revalidation Result

**Exhaustive search**, candidates $p \leq 10{,}000$, competition against all
primes $q \leq 100{,}000$.

| Model | Stable set $\mathcal{S}$ |
|-------|:-------------------------|
| $V$ (canonical, $q\ln q$) | $\{2,\;127,\;137,\;139,\;151,\;157\}$ |
| $V_{\text{ren}}$ ($S_{\text{ren}}$) | $\{2,\;127,\;137,\;139,\;151,\;157\}$ |

**The stable sets are identical.**

---

## Stability Margins: V vs V\_ren

For each prime $p \in \mathcal{S}$ with $p > 2$, the stability margins
$\Delta_\pm = B(p) - B_{\text{low}}(p)$ and $\Delta_+ = B_{\text{high}}(p) - B(p)$
are listed for both models.

| $p$ | $B(p)$ | $\Delta_-(V)$ | $\Delta_+(V)$ | $\Delta_-(V_{\text{ren}})$ | $\Delta_+(V_{\text{ren}})$ |
|----:|-------:|--------------:|--------------:|---------------------------:|---------------------------:|
| 127 | 42.6667 | 1.1939 | 1.3623 | 1.1938 | 1.3624 |
| 137 | 46.0000 | 0.5590 | 0.5646 | 0.5590 | 0.5647 |
| 139 | 46.6667 | 0.1020 | 1.5777 | 0.1020 | 1.5777 |
| 151 | 50.6667 | 0.7551 | 0.3530 | 0.7550 | 0.3530 |
| 157 | 52.6667 | 1.6470 | **0.0072** | 1.6470 | **0.0073** |

The margins agree to better than $10^{-4}$ in all cases, consistent with
the $O(p^{-2})$ difference predicted by Stirling's expansion.

**All stable primes remain stable under $S_{\text{ren}}$ within numerical
precision.**

The tightest margin is $\Delta_+(157) = 0.0072$–$0.0073$ (upper bound,
prime 163), confirming 157 as the most constrained element of $\mathcal{S}$.

---

## $S_{\text{ren}}$ vs $p\ln p$ at Stable Primes

| $p$ | $p\ln p$ | $S_{\text{ren}}(p)$ | $S_{\text{ren}} - p\ln p$ | $1/(12p)$ |
|----:|---------:|--------------------:|--------------------------:|----------:|
| 127 | 615.2118 | 615.2124 | $6.56 \times 10^{-4}$ | $6.562 \times 10^{-4}$ |
| 137 | 674.0374 | 674.0380 | $6.08 \times 10^{-4}$ | $6.083 \times 10^{-4}$ |
| 139 | 685.8919 | 685.8925 | $6.00 \times 10^{-4}$ | $5.995 \times 10^{-4}$ |
| 151 | 757.6093 | 757.6098 | $5.52 \times 10^{-4}$ | $5.519 \times 10^{-4}$ |
| 157 | 793.8306 | 793.8311 | $5.31 \times 10^{-4}$ | $5.308 \times 10^{-4}$ |

The difference matches $1/(12p)$ to better than $10^{-8}$ at all primes, confirming
the two-term Stirling approximation.

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

def V(q, B):     return q**2 - B * q * math.log(q)
def S_ren(q):    return math.lgamma(q+1) + q - 0.5*math.log(2*math.pi*q)
def V_ren(q, B): return q**2 - B * S_ren(q)
def B_of(p):     return (p+1)/3.0

def is_stable(p):
    B=B_of(p); Vp=V(p,B)
    return all(V(q,B)>Vp for q in primes if q!=p)

def is_stable_ren(p):
    B=B_of(p); Vp=V_ren(p,B)
    return all(V_ren(q,B)>Vp for q in primes if q!=p)

stable     = [p for p in primes if p<=10_000 and is_stable(p)]
stable_ren = [p for p in primes if p<=10_000 and is_stable_ren(p)]
# Both: [2, 127, 137, 139, 151, 157]  ✓
assert stable == stable_ren
```

---

## Conclusion

The canonical stable set $\mathcal{S} = \{2,127,137,139,151,157\}$ is confirmed
unchanged under the renormalised Gamma entropy $S_{\text{ren}}$.

This validates the canonical model under continuous interpolation.  The model
is not sensitive to the sub-leading $O(q^{-1})$ correction introduced by
$S_{\text{ren}}$.

**The stable sets under $V$ and $V_{\text{ren}}$ are identical** for all
primes up to $100{,}000$ — confirmed by exhaustive numerical scan.

---

## Gamma Entropy Policy (Canonical vs Non-Canonical)

| Entropy | Status | Stable set near |
|---------|--------|----------------|
| $S(q) = q\ln q$ | **Canonical** | $e^5 \approx 148$ |
| $S_{\text{ren}}(q) = \ln\Gamma(q+1) + q - \tfrac{1}{2}\ln(2\pi q)$ | **Canonical** (equivalent to $q\ln q$ up to $O(q^{-1})$) | $e^5 \approx 148$ |
| $S(q) = \ln\Gamma(q+1)$ | **Non-canonical — excluded** | $e^6 \approx 403$ |

> **Warning**: The unrenormalised Gamma entropy $\ln\Gamma(q+1)$ removes the $+1$
> term in the entropy derivative, shifting the stability threshold from
> $\ln p \approx 5$ to $\ln p \approx 6$.  The resulting cluster near $p \approx 400$
> is excluded from the canonical formulation.  See
> `canonical/alpha/prime_stability_set.tex` §Gamma, Non-Canonical Variant.
