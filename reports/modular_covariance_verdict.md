<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Modular Covariance Verdict for `S[Theta]`

**Task**: `prove_or_kill_modular_covariance_of_ubt_action`  
**Date**: 2026-05-09  
**Companion file**: `research_tracks/alpha_spectral/modular_covariance_of_STheta.tex`

---

## Verdict

> **NO-GO**
>
> For the current UBT action implementation used in this repository, full
> modular covariance under \(\mathrm{SL}(2,\mathbb{Z})\) is not derived.
> The key block is missing proof that both \(\nabla^\dagger\nabla\) and the
> measure \(d^4x\,d\psi\) transform with compensating modular weights.
> Therefore equal-action Hecke saddle degeneracy is not derivable from
> \(S[\Theta]\) at this stage.

---

## Requirement-by-requirement outcome

| Requirement | Outcome |
|---|---|
| Define \(\tau=t+i\psi\) as torus modulus | **PROVED (formal setup)** |
| Define \(\mathrm{SL}(2,\mathbb{Z})\) action on \(\tau\) | **PROVED** |
| Compute induced transformation of \(\Theta\) modes | **PROVED (lattice relabelling law)** |
| Check covariance of \(\nabla^\dagger\nabla\) | **NO-GO (not derived from current action)** |
| Check transformation of \(d^4x\,d\psi\) | **NO-GO (Jacobian appears; cancellation unproved)** |
| Determine equal-action Hecke saddles | **NO-GO (blocked by missing modular covariance)** |

---

## Hard-rule compliance

- No \(\alpha\) input used.
- No fixed-prime input used.
- No \(\eta(i)\) fitting used.
- Final verdict class used from allowed set: **NO-GO**.

