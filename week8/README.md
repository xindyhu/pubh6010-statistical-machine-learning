# Lecture 08 Exercise — Ridge, LASSO and Elastic Net

PubH 6010 Independent Study (Fall 2026). Companion to PUBH 6886 Lecture 08.

Katie replicates the **LASSO** and **elastic net** in **Gibson et al. (2019)** (NHANES 2001–2002 POPs and leukocyte telomere length) and adds ridge, which the paper did not fit. She then checks how stable the variable selection is. The data are the same `studypop.csv` used in Weeks 3 and 7. Written in **tidymodels**. Part A uses `cv.glmnet()` directly because that is how the authors chose λ, and matching their folds is the point of that part. 5 questions.

## Files

| File | What it is |
|---|---|
| `lecture08_exercise_ridge_lasso.Rmd` / `.html` | **Start here.** Reading, tasks (Parts A–E, Q1–Q5), starter code (tested), numbers to check against |
| `studypop.csv` | NHANES 2001–2002, 1,330 × 33. Identical to Weeks 3 and 7 (same MD5 as the authors' repo copy) |
| `lecture08.Rproj` | RStudio project |

**Software:** tidyverse, `tidymodels`, `glmnet` (all CRAN; no Bioconductor this week). Parts A–D run in under a minute; Part E (25 CV repeats) takes 1–2 minutes.

## Paper

Gibson EA, Nunez Y, Abuawad A, Zota AR, Renzetti S, Devick KL, Gennings C, Goldsmith J, Coull BA, Kioumourtzoglou MA. *Environ Health.* 2019;18:76. doi:10.1186/s12940-019-0515-1. Data availability: github.com/lizzyagibson/Mixtures.Workshop.2018 (now SHARP.Mixtures.Workshop). LASSO/EN code: `Supervised/Variable Selection/Lasso_elastic_net.Rmd`.

## Mapping to the slides

| Part | Slides | Task |
|---|---|---|
| A | 17, 25 | Replicate the paper's LASSO with the authors' `cv.glmnet()` setup (covariates unpenalized via `penalty.factor`) |
| B | 17–19, 25–28 | Same LASSO in tidymodels: λ_min vs 1-SE rule, CV curve vs covariates-only model, coefficient paths |
| C | 9–14, 22–23 | Ridge: no selection, CV comparison with LASSO |
| D | 36 | Elastic net, tuning α and λ jointly; compare with the paper's α = 0.8 |

## Key results (answer key)

- **Replication is exact** under the pre-R 3.6 sampler: `RNGkind(sample.kind = "Rounding")`, `set.seed(2)` gives λ = 0.00341 (paper 0.0034) and the same four POPs: PCB 99 0.0014, PCB 118 0.0034, 2,3,4,7,8-pncdf 0.022, PCB 126 0.0103. With current R's default sampler, the same seed gives λ = 0.0031 and a fifth, near-zero POP.
- **tidymodels LASSO:** λ_min = 0.0030, the same four plus 1,2,3,4,6,7,8-hpcdf (β ≈ 0.0002). **The 1-SE rule zeros every POP.** CV RMSE: covariates only 0.2030, best LASSO 0.2014, a gain of about a quarter of one SE (SE ≈ 0.006). The POPs add almost nothing to prediction.
- **Ridge:** CV RMSE 0.2015 (same as LASSO). PCB 169 gets weight that LASSO dropped. Small negative β for OCDD, PCB 180 and PCB 194.
- **Elastic net:** CV picks α = 0.4 (paper 0.8), but the best CV RMSE differs only in the 5th decimal across α = 0.1–1, so α is not identified. It selects **the same five POPs as the paper**.
