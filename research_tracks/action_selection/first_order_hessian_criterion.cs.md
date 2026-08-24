<!-- BILINGUAL-UNIT: first-order-hessian.provenance -->
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

# Přesné kritérium first-jet Hessiánu pro Eulerovy–Lagrangeovy rovnice prvního řádu

<!-- BILINGUAL-UNIT: first-order-hessian.setup -->
## Nastavení

Nechť `Phi^A` jsou reálné složky pole a lokální Lagrangián závisí pouze na
prvním jetu,

\[
L=L(\Phi,\partial_\mu\Phi).
\]

Definujme jeho Hessián podle rychlostí/prvního jetu

\[
W^{\mu\nu}{}_{AB}
:=\frac{\partial^2L}
{\partial(\partial_\mu\Phi^A)\,\partial(\partial_\nu\Phi^B)}.
\]

Pro hladký skalární Lagrangián dává rovnost smíšených derivací

\[
\boxed{W^{\mu\nu}{}_{AB}=W^{\nu\mu}{}_{BA}.}
\]

<!-- BILINGUAL-UNIT: first-order-hessian.theorem -->
## Věta o hlavním řádu [L0]

Hlavní část Eulerovy–Lagrangeovy rovnice obsahující druhý jet je

\[
- W^{\mu\nu}{}_{AB}\,\partial_\mu\partial_\nu\Phi^B.
\]

Protože druhý jet je symetrický v `mu,nu`, tento člen identicky mizí pro
libovolné druhé jety právě tehdy, když

\[
\boxed{W^{(\mu\nu)}{}_{AB}=0.}
\]

Spojení této podmínky se symetrií Hessiánu při výměně párů dává

\[
\boxed{
W^{\mu\nu}{}_{AB}
=-W^{\nu\mu}{}_{AB}
=-W^{\mu\nu}{}_{BA}.}
\]

Nenulový first-jet Hessián se tedy může vyhnout hlavní části druhého řádu v
Eulerově–Lagrangeově rovnici pouze v dvojitě antisymetrickém sektoru

\[
\boxed{W\in\Lambda^2T\otimes\Lambda^2F.}
\]

Naopak každý Hessián s těmito algebraickými symetriemi anihiluje symetrický
druhý jet na úrovni hlavního řádu.

<!-- BILINGUAL-UNIT: first-order-hessian.standard -->
## Standardní kvadratický kinetický člen je vyloučen

Pro běžný nedegenerovaný kvadratický kinetický tvar

\[
L_{\rm kin}=\frac12g^{\mu\nu}H_{AB}
\partial_\mu\Phi^A\partial_\nu\Phi^B,
\]

se symetrickými `g^{mu nu}` a symetrickým párováním polí `H_AB`,

\[
W^{\mu\nu}{}_{AB}=g^{\mu\nu}H_{AB}
\]

leží v dvojitě symetrickém sektoru, nikoli v
`Lambda^2 T tensor Lambda^2 F`. Proto dává skutečně druhý řád hlavní rovnice,
kdykoli je párování nenulové/nedegenerované, a tím reprodukuje a zpřesňuje
existující obstrukci řádu akce.

<!-- BILINGUAL-UNIT: first-order-hessian.ubt -->
## Důsledek pro UBT-native akci prvního řádu

Degenerovaná akce UBT bez dalších polí schopná dát skutečně rovnice prvního
řádu musí uspořádat **celkový** first-jet Hessián tak, aby se jeho symetrická
část v prostoročasových indexech přesně zrušila. Algebraicky musí každý
zbývající nenulový Hessián být dvojitě antisymetrický podle výše uvedeného
kritéria.

To výrazně omezuje hledání. Úspěšnou akci nelze získat pouhou změnou
koeficientu kanonického symetrického kvadratického párování. Musí použít
multisymplektickou/Wessovu–Zuminovu antisymetrickou strukturu, null Lagrangian
s netriviálními členy nižšího řádu nebo jiný mechanismus, jehož úplný Hessián
splňuje stejné kritérium rušení.

U zkušební kompozitní generalizované Diracovy hustoty skutečnost
`Gamma=Gamma(DTheta)` znamená, že je nutné spočítat celý Hessián včetně
řetězových příspěvků. Označení výrazu jako „Dirac-like“ požadovanou dvojitou
antisymetrii nedokazuje.

<!-- BILINGUAL-UNIT: first-order-hessian.verification -->
## Ověření

`tools/verify_first_order_hessian_criterion.py` sestavuje exaktní symbolické
Hessiány se symetrií při výměně párů, kontroluje, že s formálním symetrickým
druhým jetem se kontrahuje pouze symetrická část v `mu,nu`, a ověřuje
indukovanou antisymetrii v indexech polí, když tato část mizí. Párový pytest
udržuje konečněrozměrnou identitu v CI.

Věta je konečná algebra. Formalizace v Leanu je vysoce prioritní
`LEAN-PENDING` cíl, protože nezávisí na nevyřešených fyzikálních premisách.

<!-- BILINGUAL-UNIT: first-order-hessian.status -->
## Dopad na status

**FIRST-ORDER VARIATIONAL CANCELLATION CRITERION: CLOSED [L0].**

**UBT DEGENERATE FIRST-ORDER ACTION: STILL OPEN, NOW RESTRICTED TO THE
DOUBLE-ANTISYMMETRIC/MULTISYMPLECTIC PRINCIPAL SECTOR.**
