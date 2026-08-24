<!-- BILINGUAL-UNIT: one-constant-gr.provenance -->
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

# Jednokonstantní Poincarého kontrakce pátokanálového gravitačního kandidáta

<!-- BILINGUAL-UNIT: one-constant-gr.start -->
## Výchozí bod

Mergnutý pátokanálový Cliffordův kandidát má exaktní lokální rozklad

\[
S_{\rm MM}(\ell,\kappa)
=-\frac{\varepsilon_\psi\ell^2}{8\kappa}
 \int\epsilon_{abcd}R^{ab}\wedge R^{cd}
+\frac1{4\kappa}
 \int\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}
-\frac{\varepsilon_\psi}{8\kappa\ell^2}
 \int\epsilon_{abcd}E^a\wedge E^b\wedge E^c\wedge E^d,
\]

s

\[
\Lambda=\frac{3\varepsilon_\psi}{\ell^2}.
\]

Zde `E` je split-jet kompozitní tetráda architektury s jedinou `Theta`.
První integrál je čtyřrozměrná Eulerova hustota. Při pevné topologii a
obvyklých variačních podmínkách s pevnou hranicí nebo kompaktní podporou má její
bulk variace nulovou hodnotu.

<!-- BILINGUAL-UNIT: one-constant-gr.subtracted -->
## Lokální/topologicky odečtená akce

Pro lokální rovnice pole definujme

\[
\widetilde S_\ell
:=S_{\rm MM}
+\frac{\varepsilon_\psi\ell^2}{8\kappa}
 \int\epsilon_{abcd}R^{ab}\wedge R^{cd}.
\]

Pak exaktně

\[
\boxed{
\widetilde S_\ell
=\frac1{4\kappa}
 \int\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}
-\frac{\varepsilon_\psi}{8\kappa\ell^2}
 \int\epsilon_{abcd}E^a\wedge E^b\wedge E^c\wedge E^d.}
\]

Odečtení Eulerova členu nemění žádnou lokální bulk Eulerovu–Lagrangeovu
rovnici. Odstraňuje pouze topologicky závislý aditivní příspěvek, jehož
koeficient v níže uvedené kontrakci diverguje.

<!-- BILINGUAL-UNIT: one-constant-gr.limit -->
## Exaktní Poincarého kontrakce [L1]

Proveďme Inönüovu–Wignerovu/Poincarého kontrakci

\[
\boxed{\ell\to\infty}
\]

při pevném `kappa > 0`. Potom

\[
\Lambda=\frac{3\varepsilon_\psi}{\ell^2}\longrightarrow0
\]

a po koeficientech

\[
\boxed{
\widetilde S_\ell
\longrightarrow
S_{\rm P}[E,\omega]
=\frac1{4\kappa}
 \int\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}(\omega).}
\]

Lokální Eulerovy–Lagrangeovy formy konvergují k formám Hilbertovy–Palatiniho
akce s nulovou bare kosmologickou konstantou. Žádný druhý spojitý gravitační
parametr nepřežije.

Stejná kontrakce je vidět na úrovni algebry. Pro pátokanálové generátory typu
translace `P_a` platí

\[
[P_a,P_b]\propto\frac1{\ell^2}J_{ab},
\]

takže `ell -> infinity` kontrahuje de Sitterovo/anti-de Sitterovo rozšíření na
Poincarého algebru při zachování Lorentzovy konexe a tetrádového sektoru.

<!-- BILINGUAL-UNIT: one-constant-gr.splijet -->
## Rovnice single-Theta split-jet systému [L1]

Použijme již zavedenou kompozitní tetrádu

\[
E^a=\frac1{\sqrt{N_0}}
\left(dX^a+\omega^a{}_bX^b+K_J{}^a{}_bX^b+wX^a\right)
\]

na nenulovém patchi `X^2 != 0`. Variační zobrazení

\[
(\delta K_J,\delta w)\mapsto\delta E
\]

je bodově surjektivní na všechny čtyři tetrádové směry. Stacionarita vzhledem k
algebraickým jet proměnným proto dává úplnou Palatiniho tetrádovou rovnici,
nikoli pouze její projekci.

Variace fyzické Lorentzovy konexe obsahuje standardní Palatiniho konexní člen a
řetězový člen úměrný tetrádové Eulerově formě. Jakmile jet rovnice tuto formu
vynuluje, zbývající vakuová rovnice je Cartanova rovnice. Její dříve ověřená
bodová invertibilita dává

\[
\boxed{T^a=0,\qquad\omega=\mathring\omega(E).}
\]

Rovnice `Theta` je diferenciálním důsledkem úplné tetrádové rovnice a každé
lokální Palatiniho řešení má explicitní nenulový split-jet lift. Lokální množina
stacionárních bodů kontrahované akce modulo algebraický jet stabilizátor je tedy
lokální množinou stacionárních bodů běžné Palatiniho GR s nulovou bare `Lambda`.

<!-- BILINGUAL-UNIT: one-constant-gr.count -->
## Počet parametrů

Kontrahovaný gravitační sektor obsahuje pouze

\[
\boxed{\kappa}
\]

jako spojitou fyzikální gravitační konstantu. Zamčená `N0` je výslovně globální
unit-setting normalizace, nikoli nezávisle predikovaný fyzikální coupling.
Znaménko Lorentzovy metriky a orientace jsou diskrétní volby, nikoli spojité
konstanty.

Ve vakuu se celkový faktor `1/kappa` z klasických rovnic vykrátí; `kappa` se
stává fyzikálně měřitelnou až relativně k normalizaci zdrojového sektoru. Podle
pravidla jediné UBT akce musí být zdrojový sektor redukcí stejné fundamentální
akce, nikoli samostatně normalizovaným fundamentálním členem. Druhý
**gravitační** coupling proto není přípustný.

Kontrakce dělá z bare kosmologické konstanty predikci

\[
\boxed{\Lambda_{\rm bare}=0,}
\]

nikoli fitovaný gravitační parametr. Nenulový pozorovaný efektivní člen temné
energie musí vzniknout z vakua/kvantového sektoru `Theta` nebo z hraničních
stavových dat; zavedení nezávislé bare `Lambda` by opustilo jednokonstantní
větev.

<!-- BILINGUAL-UNIT: one-constant-gr.status -->
## Význam uzavření

Výsledek odděluje dvě logicky odlišné otázky:

- **Může jednokonstantní single-Theta gravitační zákon dát lokální GR?** Ano:
  kontrahovaný split-jet Palatiniho zákon má na nenulových patchích právě tuto
  množinu řešení.
- **Je tento dynamický zákon vynucen pouze staršími kinematickými axiomy?** Ne.
  Kinematika sama neurčuje celkový dynamický zákon; teorie potřebuje dynamický
  postulát.

Přijetí Poincarého kontrahované pátokanálové akce jako kanonického
**gravitačního dynamického postulátu** tedy mění GR recovery z předpokládaného
efektivního endpointu na vnitřní theorem finalizovaného gravitačního sektoru.
Postulát má jedinou spojitou gravitační konstantu `kappa`.

Tento krok sám o sobě nefinalizuje negravitační Standard-Model/kvantové sektory
jediné UBT akce ani neodvozuje pozorovanou nenulovou efektivní kosmologickou
konstantu.

<!-- BILINGUAL-UNIT: one-constant-gr.verification -->
## Ověření

`tools/verify_one_constant_gr_closure.py` symbolicky kontroluje:

- exaktní rozklad MacDowellovy–Mansouriho akce na koeficienty;
- `Lambda = 3 epsilon_psi/ell^2`;
- koeficienty topologicky odečtené akce;
- limitu `ell -> infinity`;
- jednokonstantní počet parametrů lokální kontrahované gravitace;
- derivační překážku v historickém logaritmickém potenciálu `R_psi`.

Split-jet hodnost a Palatiniho/Cartanova algebra jsou nezávisle kontrolovány
verifiery mergnutými v předchozí práci na výběru akce. Úplná formalizace
teorému diferenciálních forem v Leanu zůstává `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: one-constant-gr.verdict -->
## Verdikt

**LOKÁLNÍ SINGLE-THETA GRAVITACE S NULOVOU BARE KOSMOLOGICKOU KONSTANTOU A
JEDINOU SPOJITOU GRAVITAČNÍ KONSTANTOU: CLOSED [L1] NA NENULOVÝCH PATCHÍCH,
POKUD JE POINCARÉHO KONTRAHOVANÁ PÁTOKANÁLOVÁ AKCE PŘIJATA JAKO GRAVITAČNÍ
DYNAMICKÝ POSTULÁT.**

**VÝBĚR ABSOLUTNÍ ŠKÁLY `R_psi`: V TOMTO UZAVŘENÍ SE NEPOUŽÍVÁ.**

**ÚPLNÁ JEDINÁ UBT AKCE VČETNĚ GAUGE/HMOTOVÝCH/KVANTOVÝCH REDUKCÍ: ZŮSTÁVÁ
SAMOSTATNÝM ÚKOLEM DOKONČENÍ.**
