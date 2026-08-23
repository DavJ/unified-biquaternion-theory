import Mathlib

/-!
# Exact obstructions in the archived Appendix-AA action

This file checks only two finite logical/arithmetic defects in the archived
candidate.  It does not classify all possible microscopic UBT actions.
-/

namespace UBT.GR

/-- Four biquaternionic coordinates (eight real components each), followed by
two real complex-time coordinates, have real coordinate count 34, not 6. -/
theorem archivedMeasureCoordinateCount : 4 * 8 + 2 = 34 := by norm_num

theorem archivedSixFactorMeasureMismatch : 4 * 8 + 2 ≠ 4 + 2 := by norm_num

/-- A nonzero complex number cannot be both real-valued and remain real-valued
after multiplication by `-i`.  This is the algebraic core of the conflict
between a real-valued pairing and the claimed complex sesquilinearity. -/
theorem realAndNegIMulRealForcesZero (z : ℂ)
    (hz : z.im = 0) (hiz : (-Complex.I * z).im = 0) : z = 0 := by
  apply Complex.ext
  · simpa using hiz
  · simpa using hz

end UBT.GR
