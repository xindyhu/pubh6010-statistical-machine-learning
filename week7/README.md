# Lecture 07 Exercise — PCR and PLSR

PubH 6010 Independent Study (Fall 2026). Companion to PUBH 6886 Lecture 07.

In this exercise, you will replicate the principal components regression in **Gibson et al. (2019)** (NHANES 2001–2002 persistent organic pollutants and leukocyte telomere length). Then you will redo it the lecture's way: choosing the number of components by 10-fold CV and comparing it with PLSR. The data are the Week 3 `studypop.csv`, so the new work is the regression, not the data. Written in **tidymodels**, like Week 6.

## Files

| File | What it is |
|---|---|
| `lecture07_exercise_PCR_PLSR.Rmd` / `.html` | **Start here.** Reading, data table, tasks (Parts A–D, Q1–Q4), starter code, numbers to check against |
| `studypop.csv` | NHANES 2001–2002, 1,330 × 33 (identical to Week 3's file; from the authors' repo) |
| `lecture07.Rproj` | RStudio project |

**Software:** tidyverse, `tidymodels`, and `mixOmics` from Bioconductor (`BiocManager::install("mixOmics", update = FALSE, ask = FALSE)`, not `install.packages()`), which `step_pls()` needs. **Load mixOmics before tidyverse.** It attaches MASS and defines its own `map()`, which otherwise mask `dplyr::select()` and `purrr::map()`. Runs in under a minute.

## Paper

Gibson EA, Nunez Y, Abuawad A, Zota AR, Renzetti S, Devick KL, Gennings C, Goldsmith J, Coull BA, Kioumourtzoglou MA. An overview of methods to address distinct research questions on environmental mixtures: an application to persistent organic pollutants and leukocyte telomere length. *Environ Health.* 2019;18:76. doi:10.1186/s12940-019-0515-1. Code and data: github.com/lizzyagibson/SHARP.Mixtures.Workshop.

## Mapping to the slides

| Part | Slides | Task |
|---|---|---|
| A | 7–8 | Analytic sample (n = 1,003), collinearity of the 18 log POPs |
| B | 38–40 | Replicate Table 1: `prcomp()` → PC1–PC3 + covariates in `lm()`, with and without cotinine |
| C | 37–45 | PCR for prediction: `step_pca(num_comp = tune())`, 10-fold CV, 1-SE rule, back-transformed β |
| D | 46–51 | PLSR with `step_pls()`, same folds, PCR vs PLSR curves |
