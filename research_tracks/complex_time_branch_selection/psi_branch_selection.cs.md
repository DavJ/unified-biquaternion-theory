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

# Výběr first-order dynamické větve pomocí komplexně-časového pokračování a vláknových dat

**Typ stopy:** RESEARCH TRACK — MATHEMATICAL SELECTION LEMMA PLUS CONJECTURAL UBT INTERPRETATION  
**Datum:** 2026-09-02  
**Status:** holomorphy alone je `CLOSED AS NO-GO [L0]`; bounded branch-selection lemma je `PROPOSITION / PROOF SKETCH`; UBT identifikace `s ?= \psi` je `OPEN / CONJECTURAL`; Dirac-type operátor je `RESEARCH ANSATZ`; multivesmírné čtení je `SPECULATIVE`; RH spojitost je `CONDITIONAL RESEARCH DIRECTION — NOT AN ADVANCE TOWARD RH`.

**Anglická edice:** `psi_branch_selection.en.md`  
**Bilingvní politika:** `../../BILINGUAL_CONTENT_POLICY.cs.md`  
**Verifikační skripty:** `../../tools/verify_psi_branch_selection.py`, `../../tools/verify_holomorphy_factor_no_go.py`

---

<!-- BILINGUAL-UNIT: psi-branch.scope -->
> **Rozsah tohoto dokumentu.** Tato výzkumná stopa opravuje existující patch
> bez změny jakéhokoli kanonického axiomu, definice, master equation, claimu
> nebo gap statusu. Výslovně respektuje
> `../action_selection/holomorphy_factor_selection_no_go.en.md`,
> `../action_selection/holomorphy_factor_selection_no_go.cs.md`,
> `../canonical_relation_generalized_dirac/action_origin_obstruction.tex` a
> existující kanonický pátý / complex-time Cliffordův kanál v
> `../../canonical/geometry/biquaternion_dirac_lift.tex`.

---

<!-- BILINGUAL-UNIT: psi-branch.sec1 -->
## 1. Motivace a přesná taxonomie větví

Následující pojmy „větve“ se nesmějí zaměňovat.

<!-- BILINGUAL-UNIT: psi-branch.taxonomy -->
| ID | Pojem | Doména definice |
|---|---|---|
| B1 | Frekvenční větve faktorizované second-order ODE/PDE | Funkcionální analýza; znaménko generátoru |
| B2 | Fourierovy / winding módy na \(S^1_\psi\) | Spektrální teorie na kružnici |
| B3 | Holomorfní výběr větve v orientované komplexní polorovině | Komplexní analýza plus boundedness / spektrální data |
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

Obě větve tedy řeší stejnou second-order rovnici, a proto

$$
\boxed{\text{Holomorphy alone does not select the first-order factor.}}
$$

<!-- BILINGUAL-UNIT: psi-branch.holomorphy-status -->
### 2.2 Statusové tvrzení

To dává přesný research-track status

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
3. globální podmínku boundedness;
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
### 3.1 Setup na \((\ker A)^\perp\)

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
uniformní podmínku boundedness, například

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

Uniformní boundedness pro všechna \(s>0\) vynutí

$$
E_A([\varepsilon,\infty))u_-=0
\qquad
\text{for every }\varepsilon>0.
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

To je lemma o výběru větve pomocí boundedness, které tato stopa používá.

<!-- BILINGUAL-UNIT: psi-branch.semigroup-warning -->
### 3.4 Nulový mód a varování o boundedness

Pro \(A=0\) má second-order rovnice obecné zero-mode řešení

$$
\Phi_0(t)=u_0+t\,v_0.
$$

To **není** automaticky konstanta. Konstantním se stane až po dodatečné
podmínce, například boundedness v reálném \(t\), která vynutí \(v_0=0\).

Dokument proto rozlišuje:

1. frekvenční výběr větve na \((\ker A)^\perp\);
2. samostatnou dynamiku \(\ker A\);
3. případnou dodatečnou podmínku odstraňující lineární zero mode.

Platí také následující omezení:

$$
\boxed{\text{For each fixed finite }s,\ e^{sA}u\in H\ \text{does not imply }u\in\ker A.}
$$

Rozhodujícím vstupem je uniformní boundedness pro \(s\to\infty\), nikoli pouhá
existence pro každé konečné \(s\).

Pokud budoucí formulace použije Hardyho prostory, musí uvést přesný funkční
prostor a přesnou podpůrnou větu. Žádná neověřená ekvivalence se standardní
Hardy-\(H^2\) větou se zde netvrdí.

<!-- BILINGUAL-UNIT: psi-branch.sec4 -->
## 4. UBT bookkeeping času a překážka kompaktnosti

<!-- BILINGUAL-UNIT: psi-branch.time-symbols -->
### 4.1 Odlišné symboly, které se nesmějí ztotožnit

| Symbol | Role |
|---|---|
| \(\tau_{\mathrm{UBT}}=t+i\psi\) | Kanonický komplexní čas UBT |
| \(\bar\tau_{\mathrm{UBT}}=t-i\psi\) | Komplexně sdružená bookkeeping proměnná |
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
\(s>0\) je nekompaktní parametr poloroviny nebo heat parametru.

<!-- BILINGUAL-UNIT: psi-branch.compact-obstruction -->
### 4.3 Proč kompaktní \(\psi\) zůstává překážkou

Kanonická UBT používá bookkeeping

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

není v \(s\) periodický. Argument s boundedness v dolní polorovině tedy
automaticky nesestupuje na globální tvrzení na kompaktním \(S^1_\psi\).

Tím zůstávají dva odlišné otevřené problémy:

1. interpretační identifikace \(s\stackrel{?}{=}\psi\);
2. kompatibilita nekompaktního selektoru s kompaktním \(S^1_\psi\).

<!-- BILINGUAL-UNIT: psi-branch.sec5 -->
## 5. Kandidátní complex-time / fibre Dirac-type operátor

> **Status: RESEARCH ANSATZ — NOT A DERIVED CANONICAL EQUATION**

<!-- BILINGUAL-UNIT: psi-branch.gamma-star-status -->
### 5.1 Kanonický algebraický status \(\Gamma_*\)

Algebraický pátý / complex-time Cliffordův kanál je v aktuálním kanonickém
materiálu **již přítomen**. V
`../../canonical/geometry/biquaternion_dirac_lift.tex` platí

$$
\Gamma_*=\operatorname{diag}(I_2,-I_2),
\qquad
\{\Gamma_*,\Gamma_\mu\}=0,
\qquad
\Gamma_*^2=I_4.
$$

Jde o tvrzení o exaktní algebraické dostupnosti, nikoli o otevřený gap v
aktuálním repozitáři. Otevřené zůstává **dynamické použití**
\(\Gamma_*D_\psi\) v first-order UBT operátoru a jeho action-level původ.

<!-- BILINGUAL-UNIT: psi-branch.dirac-flat -->
### 5.2 Flat model s konstantními koeficienty

Pro omezený exaktní výpočet čtverce použijme flat model s konstantními
koeficienty

$$
\mathscr D_5^{(0)}
=
\mathscr D_4^{(0)}
+ i\hbar\Gamma_*\partial_\psi.
$$

To **není** automatické tvrzení, že kanonická UBT je obyčejná
pětidimenzionální spacetime teorie. Proměnnou \(\psi\) lze interpretovat jako

1. imaginární složku komplexně-časového fibre bookkeepingu;
2. interní kompaktní souřadnici;
3. skutečnou další reálnou dimenzi pouze v rozšířené interpretaci.

Použití nezávislého \(\partial_\psi\) nebo \(D_\psi\) může změnit počítání
nezávislých souřadnic a musí být explicitně porovnáno s kanonickým
bookkeepingem \(\tau_{\mathrm{UBT}}=t+i\psi\).

<!-- BILINGUAL-UNIT: psi-branch.dirac-general -->
### 5.3 Obecný research ansatz s definovaným \(D_\psi\)

Zapíše-li se křivý nebo gauge-coupled research ansatz, musí být \(D_\psi\)
explicitně definováno:

$$
D_\psi\Theta
=
\partial_\psi\Theta
+ A_\psi\Theta
- \Theta B_\psi.
$$

Odpovídající kandidátní rovnice je pak

$$
i\hbar\Gamma^\mu D_\mu\Theta
+ i\hbar\Gamma_*D_\psi\Theta
- \mathcal M[\Theta]\Theta
=
0.
$$

Zde \(A_\psi\), \(B_\psi\), jejich transformační zákony, jejich vztah ke
čtyřrozměrným \(A_\mu,B_\mu\) i jejich původ z kanonické akce zůstávají
`OPEN / ANSATZ`.

<!-- BILINGUAL-UNIT: psi-branch.psi-mode -->
### 5.4 Správné působení na \(\psi\)-Fourierův mód

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
### 5.5 Exaktní flat čtverec a nekřivá výhrada

Za předpokladů flat modelu

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
bridge.

Pro obecnou křivou, gauge nebo \(\Theta\)-dependent situaci obsahuje čtverec
další cross-termy, které musejí zůstat explicitní:

1. komutátory konexí;
2. derivace \(\Gamma_*\);
3. derivace hmotového funkcionálu;
4. left/right curvature terms;
5. chain-rule terms z kompozitní geometrie.

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

Lemma o výběru větve pomocí boundedness samo o sobě **neodvozuje** nic z
následujícího:

1. lokální Cliffordův Diracův operátor;
2. spinorovou reprezentaci;
3. hmotnostní člen;
4. fermionickou statistiku;
5. interpretaci částice / antičástice.

Každá položka vyžaduje nezávislé odvození z kanonické UBT.

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

> **Status: CONDITIONAL RESEARCH DIRECTION — NOT AN ADVANCE TOWARD RH**

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

<!-- BILINGUAL-UNIT: psi-branch.sec9 -->
## 9. Interpretační a architektonické guardrails

<!-- BILINGUAL-UNIT: psi-branch.guardrails -->
1. Bounded branch-selection lemma je matematická propozice, nikoli kanonická
   UBT věta o selektoru.
2. Identifikace \(s\stackrel{?}{=}\psi\) je otevřená a conjectural.
3. Kompatibilita s compact-\(\psi\) je otevřená.
4. Dirac-type operátor s \(D_\psi\) je research ansatz, nikoli odvozená
   kanonická rovnice.
5. Algebraická existence \(\Gamma_*\) je již dostupná; otevřené je pouze její
   fyzikální / dynamické použití.

<!-- BILINGUAL-UNIT: psi-branch.sec10 -->
## 10. Verifikace

<!-- BILINGUAL-UNIT: psi-branch.verification-script -->
### 10.1 Verifikační skript

Spusťte

```bash
python tools/verify_psi_branch_selection.py
```

Skript je regresní / CAS kontrola, nikoli důkaz nekonečněrozměrného lemmatu.
Jeho kontroly jsou:

| Check | Description |
|---|---|
| V1 | Exact factorization \((i\partial_t-A)(-i\partial_t-A)=\partial_t^2+A^2\) on a generic scalar test function |
| V2 | Exact verification of both exponential branches and of the correct annihilating first-order factor |
| V3 | Exact verification of \(e^{-iA(t-is)}=e^{-itA}e^{-sA}\) and its growing companion |
| V4 | Decay / growth sign check for the two branches under \(s>0\), \(A>0\) |
| V5 | Finite-dimensional diagonal spectral boundedness example for \(A=A^*\ge0\) |
| V6 | General zero mode \(\Phi_0(t)=u_0+t\,v_0\) and the boundedness caveat |
| V7 | Correct differentiation of the whole Fourier mode \(\Theta_n(q,t)e^{in\psi/R_\psi}\) |
| V8 | Eigenvalues \(n/R_\psi\) and \(n^2/R_\psi^2\) |
| V9 | Gaussian degeneracy \(n\leftrightarrow -n\) |
| V10 | Cross-term cancellation in the flat \(\Gamma_*\) model square |

`../../tools/verify_holomorphy_factor_no_go.py` zůstává exaktní regresní
kontrolou pro no-go založené pouze na holomorfii.

<!-- BILINGUAL-UNIT: psi-branch.lean-status -->
### 10.2 Stav Lean

**LEAN-PENDING.** Není přidán žádný zkompilovaný Lean důkaz. Zbývající
formalizační práce zahrnuje detaily operátorových domén, existenci pokračování
a plný nekonečněrozměrný argument se spektrální mírou.

<!-- BILINGUAL-UNIT: psi-branch.sec11 -->
## 11. Otevřené gapy

<!-- BILINGUAL-UNIT: psi-branch.gap-table -->
| Gap | Description | Status |
|---|---|---|
| G1 | Bounded branch-selection lemma: full domain and continuation verification | PROPOSITION / PROOF SKETCH |
| G2 | Identification \(s\stackrel{?}{=}\psi\) | OPEN / CONJECTURAL |
| G3 | Compatibility of the non-compact selector with compact \(S^1_\psi\) | OPEN |
| G4 | Dynamical use of \(\Gamma_*D_\psi\) in a first-order UBT operator | OPEN |
| G5 | Origin, normalization, representation, and transformation law of \(D_\psi\), \(A_\psi\), \(B_\psi\) | OPEN / ANSATZ |
| G6 | Action-level derivation of the full first-order operator and its spectral / energy selector | OPEN |
| G7 | Lean proof of the infinite-dimensional statement | LEAN-PENDING |

<!-- BILINGUAL-UNIT: psi-branch.sec12 -->
## 12. Přehled statusů

<!-- BILINGUAL-UNIT: psi-branch.status-table -->
| Section | Status |
|---|---|
| S2: Holomorphy-alone selector | CLOSED AS NO-GO [L0] |
| S3: Bounded branch-selection lemma | PROPOSITION / PROOF SKETCH |
| S4: \(s\) vs. canonical \(\psi\) and compactness | OPEN / CONJECTURAL plus OPEN |
| S5: Candidate complex-time / fibre Dirac-type operator | RESEARCH ANSATZ |
| S6: Hierarchy of limits | STANDARD PHYSICS FACT |
| S7: Multiverse interpretation | SPECULATIVE |
| S8: RH structural note | CONDITIONAL RESEARCH DIRECTION — NOT AN ADVANCE TOWARD RH |
| S10: Formal verification status | LEAN-PENDING |

Touto stopou se nemění žádný kanonický axiom, definice, master equation, claim
ani gap status.
