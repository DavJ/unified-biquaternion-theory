import Mathlib

/-!
# Composite kinetic contraction

Formalizes the theorem-critical algebraic step used in the UBT GR closure
audit.  The physical premise `hGram` is explicit: on the Lorentz-real branch,
the pairing of two covariant first jets is `N₀` times the composite metric.
The inverse-metric premise `hInverse` is also explicit.  The conclusion is
only the four-dimensional contraction; no action-selection claim is encoded.
-/

namespace UBT.GR

open scoped BigOperators

theorem compositeKineticCollapse
    {R : Type*} [CommRing R]
    (N₀ : R)
    (gInv g jetGram : Fin 4 → Fin 4 → R)
    (hGram : ∀ μ ν, jetGram μ ν = N₀ * g μ ν)
    (hInverse : ∑ μ, ∑ ν, gInv μ ν * g μ ν = 4) :
    ∑ μ, ∑ ν, gInv μ ν * jetGram μ ν = 4 * N₀ := by
  simp_rw [hGram]
  rw [← Finset.mul_sum]
  rw [← Finset.sum_mul]
  rw [hInverse]
  ring

end UBT.GR
