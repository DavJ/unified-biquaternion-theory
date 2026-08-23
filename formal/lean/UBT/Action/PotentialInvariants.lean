import Mathlib

/-!
# Exact finite claims for the local Theta-potential audit

This file proves candidate-invariance statements and the explicit
Hilbert--Schmidt counterexample.  It does not formalize the completeness of the
degree-four invariant basis; the exact 330-monomial rank certificate remains
`LEAN-PENDING`.
-/

namespace UBT.Action

open scoped Matrix

/-- Matrix form of the unique quadratic candidate used by the audit.  For a
generic `2 x 2` matrix this is
`2 Re (a * conj d) - normSq b - normSq c`. -/
def hInvariant (X : Matrix (Fin 2) (Fin 2) ℂ) : ℂ :=
  Matrix.trace (X.adjugate * Xᴴ)

/-- The quadratic candidate is invariant under the declared spin lift. -/
theorem hInvariantSpinLiftInvariant
    (S X : Matrix (Fin 2) (Fin 2) ℂ)
    (hS : S.det = 1) :
    hInvariant (S * X * Sᴴ) = hInvariant X := by
  have hAdjS : S.adjugate * S = 1 := by
    rw [Matrix.adjugate_mul, hS, one_smul]
  have hSAdj : Sᴴ * (Sᴴ).adjugate = 1 := by
    rw [Matrix.mul_adjugate, Matrix.det_conjTranspose, hS, star_one, one_smul]
  have hcore :
      ((Sᴴ).adjugate * X.adjugate * S.adjugate) * (S * Xᴴ * Sᴴ) =
        (Sᴴ).adjugate * (X.adjugate * Xᴴ) * Sᴴ := by
    calc
      _ = (Sᴴ).adjugate * X.adjugate * (S.adjugate * S) * Xᴴ * Sᴴ := by
        noncomm_ring
      _ = (Sᴴ).adjugate * (X.adjugate * Xᴴ) * Sᴴ := by
        rw [hAdjS]
        noncomm_ring
  simp only [hInvariant, Matrix.adjugate_mul_distrib,
    Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
  calc
    Matrix.trace ((Sᴴ).adjugate * (X.adjugate * S.adjugate) *
        (S * (Xᴴ * Sᴴ))) =
        Matrix.trace (((Sᴴ).adjugate * X.adjugate * S.adjugate) *
          (S * Xᴴ * Sᴴ)) := by
      congr 1
      noncomm_ring
    _ = Matrix.trace ((Sᴴ).adjugate * (X.adjugate * Xᴴ) * Sᴴ) := by
      rw [hcore]
    _ = Matrix.trace (X.adjugate * Xᴴ) := by
      rw [Matrix.trace_mul_cycle, hSAdj, Matrix.one_mul]

/-- The same quadratic candidate is invariant under a unit phase. -/
theorem hInvariantPhaseInvariant
    (u : ℂ) (X : Matrix (Fin 2) (Fin 2) ℂ)
    (hunit : u * star u = 1) :
    hInvariant (u • X) = hInvariant X := by
  have hunit' : star u * u = 1 := by
    rw [mul_comm, hunit]
  have hunit'' : (starRingEnd ℂ) u * u = 1 := by
    simpa using hunit'
  simp [hInvariant, Matrix.adjugate_smul, smul_smul, hunit'']

/-- The determinant of a generic `2 x 2` complex matrix is invariant under the
declared spin lift `X -> S X Sᴴ` when `det S = 1`. -/
theorem determinantSpinLiftInvariant
    (S X : Matrix (Fin 2) (Fin 2) ℂ)
    (hS : S.det = 1) :
    (S * X * Sᴴ).det = X.det := by
  rw [Matrix.det_mul, Matrix.det_mul, hS, one_mul,
    Matrix.det_conjTranspose, hS]
  simp

/-- A determinant has phase charge two, but its norm square is invariant under
a unit-norm phase. -/
theorem determinantNormPhaseInvariant
    (u determinant : ℂ)
    (hu : Complex.normSq u = 1) :
    Complex.normSq (u ^ 2 * determinant) = Complex.normSq determinant := by
  rw [Complex.normSq_mul, map_pow, hu]
  norm_num

/-- Exact arithmetic core of the nonunitary boost counterexample:
`X=I` has Hilbert--Schmidt norm square `2`, whereas
`diag(2,1/2) X diag(2,1/2)ᴴ` has norm square `257/16`. -/
theorem hilbertSchmidtBoostCounterexample :
    (16 + 1 / 16 : ℚ) = 257 / 16 ∧ (257 / 16 : ℚ) ≠ 2 := by
  norm_num

end UBT.Action
