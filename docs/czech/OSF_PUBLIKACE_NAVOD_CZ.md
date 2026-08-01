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

# Návod na publikaci UBT na OSF (Open Science Framework) - česky

## Co je OSF?

Open Science Framework (OSF) je platforma pro správu vědeckých projektů a publikaci preprintů provozovaná Center for Open Science. OSF nabízí:
- Předtiskovou službu (preprint server) pro rychlé sdílení výzkumu
- Projektové repozitáře s verzováním
- DOI pro každou publikaci
- Integrace s dalšími platformami (GitHub, Zenodo, Figshare)
- Spolupráce a sdílení s kolegy

## Rozdíl mezi OSF a Zenodo

| Funkce | OSF | Zenodo |
|--------|-----|--------|
| **Typ platformy** | Projektová + preprinty | Archivní repozitář |
| **Hlavní účel** | Aktivní výzkumné projekty | Dlouhodobá archivace |
| **Preprinty** | ✅ Ano, hlavní funkce | ❌ Ne (technické záznamy) |
| **Recenze** | ✅ Moderace preprintů | ❌ Ne |
| **GitHub integrace** | ✅ Ano | ✅ Ano (silnější) |
| **DOI** | ✅ Ano (CrossRef) | ✅ Ano (DataCite) |
| **Doporučení pro UBT** | Preprinty, diskuse | Archivace, citace |

**Doporučení**: Publikujte na **OBOU** platformách:
- **OSF**: Pro preprint článku, aktivní diskusi, recenze
- **Zenodo**: Pro archivaci celého repozitáře, oficiální citace

## Příprava před publikací

### 1. Registrace na OSF
1. Jděte na https://osf.io/
2. Klikněte na "Sign Up"
3. Vytvořte účet (můžete propojit s ORCID)
4. Ověřte email

### 2. Příprava dokumentů
Pro OSF preprint doporučuji připravit:
- **Hlavní dokument**: `UBT_Main.pdf` nebo `UBT_Abstract_OSF.pdf`
- **Doplňkové materiály**: Appendixy, kódy, data (jako projektové soubory)

### 3. Metadata k přípravě
- **Název**: Unified Biquaternion Theory: Complex Time, Consciousness, and Field Unification
- **Autor**: Ing. David Jaroš
- **Email**: jdavid.cz@gmail.com
- **Obor**: Physical Sciences and Mathematics → Physics → Theoretical Physics
- **Licence**: CC BY 4.0
- **Klíčová slova**: Stejná jako pro Zenodo (viz ZENODO_PUBLIKACE_NAVOD_CZ.md)

## Možnost A: OSF Preprint (doporučeno pro rychlou publikaci)

### Krok 1: Výběr preprint serveru
OSF má více specializovaných preprint serverů:
- **PhysArXiv** - pro fyziku (doporučeno pro UBT)
- **OSF Preprints** - obecný server
- **SocArXiv**, **PsyArXiv**, atd. - jiné obory

**Pro UBT doporučuji: PhysArXiv** (https://osf.io/preprints/physarxiv)

### Krok 2: Nahrání preprintu na PhysArXiv
1. Jděte na https://osf.io/preprints/physarxiv
2. Klikněte na "Submit a Preprint"
3. Přihlaste se svým OSF účtem

### Krok 3: Výběr souboru
1. Nahrajte hlavní PDF dokument:
   - `UBT_Main.pdf` (pokud chcete publikovat celou teorii), nebo
   - `UBT_Abstract_OSF.pdf` (pokud chcete publikovat jen abstrakt/overview)
2. OSF automaticky extrahuje základní metadata (název, autory)

### Krok 4: Základní informace
- **Title**: 
  ```
  Unified Biquaternion Theory: Complex Time, Consciousness, and Field Unification
  ```

- **Authors**: 
  - Name: David Jaroš
  - Affiliation: (vaše instituce, nebo "Independent Researcher")
  - ORCID: (pokud máte)

### Krok 5: Abstrakt
Vložte abstrakt z dokumentu `UBT_Abstract_OSF.tex`:
```
The Unified Biquaternion Theory (UBT) presents a comprehensive framework for unifying General Relativity, Quantum Field Theory, and Standard Model symmetries within a single mathematical structure based on biquaternionic fields over complex time τ = t + iψ...

Key Features:
- General Relativity Compatibility: UBT generalizes Einstein's General Relativity...
- Geometric Gauge Unification: The Standard Model gauge group SU(3)×SU(2)×U(1)...
[celý abstrakt]
```

### Krok 6: Disciplína a kategorie
1. **Primary subject**: Physical Sciences and Mathematics
2. **Secondary subject**: Physics
3. **Tertiary subject**: Theoretical Physics
4. Můžete přidat další relevantní kategorie:
   - Mathematical Physics
   - Quantum Physics
   - Relativity and Gravitation

### Krok 7: Klíčová slova (Tags)
Přidejte:
```
biquaternion algebra, complex time, unified field theory, General Relativity, quantum field theory, Standard Model, gauge unification, Hermitian gravity, SU(3) symmetry, theta functions, dark matter, dark energy, fermion masses, consciousness theory
```

### Krok 8: Licence
Vyberte: **CC-By Attribution 4.0 International**

### Krok 9: Konflikt zájmů a financování
- **Conflict of Interest**: None
- **Funding**: (pokud nemáte financování, nechte prázdné nebo napište "Self-funded")

### Krok 10: Doplňkové soubory (volitelné)
Můžete přidat:
- Appendixy jako samostatné PDF
- Zdrojový kód (LaTeX soubory)
- Data nebo skripty

### Krok 11: Připojení OSF projektu (volitelné)
Pokud chcete vytvořit plnohodnotný projekt:
1. Vytvořte nejprve OSF projekt (viz Možnost B níže)
2. Připojte preprint k projektu

### Krok 12: Odeslání k moderaci
1. Zkontrolujte všechna pole
2. Klikněte na "Submit for moderation"
3. PhysArXiv moderátoři zkontrolují:
   - Zda je práce relevantní pro fyziku
   - Zda má minimální vědeckou kvalitu
   - Zda neobsahuje plagiát nebo spam
4. **Moderace trvá 1-3 dny**

### Krok 13: Po schválení
1. Dostanete email s potvrzením
2. Preprint dostane DOI (formát: 10.31219/osf.io/XXXXX)
3. Práce je veřejně dostupná a citovatelná
4. Můžete aktualizovat na novou verzi kdykoliv

## Možnost B: OSF Projekt (pro komplexnější správu)

### Krok 1: Vytvoření projektu
1. Jděte na https://osf.io/
2. Klikněte na "Create Project"
3. Název: "Unified Biquaternion Theory"

### Krok 2: Popis projektu
V popisu uveďte:
```markdown
# Unified Biquaternion Theory (UBT)

A comprehensive framework unifying General Relativity, Quantum Field Theory, and Standard Model symmetries through biquaternionic fields over complex time.

## Core Equation
∇†∇Θ(q,τ) = κ𝒯(q,τ)

## Current Status
Research framework making first testable predictions (v10.0, November 2025).
Scientific rating: 5.5/10

## Repository
GitHub: https://github.com/DavJ/unified-biquaternion-theory
Zenodo: [přidáte po publikaci]

## License
CC BY 4.0
```

### Krok 3: Kategorie a tagy
- **Category**: Project
- **Tags**: Stejné jako u preprintu

### Krok 4: Nahrání souborů
V OSF projektu můžete vytvořit strukturu:
```
OSF Storage/
├── Documents/
│   ├── UBT_Main.pdf
│   ├── UBT_Abstract_OSF.pdf
│   ├── Appendix_F.pdf
│   ├── Appendix_G.pdf
│   └── Appendix_H.pdf
├── LaTeX_Sources/
│   ├── UBT_Main.tex
│   ├── references.bib
│   └── [další .tex soubory]
├── Scripts/
│   └── [Python skripty]
└── Documentation/
    ├── README.md
    ├── RESEARCH_PRIORITIES.md
    └── LICENSE.md
```

### Krok 5: Integrace s GitHubem
1. V projektu jděte na "Add-ons"
2. Povolte "GitHub"
3. Propojte s repozitářem `DavJ/unified-biquaternion-theory`
4. Synchronizace bude obousměrná

### Krok 6: Wiki (volitelné)
Můžete vytvořit Wiki s:
- Přehled teorie
- Postupy výpočtů
- FAQ
- Changelog

### Krok 7: Nastavení viditelnosti
- **Public**: Každý může číst (doporučeno)
- **Private**: Jen vy a spolupracovníci
- Po publikaci již nelze změnit na private!

### Krok 8: Registrace DOI
1. V projektu jděte do "Settings"
2. Najděte sekci "Create DOI"
3. Klikněte na "Create DOI"
4. OSF vytvoří trvalý identifikátor

### Krok 9: Vytvoření preprintu z projektu
1. V projektu klikněte na "Create Preprint"
2. Vyberte hlavní dokument
3. Vyplňte metadata (podobně jako v Možnosti A)
4. Odešlete k moderaci

## Kombinovaná strategie (DOPORUČENO)

### Fáze 1: Zenodo (týden 1)
1. Publikujte na Zenodo pro archivaci
2. Získejte Zenodo DOI
3. Aktualizujte dokumenty s DOI

### Fáze 2: OSF Projekt (týden 1-2)
1. Vytvořte OSF projekt
2. Propojte s GitHubem
3. Nahrajte dokumentaci

### Fáze 3: OSF Preprint (týden 2-3)
1. Připravte preprint na PhysArXiv
2. V metadatech uveďte Zenodo DOI jako "Related work"
3. Odešlete k moderaci

### Fáze 4: Propojení (po schválení)
Aktualizujte všechny platformy s odkazy:

**V GitHub README.md**:
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![OSF](https://img.shields.io/badge/OSF-Project-blue)](https://osf.io/XXXXX/)

## Published Versions
- **Zenodo Archive**: https://doi.org/10.5281/zenodo.XXXXXXX
- **OSF Preprint**: https://doi.org/10.31219/osf.io/XXXXX
- **OSF Project**: https://osf.io/XXXXX/
```

**V OSF projektu**: Přidejte odkaz na Zenodo
**V Zenodo záznamu**: Přidejte odkaz na OSF (lze editovat metadata)

## Po publikaci na OSF

### 1. Sdílení
OSF automaticky sdílí na:
- Google Scholar (indexování do 1-2 týdnů)
- SHARE (okamžitě)
- BASE (do 1 měsíce)

### 2. Sledování metrik
OSF poskytuje statistiky:
- Počet zobrazení
- Počet stažení
- Geolokace návštěvníků
- Citations (pokud je práce citována)

### 3. Aktualizace
Pro novou verzi:
1. Nahrajte nový soubor
2. OSF vytvoří novou verzi s vlastním DOI
3. Staré verze zůstávají dostupné

### 4. Diskuse
- Povolit komentáře na OSF projektu
- Reagovat na feedback komunity
- Případně zveřejnit peer review (pokud bude)

## Časté problémy a řešení

### Problém: Preprint byl odmítnut moderací
**Řešení**: 
- PhysArXiv odmítá práce, které nejsou vědecké nebo relevantní pro fyziku
- Pokud je odmítnut, zkuste:
  - OSF Preprints (obecný server, méně přísný)
  - Vylepšit vědeckou rigorositu dokumentu
  - Přidat více matematických detailů

### Problém: Nemohu přidat spolupracovníky
**Řešení**: V projektu → Contributors → Add → zadejte OSF email nebo jméno

### Problém: GitHub integrace nefunguje
**Řešení**: 
1. Zkontrolujte oprávnění v GitHub Settings → Applications
2. Znovu autorizujte OSF
3. V OSF projektu odpojte a znovu připojte add-on

### Problém: DOI se nevytváří
**Řešení**: 
- DOI pro projekt se vytváří jen jednou (nelze smazat!)
- Pro preprint se DOI vytváří automaticky po schválení
- Zkontrolujte, že máte správná oprávnění (musíte být admin projektu)

### Problém: Chci změnit autory po publikaci
**Řešení**: 
- U preprintu: Nahrajte novou verzi se správnými autory
- U projektu: Změňte Contributors kdykoliv

## Kontrolní seznam před publikací na OSF

**Pro Preprint:**
- [ ] PDF dokument je zkompilován bez chyb
- [ ] Abstrakt je kompletní a srozumitelný
- [ ] Všichni autoři jsou správně uvedeni
- [ ] Email kontakt je vyplněn: jdavid.cz@gmail.com
- [ ] Klíčová slova jsou relevantní
- [ ] Licence je nastavena na CC BY 4.0
- [ ] Dokument neobsahuje důvěrné informace
- [ ] Již publikováno na Zenodo (volitelné, ale doporučené)

**Pro Projekt:**
- [ ] Název projektu je popisný
- [ ] Popis projektu je kompletní
- [ ] Struktura složek je logická
- [ ] README je přehledné
- [ ] GitHub je propojený (volitelné)
- [ ] Viditelnost je nastavena na Public

## Doporučené workflow pro UBT

### Týden 1: Příprava
- [ ] Dokončit všechny dokumenty
- [ ] Zkompilovat všechny PDF
- [ ] Aktualizovat README
- [ ] Vyplnit email ve všech dokumentech
- [ ] Vytvořit GitHub release v10.0

### Týden 2: Zenodo
- [ ] Publikovat na Zenodo
- [ ] Získat Zenodo DOI
- [ ] Aktualizovat dokumenty s DOI
- [ ] Přidat badge do README

### Týden 3: OSF
- [ ] Vytvořit OSF projekt
- [ ] Propojit s GitHubem
- [ ] Nahrát dokumentaci
- [ ] Připravit preprint pro PhysArXiv

### Týden 4: PhysArXiv
- [ ] Odeslat preprint k moderaci
- [ ] Čekat na schválení (1-3 dny)
- [ ] Po schválení: získat OSF DOI
- [ ] Aktualizovat všechny platformy s odkazy

### Týden 5: Propagace
- [ ] Sdílet na social media (Twitter/X, LinkedIn)
- [ ] Poslat kolegům a v relevantních komunitách
- [ ] Diskutovat na fórech (Physics Stack Exchange, Reddit r/Physics)
- [ ] Případně kontaktovat physics blogs

## Užitečné odkazy

### OSF
- **OSF Homepage**: https://osf.io/
- **OSF Help**: https://help.osf.io/
- **PhysArXiv**: https://osf.io/preprints/physarxiv
- **OSF Support**: support@osf.io

### Preprint servery (alternativy)
- **arXiv.org**: https://arxiv.org/ (nejprestižnější, ale přísná moderace)
- **viXra.org**: https://vixra.org/ (bez moderace, ale nižší prestiž)
- **ResearchGate**: https://www.researchgate.net/ (sociální síť)

### Další zdroje
- **ORCID**: https://orcid.org/ (výzkumný identifikátor)
- **Google Scholar**: https://scholar.google.com/ (citační index)
- **Semantic Scholar**: https://www.semanticscholar.org/

## Podpora a komunita

### Diskuzní fóra pro teoretickou fyziku
- **Physics Stack Exchange**: https://physics.stackexchange.com/
- **Physics Forums**: https://www.physicsforums.com/
- **Reddit r/Physics**: https://www.reddit.com/r/Physics/
- **Reddit r/AskPhysics**: https://www.reddit.com/r/AskPhysics/

### Pro peer review
Po publikaci preprintu můžete požádat o neformální review:
- Peer Community In (PCI): https://peercommunityin.org/
- Review Commons: https://www.reviewcommons.org/
- Nebo přímo kontaktovat experty v oboru

## Srovnání publikačních strategií

| Strategie | Výhody | Nevýhody | Doporučení pro UBT |
|-----------|--------|----------|---------------------|
| **Jen Zenodo** | Rychlé, jednoduché, DOI | Malá viditelnost | ⭐⭐ Dobré pro archivaci |
| **Jen OSF** | Diskuse, komunita | Méně známé než arXiv | ⭐ Slabší pro citace |
| **Zenodo + OSF** | Archivace + viditelnost | Více práce | ⭐⭐⭐⭐ Doporučeno |
| **arXiv** | Nejprestižnější | Velmi přísná moderace | ⭐⭐⭐ Pokud projde |
| **Zenodo + OSF + arXiv** | Maximum viditelnosti | Nejvíce práce | ⭐⭐⭐⭐⭐ Ideální |

**Pro UBT doporučuji**: Zenodo + OSF (PhysArXiv), případně zkusit i arXiv.org

---

**Poznámka**: Tento návod byl vytvořen v listopadu 2025 pro publikaci UBT v10.0. OSF rozhraní se může v budoucnu změnit, ale základní workflow zůstává podobný.

**Autor návodu**: GitHub Copilot pro Davida Jaroše  
**Datum**: 3. listopadu 2025
