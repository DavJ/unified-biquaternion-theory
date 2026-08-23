import Mathlib.Algebra.Ring.Basic

/-!
# Curvature-coefficient underdetermination

This file formalizes the logical core of the no-go result.  If the complete
set of encoded kinematic assumptions admits a model whose Einstein--Hilbert
coefficient is zero, those assumptions alone cannot imply that the coefficient
is nonzero.  The theorem does not assert that the zero-coefficient model is
physical; establishing its compatibility with the UBT kinematic definitions
is a separate, explicit premise.
-/

namespace UBT.GR

theorem kinematicsDoNotForceNonzeroCurvatureCoefficient
    {Model R : Type*} [Zero R]
    (Kinematics : Model → Prop)
    (curvatureCoefficient : Model → R)
    (zeroModel : Model)
    (hKinematics : Kinematics zeroModel)
    (hZero : curvatureCoefficient zeroModel = 0) :
    ¬ ∀ model, Kinematics model → curvatureCoefficient model ≠ 0 := by
  intro hForced
  exact hForced zeroModel hKinematics hZero

end UBT.GR
