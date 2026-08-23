<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Matice statusů tvrzení UBT

Povolené statusy:

- **PROVED**
- **DERIVED_WITH_ASSUMPTIONS**
- **NUMERICAL_EVIDENCE**
- **CONJECTURE**
- **OPEN_GAP**
- **SPECULATIVE**

Definice se řídí dokumentem [`docs/UBT_SCOPE_AND_CLAIM_LEVELS.md`](docs/UBT_SCOPE_AND_CLAIM_LEVELS.md).

---

## Kanonická / výzkumná tvrzení

| Tvrzení | Status | Primární zdroj | Poznámky |
|---|---|---|---|
| Kinematika GR s kovariantní tetrádou a **podmíněná efektivní obnova GR** | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gr_recovery_completion.cs.tex`, `canonical/gr_closure/gr_recovery_status.yaml`, `canonical/gr_closure/gap_10_gr_effective_completion.tex`, `canonical/gr_closure/gap_10t_split_jet_right_inverse.tex`, `canonical/gr_closure/gap_10t_split_jet_auxiliary_completion.tex`, `canonical/gr_closure/gap_10d_induced_gravity_endgame.tex`, `papers/UBT_GR_Submission.tex` | **Obnova GR je CLOSED CONDITIONALLY** na lokální čtyřrozměrné infračervené efektivní úrovni. Centrální metrika bez projekce a hodnost 10 jsou dokázány; fyzická konexe je v obnovené větvi Levi–Civitova; pomocné split-jet proměnné jsou algebraické/nepropagující a na slupce mizí z metrických/spinových rovnic; a předpokládaná/indukovaná dvouderivační efektivní akce dává Einsteinovu–Lambda dynamiku. Každá hladká lokální Einsteinova tetráda má split-jet reprezentanta, takže Schwarzschild včetně lapse je obnoven bez použití neplatného historického přímého ansatzu pro Theta. Linearizace této obnovené větve dává standardní Regge–Wheelerův/Zerilliho sektor. Toto **netvrdí** bezpodmínečné mikroskopické odvození z jediného Theta, predikci Newtonovy konstanty, UV stabilitu psi ani globální dokončení přes nulové patche; to jsou silnější neblokující fundamentální/UV výzkumné otázky. `gr_chain` proto zůstává `DERIVED_WITH_ASSUMPTIONS`, nikoli `PROVED`. |
| Kanonická generalizovaná Diracova omezená hodnost metriky bez dalších polí | DERIVED_WITH_ASSUMPTIONS | `canonical/geometry/biquaternion_dirac_lift.tex`, `research_tracks/canonical_relation_generalized_dirac/no_extra_variable_rank_theorem.tex`, `tools/verify_no_extra_variable_rank.py` | Přesná věta: `rank(Dg|A)=dim(A+K)-6`; plná hodnost právě tehdy, když `A+K=R^16`. Invertibilní `F_Psi` zachovává bodovou hodnost first-jet mapy deset pouze s hodnotou původního `Theta`; nenulové skalární nebo skalárně-pseudoskalární členy nultého řádu postačují. Jejich odvození z kanonické akce a lokální existence PDE zůstávají otevřené. Osm nezávislých reálných omezení působících pouze na tetrádu implikuje hodnost nejvýše osm. |
| Split-jet pomocná akce a nepropagace | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gap_10t_split_jet_auxiliary_completion.tex`, `tools/verify_gr_endgame_completion.py` | `GAP-10T-JET-AUX: CLOSED [L1]`; `GAP-10T-JET-CONSTRAINT-SELECTION: CLOSED AS NO-GO [L1]`; `GAP-10T-JET-DYN: CLOSED CONDITIONALLY FOR GR RECOVERY`, zatímco mikroskopický původ efektivního selektoru a globální/mírové dokončení zůstávají otevřené. |
| Indukovaný Einsteinův koeficient z Hessiánu Theta | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gap_10d_induced_gravity_endgame.tex`, `canonical/gr_closure/gap_10_gr_effective_completion.tex`, `tools/verify_gr_endgame_completion.py` | `GAP-10D-UNDERDETERMINATION: CLOSED AS NO-GO [L1]`; `GAP-10D-A2-FORM` a `GAP-10D-SPECTRAL-IR`: CLOSED CONDITIONALLY [L1]. Pro obnovu GR postačuje konečný kladný renormalizovaný Einsteinův koeficient, takže `GAP-10D` je **CLOSED CONDITIONALLY FOR GR RECOVERY**. Kompozitní Hessián, počet fyzických módů, neminimální vazba, identifikace cutoffu a omezená míra zůstávají otevřené pro prvoprincipovou numerickou predikci `G`, nikoli pro podmíněnou obnovu GR. |
| Schwarzschildovo řešení ve větvi UBT GR | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/gr_recovery_completion.cs.tex`, `canonical/geometry/schwarzschild_claim_status.yaml`, `papers/UBT_GR_Submission_canonical_correction.cs.tex` | `GAP-U2Theta: CLOSED CONDITIONALLY FOR GR RECOVERY`. Úplná Schwarzschildova tetráda/lapse je obnovena jako vakuové Einsteinovo řešení a lokálně zvednuta split-jet pravou inverzí s pomocnými proměnnými, které se na slupce odpojí. Starší přímý ansatz v `biquaternionic_vacuum_solutions.tex` je explicitně neplatný jako kanonické odvození a zůstává nahrazen. Mikroskopický přímý výběr větve a globální pokračování přes horizont zůstávají otevřenými fundamentálními otázkami. |
| Obnova Regge–Wheelerovy rovnice pro graviton s lichou paritou | DERIVED_WITH_ASSUMPTIONS | `papers/UBT_GR_Submission.tex`, `canonical/gr_closure/gr_recovery_completion.cs.tex`, `canonical/gr_closure/` | `GAP-B-MASTER: CLOSED CONDITIONALLY FOR EFFECTIVE GR PERTURBATIONS`: linearizace obnovené Einsteinovy větve dává standardní linearizovaný Einsteinův systém, a tedy Regge–Wheelerovu redukci. Přímé odvození z mikroskopické master rovnice UBT zůstává silnějším neblokujícím problémem fundamentálního dokončení. |
| Obnova Zerilliho rovnice pro graviton se sudou paritou | DERIVED_WITH_ASSUMPTIONS | `canonical/gr_closure/zerilli_derivation.tex`, `canonical/gr_closure/gr_recovery_completion.cs.tex` | Standardní redukce sudé parity plyne ze stejné podmíněně obnovené Einsteinovy větve; přímé odvození z mikroskopické master rovnice zůstává otevřené jako silnější neblokující otázka. |
| Trasa obnovy gauge struktury Standardního modelu (strukturální řetězec SU(3)×SU(2)×U(1)) | DERIVED_WITH_ASSUMPTIONS | `canonical/interactions/`, `canonical/su3_derivation/`, `papers/UBT_Gauge_Submission.tex` | Formální řetězec je přítomen; zbývající sektorové uzávěry jsou explicitní. |
| Status one-hot chyb triqubitu | DERIVED_WITH_ASSUMPTIONS | `canonical/interactions/gap_su3_triqubit_qec.tex`, `tools/verify_triqubit_qec_status.py` | `GAP-SU3-TRIQUBIT-LEAKAGE: CLOSED [L1]`: každá jednotlivá chyba `X_i`/`Y_i` opustí barevný sektor. `GAP-SU3-TRIQUBIT-QEC: CLOSED AS NO-GO [L1]`: obecné chyby `Z_i` jsou nedetekované logické fáze a Knill--Laflammeovy podmínky selžou pro opravu neznámé jednotlivé chyby `X_i`. To je užitečné pro omezený registr kvantové simulace a neimplikuje ontologii simulace. |
| Hypernáboj $Y_Q=1/6$ z topologie | L1_FAMILY_CHECK | `canonical/interactions/colour_charge_lattice.tex` | Jedinečný v rodině $Y=n/6$ přes gravitační anomálii $\mathcal{A}_{\rm grav}(n)=n-1=0$ pouze pro $n=1$. Úplná jednoznačnost mimo tuto rodinu zůstává OPEN. |
| Strukturální cesta tří generací z rámce ψ-winding | DERIVED_WITH_ASSUMPTIONS | `canonical/n_eff/`, `canonical/interactions/` | Mechanismus je zdokumentován s explicitními předpoklady. |
| Úplné uzavření α z prvních principů (včetně odvození blockerů) | OPEN_GAP | `canonical/alpha/ALPHA_MASTER_STATUS.md`, `research_tracks/T3_ALPHA/mellin_insertion_B.tex` | Otestováno 5 cest, všechny NO-GO. $B_{\rm phenom}$ [OBS 0.0066%]. Alpha NOT DERIVED. |
| Podpora trasy α související s N_eff | DERIVED_WITH_ASSUMPTIONS | `canonical/n_eff/` | Nesmí být nadhodnocena jako úplný důkaz α. |
| Trasy numerické reprodukovatelnosti (diagnostika/validace) | NUMERICAL_EVIDENCE | `research_tracks/`, `tools/`, `experiments/` | Reprodukovatelné důkazy/evidence, nikoli důkaz na úrovni věty. |
| Úplné uzavření kvantové teorie pole UBT (Hilbert/Born/měření/path-integral úplnost) | OPEN_GAP | `src/ubt/quantum/`, `docs/quantum_sector_status.md` | Numerický scaffold existuje; řetězec odvození zůstává otevřený. |
| Bornovo pravidlo odvozené z UBT | OPEN_GAP | `src/ubt/quantum/quantum_scaffold.py`, `docs/quantum_sector_status.md` | Pouze placeholder. |
| Míra path-integralu v bikvaternionových souřadnicích | OPEN_GAP | `src/ubt/quantum/quantum_scaffold.py`, `docs/quantum_sector_status.md` | `NotDerivedPathIntegralKernel` je explicitní placeholder. |
| Regularizace solitonu s konečnou energií | NUMERICAL_EVIDENCE | `src/ubt/solitons/regularization.py`, `research_tracks/renormalization/finite_energy_soliton_regularization.md` | Regularizovaný model s konečnou energií; úplné RG odvození zůstává otevřené. |
| Renormalizační grupa z akce UBT | OPEN_GAP | `research_tracks/renormalization/finite_energy_soliton_regularization.md` | Není tvrzeno odvození RG toku. |
| UBT odvozuje porušení parity slabé interakce | CONJECTURE | `src/ubt/algebra/chirality.py`, `research_tracks/weak_sector/chirality_and_parity_status.md` | Pouze algebraický scaffold chirality; bez odvození vazby SU(2)_L. |
| Predikce anomálního magnetického momentu z UBT | OPEN_GAP | `src/ubt/observables/physics_observable_bridge.py`, `docs/observable_bridge.md` | Bridge vrací strukturovaný status otevřeného gapu. |

---

## Explicitně spekulativní tvrzení (nekanonická)

Pokud je reprodukovatelný empirický protokol neposune výše, následující zůstávají **SPECULATIVE**:

| Tvrzení | Status | Umístění |
|---|---|---|
| pole vědomí | SPECULATIVE | `speculative_extensions/consciousness/` |
| psychony jako fyzické částice | SPECULATIVE | `speculative_extensions/consciousness/` |
| posmrtný život | SPECULATIVE | `speculative_extensions/` |
| přežití vědomí | SPECULATIVE | `speculative_extensions/` |
| komunikace se zemřelým vědomím | SPECULATIVE | `speculative_extensions/` |
| ThetaComm | SPECULATIVE | `speculative_extensions/thetacomm/` |
| Program bikvaternionové metric-null / volume-null neviditelnosti | SPECULATIVE | `speculative_extensions/invisibility/` |
| duše / nesmrtelnost | SPECULATIVE | `speculative_extensions/` |
| Matrix / ontologie simulace | SPECULATIVE | `speculative_extensions/metaphysics/` (nebo ekvivalentní spekulativní cesta) |
