<!-- BILINGUAL-UNIT: theta-potential-stability.provenance -->
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

# Hranice stability klasifikovaného potenciálu Theta

<!-- BILINGUAL-UNIT: theta-potential-stability.scope -->
## Rozsah

Pro přesnou invariantní rodinu již klasifikovanou v
`theta_potential_invariants.cs.md` pišme

\[
V(X)=V_0+m^2H(X)+\lambda_1H(X)^2+\lambda_2D(X),
\qquad D(X):=|\det X|^2,
\]

kde

\[
H(X)=2\operatorname{Re}(a\bar d)-|b|^2-|c|^2,
\qquad
X=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]

Tato poznámka přesně určuje, kdy je tento polynom zdola omezený na
`Mat(2,C)` a zda může sám o sobě vybrat izolované vakuum.

<!-- BILINGUAL-UNIT: theta-potential-stability.inequality -->
## Univerzální nerovnost

Pro každou komplexní matici `2 x 2` platí

\[
\boxed{H(X)\le 2|\det X|=2\sqrt{D(X)}.}
\]

Skutečně,

\[
\begin{aligned}
H
&=2\operatorname{Re}(a\bar d)-|b|^2-|c|^2\\
&\le 2|a||d|-2|b||c|\\
&\le 2\bigl||a||d|-|b||c|\bigr|\\
&\le 2|ad-bc|.
\end{aligned}
\]

První krok používá `Re(z) <= |z|`, druhý
`|b|^2+|c|^2 >= 2|b||c|` a poslední obrácenou trojúhelníkovou nerovnost.

<!-- BILINGUAL-UNIT: theta-potential-stability.boundedness -->
## Přesná věta o omezenosti [L1]

Potenciál `V` je zdola omezený na celém `Mat(2,C)` právě tehdy, když platí
jeden z následujících vzájemně slučitelných případů:

1. `lambda1 > 0` a `lambda2 >= 0`, přičemž `m^2` je libovolné reálné;
2. `lambda1 = 0`, `lambda2 > 0` a `m^2 <= 0`;
3. `lambda1 = lambda2 = m^2 = 0`.

### Postačitelnost

Jestliže `lambda1 > 0` a `lambda2 >= 0`, doplnění na čtverec dává

\[
\lambda_1H^2+m^2H
\ge -\frac{(m^2)^2}{4\lambda_1},
\]

takže `V` je zdola omezený.

Jestliže `lambda1 = 0`, `lambda2 > 0` a `m^2=-mu <= 0`, pak pro `H <= 0`

\[
-\mu H+\lambda_2D\ge0.
\]

Pro `H>0` dává univerzální nerovnost `H <= 2 sqrt(D)`. S
`y=sqrt(D)` tedy

\[
-\mu H+\lambda_2D
\ge \lambda_2y^2-2\mu y
\ge -\frac{\mu^2}{\lambda_2}.
\]

Třetí případ je konstantní potenciál.

### Nutnost

Přesné jednoparametrické svědecké rodiny vylučují všechny zbývající volby
znamének:

- `X=t [[0,1],[0,0]]` má `H=-t^2`, `D=0`; tedy `lambda1<0` je neomezený
  a při `lambda1=0` tentýž svědek vylučuje také `m^2>0`;
- `X=t diag(1,i)` má `H=0`, `D=t^4`; tedy `lambda2<0` je neomezený;
- jestliže `lambda1=lambda2=0` a `m^2<0`, pak `X=t I_2` má `H=2t^2`
  a potenciál je neomezený zdola; první svědek řeší `m^2>0`.

Tyto případy pokrývají celý doplněk uvedené oblasti.

<!-- BILINGUAL-UNIT: theta-potential-stability.flat -->
## Přesný nekompaktní plochý směr [L0]

Pro každé reálné `t`

\[
X_t=t\begin{pmatrix}1&0\\0&0\end{pmatrix}
\]

splňuje

\[
H(X_t)=0,
\qquad
D(X_t)=0,
\qquad
V(X_t)=V_0.
\]

Proto **žádný člen úplné invariantní kvartické rodiny potenciálů pro spojenou
symetrii není koercivní na generickém prostoru polí a žádný nemůže sám
bezderivačním potenciálem vybrat izolované vakuum**. Toto tvrzení nezávisí na
koeficientech.

Nejde o důkaz nestability úplné akce UBT: derivované členy, gauge kvocient,
omezení nebo menší fyzický konfigurační prostor mohou plochý směr odstranit.
Je to no-go pro řešení výběru akce pouhým laděním `m^2`, `lambda1` a `lambda2`
uvnitř již klasifikovaného potenciálu.

<!-- BILINGUAL-UNIT: theta-potential-stability.verification -->
## Ověření

`tools/verify_theta_potential_stability.py` vyhodnocuje všechny přesné
svědecké paprsky pomocí racionální aritmetiky a kontroluje logiku případů
koeficientů uvedenou výše. `tests/test_theta_potential_stability.py` udržuje
svědky a plochý směr v CI.

Univerzální nerovnost a důkaz postačitelnosti jsou elementární analytické
nerovnosti explicitně uvedené výše. Úplná formalizace řetězce nerovností pro
komplexní absolutní hodnotu v Leanu je `LEAN-PENDING`; formální důkaz této
části se netvrdí.

<!-- BILINGUAL-UNIT: theta-potential-stability.consequence -->
## Důsledek pro program jediné akce

Klasifikace potenciálu dosáhla své přirozené hranice:

- invariantní báze je přesná;
- omezenost dává přesné oblasti znamének;
- celá rodina si zachovává nekompaktní plochý směr nezávislý na koeficientech.

Další theorem-critical selektor proto není další koeficient potenciálu. Musí
pocházet z derivační/gauge/constraint struktury téže jediné akce. Navržená
mikroskopická akce musí zejména ukázat, jak její kvocient konfiguračního
prostoru a Hessián odstraní nebo učiní gauge plochou orbitu `H=D=0` při
současném zachování GR sektoru s kovariantní tetrádou.
