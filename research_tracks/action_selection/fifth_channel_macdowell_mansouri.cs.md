<!-- BILINGUAL-UNIT: fifth-channel-mm.provenance -->
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

# Fifth-channel Cliffordův curvature-square kandidát pro GR akci

<!-- BILINGUAL-UNIT: fifth-channel-mm.scope -->
## Rozsah

Kanonický UBT Cliffordův lift již obsahuje čtyři Lorentzovy generátory
`Gamma_a` a antikomutující pátý kanál. Pišme

\[
\Gamma_\psi^2=\varepsilon_\psi I_4,
\qquad
\varepsilon_\psi=\pm1,
\qquad
\{\Gamma_\psi,\Gamma_a\}=0.
\]

Existující konstrukce dovoluje `Gamma_psi=Gamma_*` pro
`epsilon_psi=+1` nebo `Gamma_psi=i Gamma_*` pro `epsilon_psi=-1`. Tato
poznámka zkoumá, zda Palatiniho curvature člen může vzniknout z **jedné
rozšířené Cliffordovy křivosti**, místo aby byl vložen jako nezávislý člen.

Níže použitý mechanismus je standardní MacDowellův–Mansouriho algebraický
mechanismus. Na tuto standardní gravitační konstrukci se nevznáší nárok na
novost. UBT-specifické pozorování spočívá v tom, že požadovaný pátý Cliffordův
generátor už existuje v kanonické single-Theta architektuře, takže konstrukci
lze testovat bez přidání nového Cliffordova carrieru.

<!-- BILINGUAL-UNIT: fifth-channel-mm.connection -->
## Rozšířená Cliffordova konexe

Nechť

\[
J_{ab}:=\frac12\Gamma_a\Gamma_b
\qquad(a\ne b),
\qquad
P_a:=\frac12\Gamma_a\Gamma_\psi.
\]

Exaktní Cliffordova algebra dává

\[
\boxed{[P_a,P_b]=-\varepsilon_\psi J_{ab}.}
\]

Pro reálnou délkovou škálu `ell` definujme kandidátní rozšířenou konexi

\[
\boxed{
\mathcal A
=\frac12\omega^{ab}J_{ab}
+\frac1\ell E^aP_a
=\frac14\omega^{ab}\Gamma_a\Gamma_b
+\frac1{2\ell}E^a\Gamma_a\Gamma_\psi.}
\]

Zde `omega` je fyzická Lorentzova konexe a `E^a` je tatáž kanonická UBT
tetráda. Ve striktní single-Theta implementaci může být `E^a` split-jet
kompozitní tetrádou studovanou v tomto PR; nejde o nové fundamentální pole.

Tato definice je **kandidátní dynamická architektura**. Zamčené axiomy UBT
v současnosti nestanovují, že se fyzická gauge konexe rozšiřuje právě na tuto
de Sitterovskou/anti-de Sitterovskou Cliffordovu konexi.

<!-- BILINGUAL-UNIT: fifth-channel-mm.curvature -->
## Exaktní rozklad křivosti [L0]

Křivost

\[
\mathcal F=d\mathcal A+\mathcal A\wedge\mathcal A
\]

má Lorentzovu a translační část

\[
\boxed{
\mathcal F
=\frac14\left(
R^{ab}(\omega)-\frac{\varepsilon_\psi}{\ell^2}E^a\wedge E^b
\right)\Gamma_a\Gamma_b
+\frac1{2\ell}T^a\Gamma_a\Gamma_\psi,}
\]

kde

\[
T^a=dE^a+\omega^a{}_b\wedge E^b.
\]

Relativní koeficient `E wedge E` je tedy fixován komutátorem pátého Cliffordova
kanálu, jakmile je zvolena normalizace translačního generátoru `1/ell`.

`tools/verify_fifth_channel_macdowell_mansouri.py` kontroluje tento komutátor
exaktně pro obě znaménka `epsilon_psi`.

<!-- BILINGUAL-UNIT: fifth-channel-mm.action -->
## Graded curvature-square akce

Použijme kanonický čtyřrozměrný grading `Gamma_*` a definujme

\[
\boxed{
S_{\rm MM}
=-\frac{i\,\varepsilon_\psi\ell^2}{2\kappa}
\int\operatorname{Tr}
\left(\Gamma_*\mathcal F\wedge\mathcal F\right).}
\]

Graded trace anuluje translační curvature cross struktury, které neobsahují
čtyři Lorentzovy gamma matice, zatímco již ověřená identita

\[
\operatorname{Tr}(\Gamma_*\Gamma_a\Gamma_b\Gamma_c\Gamma_d)
=-4i\epsilon_{abcd}
\]

vybírá orientovaný Lorentzův bivectorový kanál. Exaktní rozvoj dává

\[
\boxed{
\begin{aligned}
S_{\rm MM}
={}&-\frac{\varepsilon_\psi\ell^2}{8\kappa}
\int\epsilon_{abcd}R^{ab}\wedge R^{cd}\\
&+\frac1{4\kappa}
\int\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}\\
&-\frac{\varepsilon_\psi}{8\kappa\ell^2}
\int\epsilon_{abcd}E^a\wedge E^b\wedge E^c\wedge E^d.
\end{aligned}}
\]

První člen je čtyřrozměrná Eulerova hustota. Při pevné topologii jde o
topologický člen, který nemění lokální bulk Einsteinovy rovnice. Druhý člen je
přesně Hilbertův–Palatiniho člen s normalizací použitou v existujících GR
closure poznámkách. Porovnání posledního členu s

\[
-\frac{\Lambda}{24\kappa}
\int\epsilon_{abcd}E^a\wedge E^b\wedge E^c\wedge E^d
\]

dává strukturální vztah

\[
\boxed{\Lambda=\frac{3\varepsilon_\psi}{\ell^2}.}
\]

Znaménko kosmologického členu tedy sleduje znaménko zvolené pro pátý Cliffordův
kanál a jeho velikost určuje délková škála rozšířené konexe.

<!-- BILINGUAL-UNIT: fifth-channel-mm.significance -->
## Proč je to silnější než ruční vložení Palatiniho členu

Split-jet Palatiniho poznámka stanovila, že single-Theta variační architektura
může nést úplné Palatiniho rovnice, ale curvature funkcionál ponechala jako
importovaného kandidáta. Současný výsledek dává jednotnější algebraický původ
jeho **tvaru**:

1. vyjdeme z jedné rozšířené Cliffordovy konexe;
2. vytvoříme jeden graded curvature-square invariant;
3. rozvineme jej;
4. získáme Eulerovu topologii, Palatiniho gravitaci a kosmologický člen s
   fixovanými relativními koeficienty.

Na algebraické úrovni není třeba nezávislý člen `epsilon E E R`. Palatiniho a
kosmologická struktura jsou svázány s toutéž curvature pátého kanálu.

To podstatně zužuje gap výběru akce, ale ještě jej neuzavírá. Otázka se přesouvá
z „proč psát Palatiniho tensorovou kontrakci?“ na „proč musí UBT zvolit právě
tuto rozšířenou konexi a tento graded curvature-square funkcionál?“

<!-- BILINGUAL-UNIT: fifth-channel-mm.parameters -->
## Redukce parametrů a zbývající problém normalizace

Jakmile je curvature-square architektura vybrána, `Lambda` už není nezávislým
koeficientem: s `ell` souvisí vztahem

\[
\Lambda=3\varepsilon_\psi/\ell^2.
\]

Celkový koeficient však stále obsahuje `kappa`. Ekvivalentně, kdyby
mikroskopičtější UBT derivace dodala bezrozměrný koeficient `g_G^{-2}` pro
curvature-square trace, porovnání s Palatiniho členem by svázalo `kappa` s
touto vazbou a `ell`; bez dalšího vstupu by však neurčilo obě veličiny.

Obzvlášť ostrým budoucím testem je, zda lze `ell` odvodit z fyzického sektoru
komplexního času `psi`. Pokud věta identifikuje pátý Cliffordův kanál s
kompaktním geometrickým `psi` směrem o poloměru `R_psi` a fixuje translační
normalizaci tak, že `ell=R_psi`, pak

\[
\boxed{\Lambda=\frac{3\varepsilon_\psi}{R_\psi^2}}
\]

bude následovat. **Žádná taková identifikace se zde netvrdí**: kanonické zdroje
UBT stále nechávají fyzickou roli, signaturu a škálu `psi` kanálu otevřenou.

<!-- BILINGUAL-UNIT: fifth-channel-mm.symmetry -->
## Symetrická výhrada

Pevné vložení gradingu `Gamma_*` je Lorentzovsky invariantní, ale není
invariantní pod celou rozšířenou de Sitterovskou/anti-de Sitterovskou grupou,
pokud grading není povýšen na nebo odvozen ze symmetry-breaking struktury. Ve
standardním MacDowellově–Mansouriho mechanismu právě toto redukuje rozšířenou
gauge symetrii na Lorentzovu podgrupu.

Pro UBT to není kosmetický bod. Úplná derivace musí vysvětlit, proč kanonická
fifth/complex-time struktura dodává potřebný grading nebo redukci symetrie,
namísto přidání externího preferovaného interního vektoru. Dokud tato věta
neexistuje, jde o silně omezeného kandidáta, nikoli finalizovanou fundamentální
akci.

[Audit ekvivalence kanálů křivosti](curvature_channel_dynamical_equivalence.cs.md)
tento požadavek zpřesňuje. Konstantní Lorentzovsky skalární maticové vložky
tvoří lineární obal jednotkové matice a graduace; úplné rozšířené komutační
podmínky ponechávají jen jednotkovou matici. Negradovaná rozšířená stopa má
nulovou lokální objemovou variaci, takže libovolný konstantní koeficient tohoto
členu nemění rovnice kandidáta. Lokální gravitace vyžaduje nenulový gradovaný
koeficient a odvození příslušné redukce symetrie, nikoli důkaz nepřítomnosti
konstantního negradovaného členu.

<!-- BILINGUAL-UNIT: fifth-channel-mm.verification -->
## Ověření

`tools/verify_fifth_channel_macdowell_mansouri.py` kontroluje v exaktní
symbolické aritmetice:

- `Gamma_psi^2=epsilon_psi` pro obě kanonické volby pátého kanálu;
- translační komutátor `[P_a,P_b]=-epsilon_psi J_ab`;
- relativní Eulerův, Palatiniho a objemový koeficient v curvature-square
  rozvoji;
- vztah `Lambda=3 epsilon_psi/ell^2`.

Diferenciálně-geometrický rozklad křivosti a topologická povaha Eulerova členu
jsou standardní analytické výsledky. Formalizace v Leanu se zde netvrdí; tato
poznámka je `LEAN-PENDING` nad rámec konečné Cliffordovy algebry kontrolované
exaktním verifierem.

<!-- BILINGUAL-UNIT: fifth-channel-mm.status -->
## Stav

**ROZVOJ FIFTH-CHANNEL CLIFFORD CURVATURE-SQUARE NA
EULER + PALATINI + KOSMOLOGICKÝ ČLEN: ALGEBRAICKY PROVED [L1].**

**RELATIVNÍ KOSMOLOGICKÝ VZTAH `Lambda=3 epsilon_psi/ell^2` V TOMTO
KANDIDÁTU: PROVED [L1].**

**ODVOZENÍ ROZŠÍŘENÉ KONEXE, VÝBĚRU GRADINGU, `ell` A CELKOVÉ NEWTONOVY
NORMALIZACE ZE ZAMČENÉ DYNAMIKY UBT: OPEN.**
