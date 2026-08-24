<!-- BILINGUAL-UNIT: first-jet-gravity.provenance -->
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

# No-go pro čistě gravitační UBT selektor z prvního jetu

<!-- BILINGUAL-UNIT: first-jet-gravity.scope -->
## Rozsah

Nechť nedegenerovaný Lorentzovsky reálný první jet jediného pole definuje
fyzickou tetrádu a metriku,

\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,
\qquad
g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab}.
\]

Uvažujme **čistě gravitační** lokální hustotu akce, která je algebraicky
sestavena z `E` (ekvivalentně `g`) v jednom bodě, je invariantní vůči lokálním
Lorentzovým změnám rámce a změnám souřadnic prostoročasu, neobsahuje pevný
pozadový tensor a neobsahuje derivaci `E` ani `g`. Explicitní invarianty hodnoty
`Theta`, například potenciál, jsou z této věty vyloučeny; byly klasifikovány
samostatně a chovají se jako hmotové/potenciálové členy.

<!-- BILINGUAL-UNIT: first-jet-gravity.orbit -->
## Věta o bodové orbitě [L0]

Všechny nedegenerované Lorentzovy metriky pevné signatury v jednom bodě tvoří
jedinou kongruenční orbitu `GL(4,R)`. Jestliže

\[
g_1=e_1\eta e_1^T,
\qquad
g_2=e_2\eta e_2^T,
\]

pak pro `A=e_2 e_1^{-1}` platí

\[
\boxed{g_2=A g_1 A^T.}
\]

Skalární funkce pouze metriky, která je přirozená vůči všem změnám souřadnic,
proto nabývá stejné hodnoty na každé nedegenerované Lorentzově metrice: na této
orbitě je konstantní. Lokální Lorentzova invariance odstraní volbu zástupce
tetrády uvnitř každé metriky.

Nejobecnější čistě gravitační hustota nezávislá na hodnotě pole a nultého
řádu v derivacích `g` je tedy

\[
\boxed{\mathcal L_{\rm grav}^{(0)}=c_0\sqrt{-g}.}
\]

Je to pouze kosmologický objemový člen. Tím se zobecňuje dříve dokázaný kolaps
přímého kvadratického kompozitního skaláru prvního jetu na
`4 N0 sqrt(-g)`.

<!-- BILINGUAL-UNIT: first-jet-gravity.order -->
## Důsledek pro diferenciální řád [L0]

Algebraická metrická hustota neobsahuje křivost a její nezávislá variace podle
metriky je algebraická v `g`. Nemůže tedy vytvořit Einsteinův tensor

\[
G_{\mu\nu}=R_{\mu\nu}-\frac12Rg_{\mu\nu},
\]

který před obvyklým rušením hraničních členů obsahuje druhé derivace metriky.
V kompozitním popisu `g=g(D Theta)` může funkcionál prvního jetu samozřejmě dát
Eulerovy–Lagrangeovy rovnice druhého řádu pro `Theta`; tato skutečnost **nemění**
jeho algebraickou závislost na metrice na Einsteinův operátor křivosti. Již
dokázaný výsledek o řádu kvadratické akce je s tímto rozlišením konzistentní.

Bezpodmínečné mikroskopické odvození GR proto nelze získat hledáním dalšího
čistě gravitačního skaláru nezávislého na hodnotě pole, sestaveného pouze ze
stejného prvního jetu `D Theta`.

<!-- BILINGUAL-UNIT: first-jet-gravity.routes -->
## Zbývající cesty

V programu jediné akce UBT musí nastat alespoň jedna z následujících možností:

1. lokální invariant vyššího jetu, jehož redukce obsahuje skalár křivosti
   (druhé derivace `Theta` jsou v přímém kompozitním popisu nevyhnutelné);
2. formulace prvního řádu s nezávisle variovanou, ale nakonec omezenou nebo
   kompozitní konexí, spolu s důkazem, že nebylo zavedeno nové fyzické
   propagující pole;
3. kvantová/funkcionální integrace finalizované dynamiky `Theta`, která
   indukuje Einsteinův–Hilbertův člen a určí požadovaný Hessián, míru a obsah
   fyzických módů.

První a druhá možnost jsou přímé mikroskopické selektorové cesty; třetí je
cesta indukované gravitace. Pouhá změna párování prvního jetu nebo ladění
bezderivačního potenciálu již není přípustným nevyřešeným mechanismem.

<!-- BILINGUAL-UNIT: first-jet-gravity.verification -->
## Ověření

`tools/verify_first_jet_gravity_orbit.py` ověřuje kongruenční identitu nad
přesnými racionálními nedegenerovanými tetrádami a kontroluje, že determinantové
hustoty se transformují s očekávaným čtvercem Jacobiánu. Samotnou větou je
bodový argument tranzitivity uvedený výše; skript je nezávislá přesná regresní
kontrola, nikoli její důkaz.

Formalizace úplného tvrzení o Lorentzovské orbitě `GL(4,R)` v Leanu je
`LEAN-PENDING`. Dokončení v Leanu zde není tvrzeno.

<!-- BILINGUAL-UNIT: first-jet-gravity.status -->
## Dopad na status

**FIRST-JET PURE-GRAVITY SELECTOR: CLOSED AS NO-GO [L0].**

Tím se zužuje `UBT-FUND-GR-ACTION`: chybějící selektor je nyní nutné hledat v
mechanismu vyššího jetu/křivosti, omezené formulaci prvního řádu nebo skutečně
indukovaném efektivním mechanismu. Tato věta sama mezi těmito mechanismy
nevybírá a proto nepovyšuje obnovu GR z `CLOSED_CONDITIONALLY`.
