<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# B_eff candidate scan report

Reference evaluation value: B_required(137) = 46.283932910083

## Prime scan for B_required(n)

| prime n | B_required(n) |
|---:|---:|
| 2 | 2.362464436599 |
| 3 | 2.859032148243 |
| 5 | 3.832242933373 |
| 7 | 4.752351324934 |
| 11 | 6.474596252604 |
| 13 | 7.293231233589 |
| 17 | 8.869842857226 |
| 19 | 9.633816165165 |
| 23 | 11.123217104939 |
| 29 | 13.280529246900 |
| 31 | 13.982900071810 |
| 37 | 16.048865193864 |
| 41 | 17.396572883489 |
| 43 | 18.062672836735 |
| 47 | 19.380853474822 |
| 53 | 21.326715179641 |
| 59 | 23.239611977973 |
| 61 | 23.870673243417 |
| 67 | 25.745996891490 |
| 71 | 26.982450636886 |
| 73 | 27.596847045917 |
| 79 | 29.425744385879 |
| 83 | 30.633859161895 |
| 89 | 32.430641785928 |
| 97 | 34.800010394814 |
| 101 | 35.974294655680 |
| 103 | 36.558989869843 |
| 107 | 37.723683587978 |
| 109 | 38.303755895979 |
| 113 | 39.459524508122 |
| 127 | 43.461989878547 |
| 131 | 44.594246897098 |
| 137 | 46.283932910083 |
| 139 | 46.844927306529 |
| 149 | 49.634021494313 |
| 151 | 50.188790980320 |
| 157 | 51.847301132115 |
| 163 | 53.497434134540 |
| 167 | 54.593059463730 |
| 173 | 56.230067222784 |
| 179 | 57.859653694466 |
| 181 | 58.401254074018 |
| 191 | 61.097775776474 |
| 193 | 61.634854728060 |
| 197 | 62.706863729077 |
| 199 | 63.241811907216 |

## Candidate comparison

| candidate | expression | value | n_star(B) | |value-B_required(137)| | forbidden-input flag | free choices |
|---|---|---:|---:|---:|---|---|
| B0_one_loop | `2*pi*N_eff/3 with N_eff=12` | 25.132741228718 | 65.028843 | 21.151191681365 | NO | None once N_eff=12 is accepted |
| B_base_Neff_3_2 | `N_eff^(3/2) with N_eff=12` | 41.569219381653 | 120.351560 | 4.714713528430 | NO | Normalization/exponent justification still debated |
| B_modular_index_over_3_at_N137 | `mu(Gamma0(137))/3 = (137+1)/3` | 46.000000000000 | 135.989243 | 0.283932910083 | YES | Requires externally selecting N=137 |
| B_modular_plus_elliptic_at_N137 | `mu(Gamma0(137))/3 + 1/2` | 46.500000000000 | 137.769839 | 0.216067089917 | YES | Requires N=137 and ad hoc +1/2 |

## Interpretation

- Non-forbidden canonical baselines (8π and N_eff^(3/2)) stay below target.
- Near-target modular values in this scan require explicit N=137 insertion and are flagged.
- Therefore this scan does not close Gap G137-B without additional first-principles input.
