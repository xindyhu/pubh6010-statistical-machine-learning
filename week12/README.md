# Lecture 12 Exercise — Support Vector Machines

PubH 6010 Independent Study (Fall 2026), Week 12. Companion to PUBH 6886 Lecture 12.

You will fit three SVMs (linear, polynomial and radial kernels) to one slice of **Searcy & Boehm (2022)**, a forecasting study of fecal indicator bacteria at California beaches. The slice is Cowell Beach *E. coli* > 400 CFU/100 mL, forecast 1 day ahead, trained on 2007–2012 and tested on 2013–2014. The paper fits about 400 models (BLR, SVM, RF, GBM); this exercise fits 3. The samples are exactly the paper's partition (SI Table S5). The predictors are fixed at the 10 that SI Table S6 lists as most often selected for Cowell *E. coli*. There are 5 questions.

## Files

| File | What it is |
|---|---|
| `lecture12_exercise_svm.Rmd` / `.html` | **Start here.** Reading, tasks (Parts A–E, Q1–Q5), starter code (tested), numbers to check against |
| `cowell_ec_lead1.csv` | 384 samples × 15 columns: date, year, `split`, `EC`, `EC_exc`, 10 predictors |
| `CB_bulk_dataset.csv`, `HSB_bulk_dastaset.csv` | The authors' full data (Stanford Digital Repository, doi:10.25740/nw799cp6263, CC BY). Only the Cowell file is used. The HSB file name has the authors' typo |
| `raw/prepare_cowell_slice.py` | Builds `cowell_ec_lead1.csv` from `CB_bulk_dataset.csv`. A line-by-line port of the authors' `load_data()`; reproduces Table S5 exactly |
| `lecture12.Rproj` | RStudio project |

The paper PDF is not included. The SI is free at https://repository.library.noaa.gov/view/noaa/56907.

**Software:** tidyverse, tidymodels, kernlab (all CRAN). The key runs in about 1.5 minutes.

## Paper

Searcy RT, Boehm AB. Know Before You Go: Data-Driven Beach Water Quality Forecasting. *Environ Sci Technol.* 2022. doi:10.1021/acs.est.2c05972. (I did not verify the volume and page numbers; check them before citing.) Code: https://github.com/rtsearcy/wq-forecasting.

## Mapping to the slides

| Part | Slides | Task |
|---|---|---|
| A | SVM recap | Counts vs Table S5, drift in prevalence, "always no" baseline, why kernels need scaled predictors |
| B | Maximal margin and support vector classifier; binary example (linear) | Unweighted SVC collapses to "always no"; balanced class weights; support vectors and ‖β‖ vs C; CV over C |
| C | SVM with polynomial and radial kernels; binary example | Tune degree/scale/C and σ/C; heatmap; test table for three kernels; bootstrap CIs for AUC |
| D | (beyond the slides) | Decision values vs Platt probabilities; reproduce the paper's sensitivity 0 / specificity 1; paper's cutoff rule on training vs out-of-fold scores |
| E | — | Why our AUC beats the paper's; time split vs CV; early-warning value; dry-season data and extreme precipitation |

