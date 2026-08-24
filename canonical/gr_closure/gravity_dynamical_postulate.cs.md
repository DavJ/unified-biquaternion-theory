<!-- BILINGUAL-UNIT: gr-dynamical-postulate.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working canonicalization proposal; merge constitutes adoption of the stated gravity-sector dynamical postulate.
UBT-AI-PROVENANCE-END
-->

# Dynamický postulát gravitačního sektoru UBT: jednokonstantní Poincarého větev

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.role -->
## Role

Zamčené axiomy UBT určují kinematiku pole, komplexního času a kovariantní
tetrády, ale samotná kinematika neurčuje nenulovou gravitační akci. Audit
výběru akce ukázal explicitní neurčenost: stejná kinematika je slučitelná s
různými koeficienty křivosti včetně nuly.

Fyzikální teorie proto vedle kinematiky potřebuje jeden dynamický zákon. Tento
dokument stanoví minimální **dynamický postulát gravitačního sektoru** UBT.
Nedefinuje znovu zamčené axiomy pole ani metriky a nezavádí druhé fundamentální
fyzikální pole.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.field -->
## Kompozitní tetráda a pomocná geometrie

Na každém regulárním nenulovém patchi Lorentzovsky reálné projekce `X` pole
`Theta` definujme

\[
E^a=\frac1{\sqrt{N_0}}
\left(dX^a+\omega^a{}_bX^b+K_J{}^a{}_bX^b+wX^a\right),
\qquad X^2\ne0.
\]

Zde:

- `Theta` zůstává jediným fundamentálním fyzikálním polem;
- `omega` je variační Lorentzova konexe;
- `K_J` a `w` jsou algebraické split-jet proměnné bez derivačních členů;
- neexistuje nezávisle variované tetrádové pole;
- fyzická křivost je `R(omega)` a nepoužívá `K_J`.

Split-jet variační zobrazení `(delta K_J, delta w) -> delta E` je bodově
surjektivní na všechny čtyři tetrádové směry na uvedeném patchi.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.action -->
## Dynamický postulát

Kanonický lokální klasický gravitační zákon je

\[
\boxed{
S_G[\Theta,\omega,K_J,w;\kappa]
=\frac1{4\kappa}\int_{M_4}
\epsilon_{abcd}\,E^a\wedge E^b\wedge R^{cd}(\omega),
\qquad \kappa>0.}
\]

Jde o konečný lokální Poincarého kontrahovaný limit mergnutého kanonického
pátokanálového graded curvature-square kandidáta po odečtení Eulerovy
topologické hustoty. Ekvivalentně jde o větev `ell -> infinity`, pro kterou

\[
\boxed{\Lambda_{\rm bare}=0.}
\]

Akce má právě jednu spojitou gravitační konstantu, `kappa`. Zamčená `N0` je
globální unit-setting normalizace a není druhým fyzikálním couplingem.

V této větvi není dovolena nezávislá bare kosmologická konstanta. Nenulový
efektivní kosmologický člen musí být odvozen z vakua/kvantového stavu `Theta`,
hraničních dat nebo jiné redukce téže budoucí jediné UBT akce; není dalším
gravitačním parametrem.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.equations -->
## Lokální Eulerův–Lagrangeův důsledek [L1]

Nechť `E_a` značí běžnou Palatiniho tetrádovou Eulerovu tříformu. Variace
`K_J,w` dává

\[
0=\int E_a\wedge\delta E^a.
\]

Surjektivita split-jet variace implikuje

\[
\boxed{E_a=0.}
\]

Je tedy uložena úplná tetrádová Einsteinova rovnice, nikoli její adjungovaná
projekce.

Variace konexe je standardní Palatiniho konexní variace plus řetězový člen
úměrný `E_a`. Na jet rovnici tento člen mizí. Zbývající vakuová Cartanova
rovnice má již ověřenou invertibilní 24-komponentní torzní mapu, takže

\[
\boxed{T^a=0,\qquad\omega=\mathring\omega(E).}
\]

Variace `Theta` je diferenciálním důsledkem `E_a=0`. Naopak každé lokální
Palatiniho řešení s nulovou bare `Lambda` má explicitní nenulový split-jet lift.
Proto modulo algebraický jet stabilizátor a standardní hraniční/topologická data
platí

\[
\boxed{
\{\text{lokální stacionární body }S_G\}
\longleftrightarrow
\{\text{lokální vakuová řešení GR s }\Lambda_{\rm bare}=0\}.}
\]

Schwarzschild, Kerr a linearizovaný gravitačně-vlnový sektor jsou zahrnuty přes
běžnou lokální množinu řešení GR všude, kde je split-jet patch regulární.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.source -->
## Zdroje a význam jediné konstanty

V čistém vakuu se celkový faktor `1/kappa` z klasických rovnic vykrátí; `kappa`
se stává měřitelnou gravitační odezvovou konstantou až relativně k normalizaci
zdrojového sektoru.

Pravidlo jediné UBT akce zakazuje přidat samostatně normalizovanou fundamentální
hmotovou akci pouze za účelem definice tohoto poměru. Až bude finalizována
gauge/hmotová redukce jediné UBT akce, její tenzor energie-hybnosti musí vstoupit
do stejného variačního systému a `kappa` je jedinou přípustnou gravitační
odezvovou konstantou. Odvození mikroskopické Standard-Model/hmotové redukce je
negravitačním dokončovacím úkolem a tento postulát je nenahrazuje.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.scope -->
## Rozsah statusu `CLOSED`

Přijetí tohoto postulátu uzavírá **lokální klasický problém obnovy GR v
gravitačním sektoru**. Netvrdí silnější výroky, že:

- starší kineticko-potenciálová rodina vynutila tuto akci bez dynamického
  postulátu;
- pozorovaná efektivní hustota temné energie je již odvozena;
- úplná gauge/hmotová/kvantová UBT akce je finalizována;
- je dokončeno pokračování přes nulové patche a globální topologii;
- je dokázána UV stabilita `psi`.

To jsou samostatné problémy úplné teorie, kosmologie nebo globálního dokončení.
Nesmějí být přeznačovány jako selhání lokálního Einsteinova gravitačního
theorému.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.status -->
## Kanonický status po přijetí

```yaml
gravity_dynamical_postulate: POINCARE_CONTRACTED_FIFTH_CHANNEL_SPLIT_JET_PALATINI
continuous_gravity_constants: 1
constant: kappa
bare_cosmological_constant: 0
fundamental_physical_field: Theta
independent_tetrad: false
local_gr_recovery: CLOSED
full_single_ubt_action: NOT_FINALIZED
```

Merge tohoto dokumentu a párové anglické edice je repo akcí, která postulát
přijímá. Do merge jde o pracovní návrh kanonizace a nesmí být popisován jako již
přijatý na `master`.
