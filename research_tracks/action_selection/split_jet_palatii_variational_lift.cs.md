<!-- BILINGUAL-UNIT: split-jet-palatii.provenance -->
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

# Split-jet pullback Palatiniho akce: lokální variační ekvivalence

<!-- BILINGUAL-UNIT: split-jet-palatii.question -->
## Otázka

Existující split-jet věta dokazuje, že každou lokální Lorentzovu tetrádu lze
reprezentovat jediným `Theta` plus algebraickými jetovými proměnnými, ale její
čistě multiplikátorová implementace tetrádu neumí vybrat. Samostatná Palatiniho
věta dokazuje, že nezávisle variovaná tetráda a Lorentzova konexe dávají
standardní Einsteinovy–Cartanovy rovnice, ale sama tato formulace nesplňuje
striktní architekturu jediného fundamentálního pole.

Tato poznámka kombinuje oba výsledky v jiném pořadí: **vůbec nezavádí nezávislou
tetrádu**. Split-jet tetráda se vloží přímo do Palatiniho funkcionálu a variuje
se pouze `Theta` a nepropagující konexní/jetové proměnné.

<!-- BILINGUAL-UNIT: split-jet-palatii.action -->
## Kandidátní akce

Nechť `X` je Lorentzovsky reálná projekce `Theta`, položme
`s=sqrt(N0)` a pracujme na patchi s

\[
X^2:=\eta_{ab}X^aX^b\ne0.
\]

Nechť `omega^{ab}` je fyzická Lorentzova konexe. Zaveďme pomocnou Lorentzovsky
hodnotovou jetovou jednoformu `K_J^{ab}` a relativně centrální reálnou jednoformu
`w`. Tetrádu definujme **kompozitně** vztahem

\[
\boxed{
E^a=\frac1s\left(
 dX^a+\omega^a{}_bX^b+K_J{}^a{}_bX^b+wX^a
\right).}
\]

Fyzická křivost používá pouze `omega`,

\[
R^{ab}(\omega)=d\omega^{ab}+\omega^a{}_c\wedge\omega^{cb}.
\]

Definujme split-jet Palatiniho funkcionál

\[
\boxed{
S_{\rm SJHP}[X,\omega,K_J,w]
=\frac1{4\kappa}\int
\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}(\omega)
-\frac{\Lambda}{24\kappa}\int
\epsilon_{abcd}E^a\wedge E^b\wedge E^c\wedge E^d.}
\]

V tomto funkcionálu není žádná nezávisle variovaná tetráda. `K_J` a `w`
neobsahují derivace a mají být pouze split-jet pomocnými proměnnými. Fyzická
konexe zůstává oddělená od jetové korekce, jak vyžaduje existující no-go pro
jednu konexi a exaktní GR.

Tato akce je **kandidát**. Hilbertova–Palatiniho struktura, `kappa` a `Lambda`
zde nejsou odvozeny z dříve zamčené kinetické akce UBT.

<!-- BILINGUAL-UNIT: split-jet-palatii.surjectivity -->
## Exaktní surjektivita jetové variace [L1]

Při pevných `X` a `omega` je pomocná variace

\[
\delta E^a
=\frac1s\left(\delta K_J{}^a{}_bX^b+\delta w\,X^a\right).
\]

Pro každou cílovou Lorentzovsky vektorovou jednoformu `Y^a` definujme

\[
\delta w=\frac{X_aY^a}{X^2},
\qquad
Y_\perp^a=Y^a-\delta w\,X^a,
\]

a

\[
\delta K_{J\,ab}
=\frac{Y_{\perp a}X_b-X_aY_{\perp b}}{X^2}.
\]

Pak

\[
\delta K_J{}^a{}_bX^b+\delta w\,X^a=Y^a.
\]

Proto je zobrazení

\[
(\delta K_J,\delta w)\longmapsto\delta E
\]

bodově surjektivní na všechny čtyři tetrádové směry pro každé nenulové
`X`. `tools/verify_split_jet_palatii_variational_lift.py`
kontroluje konečné jádro hodnosti čtyři a explicitní pravou inverzi na
exaktních racionálních svědcích.

<!-- BILINGUAL-UNIT: split-jet-palatii.tetrad-equation -->
## Pomocná variace dává úplnou tetrádovou rovnici [L1]

Označme `mathcal E_a` Eulerovu tříformu získanou variací obyčejného Palatiniho
funkcionálu podle nezávislé tetrády `E^a`:

\[
\delta_E S_{\rm HP}=\int \mathcal E_a\wedge\delta E^a.
\]

V `S_SJHP` dává variace podle `(K_J,w)`

\[
0=\int\mathcal E_a\wedge
\frac1s\left(\delta K_J{}^a{}_bX^b+\delta w\,X^a\right).
\]

Protože zobrazení v závorce je surjektivní, jeho transpozice je injektivní.
Stacionarita pro všechny pomocné jetové variace je tedy ekvivalentní

\[
\boxed{\mathcal E_a=0.}
\]

Pomocné proměnné tak přenášejí **celou** Palatiniho tetrádovou rovnici, nikoli
jen její projekci. Ve vakuu jde po dosazení konexní rovnice o Einsteinovu–`Lambda`
tetrádovou rovnici.

Jde přesně o mechanismus injektivity adjungovaného zobrazení, který chyběl v
naivní složené Einsteinově–Hilbertově cestě.

<!-- BILINGUAL-UNIT: split-jet-palatii.connection -->
## Variace fyzické konexe se on shell redukuje na Cartanovu rovnici [L1]

Fyzická konexe vstupuje do `S_SJHP` na dvou místech: přes křivost a přes
kompozitní tetrádu. Proto

\[
\delta_\omega S_{\rm SJHP}
=\left.\delta_\omega S_{\rm HP}\right|_{E\ \mathrm{fixed}}
+\int\mathcal E_a\wedge
\frac1s\,\delta\omega^a{}_bX^b.
\]

Druhý člen zmizí, jakmile jetové rovnice vynutily `mathcal E_a=0`. Zbývající
rovnice je přesně standardní Palatiniho konexní rovnice. Ve vakuu bez spinu dává
již dokázaná invertibilita Cartanovy mapy

\[
\boxed{T^a=0,
\qquad
\omega^{ab}=\mathring\omega^{ab}(E).}
\]

Fyzická křivost je tedy na vakuové větvi Levi–Civitova, i když oddělené jetové
proměnné dovolují lokálně surjektivní mapu tetrády z jediného `Theta`.

<!-- BILINGUAL-UNIT: split-jet-palatii.theta -->
## Rovnice pro Theta je po tetrádové rovnici redundantní

Při pevných pomocných proměnných a fyzické konexi mění variace `X` pouze
kompozitní tetrádu. Schematicky

\[
\delta_X S_{\rm SJHP}
=\int\mathcal E_a\wedge\delta_XE^a.
\]

Po integraci per partes potřebné pro člen `d(delta X)` je výsledná Eulerova
rovnice pro `X` lineárním diferenciálním důsledkem `mathcal E_a` a její
kovariantní derivace. Proto

\[
\boxed{\mathcal E_a=0\Longrightarrow
\frac{\delta S_{\rm SJHP}}{\delta X}=0.}
\]

Variace fundamentálního pole tedy nepřidává další lokální omezení, jakmile byla
úplná tetrádová rovnice již vynucena surjektivními pomocnými jetovými variacemi.

<!-- BILINGUAL-UNIT: split-jet-palatii.converse -->
## Obrácený lift každého lokálního Palatiniho řešení [L1]

Naopak vezměme libovolné lokální Palatiniho řešení `(E,omega)` a zvolme
libovolné hladké nenulové `X`. Definujme

\[
Z^a=sE^a-(dX^a+\omega^a{}_bX^b),
\qquad
w=\frac{X_aZ^a}{X^2},
\qquad
Z_\perp^a=Z^a-wX^a,
\]

a

\[
K_{J\,ab}
=\frac{Z_{\perp a}X_b-X_aZ_{\perp b}}{X^2}.
\]

Kompozitní definice pak přesně rekonstruuje předepsanou tetrádu. Protože
Palatiniho tetrádová i konexní rovnice už platí, platí všechny Eulerovy rovnice
`S_SJHP`. Nevyužitý stabilizátor `K_J` je algebraický a nemění `E`.

Tedy na každém nenulovém patchi

\[
\boxed{
\mathcal P:\operatorname{Crit}(S_{\rm SJHP})
\twoheadrightarrow\operatorname{Crit}(S_{\rm HP}),\qquad
\mathcal P(X,\omega,K_J,w)=(E,\omega).}
\]

Jde o ekvivalenci rovnic na dané konfiguraci a surjektivní zobrazení množin
řešení, nikoli o bijekci pouze modulo stabilizátor jetového tenzoru.
Různé reprezentanty pole mohou dávat stejnou tetrádu; tento stabilizátor
ponechává pole pevné. Protipříklad a rozšíření na kompatibilní hladké
průchody nulovou normou jsou dokázány v `split_jet_null_continuation.cs.md`.
Výše uvedená pravá inverze pro nenulovou normu sama nulové průchody nepokrývá.

<!-- BILINGUAL-UNIT: split-jet-palatii.significance -->
## Co tento výsledek uzavírá

Výsledek řeší architektonickou nejasnost, která zůstala po split-jet
multiplikátorovém no-go:

- čisté split-jet **omezení** neumí tetrádu vybrat, protože se on shell odpojí;
- split-jet proměnné vložené **dovnitř gravitačního funkcionálu** se před
  variací neodpojí;
- jejich surjektivní variace vynutí úplnou tetrádovou rovnici;
- fyzická Palatiniho konexe se pak ve vakuu redukuje na Levi–Civitovu;
- není potřeba žádné nezávislé tetrádové pole.

Proto:

**VARIAČNÍ EKVIVALENCE SINGLE-THETA SPLIT-JET ARCHITEKTURY K VYBRANÉMU
PALATINIHO FUNKCIONÁLU: PROVED LOCALLY AND CONDITIONALLY [L1].**

To však **neodvozuje** Palatiniho curvature člen z původní kineticko-potenciálové
akce UBT. Neurčuje ani `kappa` nebo `Lambda`. Fundamentální akce tedy zůstává
nefinalizovaná.

<!-- BILINGUAL-UNIT: split-jet-palatii.remaining -->
## Zbývající kritický gap

Po tomto výsledku se GR problém odděluje čistěji:

1. **architektura/variace:** lokálně vyřešena na nenulových patchích pro
   split-jet Palatiniho kandidáta;
2. **původ curvature akce:** stále otevřený --- odvodit, nikoli vložit,
   Palatiniho/Einsteinův–Hilbertův curvature člen z mikroskopických dat UBT;
3. **normalizace:** stále otevřená --- odvodit znaménko a Newtonův koeficient;
4. **globální/nulové pokračování a fyzická `psi` stabilita:** stále otevřené.

Dalším rozhodujícím úkolem už tedy není, zda single-`Theta` variační architektura
může reprodukovat všechny Einsteinovy rovnice. Podmíněně na výše uvedeném
kandidátu může. Rozhodující nevyřešený problém je nyní **proč právě tento
curvature funkcionál s touto normalizací musí plynout z UBT, místo aby byl
zvolen proto, že je to GR**.

<!-- BILINGUAL-UNIT: split-jet-palatii.status -->
## Stav

**SPLIT-JET PALATINIHO ADJUNGOVANÁ/SOLUTION-SET EKVIVALENCE NA NENULOVÝCH
PATCHÍCH: CLOSED CONDITIONALLY [L1].**

**PŮVOD A NORMALIZACE PALATINIHO CURVATURE ČLENU ZE ZAMČENÉ DYNAMIKY UBT:
OPEN.**

**NEPODMÍNĚNÁ GR REKONSTRUKCE: NOT YET CLOSED.**
