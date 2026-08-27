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

# Společná Mellinova analýza Jacobiho theta sektorů

**Datum:** 2026-08-25  
**Status:** klasické Mellinovy identity, tříkanálový no-go výsledek a rozšíření hodnosti čtyři s charakteristikami modulo \(5\) jsou zavedeny; vazba odvozená z UBT zůstává otevřená.

<a id="tmm-question"></a>
## 1. Otázka

Mohou současné Mellinovy transformace všech čtyř Jacobiho theta sektorů uložit netriviálním nulám Riemannovy zeta funkce novou podmínku nad rámec funkcionální rovnice?

Pro tři nenulové theta konstanty je odpověď záporná: jejich skalární Mellinovy kanály obsahují pouze jeden stupeň volnosti zeta. Výsledek přesně ukazuje, kde musí vstoupit skutečně nová informace.

<a id="tmm-definitions"></a>
## 2. Theta jádra

Pro \(t>0\) použijme

\[
\vartheta_2(it)=\sum_{n\in\mathbb Z}e^{-\pi(n+1/2)^2t},\qquad
\vartheta_3(it)=\sum_{n\in\mathbb Z}e^{-\pi n^2t},\qquad
\vartheta_4(it)=\sum_{n\in\mathbb Z}(-1)^n e^{-\pi n^2t}.
\]

Definujme konvergentní jádra

\[
K_2(t)=\frac{\vartheta_2(it)}2,\qquad
K_3(t)=\frac{\vartheta_3(it)-1}2,\qquad
K_4(t)=\frac{1-\vartheta_4(it)}2.
\]

Čtvrtá theta konstanta splňuje

\[
\vartheta_1(0,it)=0.
\]

V bodě \(z=0\) tedy nedává skalární Mellinův kanál. Její \(z\)-derivace je nenulová a patří do rozšířeného experimentu s modulárními formami, nikoli do následující tříkanálové věty.

<a id="tmm-transforms"></a>
## 3. Mellinovy transformace

Položme

\[
A(s)=\pi^{-s/2}\Gamma\!\left(\frac s2\right).
\]

Integrace po členech ve společné polorovině

\[
\Re s>1
\]

dává

\[
\mathcal M[K_3](s)=A(s)\zeta(s),
\]

\[
\mathcal M[K_4](s)=A(s)(1-2^{1-s})\zeta(s),
\]

\[
\mathcal M[K_2](s)=A(s)(2^s-1)\zeta(s).
\]

Ekvivalentně

\[
\mathbf M(s)
=A(s)\zeta(s)
\begin{pmatrix}
2^s-1\\[2pt]
1\\[2pt]
1-2^{1-s}
\end{pmatrix}.
\]

<a id="tmm-no-go"></a>
## 4. Věta TMM-1: hodnost a množina nul

**Věta TMM-1 (standardní důsledky, dokázané zde).** Společná skalární Mellinova data \(K_2,K_3,K_4\) mají meromorfní hodnost jedna nad společným faktorem \(A(s)\zeta(s)\). V otevřeném kritickém pásu

\[
0<\Re s<1,
\]

se všechny tři analyticky pokračované kanály anulují současně právě v netriviálních nulách

\[
\zeta(s).
\]

**Důkaz.** Předchozí faktorizace dokazuje hodnost jedna. Funkce gama nemá nuly. Nuly \(2^s-1\) leží na

\[
\Re s=0,
\]

a nuly \(1-2^{1-s}\) leží na

\[
\Re s=1.
\]

Žádný násobitel se uvnitř otevřeného pásu neanuluje. Žádný ze tří kanálů proto nepřidává nezávislou vnitřní podmínku na nuly. \(\square\)

Jde o no-go výsledek pouze pro tři skalární theta konstanty. Nevylučuje novou informaci z derivací, charakteristik, součinů, vícerozměrných theta řad ani z maticového jádra odvozeného z UBT.

<a id="tmm-modular-matrix"></a>
## 5. Modulární \(S\)-matice

Při \(t\mapsto1/t\) splňují theta konstanty

\[
\begin{pmatrix}
\vartheta_2(i/t)\\
\vartheta_3(i/t)\\
\vartheta_4(i/t)
\end{pmatrix}
=\sqrt t\,
S
\begin{pmatrix}
\vartheta_2(it)\\
\vartheta_3(it)\\
\vartheta_4(it)
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
0&0&1\\
0&1&0\\
1&0&0
\end{pmatrix},
\qquad S^2=I.
\]

Vlastní kanály jsou

\[
\vartheta_3,\qquad \vartheta_2+\vartheta_4,\qquad \vartheta_2-\vartheta_4,
\]

s vlastními čísly \(+1,+1,-1\). Modulární rozklad vysvětluje reflexní symetrii, avšak hodnost jedna skalárních Mellinových dat neumožňuje umístit všechny nuly na osu symetrie.

<a id="tmm-new-information"></a>
## 6. Kde může vstoupit nová informace

| Rozšíření | Mellinův obraz | Možný nový obsah | Nutná podmínka |
|---|---|---|---|
| charakteristiky \([a,b]\) | Hurwitzova zeta a Dirichletovy \(L(s,\chi)\) | více aritmetických kanálů | dokázat vazbu vybranou UBT, nikoli vložit charaktery ručně |
| \(\partial_z\vartheta_1(0,it)\) a theta součiny | \(L\)-funkce modulárních forem | neskalární modulární sektory | zvládnout Mellinovu konvoluci a odlišit ji od přebalení zety |
| vícerozměrné theta řady | Epsteinovy/automorfní zeta funkce | geometrie mřížky | odvodit kvadratickou formu z UBT |
| maticové jádro UBT | determinant nebo operátorová transformace | podmínka pozitivity nebo samoadjungovanosti | odvodit jádro a skalární součin z kanonické akce |

Rozhodujícím cílem není další funkcionální rovnice. Je jím nezávisle odvozená pozitivita, totální pozitivita nebo samoadjungovanost dostatečně silná k vynucení reálných spektrálních parametrů.

<a id="tmm-verification"></a>
## 7. Ověření a další experiment

Artefakt `tools/verify_theta_mellin_matrix.py` kontroluje přímky nul násobitelů, přesnou involuci \(S\)-matice a její vlastní kanály a nezávislá numerická vyčíslení tří Mellinových Dirichletových řad pro reálná \(s>1\). Regresní pokrytí je v `tests/test_theta_mellin_matrix.py`.

| Tvrzení | Status |
|---|---|
| tři Mellinovy identity | **[STD/PROVED]** |
| TMM-1: hodnost jedna a žádná nová vnitřní podmínka na nuly | **[PROVED]** |
| vlastní rozklad modulární \(S\)-matice | **[STD/PROVED]** |
| výběr rozšířeného theta jádra z UBT | **[OPEN]** |
| pozitivita nebo samoadjungovanost vynucující RH | **[OPEN]** |
| formalizace v Lean | **LEAN-PENDING** |

<a id="tmm-characteristics"></a>
## 8. Rozšíření charakteristikami modulo \(5\)

Nechť \(U_5=(\mathbb Z/5\mathbb Z)^\times\). Protože \(2\) generuje \(U_5\), zapišme každou jednotku jako \(2^j\bmod5\) a definujme

\[
\chi_k(2^j)=e^{2\pi i k j/4},\qquad k=0,1,2,3.
\]

Tabulkou charakterů je čtyřbodová diskrétní Fourierova matice

\[
C_{kj}=\chi_k(2^j),
\qquad
CC^\dagger=4I,
\qquad
\operatorname{rank}C=4.
\]

Parita je

\[
\chi_k(-1)=(-1)^k.
\]

Položme \(a_k=0\) pro sudé \(k\) a \(a_k=1\) pro liché \(k\) a definujme theta jádra charakterů

\[
\Theta_k(t)=
\sum_{n\in\mathbb Z}
\chi_k(n)n^{a_k}e^{-\pi n^2t/5}.
\]

Pro \(\Re s>1\) dává integrace po členech

\[
\frac12\int_0^\infty
t^{(s+a_k)/2-1}\Theta_k(t)\,dt
=
\left(\frac5\pi\right)^{(s+a_k)/2}
\Gamma\!\left(\frac{s+a_k}{2}\right)L(s,\chi_k).
\]

Rozšíření charakteristikami má tedy čtyři nezávislé koeficientové kanály. Hlavní kanál splňuje

\[
L(s,\chi_0)=(1-5^{-s})\zeta(s),
\]

zatímco \(\chi_1,\chi_2,\chi_3\) poskytují tři nehlavní Dirichletovy \(L\)-funkce.

**Výsledek TMM-2.** Racionální charakteristiky zvyšují konečnou hodnost kanálů charakterů z jedné na čtyři. Jde o skutečně bohatší aritmetickou informaci, avšak nulám \(\zeta\) stále neukládá novou podmínku, dokud UBT neodvodí vazbu, determinant, formu pozitivity nebo společný spektrální operátor propojující čtyři dokončené \(L\)-kanály.

Následující experiment proto musí odvodit, nikoli zvolit, matici \(G_{\mathrm{UBT}}(s)\) působící na tyto kanály a otestovat, zda

\[
\mathbf\Lambda(s)^\dagger G_{\mathrm{UBT}}(s)\mathbf\Lambda(s)
\]

má kanonickou pozitivní nebo samoadjungovanou spektrální reprezentaci.

<a id="tmm-ubt-metric"></a>
## 9. Vazebné metriky přípustné symetriemi

Zapišme čtyři dokončené kanály charakterů jako

\[
\mathbf\Lambda=(\Lambda_0,\Lambda_1,\Lambda_2,\Lambda_3)^T.
\]

Násobení generátorem \(U_5\) působí v bázi charakterů prostřednictvím

\[
D=\operatorname{diag}(1,i,-1,-i).
\]

Komplexní konjugace zaměňuje \(\chi_1\leftrightarrow\chi_3\) a ponechává \(\chi_0,\chi_2\) pevné. Položme

\[
P=
\begin{pmatrix}
1&0&0&0\\
0&0&0&1\\
0&0&1&0\\
0&1&0&0
\end{pmatrix}.
\]

Pro hermitovskou vazebnou matici \(G\) požadujme invarianci vůči fázi charakterů a kompatibilitu s antiunitární konjugací,

\[
D^\dagger G D=G,
\qquad
P^\dagger G P=\overline G.
\]

**Věta TMM-3.** Tyto podmínky jsou ekvivalentní tvaru

\[
G=\operatorname{diag}(g_0,g_1,g_2,g_1),
\qquad g_0,g_1,g_2\in\mathbb R.
\]

Forma je pozitivně definitní právě tehdy, když

\[
g_0>0,\qquad g_1>0,\qquad g_2>0.
\]

Fázová a konjugační symetrie tedy ponechávají tři nezávislé reálné váhy a nevybírají kanonickou metriku.

Pokud navíc postulujeme cyklickou symetrii kanálů

\[
X(\Lambda_0,\Lambda_1,\Lambda_2,\Lambda_3)^T
=(\Lambda_3,\Lambda_0,\Lambda_1,\Lambda_2)^T,
\qquad X^\dagger G X=G,
\]

potom

\[
G=cI.
\]

Tento silnější závěr je podmíněný, protože repozitář neodvozuje působení \(X\) na Mellinovy kanály charakterů z kanonického pole UBT.

I maximálně symetrický pozitivní kandidát dává pouze

\[
Q(s)=c\sum_{k=0}^3|\Lambda_k(s)|^2.
\]

Jeho pozitivita říká, že \(Q(s)=0\) pouze při anulování všech čtyř kanálů. RH se týká nul samotného hlavního kanálu, takže pozitivita \(Q\) jejich polohu neurčuje bez další identity vynucující současné anulování nebo bez samoadjungovaného operátoru, jehož charakteristickým determinantem je hlavní dokončený kanál zeta.

Toto omezení odpovídá auditu akce v repozitáři: reálné bikvaternionové párování, znaménko a škála nejsou dokončeny; pozitivní hermitovská veličina \(\operatorname{Tr}(X^\dagger X)\) není pro obecné pole Lorentzovsky invariantní při neunitárních boostech; a kanonická seskvilineární forma potřebná pro antiunitární obrácení času zůstává otevřená. TMM-3 je proto klasifikací přípustných kandidátů, nikoli odvozením z UBT.

| Podmínka | Status |
|---|---|
| klasifikace z fáze a konjugace | **[PROVED]** |
| skalární metrika při dodatečné cyklické symetrii | **[PROVED, CONDITIONAL ON \(X\)]** |
| odvodit symetrie kanálů z kanonické UBT | **[OPEN]** |
| sladit pozitivní metriku kanálů s Lorentzovsky invariantním párováním pole | **[OPEN]** |
| získat samoadjungovaný determinant síly RH | **[OPEN]** |

Ukotvení v repozitáři: `canonical/ACTION.en.md:50-98`, `canonical/symmetry/discrete_symmetries.tex:311-317` a `canonical/symmetry/discrete_symmetries.tex:449-454`.

<a id="tmm-functional-equations"></a>
## 10. Gaussovy součty a no-go výsledek funkcionálních rovnic

Pro tři nehlavní charaktery \(\chi_k\), \(k=1,2,3\), položme \(a_k=k\bmod2\) a

\[
\tau_k=\sum_{r=1}^{4}\chi_k(r)e^{2\pi i r/5},
\qquad
\varepsilon_k=\frac{\tau_k}{i^{a_k}\sqrt5}.
\]

Všechny tři charaktery jsou primitivní. Jejich dokončené funkce

\[
\Lambda_k(s)=
\left(\frac5\pi\right)^{(s+a_k)/2}
\Gamma\!\left(\frac{s+a_k}{2}\right)L(s,\chi_k)
\]

splňují

\[
\Lambda_k(s)=\varepsilon_k\Lambda_{4-k}(1-s).
\]

Přímý výpočet Gaussových součtů dává

\[
|\tau_k|=\sqrt5,
\qquad
\varepsilon_2=1,
\qquad
\varepsilon_3=\overline{\varepsilon_1},
\qquad
\varepsilon_1\varepsilon_3=1.
\]

Na \(\mathbf\Lambda_{\mathrm{prim}}=(\Lambda_1,\Lambda_2,\Lambda_3)^T\) má tedy funkcionální rovnice tvar

\[
\mathbf\Lambda_{\mathrm{prim}}(s)
=R\mathbf\Lambda_{\mathrm{prim}}(1-s),
\qquad
R=
\begin{pmatrix}
0&0&\varepsilon_1\\
0&1&0\\
\varepsilon_3&0&0
\end{pmatrix},
\qquad
R^\dagger R=R^2=I.
\]

Omezení metriky TMM-3 na tyto kanály je

\[
G_{\mathrm{prim}}=\operatorname{diag}(g_1,g_2,g_1).
\]

Pro všechna reálná \(g_1,g_2\), nikoli pouze pro stejná, platí

\[
R^\dagger G_{\mathrm{prim}}R=G_{\mathrm{prim}}.
\]

Funkcionální rovnice proto nepřidává žádný vztah mezi vahou lichých charakterů \(g_1\) a vahou kvadratického charakteru \(g_2\).

Hlavní charakter je odlišný. Je indukován z triviálního charakteru konduktoru jedna a

\[
L(s,\chi_0)=(1-5^{-s})\zeta(s).
\]

Je-li \(\Lambda_\zeta(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\), jeho normalizace s konduktorem pět je

\[
\Lambda_0^{(5)}(s)
=\left(5^{s/2}-5^{-s/2}\right)\Lambda_\zeta(s).
\]

Protože \(\Lambda_\zeta(s)=\Lambda_\zeta(1-s)\), dostáváme nekonstantní násobitel

\[
\Lambda_0^{(5)}(s)
=\frac{5^{s/2}-5^{-s/2}}
{5^{(1-s)/2}-5^{-(1-s)/2}}
\Lambda_0^{(5)}(1-s).
\]

Čtyři kanály tudíž netvoří konstantní unitární \(4\times4\) reprezentaci funkcionální rovnice: tři primitivní kanály tvoří uzavřený blok, zatímco hlavní kanál zeta zůstává oddělený.

**Věta TMM-4.** Přesné Gaussovy součty modulo 5 a Dirichletovy funkcionální rovnice neredukují tříparametrickou rodinu metrik z TMM-3 a nesměšují hlavní kanál zeta s primitivními kanály. Neukládají proto žádnou další podmínku netriviálním nulám \(\zeta\).

Jde o druhý no-go výsledek, nikoli o selhání výpočtu. Jakákoli silnější vazba musí pocházet z rozšířené aditivní reprezentace theta tříd, operátoru odvozeného z UBT nebo jiné identity, která není obsažena v oddělených Dirichletových funkcionálních rovnicích.

| Podmínka | Status |
|---|---|
| primitivní Gaussovy součty a kořenová čísla | **[PROVED]** |
| unitární involuce na primitivním bloku | **[PROVED]** |
| hlavní kanál má konstantní kořenové číslo při konduktoru pět | **[DISPROVED]** |
| funkcionální rovnice vynucují \(g_1=g_2\) | **[DISPROVED]** |
| vazba s hlavním kanálem odvozená z UBT | **[OPEN]** |

<a id="tmm-additive-residues"></a>
## 11. Aditivní reziduální kanály a konečná Weilova reprezentace

Pro \(r\in\mathbb Z/5\mathbb Z\) definujme

\[
\Theta_r(t)=
\sum_{n\equiv r\ (\mathrm{mod}\ 5)}
e^{-\pi n^2t/5},
\qquad t>0.
\]

Poissonova sumace dává vektorovou transformaci

\[
\mathbf\Theta(t)=t^{-1/2}\mathcal S\mathbf\Theta(1/t),
\qquad
\mathcal S_{rs}=\frac1{\sqrt5}e^{2\pi i rs/5}.
\]

Pro holomorfní verzi působí posun o dvě modulární jednotky vztahem

\[
\Theta_r(\tau+2)=e^{2\pi i r^2/5}\Theta_r(\tau),
\qquad
\mathcal T=\operatorname{diag}
\left(e^{2\pi i r^2/5}\right)_{r=0}^{4}.
\]

Nechť \(\mathcal P\) obrací rezidua, \((\mathcal Pv)_r=v_{-r}\). Přímý výpočet dává

\[
\mathcal S^\dagger\mathcal S=I,
\qquad
\mathcal S^2=\mathcal P,
\qquad
\mathcal S^4=I,
\qquad
[\mathcal T,\mathcal P]=0.
\]

Úplný prostor koeficientů se rozkládá na sektory parity reziduí

\[
\mathbb C^5=V_+\oplus V_-,
\qquad
\dim V_+=3,
\qquad
\dim V_-=2,
\qquad
\Pi_\pm=\frac12(I\pm\mathcal P).
\]

Vyřešení úplných rovnic komutantu

\[
[G,\mathcal S]=[G,\mathcal T]=0
\]

dává

\[
G=a\Pi_+ + b\Pi_-.
\]

Pro hermitovské \(G\) jsou koeficienty \(a,b\) reálné a pozitivita vyžaduje \(a,b>0\). Úplná pětirozměrná reprezentace má tedy dvě nezávislé invariantní váhy.

Skalární theta konstanty však splňují

\[
\Theta_r(t)=\Theta_{-r}(t).
\]

Obsazují proto pouze

\[
V_+=\operatorname{span}
\left\{e_0,\frac{e_1+e_4}{\sqrt2},
\frac{e_2+e_3}{\sqrt2}\right\}.
\]

Omezený komutant \(\mathcal S\) a \(\mathcal T\) na tomto třírozměrném sektoru má dimenzi jedna. Jeho invariantní hermitovská metrika je tudíž

\[
G_+=aI_3.
\]

Dva liché kanály při \(z=0\) chybějí; lze je dodat derivacemi podle eliptické proměnné, analogicky k chybějícímu skalárnímu kanálu \(\vartheta_1\).

Hlavní funkce zeta je nyní skutečně obsažena v aditivním systému, protože

\[
\frac12\sum_{r=0}^{4}
\left(\Theta_r(t)-\delta_{r0}\right)
=\sum_{n=1}^{\infty}e^{-\pi n^2t/5},
\]

a tedy pro \(\Re s>1\)

\[
\frac12\int_0^\infty t^{s/2-1}
\sum_{r=0}^{4}\left(\Theta_r(t)-\delta_{r0}\right)dt
=\left(\frac5\pi\right)^{s/2}
\Gamma\!\left(\frac s2\right)\zeta(s).
\]

**Věta TMM-5.** Aditivní reziduální reprezentace skutečně směšuje nulovou reziduální třídu se čtyřmi nenulovými třídami. Modulární invariance určuje metriku skalárního sudého sektoru jednoznačně až na celkovou škálu. Kanál zeta je však lineárním funkcionálem tří theta složek, zatímco pozitivita \(aI_3\) kontroluje jejich současné anulování. Nevyplývá z ní proto, že nuly tohoto lineárního funkcionálu leží na \(\Re s=1/2\).

Tento experiment poskytuje kanonické modulární směšování a skalární metriku na realizovaném sektoru, nikoli však spektrální operátor síly RH. Zbývající chybějící složkou je samoadjungovaný operátor odvozený z UBT, jehož determinant nebo význačný vlastní kanál se rovná dokončené funkci zeta.

| Podmínka | Status |
|---|---|
| Fourierova transformace pěti reziduí | **[PROVED]** |
| úplný komutant \(a\Pi_++b\Pi_-\) | **[PROVED]** |
| skalární metrika na realizovaném sudém sektoru | **[PROVED]** |
| aditivní systém obsahuje Mellinův kanál zeta | **[PROVED]** |
| pozitivita určuje polohu nul tohoto lineárního kanálu | **[DISPROVED]** |
| samoadjungovaný operátor zeta odvozený z UBT | **[OPEN]** |

<a id="tmm-elliptic-derivatives"></a>
## 12. Eliptické derivace a lichý sektor

Zaveďme eliptická reziduální jádra

\[
\Theta_r(z,\tau)=
\sum_{n\equiv r\ (\mathrm{mod}\ 5)}
\exp\!\left(\frac{\pi i\tau n^2}{5}
+\frac{2\pi i n z}{5}\right)
\]

a jejich první derivace v \(z=0\), normalizované jako

\[
\Phi_r(t)=
\frac5{2\pi i}
\left.\frac{\partial}{\partial z}\Theta_r(z,it)\right|_{z=0}
=\sum_{n\equiv r\ (\mathrm{mod}\ 5)}
n e^{-\pi n^2t/5}.
\]

Mají lichou paritu reziduí,

\[
\Phi_0(t)=0,
\qquad
\Phi_{-r}(t)=-\Phi_r(t),
\qquad
\sum_{r=0}^{4}\Phi_r(t)=0.
\]

Vektor derivací tedy leží v

\[
V_-=\operatorname{span}
\left\{\frac{e_1-e_4}{\sqrt2},
\frac{e_2-e_3}{\sqrt2}\right\}.
\]

Derivování Poissonovy transformace nebo přímá transformace váženého Gaussova jádra dává

\[
\mathbf\Phi(t)
=-i\,t^{-3/2}\mathcal S\mathbf\Phi(1/t).
\]

Mocnina se mění z \(t^{-1/2}\) na \(t^{-3/2}\): sektor derivací má modulární váhu vyšší o jedna. Posun o dvě stále působí prostřednictvím \(\mathcal T\).

Omezený komutant na \(V_-\) má dimenzi jedna, takže jeho invariantní hermitovská metrika je

\[
G_-=bI_2.
\]

Úplná metrika skalárních a derivovaných kanálů je proto

\[
G=aI_3\oplus bI_2
=a\Pi_+ + b\Pi_-.
\]

Mohlo by se zdát, že derivace vynutí \(a=b\). Nevynutí. Vyřešení všech rovnic pro konstantní intertwiner

\[
Q\mathcal S_+=(-i\mathcal S_-)Q,
\qquad
Q\mathcal T_+=\mathcal T_-Q,
\qquad
Q:V_+\longrightarrow V_-
\]

dává pouze

\[
Q=0.
\]

To odpovídá rozdílným dimenzím a modulárním vahám obou ireducibilních sektorů. Derivace propojuje podkladové funkce, není však konstantním endomorfismem konečné reprezentace koeficientů.

**Věta TMM-6.** První eliptické derivace realizují dva chybějící liché reziduální kanály a dávají jim skalární invariantní metriku. Sdružená Jacobiho data zachovávají dvě nezávislé pozitivní škály \(a,b\); modulární kovariance neposkytuje nenulový konstantní intertwiner ze sudého do lichého sektoru, a proto nevynucuje \(a=b\).

Sudé/liché rozdělení lze použít jako pečlivě omezenou bosonickou/fermionickou analogii: skalární theta hodnoty jsou sudé a derivované kanály liché, přičemž v druhých nastává párové rušení. Nejde o odvození fyzikálních částic, spinové statistiky ani stavů částice-antičástice. Taková interpretace by vyžadovala gradovaný Hilbertův prostor odvozený z UBT a operátor Diracova typu nebo supernáboj měnící váhu.

| Podmínka | Status |
|---|---|
| lichá derivovaná jádra a jejich Poissonův zákon | **[PROVED]** |
| skalární invariantní metrika \(bI_2\) | **[PROVED]** |
| nenulový konstantní modulární intertwiner \(V_+\to V_-\) | **[DISPROVED]** |
| modulární kovariance vynucuje \(a=b\) | **[DISPROVED]** |
| Diracova nebo supernábojová vazba odvozená z UBT | **[OPEN]** |
| interpretace fyzikálních fermionů | **[OPEN]** |

<a id="tmm-jacobi-dirac"></a>
## 13. Jacobiho Diracova faktorizace a její spektrální mez

Pracujme v Hilbertově prostoru \(5\)-periodických funkcí eliptické proměnné,

\[
\mathcal H_z=L^2(\mathbb R/5\mathbb Z),
\qquad
\langle f,g\rangle_z=\frac15\int_0^5\overline{f\(z\)}g\(z\)\,dz,
\]

s hustým definičním oborem \(H^1(\mathbb R/5\mathbb Z)\). Normalizovaná eliptická derivace

\[
\mathscr D_z:=\frac5{2\pi i}\frac{\partial}{\partial z}
\]

je na periodickém oboru samoadjungovaná a splňuje

\[
\mathscr D_z e^{2\pi i n z/5}=n e^{2\pi i n z/5}.
\]

Nechť \((\mathcal Pf)(z)=f(-z)\). Potom

\[
\mathcal P\mathscr D_z\mathcal P=-\mathscr D_z.
\]

Operátor \(\mathscr D_z\) je tedy lichý vzhledem k paritnímu gradování a zaměňuje sudý a lichý funkční prostor. Aplikace na reziduální theta jádra dává přesně kanály z TMM-6,

\[
\left.\mathscr D_z\Theta_r(z,it)\right|_{z=0}=\Phi_r(t).
\]

Současně faktorizuje volný theta tepelný generátor. Jestliže

\[
H_0 e^{2\pi i n z/5}=\frac{\pi n^2}{5}e^{2\pi i n z/5},
\]

pak

\[
\boxed{H_0=\frac\pi5\mathscr D_z^2},
\qquad
e^{-tH_0}e^{2\pi i n z/5}=e^{-\pi n^2t/5}e^{2\pi i n z/5}.
\]

V rozkladu \(\mathcal H_z=\mathcal H_+\oplus\mathcal H_-\) má operátor Diracův tvar

\[
\mathscr D_z=
\begin{pmatrix}
0&\mathscr D_-\\
\mathscr D_+&0
\end{pmatrix},
\qquad
\mathscr D_- = \mathscr D_+^\dagger.
\]

Jde o skutečný diferenciální operátor měnící váhu, nikoli o konstantní intertwiner vyloučený v TMM-6. Neztotožňuje však dvě škály metrik konečných sektorů. Pro gradovanou metriku \(aI_3\oplus bI_2\) je adjungovaný operátor k mapě \(D:V_+\to V_-\) roven \(D^{\dagger_{a,b}}=(b/a)D^\dagger\); samoadjungované blokové doplnění proto existuje pro všechna \(a,b>0\). Požadavek stejného nepřeškálovaného diferenciálního výrazu v obou mimodiagonálních blocích by uložil \(a=b\), ale jde o dodatečnou volbu normalizace, nikoli o důsledek modulární kovariance.

**Věta TMM-7.** Jacobiho derivace dává kanonickou paritně lichou samoadjungovanou odmocninu volného theta Hamiltoniánu na periodickém eliptickém Hilbertově prostoru. Její spektrum je

\[
\operatorname{spec}(\mathscr D_z)=\mathbb Z,
\qquad
\operatorname{spec}(H_0)=\left\{\frac{\pi n^2}{5}:n\in\mathbb Z\right\}.
\]

Tento operátor proto nemá za vlastní hodnoty ordináty netriviálních nul zeta a jeho spektrální determinant není dokončená zeta funkce. Repozitář navíc neodvozuje identifikaci pomocné Jacobiho souřadnice \(z\) s kanonickým bikvaternionovým prostoročasovým směrem nebo směrem komplexního času. Operátor \(\mathscr D_z\) tedy uzavírá lokální problém gradované faktorizace, nikoli most UBT nebo Hilbertův--Pólyův program.

| Podmínka | Status |
|---|---|
| samoadjungovaná eliptická derivace na periodickém oboru | **[PROVED]** |
| paritně lichá mapa a \(H_0=(\pi/5)\mathscr D_z^2\) | **[PROVED]** |
| stejná normalizace bloků plyne z modulární symetrie | **[DISPROVED]** |
| spektrum se rovná ordinátám netriviálních nul zeta | **[DISPROVED]** |
| \(z\) je ztotožněno s kanonickým směrem UBT | **[OPEN]** |
| Hilbertův--Pólyův operátor je odvozen z UBT | **[OPEN]** |

Ověření: `tools/verify_theta_mellin_matrix.py` kontroluje Fourierovy vlastní hodnoty, antikomutaci s paritou, faktorizaci tepelného generátoru a škálování adjungovaného operátoru podle metriky na konečných invariantních ořezech módů; `tests/test_theta_mellin_matrix.py` poskytuje regresní vstup. Tyto konečné exaktní/numerické kontroly nedokazují větu o definičním oboru neomezeného operátoru ani identifikaci s UBT. **LEAN-PENDING:** věta používá fakta o Fourierových/Sobolevových definičních oborech operátorů, která zatím nejsou reprezentována v Lean prostředí repozitáře.

<a id="tmm-local-polynomial-no-go"></a>
## 14. No-go pro lokální operátory konečného řádu

Nechť \(P(x)=\sum_{k=0}^{m}c_kx^k\) je reálný polynom a aplikujme \(P(\mathscr D_z)\) na skalární theta jádro. Pro \(\Re s>2j+1\) dává členová Mellinova integrace

\[
\frac12\int_0^\infty t^{s/2-1}
\left.
P(\mathscr D_z)
\sum_{n\ne0}e^{-\pi n^2t/5}e^{2\pi inz/5}
\right|_{z=0}dt
=
\left(\frac5\pi\right)^{s/2}\Gamma\!\left(\frac s2\right)
\sum_{j=0}^{\lfloor m/2\rfloor}c_{2j}\zeta(s-2j).
\]

Všechny liché mocniny se zruší, protože módy \(n\) a \(-n\) mají stejné koeficienty. Každý lokální diferenciální polynom konečného řádu tedy v hlavním skalárním kanálu vytváří pouze konečnou lineární kombinaci posunutých zeta funkcí. Projekce na rezidua nebo charakteristiky je nahrazují odpovídajícími konečnými kombinacemi Hurwitzových nebo Dirichletových \(L\)-funkcí; nevytvářejí nový spektrální determinant.

Existuje i nezávislá asymptotická překážka. Jestliže \(m\ge1\) a \(c_m\ne0\), vlastní hodnoty jsou \(P(n)\), \(n\in\mathbb Z\), a jejich absolutní počítací funkce splňuje

\[
N_P(T):=\#\{n\in\mathbb Z:|P(n)|\le T\}
=2|c_m|^{-1/m}T^{1/m}+O(1).
\]

Pevná konečná vnitřní násobnost mění pouze vedoucí konstantu. Naproti tomu Riemannův--von Mangoldtův vzorec pro kladné ordináty netriviálních nul zeta je

\[
N_\zeta(T)=
\frac{T}{2\pi}\log\!\frac{T}{2\pi}
-\frac{T}{2\pi}+O(\log T).
\]

Žádný exponent \(1/m\) nedává růst \(T\log T\). Konstantní polynom má nekonečnou degeneraci a nemá kompaktní rezolventu, takže překážku neobchází.

**Věta TMM-8.** Žádný samoadjungovaný diferenciální polynom konečného řádu v periodickém Jacobiho operátoru \(\mathscr D_z\), ani s pevnou konečnou maticovou násobností, nemůže mít za své úplné spektrum ordináty netriviálních nul zeta. Jeho skalární Mellinův kanál je konečnou kombinací posunutých zeta funkcí a jeho zákon počtu vlastních hodnot je neslučitelný s Riemannovým--von Mangoldtovým zákonem.

Věta nevylučuje nelokální pseudodiferenciální operátor, nekompaktní fázový prostor, energeticky závislou okrajovou podmínku ani aritmetickou prime/Eulerovu interakci. Říká, že alespoň jedna taková složka je nutná; přidávání dalších konečných mocnin \(\partial_z\) Hilbertův--Pólyův most neuzavře.

| Podmínka | Status |
|---|---|
| Mellinův obraz každého polynomu \(P(\mathscr D_z)\) | **[PROVED]** |
| rušení lichých mocnin ve skalárním kanálu | **[PROVED]** |
| polynomiální spektrální počet oproti \(T\log T\) | **[PROVED]** |
| lokální Jacobiho operátor konečného řádu realizuje všechny ordináty zeta | **[DISPROVED]** |
| nelokální aritmetický operátor je odvozen z UBT | **[OPEN]** |

Ověření: repozitářový verifier nezávisle porovnává oříznuté Dirichletovy řady pro monomy \(1,n^2,n^4\) s \(\zeta(s),\zeta(s-2),\zeta(s-4)\), kontroluje rušení lichých monomů a polynomiální exponenty počítací funkce na rostoucích ořezech. Analytická věta používá členovou integraci v uvedené polorovině absolutní konvergence a standardní Riemannův--von Mangoldtův vzorec. **LEAN-PENDING:** asymptotické počítání a záměna Mellinovy integrace dosud nebyly formalizovány v Lean.

<a id="tmm-infinite-series-nonlocal"></a>
## 15. Nekonečná Maclaurinova řada a první nelokální baseline

Uvažujme konvergentní nekonečný funkcionální kalkul

\[
F(\mathscr D_z)=\sum_{k=0}^{\infty}a_k\mathscr D_z^k,
\qquad
F(\mathscr D_z)e_n=F(n)e_n,
\qquad
e_n\(z\)=e^{2\pi inz/5}.
\]

Tím lze obejít větu o konečném řádu, ale operátor obecně nezůstane lokální. Translačně invariantní operátor na kružnici je konvoluce s periodickou distribucí \(K_F\), jejíž Fourierovy koeficienty jsou \(F(n)\). Je-li operátor lokální, má konvoluční jádro podporu v neutrálním prvku. Distribuce podporovaná v jediném bodě je konečnou sumou derivací delta distribuce, takže její Fourierovy koeficienty jsou polynomy v \(n\). Proto

\[
\operatorname{supp}K_F\subseteq\{0\}
\quad\Longleftrightarrow\quad
\exists P\in\mathbb C[x]\ \forall n\in\mathbb Z:\ F(n)=P(n).
\]

Skutečně nepolynomiální nekonečná Maclaurinova řada je tedy už nelokální operátor nekonečného řádu nebo pseudodiferenciální operátor. Kvalifikace pomocí celočíselné posloupnosti je podstatná: dvě celé funkce shodné na všech celých číslech definují tentýž Fourierův multiplikátor.

Pouhá existence nemá predikční sílu. Celá interpolace na diskrétní množině \(\mathbb Z\) může vytvořit \(F\) s předepsanými hodnotami \(F(n)=\gamma_n\), kde \(\gamma_n\) jsou ordináty zeta. Je nekonečně nejednoznačná, protože pro každou celou funkci \(G\)

\[
\widetilde F(z)=F(z)+\sin(\pi z)G(z)
\quad\Longrightarrow\quad
\widetilde F(n)=F(n).
\]

Takový operátor pouze ukládá požadované nuly do své definice a není odvozením Hilbertova--Pólyova programu.

Neladěný baseline však může reprodukovat potřebnou hladkou hustotu. Nechť \(W\) je kladná hlavní Lambertova funkce a definujme lichý reálný symbol

\[
A_0(0)=0,
\qquad
A_0(n)=\operatorname{sgn}(n)
\frac{2\pi|n|}{W(|n|/e)},
\qquad n\ne0.
\]

Odpovídající diagonální Fourierův multiplikátor je samoadjungovaný na svém maximálním spektrálním oboru. Definujme hladkou dvoučlennou aproximaci počítací funkce

\[
N_0(T)=\frac{T}{2\pi}
\left(\log\frac{T}{2\pi}-1\right).
\]

Pro \(w=W(n/e)\) dává identita \(we^w=n/e\) přesně

\[
\frac{A_0(n)}{2\pi}=\frac n w,
\qquad
\log\frac{A_0(n)}{2\pi}=w+1,
\qquad
\boxed{N_0(A_0(n))=n}
\]

pro každé kladné celé \(n\). Operátor \(A_0\) tedy přesně invertuje hladký vedoucí Riemannův--von Mangoldtův zákon. Poskytuje chybějící hustotu \(T\log T\), kterou nemohl dát žádný konečný diferenciální polynom.

**Věta TMM-9.** Nekonečný Maclaurinův funkcionální kalkul může obejít TMM-8 pouze tím, že se stane nelokálním, pokud se jeho celočíselný symbol neredukuje na polynomiální posloupnost. Libovolná celá interpolace ordinát zeta je možná, ale kruhová a nejednoznačná. Explicitní nelokální multiplikátor \(A_0\) je samoadjungovaný a bez použití jednotlivých nul odpovídá hladkému dvoučlennému zákonu počtu nul zeta, nereprodukuje však oscilační člen, korekci \(7/8\) ani jednotlivé ordináty.

Zbývající aritmetický problém je tím ostře izolován: odvodit z UBT nebo theta/Eulerových dat samoadjungovanou korekci \(V_{\mathrm{arith}}\) takovou, že

\[
A=A_0+V_{\mathrm{arith}}
\]

reprodukuje prvočísly řízenou fluktuaci a přitom zachová odůvodněný definiční obor a samoadjungovanost. Primitivním vstupem musejí být odvozená data \(\log p\), nikoli tabulka nul zeta.

| Podmínka | Status |
|---|---|
| kritérium lokality translačně invariantního \(F(\mathscr D_z)\) | **[PROVED]** |
| libovolná celá interpolace existuje a je nejednoznačná | **[CLASSICAL / PROVED]** |
| interpolace představuje odvození RH | **[DISPROVED]** |
| Lambertův-\(W\) baseline přesně invertuje \(N_0\) | **[PROVED]** |
| baseline reprodukuje jednotlivé ordináty zeta | **[DISPROVED]** |
| prime/\(\log p\) korekce je odvozena z UBT | **[OPEN]** |

Ověření: `tools/verify_theta_mellin_matrix.py` kontroluje Lambertovu rovnici, přesnou identitu \(N_0(A_0(n))=n\) v několika škálách, monotonii a lichost symbolu a nejednoznačnost celočíselného spektra po přičtení \(\sin(\pi z)G(z)\). Tvrzení o lokalitě používá klasickou strukturní větu pro distribuce podporované v bodě. **LEAN-PENDING:** podpora distribucí a neomezený spektrální funkcionální kalkul nejsou formalizovány v Lean prostředí repozitáře.

<a id="tmm-regulated-prime-operator"></a>
## 16. Regulovaný operátor prvočíselné fáze

Nechť \(A_0\) je samoadjungovaný Lambertův-\(W\) baseline z TMM-9 a položme \(\sigma=\tfrac12+\varepsilon>1\). Funkcionální kalkul dává

\[
U_{p,k}=e^{ik(\log p)A_0},
\qquad U_{p,k}^\dagger=U_{p,k}^{-1}.
\]

Definujme

\[
\mathcal D_\sigma=-\frac1\pi\sum_{p,k\ge1}
\frac{\log p}{p^{k\sigma}}\cos\!\bigl(k(\log p)A_0\bigr),
\]

\[
\mathcal S_\sigma=-\frac1\pi\sum_{p,k\ge1}
\frac{1}{k p^{k\sigma}}\sin\!\bigl(k(\log p)A_0\bigr).
\]

Pro \(\sigma>1\) konvergují obě sumy koeficientů absolutně, a tedy v operátorové normě, k omezeným samoadjungovaným operátorům. Na spektrální hodnotě \(T\)

\[
d_\sigma(T)=\frac1\pi\operatorname{Re}\frac{\zeta'}{\zeta}(\sigma+iT),
\qquad
s_\sigma'(T)=d_\sigma(T).
\]

Hustotu \(d_\sigma\) nelze přičíst přímo k ordinátě. Kvantizační rovnice a její korekce v prvním řádu jsou

\[
N_0(T)+s_\sigma(T)=n,
\qquad
\delta_\sigma(T)=-\frac{s_\sigma(T)}{N_0'(T)},
\qquad
N_0'(T)=\frac1{2\pi}\log\frac{T}{2\pi}.
\]

Na kladném spektrálním sektoru

\[
A_\sigma^{(1)}
=A_0-\bigl[N_0'(A_0)\bigr]^{-1}\mathcal S_\sigma.
\]

Všechny faktory jsou reálnými borelovskými funkcemi téhož samoadjungovaného \(A_0\), takže komutují. Korekce je pro pevné \(\sigma>1\) omezená, \(A_\sigma^{(1)}\) je samoadjungovaný na \(\operatorname{Dom}(A_0)\) a

\[
N_0'(T_n^{(0)})\delta_\sigma(T_n^{(0)})
+s_\sigma(T_n^{(0)})=0.
\]

**Věta TMM-10.** Pro každé \(\sigma>1\) definují Eulerova data prvočíselných mocnin explicitní normově konvergentní omezené samoadjungované funkce hustoty a počítací fáze operátoru \(A_0\). Počítací fáze dává regulovanou korekci ordinát v prvním řádu pouze z prvočísel, bez tabulky nul zeta.

Pro \(\sigma=\tfrac12\) se ztrácí absolutní normová konvergence. Hustota diverguje na nulovém módu, zatímco ztráta absolutní konvergence integrované sinusové fáze sama nevylučuje podmíněný nebo renormalizovaný limit. Exaktní nelineární kvantizační rovnice, archimédovská korekce \(7/8\) a gama korekce i odvození primitivních fází \(\log p\) z UBT zůstávají otevřené. TMM-10 není Hilbertův--Pólyův operátor a neimplikuje RH.

| Podmínka | Status |
|---|---|
| normová konvergence pro \(\sigma>1\) | **[PROVED]** |
| omezená samoadjungovaná prvočíselná hustota a fáze | **[PROVED]** |
| \(s_\sigma'(T)=d_\sigma(T)\) | **[PROVED]** |
| korekce ordinát v prvním řádu | **[PROVED, REGULATED]** |
| normový limit hustoty při \(\sigma=1/2\) na celém prostoru | **[DISPROVED]** |
| podmíněná/renormalizovaná kritická fáze | **[OPEN]** |
| primitivní fáze \(\log p\) jsou odvozeny z UBT | **[OPEN]** |
| RH plyne z této konstrukce | **[DISPROVED]** |

Ověření: verifier nezávisle generuje prvočísla, kontroluje derivaci fáze proti hustotě, paritní symetrie a rušení v prvním řádu. Kontroluje konečné ořezy, nikoli analytický kritický limit. **LEAN-PENDING:** spektrální funkcionální kalkul a konvergence prvočíselných řad nejsou formalizovány v Lean.
