<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Operator Formalism

The biquaternionic covariant derivative ∇ is the central differential operator
in UBT. The field equation ∇†∇Θ = κ𝒯 governs all physical dynamics.

**Canonical file**: [`canonical/explanation_of_nabla.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/explanation_of_nabla.tex)

---

## The Covariant Derivative ∇

The biquaternionic covariant derivative acts on the field Θ as:

```
∇Θ = ∂_μ Θ + [A_μ, Θ]
```

where A_μ is the biquaternionic gauge connection (encodes both gravitational and
gauge field degrees of freedom).

The **quaternionic conjugate** ∇† reverses the order of quaternion multiplication:

```
∇†Θ = ∂_μ Θ† - [A_μ, Θ†]
```

File: [`canonical/explanation_of_nabla.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/explanation_of_nabla.tex)

---

## The Wave Operator ∇†∇

The second-order operator ∇†∇ is the biquaternionic generalisation of the
covariant wave operator □ = ∇^μ∇_μ in GR.

In the real limit:

```
∇†∇  →  □ = g^{μν} ∇_μ ∇_ν
```

The field equation:

```
∇†∇ Θ(q,τ) = κ 𝒯(q,τ)
```

reduces to Einstein's equations in the ψ → 0 limit.

---

## Spectral Theory

The eigenvalue problem for ∇†∇:

```
∇†∇ Θ_n = λ_n Θ_n
```

gives a spectrum of eigenvalues λ_n. The winding modes Θ_n correspond to the
fermion generations (ψ-modes), and the spectrum is related to the lepton
mass ratios via the Hecke eigenvalue conjecture.

---

## Action Principle

The kinetic part of the UBT action:

```
S_kin[Θ] = ∫ Tr(∇Θ · (∇Θ)†) √|g| d⁴x dψ
```

Variation δS/δΘ† = 0 gives the field equation ∇†∇Θ = κ𝒯.

---

## Comparison with Standard Physics

| Operator | Physics | UBT generalization |
|----------|---------|-------------------|
| ∂_μ (partial derivative) | Flat spacetime | ∇ (with gauge connection) |
| □ = ∂^μ∂_μ | Klein-Gordon | ∇†∇ (biquaternionic) |
| G_μν (Einstein tensor) | GR LHS | Emergent from ∇†∇Θ |
| D̸ (Dirac operator) | QFT fermions | Related to ∇ on spinor sector |

---

## See Also

- [Theta Field](Theta_Field) — field equation and action
- [Emergent Spacetime](Emergent_Spacetime) — metric from ∇Θ
- [GR Recovery](GR_Recovery) — how ∇†∇Θ = κ𝒯 reduces to Einstein
