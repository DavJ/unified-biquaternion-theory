<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# alpha_missing_lemma.md — Exact Statement of the Missing Lemma

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T3_ALPHA — Fine Structure Constant  
**Purpose**: State the single missing lemma for the primary alpha route with
maximal precision.  This is what must be proved to complete the integer-137 result.  
**Gap ID**: G137-B  
**Sources**: `canonical/alpha/prime_137_status.md`,
`canonical/alpha/alpha_best_route.tex`, `reports/gamma0_137_invariants.md`

---

## The Single Missing Lemma

### Informal Statement

The effective coupling parameter B in the V_eff winding-mode potential of UBT
takes the value B ≈ 46.298 (= B_phenom), which is determined by the modular
geometry of the imaginary-time circle at winding level n* = 137.

### Formal Statement (Gap G137-B)

**Lemma G137-B** (not yet proved):

Let $S[\Theta]$ be the UBT action evaluated on the winding-mode sector at
level $n$, with imaginary-time circle $S^1_\psi$ of radius $R_\psi$.
Let the effective potential be
$$
V_\mathrm{eff}(n) = n^2 - B \cdot n \cdot \ln n,
$$
where $B$ is the effective coupling arising from the one-loop contribution
to the UBT path integral over $S^1_\psi$ at level $n$.

**Claim**: At the V_eff minimum $n^* = 137$ (selected by $N_\mathrm{eff} = 12$ [L0]),
$$
B \;=\; \frac{\mu(\Gamma_0(n^*))} {3} + \varepsilon,
\qquad
\frac{\mu(\Gamma_0(137))}{3} = \frac{138}{3} = 46.
$$
where $\mu(\Gamma_0(p)) = p + 1$ is the index of $\Gamma_0(p)$ in $\mathrm{SL}(2,\mathbb{Z})$,
and $\varepsilon$ is a small correction ($\varepsilon \approx 0.298$, error 0.64%)
arising from elliptic-point contributions.

Equivalently: the modular volume of the congruence subgroup $\Gamma_0(137)$,
evaluated at the prime $p = n^*$, equals the effective coupling $B$ up to a
small correction from the elliptic elements of $\Gamma_0(137)$.

---

## Current Status

| Component | Status |
|-----------|--------|
| $N_\mathrm{eff} = 12$ derived from $\mathbb{C}\otimes\mathbb{H}$ | **[L0] Proved** |
| $n^*(B_\mathrm{phenom}) = 137$ for $B = B_\mathrm{phenom}$ | **[L1] Proved** (given B) |
| $B_0 = 8\pi$ (one-loop UBT) | **[L1] Proved** |
| $B_\mathrm{phenom} = 46.298$ | **Numerical** (inverse: V_eff minimum at 137 requires this B) |
| **B_phenom derived from S[Θ] or from modular geometry of Γ₀(137)** | **[L2] OPEN — this is the gap** |
| $\mu(\Gamma_0(137)) = 138$ (numerical, exact) | **[STD]** (modular curve formula) |
| $\mu(\Gamma_0(137))/3 \approx B_\mathrm{phenom}$ (error 0.64%) | **Observation** — not yet derived |

---

## Why This Gap Is Hard

### Known sub-obstacles

1. **B₀ ≠ B_phenom**: The one-loop UBT calculation gives $B_0 = 8\pi \approx 25.1$.
   This produces $n^* \approx 65$, not 137.  The ratio $B_\mathrm{phenom}/B_0 \approx 1.84$
   must come from higher-loop or non-perturbative contributions.

2. **Non-perturbative origin**: The modular index $\mu(\Gamma_0(137))$ counts cosets
   in $\mathrm{SL}(2,\mathbb{Z})$, which is a global (non-perturbative) object.
   Standard perturbative loop expansion does not produce $\mu(\Gamma_0(p))$ naturally.

3. **Why p specifically**: The modular formula $\mu(\Gamma_0(p)) = p + 1$ holds for
   all primes.  The specific value $B \approx (p+1)/3$ at $p = n^*$ requires a
   self-consistency argument: $n^*(B) = p$ and $B \approx (p+1)/3$ must both hold
   simultaneously.  This is a fixed-point equation.

4. **R_ψ calibration**: $B$ depends on $R_\psi$ (radius of $S^1_\psi$), which must
   be derived from UBT or expressed purely in terms of $n^*$.  If $R_\psi$ is an
   independent free parameter, the route fails the "no free parameters" criterion.

---

## Candidate Strategies (Ranked by Plausibility)

### Strategy 1: Modular Bootstrap (highest priority)

**Idea**: The self-consistency equation $n^*(B) = p$, $B \approx (p+1)/3$
constitutes a bootstrap.  Show that the only consistent solution with
$p$ prime and $B > 0$ is $(p,B) = (137, 46)$.

**Formulation**: Solve the fixed-point system
$$
2n = B(\ln n + 1), \qquad B = \frac{n+1}{3},
$$
and verify that the unique prime solution is $n = 137$, $B = \frac{138}{3} = 46$.

**Checking**: Numerically, $2 \times 137 = 274$ and $46 \times (\ln 137 + 1) = 46 \times (4.919 + 1) = 272.3$.
Discrepancy: $274 - 272.3 = 1.7$ (0.6%) — exactly the gap.  This is the
elliptic correction $\varepsilon$.

**Remaining question**: Derive the relation $B = (n+1)/3$ from $S[\Theta]$.

**Estimated chance**: 30% in 4 weeks if one approaches this as a functional
equation in the Sobolev space of winding fields.

### Strategy 2: Heat Kernel Expansion

**Idea**: The one-loop effective action on $S^1_\psi$ involves the heat kernel
of the Laplacian.  The modular index $\mu(\Gamma_0(p))$ may appear as the
degree of a Hecke operator in the spectral expansion of this heat kernel.

**Status**: Preliminary calculation shows $B_\mathrm{base} = 12^{3/2} \approx 41.6$
from a heat-kernel argument, closer to B_phenom than B₀ but still 10% off.
A further correction $R = B_\mathrm{phenom}/B_\mathrm{base} \approx 1.114$ is unexplained.

**Estimated chance**: 20% in 4 weeks.

### Strategy 3: Renormalisation Group at Prime Scales

**Idea**: The renormalization group running of the winding-mode effective coupling
from the UV scale to the IR scale $n = n^*$ produces a multiplicative factor.
If this factor is $\approx 1.84$ (ratio $B_\mathrm{phenom}/B_0$), the gap is closed.

**Status**: No successful calculation yet.  The factor 1.84 has no known
RG interpretation in standard QFT.

**Estimated chance**: 10%.

### Strategy 4: Accept the gap; publish conditional result

**Idea**: State explicitly that $B = B_\mathrm{phenom}$ is a numerical fact, gap G137-B
is open, and the integer-137 result is conditional.  This is honest and publishable.

**Estimated chance of publication**: 90% (this is the fallback).

---

## What "Solving the Lemma" Means

Proof of Gap G137-B consists of showing, from axioms A1–A3 and S[Θ] alone
(no experimental inputs), that:

$$
B \;=\; \frac{\mu(\Gamma_0(n^*))}{3} + \varepsilon_\mathrm{elliptic},
$$

where $\varepsilon_\mathrm{elliptic}$ is the contribution from the two elliptic
fixed points of $\Gamma_0(137)$ (order-2 points, contributing $\nu_2/4 = 0.5$),
giving $B = 46.5$ (error reduced to 0.44% vs. B_phenom = 46.298).

Alternatively: derive $B = B_\mathrm{phenom}$ numerically from a well-defined
UBT integral over $S^1_\psi$ without any numerical fitting.

---

## Success Probability Estimate

Based on 27+ previous failed approaches and the current state of three viable
strategies:

| Strategy | Probability in 4 weeks | Probability in 3 months |
|----------|------------------------|-------------------------|
| Modular bootstrap | 30% | 45% |
| Heat kernel expansion | 20% | 30% |
| RG at prime scales | 10% | 15% |
| **Any strategy** | **~45% (non-overlapping)** | **~65%** |

**Recommendation**: Time-box modular bootstrap for 4 weeks.  If unsuccessful,
publish conditional integer-137 result and refocus on T1_GR + T2_GAUGE.

---

## Definition of Failure

Gap G137-B is considered **definitively failed** if:
1. All three strategies fail within 3 months.
2. A proof is found that $B$ cannot be expressed as $\mu(\Gamma_0(n))/3 + \varepsilon$
   for any $\varepsilon$ derived from the elliptic structure of $\Gamma_0(n)$.

In that case: the integer-137 result remains structural but the route to 137.036
is unknown, and the T3_ALPHA track is downgraded to "strong structural evidence,
not a derivation."

---

## References

- `canonical/alpha/primary_route.md` — primary route decision
- `canonical/alpha/alpha_best_route.tex` — V_eff derivation chain
- `canonical/alpha/prime_137_status.md` — prime 137 structural roles
- `reports/gamma0_137_invariants.md` — modular curve Γ₀(137) analysis
- `ALPHA_STRUCTURAL_ORIGINS.md` — N_eff derivation and exponent origins
- `research_tracks/alpha/layer2_coding_alpha_scan.py` — failed coding route (archive)
