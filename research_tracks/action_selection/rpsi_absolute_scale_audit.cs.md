<!-- BILINGUAL-UNIT: rpsi-scale-audit.provenance -->
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

# Audit tvrzení o absolutní škále `R_psi`

<!-- BILINGUAL-UNIT: rpsi-scale-audit.scope -->
## Rozsah

V kanonickém geometrickém korpusu je historické tvrzení, že jednosmyčkový
modulový potenciál fixuje kompaktní poloměr imaginárního času v self-duálním
bodě `R_psi = R_t`. Než použijeme `R_psi` k určení délkové škály `ell`
pátokanálové gravitační konexe, je nutné přímo ověřit skutečné tvrzení o
stacionaritě.

Zobrazený jednosmyčkový potenciál v `canonical/geometry/Rpsi_dynamical_fix.tex`
je

\[
V_{\rm mod}(R_\psi)
=-\frac32\ln(2\pi R_\psi)-E_3'(0).
\]

<!-- BILINGUAL-UNIT: rpsi-scale-audit.derivative -->
## Exaktní kontrola derivace [L0]

Pro každé konečné `R_psi > 0` platí

\[
\boxed{
\frac{dV_{\rm mod}}{dR_\psi}
=-\frac{3}{2R_\psi}\ne0.}
\]

Zobrazený potenciál tedy **nemá žádný konečný stacionární bod**. Sám o sobě
zejména nemá minimum v `R_psi = R_t`.

Jde o opravu vnitřní konzistence: neodmítá modularní self-dualitu jako
strukturální podmínku; odmítá pouze silnější tvrzení, že zobrazený logaritmický
determinant již poskytuje dynamické absolutní minimum.

<!-- BILINGUAL-UNIT: rpsi-scale-audit.modular -->
## Co může fixovat modularní self-dualita

Položme

\[
x:=\frac{R_\psi}{R_t}>0.
\]

Modulární inverze působí jako `x -> 1/x`. Její jediný kladný pevný bod je

\[
\boxed{x=1,\qquad R_\psi=R_t.}
\]

Pokud je diferencovatelný dokončený efektivní potenciál skutečně invariantní,

\[
V(x)=V(1/x),
\]

pak derivace dává

\[
V'(x)=-\frac1{x^2}V'(1/x),
\]

a v pevném bodě

\[
\boxed{V'(1)=0.}
\]

Exaktní modularní invariance tedy může vybrat **bezrozměrný poměr**
`R_psi/R_t = 1` jako stacionární bod dokončeného invariantního potenciálu.
Bez další fyzikální škály nebo mechanismu generujícího škálu neurčuje společnou
absolutní délku.

<!-- BILINGUAL-UNIT: rpsi-scale-audit.n0 -->
## Proč `N0` nepřidává druhou fyzikální škálu

Zamčené axiomy UBT definují `N0 > 0` jako pevnou globální **unit-setting
konstantu** ve vztahu

\[
E_\mu=N_0^{-1/2}D_\mu\Theta.
\]

Není registrována jako nezávisle predikovaná dynamická pozorovatelná veličina.
Konvence škálování nesená pouze `N0` se proto nesmí počítat jako druhý
fyzikální coupling a nesmí se použít k vytvoření absolutní predikce `R_psi`,
pokud není odvozen samostatný vztah k pozorovatelné veličině.

<!-- BILINGUAL-UNIT: rpsi-scale-audit.impact -->
## Dopad na status

**ABSOLUTNÍ MINIMUM `R_psi` ZE ZOBRAZENÉHO LOGARITMICKÉHO JEDNOSMYČKOVÉHO
POTENCIÁLU: CLOSED AS NO-GO [L0].**

**MODULÁRNÍ PEVNÝ POMĚR `R_psi/R_t = 1`:
EXACT [L0].**

**ABSOLUTNÍ SPOLEČNÁ DÉLKOVÁ ŠKÁLA ZE SOUČASNÉHO MODULÁRNÍHO ARGUMENTU:
OPEN.**

Pátokanálová gravitační škála `ell` proto nesmí být označena jako odvozená ze
starého tvrzení o minimu `R_psi`. Jednokonstantní gravitační dokončení musí buď
ponechat jednu skutečnou délkovou/couplingovou konstantu, nebo odvodit
absolutní škálu samostatným mechanismem.

<!-- BILINGUAL-UNIT: rpsi-scale-audit.verification -->
## Ověření

`tools/verify_one_constant_gr_closure.py` symbolicky kontroluje derivaci
zobrazeného potenciálu a derivovanou identitu v pevném bodě. Tvrzení o zamčené
roli `N0` je ukotveno v `canonical/AXIOMS.md` a
`canonical/CANONICAL_DEFINITIONS.md`.
