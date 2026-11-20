# Lecture 13 Exercise — Neural Networks

PubH 6010 Independent Study (Fall 2026), Week 13. Companion to PUBH 6886 Lecture 13.

You will fit feedforward neural networks (one hidden layer, `nnet`) to **Guo, Liu & Chen (2021)**: daily all-cause deaths in Taipei, 2012–2016, predicted from 31 days of lagged temperature, O3, PM2.5 and calendar terms. You will compare three ways to cross-validate a time series (random, blocked and forward-chaining), benchmarks the networks against a Poisson GLM with a DLNM cross-basis, and looks at what the network learned. 

## Files

| File | What it is |
|---|---|
| `lecture13_exercise_nn.Rmd` / `.html` | **Start here.** Reading, tasks (Parts A–E, Q1–Q5), starter code (tested), numbers to check against |
| `pone.0244094.s001.csv` | The paper's S1 File: 1,818 days × 17 columns (date, deaths, temperature, 5 pollutants, weekday indicators). PLOS ONE, CC BY |
| `lecture13.Rproj` | RStudio project |
| `answer_key/` | Instructor key (`.Rmd`, `.R`, `.html`). **Do not commit** (it is in `.gitignore`) |

**Software:** tidyverse, tidymodels, nnet, NeuralNetTools, dlnm (all CRAN). The starter code runs in about 3 minutes and the key in about 4, most of it the tuning in Task 7.

## Paper

Guo C-Y, Liu T-W, Chen Y-H. A novel cross-validation strategy for artificial neural networks using distributed-lag environmental factors. *PLOS ONE* 2021;16(1):e0244094. doi:10.1371/journal.pone.0244094.

## Mapping to the slides

| Part | Slides | Task |
|---|---|---|
| A | — (Week 9 GLM, plus distributed lags) | Table 1, missing days, the 70/30 split, trivial baselines, Poisson GLM + DLNM benchmark |
| B | Regression example (`nnet`, `plotnet`); parameters, cost, gradient descent, local minima | One 51-5-1 network; raw vs standardized outcome; weight count; 5 random starts |
| C | Validation (k-fold CV for tuning); weight penalization | Tune size × decay under random, blocked and forward-chaining CV; optimism of each |
| D | Drawbacks (black box); attribution | Test-set comparison with linear regression and the GLM; block permutation importance; sustained-temperature curve vs DLNM |
| E | — | Critique of the paper; implications for waterborne-illness project |
