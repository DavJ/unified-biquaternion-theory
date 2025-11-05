# Návod na publikaci UBT na Zenodo (česky)

## Co je Zenodo?

Zenodo je otevřený repozitář pro vědecké publikace provozovaný CERNem. Každé nahrané dílo získá DOI (Digital Object Identifier), což je trvalý identifikátor pro citace. Zenodo je ideální pro:
- Archivaci vědeckých prací
- Získání citovatelného DOI
- Zabezpečení dlouhodobého přístupu k dokumentům
- Integrace s GitHubem

## Příprava před publikací

### 1. Kontrola dokumentů
Ujistěte se, že máte připraveny tyto soubory:
- ✅ `UBT_Abstract_OSF.tex` - Abstrakt pro publikaci
- ✅ `UBT_Main.tex` - Hlavní dokument
- ✅ `references.bib` - Bibliografie
- ✅ Všechny appendixy (Appendix_F, G, H, atd.)
- ✅ README.md s popisem teorie
- ✅ LICENSE.md (CC BY 4.0)

### 2. Kompilace PDF dokumentů
GitHub Actions automaticky kompiluje PDF soubory při každém push. Zkontrolujte, že:
- Všechny dokumenty se kompilují bez chyb
- PDF soubory jsou v adresáři `docs/pdfs/`
- Netlachlá v dokumentech žádné chyby nebo varování

### 3. Metadata k přípravě
Připravte si tyto informace:
- **Název**: Unified Biquaternion Theory (UBT) v10.0
- **Autor**: Ing. David Jaroš
- **Email**: jdavid.cz@gmail.com
- **Datum**: Listopad 2025
- **Licence**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Klíčová slova**: biquaternion algebra, complex time, unified field theory, General Relativity, quantum field theory, Standard Model, gauge unification, Hermitian gravity, SU(3) symmetry, theta functions, dark matter, dark energy
- **Vědecké obory**: Theoretical Physics, Mathematical Physics, Quantum Field Theory, General Relativity

## Krok za krokem: Publikace na Zenodo

### Krok 1: Vytvoření účtu
1. Jděte na https://zenodo.org/
2. Klikněte na "Sign up" nebo "Log in"
3. Můžete se přihlásit přes:
   - GitHub účet (doporučeno - umožňuje automatické nahrávání)
   - ORCID
   - Email

### Krok 2: Propojení s GitHubem (doporučeno)
1. Po přihlášení jděte do Settings → GitHub
2. Klikněte na "Connect"
3. Autorizujte Zenodo přístup k vašim GitHub repozitářům
4. Najděte repozitář `DavJ/unified-biquaternion-theory`
5. Aktivujte přepínač pro automatickou archivaci

### Krok 3: Vytvoření release na GitHubu
1. Jděte na https://github.com/DavJ/unified-biquaternion-theory
2. Klikněte na "Releases" → "Draft a new release"
3. Vyplňte:
   - **Tag version**: v10.0
   - **Release title**: Unified Biquaternion Theory v10.0
   - **Description**: (viz níže)
4. Klikněte na "Publish release"

#### Doporučený text pro GitHub Release:

```markdown
# Unified Biquaternion Theory v10.0 (November 2025)

## Major Updates
- Fermion masses derived from first principles with experimental validation
- Standard Model gauge group SU(3)×SU(2)×U(1) rigorously derived from geometry
- Added comprehensive documentation and publication metadata
- Email contact information completed

## Key Documents
- UBT_Main.pdf - Full consolidated theory document
- UBT_Abstract_OSF.pdf - Abstract for academic publication
- Complete appendices (F, G, H) with mathematical proofs

## Scientific Status
Research framework making first testable predictions. Scientific rating: 5.5/10.
See UBT_SCIENTIFIC_RATING_2025.md for detailed evaluation.

## Citation
Jaroš, D. (2025). Unified Biquaternion Theory v10.0. Zenodo. https://doi.org/[bude přiděleno]

## License
Creative Commons Attribution 4.0 International (CC BY 4.0)
```

### Krok 4: Automatická archivace na Zenodo
Pokud jste propojili GitHub s Zenodo:
1. Zenodo automaticky vytvoří záznam po publikování release
2. Přejděte na https://zenodo.org/account/settings/github/
3. Najděte nový release a klikněte na název
4. Zenodo vás přesměruje na stránku s návrhem záznamu

### Krok 5: Ruční nahrání (alternativa)
Pokud nechcete propojit GitHub:
1. Jděte na https://zenodo.org/deposit/new
2. Klikněte na "Upload files"
3. Nahrajte tyto soubory:
   - Všechny PDF dokumenty z `docs/pdfs/`
   - README.md
   - LICENSE.md
   - references.bib
   - Případně ZIP archiv celého repozitáře

### Krok 6: Vyplnění metadat

#### Základní informace
- **DOI**: (nechte prázdné, Zenodo přidělí automaticky)
- **Publication date**: Listopad 2025 nebo přesné datum publikace
- **Title**: Unified Biquaternion Theory v10.0
- **Creators**: 
  - Name: Jaroš, David
  - Affiliation: (vaše instituce, pokud máte)
  - ORCID: (pokud máte)

#### Popis
Vložte abstrakt z `UBT_Abstract_OSF.tex`:
```
The Unified Biquaternion Theory (UBT) presents a comprehensive framework for unifying General Relativity, Quantum Field Theory, and Standard Model symmetries within a single mathematical structure based on biquaternionic fields over biquaternionic time τ = t + iψ...
```
(celý abstrakt z dokumentu)

#### Typ publikace
- **Upload type**: Publication
- **Publication type**: Preprint (nebo Technical note)

#### Licence
- Vyberte: **Creative Commons Attribution 4.0 International**

#### Klíčová slova (Keywords)
Přidejte jedno po druhém:
- biquaternion algebra
- complex time
- unified field theory
- General Relativity
- quantum field theory
- Standard Model
- gauge unification
- Hermitian gravity
- SU(3) symmetry
- theta functions
- dark matter
- dark energy
- fermion masses

#### Vědecké obory (Subjects)
- Physics → Theoretical Physics
- Physics → Mathematical Physics
- Physics → Quantum Field Theory
- Physics → General Relativity and Quantum Cosmology

#### Doplňující informace
- **Version**: v10.0
- **Language**: English
- **Related identifiers**: 
  - GitHub: https://github.com/DavJ/unified-biquaternion-theory
  - (později můžete přidat OSF odkaz)

### Krok 7: Kontrola a publikace
1. Zkontrolujte všechna metadata
2. Použijte "Preview" pro náhled
3. Klikněte na "Publish"
4. **POZOR**: Po publikaci nelze záznam smazat! (lze jen skrýt nebo vytvořit novou verzi)

### Krok 8: Získání DOI
Po publikaci:
1. Zenodo přidělí DOI (formát: 10.5281/zenodo.XXXXXXX)
2. Zkopírujte DOI a poznamenejte si ho
3. DOI lze použít pro citace

## Aktualizace dokumentů s DOI

Po získání DOI aktualizujte tyto soubory:

### 1. README.md
Přidejte badge na začátek:
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

### 2. UBT_Abstract_OSF.tex
V sekci na konci dokumentu:
```latex
\textbf{DOI:} \href{https://doi.org/10.5281/zenodo.XXXXXXX}{10.5281/zenodo.XXXXXXX}
```

### 3. Citace
Doporučený citační formát:
```
Jaroš, D. (2025). Unified Biquaternion Theory v10.0. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX
```

## Další kroky po publikaci

### 1. Sdílení
- Přidejte odkaz na Zenodo do GitHub README
- Sdílejte DOI s kolegy a v komunitě
- DOI můžete použít v dalších publikacích

### 2. Nové verze
Když budete chtít publikovat novou verzi:
1. Vytvořte nový GitHub release (např. v10.1)
2. Zenodo automaticky vytvoří nový záznam
3. Všechny verze budou propojeny pod stejným "Concept DOI"
4. Každá verze má vlastní specifické DOI

### 3. Statistiky
V Zenodo můžete sledovat:
- Počet stažení
- Počet zobrazení
- Geografické rozložení návštěvníků

## Časté problémy a řešení

### Problém: GitHub integration nefunguje
**Řešení**: Použijte ruční nahrání přes webové rozhraní Zenodo.

### Problém: Příliš velké soubory
**Řešení**: Zenodo podporuje soubory až 50 GB. Pokud máte větší, rozdělte je nebo nahrajte jako ZIP archiv.

### Problém: Chci změnit metadata po publikaci
**Řešení**: Metadata lze editovat i po publikaci (kromě souborů). Jděte do záznamu → "Edit" → upravte → "Publish".

### Problém: Zapomněl jsem přidat soubor
**Řešení**: Vytvořte novou verzi s opravou. Nelze přidávat soubory do již publikované verze.

### Problém: Chyba v dokumentu
**Řešení**: Opravte v GitHub repozitáři a vytvořte novou verzi (např. v10.0.1).

## Kontrolní seznam před publikací

- [ ] Všechny dokumenty se úspěšně kompilují
- [ ] Email je vyplněn: jdavid.cz@gmail.com
- [ ] README.md obsahuje kompletní popis
- [ ] LICENSE.md je správně nastavena (CC BY 4.0)
- [ ] references.bib obsahuje všechny citace
- [ ] GitHub release je vytvořen s verzí v10.0
- [ ] Všechna metadata jsou připravena
- [ ] PDF dokumenty jsou dostupné

## Užitečné odkazy

- **Zenodo homepage**: https://zenodo.org/
- **Zenodo dokumentace**: https://help.zenodo.org/
- **Zenodo GitHub guide**: https://guides.github.com/activities/citable-code/
- **DOI systém**: https://www.doi.org/
- **Creative Commons licences**: https://creativecommons.org/licenses/

## Podpora

Pokud máte problémy:
- Zenodo Support: support@zenodo.org
- Zenodo FAQ: https://help.zenodo.org/faq/
- GitHub Issues: https://github.com/zenodo/zenodo/issues

---

**Poznámka**: Tento návod byl vytvořen v listopadu 2025 pro publikaci UBT v10.0. Rozhraní Zenodo se může v budoucnu změnit, ale základní principy zůstávají stejné.
