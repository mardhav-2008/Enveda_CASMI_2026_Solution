# Enveda CASMI 2026 — Molecule Identification from Mass Spectra

A machine learning and computational mass-spectrometry project for the **Enveda CASMI 2026 — Molecule ID From Mass Spectra** Kaggle competition.

The goal is to identify the molecular structure responsible for an MS/MS spectrum and rank up to 25 candidate molecules for each query.

---

## Competition

**Competition:** Enveda CASMI 2026 — Molecule ID From Mass Spectra

**Platform:** Kaggle

**Task:** Molecular structure identification from tandem mass spectrometry (MS/MS)

**Evaluation:** MRR@25

The competition provides millions of reference spectra associated with molecular structures. Given an unknown MS/MS spectrum, the system must retrieve and rank candidate molecules.

---

## Project Status

🚧 **In development**

Current approach:

```text
MS/MS Query
     │
     ▼
Candidate Generation
     │
     ├── Same-adduct precursor matching
     │
     └── Neutral-mass matching
             │
             ▼
      Candidate Molecules
             │
             ▼
    Spectral Similarity
             │
             ▼
   Molecule-level Ranking
             │
             ▼
       Top-25 Candidates
