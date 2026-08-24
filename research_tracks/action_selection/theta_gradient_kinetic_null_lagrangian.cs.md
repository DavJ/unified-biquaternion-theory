<!-- BILINGUAL-UNIT: gradient-null.provenance -->
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

# Čistě gradientový metric-lock kinetický člen je null Lagrangian

<!-- BILINGUAL-UNIT: gradient-null.scope -->
## Rozsah

Tato poznámka testuje nejjednodušší Lorentzovsky reálnou větev současně
deklarované kvadratické kinetické rodiny. Nechť

\[
E_\mu{}^a=\mathcal N_0^{-1/2}\partial_\mu X^a,
\qquad
g_{\mu\nu}=E_\mu{}^aE_\nu{}^b\eta_{ab},
\]

na nedegenerovaném patchi s pevnou orientací. Tento test neobsahuje žádný člen
konexe ani torze. Výsledek je proto exaktní obstrukcí konkrétní větve, nikoli
větou o každém možném kovariantním dokončení.

<!-- BILINGUAL-UNIT: gradient-null.collapse -->
## Kolaps metric-locku

Kanonická sharp/Minkowského kontrakce splňuje již dokázanou identitu

\[
g^{\mu\nu}\langle D_\mu\Theta,D_\nu\Theta\rangle_\sharp=4\mathcal N_0.
\]

Kvadratická kinetická akce je tedy na této větvi úměrná

\[
S_{\rm kin}=2\mathcal N_0\int d^4x\sqrt{-g}.
\]

Protože `g=E eta E^T` a `det eta=-1`,

\[
\sqrt{-g}=|\det E|
=\mathcal N_0^{-2}|\det(\partial_\mu X^a)|.
\]

Na patchi s pevnou orientací je absolutní hodnota pouze pevným celkovým
znaménkem, takže lokální variační problém je determinant Jacobiánu.

<!-- BILINGUAL-UNIT: gradient-null.theorem -->
## Věta o null Lagrangian [L0]

Pišme `J_mu^a=partial_mu X^a`. Ve čtyřech rozměrech

\[
\det J
=\frac1{4!}\epsilon^{\mu\nu\rho\sigma}\epsilon_{abcd}
 J_\mu{}^aJ_\nu{}^bJ_\rho{}^cJ_\sigma{}^d.
\]

Jeho derivace podle `J_mu^a` je kofaktor,

\[
\frac{\partial\det J}{\partial J_\mu{}^a}
=\frac1{3!}\epsilon^{\mu\nu\rho\sigma}\epsilon_{abcd}
 J_\nu{}^bJ_\rho{}^cJ_\sigma{}^d.
\]

Eulerova–Lagrangeova rovnice je tedy

\[
\partial_\mu\left(\frac{\partial\det J}{\partial J_\mu{}^a}\right)=0.
\]

Každý diferencovaný člen obsahuje Hessián
`partial_mu partial_nu X^b`, symetrický v `mu,nu`, kontrahovaný s
antisymetrickým tenzorem epsilon prostoročasu. Členy se po dvojicích ruší.
Proto

\[
\boxed{\frac{\delta}{\delta X^a}\int d^4x\det(\partial X)=0}
\]

identicky v objemu. Ekvivalentně kofaktor gradientu splňuje Piolovu identitu

\[
\partial_\mu\operatorname{Cof}(\partial X)_\mu{}^a=0.
\]

Metric-lockovaný kvadratický kinetický člen tedy na této čistě gradientové
větvi neposkytuje žádnou lokální objemovou rovnici pole.

<!-- BILINGUAL-UNIT: gradient-null.hessian -->
## Důsledek pro Hessián

Protože první variace je hraniční člen, objemový kvadratický operátor fluktuací
je na této větvi variačně degenerovaný. Ze samotného zobrazeného kvadratického
kanonického kinetického členu jej proto na této větvi nelze identifikovat s
předpokládanou nedegenerovanou kolekcí bosonických operátorů Laplaceova typu.

Toto nevyvrací indukovanou gravitaci z **jiné finalizované kovariantní akce
Theta**. Ukazuje však, že Hessián Laplaceova typu použitý v existujícím
podmíněném vzorci indukované gravitace není odvozen pouhým doslovným použitím
metric-lockovaného čistě gradientového kvadratického kinetického členu.

<!-- BILINGUAL-UNIT: gradient-null.verification -->
## Ověření

`tools/verify_gradient_null_lagrangian.py` provádí exaktní symbolickou
čtyřrozměrnou kontrolu Piolovy identity kontrakcí symetrického formálního
Hessiánu s antisymetrickými Levi-Civitovými tenzory. Odpovídající pytest drží
toto rušení v CI.

Výše uvedený důkaz pomocí epsilon tenzorů je exaktní. Formalizace Piolovy
identity v této notaci UBT v Leanu je `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: gradient-null.status -->
## Dopad na status

**PURE-GRADIENT QUADRATIC KINETIC SELECTOR: CLOSED AS NO-GO [L0].**

Současný kvadratický metric-lock člen nelze použít jako chybějící
mikroskopický propagující Hessián na čistě gradientové větvi. Úspěšné dokončení
jediné akce musí získat svůj nedegenerovaný fluktuační operátor z další
kovariantní derivační/konexní struktury, členu vyššího jetu nebo jiného
explicitně vybraného mechanismu. Obnova GR zůstává `CLOSED_CONDITIONALLY`,
dokud nebude tato struktura odvozena.
