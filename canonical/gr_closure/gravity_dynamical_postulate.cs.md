<!-- BILINGUAL-UNIT: gr-dynamical-postulate.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->

# Dynamický postulát gravitačního sektoru UBT: jednovazbová Einsteinova-Lambda větev

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.role -->
## Role

Zamčené axiomy UBT určují kinematiku pole, komplexního času a kovariantní
tetrády, ale samotná kinematika neurčuje nenulovou gravitační akci. Fyzikální
teorie proto vedle kinematiky potřebuje jeden dynamický zákon.

Minimální gravitační zákon přijatý zde má právě jednu nezávislou spojitou vazbu
akce, `kappa`. Kosmologická konstanta se nepokládá rovna nule ani se nezavádí
jako druhá vazba: na slupce vzniká jako integrační konstanta pomocí
difeomorfismově invariantního unimodulárního/Henneaux--Teitelboimova doplnění.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.field -->
## Kompozitní tetráda a pomocná geometrie

Na každém regulárním nenulovém patchi Lorentzovsky reálné projekce `X` pole
`Theta` definujme

\[
E^a=\frac1{\sqrt{N_0}}
\left(dX^a+\omega^a{}_bX^b+K_J{}^a{}_bX^b+wX^a\right),
\qquad X^2\ne0.
\]

`Theta` zůstává jediným fundamentálním fyzikálním polem. `omega` je variační
Lorentzova konexe a `K_J,w` jsou algebraické split-jet proměnné. Navíc zaveďme
pomocný skalár `Lambda(x)` a pomocnou tříformu `C_3`. Ani jedna z těchto
proměnných nemá v gravitačním sektoru lokální propagující stupeň volnosti.
Neexistuje nezávisle variované tetrádové pole ani pevná pozaďová objemová forma.

Split-jet variační zobrazení `(delta K_J,delta w) -> delta E` je bodově
surjektivní na všechny tetrádové směry na uvedeném patchi.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.action -->
## Dynamický postulát

Definujme

\[
\nu_E:=\frac1{24}\epsilon_{abcd}
E^a\wedge E^b\wedge E^c\wedge E^d.
\]

Kanonický lokální klasický gravitační zákon je

\[
\boxed{
S_G[\Theta,\omega,K_J,w,\Lambda,C_3;\kappa]
=\frac1{4\kappa}\int_{M_4}
\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}(\omega)
-\frac1\kappa\int_{M_4}\Lambda(x)\left(\nu_E-dC_3\right),
\qquad \kappa>0.}
\]

Akce obsahuje právě jednu nezávislou spojitou vazbu, `kappa`. `N0` je zamčená
globální normalizace volby jednotek. `Lambda(x)` je pole Lagrangeova
multiplikátoru, nikoli vazbová konstanta.

Mergnutá pátokanálová MacDowell--Mansouriho konstrukce zůstává algebraickou
motivací, proč Palatiniho a kosmologická struktura patří do stejného rozšířeného
Cliffordova sektoru křivosti, ale dřívější volba `ell -> infinity` a
`Lambda_bare=0` nejsou součástí tohoto postulátu.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.selection -->
## Důvod výběru: minimální low-energy princip

Postulát není vydáván za důsledek samotné kinematiky. Jeho tvar je ale výrazně
užší než libovolná volba rovnic pole. Přijměme na regulární Lorentzovsky reálné
větvi následující low-energy požadavky gravitačního sektoru:

1. lokalitu a difeomorfismovou invarianci;
2. lokální Lorentzovu invarianci tetrádového popisu;
3. metrické rovnice nejvýše druhého diferenciálního řádu v klasickém low-energy
   sektoru;
4. žádné další lehké propagující geometrické pole nad stupně volnosti
   kompozitní metriky;
5. nejvýše jednu nezávislou spojitou vazbu akce.

Existující čtyřrozměrný Lovelockův teorém zaznamenaný v
`canonical/gr_closure/gap_10d_low_energy_uniqueness.tex` pak omezuje každý
přirozený symetrický identicky bezdivergenční metrický tensor v této třídě na

\[
\boxed{\mathcal E_{\mu\nu}=aG_{\mu\nu}+bg_{\mu\nu}.}
\]

Metrickým endpointem je tedy Einstein-`Lambda` až na normalizaci; nejde o jednu
libovolnou tensorovou rovnici mezi mnoha. Výše uvedený Palatiniho člen je
minimálním first-order tetrádově/konexním reprezentantem tohoto endpointu,
zatímco HT sektor realizuje kosmologický člen bez druhé vazby akce. V samostatně
deklarované afinní, background-free, first-order pomocné třídě je toto HT
doplnění jednoznačné až na invertibilní lineární redefinice pomocných polí,
konvenci znaménka/orientace a hraniční člen.

Toto zdůvodnění **nedokazuje**, že hlubší mikroskopická UBT jednoznačně vynucuje
lokalitu, druhý řád nebo hypotézu bez dalších lehkých polí. Tyto požadavky jsou
součástí přijatého klasického dynamického principu. Budoucí mikroskopické
odvození je může vysvětlit, ale současné tvrzení je záměrně slabší a obhajitelné:
jakmile jsou tyto minimální low-energy principy přijaty, Einsteinův-`Lambda`
endpoint i jednovazbová pomocná realizace jsou silně omezené.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.lambda -->
## Kosmologická konstanta jako integrační údaj [STD]

Variace `C_3` a `Lambda` dává

\[
\boxed{d\Lambda=0,}
\qquad
\boxed{\nu_E=dC_3.}
\]

Na každém souvislém lokálním patchi tedy

\[
\boxed{\Lambda(x)=\Lambda_0=\mathrm{constant}.}
\]

`Lambda_0` je integrační/stavová konstanta řešení, nikoli druhý parametr teorie.
Povoleny jsou kladné, nulové i záporné větve.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.equations -->
## Lokální Eulerův--Lagrangeův důsledek [L1]

Tetrádová Eulerova rovnice je

\[
\boxed{
\epsilon_{abcd}E^b\wedge
\left(R^{cd}-\frac{\Lambda}{3}E^c\wedge E^d\right)=0.}
\]

Surjektivita split-jet variace implikuje, že variace `K_J,w` ukládá tuto úplnou
tetrádovou rovnici, nikoli adjungovanou projekci.

Variace konexe je běžná Palatiniho konexní variace plus řetězový člen přes
kompozitní tetrádu. Na tetrádové rovnici tento člen mizí. Zbývající vakuová
Cartanova rovnice má již ověřenou invertibilní 24-komponentní torzní mapu, takže

\[
\boxed{T^a=0,\qquad\omega=\mathring\omega(E).}
\]

Metrická rovnice je tedy

\[
\boxed{G_{\mu\nu}+\Lambda_0g_{\mu\nu}=0.}
\]

Variace `Theta` je diferenciálním důsledkem úplné tetrádové rovnice. Naopak
každé regulární lokální Einsteinovo řešení s libovolnou konstantou `Lambda_0`
má existující nenulový split-jet lift. Na kontraktibilním čtyřrozměrném patchi
je `nu_E` lokálně exaktní, takže existuje `C_3` splňující `dC_3=nu_E`. Proto

\[
\boxed{
\operatorname{Sol}_{\rm loc}(S_G)/\operatorname{Stab}_{\rm jet}
\longleftrightarrow
\bigcup_{\Lambda_0\in\mathbb R}
\operatorname{Sol}_{\rm loc}(\mathrm{GR},\Lambda_0).}
\]

To zahrnuje lokální Schwarzschildovu, Kerrovu, de Sitterovu, anti-de Sitterovu
a Schwarzschild--de Sitterovu/Kottlerovu větev a jejich běžné GR perturbace.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.source -->
## Význam jediné konstanty

V čistém vakuu se celkový faktor `1/kappa` z klasických rovnic vykrátí; `kappa`
se stává gravitační odezvovou konstantou relativně k normalizaci zdrojového
sektoru budoucí jediné UBT redukce hmoty/gauge sektoru.

`Lambda_0` se nepočítá jako fundamentální konstanta teorie, stejně jako hmotnost
černé díry nebo moment hybnosti mohou označovat řešení, aniž by byly vazbou
Lagrangiánu. Silnější budoucí kosmologie může zkusit vybrat nebo predikovat
pozorovanou hodnotu `Lambda_0` z globálních, topologických, vakuových nebo
kvantových stavových dat. Tato numerická selekce je problém kosmologie, nikoli
gap lokální obnovy Einstein-`Lambda` GR.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.scope -->
## Rozsah statusu `CLOSED`

Přijetí tohoto postulátu uzavírá **lokální klasický problém obnovy GR včetně
libovolné konstantní kosmologické konstanty**. Netvrdí, že již byla
předpovězena pozorovaná numerická hodnota temné energie, že je finalizována
úplná gauge/hmotová/kvantová UBT akce, že je dokončeno globální pokračování přes
nulové patche nebo že je dokázána UV stabilita `psi`.

<!-- BILINGUAL-UNIT: gr-dynamical-postulate.status -->
## Kanonický status po přijetí

```yaml
gravity_dynamical_postulate: ONE_COUPLING_UNIMODULAR_SPLIT_JET_PALATINI
independent_continuous_action_couplings: 1
constant: kappa
Lambda_role: INTEGRATION_CONSTANT
Lambda_allowed_signs: POSITIVE_ZERO_NEGATIVE
fundamental_physical_field: Theta
independent_tetrad: false
local_Einstein_Lambda_recovery: CLOSED
numerical_Lambda_prediction: OPEN_COSMOLOGY
full_single_ubt_action: NOT_FINALIZED
```

Merge tohoto dokumentu a párové anglické edice je repo akcí, která postulát
přijímá. Do merge jde o pracovní návrh kanonizace a nesmí být popisován jako již
přijatý na `master`.
