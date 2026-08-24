<!-- BILINGUAL-UNIT: spectral-underdetermination.provenance -->
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

# Neurčenost spektrální akce z Cliffordova hlavního symbolu

<!-- BILINGUAL-UNIT: spectral-underdetermination.scope -->
## Rozsah

Kanonický generalizovaný Diracův lift určuje exaktní Cliffordův hlavní symbol
prvního řádu,

\[
\sigma_4(\xi)^2=g^{\mu\nu}\xi_\mu\xi_\nu I_4,
\qquad
\det\sigma_4(\xi)=\bigl(g^{\mu\nu}\xi_\mu\xi_\nu\bigr)^2.
\]

Tím je určena metrická kauzální kuželová struktura nesená operátorem.
Spektrální akce však závisí na **úplném** eliptickém/operátoru Laplaceova typu,
nikoli pouze na jeho hlavním symbolu. Tato poznámka dává exaktní
jednoparametrickou protipříkladovou rodinu, která ukazuje, že Cliffordův hlavní
symbol sám nemůže určit koeficienty tepelného jádra generující nízkoenergetickou
gravitační a gauge akci.

<!-- BILINGUAL-UNIT: spectral-underdetermination.family -->
## Přesná jednoparametrická rodina [L0]

Nechť `P0` je libovolná kladná realizace Laplaceova typu s hlavním symbolem
vybraným kanonickou metrikou UBT a nechť `u` je reálná konstanta. Definujme

\[
\boxed{P_u=P_0+uI.}
\]

Přidaný člen je nultého řádu. Každý `P_u` má tedy přesně stejný hlavní symbol
jako `P0`, a tím stejnou metriku a charakteristický kužel. Protože `uI`
komutuje s `P0`, tepelný semigroup splňuje exaktní identitu

\[
\boxed{e^{-tP_u}=e^{-tu}e^{-tP_0}.}
\]

Jestliže ve čtyřech rozměrech

\[
\operatorname{Tr}e^{-tP_0}
\sim a_0t^{-2}+a_2t^{-1}+a_4+a_6t+\cdots,
\]

pak násobení výrazem

\[
e^{-tu}=1-ut+\frac{u^2t^2}{2}-\frac{u^3t^3}{6}+\cdots
\]

dává přesně

\[
\boxed{
\begin{aligned}
a_0(u)&=a_0,\\
a_2(u)&=a_2-u a_0,\\
a_4(u)&=a_4-u a_2+\frac{u^2}{2}a_0.
\end{aligned}}
\]

Operátory se **stejným Cliffordovým hlavním symbolem UBT** tedy mají různé
subleading koeficienty tepelného jádra.

<!-- BILINGUAL-UNIT: spectral-underdetermination.consequence -->
## Důsledek pro spektrální cestu UBT

Kanonický Cliffordův lift a jeho přesná faktorizace hlavního symbolu nestačí k
určení jediné spektrální akce. Minimálně musí být navíc vybrána nebo odvozena
tato data nižšího řádu:

- úplný endomorfismus nultého řádu / hmotový blok generalizovaného Diracova
  operátoru;
- fyzická spinová/gauge konexe a torzní dokončení vstupující do symbolu nižšího
  řádu;
- realizace `psi` a signatura/eukleidovské pokračování potřebné k přípustnému
  spektrálnímu problému;
- fyzický Hilbertův prostor/kvocient módů a hraniční podmínky;
- spektrální profil/cutoff předpis, pokud se používá cutoff spektrální akce.

Změna těchto dat může ponechat exaktní Cliffordův hlavní symbol beze změny a
současně změnit `a2`, `a4`, a tedy koeficienty Einsteinova–Hilbertova,
kosmologického, gauge a dalších nízkoenergetických invariantů.

Existující formule generalizovaného Diracova operátoru v kanonickém zdroji je
explicitně architektonickým kandidátem do doby, než bude odvozena z akce UBT,
a její blok nultého řádu není současnou dokázanou Cliffordovou relací určen.
Existující NCG/spektrální poznámka je rovněž pracovní/spekulativní konstrukce.

<!-- BILINGUAL-UNIT: spectral-underdetermination.no-go -->
## Co je uzavřeno jako no-go

Následující úsudek je neplatný:

> Cliffordův hlavní symbol UBT je jednoznačně určen, proto jsou jednoznačně
> určeny jeho spektrální akce a Einsteinův–Hilbertův koeficient.

Rodina `P_u` je exaktním protipříkladem tomuto úsudku.

Tím se spektrální cesta nevyvrací. Zpřesňuje se její cíl uzavření: je třeba
odvodit úplný přípustný operátor a spektrální předpis, nikoli pouze kauzální
hlavní symbol.

<!-- BILINGUAL-UNIT: spectral-underdetermination.verification -->
## Ověření

`tools/verify_spectral_symbol_underdetermination.py` násobí formální tepelnou
řadu výrazem `exp(-u t)` a kontroluje identity koeficientů exaktně pomocí
SymPy. `tests/test_spectral_symbol_underdetermination.py` udržuje identity v
CI.

Identita semigroup plyne přímo z toho, že konstantní skalární posun komutuje s
`P0`; není použita žádná numerická aproximace. Formalizace abstraktního
důsledku pro semigroup/asymptotiku tepelného jádra v Leanu je `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: spectral-underdetermination.status -->
## Dopad na status

**SPECTRAL ACTION FROM CLIFFORD PRINCIPAL SYMBOL ALONE: CLOSED AS NO-GO [L0].**

**SPECTRAL/GENERALIZED-DIRAC ACTION ROUTE: NARROWED, STILL OPEN.**

Pro uzavření musí UBT odvodit úplný operátor a spektrální předpis, jejichž data
nižšího řádu jsou určena jedinou fundamentální strukturou a nejsou zvolena až
po znalosti požadovaného výsledku GR/gauge.
