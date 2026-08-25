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

# Gradovaný prvočíselný Fockův most k Möbiově funkci

**Datum:** 2026-08-25  
**Status:** klasické konečné/nekonečné Fockovy identity jsou zavedené; odvození prvočíselných módů, gradování a rušení na úrovni potřebné pro RH z UBT zůstává otevřené.  
**Vztah:** rozšiřuje existující bosonickou prvočíselnou Fockovu konstrukci beze změny statusu jejích tvrzení.

<a id="gm-scope"></a>
## 1. Otázka a hranice tvrzení

Existující prvočíselná Fockova větev používá jeden bosonický oscilátor pro každé prvočíslo a získává

\[
Z_P^+(s)=\prod_{p\in P}(1-p^{-s})^{-1}.
\]

Tato poznámka hledá přesný gradovaný protějšek, jehož koeficienty tvoří Möbiovu funkci. Odpověď je standardní: neomezené bosonické obsazení se nahradí fermionickým obsazením \(0/1\) a vezme se superstopa. Tím se zavádí algebraický mechanismus, ale prvočíselně indexované módy ani fermionická parita se neodvozují z kanonické UBT.

Konstrukce proto řeší algebraickou část GAP-RH-MOEBIUS-UBT. Nedokazuje RH a neuzavírá most UBT.

<a id="gm-finite-space"></a>
## 2. Konečný gradovaný prvočíselný Fockův prostor

Nechť \(P\) je konečná množina prvočísel. Pro každé \(p\in P\) definujme

\[
\mathcal F_p^-:=\operatorname{span}\{|0\rangle_p,|1\rangle_p\}\cong\mathbb C^2,
\qquad
N_p|\varepsilon_p\rangle_p=\varepsilon_p|\varepsilon_p\rangle_p,
\quad \varepsilon_p\in\{0,1\}.
\]

Konečný fermionický prvočíselný Fockův prostor a jeho hamiltonián jsou

\[
\mathcal F_P^-:=\bigotimes_{p\in P}\mathcal F_p^-,
\qquad
H_P^-:=\sum_{p\in P}(\log p)N_p.
\]

Celkový počet fermionů a paritu definujme vztahy

\[
F_P:=\sum_{p\in P}N_p,
\qquad
(-1)^{F_P}|(\varepsilon_p)\rangle
=(-1)^{\sum_p\varepsilon_p}|(\varepsilon_p)\rangle.
\]

Každý bázový stav odpovídá bezčtvercovému celému číslu

\[
n=\prod_{p\in P}p^{\varepsilon_p}.
\]

Opakované prvočíselné faktory se nevyskytují, protože \(\varepsilon_p\le1\).

<a id="gm-supertrace-theorem"></a>
## 3. Věta o gradované partiční funkci

**Věta GM-1 (konečná gradovaná identita; standardní).** Pro každou konečnou množinu \(P\) a každé \(s\in\mathbb C\) platí

\[
\boxed{
Z_P^-(s)
:=\operatorname{Str}_{\mathcal F_P^-}(e^{-sH_P^-})
=\operatorname{Tr}_{\mathcal F_P^-}\!\left((-1)^{F_P}e^{-sH_P^-}\right)
=\prod_{p\in P}(1-p^{-s})
=\sum_{\substack{n\ \mathrm{square\!-\!free}\\p\mid n\Rightarrow p\in P}}
\frac{\mu(n)}{n^s}.
}
\]

**Důkaz.** Hamiltonián a parita se rozkládají na komutující jednoprvkové faktory. Na \(\mathcal F_p^-\) platí

\[
\operatorname{Tr}_{\mathcal F_p^-}\!\left((-1)^{N_p}e^{-s(\log p)N_p}\right)
=1-p^{-s}.
\]

Faktorizace stopy na tenzorovém součinu dává součin. Jeho rozvoj vybírá podmnožinu \(S\subseteq P\); zvolené číslo \(n=\prod_{p\in S}p\) má koeficient \((-1)^{|S|}=\mu(n)\). \(\square\)

Obyčejná fermionická stopa je naproti tomu

\[
\operatorname{Tr}_{\mathcal F_P^-}(e^{-sH_P^-})
=\prod_{p\in P}(1+p^{-s}).
\]

Samotný vylučovací princip tedy nevytváří \(1/\zeta\); vložení parity a superstopa jsou nezbytné.

<a id="gm-boson-fermion-inverse"></a>
## 4. Přesná inverze bosonického sektoru

Pro tutéž konečnou množinu prvočísel splňují existující bosonický faktor a nový gradovaný faktor

\[
\boxed{Z_P^+(s)Z_P^-(s)=1.}
\]

Ve formální Dirichletově algebře s \(D_mD_n=D_{mn}\) platí

\[
\prod_{p\in P}(1-D_p)
=\sum_{S\subseteq P}(-1)^{|S|}D_{\prod_{p\in S}p}
=\sum_{\substack{n\ \mathrm{square\!-\!free}\\p\mid n\Rightarrow p\in P}}\mu(n)D_n.
\]

Když \(P\) roste přes všechna prvočísla, dává absolutní konvergence pro \(\Re s>1\) klasickou identitu

\[
\boxed{
Z^-(s)=\prod_p(1-p^{-s})=\frac1{\zeta(s)}
=\sum_{n\ge1}\frac{\mu(n)}{n^s},
\qquad \Re s>1.
}
\]

Jde o přesnou realizaci formální inverze z předchozí poznámky o reziduích a Möbiově funkci. Dokud nebudou její stupně volnosti odvozeny z UBT, zůstává standardní aritmetickou/Fockovou konstrukcí.

<a id="gm-theta-revival-interface"></a>
## 5. Rozhraní s theta revivaly

Redukovaný theta most v racionálním čase \(t=a/q\) je uspořádán kvadratickými Gaussovými součty. Jejich čínsko-zbytková faktorizace pro \(\gcd(q_1,q_2)=1\),

\[
g(a,q_1q_2)=g(aq_2,q_1)g(aq_1,q_2),
\]

ukazuje, že sektory s nesoudělnými jmenovateli se násobí. Mocniny prvočísel jsou lokálními nerozložitelnými aritmetickými bloky této faktorizace.

Toto pozorování poskytuje kandidátní rozhraní, nikoli odvození:

\[
\text{rational theta revivals}
\rightsquigarrow
\text{coprime local factors}
\rightsquigarrow
\text{prime-mode tensor factors}
\rightsquigarrow
\text{graded determinant}.
\]

Chybějí dva netriviální kroky UBT:

1. získat prvočíselně lokální rozklad bez faktorizace \(q\) nebo vnějšího vložení prvočíselnosti;
2. odvodit kanonickou \(\mathbb Z_2\) paritu, jejíž superstopa, nikoli obyčejná stopa, je fyzikálně nebo geometricky vybrána.

Samotná existence spinorové nebo Cliffordovské struktury v UBT nestačí. Konkrétní Fockovo gradování \((-1)^{F_P}\), jeho stavový prostor a vazba na theta/revival sektor musí plynout z kanonické akce nebo dokázané redukce.

<a id="gm-circularity-gate"></a>
## 6. Podmínka necirkularity a falzifikace

Cesta projde první podmínkou necirkularity pouze tehdy, pokud platí vše následující:

| Test | Podmínka úspěchu | Význam neúspěchu |
|---|---|---|
| Původ prvočíselných módů | projektory nebo lokální sektory jsou definovány bez orákula prvočíselnosti nebo předchozího Eulerova součinu | prvočísla byla vložena ručně |
| Původ energie | \(\log p\) plyne z odvozeného operátoru/toku | požadované Dirichletovy frekvence byly postselektovány |
| Původ gradování | \((-1)^F\) plyne z kanonické symetrie, okrajových podmínek nebo sektoru vnější algebry | Möbiova znaménka byla vložena ručně |
| Bezčtvercové pravidlo | opakované lokální obsazení je dynamicky nebo algebraicky vyloučeno | \(\mu(p^2)=0\) nemá původ v UBT |
| Odhad síly RH | odvozený objekt dává \(M(x)=O_\varepsilon(x^{1/2+\varepsilon})\) nezávisle na nulách zeta | konstrukce reprodukuje \(1/\zeta\) pouze v \(\Re s>1\) |

Neúspěch kteréhokoli z prvních čtyř testů redukuje návrh na správné klasické přebalení. Jejich splnění by vytvořilo skutečný Möbiův most UBT, ale RH by stále vyžadovala pátý test.

<a id="gm-gap-ladder"></a>
## 7. Žebřík vět a mezer

| ID | Tvrzení | Status |
|---|---|---|
| GM-1 | superstopa konečných prvočíselných fermionů se rovná oříznutému Möbiovu Dirichletovu polynomu | **[STD/PROVED]** |
| GM-2 | nekonečný gradovaný součin se rovná \(1/\zeta(s)\) pro \(\Re s>1\) | **[STD/PROVED]** |
| GM-UBT-1 | odvodit prvočíselně lokální faktory z kanonické theta/revival dynamiky | **[OPEN]** |
| GM-UBT-2 | odvodit zákon obsazení \(0/1\) a vložení parity z UBT | **[OPEN]** |
| GM-UBT-3 | odvodit energie \(\log p\) bez aritmetické postselekce | **[OPEN]** |
| GM-RH | dokázat Mertensův odhad druhé odmocniny pro odvozené koeficienty | **[OPEN; silou ekvivalentní RH]** |

Jde o lokální zpřesnění GAP-RH-MOEBIUS-UBT; status žádného kanonického ani globálního tvrzení se nezvyšuje.

<a id="gm-verification"></a>
## 8. Ověření

| Tvrzení | Artefakt | Výsledek | Rozsah | Omezení | Status Lean |
|---|---|---|---|---|---|
| Identita koeficientů GM-1 | tools/verify_graded_mobius_bridge.py | exaktní úspěch pomocí výčtu podmnožin, rozvoje součinu a nezávislé faktorizace | nastavitelné konečné množiny prvočísel | konečná kontrola doplňuje, ale nenahrazuje analytický důkaz | LEAN-PENDING — v repozitáři není formalizace gradované Fockovy konstrukce |
| Konečná Dirichletova inverze | tentýž artefakt | exaktní úspěch konvoluce do nastavitelné meze | konečné aritmetické koeficienty | nejde o výsledek analytického pokračování | LEAN-PENDING |
| \(Z_P^+Z_P^-=1\) | tentýž artefakt | úspěch ve floating-point aritmetice pro několik reálných \(s>1\) | konečné součiny | neřeší kritický pás | LEAN-PENDING |
| Přibližování k \(1/\zeta(2)=6/\pi^2\) | tentýž artefakt | deterministická numerická kontrola konvergence | jeden klasický benchmark | numerická konvergence není důkazem GM-2 | NOT-APPLICABLE |

Žádný otevřený krok specifický pro UBT není označen za ověřený.

<a id="gm-next-experiment"></a>
## 9. Následující experiment

Následující přípustný experiment musí vyjít z dat racionálních theta revivalů indexovaných \(q\), sestrojit kandidátní lokální projektory bez volání síta prvočísel uvnitř konstrukce a otestovat, zda jejich tenzorový rozklad získá bloky mocnin prvočísel. Teprve po splnění této podmínky se smí připojit gradovaný determinant.

Rozhodující negativní výsledek je rovněž cenný: pokud každý úspěšný rozklad vyžaduje explicitní faktorizaci celých čísel, revival cesta prvočíselné módy neodvodila a nemá být povýšena.
