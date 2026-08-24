<!-- BILINGUAL-UNIT: unimodular-one-constant.provenance -->
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

# Jednovazbová split-jet GR s kosmologickou konstantou jako integrační konstantou

<!-- BILINGUAL-UNIT: unimodular-one-constant.scope -->
## Rozsah

Poincarého kontrakce s nulovým `Lambda` je pro úplné lokální uzavření GR příliš
úzká: běžná Einsteinova gravitace obsahuje rodinu Einstein-`Lambda` a kladné
`Lambda` dává de Sitterovu větev relevantní pro zrychlenou expanzi. Požadavek
ekonomie parametrů má proto znít tak, že `Lambda` nesmí být druhou nezávislou
vazbou akce.

Tato poznámka dává difeomorfismově invariantní Henneaux--Teitelboimovo /
unimodulární doplnění split-jet Palatiniho větve. Obsahuje právě jeden spojitý
parametr akce, `kappa`, zatímco konstanta `Lambda_0` vzniká na slupce jako
integrační údaj.

<!-- BILINGUAL-UNIT: unimodular-one-constant.action -->
## Akce

Definujme tetrádovou objemovou čtyřformu

\[
\nu_E:=\frac1{24}\epsilon_{abcd}
E^a\wedge E^b\wedge E^c\wedge E^d.
\]

Se stejnou split-jet kompozitní tetrádou `E[Theta,omega,K_J,w]` zaveďme pomocný
skalár `Lambda(x)` a pomocnou tříformu `C_3`. Gravitační zákon je

\[
\boxed{
S_{\rm UGR}
=\frac1{4\kappa}\int\epsilon_{abcd}
E^a\wedge E^b\wedge R^{cd}(\omega)
-\frac1\kappa\int \Lambda(x)\left(\nu_E-dC_3\right),
\qquad \kappa>0.}
\]

`Lambda(x)` a `C_3` jsou variační pomocné proměnné, nikoli vazbové konstanty.
Tříforma ve čtyřech rozměrech nemá lokální propagující stupeň volnosti.
Neexistuje nezávislé tetrádové pole ani pevná pozaďová objemová forma.

<!-- BILINGUAL-UNIT: unimodular-one-constant.lambda -->
## Přesný mechanismus kosmologické konstanty [STD + L1 composition]

Variace `C_3` dává

\[
\boxed{d\Lambda=0,}
\]

takže na každém souvislém lokálním patchi

\[
\boxed{\Lambda(x)=\Lambda_0=\mathrm{constant}.}
\]

Variace `Lambda` dává

\[
\boxed{\nu_E=dC_3.}
\]

`Lambda_0` tedy označuje řešení, ale není v seznamu vazeb akce. Jde o standardní
unimodulární/Henneaux--Teitelboimův mechanismus.

<!-- BILINGUAL-UNIT: unimodular-one-constant.einstein -->
## Úplná Einsteinova rovnice ze split-jet variace

Tetrádová variace akce je úměrná rovnici

\[
\boxed{
\epsilon_{abcd}E^b\wedge
\left(R^{cd}-\frac{\Lambda}{3}E^c\wedge E^d\right)=0.}
\]

Na každém regulárním nenulovém split-jet patchi je již dokázané zobrazení
`(delta K_J,delta w) -> delta E` surjektivní na všechny tetrádové směry.
Variace algebraických jet proměnných proto ukládá celou tuto tetrádovou
Einsteinovu rovnici, nikoli pouze adjungovanou projekci.

Variace `omega` se rovná běžné Palatiniho konexní variaci plus řetězovému členu
přes kompozitní tetrádu. Tento člen je úměrný tetrádové rovnici a na ní mizí.
Zbývající Cartanova rovnice má již ověřenou bodově invertibilní torzní mapu,
takže ve vakuu bez spinu

\[
\boxed{T^a=0,\qquad\omega=\mathring\omega(E).}
\]

Metrická rovnice je tedy

\[
\boxed{G_{\mu\nu}+\Lambda_0g_{\mu\nu}=0.}
\]

<!-- BILINGUAL-UNIT: unimodular-one-constant.equivalence -->
## Lokální ekvivalence množin řešení

Naopak každé regulární lokální vakuové Einsteinovo řešení s libovolnou
konstantou `Lambda_0` má podle existující věty o pravé inverzi split-jet lift.
Na kontraktibilním čtyřrozměrném patchi je jeho objemová čtyřforma lokálně
exaktní, takže existuje tříforma `C_3` splňující `dC_3=nu_E`. Proto

\[
\boxed{
\operatorname{Sol}_{\rm loc}(S_{\rm UGR})/\operatorname{Stab}_{\rm jet}
\longleftrightarrow
\bigcup_{\Lambda_0\in\mathbb R}
\operatorname{Sol}_{\rm loc}(\mathrm{GR},\Lambda_0).}
\]

Lokální větev proto obsahuje Schwarzschilda, Kerra, de Sittera,
anti-de Sittera, Schwarzschild--de Sitter/Kottlera a jejich běžné klasické
perturbační sektory všude, kde je split-jet patch regulární.

<!-- BILINGUAL-UNIT: unimodular-one-constant.parameters -->
## Rozpočet konstant

Akce obsahuje právě jednu nezávislou spojitou fyzikální vazbu:

\[
\boxed{\{\text{action couplings}\}=\{\kappa\}.}
\]

`Lambda_0` je integrační konstanta/stavový údaj, nikoli Lagrangeova vazba, stejně
jako hmotnost nebo moment hybnosti mohou označovat klasické řešení, aniž by byly
fundamentálními konstantami teorie. Pozdější kosmologie UBT se může pokusit
vybrat či predikovat pozorovanou hodnotu `Lambda_0` z globálních,
topologických nebo kvantových stavových dat; tato silnější predikce není nutná
pro lokální ekvivalenci s GR.

<!-- BILINGUAL-UNIT: unimodular-one-constant.limit -->
## Co tento mechanismus řeší a co nikoli

Mechanismus řeší **jednovazbový problém obnovy GR** a odstraňuje nesprávnou
nutnost pokládat kosmologickou konstantu rovnu nule. Sám však neřeší hierarchii
kosmologické konstanty ani nepředpovídá její pozorovanou malou kladnou hodnotu.
Existující UBT poznámka o vakuové energii explicitně nenachází v prvním zeta
odhadu automatickou supresi o 120 řádů, takže zde taková predikce není tvrzena.

<!-- BILINGUAL-UNIT: unimodular-one-constant.status -->
## Status

**ONE-COUPLING LOCAL EINSTEIN-`Lambda` SOLUTION-SET RECOVERY: DERIVED FROM THE
ADOPTED SPLIT-JET PALATINI POSTULATE PLUS THE STANDARD DIFFEOMORPHISM-INVARIANT
UNIMODULAR COMPLETION.**

**`Lambda_0` AS AN INTEGRATION CONSTANT RATHER THAN A SECOND ACTION COUPLING:
PROVED WITHIN THIS VARIATIONAL SYSTEM.**

**MICROSCOPIC PREDICTION OF THE NUMERICAL COSMOLOGICAL CONSTANT: OPEN.**
