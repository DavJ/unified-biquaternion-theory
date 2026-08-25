<!-- BILINGUAL-UNIT: one-constant-rule.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->

# Pravidlo jediné konstanty UBT

<!-- BILINGUAL-UNIT: one-constant-rule.rule -->
## Závazné pravidlo ekonomie po přijetí

Dokončená Unified Biquaternion Theory smí mít **nejvýše jednu nezávislou
spojitou fyzikální vstupní vazbu**. V současném návrhu kanonizace je touto
vazbou gravitační odezvová škála

\[
\boxed{\kappa>0.}
\]

Jde o konstrukční omezení teorie, nikoli o tvrzení, že všechny zbývající
sektory jsou již odvozené.

Zamčená normalizace `N0` je konvence volby jednotek a nepočítá se jako nezávislý
fyzikální coupling. Diskrétní volby jako orientace, signatura a větev
reprezentace nejsou spojité konstanty.

Od vazeb akce se odlišují také parametry řešení a integrační konstanty. Hmotnost,
moment hybnosti nebo kosmologická integrační konstanta mohou označovat klasické
řešení, aniž by se staly druhou fundamentální konstantou teorie.

<!-- BILINGUAL-UNIT: one-constant-rule.forbidden -->
## Žádné nezávislé sektorové vazby

Žádný finalizovaný sektor nesmí zavést další volně fitovanou spojitou
fundamentální vazbu. Zejména následující veličiny musí být odvozeny z jediné UBT
akce, z diskrétních algebraických/topologických dat, ze stavu nebo hraniční
podmínky, případně z jediné povolené škály `kappa`:

- gauge couplingy a směšovací parametry;
- hmotnosti a koeficienty typu Yukawa;
- koeficienty potenciálu `Theta`;
- kompaktifikační nebo komplexně-časové délkové škály, pokud jsou fyzikálně
  pozorovatelné;
- normalizační konstanty hmotových, kvantových nebo statistických redukcí.

Lokální gravitační větev **nepokládá kosmologickou konstantu za nulu**. Místo
toho z unimodulárních pomocných rovnic plyne

\[
\boxed{d\Lambda=0,\qquad\Lambda=\Lambda_0}
\]

a `Lambda_0` je integrační konstanta, nikoli druhá vazba akce. Pozdější
kosmologická teorie se může pokusit předpovědět její pozorovanou hodnotu z
globálních/stavových/topologických dat.

<!-- BILINGUAL-UNIT: one-constant-rule.units -->
## Rozměrové jednotky nezvyšují počet parametrů

Rozměrová teorie potřebuje konvenci jednotek. Změna jednotek může přesouvat
mocniny `kappa`, `N0`, `c` nebo `hbar` mezi vzorci, aniž by vytvářela novou
nezávislou bezrozměrnou informaci. Počet parametrů se týká nezávislých
fyzikálních vstupů v akci po zafixování konvencí jednotek.

<!-- BILINGUAL-UNIT: one-constant-rule.falsification -->
## Předem stanovené falzifikační kritérium

Jednokonstantní program UBT selhává, pokud lze fenomenologicky nutný sektor
učinit konzistentním pouze přidáním druhé nezávislé spojité vazby akce, kterou
nelze odstranit volbou jednotek a nelze odvodit z jediné akce nebo z
diskrétních/stavových dat.

Libovolně fitovaný člen `Lambda` vložený přímo do akce by toto pravidlo porušil.
Integrační konstanta vybraná rovnicemi pole a hraničními nebo stavovými daty jej
neporušuje.

<!-- BILINGUAL-UNIT: one-constant-rule.status -->
## Status

```yaml
maximum_independent_continuous_action_couplings: 1
current_constant: kappa
N0: unit_setting_only
Lambda: INTEGRATION_CONSTANT_NOT_ACTION_COUPLING
other_sector_couplings: MUST_BE_DERIVED
full_derivation_of_other_sectors: OPEN
```

Merge tohoto dokumentu a párové anglické edice přijímá pravidlo rozpočtu
konstant. Sám o sobě neuzavírá gapy Standardního modelu, kvantového ani
numerického kosmologického výběru.
