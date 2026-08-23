import Mathlib

/-!
# Stationarity of a composite metric action

This file formalizes the exact linear-algebra core of the composite variation.
If the differential of the field-to-metric map is surjective and the pullback
of a metric Euler--Lagrange covector vanishes on every field variation, then
that metric Euler--Lagrange covector vanishes.  The theorem does not select an
action and does not prove analytic regularity of the field-to-metric map.
-/

namespace UBT.GR

theorem metricEquationOfCompositeStationarity
    {R V W : Type*}
    (dMetric : V → W)
    (metricEulerLagrange : W → R)
    (hSurjective : Function.Surjective dMetric)
    (zero : R)
    (hCompositeStationary : ∀ v, metricEulerLagrange (dMetric v) = zero) :
    ∀ w, metricEulerLagrange w = zero := by
  intro w
  obtain ⟨v, rfl⟩ := hSurjective w
  exact hCompositeStationary v

theorem nonzeroCoefficientPreservesEquation
    {R : Type*} [Field R]
    (c : R) (hc : c ≠ 0) (equation : R)
    (hScaled : c * equation = 0) : equation = 0 := by
  exact (mul_eq_zero.mp hScaled).resolve_left hc

end UBT.GR
