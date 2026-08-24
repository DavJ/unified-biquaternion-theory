<!-- BILINGUAL-UNIT: equivariant-curvature-rank.provenance -->
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

# Ekvivariantní symplektické curvature dokončení: exaktní hranice hodnosti

<!-- BILINGUAL-UNIT: equivariant-curvature-rank.setup -->
## Kanonické ekvivariantní dokončení

Invariantní symplektická forma na prostoru polí `omega` a lokálně symplektické
spin+phase působení definují standardní kvadratickou momentovou mapu. Pro každý
Lieův generátor `T_r` zvolme konvenci

\[
\boxed{\mu_r(\Theta)=\frac12\omega(T_r\Theta,\Theta).}
\]

Identita symplektického generátoru implikuje

\[
D\mu_r=\omega(T_r\Theta,D\Theta).
\]

S

\[
Q=\frac12\omega(D\Theta\wedge D\Theta),
\qquad
D^2\Theta=\mathcal F^rT_r\Theta,
\]

dostáváme

\[
dQ=D\mu_r\wedge\mathcal F^r,
\]

kde kontrakce adjungovaného a koadjungovaného indexu je gauge invariantní a
Bianchiho identita dává `D mathcal F=0`. Proto

\[
\boxed{\widehat Q:=Q-\mu_r\mathcal F^r,
\qquad d\widehat Q=0.}
\]

To je důležité: křivost může vstoupit do UBT-native gauge-kovariantní exterior
formy bez ručního vložení Einsteinova–Hilbertova skaláru.

<!-- BILINGUAL-UNIT: equivariant-curvature-rank.linear -->
## Člen lineární v křivosti

Uvažujme nejjednodušší skalární akci vytvořenou z této uzavřené dvouformy,

\[
S_{\rm eq}=\frac12\int F(\Theta)\,\widehat Q\wedge\widehat Q,
\]

s invariantním skalárem `F`. Rozvoj podle mocnin křivosti dává

\[
S_{\rm eq}
=\frac12\int FQ\wedge Q
-\int F\mu_rQ\wedge\mathcal F^r
+\frac12\int F\mu_r\mu_s\mathcal F^r\wedge\mathcal F^s.
\]

Koeficient členu lineárního v Lorentzově křivosti je tedy

\[
\boxed{B_r^{\rm eq}=-F\mu_rQ.}
\]

Pro pevné `Theta` jsou všech šest Lorentzovsky označených dvouforem skalárními
násobky **téže** prostorové dvouformy `Q`. Zobrazení

\[
\mathfrak{so}(1,3)\longrightarrow\Lambda^2T^*M,
\qquad
T_r\longmapsto B_r^{\rm eq}
\]

má proto hodnost nejvýše jedna.

<!-- BILINGUAL-UNIT: equivariant-curvature-rank.palatini -->
## Palatini vyžaduje hodnost šest [L0]

Pro nedegenerovanou tetrádu je Hilbertův–Palatiniho koeficient křivosti

\[
\boxed{B_{ab}^{\rm HP}=\frac12\epsilon_{abcd}E^c\wedge E^d.}
\]

Koframe `E^a` identifikuje šestirozměrný vnitřní prostor bivectorů se
šestirozměrným prostorem časoprostorových dvouforem. Vnitřní Hodgeova dualita
přes `epsilon_{abcd}` je invertibilní. Proto

\[
\boxed{\operatorname{rank}(B^{\rm HP})=6}
\]

pro každou nedegenerovanou tetrádu.

`tools/verify_equivariant_symplectic_curvature_rank.py` dává exaktní konečný
certifikát: pro celočíselnou tetrádu s determinantem `24` má výsledná `6 x 6`
Palatiniho bivectorová matice nenulový determinant a hodnost šest, zatímco
libovolný skalární outer-product koeficient `mu_r Q` má hodnost jedna.

<!-- BILINGUAL-UNIT: equivariant-curvature-rank.no-go -->
## Exaktní no-go pro nejjednodušší skalární dokončení [L1]

Nesoulad hodností je invariantní vůči regulárním změnám báze Lorentzových i
časoprostorových dvouforem. Na větvi s nedegenerovanou tetrádou tedy

\[
\boxed{B_r^{\rm eq}\ne B_r^{\rm HP}}
\]

pro úplnou množinu Lorentzových curvature složek. Žádná volba skalární funkce
`F`, hodnot momentové mapy `mu_r` ani nenulové dvouformy `Q` nemůže zvýšit
rank-one faktorizaci na hodnost šest.

Proto:

**NEJJEDNODUŠŠÍ SKALÁRNÍ EKVIVARIANTNÍ DOKONČENÍ
`F (Q - <mu,Fcurv>)^2/2` NEMŮŽE GENEROVAT HILBERTŮV–PALATINIHO ČLEN
LINEÁRNÍ V KŘIVOSTI NA NEDEGENEROVANÉ ČTYŘROZMĚRNÉ TETRÁDĚ.**

To ekvivariantní konstrukci neznehodnocuje. Přesně identifikuje, co chybí:
**Lie-algebra/bivectorová dvouforma nesoucí šest nezávislých curvature
koeficientů**, nikoli jediná skalární časoprostorová dvouforma násobená šesti
čísly momentové mapy.

<!-- BILINGUAL-UNIT: equivariant-curvature-rank.next -->
## Další UBT-native objekt už existuje

Kanonická Lorentzova tetráda má antisymetrického biquaternionického partnera

\[
\Sigma_{\mu\nu}
=\frac12(E_\mu^\sharp E_\nu-E_\nu^\sharp E_\mu),
\]

a kanonický Cliffordův lift poskytuje odpovídající bivectorovou algebru. Na
rozdíl od skalárního `Q` může tento objekt nést úplný šestirozměrný Lorentzův
bivector. Další test původu curvature členu proto musí použít
**bivectorový `E wedge E` / Cliffordův partner**, ideálně v již zavedené
split-jet architektuře oddělující jetovou konexi od fyzické Palatiniho konexe.

Věta o hodnosti zatím neurčuje jedinečnou akci ani její normalizaci. Říká, že
skalární symplektická cesta je příliš malá, a určuje minimální reprezentační
obsah potřebný pro životaschopný curvature coupling.

<!-- BILINGUAL-UNIT: equivariant-curvature-rank.verification -->
## Ověření

Exaktní spustitelná kontrola:

`tools/verify_equivariant_symplectic_curvature_rank.py`

Ověřuje hodnost šest Palatiniho mapy na exaktní nedegenerované tetrádě a
rank-one outer-product strukturu skalárního ekvivariantního koeficientu.
Odvození `d Qhat=0` pomocí diferenciálních forem je analytické. Formalizace v
Leanu je `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: equivariant-curvature-rank.status -->
## Stav

**VSTUP KŘIVOSTI PŘES EKVIVARIANTNÍ SYMPLEKTICKOU FORMU: AVAILABLE [L1].**

**NEJJEDNODUŠŠÍ SKALÁRNÍ EKVIVARIANTNÍ DOKONČENÍ JAKO PŮVOD PALATINIHO ČLENU:
CLOSED AS NO-GO [L1].**

**BIVECTOROVÝ/CLIFFORDŮV PŮVOD KŘIVOSTI A NORMALIZACE: OPEN.**
