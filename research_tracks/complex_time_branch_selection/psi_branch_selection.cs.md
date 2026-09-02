<!-- BILINGUAL-UNIT: psi-branch.provenance -->
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

# Výběr větve prvního řádu pomocí komplexně-časového pokračování a vláknových dat

**Typ stopy:** VÝZKUMNÁ STOPA — MATEMATICKÉ LEMMA O SELEKCI PLUS KONJEKTURÁLNÍ UBT INTERPRETACE
**Datum:** 2026-09-02  
**Status:** holomorfie samotná je `CLOSED AS NO-GO [L0]`; lemma o výběru větve pomocí omezenosti je `PROPOSITION / PROOF SKETCH`; UBT identifikace `s ?= \psi` je `OPEN / CONJECTURAL`; operátor Diracova typu je `RESEARCH ANSATZ`; multivesmírné čtení je `SPECULATIVE`; vztah k RH je `CONDITIONAL RESEARCH DIRECTION — NOT A PROOF OF RH OR AN ADVANCE TOWARD RH`.

**Anglická edice:** `psi_branch_selection.en.md`  
**Bilingvní politika:** `../../BILINGUAL_CONTENT_POLICY.cs.md`  
**Verifikační skripty:** `../../tools/verify_psi_branch_selection.py`, `../../tools/verify_holomorphy_factor_no_go.py`

---

<!-- BILINGUAL-UNIT: psi-branch.scope -->
> **Rozsah tohoto dokumentu.** Tato výzkumná stopa opravuje stávající záplatu
> bez změny jakéhokoli kanonického axiomu, definice, master rovnice, tvrzení
> nebo statusu mezery. Výslovně respektuje
> `../action_selection/holomorphy_factor_selection_no_go.en.md`,
> `../action_selection/holomorphy_factor_selection_no_go.cs.md`,
> `../canonical_relation_generalized_dirac/action_origin_obstruction.tex` a
> existující kanonický pátý / komplexně-časový Cliffordův kanál v
> `../../canonical/geometry/biquaternion_dirac_lift.tex`.

---

<!-- BILINGUAL-UNIT: psi-branch.sec1 -->
## 1. Motivace a přesná taxonomie větví

Následující pojmy „větve“ se nesmějí zaměňovat.

<!-- BILINGUAL-UNIT: psi-branch.taxonomy -->
| ID | Pojem | Doména definice |
|---|---|---|
| B1 | Frekvenční větve faktorizované ODE/PDE druhého řádu | Funkcionální analýza; znaménko generátoru |
| B2 | Fourierovy / winding módy na \(S^1_\psi\) | Spektrální teorie na kružnici |
| B3 | Holomorfní výběr větve v orientované komplexní polorovině | Komplexní analýza plus omezenost / spektrální data |
| B4 | Diracovy sektory částice vs. antičástice | Teorie reprezentací; CPT |
| B5 | Dekoherované nebo Everettovské makroskopické větve | Teorie dekoherence; interpretace |

**Těchto pět pojmů není automaticky totožných.** Tato stopa řeší pouze B1–B3.
Každé mapování z B1–B3 do B4 nebo B5 vyžaduje explicitní dynamický operátor a
nezávislý důkaz.

<!-- BILINGUAL-UNIT: psi-branch.sec2 -->
## 2. Samotná holomorfie: exaktní no-go

<!-- BILINGUAL-UNIT: psi-branch.holomorphy-counterexample -->
### 2.1 Exaktní protipříklad [L0]

Stávající no-go poznámka zůstává závazná:

$$
(\partial_\tau-m)(\partial_\tau+m)f=0,
\qquad m\ne0.
$$

Má dvě celé holomorfní větve

$$
f_\pm(\tau)=e^{\pm m\tau}.
$$

Skutečně,

$$
(\partial_\tau-m)f_+=0,
\qquad
(\partial_\tau+m)f_-=0.
$$

Obě větve tedy řeší stejnou rovnici druhého řádu, a proto

$$
\boxed{\text{HOLOMORPHY-ALONE-SELECTOR: CLOSED AS NO-GO [L0]}}
$$

<!-- BILINGUAL-UNIT: psi-branch.holomorphy-status -->
### 2.2 Statusové tvrzení

To dává přesný status této výzkumné stopy

$$
\boxed{\text{holomorphy alone: CLOSED AS NO-GO [L0]}}
$$

a je to plně konzistentní s
`../action_selection/holomorphy_factor_selection_no_go.en.md` a
`../action_selection/holomorphy_factor_selection_no_go.cs.md`.

<!-- BILINGUAL-UNIT: psi-branch.holomorphy-strengthened -->
### 2.3 Co ještě zůstává k dispozici

Tato poznámka **neodporuje** uvedenému no-go, protože navržený selekční princip
používá dodatečná data:

1. samosdruženost a nezápornost \(A\);
2. orientovanou komplexní polorovinu;
3. globální podmínku omezenosti;
4. spektrální / energetickou podmínku.

Proto je zesílené tvrzení pouze

$$
\boxed{\text{holomorphy + positivity + oriented boundedness: PROPOSITION / PROOF SKETCH}}
$$

Žádné kanonické UBT odvození tohoto silnějšího selektoru se zde netvrdí.

<!-- BILINGUAL-UNIT: psi-branch.sec3 -->
## 3. Lemma o výběru větve pomocí omezené semigrupy

> **Status: PROPOSITION / PROOF SKETCH**
> Níže uvedené tvrzení je záměrně užší než odkaz na standardní Hardy-\(H^2\)
> větu. Izoluje argument s omezenou semigrupou, který se zde skutečně používá,
> a ponechává domény neomezených operátorů, existenci pokračování i úplnou
> nekonečněrozměrnou funkcionální analýzu jako otevřenou verifikační práci.

<!-- BILINGUAL-UNIT: psi-branch.semigroup-setup -->
### 3.1 Nastavení na \((\ker A)^\perp\)

Nechť \(H\) je komplexní Hilbertův prostor a \(A\) je samosdružený a
nezáporný operátor na husté doméně:

$$
A=A^*,
\qquad
A\ge0.
$$

Předpokládejme, že řešení na \((\ker A)^\perp\) připouští rozklad na větve

$$
\Phi(t)=e^{-itA}u_+ + e^{itA}u_-,
\qquad
u_\pm\in(\ker A)^\perp.
$$

To je frekvenční rozklad B1. Kernelový sektor je samostatný a je řešen v
Sekci 3.4.

<!-- BILINGUAL-UNIT: psi-branch.semigroup-continuation -->
### 3.2 Orientovaný parametr pokračování \(s>0\)

Pro matematické lemma se **nesmí** začínat kanonickým UBT symbolem \(\psi\).
Místo toho zaveďme pomocnou nekompaktní hloubku pokračování

$$
z=t-is,
\qquad
s>0.
$$

Analyticky pokračovaný výraz je

$$
\Phi(t,s)
=
e^{-itA}e^{-sA}u_+
+
e^{itA}e^{sA}u_-.
$$

Jde o tvrzení pro dolní polorovinu. Otočení orientace poloroviny obrátí, která
větev je tlumena.

<!-- BILINGUAL-UNIT: psi-branch.semigroup-proposition -->
### 3.3 Propozice a náčrt důkazu

Předpokládejme, že pokračování existuje pro všechna \(s>0\) a splňuje
uniformní podmínku omezenosti, například

$$
\sup_{s>0}\|\Phi(0,s)\|_H<\infty.
$$

Nechť \(E_A\) je spektrální míra operátoru \(A\). Pro každé \(\varepsilon>0\)
platí

$$
\left\|e^{sA}E_A([\varepsilon,\infty))u_-\right\|_H^2
=
\int_{[\varepsilon,\infty)} e^{2s\lambda}\,d\mu_-(\lambda),
$$

kde

$$
\mu_-(B)=\|E_A(B)u_-\|_H^2.
$$

Odtud

$$
\left\|e^{sA}E_A([\varepsilon,\infty))u_-\right\|_H^2
\ge
e^{2s\varepsilon}\|E_A([\varepsilon,\infty))u_-\|_H^2.
$$

Označme
$$
E_\varepsilon:=E_A([\varepsilon,\infty)),
\qquad
M:=\sup_{s>0}\|\Phi(0,s)\|_H.
$$

Abychom vyloučili vzájemné rušení rostoucí a klesající větve při odhadu normy, poznamenáme:
$$
\begin{aligned}
\|e^{sA}E_\varepsilon u_-\|_H
&\le
\|E_\varepsilon\Phi(0,s)\|_H
+
\|e^{-sA}E_\varepsilon u_+\|_H \\
&\le M+\|u_+\|_H.
\end{aligned}
$$
Zde jsme použili, že $E_\varepsilon$ komutuje s funkcionálním kalkulem, a kontraktivitu $e^{-sA}$ pro $A\ge0$.

Kombinací s dolní mezí
$$
\|e^{sA}E_\varepsilon u_-\|_H
\ge
e^{s\varepsilon}\|E_\varepsilon u_-\|_H
$$
dostaneme
$$
e^{s\varepsilon}\|E_\varepsilon u_-\|_H \le M+\|u_+\|_H
$$
pro všechna $s>0$. Protože $e^{s\varepsilon}\to\infty$ pro $s\to\infty$ (při pevném $\varepsilon>0$), z toho plyne

Uniformní omezenost pro všechna \(s>0\) vynutí

$$
E_A([\varepsilon,\infty))u_-=0
\qquad
\forall\varepsilon>0.
$$

Tedy

$$
u_-\in\ker A.
$$

Na \((\ker A)^\perp\) z toho plyne

$$
u_-=0,
$$

takže přežívající větev splňuje

$$
(i\partial_t-A)\Phi=0.
$$

To je lemma o výběru větve pomocí omezenosti, které tato stopa používá.

<!-- BILINGUAL-UNIT: psi-branch.semigroup-warning -->
### 3.4 Nulový mód a varování o omezenosti

Pro \(A=0\) má rovnice druhého řádu obecné řešení nulových módů

$$
\Phi_0(t)=u_0+t\,v_0.
$$

To **není** automaticky konstanta. Konstantním se stane až po dodatečné
podmínce, například omezenosti v reálném \(t\), která vynutí \(v_0=0\).

Dokument proto rozlišuje:

1. frekvenční výběr větve na \((\ker A)^\perp\);
2. samostatnou dynamiku \(\ker A\);
3. případnou dodatečnou podmínku odstraňující lineární zero mode.

Platí také následující omezení:

$$
\boxed{e^{s_0 A}u\in H,\quad s_0>0\quad\not\!\!\Rightarrow\quad u\in\ker A}
$$

Rozhodujícím vstupem je uniformní omezenost pro \(s\to\infty\), nikoli pouhá
existence pro každé konečné \(s\).

Pokud budoucí formulace použije Hardyho prostory, musí uvést přesný funkční
prostor a přesnou podpůrnou větu. Žádná neověřená ekvivalence se standardní
Hardy-\(H^2\) větou se zde netvrdí.

<!-- BILINGUAL-UNIT: psi-branch.sec4 -->
## 4. Značení času v UBT a překážka kompaktnosti

<!-- BILINGUAL-UNIT: psi-branch.time-symbols -->
### 4.1 Odlišné symboly, které se nesmějí ztotožnit

| Symbol | Role |
|---|---|
| \(\tau_{\mathrm{UBT}}=t+i\psi\) | Kanonický komplexní čas UBT |
| \(\bar\tau_{\mathrm{UBT}}=t-i\psi\) | Komplexně sdružená pomocná proměnná |
| \(z=t-is\) | Pomocná proměnná pokračování v dolní polorovině |
| \(\tau_\theta\) | Theta modulus |
| \(z_\theta\) | Theta argument |
| \(s>0\) | Heat / proper-time / continuation-depth parametr |

Kanonická definice

$$
\tau_{\mathrm{UBT}}=t+i\psi
$$

není touto poznámkou redefinována.

<!-- BILINGUAL-UNIT: psi-branch.s-equals-psi -->
### 4.2 Otevřená identifikace \(s\stackrel{?}{=}\psi\)

Teprve v interpretační části UBT lze položit hypotézu

$$
s\stackrel{?}{=}\psi.
$$

Tato identifikace zůstává `OPEN / CONJECTURAL`. Důvod je strukturální:
kanonické \(\psi\) je periodická / kompaktní vláknová souřadnice, zatímco
\(s>0\) je nekompaktní parametr poloroviny nebo tepelného parametru.

<!-- BILINGUAL-UNIT: psi-branch.compact-obstruction -->
### 4.3 Proč kompaktní \(\psi\) zůstává překážkou

Kanonická UBT používá značení

$$
\tau_{\mathrm{UBT}}=t+i\psi,
\qquad
\bar\tau_{\mathrm{UBT}}=t-i\psi,
$$

a může chápat \(\psi\) jako periodickou proměnnou s poloměrem \(R_\psi\).
Tlumicí faktor

$$
e^{-sA}
$$

není v \(s\) periodický. Argument s omezeností v dolní polorovině tedy
automaticky nesestupuje na globální tvrzení na kompaktním \(S^1_\psi\).

Tím zůstávají dva odlišné otevřené problémy:

1. interpretační identifikace \(s\stackrel{?}{=}\psi\);
2. kompatibilita nekompaktního selektoru s kompaktním \(S^1_\psi\).

<!-- BILINGUAL-UNIT: psi-branch.sec5 -->
## 5. Kandidátní operátor Diracova typu pro komplexní čas / vlákno

> **Status: RESEARCH ANSATZ — NOT A DERIVED CANONICAL EQUATION**

<!-- BILINGUAL-UNIT: psi-branch.gamma-star-status -->
### 5.1 Kanonický algebraický status \(\Gamma_*\)

Algebraický pátý / komplexně-časový Cliffordův kanál je v aktuálním kanonickém
materiálu **již přítomen**. V
`../../canonical/geometry/biquaternion_dirac_lift.tex` platí

$$
\Gamma_*=\operatorname{diag}(I_2,-I_2),
\qquad
\{\Gamma_*,\Gamma_\mu\}=0,
\qquad
\Gamma_*^2=I_4.
$$

Jde o ustavené tvrzení o algebraické dostupnosti, nikoli o otevřenou mezeru v
aktuálním repozitáři:

$$
\boxed{\text{algebraic existence and anticommutation of }\Gamma_*:\ \text{ESTABLISHED [L0]; recorded in the A-attested status ledger, with the detailed canonical source at tier B\_machine\_verified}}
$$

Zdrojem je kanonický soubor
`../../canonical/geometry/biquaternion_dirac_lift.tex`. Otevřené zůstává
**dynamické použití** \(\Gamma_*D_\psi\) v UBT operátoru prvního řádu, jeho
normalizace, levé/pravé působení a původ na úrovni akce.

<!-- BILINGUAL-UNIT: psi-branch.dirac-flat -->
### 5.2 Plochý model s konstantními koeficienty

Pro omezený exaktní výpočet čtverce použijme plochý model s konstantními
koeficienty

$$
\mathscr D_5^{(0)}
=
\mathscr D_4^{(0)}
+ i\hbar\Gamma_*\partial_\psi.
$$

To **není** automatické tvrzení, že kanonická UBT je obyčejná
pětidimenzionální prostoročasová teorie. Proměnnou \(\psi\) lze interpretovat jako

1. imaginární složku komplexně-časového vláknového značení;
2. interní kompaktní souřadnici;
3. skutečnou další reálnou dimenzi pouze v rozšířené interpretaci.

Použití nezávislého \(\partial_\psi\) nebo \(D_\psi\) může změnit počítání
nezávislých souřadnic a musí být explicitně porovnáno s kanonickým
značením \(\tau_{\mathrm{UBT}}=t+i\psi\).

<!-- BILINGUAL-UNIT: psi-branch.dirac-carrier -->
### 5.3 Sloupcový nosič \(\Psi=\operatorname{vec}(\Theta)\)

Matice $4\times4$ gamma $\Gamma^\mu$, $\Gamma_*$ působí na čtyřsložkový sloupcový vektor.
Protože $\Theta\in\mathbb C\otimes\mathbb H\simeq M_2(\mathbb C)$, definujeme

$$
\Psi:=\operatorname{vec}(\Theta)\in\mathbb C^4,
$$

kde $\operatorname{vec}$ skládá sloupce matice $2\times2$ $\Theta$ do jednoho sloupce.
**$\Psi$ není nové fundamentální pole**; jde o sloupcovou reprezentaci téhož $\Theta$.

Dvoustranná biquaternionová derivace je

$$
D_\psi^{(\Theta)}\Theta
:=
\partial_\psi\Theta+A_\psi\Theta-\Theta B_\psi.
$$

Indukovaná derivace na sloupcovém nosiči je

$$
\nabla_\psi\Psi
:=
\operatorname{vec}\!\left(D_\psi^{(\Theta)}\Theta\right).
$$

Poznamenejme, že vectorizace pravého násobení $B_\psi$ obecně indukuje maticové působení obsahující transponovanou pravou reprezentaci; nesmí se tiše zaměnit za obyčejné levé násobení.

Analogicky $\nabla_\mu\Psi:=\operatorname{vec}(D_\mu^{(\Theta)}\Theta)$ je indukováno z dvoustranného $D_\mu\Theta$.

Plochý operátor $\mathscr D_4^{(0)}$ je rovněž operátorem na $\Psi\in\mathbb C^4$, nikoli přímo na maticovém $\Theta$.

<!-- BILINGUAL-UNIT: psi-branch.dirac-general -->
### 5.4 Obecný výzkumný ansatz s definovaným \(D_\psi\)

Zapíše-li se křivý nebo gauge-coupled výzkumný ansatz, musí být $D_\psi$ explicitně definováno jako výše. Kandidátní rovnice, typově správně zapsaná, je pak

$$
i\hbar\Gamma^\mu\nabla_\mu\Psi
+ i\hbar\Gamma_*\nabla_\psi\Psi
- \mathcal M[\Theta,D\Theta]\Psi
=0.
$$

Zde $A_\psi$, $B_\psi$, jejich transformační zákony, jejich vztah ke čtyřrozměrným $A_\mu,B_\mu$ i jejich původ z kanonické akce zůstávají `OPEN / ANSATZ`.

<!-- BILINGUAL-UNIT: psi-branch.psi-mode -->
### 5.5 Správné působení na \(\psi\)-Fourierův mód

Pro Fourierův mód

$$
\Theta_n(q,t)e^{in\psi/R_\psi},
$$

je koeficient \(\Theta_n(q,t)\) v tomto rozkladu na \(\psi\) nezávislý, a tedy

$$
-i\partial_\psi
\left[
\Theta_n(q,t)e^{in\psi/R_\psi}
\right]
=
\frac{n}{R_\psi}
\Theta_n(q,t)e^{in\psi/R_\psi}.
$$

Stejně tak

$$
-\partial_\psi^2
\left[
\Theta_n(q,t)e^{in\psi/R_\psi}
\right]
=
\frac{n^2}{R_\psi^2}
\Theta_n(q,t)e^{in\psi/R_\psi}.
$$

Gaussianová váha je znaménkově degenerovaná:

$$
e^{-sn^2/R_\psi^2}
=
e^{-s(-n)^2/R_\psi^2}.
$$

Samotný theta / heat Gaussian tedy znaménko větve **nevybírá**.

<!-- BILINGUAL-UNIT: psi-branch.dirac-square -->
### 5.6 Exaktní plochý čtverec a nekřivá výhrada

Za předpokladů plochého modelu

$$
\{\mathscr D_4^{(0)},\Gamma_*\}=0,
\qquad
\Gamma_*^2=\varepsilon_\psi I,
$$

platí exaktní identita

$$
\left(\mathscr D_5^{(0)}\right)^2
=
\left(\mathscr D_4^{(0)}\right)^2
-\hbar^2\varepsilon_\psi\partial_\psi^2.
$$

To je jediný smysl, v němž se zde tvrdí exaktní algebraický / spektrální
můstek.

Pro obecnou křivou, gauge nebo \(\Theta\)-dependent situaci obsahuje čtverec
další smíšené členy, které musejí zůstat explicitní:

1. komutátory konexí;
2. derivace \(\Gamma_*\);
3. derivace hmotového funkcionálu;
4. členy křivosti levé/pravé strany;
5. členy řetězového pravidla z kompozitní geometrie.

Každé tvrzení o heat kernelu patří odpovídajícímu nezápornému eukleidovskému
čtverci, nikoli automaticky Lorentzovskému operátoru.

<!-- BILINGUAL-UNIT: psi-branch.sec6 -->
## 6. Diracovy a Schrödingerovy limity

<!-- BILINGUAL-UNIT: psi-branch.hierarchy -->
### 6.1 Správná hierarchie

Hierarchie operátorů je

$$
\text{first-order Dirac}
\longrightarrow
\text{non-relativistic Pauli / Schrödinger limit}
$$

a samostatně

$$
\text{Dirac}^2
\longrightarrow
\text{Laplace / Klein--Gordon type}
\longrightarrow
\text{heat kernel}
\longrightarrow
\text{theta function}.
$$

<!-- BILINGUAL-UNIT: psi-branch.not-implied -->
### 6.2 Co výběr větve neodvozuje

Lemma o výběru větve pomocí omezenosti samo o sobě **neodvozuje** nic z
následujícího:

1. lokální Cliffordův Diracův operátor;
2. spinorovou reprezentaci;
3. hmotnostní člen;
4. fermionickou statistiku;
5. interpretaci částice / antičástice.

Každá položka vyžaduje nezávislé odvození z kanonické UBT.

Navíc, podle `../canonical_relation_generalized_dirac/action_origin_obstruction.tex`, nedegenerovaná kvadratická akce prvních derivací $\Theta$ vede k rovnici Eulera–Lagrangeovy druhého řádu a nemůže být proto přímo totožná s first-order zobecněnou Diracovou rovnicí. Jde o no-go pouze pro dokumentovanou nedegenerovanou třídu akcí, nikoli pro všechny myslitelné UBT akce. Možné uzavření vyžaduje odvozenou degeneraci, přesnou faktorizaci plus selekční teorém, nebo ekvivalentní vazbový variační princip. Lemma s analytickým pokračováním může za svých předpokladů vybrat větev již faktorizované rovnice, ale samo neodvozuje faktorizaci, Diracův operátor ani jeho akci.

Tento $\psi$-track neodstraňuje překážku action-origin.

<!-- BILINGUAL-UNIT: psi-branch.sec7 -->
## 7. Multivesmírná interpretace

> **Status: SPECULATIVE**

<!-- BILINGUAL-UNIT: psi-branch.mode-decomposition -->
### 7.1 Módový rozklad

Formálně lze psát

$$
\Theta(q,t,\psi)
=
\sum_\alpha \Theta_\alpha(q,t)\chi_\alpha(\psi),
$$

s bází \(\{\chi_\alpha\}\) přizpůsobenou \(S^1_\psi\), například Fourierovými
módy.

<!-- BILINGUAL-UNIT: psi-branch.multiverse-caveats -->
### 7.2 Proč to neustanovuje mnoho světů

1. Bodová hodnota \(\psi=\psi_0\) je obecně superpozicí mnoha Fourierových
   módů; není projektorem na jediný mód.
2. Neodvozuje se zde žádné Bornovo pravidlo, věta o dekoherenci ani
   interpretace vesmírů.
3. Označení módů nejsou automaticky vesmíry.

Multivesmírné čtení tedy zůstává přísně `SPECULATIVE`.

<!-- BILINGUAL-UNIT: psi-branch.sec8 -->
## 8. Podmíněná poznámka k Riemannově hypotéze

> **Status: CONDITIONAL RESEARCH DIRECTION — NOT A PROOF OF RH OR AN ADVANCE TOWARD RH**

<!-- BILINGUAL-UNIT: psi-branch.rh-structural -->
### 8.1 Pouze strukturální pozorování

Při logaritmické substituci \(u=e^{2\psi}\) se klasická Mellinova vazba mezi
Jacobiho theta funkcí a \(\xi(s)\) týká pouze struktury funkcionální rovnice.
Riemannovu hypotézu tím **nevzniká**.

<!-- BILINGUAL-UNIT: psi-branch.rh-missing -->
### 8.2 Co stále chybí

Nadále chybějí tyto složky:

1. samosdružený operátor se spektrem svázaným s ordinátami nul zeta funkce;
2. determinantová nebo trace formula obsahující prvočíselné délky \(k\log p\);
3. odvození vztahu takového operátoru k \(N_\psi=-iR_\psi\partial_\psi\).

Jednoduchý winding operátor \(N_\psi\) má celočíselné spektrum. To samo o sobě
neodpovídá ordinátám nul zeta funkce.

<!-- BILINGUAL-UNIT: psi-branch.gr-claim-boundary -->
## 9. Vztah k aktuální hranici tvrzení o GR

<!-- BILINGUAL-UNIT: psi-branch.gr-kinematics -->
### 9.1 Co je dokázáno kinematicky

V rámci přesných předpokladů jsou ustaveny zejména:

- centrální metrika z antikomutátorové identity: $\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf{1}$;
- hodnost 10 zobrazení tetrády na metriku a šest lokálních Lorentzových nulových směrů: `GAP-10K: CLOSED locally`;
- rekonstrukce metrické konexe ze zadané tetrády a torze: `GAP-10Omega-KIN: CLOSED [L1]`;
- torzně volná větev jako Levi-Civitova spinová konexe: `GAP-10Omega-GR: CLOSED [L1]`;
- plochý Minkowského reprezentant: `GAP-10I-SR: CLOSED [L1]`;
- lokální reprezentovatelnost zakřivených tetrád na regulárních nenulových patchích pomocí kompozitního/split-jet mechanismu: `GAP-10I-TORSION-LOCAL: CLOSED LOCALLY [L1]`.

Lokální reprezentovatelnost **neznamená** dynamický výběr tetrády z $\Theta$.

<!-- BILINGUAL-UNIT: psi-branch.gr-conditional -->
### 9.2 Co je uzavřeno pouze podmíněně

`GR-RECOVERY: CLOSED CONDITIONALLY`

Podmíněná lokální infračervená efektivní větev skládá:

- split-jet pravou inverzi;
- nepropagující pomocný sektor;
- předpokládanou/odvozenou podmíněnou Einsteinovu–Hilbertovu efektivní větev;
- Levi-Civitovu fyzickou konexi;
- potlačení vyšších derivací v příslušném infračerveném řádu.

Podmíněný vztah je

$$
\frac{1}{G_{\mathrm{ind}}}
=
\frac{N_B(1-6\xi)I_1}{12\pi}.
$$

Jeho podmínky jsou: specifikovaný gauge-fixed Laplace-type Hessián, počet reálných bosonických módů $N_B$, coupling $\xi$, cutoff/scale identification, regulátor a constrained measure.

<!-- BILINGUAL-UNIT: psi-branch.gr-not-derived -->
### 9.3 Co odvozeno není

Podle `AXIOM D` v `canonical/AXIOMS.md` není implikace

$$
\mathrm{UBT}
\Longrightarrow
G_{\mu\nu}=\kappa T_{\mu\nu}
$$

(kanonické UBT rovnice implikují Einsteinovy polní rovnice) bezpodmínečně dokázána.

Otevřené statusové položky:

- `UBT-FUND-GR-ACTION: OPEN`
- `UBT-UV-G-PREDICTION: OPEN`
- `UBT-FUND-GLOBAL: OPEN`

Současné axiomy neurčují numerickou Newtonovu konstantu; `canonical/CANONICAL_DEFINITIONS.md` vede $G$ jako `Input`, nikoli `Prediction`. Čistý split-jet constraint nemůže vybrat tetrádu, protože je univerzálně surjektivní: `GAP-10T-JET-CONSTRAINT-SELECTION: CLOSED AS NO-GO [L1]`. Action-level selekce z mikroskopické $\Theta$-akce zůstává otevřená. Globální pokračování přes nulové plochy, horizonty a topologicky netriviální oblasti není dokázáno. Starší povýšení prostorové Schwarzschildovy identity na úplné on-shell řešení z jediného $\Theta$ zůstává `SUPERSEDED_INVALID_DERIVATION`. Schwarzschild jako řešení podmíněně obnovené Einsteinovy větve není totéž jako přímé odvození Schwarzschildova řešení z mikroskopické $\Theta$-rovnice.

<!-- BILINGUAL-UNIT: psi-branch.gr-psi-relation -->
### 9.4 Vztah nového \(\psi\)-tracku ke GR

Tato výzkumná stopa **nemění** žádný GR status. Selekce frekvenční větve neodvozuje Einsteinovu–Hilbertovu akci, nepredikuje $G$, neřeší globální pokračování a neopravuje stažený přímý Schwarzschildův ansatz. Každý first-order UBT operátor musí být nejprve odvozen z konzistentní akce; teprve poté lze zkoumat jeho GR limit.

<!-- BILINGUAL-UNIT: psi-branch.sec9 -->
## 10. Interpretační a architektonické mantinely

<!-- BILINGUAL-UNIT: psi-branch.guardrails -->
1. Lemma o výběru větve pomocí omezenosti je matematická propozice, nikoli kanonická
   UBT věta o selektoru.
2. Identifikace \(s\stackrel{?}{=}\psi\) je otevřená a konjekturální.
3. Kompatibilita s kompaktním \(\psi\) je otevřená.
4. Operátor Diracova typu s \(D_\psi\) je výzkumný ansatz, nikoli odvozená
   kanonická rovnice.
5. Algebraická existence \(\Gamma_*\) je již dostupná; otevřené je pouze její
   fyzikální / dynamické použití.

<!-- BILINGUAL-UNIT: psi-branch.sec10 -->
## 11. Verifikace

<!-- BILINGUAL-UNIT: psi-branch.verification-script -->
### 11.1 Verifikační skript

Spusťte

```bash
python tools/verify_psi_branch_selection.py
```

Skript je samostatně spouštěný ověřovač. Je to regresní / CAS kontrola, nikoli důkaz nekonečněrozměrného lemmatu.
Jeho kontroly jsou:

| Kontrola | Popis |
|---|---|
| V1 | Exaktní faktorizace \((i\partial_t-A)(-i\partial_t-A)=\partial_t^2+A^2\) na obecné skalární testovací funkci |
| V2 | Exaktní ověření obou exponenciálních větví a správného anihilujícího faktoru prvního řádu |
| V3 | Exaktní ověření \(e^{-iA(t-is)}=e^{-itA}e^{-sA}\) a jeho rostoucího protějšku |
| V4 | Kontrola znaménka tlumení/růstu pro obě větve při \(s>0\), \(A>0\) |
| V5 | Konečněrozměrný příklad diagonální spektrální omezenosti pro \(A=A^*\ge0\) |
| V6 | Obecný nulový mód \(\Phi_0(t)=u_0+t\,v_0\) a výhrada omezenosti |
| V7 | Správná derivace celého Fourierova módu \(\Theta_n(q,t)e^{in\psi/R_\psi}\) |
| V8 | Vlastní hodnoty \(n/R_\psi\) a \(n^2/R_\psi^2\) |
| V9 | Gaussianová degenerace \(n\leftrightarrow -n\) |
| V10 | Rušení smíšených členů při umocnění plochého modelu \(\Gamma_*\) |

`../../tools/verify_holomorphy_factor_no_go.py` zůstává exaktní regresní
kontrolou pro no-go založené pouze na holomorfii.

<!-- BILINGUAL-UNIT: psi-branch.lean-status -->
### 11.2 Stav Lean

**LEAN-PENDING.** Není přidán žádný zkompilovaný Lean důkaz. Zbývající
formalizační práce zahrnuje detaily operátorových domén, existenci pokračování
a plný nekonečněrozměrný argument se spektrální mírou.

<!-- BILINGUAL-UNIT: psi-branch.sec11 -->
## 12. Otevřené gapy

<!-- BILINGUAL-UNIT: psi-branch.gap-table -->
| Mezera | Popis | Status |
|---|---|---|
| G1 | Lemma o výběru větve pomocí omezenosti: úplná doména a ověření pokračování | PROPOSITION / PROOF SKETCH |
| G2 | Identifikace \(s\stackrel{?}{=}\psi\) | OPEN / CONJECTURAL |
| G3-DYN | Dynamické použití \(\Gamma_*D_\psi\), jeho normalizace, levé/pravé působení a původ na úrovni akce | OPEN |
| G4 | Kompatibilita nekompaktního selektoru s kompaktním \(S^1_\psi\) | OPEN |
| G5 | Původ, normalizace, reprezentace a transformační zákon \(D_\psi\), \(A_\psi\), \(B_\psi\) za plochým ansatzem | OPEN / ANSATZ |
| G6 | Odvození na úrovni akce celého operátoru prvního řádu a jeho spektrálního / energetického selektoru | OPEN |
| G7 | Lean proof of the infinite-dimensional statement | LEAN-PENDING |

<!-- BILINGUAL-UNIT: psi-branch.sec12 -->
## 13. Přehled statusů

<!-- BILINGUAL-UNIT: psi-branch.status-table -->
| Oddíl | Status |
|---|---|
| S2: Selektor samotné holomorfie | CLOSED AS NO-GO [L0] |
| S3: Lemma o výběru větve pomocí omezenosti | PROPOSITION / PROOF SKETCH |
| S4: \(s\) vs. kanonické \(\psi\) a kompaktnost | OPEN / CONJECTURAL plus OPEN |
| S5: Kandidátní operátor Diracova typu pro komplexní čas / vlákno | RESEARCH ANSATZ |
| S6: Hierarchie limit | STANDARD PHYSICS FACT |
| S7: Multivesmírná interpretace | SPECULATIVE |
| S8: Strukturální poznámka k RH | CONDITIONAL RESEARCH DIRECTION — NOT A PROOF OF RH OR AN ADVANCE TOWARD RH |
| S9: Vztah k GR | KINEMATICS ESTABLISHED; GR-RECOVERY CLOSED CONDITIONALLY; FUNDAMENTAL / UV / GLOBAL DERIVATION OPEN |
| S11: Stav formální verifikace | LEAN-PENDING |

Touto stopou se nemění žádný kanonický axiom, definice, master rovnice, tvrzení
ani status mezery.
