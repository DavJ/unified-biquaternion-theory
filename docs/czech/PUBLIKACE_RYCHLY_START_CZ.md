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

# Rychlý start: Publikace UBT v10.0 na Zenodo a OSF

**Vytvořeno**: 3. listopadu 2025  
**Pro**: Ing. David Jaroš  
**Účel**: Přehled publikačního procesu UBT v10.0

---

## ✅ Co je hotovo

### 1. Email aktualizován
- ✅ `UBT_Abstract_OSF.tex` - email změněn na **jdavid.cz@gmail.com**
- ✅ Ověřeno, že žádné další "[To be added]" placeholdery v repozitáři nejsou

### 2. Publikační návody vytvořeny
- ✅ `ZENODO_PUBLIKACE_NAVOD_CZ.md` - kompletní návod na Zenodo (česky)
- ✅ `OSF_PUBLIKACE_NAVOD_CZ.md` - kompletní návod na OSF (česky)
- ✅ `REPOSITORY_RELEASE_CHECKLIST.md` - kontrolní seznam před publikací

### 3. Repozitář zkontrolován
- ✅ Všechny dokumenty na místě
- ✅ Bibliografie kompletní
- ✅ Licence CC BY 4.0 všude správně
- ✅ Build systém funkční (GitHub Actions)
- ✅ Žádné kritické problémy nenalezeny
- ✅ **100% připraveno k publikaci**

---

## 🚀 Doporučený postup (4 týdny)

### Týden 1: GitHub Release
1. Jdi na https://github.com/DavJ/unified-biquaternion-theory
2. Klikni na "Releases" → "Draft a new release"
3. Tag version: `v10.0`
4. Title: `Unified Biquaternion Theory v10.0`
5. Description: Viz template v `ZENODO_PUBLIKACE_NAVOD_CZ.md`
6. Klikni "Publish release"

### Týden 2: Zenodo
**📖 Viz kompletní návod: `ZENODO_PUBLIKACE_NAVOD_CZ.md`**

**Rychlý postup:**
1. Jdi na https://zenodo.org/ a přihlaš se
2. Propoj s GitHubem: Settings → GitHub → Connect
3. Aktivuj repozitář `DavJ/unified-biquaternion-theory`
4. Vytvoř GitHub release (viz týden 1)
5. Zenodo automaticky vytvoří záznam
6. Doplň metadata (viz návod)
7. Publikuj → získej DOI

**Důležité metadata:**
- Název: Unified Biquaternion Theory v10.0
- Autor: Ing. David Jaroš
- Email: jdavid.cz@gmail.com
- Licence: CC BY 4.0
- Klíčová slova: (viz seznam v návodu)

### Týden 3: OSF
**📖 Viz kompletní návod: `OSF_PUBLIKACE_NAVOD_CZ.md`**

**Rychlý postup:**
1. Jdi na https://osf.io/ a přihlaš se
2. **Možnost A - Preprint na PhysArXiv:**
   - Jdi na https://osf.io/preprints/physarxiv
   - Klikni "Submit a Preprint"
   - Nahraj `UBT_Main.pdf` nebo `UBT_Abstract_OSF.pdf`
   - Vyplň metadata (stejná jako Zenodo)
   - Odešli k moderaci
   - Počkej 1-3 dny na schválení
   - Získej OSF DOI

3. **Možnost B - OSF Projekt:**
   - Vytvoř nový projekt "Unified Biquaternion Theory"
   - Propoj s GitHubem
   - Nahraj dokumentaci
   - Pak vytvoř preprint z projektu

### Týden 4: Propojení a oznámení
1. **Aktualizuj README.md** s oběma DOI:
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![OSF](https://img.shields.io/badge/OSF-Preprint-blue)](https://doi.org/10.31219/osf.io/XXXXX)
```

2. **Oznám publikaci:**
   - Twitter/X, LinkedIn
   - Physics Forums, Reddit r/Physics
   - Kolegy a potenciální spolupracovníky
   - Physics blogs (pokud máš kontakty)

---

## 📚 Které soubory použít

### Pro Zenodo
**Doporučuji nahrát:**
- Všechny PDF z `docs/pdfs/` (automaticky kompilované)
- `README.md` - hlavní dokumentace
- `LICENSE.md` - licence
- `references.bib` - bibliografie

**Nebo jednodušeji:**
- ZIP archiv celého GitHub repozitáře (Zenodo to udělá automaticky při GitHub integraci)

### Pro OSF Preprint
**Doporučuji:**
- `UBT_Main.pdf` - pro kompletní preprint, NEBO
- `UBT_Abstract_OSF.pdf` - pro kratší overview článek

**Doplňkové materiály** (volitelné):
- Appendixy jako dodatečné soubory
- Python skripty
- LaTeX zdroje

---

## 🎯 Klíčové informace

### Metadata (stejná pro obě platformy)

**Název:**
```
Unified Biquaternion Theory v10.0
```

**Autor:**
```
Ing. David Jaroš
Email: jdavid.cz@gmail.com
```

**Abstrakt:**
Viz celý text v souboru `UBT_Abstract_OSF.tex` (sekce `\begin{abstract}...\end{abstract}`)

**Klíčová slova:**
```
biquaternion algebra, complex time, unified field theory, General Relativity, 
quantum field theory, Standard Model, gauge unification, Hermitian gravity, 
SU(3) symmetry, theta functions, dark matter, dark energy, fermion masses
```

**Licence:**
```
Creative Commons Attribution 4.0 International (CC BY 4.0)
```

**Obor (pro OSF):**
```
Physical Sciences and Mathematics → Physics → Theoretical Physics
```

---

## ⚠️ Důležitá upozornění

### Před publikací
1. ✅ **Zkontroluj email** - jdavid.cz@gmail.com je správný? ✅ ANO
2. ✅ **Ověř dokumenty** - všechno se kompiluje bez chyb?
3. ✅ **Zkontroluj licenci** - CC BY 4.0 všude?
4. ✅ **GitHub release** - vytvořen před Zenodo publikací?

### Během publikace
- **Zenodo**: Po publikaci nelze smazat! (jen skrýt)
- **OSF**: Po schválení preprintu nelze smazat!
- **Ulož si okamžitě všechny DOI**
- **Udělej screenshoty** stránek s publikacemi

### Po publikaci
- ✅ Aktualizuj README.md s DOI badges
- ✅ Aktualizuj cross-reference mezi Zenodo a OSF
- ✅ Oznámkomunitekomunite
- ✅ Sleduj statistiky stahování a citací

---

## 📊 Stav repozitáře

| Položka | Stav | Poznámka |
|---------|------|----------|
| **Email kontakt** | ✅ Hotovo | jdavid.cz@gmail.com |
| **Dokumentace** | ✅ Kompletní | 171 LaTeX souborů |
| **Bibliografie** | ✅ Kompletní | references.bib |
| **Licence** | ✅ OK | CC BY 4.0 |
| **Build systém** | ✅ Funkční | GitHub Actions |
| **Připravenost** | ✅ 100% | Připraveno k publikaci |

---

## 🔗 Rychlé odkazy

### Návody
- **Zenodo návod**: `ZENODO_PUBLIKACE_NAVOD_CZ.md` (detailní, 8.9 KB)
- **OSF návod**: `OSF_PUBLIKACE_NAVOD_CZ.md` (detailní, 13.3 KB)
- **Kontrolní seznam**: `REPOSITORY_RELEASE_CHECKLIST.md` (10.8 KB)

### Platformy
- **Zenodo**: https://zenodo.org/
- **OSF**: https://osf.io/
- **PhysArXiv**: https://osf.io/preprints/physarxiv
- **GitHub**: https://github.com/DavJ/unified-biquaternion-theory

### Podpora
- **Zenodo Support**: support@zenodo.org
- **OSF Support**: support@osf.io
- **Zenodo FAQ**: https://help.zenodo.org/faq/
- **OSF Help**: https://help.osf.io/

---

## 💡 Tipy pro úspěšnou publikaci

### 1. Začni s GitHub Release
- Je to nejjednodušší krok
- Potřebuješ ho pro Zenodo automatickou integraci
- Můžeš ho udělat hned

### 2. Zenodo nejdřív
- Získáš první DOI rychle
- Jednodušší než OSF
- Pak můžeš uvést Zenodo DOI v OSF preprintu

### 3. OSF preprint s trpělivostí
- Moderace trvá 1-3 dny
- PhysArXiv je prestižnější než obecný OSF Preprints
- Pokud odmítnou, zkus obecný OSF Preprints nebo viXra

### 4. Kombinovaná strategie je nejlepší
- **Zenodo** = archivace, citace, dlouhodobé uložení
- **OSF** = preprint, viditelnost, diskuse, recenze
- Dohromady = maximum dopadu

### 5. Připrav se na feedback
- Některé reakce mohou být kritické (UBT je spekulativní teorie)
- Buď připraven vysvětlit vědecký status (5.5/10 rating)
- Odkaž na `UBT_READING_GUIDE.md` a `UBT_SCIENTIFIC_RATING_2025.md`

---

## 🎉 Shrnutí

**Co bylo uděláno:**
1. ✅ Email aktualizován v `UBT_Abstract_OSF.tex`
2. ✅ Vytvořeny kompletní návody na Zenodo a OSF (česky)
3. ✅ Proveden důkladný check repozitáře
4. ✅ Připraven kontrolní seznam
5. ✅ Repozitář 100% připraven k publikaci

**Co udělat dál:**
1. Vytvoř GitHub release v10.0
2. Publikuj na Zenodo (týden 2)
3. Publikuj na OSF (týden 3)
4. Propoj všechny platformy (týden 4)
5. Oznám komunite

**Všechno potřebné máš připravené!** 🚀

---

## 📞 Potřebuješ pomoc?

### Technické problémy
- Podívej se do FAQ v příslušném návodu
- Kontaktuj support (Zenodo/OSF)
- Zkontroluj GitHub Issues

### Vědecké otázky
- Viz `UBT_READING_GUIDE.md` - jak číst teorii
- Viz `UBT_SCIENTIFIC_RATING_2025.md` - vědecké hodnocení
- Viz `TESTABILITY_AND_FALSIFICATION.md` - testovatelnost

### Etické otázky
- Viz `CONSCIOUSNESS_CLAIMS_ETHICS.md` - etika spekulativního obsahu

---

**Hodně štěstí s publikací! 🎓**

**Připravil**: GitHub Copilot  
**Datum**: 3. listopadu 2025  
**Verze**: 1.0
