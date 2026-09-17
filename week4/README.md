# Lecture 04 Exercise — Classification: KNN, Logistic Regression & Model Evaluation

PubH 6010 Independent Study (Fall 2026). Companion to PUBH 6886 Lecture 04.

**Question:** Using only what is known the day before, can we predict whether a Chicago beach will exceed **235 CFU/100 mL *E. coli***? The problem links extreme weather (rainfall, sewer-overflow lock openings) to waterborne-illness risk, and the event is rare: 13.9% of beach-days exceed the limit.

## Files

| File | What it is |
|---|---|
| `lecture04_exercise_classification.Rmd` / `.html` | **Start here.** Background, reading, tasks (Parts A–E, Q1–Q6), starter code |
| `beach_ecoli.csv` | Analytic dataset: 9,259 beach-days, 20 beaches, 2006–2016 |
| `beach_ecoli_data_dictionary.Rmd` / `.html` | Column definitions, provenance, limitations |
| `prepare_beach_ecoli.R` | Rebuilds `beach_ecoli.csv` from the City of Chicago repository (pinned commit). Students do not need to run it. |
| `lecture04.Rproj` | RStudio project |

**Software:** base R plus the `class` package (installs with R). The optional bonus uses `nnet`, which also installs with R.

## Reading

- **Main:** Elahi A, et al. Machine learning, generalization, and transfer learning for predicting the exceedance of fecal indicator bacteria thresholds at beaches. *Environ Sci Technol.* 2025;59(42):22386–22396. doi:10.1021/acs.est.5c02835
- **Data source:** Lucius N, et al. Predicting *E. coli* concentrations using limited qPCR deployments at Chicago beaches. *Water Research X.* 2019;2:100016. doi:10.1016/j.wroa.2018.100016

## Data license

Source data and code © 2015 City of Chicago, MIT License (https://github.com/Chicago/e-coli-beach-predictions). *E. coli* results come from Chicago Park District beach monitoring. Weather values come from the discontinued Dark Sky API, as redistributed in that repository.

## Instructor notes

- `answer_key/` (`.Rmd`, `.R`, `.html`) is **git-ignored and never committed**. A file removed later with `git rm` stays recoverable from the repository history, so keep the key local or in a separate private repository.
- To rebuild the data, run `Rscript prepare_beach_ecoli.R` (downloads about 7.7 MB into `raw/`, which is git-ignored).
