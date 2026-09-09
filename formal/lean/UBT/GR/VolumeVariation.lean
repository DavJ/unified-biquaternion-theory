import Mathlib

/-!
# Four-dimensional volume: first-jet principal symbol

The covariant tetrad is retained. At a fixed field value a value-dependent
connection contributes an arbitrary additive first-jet shift. The theorems
use the actual matrix determinant and real derivatives. No zero-symbol
hypothesis is assumed.

This module does not identify physical quantum modes, select the microscopic
action, or prove a statement about Riemann zeta zeros.
-/

namespace UBT.GR.VolumeVariation

open scoped BigOperators

abbrev Vec := Fin 4 → ℝ
abbrev Mat := Matrix (Fin 4) (Fin 4) ℝ

/-- Coordinate expansion, subsequently identified with Matrix.det. -/
def detFour (e : Mat) : ℝ :=
  e 0 0 * (e 1 1 * e 2 2 * e 3 3 + e 1 2 * e 2 3 * e 3 1
    + e 1 3 * e 2 1 * e 3 2 - e 1 3 * e 2 2 * e 3 1
    - e 1 2 * e 2 1 * e 3 3 - e 1 1 * e 2 3 * e 3 2)
  - e 0 1 * (e 1 0 * e 2 2 * e 3 3 + e 1 2 * e 2 3 * e 3 0
    + e 1 3 * e 2 0 * e 3 2 - e 1 3 * e 2 2 * e 3 0
    - e 1 2 * e 2 0 * e 3 3 - e 1 0 * e 2 3 * e 3 2)
  + e 0 2 * (e 1 0 * e 2 1 * e 3 3 + e 1 1 * e 2 3 * e 3 0
    + e 1 3 * e 2 0 * e 3 1 - e 1 3 * e 2 1 * e 3 0
    - e 1 1 * e 2 0 * e 3 3 - e 1 0 * e 2 3 * e 3 1)
  - e 0 3 * (e 1 0 * e 2 1 * e 3 2 + e 1 1 * e 2 2 * e 3 0
    + e 1 2 * e 2 0 * e 3 1 - e 1 2 * e 2 1 * e 3 0
    - e 1 1 * e 2 0 * e 3 2 - e 1 0 * e 2 2 * e 3 1)

theorem detFour_eq_det (e : Mat) : detFour e = e.det := by
  rw [Matrix.det_succ_row_zero]
  norm_num [detFour, Fin.sum_univ_succ, Matrix.det_fin_three,
    Matrix.submatrix, Fin.succAbove]
  <;> ring

/-- A first-jet increment with one spacetime covector and one field vector. -/
def rankOne (k v : Vec) : Mat := fun μ a => k μ * v a

set_option maxHeartbeats 4000000 in
theorem det_rankOne_affine (e : Mat) (k v : Vec) (t : ℝ) :
    (e + t • rankOne k v).det =
      e.det + t * ((e + rankOne k v).det - e.det) := by
  simp only [← detFour_eq_det, detFour, rankOne,
    Matrix.add_apply, Matrix.smul_apply, smul_eq_mul]
  ring

set_option maxHeartbeats 8000000 in
theorem det_common_covector_affine (e : Mat) (k u v : Vec) (s t : ℝ) :
    (e + s • rankOne k u + t • rankOne k v).det =
      e.det + s * ((e + rankOne k u).det - e.det)
        + t * ((e + rankOne k v).det - e.det) := by
  simp only [← detFour_eq_det, detFour, rankOne,
    Matrix.add_apply, Matrix.smul_apply, smul_eq_mul]
  ring

/-- invScale = N0^(-1/2); shift x is the connection contribution at x.
There is no independent tetrad and no assumption that shift is constant
as a function of the field. The field is held fixed only for a first-jet
partial derivative, as required by the definition of the principal symbol. -/
def density (invScale : ℝ) (weight : Vec → ℝ) (shift : Vec → Mat)
    (x : Vec) (p : Mat) : ℝ :=
  weight x * (invScale • (p + shift x)).det

theorem density_rankOne_affine (c : ℝ) (f : Vec → ℝ) (b : Vec → Mat)
    (x : Vec) (p : Mat) (k v : Vec) (t : ℝ) :
    density c f b x (p + t • rankOne k v) =
      density c f b x p +
        t * (density c f b x (p + rankOne k v) - density c f b x p) := by
  have h := det_rankOne_affine (p + b x) k v t
  simp only [density, Matrix.det_smul, Fintype.card_fin]
  rw [show p + t • rankOne k v + b x = p + b x + t • rankOne k v by abel,
    show p + rankOne k v + b x = p + b x + rankOne k v by abel, h]
  ring

theorem density_common_covector_affine (c : ℝ) (f : Vec → ℝ) (b : Vec → Mat)
    (x : Vec) (p : Mat) (k u v : Vec) (s t : ℝ) :
    density c f b x (p + s • rankOne k u + t • rankOne k v) =
      density c f b x p
        + s * (density c f b x (p + rankOne k u) - density c f b x p)
        + t * (density c f b x (p + rankOne k v) - density c f b x p) := by
  have h := det_common_covector_affine (p + b x) k u v s t
  simp only [density, Matrix.det_smul, Fintype.card_fin]
  rw [show p + s • rankOne k u + t • rankOne k v + b x =
      p + b x + s • rankOne k u + t • rankOne k v by abel,
    show p + rankOne k u + b x = p + b x + rankOne k u by abel,
    show p + rankOne k v + b x = p + b x + rankOne k v by abel, h]
  ring

theorem hasDerivAt_density_rankOne (c : ℝ) (f : Vec → ℝ) (b : Vec → Mat)
    (x : Vec) (p : Mat) (k v : Vec) (t : ℝ) :
    HasDerivAt (fun r => density c f b x (p + r • rankOne k v))
      (density c f b x (p + rankOne k v) - density c f b x p) t := by
  simp_rw [density_rankOne_affine]
  simpa using ((hasDerivAt_id t).mul_const
    (density c f b x (p + rankOne k v) - density c f b x p)).const_add
      (density c f b x p)

/-- The second directional derivative is zero at every first jet. -/
theorem secondDeriv_density_rankOne (c : ℝ) (f : Vec → ℝ) (b : Vec → Mat)
    (x : Vec) (p : Mat) (k v : Vec) (t : ℝ) :
    deriv (fun s => deriv (fun r => density c f b x (p + r • rankOne k v)) s) t = 0 := by
  have h : (fun s => deriv (fun r => density c f b x (p + r • rankOne k v)) s) =
      (fun _ => density c f b x (p + rankOne k v) - density c f b x p) := by
    funext s
    exact (hasDerivAt_density_rankOne c f b x p k v s).deriv
  rw [h]
  simp

/-- Every mixed field block contracted with the same spacetime covector is
zero. This is stronger than checking a selected matrix or numerical jet. -/
theorem mixedSecondDeriv_density_common_covector
    (c : ℝ) (f : Vec → ℝ) (b : Vec → Mat)
    (x : Vec) (p : Mat) (k u v : Vec) :
    deriv (fun s => deriv
      (fun t => density c f b x (p + s • rankOne k u + t • rankOne k v)) 0) 0 = 0 := by
  have h : (fun s => deriv
      (fun t => density c f b x (p + s • rankOne k u + t • rankOne k v)) 0) =
      (fun _ => density c f b x (p + rankOne k v) - density c f b x p) := by
    funext s
    simp_rw [density_common_covector_affine]
    exact (by
      simpa using ((hasDerivAt_id (0 : ℝ)).mul_const
        (density c f b x (p + rankOne k v) - density c f b x p)).const_add
        (density c f b x p +
          s * (density c f b x (p + rankOne k u) - density c f b x p))
      : HasDerivAt _ _ 0).deriv
  rw [h]
  simp

end UBT.GR.VolumeVariation
