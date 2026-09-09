# PubH 6010 — Applying Statistical & Machine Learning to Extreme Weather and Waterborne Disease

## 📌 Overview
This repository holds the teaching materials for a **3-credit independent study** in the Department of Environmental & Occupational Health, GW Milken Institute School of Public Health (Fall 2026). The study, *Applying Statistical and Machine Learning Methods to Environmental Health Problems*, walks through the statistical- and machine-learning toolkit one method at a time and applies to environmental-health data.

## 🎯 Learning Objectives
By the end of the semester, the student will be able to:
* Distinguish supervised from unsupervised learning, and prediction from causal inference, and say which question a given study design answers
* Apply core methods — PCA, clustering, classification (LDA/QDA), resampling, regularization/dimension reduction, tree-based methods, SVMs, and neural networks — in R
* Read a machine-learning paper critically and identify common methodological flaws (e.g. temporal leakage from random cross-validation folds on time-series data, unaddressed spatial autocorrelation, causal claims from a predictive model)
* Select and justify an appropriate modeling approach for an extreme-weather → waterborne-disease prediction question, given real constraints of administrative and surveillance data

## 🛠 Prerequisites
The student should have, or be building in parallel:
- Working proficiency in **R** and RStudio (R Markdown and Git are used throughout)
- **Applied linear regression** (PubH 6862 or equivalent); logistic regression is helpful and is reviewed as needed
- Comfort with basic **linear algebra** (matrices, eigenvectors) and calculus — reviewed briefly where a method requires it
- R and RStudio installed, plus `tidyverse`, `rmarkdown`, and `knitr`

> Reference texts, both free online: *An Introduction to Statistical Learning* (ISL, https://www.statlearning.com/) and *The Elements of Statistical Learning* (ESL, https://hastie.su.domains/ElemStatLearn/).

## 📋 Course Schedule
Weekly one-on-one meetings; assigned readings and a lecture video before each meeting, a short exercise after. Each topic is paired with an application to extreme-weather / waterborne-disease data.

| Week | Dates | Meeting | Topic |
|------|-------|---------|-------|
| 1  | 8/24 – 8/29 | — | No meeting |
| 2  | 8/30 – 9/5  | 9/2  | Overview of statistical / machine learning |
| 3  | 9/6 – 9/12  | 9/9  | Unsupervised learning: principal components analysis & clustering |
| 4  | 9/13 – 9/19 | 9/16 | Classification via logistic regression through the lens of statistical / machine learning |
| 5  | 9/20 – 9/26 | 9/23 | Linear & quadratic discriminant analysis; comparing classification methods |
| 6  | 9/27 – 10/3 | 9/30 | Resampling methods: cross-validation & bootstrapping |
| 7  | 10/4 – 10/10 | 10/7 | Linear & logistic model selection: subset selection & shrinkage methods |
| 8  | 10/11 – 10/17 | 10/14 | Dimension reduction & dealing with high-dimensional predictors |
| 9  | 10/18 – 10/24 | 10/21 | Extending linear models: basis functions, splines & GAMs |
| 10 | 10/25 – 10/31 | 10/28 | Tree-based methods I &nbsp;·&nbsp; **Literature review due** |
| 11 | 11/1 – 11/7 | 11/4  | Tree-based methods II |
| 12 | 11/8 – 11/14 | 11/11 | Support vector machines |
| 13 | 11/15 – 11/21 | 11/18 | Introduction to neural networks |
| 14 | 11/22 – 11/28 | — | No meeting (Thanksgiving break) |
| 15 | 11/29 – 12/5 | 12/2 | Algorithmic fairness &nbsp;·&nbsp; **Article critique due** |
| 16 | 12/6 – 12/8 | — | No meeting &nbsp;·&nbsp; **Write-up on chosen method due** |

### Graded deliverables
| Deliverable | Due |
|-------------|-----|
| Literature review — factors related to waterborne-disease transmission risk after extreme weather events | Oct 30 (Week 10) |
| Article critique — student's choice of paper | Dec 2 (Week 15) |
| Write-up — choosing an appropriate ML method for a prediction model | Dec 8 (Week 16) |

## 📂 Repository Materials
All materials — datasets, exercises, and answer keys — are organized by week. Clone the repository with:

```sh
git clone https://github.com/xindyhu/pubh6010-statistical-machine-learning.git
```

Each week's folder contains the student handout (`*_exercise_*.Rmd`), the data and its data dictionary, and, for the instructor, an answer key and pre-rendered figures. Open the week's `.Rproj` first so relative paths resolve.

> **Note for the instructor:** answer-key files are kept in the repo during preparation and should be removed from the copy shared with the student before each release.

## 🤝 Contributors
Instructor: **Xindi (Cindy) Hu, ScD**
Student: **Katie O'Brien**, PhD candidate
Contact: **xindi.hu@gwu.edu**

---
Happy learning! 📈🤖
