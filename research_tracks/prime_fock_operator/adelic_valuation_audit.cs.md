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

# Audit adelických valuací a racionálních revivalů

**Větev:** `research_tracks/prime_fock_operator`  
**Status:** klasická lokálně-globální konstrukce dokázána; původ v UBT a krok Hilberta--Pólyi otevřeny  
**Úroveň důkazu:** standardní/exaktní matematika plus deterministické kontroly; `LEAN-PENDING`  
**Rozsah:** výzkumný audit; beze změny kanonického statusu UBT a bez tvrzení RH

<a id="apd-purpose"></a>
## 1. Účel a rozhodovací hranice

Tato poznámka nahrazuje posloupnost malých rozšíření theta operátorů jedním lokálně-globálním auditem. Odpovídá na tři otázky:

1. co prime-Fockova konstrukce představuje ve skutečně (p)-adickém jazyce;
2. zda se racionální theta revivaly kanonicky rozpadají na bloky prvočíselných mocnin;
3. která část výsledné struktury je standardní aritmetika a která část v kanonické UBT stále chybí.

Výsledek je smíšený, ale rozhodující. Radiální multi-prvočíselná konstrukce je exaktní, její logaritmický Hamiltonián je samoadjungovaný a fáze racionálních revivalů se přesně faktorizují pomocí čínsko-zbytkových idempotentů. Konstrukce však stále vychází z celočíselných jmenovatelů nebo lokálních míst označených prvočísly. Neodvozuje tyto aritmetické vstupy z akce UBT a nevytváří Hilbertův--Pólyův operátor.

<a id="apd-prior-audit"></a>
## 2. Audit předchozí theta--Mellinovy cesty

| Etapa | Dokázaný výsledek | Zbývající překážka |
|---|---|---|
| skalární theta konstanty | jeden zeta kanál nul v otevřeném kritickém pásu | žádná nezávislá podmínka polohy nul |
| multiplikativní charaktery modulo (5) | čtyři Dirichletovy kanály | žádné kanonické směšování hlavního kanálu s primitivním blokem |
| aditivní rezidua a eliptické derivace | kanonické sudé/liché Weilovy sektory a sektorové metriky | žádný konstantní sudě--lichý intertwiner |
| lokální Jacobiho operátory | explicitní gradovaná Diracova mapa | polynomiální spektra mají nesprávný zákon počítání |
| nekonečný funkcionální kalkul | nelokální symboly mohou vystihnout hladký zákon počítání | interpolace jednotlivými nulami je kruhová |
| regulovaná prvočíselná fáze | omezená samoadjungovaná korekce pro (sigma>1) | prvočíselné značky a (log p) byly aritmetické vstupy |

Vhodným restartem tedy není další funkce Jacobiho derivace. Je jím omezený součin všech konečných míst spolu s reálným místem.

<a id="apd-radial-space"></a>
## 3. Radiální valuační prostor

Pro každé prvočíslo (p) položme

\[
\mathcal H_p^{\mathrm{rad}}=\ell^2(\mathbb N_0),
\qquad
N_p|m\rangle_p=m|m\rangle_p.
\]

Pomocí vakuového vektoru (|0\rangle_p) vytvořme omezený tenzorový součin

\[
\mathcal H_{\mathrm{rad}}
=\bigotimes_p'\bigl(\mathcal H_p^{\mathrm{rad}},|0\rangle_p\bigr).
\]

Jeho standardní ortonormální bázi tvoří obsazovací vektory (mathbf m=(m_p)_p) s konečným nosičem. Jednoznačný rozklad na prvočísla definuje bijekci

\[
\mathbf m\longleftrightarrow
n(\mathbf m)=\prod_p p^{m_p},
\qquad
|\mathbf m\rangle\longleftrightarrow|n\rangle.
\]

Ta se rozšiřuje na unitární mapu

\[
U:\mathcal H_{\mathrm{rad}}\longrightarrow\ell^2(\mathbb N).
\]

Na vektorech s konečným nosičem nejprve definujme logaritmický Hamiltonián

\[
H_{\log}=\sum_p(\log p)N_p.
\]

Potom

\[
UH_{\log}U^{-1}|n\rangle=(\log n)|n\rangle.
\]

**Věta APD-1 (samoadjungovaný logaritmický Hamiltonián).** Uzávěr (H_{\log}) je kladný samoadjungovaný operátor násobení s definičním oborem

\[
\mathcal D(H_{\log})
=\left\{c\in\ell^2(\mathbb N):
\sum_{n\ge1}(\log n)^2|c_n|^2<\infty\right\}.
\]

Vektory s konečným nosičem tvoří jádro, protože useknutí koeficientů konvergují v grafové normě. Dřívější prime-Fockova mezera F5 je tedy na úrovni klasického operátoru uzavřena.

<a id="apd-local-trace"></a>
## 4. Lokální stopy a Eulerův součin

Pro (Re s>0) je stopa jednoho místa

\[
\operatorname{Tr}_{\mathcal H_p^{\mathrm{rad}}}
\bigl(p^{-sN_p}\bigr)
=\sum_{m\ge0}p^{-ms}
=\frac1{1-p^{-s}}.
\]

Pro konečnou množinu (P) prvočísel platí

\[
\operatorname{Tr}\exp\left(-s\sum_{p\in P}(\log p)N_p\right)
=\prod_{p\in P}\frac1{1-p^{-s}}.
\]

Úplná stopa konverguje právě v obvyklé polorovině:

\[
\boxed{
\operatorname{Tr}_{\mathcal H_{\mathrm{rad}}}(e^{-sH_{\log}})
=\sum_{n\ge1}n^{-s}
=\prod_p\frac1{1-p^{-s}}
=\zeta(s),
\qquad \Re s>1.
}
\]

**Věta APD-2 (identita radiální stopy).** Prime-Fockova partiční funkce je unitárně ekvivalentní Dirichletově stopě operátoru násobení (log n). Jde o Eulerův součin v operátorovém zápisu, nikoli o nové analytické pokračování ani o větu o spektru nul.

<a id="apd-padic-integral"></a>
## 5. Exaktní (p)-adický význam

Normalizujme multiplikativní Haarovu míru vztahem

\[
\operatorname{vol}_{d^\times x}(\mathbb Z_p^\times)=1.
\]

Rozklad na radiální slupky je

\[
\mathbb Z_p\setminus\{0\}
=\bigsqcup_{m\ge0}p^m\mathbb Z_p^\times.
\]

Protože na (m)-té slupce je (|x|_p=p^{-m}), má nerozvětvený lokální Tateův integrál tvar

\[
\boxed{
\int_{\mathbb Q_p^\times}
\mathbf1_{\mathbb Z_p}(x)|x|_p^s\,d^\times x
=\sum_{m\ge0}p^{-ms}
=\operatorname{Tr}(p^{-sN_p})
=\frac1{1-p^{-s}}.
}
\]

**Věta APD-3 (radiální Tateova ekvivalence).** Lokální prime-Fockův oscilátor je přesně radiálním sektorem triviálního charakteru (p)-adického lokálního zeta integrálu.

Nejde o celé lokální těleso. Platí

\[
\mathbb Q_p^\times\cong p^{\mathbb Z}\times\mathbb Z_p^\times.
\]

Prostor (ell^2(\mathbb N_0)) ponechává pouze nezáporné valuace vybrané funkcí (mathbf1_{\mathbb Z_p}). Rozvětvené charaktery, Gaussovy součty a Dirichletovy (L)-faktory vyžadují sektor jednotek (mathbb Z_p^\times). Dřívější kanály modulo (5) se proto přirozeně reinterpretují jako konečný kvocient sektoru jednotek v místě (p=5), nikoli jako čtyři nezávislá globální pole.

<a id="apd-archimedean"></a>
## 6. Archimédovská korekce

Při standardní normalizaci

\[
\vartheta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t},
\]

je Mellinova identita

\[
\boxed{
\frac12\int_0^\infty
\bigl(\vartheta(t)-1\bigr)t^{s/2}\frac{dt}{t}
=\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad \Re s>1.
}
\]

Mellinova transformace thety již obsahuje jak konečný Eulerův součin, tak gama faktor reálného místa. Lokální adelická faktorizace je

\[
Z_\infty(s)=\pi^{-s/2}\Gamma(s/2),
\qquad
Z_p(s)=\frac1{1-p^{-s}},
\qquad
\Lambda(s)=Z_\infty(s)\prod_p Z_p(s).
\]

Nezávislý součin tepelných stop tvaru (artheta(t)^d\zeta(t)) tedy může ve své oblasti konvergence definovat platnou partiční funkci, není však dokončenou funkcí zeta a nedává její funkcionální rovnici. Považovat jej za adelické dokončení by vzhledem k theta--Mellinově identitě znamenalo dvojí započtení konečného zeta faktoru.

<a id="apd-crt"></a>
## 7. Racionální revivaly a bloky prvočíselných mocnin

Nechť

\[
q=\prod_{j=1}^r q_j,
\qquad
q_j=p_j^{k_j},
\qquad
\gcd(q_i,q_j)=1\quad(i\ne j).
\]

Položme

\[
Q_j=q/q_j,
\qquad
u_j=Q_j^{-1}\pmod{q_j},
\qquad
e_j=Q_ju_j\pmod q.
\]

Prvky (e_j) jsou ortogonální idempotenty splňující

\[
e_i e_j=\delta_{ij}e_j\pmod q,
\qquad
\sum_j e_j=1\pmod q.
\]

Každé reziduum má jednoznačnou rekonstrukci

\[
r=\sum_j r_je_j\pmod q,
\qquad
r_j=r\pmod{q_j}.
\]

Kvadratická fáze revivalu se potom přesně faktorizuje:

\[
e^{2\pi i a r^2/q}
=\prod_j e^{2\pi i a u_j r_j^2/q_j}.
\]

Kvadratický Gaussův součet proto splňuje

\[
\boxed{
g(a,q)=\prod_j g(a u_j,q_j).
}
\]

**Věta APD-4 (konečná lokální faktorizace).** Při CRT unitární permutaci je operátor racionálního revivalu na (ell^2(\mathbb Z/q\mathbb Z)) tenzorovým součinem operátorů na prostorech prvočíselných mocnin (ell^2(\mathbb Z/p_j^{k_j}\mathbb Z)), s explicitními inverzními zvraty (u_j).

Jde o konečný předstupeň vztahu

\[
\widehat{\mathbb Z}=\prod_p\mathbb Z_p.
\]

Vysvětluje, proč jsou správnými lokálními bloky prvočíselné mocniny, nikoli libovolný modul jako (5).

<a id="apd-factorization-gate"></a>
## 8. Opravená podmínka necirkularity

Dřívější požadavek žádal získat bloky prvočíselných mocnin (q) bez faktorizace (q). Doslovně tento požadavek nelze od faktorizace odlišit.

**Věta APD-5 (podmínka faktorizujícího výstupu).** Každý postup, který vypíše maximální prvočíselné mocniny

\[
\{p^{v_p(q)}:p\mid q\}
\]

zároveň vypíše prvočíselný rozklad (q): z každé uvedené prvočíselné mocniny vezmeme její jednoznačný prvočíselný základ a exponent. Obráceně prvočíselný rozklad tyto bloky okamžitě určuje.

Fyzikálně smysluplnou podmínkou tedy není algoritmus, který skrývá faktorizaci celých čísel. Je jí:

1. odvodit racionální jmenovatele (q) nebo ekvivalentní profinitní/lokální stavový prostor z dynamiky UBT bez použití Eulerova součinu;
2. dovolit standardní CRT/Sylowově aritmetice rozložit vzniklé konečné sektory;
3. odvodit Hamiltonián a gradování na těchto sektorech z téže redukce.

V současnosti zůstává otevřen krok 1 a dynamická část kroku 3. APD-4 neuzavírá mezeru původu prvočísel v UBT.

<a id="apd-claim-control"></a>
## 9. Kontrola tvrzení a seznam mezer

| ID | Tvrzení | Status |
|---|---|---|
| APD-1 | samoadjungovaný uzávěr a jádro s konečným nosičem operátoru (H_{\log}) | **[STD/PROVED]** |
| APD-2 | prime-Fockova stopa se rovná (zeta(s)) pro (Re s>1) | **[STD/PROVED]** |
| APD-3 | radiální Fockova stopa se rovná nerozvětvenému lokálnímu Tateovu integrálu | **[STD/PROVED]** |
| APD-4 | operátor racionálního revivalu a Gaussův součet se faktorizují přes prvočíselné mocniny | **[STD/PROVED]** |
| APD-5 | získání maximálních bloků prvočíselných mocnin je ekvivalentní faktorizaci výstupu | **[L1 elementary theorem]** |
| APD-UBT-1 | odvodit racionální/profinitní lokální sektory z kanonické akce UBT | **[OPEN]** |
| APD-UBT-2 | dynamicky odvodit (log p), charaktery jednotek a případné fermionové gradování | **[OPEN]** |
| APD-HP | sestrojit samoadjungovaný operátor nebo stopové párování, jehož spektrální strana je množinou netriviálních nul | **[OPEN]** |

Konstrukce dává zeta jako tepelnou stopu. Nuly analytického pokračování nejsou vlastními hodnotami kladného operátoru (H_{\log}). Toto omezení je patrné již v partičním rámci Bosta--Connese a připojení theta tepelné stopy je neodstraňuje.

<a id="apd-next"></a>
## 10. Další přípustný experiment

Následující experiment má přidat sektor jednotek bez vymýšlení další rodiny globálních kanálů:

1. realizovat (mathbb Q_p^\times\cong p^{\mathbb Z}\times\mathbb Z_p^\times) jako radiální valuaci krát lokální jednotky;
2. ztotožnit existující multiplikativní charaktery modulo (5) s charaktery (mathbb Z_5^\times/(1+5\mathbb Z_5));
3. spočítat odpovídající lokální Tateovy integrály a lokální Fourierovy mapy/kořenová čísla;
4. otestovat kompatibilitu konečných revivalových bloků při růstu (p^k) směrem k (mathbb Z_p);
5. skončit, pokud výsledkem bude pouze standardní Tateova faktorizace bez operátoru nebo kladného stopového párování odvozeného z UBT.

Tím se zachovají užitečné výpočty modulo (5), ale jejich libovolná globální interpretace se nahradí interpretací lokální.

<a id="apd-verification"></a>
## 11. Ověření

| Tvrzení | Artefakt/nástroj | Výsledek | Rozsah | Omezení | Status Lean |
|---|---|---|---|---|---|
| konečné důsledky APD-1 | `tools/verify_adelic_prime_decomposition.py`, Python (3.12) | úspěch | useknutí grafové normy pro deterministický vektor definičního oboru | numerická kontrola chvostu doplňuje analytický důkaz operátoru násobení | `LEAN-PENDING` — Lean není v běhovém prostředí dostupný |
| APD-2 a APD-3 | tentýž artefakt | úspěch | rekonstrukce valuací, lokální geometrické stopy, konečné tenzorové stopy | konečné/numerické kontroly nedokazují analytické pokračování | `LEAN-PENDING` |
| APD-4 | tentýž artefakt | úspěch | exaktní CRT idempotenty a bijekce reziduí; numerické fáze a Gaussovy součty pro složené moduly | konečná sada testů doplňuje analytický CRT důkaz | `LEAN-PENDING` |
| archimédovská Mellinova normalizace | tentýž artefakt | úspěch v (s=2) s relativní tolerancí (2\times10^{-8}) | nezávislá kvadratura s Jacobiho inverzí | jeden numerický bod není obecným Mellinovým důkazem | `LEAN-PENDING` |
| APD-5 | tentýž artefakt | exaktní úspěch pro (2\le q<1000) plus analytický důkaz | rekonstrukce prvočíselných základů a exponentů z maximálních prvočíselných mocnin | konečný výčet doplňuje elementární implikaci | `LEAN-PENDING` |

Žádná kontrola neodvozuje lokální místa, racionální jmenovatele ani spektrální operátor nul z UBT.

<a id="apd-references"></a>
## 12. Primární literatura

- J. Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions*, in *Algebraic Number Theory*, 1967, pp. 305--347.
- J.-B. Bost and A. Connes, [*Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*](https://doi.org/10.1007/BF01589495), 1995.
- A. Connes, [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/9811068), 1998/1999.

