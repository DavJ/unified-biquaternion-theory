import BiQuaternion.Operators

def MBQ_dagger_MBQ (f : BQTime → BQ) (τ : BQTime) : BQ :=
  let m := M_BQ f τ
  dagger (M_BQ m τ)

-- Represents (M_BQ)† M_BQ, used to test self-adjointness and real spectrum
