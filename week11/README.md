# Lectures 10–11 Exercise — Trees, Bagging, Random Forests and Boosting

PubH 6010 Independent Study (Fall 2026), Week 11. Companion to PUBH 6886 Lectures 10 and 11.

Katie replicates **Lombard et al. (2021)**, a national model of arsenic in US private wells built for exposure assessment in health studies. The paper fits boosted regression trees (BRT, `gbm`) for arsenic > 1, 5 and 10 µg/L and a 3-class random forest. The data file contains the paper's own train/test split, so Katie can compare her numbers directly with Table 1. She then fits a single pruned classification tree, compares bagging with random forests, tunes boosting with tidymodels (xgboost), and finishes with variable importance, partial dependence and the choice of a probability cutoff. 5 questions.

## Files

| File | What it is |
|---|---|
| `lecture10_11_exercise_trees.Rmd` / `.html` | **Start here.** Reading, tasks (Parts A–E, Q1–Q5), starter code (tested), numbers to check against |
| `AsModelInput.csv` | 20,450 private wells × 93 columns: outcomes `bas1/5/10` and `As3Cat`, split flags `spl1/5/10/3cat`, and 85 predictors. USGS data release doi:10.5066/P90RBJXS |
| `Model_input_definitions.csv`, `Model_input_sources.csv` | Variable definitions and sources, from the same release (see the data notes below) |
| `lecture10_11.Rproj` | RStudio project |
| `answer_key/` | Instructor key (`.Rmd`, `.R`, `.html`). **Do not commit** (it is in `.gitignore`) |

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

## Key results (answer key)

- **The replication is essentially exact.** BRT10 test accuracy / sensitivity / specificity / AUC / kappa = 0.912 / 0.336 / 0.981 / 0.855 / 0.409. The paper's Table 1 gives 0.912 / 0.339 / 0.982 / 0.850 / 0.413. Training metrics also match to within 0.01.
- **The paper's accuracy is close to the baseline.** Prevalence is 10.8%, so "always no" scores 89.2%. At the 0.5 cutoff the model misses two-thirds of the wells above the MCL.
- **3-class RF replicates as well.** Test accuracy is 0.829 and kappa 0.399 (paper 0.826 / 0.392). The paper's 100% training accuracy is resubstitution of fully grown trees; we get 99.9% training vs 82.6% OOB. C2 (5–10 µg/L) recall is 12%.
- **Method ranking.** Test AUC is 0.795 for logistic regression, 0.79 for the best single tree, 0.850 for bagging, 0.856 for RF (m = 20), 0.855 for gbm and 0.854 for tuned xgboost. All four ensembles are within noise of each other (SE ≈ 0.008). The real gains are ensemble vs single tree and vs main-effects logistic.
- **CART.** The root split is precipitation < 408 mm/yr. The 1-SE rule on accuracy keeps 31 leaves, while CV AUC wants about 200. On bootstrap resamples the root switches between precipitation, soil As and soil Sb (Spearman correlation of As and Sb = 0.69).
- **RF.** OOB AUC peaks at m ≈ 6–9 (≈ √p). Bagging is worse because the correlated soil-geochemistry predictors give correlated trees.
- **Boosting.** At ν = 0.1 CV AUC falls as B grows (overfitting). At ν = 0.01 it is still rising at 2,000 trees. Depth 6 beats stumps by about 0.04 AUC, which is evidence of interactions.
- **Importance and PDP.** Precipitation ranks first by every measure. The lateral-position variables (`LP4`, `LP6`) rank high by impurity and low by permutation, which is the impurity bias. The partial dependence is P ≈ 0.24 at 200 mm/yr falling to ≈ 0.08–0.10 above about 800 mm, and the raw decile proportions show the same.
- **Cutoff.** The Youden-optimal cutoff on OOB predictions is 0.13. On the test set it gives sensitivity 0.72, specificity 0.82 and PPV 0.33, with 24% of wells flagged (vs sensitivity 0.39 at 0.5).

## Instructor notes (also good material for the Dec 4 article critique)

- **Problems in the data files (the handout warns Katie about each).**
  - `DMppt8110` is labelled inches but is in mm.
  - The `p_c` and `orgc_c` descriptions are swapped.
  - C3 is "≥ 10" while `bas10` is "> 10", which puts 174 wells at exactly 10 µg/L in C3 with `bas10 = 0`.
- **The "user's" and "producer's" accuracy labels in the paper's Table 1 appear to be swapped.** Our per-class recall matches the paper's "user's" accuracy and our precision matches its "producer's" accuracy. Standard remote-sensing usage is the reverse. Q3 asks Katie to find this. Worth checking against the SI before stating it as an error.
- **Validation is optimistic for the paper's mapping use.** The 30% test set is a random sample of wells, not spatially blocked, and the public file has no coordinates, so this can't be fixed here. Same lesson as Week 9's random-fold CV.
- **Dichotomising at 0.5 for exposure assessment** flags only about a third of exceedances. The paper reports this honestly, but the abstract leads with accuracy. The health-study use (Q5) is the point to press.
- **Precipitation is a 30-year climate normal, not a weather exposure.** [Interpretation: it proxies arid hydrogeochemistry (evaporative concentration, high-pH desorption).] Q5 asks Katie to say why this does not transfer to her extreme-weather question.
- **Deviations from the paper.**
  - We use all 85 predictors. The paper's final models keep 41–65 each (SI Tables SI_3/SI_4, not in the data release).
  - 27 wells with a missing predictor are dropped.
  - `bag.fraction` is not reported in the paper; we use gbm's default of 0.5.
  - The RF uses ranger with `min_n = 1`, to match randomForest's `nodesize = 1`. parsnip's ranger default (probability forest, min node size 10) gives 94% training accuracy rather than 100%.
- **gbm vs xgboost.** `interaction.depth` (number of splits) is not `tree_depth` (depth, up to 2^d leaves). Q4 asks about this.
- **5-fold rather than 10-fold CV** for the tidymodels grids, to keep runtime down. The `rpart` cptable uses its built-in 10-fold CV, as on the slides.
- Numbers were produced with R 4.4.3, tidymodels 1.4.1, parsnip 1.6.1, tune 2.1.0, gbm 2.3.1, ranger 0.18.0, xgboost 3.4.2.1 and rpart 4.1.27. Stochastic results depend on `set.seed(1234)` and ranger's `seed = 1234`. Small differences on Katie's machine (other package versions, more threads) are expected.
