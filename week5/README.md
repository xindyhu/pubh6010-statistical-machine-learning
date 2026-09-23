# Lecture 05 Exercise — Checking a published LDA paper

PubH 6010 Independent Study (Fall 2026). Companion to PUBH 6886 Lecture 05 (LDA, QDA, naive Bayes).

Students fit LDA, QDA and naive Bayes to the Wisconsin Diagnostic Breast Cancer data and compare their results with **Adebiyi et al. (2022)**. That paper names LDA in its title but uses it only as a preprocessing step. The exercise uses this gap to test whether students understand what LDA actually does.

## Files

| File | What it is |
|---|---|
| `lecture05_exercise_LDA_QDA_NB.Rmd` / `.html` | **Start here.** Reading, tasks (Parts A–D, Q1–Q5), starter code |
| `wdbc.csv` | WDBC data, 569 × 32, cleaned from the Kaggle file the paper cites |
| `data_dictionary.Rmd` / `.html` | Columns, how the features were measured, collinearity, what changed from the Kaggle file |
| `lecture05.Rproj` | RStudio project |

**Software:** tidyverse (`readr`, `dplyr`, `tidyr`, `ggplot2`, `purrr`), `MASS` (`lda`, `qda`), `e1071` (`naiveBayes`, `svm`). Load MASS with `library(MASS, exclude = "select")`.

## Reading

Adebiyi MO, Arowolo MO, Mshelia MD, Olugbara OO. Linear discriminant analysis classification model for breast cancer diagnosis. *Appl Sci.* 2022;12(22):11455. doi:10.3390/app122211455 (open access).

Data: Street WN, Wolberg WH, Mangasarian OL. Nuclear feature extraction for breast tumor diagnosis. *IS&T/SPIE Electronic Imaging* 1993. UCI ML Repository dataset 17; Kaggle `uciml/breast-cancer-wisconsin-data`.
