<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# Rezidua, princip argumentu a Möbiova cesta k RH

**Datum:** 2026-08-25  
**Status:** pracovní matematická syntéza; nejde o důkaz Riemannovy hypotézy ani o zvýšení statusu kteréhokoli tvrzení UBT.  
**Rozsah:** klasická analytická teorie čísel a výslovné rozhraní k současné pracovní theta–Mellinově/RH cestě UBT.

<a id="scope-and-notation"></a>
## 0. Rozsah a značení

Pišme

\[
\zeta(s)=\sum_{n\ge 1}n^{-s}=\prod_p(1-p^{-s})^{-1},
\qquad \Re s>1,
\]

a označme symbolem \(\mu\) Möbiovu funkci, symbolem \(\Lambda\) von Mangoldtovu funkci a

\[
M(x):=\sum_{n\le x}\mu(n)
\]

Mertensovu sumační funkci. Není-li výslovně uvedeno analytické pokračování, manipulace s řadami a Eulerovými součiny se nejprve provádějí v polorovině jejich absolutní konvergence.

Následující čtyři části oddělují zavedenou matematiku od specifického mostu UBT. Tam, kde navržená zkratka nestačí, jsou závěry záměrně negativní.

<a id="part-a"></a>
## A. Rezidua a holomorfie

<a id="a1-local-data"></a>
### A.1 Lokální meromorfní údaje

Funkce zeta má v bodě \(s=1\) jednoduchý pól s reziduem \(1\). Je-li \(\rho\) nulový bod násobnosti \(m_\rho\), potom lokálně

\[
\zeta(s)=(s-\rho)^{m_\rho}g(s),\qquad g(\rho)\ne0.
\]

Proto

\[
\operatorname*{Res}_{s=\rho}\frac{\zeta'(s)}{\zeta(s)}=m_\rho,
\qquad
\operatorname*{Res}_{s=\rho}\left(-\frac{\zeta'(s)}{\zeta(s)}\right)=-m_\rho,
\]

zatímco v pólu \(s=1\) platí

\[
\operatorname*{Res}_{s=1}\left(-\frac{\zeta'(s)}{\zeta(s)}\right)=1.
\]

Funkce \(-\zeta'/\zeta\) tedy zaznamenává nulové body se zápornou násobností a pól funkce \(\zeta\) s kladnou násobností. Převrácená funkce \(1/\zeta\) má v bodě \(s=1\) nulový bod a póly právě v nulových bodech funkce \(\zeta\), se stejnými řády.

<a id="a2-rh-holomorphicity"></a>
### A.2 Formulace RH pomocí oblasti bez nul

S použitím funkcionální rovnice a známé polohy triviálních nul je RH ekvivalentní tvrzení, že \(\zeta(s)\ne0\) pro \(\Re s>1/2\). Ekvivalentně

\[
\boxed{\;1/\zeta\in\mathcal O\!\left(\{s\in\mathbb C:\Re s>1/2\}\right).\;}
\]

Bod \(s=1\) nepředstavuje výjimku, protože \(1/\zeta\) v něm má nulový bod. Tato ekvivalence neříká, že Dirichletova řada \(\sum\mu(n)n^{-s}\) již konverguje v celé této polorovině; rozšíření řady vyžaduje odhady jejích částečných součtů.

<a id="part-b"></a>
## B. Princip argumentu a číslo obtáčení

<a id="b1-principle"></a>
### B.1 Přesné počítací tvrzení

Nechť \(f\) je meromorfní uvnitř i na kladně orientované kontuře \(C\) a nemá na \(C\) žádné nuly ani póly. Pak

\[
\frac{1}{2\pi i}\oint_C\frac{f'(s)}{f(s)}\,ds
=N_Z(C)-N_P(C),
\]

kde se nuly a póly počítají s násobností. Totéž celé číslo je číslem obtáčení uzavřené křivky \(f(C)\) kolem počátku:

\[
\operatorname{wind}(f(C),0)=\frac{1}{2\pi}\Delta_C\arg f.
\]

Pro \(f=\zeta\) vrací kontura obepínající \(s=1\) počet uzavřených nul funkce zeta minus jedna. Pro doplněnou celou funkci ksí

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]

počítá tentýž integrál netriviální nulové body bez odečítání pólu.

<a id="b2-what-winding-cannot-do"></a>
### B.2 Co obtáčení nedokazuje

Princip argumentu počítá nulové body v oblasti; sám o sobě je nenutí ležet na její ose symetrie. Kontura rozdělená kolem kritické přímky může dokázat RH jen tehdy, když další odhad ukáže nulový počet nul v \(\Re s>1/2\), nebo když jiná věta přinutí všechny započtené nuly ležet na \(\Re s=1/2\). Samotná symetrie funkcionální rovnice připouští dvojice \(\rho\) a \(1-\rho\) mimo přímku.

Konstrukce UBT založená na obtáčení nebo fázi proto musí dodat novou analytickou složku — například pozitivitu, monotonicitu, odhad oblasti bez nul nebo skutečně samosdruženou spektrální identifikaci — a nestačí pouze znovu získat klasický počítací integrál.

<a id="part-c"></a>
## C. Möbiova/Mertensova ekvivalence a most Dirichletovy algebry

<a id="c1-dirichlet-series"></a>
### C.1 Převrácená zeta a parciální sumace

Absolutní konvergence pro \(\Re s>1\) dává

\[
\frac1{\zeta(s)}=\sum_{n\ge1}\frac{\mu(n)}{n^s}.
\]

Abelova parciální sumace poskytuje, zpočátku pro \(\Re s>1\),

\[
\sum_{n\ge1}\frac{\mu(n)}{n^s}
=s\int_1^\infty M(x)x^{-s-1}\,dx,
\]

za předpokladu, že hraniční člen \(M(X)X^{-s}\) konverguje k nule. Přesněji, pro konečné \(X\) platí

\[
\sum_{n\le X}\frac{\mu(n)}{n^s}
=M(X)X^{-s}+s\int_1^X M(x)x^{-s-1}\,dx.
\]

Klasická Mertensova formulace zní

\[
\boxed{\;\mathrm{RH}\iff
(\forall\varepsilon>0)\quad
M(x)=O_\varepsilon\!\left(x^{1/2+\varepsilon}\right).\;}
\]

Dopředná i zpětná implikace používají analytické pokračování a standardní konturové/Perronovy argumenty; zobrazený integrál vysvětluje práh exponentu, ale sám o sobě není úplným důkazem obou směrů.

<a id="c2-formal-dirichlet-algebra"></a>
### C.2 Formální operátorové značení

Zaveďme formální bázové prvky \(D_n\) s násobením

\[
D_mD_n=D_{mn},\qquad D_1=1.
\]

Násobení řad koeficientů je potom Dirichletovou konvolucí. V doplněné formální Dirichletově algebře, kde ke každému koeficientu přispívá jen konečně mnoho dělitelů, definujme

\[
\mathcal Z:=\sum_{n\ge1}D_n.
\]

Protože \(1*\mu=\varepsilon\), platí

\[
\boxed{\;\mathcal Z^{-1}=\sum_{n\ge1}\mu(n)D_n.\;}
\]

Nechť je derivace \(\delta\) definována vztahem \(\delta D_n=(\log n)D_n\). Potom

\[
\mathcal Z^{-1}\delta\mathcal Z
=\sum_{n\ge1}(\mu*\log)(n)D_n
=\sum_{n\ge1}\Lambda(n)D_n,
\]

protože

\[
\boxed{\;\Lambda=\mu*\log.\;}
\]

Při Mellinově charakteru \(D_n\mapsto n^{-s}\), který analyticky platí pro \(\Re s>1\), přecházejí tyto formální identity na

\[
\mathcal Z\mapsto\zeta(s),\qquad
\delta\mathcal Z\mapsto-\zeta'(s),\qquad
\mathcal Z^{-1}\delta\mathcal Z\mapsto-\frac{\zeta'(s)}{\zeta(s)}
=\sum_{n\ge1}\frac{\Lambda(n)}{n^s}.
\]

Uvedená inverze je formální inverzí vzhledem k Dirichletově konvoluci. Není automaticky inverzí omezeného operátoru na Hilbertově prostoru UBT. Každá operátorová interpretace musí samostatně určit prostor, definiční obor, uzávěr, konvergenci a spektrum.

<a id="part-d"></a>
## D. Vztah k současné RH/theta–Mellinově cestě UBT

<a id="d1-variable-map"></a>
### D.1 Přesné zobrazení proměnných

Současný redukovaný most používá

\[
S(t,\psi)=\sum_{n\ge1}a_ne^{-\pi\psi n^2}e^{i\pi t n^2}
\]

a pro \(t=0\) a jednotkové váhy platí

\[
\int_0^\infty \psi^{w-1}S(0,\psi)\,d\psi
=\Gamma(w)\pi^{-w}\zeta(2w).
\]

Klasická proměnná zeta z částí A–C je tedy

\[
s=2w.
\]

Kritická přímka RH \(\Re s=1/2\) se proto zobrazuje na \(\Re w=1/4\), nikoli na \(\Re w=1/2\). Dále

\[
-\frac{d}{dw}\log\zeta(2w)
=-2\frac{\zeta'(2w)}{\zeta(2w)}
=2\sum_{n\ge1}\frac{\Lambda(n)}{n^{2w}},
\qquad \Re w>1/2.
\]

Je-li řada přes mocniny prvočísel zapsána bez faktoru \(2\), čárka označuje derivaci podle argumentu zeta \(s=2w\), nikoli derivaci podle \(w\).

<a id="d2-admissible-bridge"></a>
### D.2 Co by představovalo necirkulární most UBT

Uvedené identity nabízejí dva přesné, navzájem neekvivalentní cíle:

1. odvodit z kanonické dynamiky UBT objekt, jehož Dirichletovy koeficienty jsou \(\mu(n)\), a poté dokázat odhad \(M(x)=O_\varepsilon(x^{1/2+\varepsilon})\); nebo
2. odvodit operátor či determinant, jehož logaritmická derivace má koeficienty \(\Lambda(n)\) a jehož analytické vlastnosti, pozitivita nebo samosdruženost vylučují nuly v \(\Re s>1/2\).

Definovat formální algebru \(D_n\), dosadit \(\mu\) nebo \(\Lambda\) ručně nebo použít Mellinovu inverzi na známou identitu zeta není odvozením z UBT. Koeficienty musí vzniknout z kanonické akce, dokázaného theta/revival mechanismu nebo odvozené stopové/orbitální struktury bez použití nul zeta jako vstupu.

<a id="d3-current-verdict"></a>
### D.3 Současný verdikt a otevřená mezera

Tvrzení o reziduích, obtáčení, Möbiově a Mertensově funkci a logaritmické derivaci jsou zavedenou klasickou matematikou. Zpřesňují cíl, ale neuzavírají současné mezery UBT `GAP-THETA-PROP` a `GAP-THETA-PRIME-1`.

**GAP-RH-MOEBIUS-UBT:** odvodit z kanonických rovnic pole nebo akce UBT nepostselektovaný mechanismus vytvářející Möbiův odhad rušení nebo ekvivalentní tvrzení o oblasti bez nul či spektru. Dokud tato mezera nebude uzavřena, jde o výzkumný program, nikoli o důkaz RH.

<a id="verification"></a>
## Ověření

| Tvrzení / rovnice | Analytický status | Nástroj a artefakt | Výsledek a rozsah | Omezení | Status Lean |
|---|---|---|---|---|---|
| \(\mathcal Z^{-1}=\sum\mu(n)D_n\) | klasická přesná identita | kontrola v Pythonu s přesnými celými čísly, `tools/verify_residue_moebius_argument_principle.py` | ověřuje \(1*\mu=\varepsilon\) do nastavitelné konečné meze | konečná kontrola koeficientů není důkazem tvrzení v nekonečné formální algebře | `LEAN-PENDING` — v repozitáři není formalizace doplněné Dirichletovy algebry |
| \(\Lambda=\mu*\log\) | klasická přesná identita | kontrola v čistém Pythonu bez závislostí, tentýž artefakt | ověřuje koeficienty exaktně jako vektory prvočíselných exponentů do nastavitelné meze | konečná kontrola koeficientů není nekonečným důkazem | `LEAN-PENDING` — přesná věta o aritmetických funkcích zde dosud není formalizována |
| konečná identita Abelovy sumace | klasická přesná identita | kontrola komplexní aritmetiky v čistém Pythonu bez závislostí, tentýž artefakt | porovnává oba konečné výrazy v ne­reálném \(s\) | pouze výběrové numerické vyhodnocení | `LEAN-PENDING` — analytická formalizace v repozitáři není přítomna |
| znaménka reziduí a obtáčení | klasická komplexní analýza | diagnostika pomocí Hasseovy řady bez závislostí, tentýž artefakt | kontroluje malé kontury kolem \(s=1\) a první netriviální nuly | používá konečně přesné vyhodnocení zeta a známou aproximaci nuly | `LEAN-PENDING` — formalizace komplexně analytické funkce zeta v repozitáři není přítomna |

Tato poznámka neoznačuje za ověřený žádný specifický most UBT. Kontrolní skript testuje pouze vybrané klasické důsledky, které jsou v něm zakódovány.

<a id="references"></a>
## Literatura

1. T. M. Apostol, *Introduction to Analytic Number Theory*, Springer, 1976.
2. E. C. Titchmarsh, revidoval D. R. Heath-Brown, *The Theory of the Riemann Zeta-function*, 2. vyd., Oxford University Press, 1986.
3. `research_tracks/theta_spectral/theta_mellin_feynman_prime_synthesis_2026-08-19.md`.
4. `research_tracks/rh_trace_formula/README.md`.
