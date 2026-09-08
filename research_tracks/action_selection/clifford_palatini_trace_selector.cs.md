<!-- BILINGUAL-UNIT: clifford-palatini.provenance -->
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

# Kanonický Cliffordův trace selektor Palatiniho curvature formy

<!-- BILINGUAL-UNIT: clifford-palatini.setup -->
## Nastavení z existujícího UBT Cliffordova liftu

Na kanonické Lorentzově bázi nechť

\[
\frac12\{\Gamma_a,\Gamma_b\}=\eta_{ab}I_4,
\qquad
\eta=\operatorname{diag}(-1,1,1,1),
\]

s exaktními `4 x 4` blokovými maticemi již získanými z biquaternionické
tetrády. Stejná konstrukce poskytuje grading

\[
\Gamma_*^2=I_4,
\qquad
\{\Gamma_*,\Gamma_a\}=0.
\]

Nechť Cliffordovsky hodnotová koframe a fyzická spinová křivost jsou

\[
\mathbb E:=\Gamma_aE^a,
\qquad
\mathbb R:=\frac14R^{cd}\Gamma_c\Gamma_d.
\]

Nezavádí se zde žádná nová tetráda: `E^a` je tatáž kanonická UBT tetráda,
případně reprezentovaná přes split-jet architekturu.

<!-- BILINGUAL-UNIT: clifford-palatini.trace -->
## Exaktní graded trace identita [L0]

Pro kanonickou blokovou reprezentaci

\[
\boxed{
\operatorname{Tr}(\Gamma_*\Gamma_a\Gamma_b\Gamma_c\Gamma_d)
=-4i\,\epsilon_{abcd},
\qquad \epsilon_{0123}=+1.}
\]

Proto

\[
\begin{aligned}
\operatorname{Tr}(\Gamma_*\mathbb E\wedge\mathbb E\wedge\mathbb R)
&=\frac14
\operatorname{Tr}(\Gamma_*\Gamma_a\Gamma_b\Gamma_c\Gamma_d)
E^a\wedge E^b\wedge R^{cd}\\
&=-i\,\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}.
\end{aligned}
\]

Ekvivalentně

\[
\boxed{
\frac1{4\kappa}\int
\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}
=
\frac{i}{4\kappa}\int
\operatorname{Tr}(\Gamma_*\mathbb E\wedge\mathbb E\wedge\mathbb R).}
\]

Hilbertova–Palatiniho curvature kontrakce je tedy **přesně graded Cliffordův
trace objektů, které již existují v kanonickém UBT liftu**. Tensor `epsilon`
není nutné zavádět jako nesouvisející dodatečnou algebraickou strukturu.

`tools/verify_clifford_palatini_trace_selector.py` kontroluje identitu pro všech
`4^4` kombinací indexů v exaktní symbolické aritmetice.

<!-- BILINGUAL-UNIT: clifford-palatini.grading -->
## Grading je unikátní až na měřítko [L0]

Nechť `Z` je libovolná komplexní `4 x 4` matice splňující

\[
\{Z,\Gamma_a\}=0
\qquad(a=0,1,2,3).
\]

Exaktní lineární systém má jednorozměrný komplexní prostor řešení. Po
normalizaci `Z^2=I_4`,

\[
\boxed{Z=\pm\Gamma_*.}
\]

Jakmile tedy mikroskopické pravidlo vyžaduje právě jedno vložení normalizovaného
Cliffordova gradingu, není v tomto vložení žádná spojitá maticová nejednoznačnost.

Jde o tvrzení o kanonické reprezentaci. Zatím nestanovuje, že zamčená dynamika
UBT vložení gradingu do akce vyžaduje.

<!-- BILINGUAL-UNIT: clifford-palatini.holst -->
## Proč samotná Lorentzova invariance stále nestačí

Také negradovaný trace čtyř gamma matic je exaktní:

\[
\boxed{
\operatorname{Tr}(\Gamma_a\Gamma_b\Gamma_c\Gamma_d)
=4(\eta_{ab}\eta_{cd}-\eta_{ac}\eta_{bd}+\eta_{ad}\eta_{bc}).}
\]

Protože `E^a wedge E^b` i `R^{cd}` jsou antisymetrické ve svých indexových
dvojicích, dostáváme

\[
\boxed{
\operatorname{Tr}(\mathbb E\wedge\mathbb E\wedge\mathbb R)
=-2E^a\wedge E^b\wedge R_{ab},}
\]

což je metric/Holst curvature kanál, nikoli orientovaný Palatiniho kanál.

Obecněji dává exaktní Lie-algebra redukce na šestirozměrné Lorentzově
bivectorové reprezentaci

\[
\boxed{
\dim\left[\operatorname{Sym}^2(\Lambda^2\mathbb R^{1,3})^*
\right]^{SO^+(1,3)}=2.}
\]

Bázi tvoří bivectorová metrická kontrakce a epsilon/Hodge kontrakce. Verifier
řeší úplný systém invariantních bilineárních forem exaktně a nachází rozměr
dva.

Lorentzova kovariance a lokalita samy o sobě tedy dovolují dvoukanálovou rodinu
lineární v křivosti, konvenčně Palatini plus Holst. Kanonický grading identifikuje
Palatiniho směr uvnitř této rodiny, ale k vyloučení nezávislého negradovaného
koeficientu je potřeba další UBT-native grading/parity/chirality selekční
princip.

Jde o otázku jednoznačnosti akce.
[Věta o dynamické ekvivalenci](curvature_channel_dynamical_equivalence.cs.md)
ukazuje, že konstantní reálný Holstův koeficient nebrání lokální vakuové
GR při nenulovém Palatiniho koeficientu, nedegenerovaném koreperu a nulovém
spinovém proudu. Jeho nepřítomnost proto není nutnou podmínkou tohoto
omezeného cíle klasické obnovy. Spinové zdroje a koeficienty závislé
na poli vyžadují samostatné posouzení.

<!-- BILINGUAL-UNIT: clifford-palatini.conditional-uniqueness -->
## Podmíněná jednoznačnost curvature formy

Předpokládejme, že budoucí mikroskopická UBT věta stanoví současně:

1. vedoucí lokální gravitační člen je lineární ve fyzické Lorentzově křivosti
   a kvadratický v kanonické tetrádě;
2. je vytvořen kanonickým Cliffordovým trace;
3. musí být vložena právě jedna normalizovaná matice antikomutující se všemi
   `Gamma_a` (například protože fyzický `psi`/grading sektor dodá odvozené
   pravidlo chirality nebo orientace).

Pak předchozí věta o jednoznačnosti vynutí matici `+/- Gamma_*` a curvature člen
je následně Hilbertova–Palatiniho forma, **až na celkový reálný koeficient a
znaménko orientace**.

Tím by se tensorový tvar GR curvature akce odvodil místo nezávislého postulování
`epsilon E E R`. Současný repozitář zatím premisu 3 z dynamiky komplexního času
neodvodil, takže tato implikace zůstává podmíněná.

<!-- BILINGUAL-UNIT: clifford-palatini.normalization -->
## Co zůstává po trace identitě

Cliffordův trace fixuje relativní číselnou normalizaci uvnitř identity (`-4 i`),
jakmile je kanonická gamma báze pevná. Nefixuje však fyzický koeficient
`1/kappa`. Současné `N0` je globální konstanta nastavující jednotky, nikoli již
odvozená Newtonova/Planckova škála, a audit akce neobsahuje větu, která by je
jednoznačně spojovala.

Zbývající problém původu křivosti se proto rozděluje do dvou menších úloh:

- **gravitační kanál:** odvodit nenulový Palatiniho koeficient; určení
  nezávislého Holstova koeficientu zůstává otázkou jednoznačnosti akce
  a hmotového či kvantového sektoru, ale uvedená věta o klasické vakuové
  ekvivalenci je nevyžaduje;
- **celková normalizace:** odvodit `kappa` (a samostatně `Lambda`) z
  mikroskopických dat UBT.

<!-- BILINGUAL-UNIT: clifford-palatini.status -->
## Stav

**PALATINIHO EPSILON KONTRAKCE JAKO KANONICKÝ GRADED CLIFFORDŮV TRACE:
PROVED [L0].**

**JEDNOZNAČNOST NORMALIZOVANÉHO CLIFFORDOVA GRADINGU AŽ NA ZNAMÉNKO:
PROVED [L0].**

**PROSTOR LORENTZOVSKY INVARIANTNÍCH CURVATURE-LINEÁRNÍCH BIVECTOROVÝCH
KANÁLŮ: PŘESNĚ DVOUROZMĚRNÝ [L1].**

**DYNAMICKÝ VÝBĚR GRADED KANÁLU V UBT A NEWTONOVA NORMALIZACE:
OPEN.**
