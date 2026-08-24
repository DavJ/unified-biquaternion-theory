<!-- BILINGUAL-UNIT: composite-eh.provenance -->
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

# Řetězové kritérium pro kompozitní Einsteinovu–Hilbertovu akci Theta

<!-- BILINGUAL-UNIT: composite-eh.question -->
## Otázka

Přímým kandidátem vyššího jetu pro program jediného pole je

\[
S_{\rm cEH}[\Theta]
 =c\int d^4x\sqrt{-g[\Theta]}\,(R[g[\Theta]]-2\Lambda).
\]

Jakmile je úplně definováno kovariantní zobrazení `Theta -> g[Theta]`, jde
formálně o funkcionál pouze pole `Theta`. Tato poznámka zapisuje přesnou
podmínku, za níž je variace tohoto složeného funkcionálu ekvivalentní
Einsteinově rovnici. Pouhé zapsání kompozice ještě takovým důkazem není.

<!-- BILINGUAL-UNIT: composite-eh.chain -->
## Přesná věta o řetězovém pravidle [L0]

Označme `Phi` zobrazení pole na metriku a `L_Theta=D Phi_Theta` jeho
linearizaci,

\[
\delta g=L_\Theta\,\delta\Theta.
\]

Po odstranění nebo fixaci standardního hraničního členu
Einsteinovy–Hilbertovy akce pišme ve vakuu

\[
\delta S_{\rm EH}
 =c\int d^4x\sqrt{-g}\,\mathcal E^{\mu\nu}\delta g_{\mu\nu},
\qquad
\mathcal E^{\mu\nu}=G^{\mu\nu}+\Lambda g^{\mu\nu}.
\]

Dosazení kompozitní variace a integrace per partes dávají

\[
\boxed{\frac{\delta S_{\rm cEH}}{\delta\Theta}
       =c\,L_\Theta^*\mathcal E.}
\]

Proto

\[
\mathcal E=0\Longrightarrow \frac{\delta S_{\rm cEH}}{\delta\Theta}=0,
\]

ale opačná implikace platí jen tehdy, když má formální adjungovaný operátor
`L_Theta^*` triviální jádro na uvažovaném fyzickém sektoru symetrických
tenzorů:

\[
\boxed{\ker L_\Theta^*\big|_{\rm phys}=\{0\}.}
\]

Bodová hodnost deset algebraického zobrazení tetrády na metriku tuto
injektivitu diferenciálního operátoru nedokazuje. Ta zahrnuje integrabilitu,
hraniční podmínky, konexi, gauge strukturu a diferenciální symbol.

<!-- BILINGUAL-UNIT: composite-eh.gradient -->
## Přesná obstrukce čistého gradientu [L0]

Rozdíl je vidět už v nejjednodušší větvi se čtyřmi reálnými komponentami a
čistě derivační tetrádou,

\[
e_\mu{}^a=\partial_\mu X^a.
\]

Na nedegenerovaném patchi je `X` lokálním souřadnicovým zobrazením a

\[
g_{\mu\nu}=\eta_{ab}\partial_\mu X^a\partial_\nu X^b=X^*\eta.
\]

Metrika je tedy lokálně plochá. Kolem afinního pozadí
`X^a=E_\mu{}^a x^\mu` definujme

\[
\xi_\nu:=\eta_{ab}E_\nu{}^a\delta X^b.
\]

Pak přesně platí

\[
\boxed{\delta g_{\mu\nu}
 =\partial_\mu\xi_\nu+\partial_\nu\xi_\mu,}
\]

tedy čistý infinitezimální difeomorfismus. Následně

\[
\int \mathcal E^{\mu\nu}\delta g_{\mu\nu}
 =-2\int (\partial_\mu\mathcal E^{\mu\nu})\xi_\nu
 +\text{boundary},
\]

což pro Einsteinův tensor identicky mizí díky Bianchiho identitě. Složená EH
akce proto na této čistě gradientové větvi nedává nezávislou rovnici pro `X`.
Jde o variační protějšek známé ploché integrabilitní obstrukce.

<!-- BILINGUAL-UNIT: composite-eh.split -->
## Důsledek pro split-jet větev

Split-jet pravá inverze obchází obstrukci čistého gradientu tím, že dovoluje
libovolnou tetrádu a rekonstruuje kompozitní jetovou konexi. Existující pravá
inverze však používá tetrádu jako vstup. Pokud se potom `e` variuje jako
nezávislé pole v Einsteinově–Hilbertově nebo Palatiniho akci, GR plyne, ale
mikroskopická teorie obsahuje nezávisle variovanou geometrickou proměnnou,
pokud dodatečná věta neeliminuje tuto proměnnou jako funkcionál jediného
fundamentálního `Theta`.

Pomocný split-jet multiplikátor dokazuje nepropagaci jetových proměnných;
nečiní z Einsteinovy tetrády jednoznačný lokální funkcionál `Theta`. Právě
surjektivita pravé inverze je důvod, proč čisté omezení metriku nevybírá.

<!-- BILINGUAL-UNIT: composite-eh.target -->
## Nový minimální cíl uzavření

Přímé mikroskopické uzavření vyššího jetu musí dodat **obojí**:

1. lokální kovariantní zobrazení `Theta -> g[Theta]`, které umožňuje nenulovou
   obecnou křivost bez nezávisle propagující tetrády/konexe; a
2. důkaz, že `L_Theta^*` je injektivní na fyzickém sektoru Einsteinových rovnic
   (nebo ekvivalentní větu, že Eulerova–Lagrangeova rovnice pro `Theta` je
   přesně Einsteinovou rovnicí modulo gauge identity).

Teprve po důkazu této věty složený Einsteinův–Hilbertův funkcionál uzavírá
dynamickou implikaci. Jeho celkový koeficient `c` zůstává samostatným problémem
výběru/normalizace, pokud jej neurčí tentýž mikroskopický princip.

<!-- BILINGUAL-UNIT: composite-eh.status -->
## Status

**COMPOSITE EH FORM: ADMISSIBLE CANDIDATE; DYNAMICAL EQUIVALENCE OPEN.**

Přesné kritérium řetězového pravidla uzavírá logickou nejasnost, ale nepovyšuje
`UBT-FUND-GR-ACTION`. Vylučuje úsudek „`S_EH[g(Theta)]` je pouze z Theta, tedy
variace podle Theta dává všechny Einsteinovy rovnice“, dokud není dodána věta
o injektivitě adjungovaného operátoru.
