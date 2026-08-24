<!-- BILINGUAL-UNIT: theta-multisymplectic.provenance -->
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

# Kanonická invariantní multisymplektická rodina akcí z kvadratického tvaru Theta

<!-- BILINGUAL-UNIT: theta-multisymplectic.hermitian -->
## Invariantní hermitovský tvar z dokázaného kvadratického invariantu

Pišme obecnou hodnotu pole jako

\[
z=(a,b,c,d)^T\in\mathbb C^4,
\]

takže již klasifikovaný kvadratický invariant je

\[
H(z)=z^\dagger Gz,
\qquad
G=\begin{pmatrix}
0&0&0&1\\
0&-1&0&0\\
0&0&-1&0\\
1&0&0&0
\end{pmatrix}.
\]

Spojené působení UBT na pole je komplexně lineární a zachovává `H`. Komplexní
polarizací tedy zachovává celý hermitovský tvar

\[
\boxed{h(u,v)=u^\dagger Gv.}
\]

Matice `G` je reálná, hermitovská a invertibilní (`det G=-1`). Tvar `h` je
tedy nedegenerovaný.

<!-- BILINGUAL-UNIT: theta-multisymplectic.symplectic -->
## Kanonická invariantní reálná symplektická forma [L0]

Na podkladovém osmirozměrném reálném prostoru polí definujme

\[
\boxed{\omega(u,v):=\operatorname{Im}h(u,v).}
\]

Pro `z=x+iy` má její reálná matice tvar

\[
\Omega=\begin{pmatrix}0&G\\-G&0\end{pmatrix}.
\]

Proto

\[
\det\Omega=(\det G)^2=1,
\]

takže `omega` je nedegenerovaná. Je antisymetrická, protože `h` je hermitovský,
a invariantní, protože `h` je invariantní. Její koeficienty jsou v lineárních
souřadnicích prostoru polí konstantní, a tedy

\[
\boxed{d\omega=0.}
\]

Současná reprezentace pole UBT proto nese kanonickou invariantní
pseudo-Kählerovskou/symplektickou strukturu bez zavedení druhého fyzického pole.

<!-- BILINGUAL-UNIT: theta-multisymplectic.action -->
## Rodina variačních principů prvního řádu bez dalších polí [L1]

Nechť

\[
\Omega_4:=\frac12\omega\wedge\omega
\]

a nechť `F` je libovolný reálný skalární invariant hodnoty pole, například
funkce již klasifikovaných invariantů `H` a `D=|det X|^2`. Pro čtyřrozměrné
prostoročasové zobrazení `Theta:M_4 -> R^8` definujme

\[
\boxed{S_F[\Theta]=\int_{M_4}\Theta^*(F\,\Omega_4).}
\]

Tato akce:

- používá pouze `Theta` a jeho první derivace;
- je invariantní vůči změnám souřadnic prostoročasu, protože integruje pullback
  čtyřformy;
- je invariantní vůči spojenému internímu působení UBT, pokud je `F`
  invariantní;
- neobsahuje nezávislou tetrádu, metriku ani konexi;
- má first-jet Hessián v dvojitě antisymetrickém sektoru vyžadovaném přesným
  kritériem Hessiánu prvního řádu.

Pomocí Cartanovy variační formule a `d Omega_4=0` je její objemová variace

\[
\boxed{
\delta S_F
=\int_{M_4}\Theta^*\!\left(
\iota_{\delta\Theta}(dF\wedge\Omega_4)
\right)
+\text{boundary}.}
\]

Eulerova–Lagrangeova rovnice tedy obsahuje pouze první derivace `Theta`. Pro
konstantní `F` je `dF=0` a akce je null/topologický Lagrangián. Pro nekonstantní
invariantní `F` je pěti-forma `dF wedge Omega_4` genericky nenulová a variační
princip není identicky pouze hraničním členem.

<!-- BILINGUAL-UNIT: theta-multisymplectic.witness -->
## Svědek netriviality

Vezměme `F=H`. V bodě s `x_a=1` a všemi ostatními reálnými složkami nulovými
je `dH=2 dx_d` nenulové. Protože `omega` je symplektická na osmirozměrném
prostoru, Lefschetzovo zobrazení

\[
\alpha\longmapsto\alpha\wedge\omega^2
\]

je na jednoformách injektivní. Proto

\[
\boxed{dH\wedge\omega^2\ne0}
\]

v tomto bodě. `S_H` je tedy explicitní invariantní člen rodiny, jehož objemová
Eulerova–Lagrangeova forma prvního řádu není identicky nulová.

<!-- BILINGUAL-UNIT: theta-multisymplectic.limit -->
## Co se tím řeší a co ne

Tím se uzavírá důležitá existenční otázka ponechaná obstrukcí původu
generalizovaného Diracova operátoru z akce: **kanonická data UBT připouštějí
netriviální invariantní first-jet akce bez dalších polí, jejichž
Eulerovy–Lagrangeovy rovnice jsou skutečně prvního řádu.** Obstrukce běžného
symetrického kvadratického kinetického členu tedy není univerzálním no-go proti
dynamice UBT prvního řádu.

Rodina `S_F` však ještě není hledanou jedinou fundamentální akcí. Invariantní
skalár `F` není vybrán; Eulerova–Lagrangeova rovnice ještě nebyla dokázána jako
ekvivalentní kanonické generalizované Diracově rovnici; je třeba otestovat
transverzalitu hodnosti deset, zakřivenou obnovu GR, fyzický sektor `psi` a
kvantový Hessián. Existence této rodiny zejména nesmí být vykazována jako
uzavření `UBT-FUND-GR-ACTION`.

<!-- BILINGUAL-UNIT: theta-multisymplectic.verification -->
## Ověření

`tools/verify_theta_multisymplectic_action.py` exaktně kontroluje, že reálná
symplektická matice je antisymetrická a nedegenerovaná, a sestavuje nenulovou
složku `dH wedge omega wedge omega`. Párový pytest udržuje tato konečně
algebraická tvrzení v CI.

Polarizační argument a Cartanova variační formule jsou analytické. Formalizace
konečných maticových/symplektických tvrzení v Leanu je `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: theta-multisymplectic.status -->
## Dopad na status

**EXISTENCE OF AN INVARIANT NO-EXTRA-FIELD FIRST-ORDER VARIATIONAL FAMILY:
PROVED [L1].**

**SELECTION OF A UNIQUE MEMBER AND EQUIVALENCE TO GENERALIZED-DIRAC/GR
DYNAMICS: OPEN.**
