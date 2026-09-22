# Lecture 04 Exercise — Replicating a published beach-water classifier

PubH 6010 Independent Study (Fall 2026). Companion to PUBH 6886 Lecture 04.

Students rebuild the Chicago analysis from **Elahi et al. (2025)** on the authors' own data, using the paper's features, split, preprocessing and metrics — then evaluate it more thoroughly than the paper does.

## Files

| File | What it is |
|---|---|
| `lecture04_exercise_classification.Rmd` / `.html` | **Start here.** Reading, tasks (Parts A–F, Q1–Q8), starter code |
| `Data-CHI.csv` | The authors' Chicago dataset, from the figshare archive cited in the paper |
| `data_dictionary.Rmd` / `.html` | Columns, the paper's 12 features, missingness, what their code drops |
| `lecture04.Rproj` | RStudio project |

**Software:** tidyverse (`readr`, `dplyr`, `tidyr`, `ggplot2`, `purrr`) plus `class`; `nnet` for the optional three-class part.

## Reading

Elahi A, Shumway D, Kowalcyk M, Shrestha A, Caragea D, Caragea C, Dorevitch S. Machine learning, generalization, and transfer learning for predicting the exceedance of fecal indicator bacteria thresholds at beaches. *Environ Sci Technol.* 2025;59(42):22386–22396. doi:10.1021/acs.est.5c02835 (open access). Data: the figshare archive cited in the paper. Code: `github.com/aliielahi/ONR-WQ`.

## How closely this follows the paper

| Step | The paper | This exercise |
|---|---|---|
| Years | Chicago 2016–2019 | same |
| Split | Before 2019 = training; 2019 = testing; no validation set | same |
| Outcome | ENT > 320 CCE/100 mL (half the 640 BAV) | same |
| Features | The 12 columns surviving their drop list | same |
| Imputation | Noisy average from training mean and SD | same |
| Scaling | Min-max on training range | same |
| Tuning | 4-fold CV inside the training years, 15 seeds | 4-fold CV inside the training years, single seed |
| Models | Logistic regression, random forest, transfer learning | Logistic regression, KNN (Lecture 04's methods) |
| Metrics | Sensitivity, specificity, PPV, NPV, AUC, weighted F1 | same, plus a calibration plot |

## What the replication shows

1. **Table 1 reproduces exactly** (4,404 / 1,900; 68.143% / 79.158% negative), and plain `glm()` reaches **AUC 0.695** against the paper's 0.693 — with no regularisation, tuning or repeated seeds.
2. **Identical AUC, opposite behaviour.** At a 0.5 cutoff our model warns on 95% of days (sensitivity 0.992, specificity 0.057); theirs warns almost never (0.220, 0.966). AUC says nothing about where the probabilities sit.
3. **Lake level is the reason.** Training runs 176.69–177.24 m and 2019 runs 177.12–177.60 m, a record high, so min-max scaled test values reach 1.65 — outside the range the coefficient came from. Dropping it lowers AUC to 0.632 and repairs the probabilities (mean 0.333 against 0.208 observed). The better-ranking model is the one you could not deploy.

## Instructor notes

- `answer_key/` is **git-ignored and never committed**. A file removed later with `git rm` stays recoverable from history, so keep the key local or in a separate private repo.
- Article-critique material for the December deliverable: the feature set is fixed by the Chicago/San Diego intersection rather than by Chicago predictive value; wave height is 59% missing in the training years and imputed from its own mean and SD; `tide_gtm` uses the mean of the whole series including the test year; Table 4 reports PPV 0.990 with sensitivity 0.220 for the Chicago logistic model, which is hard to reconcile with 20.8% prevalence; Table 5's Chicago:Chicago row duplicates the Chicago:San Diego generalization row; and the two released copies of `Data-CHI.csv` disagree on solar irradiance.
