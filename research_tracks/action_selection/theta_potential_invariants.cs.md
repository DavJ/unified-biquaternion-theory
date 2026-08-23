<!-- BILINGUAL-UNIT: theta-potential.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Lokální polynomiální invarianty potenciálu Theta

<!-- BILINGUAL-UNIT: theta-potential.scope -->
## Rozsah a předpoklady

Tato poznámka klasifikuje reálné polynomiální členy bez derivací, které může
obsahovat lokální potenciál již deklarované rodiny akce. Používá obecnou
realizaci hodnoty pole

\[
 X=\rho(\Theta)=
 \begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{Mat}(2,\mathbb C)
\]

a právě toto souvislé působení

\[
 X\longmapsto e^{i\alpha}SXS^\dagger,
 \qquad S\in SL(2,\mathbb C),\quad e^{i\alpha}\in U(1).
\]

První faktor je deklarovaná skalární fáze a druhý je deklarovaný gravitační
spinový lift. Výsledek se týká reálných polynomů v osmi reálných složkách
obecného `X`, celkového stupně nejvýše čtyři, bez derivací a bez explicitní
závislosti na souřadnicích. Pro hodnotu pole nepředpokládá klasický Lorentzův
reálný řez.

<!-- BILINGUAL-UNIT: theta-potential.theorem -->
## Klasifikační věta [L1, exaktní s počítačovou podporou]

Nechť maticová operace sharp je adjungované zobrazení

\[
 X^\sharp=\begin{pmatrix}d&-b\\-c&a\end{pmatrix},
\]

a definujme reálnou kvadratickou formu

\[
 H(X):=\operatorname{Tr}(X^\sharp X^\dagger)
 =2\operatorname{Re}(a\bar d)-|b|^2-|c|^2.
\]

Pro výše uvedené působení grupy platí:

1. prostor reálných homogenních kvadratických invariantů je jednorozměrný a
   je generován `H`;
2. prostor reálných homogenních kvartických invariantů je dvourozměrný a je
   generován `H^2` a `|det X|^2`;
3. homogenní invarianty lichého stupně jsou nulové.

Každý invariantní reálný lokální polynomiální potenciál stupně nejvýše čtyři
má proto jednoznačně tvar

\[
 \boxed{V(X)=V_0+m^2H(X)+\lambda_1H(X)^2
                 +\lambda_2|\det X|^2,}
 \qquad V_0,m^2,\lambda_1,\lambda_2\in\mathbb R.
\]

„Jednoznačný tvar“ znamená jednoznačný rozvoj v bázi po zafixování normalizace
`H`. Neurčuje čtyři reálné koeficienty.

<!-- BILINGUAL-UNIT: theta-potential.proof -->
## Důkaz a exaktní certifikát hodnosti

Pro infinitezimální spinovou transformaci pišme

\[
 \delta_A X=AX+XA^\dagger,
 \qquad
 A\in\left\{\frac{\sigma_i}{2},\frac{i\sigma_i}{2}\right\}_{i=1}^3,
\]

a přidejme fázový generátor `delta X=iX`. Realifikací získáme sedm racionálních
generátorů `8 x 8`. Jejich indukované derivace působí lineárně na každý prostor
homogenních monomů.

Monomů druhého stupně je 36. Složená matice infinitezimálních podmínek má
exaktní racionální hodnost 35, takže její jádro má rozměr jedna. Přímý rozvoj
ukazuje, že v tomto jádře leží `H`.

Monomů čtvrtého stupně je 330. Po vynásobení všech generátorů dvěma je matice
podmínek celočíselná. Má hodnost 328 nad oběma konečnými tělesy s prvočísly
`1000003` a `1000033`. Nenulový minor řádu 328 modulo kterékoli z těchto
prvočísel je nenulovým celočíselným minorem, takže racionální hodnost je
alespoň 328. Dva explicitně ověřené nezávislé prvky jádra `H^2` a `|det X|^2`
dávají racionální hodnost nejvýše 328. Hodnost v charakteristice nula je tedy
přesně 328 a rozměr jádra je přesně dva.

Grupy `SL(2,C)` a `U(1)` jsou souvislé, takže anulování všemi sedmi generátory
Lieovy algebry je zde ekvivalentní invarianci vůči uvedené souvislé grupě.
Nakonec fázový prvek s `alpha=pi` posílá `X` na `-X`, což vylučuje všechny liché
homogenní stupně.

Konečná invariance plyne také analyticky. Protože `det S=1`,

\[
 (SXS^\dagger)^\sharp=(S^\dagger)^{-1}X^\sharp S^{-1}.
\]

Cykličnost stopy dokazuje invarianci `H`; multiplikativita determinantu
dokazuje Lorentzovu invarianci `det X` a fázový náboj `det X` je dva, takže
`|det X|^2` je fázově neutrální.

<!-- BILINGUAL-UNIT: theta-potential.counterexample -->
## Proč dřívější kladný hmotový člen není přípustný

Kladný Hilbertův–Schmidtův výraz není kvadratickým invariantem. Vezměme

\[
 S=\operatorname{diag}(2,1/2),\qquad X=I_2.
\]

Potom `det S=1`, ale

\[
 \operatorname{Tr}(X^\dagger X)=2,
 \qquad
 \operatorname{Tr}[(SXS^\dagger)^\dagger(SXS^\dagger)]
 =16+\frac1{16}=\frac{257}{16}.
\]

Výraz `Tr(X^dagger X)` tedy selhává při neunitárním Lorentzově boostu.
Přípustná kvadratická forma `H` je indefinitní; samotná symetrie nedokazuje
stabilitu.

<!-- BILINGUAL-UNIT: theta-potential.verification -->
## Záznam ověření

| Tvrzení | Nástroj a artefakt | Výsledek | Omezení | Stav Leanu |
|---|---|---|---|---|
| Rozměry prostorů invariantů stupně dva a čtyři | SymPy 1.14.0 a exaktní eliminace nad konečnými tělesy, `tools/verify_theta_potential_invariants.py` | PASS: rozměry `1` a `2` | Pouze uvedená reprezentace pole, grupa a omezení stupně | `LEAN-PENDING` pro certifikát úplnosti s 330 monomy |
| Invariance při konečných transformacích a Hilbertův–Schmidtův protipříklad | Pythonová standardní knihovna `Fraction`, `tools/verify_theta_potential_invariants_independent.py` | PASS s exaktními racionálními a komplexně racionálními reprezentanty | Namátkové kontroly nedokazují úplnost | `PARTIAL` |
| Spinová a fázová invariance `H`, spinová invariance determinantu, fázová invariance normy determinantu a boostový protipříklad | Lean 4.33.1 s mathlibem, `formal/lean/UBT/Action/PotentialInvariants.lean` | PASS; modul i kořenový cíl `UBT` se kompilují | Nedokazuje rozměry prostorů invariantů | `PROVED` pro zakódovaná tvrzení |

Oba skripty výslovně uvádějí vyloučenou fyziku. První je exaktní klasifikace,
nikoli numerický vzorek; druhý používá nezávislou implementaci matic a nepoužívá
SymPy. Lean kontroluje identity kandidátů bez `sorry` a nových axiomů; úplnost
klasifikace s 330 monomy zůstává výslovně `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: theta-potential.consequence -->
## Důsledek pro program jediné akce

Tento výsledek odstraňuje neomezenou funkci `V[Theta]` z renormalizovatelného
ansatzu bez derivací a nahrazuje ji třemi nekonstantními koeficienty. Nevybírá
`m^2`, `lambda_1` ani `lambda_2`, nefixuje normalizaci nebo znaménko kinetického
členu, neodvozuje mikroskopickou míru ani koeficient Einsteinova–Hilbertova
členu. Proto zužuje `UBT-FUND-GR-ACTION`, ale neuzavírá jej a nezvyšuje status
obnovení GR.

Dále je nutné zavést a ověřit další deklarovaná působení na vnitřní nosič,
diskrétní involuce, omezenost zdola, vakuum, kalibračně fixovaný Hessián a
fyzikální stabilitu sektoru `psi`. Kterákoli z těchto podmínek může tříparametrovou
nekonstantní rodinu dále zúžit nebo vyloučit.
