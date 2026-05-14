<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# GR Off-Shell Closure: Precise Gap Statement

**Status**: OPEN [L2]  
**Date**: 2026-03-14  
**Related files**:
- `canonical/gr_closure/step2_theta_only_closure.tex` — on-shell closure (GAP-01, GAP-10)
- `canonical/geometry/gr_completion_attempt.tex` — rank obstruction and multi-step GR recovery chain

---

## 1. What Is Being Claimed

The **Θ-only closure** asks: can the pure-Θ action
```
Ŝ[Θ] := S_total[g[Θ], Θ]
```
reproduce the Einstein field equations **G_μν = 8πG T_μν** by varying with
respect to Θ alone, without treating g as an independent variable?

The **on-shell result** (proved, Level 2 recovery) says:

> At Θ satisfying its own Euler–Lagrange equation, and **assuming** the
> gauge-reduced local rank condition (non-degeneracy of J = δg^μν/δΘ on the
> metric-generating sector), the condition δŜ/δΘ = 0 is equivalent to the
> Einstein equations evaluated on g = g[Θ].

This is documented as **GR-compatible sector recovered (Level 2)** in
`canonical/gr_closure/step2_theta_only_closure.tex`.

---

## 2. What Needs Proving for Off-Shell Closure

The **off-shell gap** (GAP-01, GAP-10) is:

> **Claim that needs proving**: Global non-degeneracy of the induced variation
> map J = δg^μν/δΘ for *all* field configurations Θ (not only on-shell
> solutions in the admissible class A_UBT).

Concretely:

- **On-shell**: For Θ ∈ A_UBT (satisfying the E-L equation, with non-degenerate
  first derivatives), injectivity of Θ → g[Θ] is **proved** via the Gram
  matrix det(G_μν) ≠ 0 (step2_nondegeneracy.tex + Prop. 1.5 in step2_theta_only_closure.tex).
- **Off-shell**: For arbitrary Θ not restricted to A_UBT, global injectivity
  is **not proved**. Degenerate configurations (e.g. ∂_μΘ = 0 along a
  codimension-1 surface) are excluded from A_UBT but may arise in the full
  off-shell path integral.

The lemma required is:

> **Missing Lemma (rank of J = δg/δΘ off-shell)**: Show that the kernel of
> J = δg^μν/δΘ consists only of gauge directions (i.e., configurations that
> do not change the physical metric g[Θ]) for all Θ in the full field space,
> not just on-shell solutions.

---

## 3. Why On-Shell Is Insufficient

The on-shell proof proceeds via the chain rule:

```
δŜ/δΘ = [δS_total/δΘ]_{g fixed}  +  [δS_total/δg^μν]_{g=g[Θ]} · J
```

- **Term A** vanishes when Θ satisfies its own E-L equation.
- **Term B** = 0 then requires J to be non-degenerate on the physical sector,
  so that [δS_total/δg^μν] = 0, which gives G_μν = 8πG T_μν.

**Why on-shell is not enough for a path integral or quantum treatment**:

1. In a path integral over all Θ, off-shell configurations contribute.
   Without global rank control, saddle-point approximations may miss
   degenerate directions where J has a non-trivial kernel.
2. Canonical quantisation requires the constraint analysis on the full
   phase space (Dirac constraint machinery), not just on-shell.
3. A rigorous variational principle (e.g., in Sobolev spaces) requires
   well-posedness of δŜ/δΘ = 0 as a PDE, which depends on J being
   non-degenerate as an operator on the relevant function space.

---

## 4. Known Obstructions (from gr_completion_attempt.tex)

From `canonical/geometry/gr_completion_attempt.tex`:

### 4.1 Rank Obstruction for Direct Identification

The object Re(∇†∇Θ) is a **rank-0 spacetime tensor** (a scalar), whereas
G_μν is a rank-(2,0) tensor. The conjectured direct identity

```
Re(∇†∇Θ) =? G_μν
```

**fails by dimensional inconsistency** (Proposition 2 in gr_completion_attempt.tex).

This means that recovering G_μν requires the multi-step chain:

```
Θ → E_μ = ∂_μΘ·𝒩 → 𝒢_μν = Sc(E_μ E_ν†) → Ω_μ → ℛ_μνρσ → ℰ_μν → G_μν = Re(ℰ_μν)
```

Off-shell closure requires this full chain to remain well-defined and
non-degenerate at each step for general Θ.

### 4.2 Topology-Dependent Obstruction

Global injectivity of Θ → g[Θ] requires Θ to be a **global section** of a
non-trivial fibre bundle over the spacetime manifold M⁴. Whether such global
sections exist depends on:

- The topology of M⁴ (e.g., compact vs non-compact, presence of non-trivial
  second cohomology H²(M⁴, ℤ)).
- The structure of the Θ-bundle (a principal bundle with structure group
  derived from the ℂ⊗ℍ automorphism group).

Controlling the kernel of J = δg/δΘ globally requires methods from global
analysis, e.g., sheaf cohomology of the Θ-bundle.

### 4.3 Non-Perturbative Existence

Even if the chain (Section 4.1 above) is well-defined perturbatively, the
non-perturbative existence and uniqueness of solutions to the self-consistency
loop requires a fixed-point theorem in an appropriate Banach or Sobolev space.
This is listed as an open problem in gr_completion_attempt.tex §4.

---

## 5. Precise Gap Statement

**The gap (GAP-10, canonical name)** is:

> Prove (or disprove) that the induced variation map
> J = δg^μν/δΘ : T_Θ(Field space) → Γ(Sym²(T*M))
> has its kernel consisting **only** of gauge directions for all Θ in the
> full off-shell field space — not only for on-shell configurations in A_UBT.

Equivalently:

> Provide a global rank argument showing that for generic off-shell Θ,
> any variation δΘ with J·δΘ = 0 is a gauge transformation (pure phase
> rotation or diffeomorphism) of Θ.

---

## 6. What Must Not Be Attempted

Per AGENTS.md §13 and the task specification: **do not attempt to prove this gap here**.

The purpose of this document is to record the gap with precision, so that:
1. Future work can target the exact missing lemma.
2. The DERIVATION_INDEX entry for "Θ-only closure (off-shell)" correctly
   reflects OPEN [L2] status.
3. No future agent mistakes the on-shell result for an unconditional proof.

---

## 7. Cross-References

| File | Relevance |
|------|-----------|
| `canonical/gr_closure/step2_theta_only_closure.tex` | On-shell closure proof + GAP-01, GAP-10 statements |
| `canonical/geometry/gr_completion_attempt.tex` | Rank obstruction (Prop. 2) + multi-step chain |
| `canonical/gr_closure/step2_nondegeneracy.tex` | det(G_μν) ≠ 0 on-shell for A_UBT class |
| `DERIVATION_INDEX.md` §GR Recovery | Status table: "Θ-only closure (on-shell): GR-compatible sector recovered (Level 2)" |
| `AUDITS/followup_gap_backlog_2026_03.md` | GAP-01 and GAP-10 entries |
