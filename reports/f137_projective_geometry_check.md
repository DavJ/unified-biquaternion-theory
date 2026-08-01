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


# Finite Projective Line P¹(𝔽₁₃₇) — Geometry Check

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Workstream**: G137_2 (finite-field geometry) + G137_4 (polytope sanity check)  
**Status**: Research document  
**Companion files**:
- `reports/gamma0_137_invariants.md` — Γ₀(137) modular structure
- `reports/prime_137_structural_audit.md` — cross-workstream summary

---

## 1. Purpose

Workstream G137_2 asks whether the projective line P¹(𝔽₁₃₇) with 138 points
has a UBT-invariant interpretation — specifically whether
138 = 137 + 1 connects to UBT phase compactification or mode counting.
The test criterion is strict: only accept a connection if a *geometric invariant map*
exists (not a raw number coincidence).

Workstream G137_4 asks for a sanity check on the polytope/root-system route
to 137, with explicit rejection criteria.

---

## 2. P¹(𝔽₁₃₇): Definition and Cardinality

The finite projective line over 𝔽_q is:

```
P¹(𝔽_q) = { [x : y] : (x, y) ∈ 𝔽_q², (x,y) ≠ (0,0) } / ∼
```

where [x:y] ∼ [λx:λy] for λ ∈ 𝔽_q*.  Its cardinality is:

```
|P¹(𝔽_q)| = q + 1
```

For q = p = 137 (prime field):

```
|P¹(𝔽₁₃₇)| = 137 + 1 = 138
```

The 138 points are: [1:0], [1:1], [1:2], …, [1:136], and [0:1],
i.e., the 137 affine points plus the point at infinity.

---

## 3. Exact Algebraic Identity: μ(Γ₀(137)) = |P¹(𝔽₁₃₇)|

For any prime p, the index of Γ₀(p) in SL(2,ℤ) is:

```
μ(Γ₀(p)) = [SL(2,ℤ) : Γ₀(p)] = p + 1 = |P¹(𝔽_p)|
```

This is an **exact algebraic identity**, not a coincidence.  The cosets of
Γ₀(p) in SL(2,ℤ) are naturally parametrised by the points of P¹(𝔽_p):
a matrix [[a,b],[c,d]] ∈ SL(2,ℤ) maps to [c : d] mod p.
Two matrices are in the same Γ₀(p) right-coset iff their (c,d) rows are
proportional mod p, i.e., iff they represent the same element of P¹(𝔽_p).

**Consequence**: The modular curve X₀(p) is a quotient of the upper half-plane
that parametrises pairs of elliptic curves related by cyclic p-isogenies, and
its degree over X(1) equals |P¹(𝔽_p)| = p + 1.

For p = 137: μ = 138 = |P¹(𝔽₁₃₇)|.  This is structural — it holds for
every prime p, not specifically for p = 137.

---

## 4. The 138 = p + 1 Structure in UBT Context

### 4.1 Mode Counting on S¹_ψ

The UBT winding-number spectrum on the S¹_ψ circle counts modes
n ∈ {−N/2, …, N/2} for compactification radius R_ψ.  The total number
of modes at cutoff N is N + 1 (including n = 0).  For n* = 137:

```
Mode count including zero mode = n* + 1 = 138 = |P¹(𝔽₁₃₇)|
```

This is a coincidence of the form "count of {0, 1, 2, …, 137} = 138."
It holds for *any* integer n*, not just primes.  **Classification**: raw
counting coincidence — **rejected** by the task criterion.

### 4.2 Phase Compactification Periodicity

In the ψ-direction, the UBT field satisfies Θ(q, τ + R_ψ) = Θ(q, τ)
(or a twisted version with a gauge factor).  The number of independent
phase-space cells at winding number n* in P¹(𝔽_{n*}) is n* + 1.

This would require n* to be prime for the P¹(𝔽_{n*}) interpretation to
be non-trivial (the structure collapses for composite n*).  Since n* = 137
is prime, the identification P¹(𝔽_{137}) is well-defined.

However, the requirement "n* must be prime for the phase space to be
irreducible" is **not derived from UBT axioms**.  It is a post-hoc
constraint imposed after knowing n* = 137 is prime.  **Classification**:
unconfirmed conjecture — requires derivation from S[Θ].

### 4.3 Projective Space as Phase Space of Spinor Modes

A more structural candidate: if the biquaternion phase space at winding
number n is identified with a projective space over 𝔽_p (with p = n for
prime n), then P¹(𝔽_{137}) counts the elementary charge sectors at level n = 137.

This would produce:
```
Number of charge sectors at n = 137 ↔ |P¹(𝔽₁₃₇)| = 138
```

**Assessment**: No derivation of such a 𝔽_p structure from the UBT field
equations exists.  The biquaternion algebra ℬ = ℂ⊗ℍ is defined over ℂ,
not over finite fields.  A reduction modulo a prime would require a
specific arithmetic structure (e.g., an integral form of ℬ and a prime ideal).

**Classification**: SPECULATIVE — no invariant map identified.

### 4.4 The Exact Identity at the Level of the Index

What *is* invariant and exact (without any fitting or post-hoc constraint):

```
μ(Γ₀(p)) / 3 ≈ B_phenom  at  p = 137
```

The factor 3 comes from the normalised SL(2,ℤ) fundamental domain volume π/3.
The identity is:

```
B_phenom = 2n* / (ln n* + 1) = 274 / (ln 137 + 1) ≈ 46.298
μ(Γ₀(137)) / 3 = 138 / 3 = 46.000  (error: 0.64%)
```

If UBT can derive B = (p+1)/3 from first principles at the prime p = n*, this
would constitute an invariant connection between the finite-field projective line
cardinality and the theta-spectrum coefficient.

**Current status**: MOTIVATED COINCIDENCE [MC] — not yet derived.

---

## 5. Test: Does 138 Relate to Mode Counting in UBT?

| Candidate interpretation | Formula | Invariant? | UBT derivation? | Verdict |
|--------------------------|---------|------------|-----------------|---------|
| n* + 1 = 138 | Trivial counting | For any n* | No | REJECTED (raw count) |
| Γ₀(p) coset count | [SL₂(ℤ):Γ₀(p)] = p+1 | Yes (exact, all p) | No direct S[Θ] link | [MC] |
| Phase-space cells at prime n* | P¹(𝔽_{n*}) | Only if n* prime | Not derived | SPECULATIVE |
| Normalised vol = B_phenom/factor | (p+1)/3 ≈ B | For specific p | Not derived | [MC] |

**Finding**: No invariant map between P¹(𝔽₁₃₇) and UBT phase structure is
established.  The strongest candidate is the index relation
μ(Γ₀(137))/3 ≈ B_phenom, which is documented in
`reports/gamma0_137_invariants.md` §4.

---

## 6. Workstream G137_4: Polytope and Root-System Check

### 6.1 Criterion

Accept only non-arbitrary polytope or root-system links.  Reject raw
orbit-count coincidences.  Classify the dodecahedron/A₅ route as speculative
unless a representation-theoretic link to UBT appears.

### 6.2 Root Systems

The positive root counts for classical root systems are:

| System | Positive roots | Equals 137? |
|--------|---------------|-------------|
| A_n | n(n+1)/2 | n(n+1) = 274: no integer solution |
| B_n / C_n | n² | √137 ≈ 11.70: not integer |
| D_n | n(n−1) | n²−n−137 = 0: n ≈ 12.2, not integer |
| G₂ | 6 | No |
| F₄ | 24 | No |
| E₆ | 36 | No |
| E₇ | 63 | No |
| E₈ | 120 | No |

**Result**: 137 does not appear as a root-system orbit count in any classical
or exceptional Lie algebra.  **REJECTED** as root-system orbit count.

### 6.3 Exceptional and Finite Groups

| Object | Relevant count | Equals 137? |
|--------|---------------|-------------|
| \|A₅\| = 60 | Icosahedral rotations | No |
| \|S₅\| = 120 | Icosahedral full symmetry | No |
| \|A₅\| × 2 = 120 | Binary icosahedral group | No |
| Regular 4D polytopes (120-cell, 600-cell) | |Sym| = 14400 | No |
| Monster group | Orders in 10^{53} range | No |
| Mathieu group M₁₂ | 95040 | No |
| Mathieu group M₁₁ | 7920 | No |

**Dodecahedron/A₅ specific check**: The icosahedral group A₅ ≅ PSL(2, 𝔽₅)
has order 60.  The number 137 is prime and does not divide any known
icosahedral-symmetry orbit count.  No representation of A₅ over ℂ has
dimension 137 (all dimensions are 1, 3, 4, 5 — the irrep dimensions of A₅).

**Result**: The dodecahedron/A₅ route is **CLASSIFIED AS SPECULATIVE** with
no representation-theoretic link to UBT or to 137.

### 6.4 Would Any Polytope Connection Be Invariant?

A non-arbitrary polytope connection to 137 would require:
1. A specific polytope whose combinatorial invariant (vertex count, face
   count, root count, Euler characteristic) equals 137 for a structural reason.
2. A map from UBT geometry (biquaternion phase space) to that polytope.
3. The number 137 appearing as a *derived consequence*, not as a fitting target.

No such structure has been found.  The search space (polytopes, root systems,
Mathieu groups, exceptional Lie algebras) has been checked; 137 does not appear.

**Classification**: Polytope/root-system route → **REJECTED** (no non-arbitrary link).

---

## 7. Finite-Field Geometry: What Remains Open

The following questions could produce an invariant 𝔽₁₃₇ connection if answered
affirmatively, but remain unanswered:

| Question | Status |
|----------|--------|
| Does the UBT field equation reduce to a system over 𝔽_p at primes p? | Open — no arith reduction known |
| Is there a mod-137 reduction of the biquaternion spectrum with special properties? | Open |
| Does P¹(𝔽₁₃₇) appear as the space of eigenvalues of a UBT Hecke operator? | Open — would be structural if true |
| Do supersingular elliptic curves over 𝔽₁₃₇ connect to UBT phase space? | Open |

---

## 8. Verdict

| Workstream | Claim tested | Result |
|------------|-------------|--------|
| G137_2 | P¹(𝔽₁₃₇) ↔ UBT phase compactification | **No invariant map found** — μ/3 ≈ B_phenom is [MC] |
| G137_4 | Polytope/root-system origin of 137 | **REJECTED** — no non-arbitrary link |
| G137_4 | Dodecahedron/A₅ route | **CLASSIFIED SPECULATIVE** — no rep-theoretic connection |

The only non-trivial structural result is the exact identity
μ(Γ₀(p)) = |P¹(𝔽_p)| = p + 1, which holds for all primes and connects
the modular index to the projective line cardinality.  At p = 137, the
normalised form (p+1)/3 ≈ B_phenom is a motivated coincidence, documented
for further investigation in `reports/gamma0_137_invariants.md`.

---

## References (Internal)

- `reports/gamma0_137_invariants.md` — Γ₀(137) analysis
- `reports/prime_137_structural_audit.md` — full audit
- `canonical/alpha/alpha_best_route.tex` — V_eff derivation
- Diamond & Shurman, *A First Course in Modular Forms*, §3.1 (index formula)
