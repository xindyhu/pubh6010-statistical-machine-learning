# Lecture 07 Exercise — PCR and PLSR

PubH 6010 Independent Study (Fall 2026). Companion to PUBH 6886 Lecture 07.

Katie replicates the principal components regression in **Gibson et al. (2019)** (NHANES 2001–2002 persistent organic pollutants and leukocyte telomere length). She then redoes it the lecture's way: choosing the number of components by 10-fold CV and comparing it with PLSR. Subset selection (slides 12–36) is not covered. The data are the Week 3 `studypop.csv`, so the new work is the regression, not the data. Written in **tidymodels**, like Week 6.

## Files

| File | What it is |
|---|---|
| `lecture07_exercise_PCR_PLSR.Rmd` / `.html` | **Start here.** Reading, data table, tasks (Parts A–D, Q1–Q4), starter code, numbers to check against |
| `studypop.csv` | NHANES 2001–2002, 1,330 × 33 (identical to Week 3's file; from the authors' repo) |
| `lecture07.Rproj` | RStudio project |
| `answer_key/` | Instructor key (`.Rmd`, `.R`, `.html`). **Do not commit** |

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

## Key results (answer key)

- **Replication is exact.** PC1 β = −0.0116 (95% CI −0.018, −0.005), PC2 0.0008, PC3 0.0023, matching Table 1 of the paper, but only without cotinine (see notes). All PC1 loadings are negative, so the negative β is the paper's "positive association". Without covariates the sign flips (+0.019; r(PC1, age) = −0.76).
- **PCR (POPs only):** best M = 9, 1-SE M = 4. RMSE 0.217 vs 0.232 for the intercept-only model.
- **PLSR:** best M = 3, 1-SE M = 2. Same pattern as the PSA example: PLS packs the signal into fewer components.

## Instructor notes

- **Checked against the paper (PDF, 2026-10-12).** Table 1's PCA row reproduces exactly: PC1 −0.01 (−0.02, −0.01), p < 0.001; PC2 p = 0.87; PC3 p = 0.76. The sample is 1,003, and the PCs were chosen *a priori* to explain ≥ 75% of the variance (the paper says 79.7%; we get 79.9%). The paper did not use survey weights.
- **Methods–results inconsistency (good for the article critique).** The Methods (p. 3) say every model adjusts for log serum cotinine, but Table 1's PCR numbers reproduce only **without** cotinine. With cotinine: PC1 −0.0112, PC2 p = 0.67, PC3 p = 0.46. Part B has Katie find this herself.
- **Furan label.** The paper calls `LBXF08LA` "1,2,3,4,6,7,8-hxcdf", but it is the hepta congener (hpcdf). The handout's data table notes this.
- **mixOmics install.** `install.packages("mixOmics")` fails with "not available for this version of R" because mixOmics is on Bioconductor; use `BiocManager::install("mixOmics", update = FALSE, ask = FALSE)`. Without `update = FALSE` BiocManager offers to update every outdated package, and answering "a" with packages loaded can hang RStudio. The starter code has a CRAN-only fallback for Part D (`pls::plsr()` on the same folds), which also gives best M = 3.
- **Week 3 dictionary error.** `claude-output/week3_pca_clustering/studypop_data_dictionary.md` labels `LBXPCBLA` as PCB 169 and `LBXHXCLA` as PCB 156. Per the NHANES codebook and the authors' code they are **PCB 126** and **PCB 169**. The Week 7 handout flags the correction; the Week 3 file has not been edited.
- **Sign of PCs.** `prcomp()` signs can differ across BLAS/LAPACK builds. If Katie's PC1 loadings come out positive, her β will be +0.0116, and Q2 still works.
- Numbers were produced with R 4.3.3, recipes 1.0.9, tune 1.1.2 and mixOmics 6.23. Newer versions on Katie's Mac should agree to the printed digits. CV numbers depend on the fold assignment (`set.seed(1234)`).
