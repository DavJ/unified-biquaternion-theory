structure BQ where
  a b c d : ℂ
deriving Repr

def conjH (q : BQ) : BQ := ⟨q.a, -q.b, -q.c, -q.d⟩
def conjC (q : BQ) : BQ := ⟨conj q.a, conj q.b, conj q.c, conj q.d⟩
def dagger (q : BQ) : BQ := conjC (conjH q)
def Scal (q : BQ) : ℂ := (q.a + conj q.a) / 2
def norm2 (q : BQ) : ℝ := realPart ((dagger q).a * q.a + (dagger q).b * q.b)

structure BQTime where
  t x y z : ℝ
  u v w r : ℝ
deriving Repr

namespace BQTime
  def toBQ (τ : BQTime) : BQ :=
    ⟨τ.t + Complex.I * τ.u,
     τ.x + Complex.I * τ.v,
     τ.y + Complex.I * τ.w,
     τ.z + Complex.I * τ.r⟩
  def projC (τ : BQTime) : ℂ := τ.t + Complex.I * τ.u
end BQTime
