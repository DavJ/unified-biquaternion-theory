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
spojitou fyzikální vstupní konstantu**. V současném návrhu kanonizace je touto
konstantou gravitační odezvová škála

\[
\boxed{\kappa>0.}
\]

Jde o konstrukční omezení teorie, nikoli o tvrzení, že všechny zbývající
sektory jsou již odvozené.

Zamčená normalizace `N0` je konvence volby jednotek a nepočítá se jako nezávislý
fyzikální coupling. Diskrétní volby jako orientace, signatura a větev
reprezentace nejsou spojité konstanty.

<!-- BILINGUAL-UNIT: one-constant-rule.forbidden -->
## Žádné nezávislé sektorové konstanty

Žádný finalizovaný sektor nesmí zavést další volně fitovaný spojitý
fundamentální parametr. Zejména následující veličiny musí být odvozeny z jediné
UBT akce, z diskrétních algebraických/topologických dat, ze stavu nebo hraniční
podmínky, případně z jediné povolené škály `kappa`:

- gauge couplingy a směšovací parametry;
- hmotnosti a koeficienty typu Yukawa;
- koeficienty potenciálu `Theta`;
- kompaktifikační nebo komplexně-časové délkové škály, pokud jsou fyzikálně
  pozorovatelné;
- efektivní kosmologický/temně-energetický člen;
- normalizační konstanty hmotových, kvantových nebo statistických redukcí.

Lokální gravitační větev fixuje

\[
\boxed{\Lambda_{\rm bare}=0.}
\]

Nenulový efektivní kosmologický člen tedy není druhou fundamentální konstantou.

<!-- BILINGUAL-UNIT: one-constant-rule.units -->
## Rozměrové jednotky nezvyšují počet parametrů

Rozměrová teorie potřebuje konvenci jednotek. Změna jednotek může přesouvat
mocniny `kappa`, `N0`, `c` nebo `hbar` mezi vzorci, aniž by vytvářela novou
nezávislou bezrozměrnou informaci. Počet parametrů se týká nezávislých
fyzikálních vstupů po zafixování konvencí jednotek.

Budoucí formulace proto může jedinou referenční škálu v přirozených jednotkách
položit rovnu jedné a později ji rozměrově obnovit. Taková volba jednotek však
neudělá ze samostatně fitovaného bezrozměrného couplingu odvozenou veličinu.

<!-- BILINGUAL-UNIT: one-constant-rule.falsification -->
## Předem stanovené falzifikační kritérium

Jednokonstantní program UBT selhává, pokud lze fenomenologicky nutný sektor
učinit konzistentním pouze přidáním druhého nezávislého spojitého vstupu, který
nelze odstranit volbou jednotek a nelze odvodit z jediné akce nebo z
diskrétních/stavových dat.

Fit s více nezávislými spojitými konstantami může stále definovat efektivní
model, ale nesmí být prezentován jako finalizovaná jednokonstantní UBT.

<!-- BILINGUAL-UNIT: one-constant-rule.status -->
## Status

```yaml
maximum_independent_continuous_physical_constants: 1
current_constant: kappa
N0: unit_setting_only
Lambda_bare: 0
other_sector_constants: MUST_BE_DERIVED
full_derivation_of_other_sectors: OPEN
```

Merge tohoto dokumentu a párové anglické edice přijímá pravidlo rozpočtu
konstant. Sám o sobě neuzavírá gapy redukce Standardního modelu, kvantového ani
kosmologického sektoru.
