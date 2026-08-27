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

# Dvoustranný renormalizovaný Eulerův součin a podmínka prvočíselné nelokality

**Větev:** `research_tracks/prime_fock_operator`
**Status:** klasická dvouchartová faktorizace dokázána; operátor na hranici kritické přímky a původ v UBT otevřeny
**Úroveň důkazu:** standardní analytická matematika plus deterministické konečné/numerické kontroly; `LEAN-PENDING`
**Rozsah:** výzkumný audit; beze změny kanonického statusu UBT a bez tvrzení RH

<a id="tre-purpose"></a>
## 1. Účel a rozhodovací hranice

Audit adelických valuací ztotožňuje radiální stopu konečných míst s Eulerovým součinem v jeho konvergentní polorovině. Tato poznámka zkoumá, zda se formální rovnice

\[
\prod_p\left(\sum_{m\geq0}p^{-ms}\right)=0
\]

může stát cestou k netriviálním nulám. Odpověď je přesná. Surový součin je nenulový tam, kde konverguje absolutně, zatímco v kritickém pásu není oprávněnou definicí zety. Užitečné pokračování musí nejprve odstranit konečný počet divergentních vrstev prvočíselných mocnin a musí zacházet s oběma stranami kritické přímky jako se samostatnými charty propojenými funkcionální rovnicí.

Výsledná konstrukce je informativní, ale není důkazem RH. Izoluje jediný skutečně obtížný člen: první prvočíselnou vrstvu

\[
P(s)=\sum_p p^{-s}.
\]

Všechny vyšší lokální vrstvy lze libovolně blízko kritické přímky reprezentovat normově konvergentním nelokálním operátorem translací. Nerenormalizovanou první vrstvu tak reprezentovat nelze.

<a id="tre-raw-product"></a>
## 2. Surový součin nemůže ve svém stopovém oboru vymizet

Pro každé pevné prvočíslo a \(\Re s>0\) platí

\[
Z_p(s)=\sum_{m\geq0}p^{-ms}=\frac{1}{1-p^{-s}}.
\]

Pro \(\Re s>1\) platí

\[
Z_{\mathrm{fin}}(s)
=\prod_p Z_p(s)
=\prod_p\frac{1}{1-p^{-s}}
=\zeta(s).
\]

Každý lokální faktor je nenulový a logaritmus součinu konverguje absolutně. Tedy

\[
\boxed{Z_{\mathrm{fin}}(s)\neq0\qquad(\Re s>1).}
\]

Konečná useknutí množiny prvočísel také nikdy nejsou nulová. Mimo polorovinu absolutní konvergence tato useknutí kanonicky nedefinují analytické pokračování. Netriviální nula zety je proto globální překážkou holomorfního logaritmu, nikoli vymizením některého lokálního geometrického součtu.

<a id="tre-maclaurin-subtraction"></a>
## 3. Konečné Maclaurinovo odečtení

Pro celé \(M\geq1\) definujme

\[
R_M(s)=
\prod_p
\frac{1}{1-p^{-s}}
\exp\left(-\sum_{m=1}^{M}\frac{p^{-ms}}{m}\right).
\]

Jeho logaritmus je

\[
\log R_M(s)
=\sum_p\sum_{m=M+1}^{\infty}\frac{p^{-ms}}{m}.
\]

Tato dvojitá řada konverguje absolutně a lokálně stejnoměrně, pokud

\[
\Re s>\frac{1}{M+1}.
\]

Proto je \(R_M\) v této polorovině holomorfní a nenulová. Zpočátku pro \(\Re s>1\) platí

\[
\boxed{
\zeta(s)=R_M(s)
\exp\left(\sum_{m=1}^{M}\frac{P(ms)}{m}\right).
}
\]

Zvyšování \(M\) posouvá absolutně konvergentní zbytek směrem k \(\Re s=0\), ale neodstraňuje potřebu pokračovat konečný počet členů prvočíselné zeta funkce \(P(ms)\). To je přesný obsah myšlenky nekonečného Maclaurinova rozvoje: odděluje konvergentní lokální chvosty od globálních singulárních vrstev, ale nedokazuje regularitu těchto vrstev.

<a id="tre-right-chart"></a>
## 4. Pravý chart

Prvním užitečným případem je

\[
R_1(s)=\prod_p\frac{e^{-p^{-s}}}{1-p^{-s}},
\qquad
\log R_1(s)=\sum_p\sum_{m\geq2}\frac{p^{-ms}}{m}.
\]

Funkce \(R_1\) je tedy holomorfní a nenulová pro \(\Re s>1/2\). Na každé jednoduše souvislé oblasti \(U\) v této polorovině, která neobsahuje \(s=1\) ani nuly zety, s konzistentní větví logaritmu, platí

\[
\zeta(s)=R_1(s)e^{P(s)}.
\]

Identita

\[
\log\zeta(s)=P(s)+\sum_{m\geq2}\frac{P(ms)}{m}
\]

ukazuje, že chvost je holomorfní pro \(\Re s>1/2\). V okolí \(V_\rho\) nuly \(\rho\) násobnosti \(m_\rho\) v této otevřené polorovině proto platí

\[
P(s)=m_\rho\log(s-\rho)+h_\rho(s),
\qquad h_\rho\in\mathcal O(V_\rho),
\]

Prvočíselná zeta funkce má také logaritmickou singularitu vyvolanou pólem v \(s=1\). RH je tedy ekvivalentně přeformulována jako neexistence jakéhokoli dalšího logaritmického bodu větvení \(P(s)\) v \(\Re s>1/2\). Tato ekvivalence je klasickým přeformulováním, nikoli pokrokem v důkazu požadované neexistence.

<a id="tre-left-chart"></a>
## 5. Levý chart není vynechán

Použijme celou dokončenou funkci

\[
\xi(s)=C(s)\zeta(s),
\qquad
C(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2),
\qquad
\xi(s)=\xi(1-s).
\]

Oba chartové zápisy jsou

\[
\boxed{
\xi(s)=C(s)R_1(s)e^{P(s)},
\qquad \Re s>\frac12,
}
\]

a

\[
\boxed{
\xi(s)=C(1-s)R_1(1-s)e^{P(1-s)},
\qquad \Re s<\frac12.
}
\]

Druhý zbytek konverguje absolutně, protože \(\Re(1-s)>1/2\). Pro \(\Re s<0\) je dokonce \(P(1-s)\) reprezentována svou obyčejnou konvergentní prvočíselnou řadou. V levé polovině kritického pásu, \(0<\Re s<1/2\), je jediným problémem pokračování odražená prvočíselná vrstva \(P(1-s)\).

Tato formulace také neinterpretuje triviální nuly zety jako spektrální nuly: gama faktor je ve \(\xi\) vyruší. Netriviální nula mimo kritickou přímku se vyskytuje v odražené čtveřici

\[
\{\rho,\overline\rho,1-\rho,1-\overline\rho\}.
\]

Kontrola pravého otevřeného polopásu tedy pomocí dokázané symetrie kontroluje i levý, ale levý chart zůstává v konstrukci explicitní.

<a id="tre-boundary"></a>
## 6. Kritická přímka jako společná regulovaná hranice

Pro reálné \(t\) a \(\varepsilon>0\) položme

\[
s_+(\varepsilon,t)=\frac12+\varepsilon+it,
\qquad
s_-(\varepsilon,t)=\frac12-\varepsilon+it.
\]

Potom

\[
1-s_-(\varepsilon,t)
=\frac12+\varepsilon-it
=\overline{s_+(\varepsilon,t)},
\]

a funkcionální rovnice spolu s reálnou analytičností dává

\[
\boxed{
\xi(s_-(\varepsilon,t))
=\overline{\xi(s_+(\varepsilon,t))}.
}
\]

Obě strany tedy mají stejný modul a opačnou fázi. Limita \(\varepsilon\downarrow0\) neplyne z absolutní konvergence \(R_1\): její vedoucí zbývající vrstva má na hranici exponent \(2\Re s=1\). Každý hraniční operátor musí určit regulátor, topologii konvergence a předpis odečítání.

<a id="tre-nonlocal-operator"></a>
## 7. Exaktní rozklad nelokálního operátoru

Nechť \(U_a\) je unitární translace na \(L^2(\mathbb R)\),

\[
(U_af)(x)=f(x+a).
\]

Pro \(\varepsilon>0\) operátor vyšších vrstev

\[
B_\varepsilon
=\sum_p\sum_{m\geq2}
\frac{p^{-m(1/2+\varepsilon)}}{m}
U_{m\log p}
\]

konverguje v operátorové normě, protože součet norem koeficientů je konečný. Jeho Fourierův multiplikátor je až na konvenci znaménka Fourierovy transformace logaritmem vyšších vrstev \(\log R_1\).

První vrstva má konečná useknutí

\[
A_{\varepsilon,X}
=\sum_{p\leq X}p^{-1/2-\varepsilon}U_{\log p}.
\]

Všechny koeficienty se při nulové Fourierově frekvenci sečtou se stejnou fází, takže

\[
\boxed{
\|A_{\varepsilon,X}\|
=\sum_{p\leq X}p^{-1/2-\varepsilon}.
}
\]

Necentrovaná první vrstva proto konverguje v operátorové normě pouze v bezpečné oblasti \(\varepsilon>1/2\), ekvivalentně \(\Re s>1\). Pro \(0<\varepsilon\leq1/2\) její normy divergují. Pouhý zápis všech prvočíselných translací jako operátoru je analyticky nepokračuje.

Platný UBT/nelokální krok proto musí dodat kanonické centrování nebo renormalizaci první vrstvy a dokázat topologii dostatečně silnou ke kontrole resolventy. Nesmí vložit nuly zety do spektrálního multiplikátoru.

<a id="tre-chebyshev-gate"></a>
## 8. Čebyševův zbytek odhaluje podmínku síly RH

Nechť

\[
\psi(x)=\sum_{n\leq x}\Lambda(n).
\]

Pro \(\Re s>1\) platí

\[
-\frac{\zeta'}{\zeta}(s)
=\int_1^\infty x^{-s}\,d\psi(x)
=s\int_1^\infty\psi(x)x^{-s-1}\,dx.
\]

Po odečtení hlavního členu,

\[
\boxed{
-\frac{\zeta'}{\zeta}(s)-\frac{s}{s-1}
=s\int_1^\infty(\psi(x)-x)x^{-s-1}\,dx.
}
\]

Pokud se dokáže

\[
\psi(x)-x=O_\delta(x^{1/2+\delta})
\qquad(\delta>0),
\]

pak centrovaná transformace pokračuje s požadovanou kontrolou v celé oblasti \(\Re s>1/2\). Obráceně je tato odmocninová chyba prvočíselné věty tvrzením síly RH. Požadovaná renormalizace první vrstvy tedy není neškodným technickým detailem; její rozhodující odhad obsahuje hlavní obtíž.

<a id="tre-ledger"></a>
## 9. Přehled vět a mezer

| ID | Tvrzení | Status |
|---|---|---|
| TRE-1 | surový radiální Eulerův součin je nenulový pro \(\Re s>1\) | **[STD/PROVED]** |
| TRE-2 | \(R_M\) je holomorfní a nenulová pro \(\Re s>1/(M+1)\) | **[STD/PROVED]** |
| TRE-3 | pravý a levý chart \(\xi\) jsou přesně propojeny záměnou \(s\leftrightarrow1-s\) | **[STD/PROVED]** |
| TRE-4 | \(B_\varepsilon\) konverguje v normě pro každé \(\varepsilon>0\) | **[STD/PROVED]** |
| TRE-5 | normy necentrované první vrstvy divergují pro \(0<\varepsilon\leq1/2\) | **[STD/PROVED NO-GO]** |
| TRE-RH | zkonstruovat kanonický centrovaný operátor první vrstvy s odmocninovou kontrolou | **[OPEN; RH-strength]** |
| TRE-UBT | odvodit prvočíselné translace, centrování a zdvojenou involuci z kanonické akce UBT | **[OPEN]** |
| TRE-HP | získat samoadjungovaný operátor, jehož spektrální singularity nebo singularity resolventy jsou právě netriviální nuly | **[OPEN]** |

<a id="tre-next"></a>
## 10. Další přípustný experiment

Další experiment nemá vyčíslovat větší surové Eulerovy součiny. Má:

1. zkonstruovat konečné centrované operátory prvočíselných translací z \(\psi(x)-x\);
2. porovnat způsoby useknutí a testovat existenci na regulátoru nezávislé silné nebo resolventní limity mimo kritickou přímku;
3. zdvojit konstrukci involucí \(s\leftrightarrow1-s\), nikoli přidat levou stranu až dodatečně;
4. použít princip argumentu pro \(\xi\) ke kontrole vinutí, nikoli nuly konečných Eulerových součinů;
5. zastavit se, pokud je centrování definováno pomocí \(\zeta'/\zeta\), tabulky nul nebo předpokládané odmocninové chyby prvočísel.

Úspěch konečných numerických testů ověří pouze normalizaci a symetrii. Rozhodující větou musí být analytický odhad nezávislý na vstupu ekvivalentním RH.

<a id="tre-verification"></a>
## 11. Ověření

| Tvrzení | Artefakt/nástroj | Výsledek | Rozsah | Omezení | Status Lean |
|---|---|---|---|---|---|
| TRE-1 a konečná Maclaurinova identita | `tools/verify_two_sided_renormalized_euler.py`, Python 3.12 | prošlo | komplexní součiny konečných množin prvočísel a logaritmické vrstvy | konečné součiny nedokazují analytické pokračování | `LEAN-PENDING` — Lean není v běhovém prostředí dostupný |
| práh konvergence TRE-2 | stejný artefakt | prošlo | deterministické porovnání useknutí nad a pod vybranými prahy | numerická konvergence není lokálně stejnoměrným analytickým důkazem | `LEAN-PENDING` |
| odraz TRE-3 | stejný artefakt | prošlo | exaktní afinní odraz a známé hodnoty \(\xi(2)=\xi(-1)=\pi/6\) | jeden kontrolní bod nedokazuje funkcionální rovnici | `LEAN-PENDING` |
| TRE-4 a TRE-5 | stejný artefakt | prošlo | odhady norem koeficientů a vzorkované multiplikátory translací | konečné Fourierovy vzorky pouze doplňují analytický argument o normě | `LEAN-PENDING` |
| prvočíselné mocniny logaritmické derivace | stejný artefakt | exaktně prošlo | konečný von Mangoldtův součet proti výčtu prvočíselných mocnin | netestuje se pokračování ani poloha nul | `LEAN-PENDING` |

Žádný výsledek ověřovače neodvozuje prvočíselný operátor UBT, hraniční hodnotu na kritické přímce ani RH.

<a id="tre-references"></a>
## 12. Primární reference

- H. Davenport, *Multiplicative Number Theory*, 3rd ed., Springer, 2000.
- G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, 6th ed., Oxford University Press, 2008.
- C.-E. Fröberg, [*On the prime zeta function*](https://doi.org/10.1007/BF01933420), *BIT* **8** (1968), 187--202.
