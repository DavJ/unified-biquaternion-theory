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

# Patch notes: adelický restart prvočíselného rozkladu

**Datum:** 2026-08-28  
**Rozsah:** aktivní výzkumná větev RH; beze změn kanonických tvrzení.

<a id="apd-patch-summary"></a>
## Shrnutí

Tento patch realizuje první rozhodovací experiment adelického restartu. Nepřidává další theta--Mellinův kanál. Místo toho audituje a propojuje existující větve prime-Fockova prostoru, racionálních revivalů a theta--Mellinovy transformace.

Omezený tenzorový součin radiálních prvočíselných prostorů je unitárně ekvivalentní (ell^2(\mathbb N)), přičemž

\[
H_{\log}|n\rangle=(\log n)|n\rangle.
\]

Jeho uzávěr je kladný samoadjungovaný operátor násobení, takže dřívější prime-Fockova mezera samoadjungovanosti F5 je na úrovni klasického operátoru uzavřena. Jeho tepelná stopa zůstává standardní Eulerovou identitou

\[
\operatorname{Tr}(e^{-sH_{\log}})=\zeta(s),
\qquad \Re s>1.
\]

Lokální oscilátor je přesně ztotožněn s radiálním nerozvětveným Tateovým integrálem

\[
\operatorname{Tr}(p^{-sN_p})
=\int_{\mathbb Q_p^\times}\mathbf1_{\mathbb Z_p}(x)|x|_p^s\,d^\times x
=\frac1{1-p^{-s}}.
\]

Tím se opravuje také interpretace práce s charaktery modulo (5): jde o konečný kvocient sektoru jednotek v místě (p=5), zatímco prime-Fockův oscilátor zachycuje pouze valuační sektor.

Archimédovský audit opravuje strukturální směšování. Theta--Mellinův integrál dává dokončený kanál

\[
\frac12\int_0^\infty(\vartheta(t)-1)t^{s/2}\frac{dt}{t}
=\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Nezávislý součin tepelných stop (artheta(t)^d\zeta(t)) proto není dokončenou funkcí zeta a nelze jej použít jako mechanismus její funkcionální rovnice.

Pro každý jmenovatel (q) faktorizují CRT idempotenty racionální kvadratický revivalový operátor přes maximální bloky prvočíselných mocnin (p^{v_p(q)}). Odpovídající faktorizace Gaussova součtu je exaktní. Druhý elementární výsledek zpřesňuje podmínku necirkularity: každý výstup uvádějící tyto maximální prvočíselné mocniny už obsahuje faktorizaci (q). Smysluplnou otázkou UBT je tedy dynamický původ racionálních/profinitních lokálních sektorů, nikoli algoritmus skrývající celočíselnou faktorizaci.

<a id="apd-patch-claim-control"></a>
## Kontrola tvrzení

Patch dokazuje standardní aritmetické a operátorové identity. Neodvozuje racionální jmenovatele, lokální místa označená prvočísly, charaktery jednotek, energie (log p) ani fermionové gradování z kanonické akce UBT. Dává zeta jako partiční funkci, nikoli nuly zeta jako samoadjungované spektrum, a neimplikuje RH.

<a id="apd-patch-verification"></a>
## Ověření

- `tools/verify_adelic_prime_decomposition.py` kontroluje rekonstrukci valuací, lokální a konečné tenzorové stopy, useknutí jádra v grafové normě, CRT idempotenty a bijekce, faktorizaci revivalových fází a Gaussových součtů, archimédovskou Mellinovu normalizaci v (s=2) a podmínku faktorizujícího výstupu.
- `tests/test_adelic_prime_decomposition.py` poskytuje osm regresních testů.
- Ověřovač používá pouze prostředky standardní knihovny Pythonu (3.12).
- Lean není v aktuálním běhovém prostředí dostupný; status je `LEAN-PENDING` a netvrdí se žádné formální ověření.
- Zdrojem překladu byla anglická verze. Párová česká verze má shodné kotvy, rovnice, statusové značky, tabulky, citace a výhrady; před sloučením je stále nutná lidská kontrola významové shody.

<a id="apd-patch-next"></a>
## Další podmínka

Následující experiment musí rozšířit radiální místo o lokální sektor jednotek (mathbb Z_p^\times), ztotožnit existující kanály modulo (5) s kvocientem (mathbb Z_5^\times/(1+5\mathbb Z_5)) a otestovat inverzní systém přes (5^k). Pokud tím vznikne pouze standardní Tateova faktorizace bez operátoru nebo kladného stopového párování odvozeného z UBT, zůstane cesta klasickým adelickým přebalením.

