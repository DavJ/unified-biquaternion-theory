<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Graded prime-Fock bridge to the Möbius function

**Date:** 2026-08-25  
**Status:** classical finite/infinite Fock identities established; UBT derivation of prime modes, grading, and RH-strength cancellation open.  
**Relation:** extends the existing bosonic prime-Fock construction without changing its claim status.

<a id="gm-scope"></a>
## 1. Question and claim boundary

The existing prime-Fock track uses one bosonic oscillator for every prime and obtains

\[
Z_P^+(s)=\prod_{p\in P}(1-p^{-s})^{-1}.
\]

This note asks for the exact graded partner whose coefficients are the Möbius function. The answer is standard: replace unrestricted bosonic occupation by fermionic occupation \(0/1\) and take a supertrace. This establishes the algebraic mechanism, but it does not derive prime-indexed modes or fermionic parity from canonical UBT.

The construction therefore addresses the algebraic part of GAP-RH-MOEBIUS-UBT. It does not prove RH and does not close the UBT bridge.

<a id="gm-finite-space"></a>
## 2. Finite graded prime-Fock space

Let \(P\) be a finite set of primes. For each \(p\in P\), define

\[
\mathcal F_p^-:=\operatorname{span}\{|0\rangle_p,|1\rangle_p\}\cong\mathbb C^2,
\qquad
N_p|\varepsilon_p\rangle_p=\varepsilon_p|\varepsilon_p\rangle_p,
\quad \varepsilon_p\in\{0,1\}.
\]

The finite fermionic prime-Fock space and its Hamiltonian are

\[
\mathcal F_P^-:=\bigotimes_{p\in P}\mathcal F_p^-,
\qquad
H_P^-:=\sum_{p\in P}(\log p)N_p.
\]

Define total fermion number and parity by

\[
F_P:=\sum_{p\in P}N_p,
\qquad
(-1)^{F_P}|(\varepsilon_p)\rangle
=(-1)^{\sum_p\varepsilon_p}|(\varepsilon_p)\rangle.
\]

Every basis state corresponds to the square-free integer

\[
n=\prod_{p\in P}p^{\varepsilon_p}.
\]

Repeated prime factors are absent because \(\varepsilon_p\le1\).

<a id="gm-supertrace-theorem"></a>
## 3. Graded partition-function theorem

**Theorem GM-1 (finite graded identity; standard).** For every finite \(P\) and every \(s\in\mathbb C\),

\[
\boxed{
Z_P^-(s)
:=\operatorname{Str}_{\mathcal F_P^-}(e^{-sH_P^-})
=\operatorname{Tr}_{\mathcal F_P^-}\!\left((-1)^{F_P}e^{-sH_P^-}\right)
=\prod_{p\in P}(1-p^{-s})
=\sum_{\substack{n\ \mathrm{square\!-\!free}\\p\mid n\Rightarrow p\in P}}
\frac{\mu(n)}{n^s}.
}
\]

**Proof.** The Hamiltonian and parity split into commuting one-prime factors. On \(\mathcal F_p^-\),

\[
\operatorname{Tr}_{\mathcal F_p^-}\!\left((-1)^{N_p}e^{-s(\log p)N_p}\right)
=1-p^{-s}.
\]

Tensor-product trace factorization gives the product. Expanding it selects a subset \(S\subseteq P\); the selected integer \(n=\prod_{p\in S}p\) has coefficient \((-1)^{|S|}=\mu(n)\). \(\square\)

The ordinary fermionic trace is instead

\[
\operatorname{Tr}_{\mathcal F_P^-}(e^{-sH_P^-})
=\prod_{p\in P}(1+p^{-s}).
\]

Thus exclusion alone does not produce \(1/\zeta\); the parity insertion and supertrace are essential.

<a id="gm-boson-fermion-inverse"></a>
## 4. Exact inverse of the bosonic sector

For the same finite prime set, the existing bosonic factor and the new graded factor obey

\[
\boxed{Z_P^+(s)Z_P^-(s)=1.}
\]

In the formal Dirichlet algebra with \(D_mD_n=D_{mn}\),

\[
\prod_{p\in P}(1-D_p)
=\sum_{S\subseteq P}(-1)^{|S|}D_{\prod_{p\in S}p}
=\sum_{\substack{n\ \mathrm{square\!-\!free}\\p\mid n\Rightarrow p\in P}}\mu(n)D_n.
\]

As \(P\) increases through all primes, absolute convergence for \(\Re s>1\) gives the classical identity

\[
\boxed{
Z^-(s)=\prod_p(1-p^{-s})=\frac1{\zeta(s)}
=\sum_{n\ge1}\frac{\mu(n)}{n^s},
\qquad \Re s>1.
}
\]

This is an exact realization of the formal inverse in the preceding residue–Möbius note. It remains a standard arithmetic/Fock construction until its degrees of freedom are derived from UBT.

<a id="gm-theta-revival-interface"></a>
## 5. Interface with theta revivals

The reduced theta bridge at rational time \(t=a/q\) is organized by quadratic Gauss sums. Their Chinese-remainder factorization for \(\gcd(q_1,q_2)=1\),

\[
g(a,q_1q_2)=g(aq_2,q_1)g(aq_1,q_2),
\]

shows that coprime denominator sectors multiply. Prime powers are the local irreducible arithmetic blocks of this factorization.

This observation supplies a candidate interface, not a derivation:

\[
\text{rational theta revivals}
\rightsquigarrow
\text{coprime local factors}
\rightsquigarrow
\text{prime-mode tensor factors}
\rightsquigarrow
\text{graded determinant}.
\]

Two nontrivial UBT steps are missing:

1. obtain the prime-local decomposition without factoring \(q\) or inserting primality externally;
2. derive a canonical \(\mathbb Z_2\) parity whose supertrace, rather than ordinary trace, is physically or geometrically selected.

The existence of spinorial or Clifford-like structure in UBT is not sufficient by itself. The specific Fock grading \((-1)^{F_P}\), its state space, and its coupling to the theta/revival sector must follow from the canonical action or a proved reduction.

<a id="gm-circularity-gate"></a>
## 6. Circularity and falsification gate

The route passes the first noncircularity gate only if all of the following hold:

| Test | Pass condition | Failure meaning |
|---|---|---|
| Prime-mode origin | projectors or local sectors are defined without a primality oracle or prior Euler product | primes were inserted by hand |
| Energy origin | \(\log p\) follows from the derived operator/flow | the desired Dirichlet frequencies were post-selected |
| Grading origin | \((-1)^F\) follows from canonical symmetry, boundary conditions, or an exterior-algebra sector | the Möbius signs were inserted by hand |
| Square-free rule | repeated local occupation is dynamically or algebraically excluded | \(\mu(p^2)=0\) has no UBT origin |
| RH-strength estimate | the derived object yields \(M(x)=O_\varepsilon(x^{1/2+\varepsilon})\) independently of zeta zeros | the construction reproduces \(1/\zeta\) only in \(\Re s>1\) |

Failure of any of the first four tests reduces the proposal to a correct classical repackaging. Passing them would produce a genuine UBT Möbius bridge, but RH would still require the fifth test.

<a id="gm-gap-ladder"></a>
## 7. Theorem and gap ladder

| ID | Statement | Status |
|---|---|---|
| GM-1 | finite prime-fermion supertrace equals the truncated Möbius Dirichlet polynomial | **[STD/PROVED]** |
| GM-2 | infinite graded product equals \(1/\zeta(s)\) for \(\Re s>1\) | **[STD/PROVED]** |
| GM-UBT-1 | derive prime-local factors from canonical theta/revival dynamics | **[OPEN]** |
| GM-UBT-2 | derive the \(0/1\) occupation law and parity insertion from UBT | **[OPEN]** |
| GM-UBT-3 | derive \(\log p\) energies without arithmetic post-selection | **[OPEN]** |
| GM-RH | prove the square-root Mertens bound for the derived coefficients | **[OPEN; equivalent in strength to RH]** |

These are local refinements of GAP-RH-MOEBIUS-UBT; no canonical or global claim status is upgraded.

<a id="gm-verification"></a>
## 8. Verification

| Claim | Artifact | Result | Scope | Limitation | Lean status |
|---|---|---|---|---|---|
| GM-1 coefficient identity | tools/verify_graded_mobius_bridge.py | exact pass by subset enumeration, product expansion, and independent factorization | configurable finite prime sets | finite check supplements but does not replace the analytic proof | LEAN-PENDING — no repository formalization of the graded Fock construction |
| finite Dirichlet inverse | same artifact | exact convolution pass through configurable cutoff | finite arithmetic coefficients | not an analytic-continuation result | LEAN-PENDING |
| \(Z_P^+Z_P^-=1\) | same artifact | floating-point pass for several real \(s>1\) | finite products | does not address the critical strip | LEAN-PENDING |
| approach to \(1/\zeta(2)=6/\pi^2\) | same artifact | deterministic numerical convergence check | one classical benchmark | numerical convergence is not a proof of GM-2 | NOT-APPLICABLE |

No UBT-specific open step is called verified.

<a id="gm-next-experiment"></a>
## 9. Next experiment

The next admissible experiment should start from rational theta-revival data indexed by \(q\), construct candidate local projectors without calling a prime sieve inside the construction, and test whether their tensor decomposition recovers prime-power blocks. Only after that gate passes should the graded determinant be attached.

The decisive negative result is also valuable: if every successful decomposition requires explicit integer factorization, the revival route has not derived the prime modes and should not be promoted.

