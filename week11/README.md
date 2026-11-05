# Lectures 10–11 Exercise — Trees, Bagging, Random Forests and Boosting

PubH 6010 Independent Study (Fall 2026), Week 11. Companion to PUBH 6886 Lectures 10 and 11.

This week, we replicate **Lombard et al. (2021)**, a national model of arsenic in US private wells built for exposure assessment in health studies. 

## Files

| File | What it is |
|---|---|
| `lecture10_11_exercise_trees.Rmd` / `.html` | **Start here.** Reading, tasks (Parts A–E, Q1–Q5), starter code (tested), numbers to check against |
| `AsModelInput.csv` | 20,450 private wells × 93 columns: outcomes `bas1/5/10` and `As3Cat`, split flags `spl1/5/10/3cat`, and 85 predictors. USGS data release doi:10.5066/P90RBJXS |
| `Model_input_definitions.csv`, `Model_input_sources.csv` | Variable definitions and sources, from the same release (see the data notes below) |
| `lecture10_11.Rproj` | RStudio project |

The paper PDF is not included (doi:10.1021/acs.est.0c05239).

**Software:** tidyverse, tidymodels, `gbm`, `rpart`, `rpart.plot`, `ranger`, `xgboost`, `probably` (all CRAN). The key runs in about 16 minutes on 2 cores. Most of that is the `gbm()` fit (~4 min), the CART and xgboost grids (~3 min each) and about 30 ranger fits.

## Paper

Lombard MA, Scannell Bryan M, Jones DK, Bulka C, Bradley PM, Backer LC, Focazio MJ, Silverman DT, Toccalino P, Argos M, Gribble MO, Ayotte JD. Machine learning models of arsenic in private wells throughout the conterminous United States as a tool for exposure assessment in human health studies. *Environ Sci Technol.* 2021;55(8):5012–5023. doi:10.1021/acs.est.0c05239

## Mapping to the slides

| Part | Slides | Task |
|---|---|---|
| A | L11 4–7, 13–15 | Replicate BRT10 with `gbm()` and the paper's settings on the paper's split; compare with Table 1; "always no" and logistic baselines |
| B | L10 25–37 | Maximal `rpart` tree, CV for cp (best and 1-SE), accuracy vs AUC as the criterion, a small interpretable tree, bootstrap instability |
| C | L10 38–53 | OOB error vs B for bagging and RF; OOB across mtry; replicate the 3-class RFC (training vs OOB vs test accuracy) |
| D | L11 7, 18–21 | `boost_tree()` + xgboost grid over trees × depth × learning rate; a final test-set table of all six methods |
| E | L11 8–10 | gbm influence vs RF impurity vs permutation importance; PDP for precipitation; choosing the cutoff on OOB predictions |
