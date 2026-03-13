<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->

# The Theta Field Θ(q, τ)

The **Theta field** Θ(q, τ) is the fundamental dynamical object of UBT. All physical
content — geometry, gauge fields, particle spectrum — is encoded in Θ.

**Canonical source**: [`canonical/fields/theta_field.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/fields/theta_field.tex)

---

## Definition

```
Θ(q, τ) : ℍ × ℂ  →  ℂ⊗ℍ
```

- **Domain**: quaternionic coordinate q ∈ ℍ, complex time τ = t + iψ
- **Range**: biquaternion value in ℂ⊗ℍ ≅ Mat(2,ℂ)

The field Θ is a **Mat(2,ℂ)-valued function** on the space of biquaternion coordinates.

---

## Field Equation

The fundamental field equation of UBT is:

```
∇†∇ Θ(q, τ) = κ 𝒯(q, τ)
```

where:
- ∇ is the biquaternionic covariant derivative (see [`canonical/explanation_of_nabla.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/explanation_of_nabla.tex))
- ∇† is its quaternionic conjugate
- 𝒯 is the biquaternionic stress-energy tensor
- κ is the coupling constant

In the real limit ψ → 0, this equation reduces exactly to Einstein's field equations.

---

## Action Functional

The kinetic action for Θ is:

```
S[Θ] = ∫ Tr(∇Θ · ∇†Θ) dq dτ
```

Variation of S[Θ] with respect to Θ yields the field equation above.  
Variation with respect to the emergent metric g_μν yields the Einstein–Hilbert action
(at [L1], with one-loop corrections).

---

## Physical Decomposition

Θ decomposes into sectors corresponding to physical fields:

| Sector | Physical content |
|--------|-----------------|
| Re(Θ) | Gravitational / geometric sector |
| Im(Θ) | Gauge field sector |
| Phase on ψ-circle | U(1)_EM electromagnetic phase |
| ψ-modes (winding n) | Fermion generations (conjecture) |

---

## ψ-Winding Modes

Expanding Θ in a Fourier series on the ψ-circle:

```
Θ(q, τ) = Σ_n  Θ_n(q, t) · e^{inψ/R_ψ}
```

The winding number n plays a central role:
- n = 0 : vacuum / ground state
- n = 137 (= n*) : physical sector, fine structure constant
- n = 139 (= n**) : mirror sector

---

## Canonical Files

| File | Content |
|------|---------|
| [`canonical/fields/theta_field.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/fields/theta_field.tex) | Θ definition, field equation, action |
| [`canonical/fields/biquaternion_time.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/fields/biquaternion_time.tex) | Complex time T_B definition |
| [`canonical/explanation_of_nabla.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/explanation_of_nabla.tex) | Covariant derivative ∇ |
| [`canonical/core_assumptions.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/core_assumptions.tex) | Core assumptions behind the field |

---

## See Also

- [Fundamental Objects](Fundamental_Objects) — the algebra ℂ⊗ℍ
- [Emergent Spacetime](Emergent_Spacetime) — metric extracted from Θ
- [GR Recovery](GR_Recovery) — Einstein equations from ∇†∇Θ = κ𝒯
