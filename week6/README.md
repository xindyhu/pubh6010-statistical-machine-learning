# Lecture 06 Exercise — Cross-validation and the bootstrap

PubH 6010 Independent Study (Fall 2026). Companion to PUBH 6886 Lecture 06.

The exercise follows the lecture's R examples step by step, using daily PM2.5 in Beijing (UCI Machine Learning Repository, *Beijing PM2.5 Data*, dataset 381) instead of the prostate and heart-disease data. It is written in **tidymodels** rather than the slides' caret. The handout opens with a caret → tidymodels translation table.

## Files

| File | What it is |
|---|---|
| `lecture06_exercise_CV_bootstrap.Rmd` / `.html` | **Start here.** Tasks (Parts A–F, Q1–Q6), starter code, numbers to check against |
| `beijing_pm25_2014.csv` | 360 days of 2014: daily PM2.5 and weather |
| `lecture06.Rproj` | RStudio project |

**Software:** tidyverse, `tidymodels`, `kknn` (KNN engine) and `probably` (thresholds). Install with `install.packages(c("tidymodels", "kknn", "probably"))`. Runs in about 2 minutes.

## Mapping to the slides

| Part | Slides | Task |
|---|---|---|
| B | 7–9 | Validation set: one split with `initial_validation_split()` + `validation_set()` |
| C | 13, 26–28, 32 | LOOCV (`vfold_cv(v = n)`) and 10-fold for `linear_reg()`; check the leverage shortcut |
| D | 29–34 | Tune K for KNN regression (1–20) with `tune_grid()`, `select_best()`, `finalize_workflow()` |
| E | 35–39 | Logistic regression, 10-fold: `metric_set(accuracy, kap, roc_auc, sens, spec)`, `probably::threshold_perf()` |
| F | 41–43 | `bootstraps()` + `int_pctl()`: SE and CI for a coefficient and for the 90th percentile of PM2.5 |

## Data source

Liang X, et al. Assessing Beijing's PM2.5 pollution: severity, weather impact, APEC and winter heating. *Proc R Soc A.* 2015;471:20150257. UCI dataset 381 (https://archive.ics.uci.edu/dataset/381/beijing+pm2+5+data). The hourly file in `raw/` was downloaded directly from UCI on 2026-09-30.