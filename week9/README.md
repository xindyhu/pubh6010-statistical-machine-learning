# Lecture 09 Exercise — Polynomials, Step Functions and Splines

PubH 6010 Independent Study (Fall 2026). Companion to PUBH 6886 Lecture 09.

Katie replicates **Bhaskaran et al. (2013)**, a time-series analysis of London daily mortality, temperature and ozone. The paper models season with step functions, Fourier terms and a cubic B-spline. She then models the temperature–mortality curve with polynomials, step functions and regression splines, chooses df by 10-fold CV, and asks how much the paper's ozone estimate depends on those choices. The outcome is a **count**, so the models are quasi-Poisson `glm()` for estimates and tidymodels `poisson_reg()` for CV. CV uses **random folds**, as in the slides, and the handout carries a note on why blocked folds are correct practice for time series. 5 questions.

## Files

| File | What it is |
|---|---|
| `lecture09_exercise_splines.Rmd` / `.html` | **Start here.** Reading, tasks (Parts A–E, Q1–Q5), starter code (tested), numbers to check against |
| `londondataset2002_2006.dta` | London 2002–2006, 1,826 days × 5 variables (date, numdeaths, ozone, temperature, relative_humidity). From the authors' GitHub repo |
| `lecture09.Rproj` | RStudio project |

The paper PDF is not included. It is open access at doi:10.1093/ije/dyt092.

**Software:** tidyverse, `tidymodels`, `poissonreg`, `haven`, `tsModel` (all CRAN). The whole key runs in about 1 minute.

## Paper

Bhaskaran K, Gasparrini A, Hajat S, Smeeth L, Armstrong B. Time series regression studies in environmental epidemiology. *Int J Epidemiol.* 2013;42(4):1187–1195. doi:10.1093/ije/dyt092. Code and data: github.com/gasparrini/2013_bhaskaran_IJE_Codedata (archived at LSHTM Data Compass, record 969).

## Mapping to the slides

| Part | Slides | Task |
|---|---|---|
| A | 24–25, 30, 35–36 | Replicate Figure 2 (month strata, Fourier, bs(time, df = 35)) and the three ozone RRs |
| B | 16–28 | Temperature as polynomials (degree 1–4) and step functions (paper's deciles, 4 equal bins) |
| C | 29–39 | Linear, cubic and natural splines with a chosen knot; truncated power basis for the hockey stick |
| D | 40–47 | CV over df for ns / bs / polynomial; best vs 1-SE; selected bs vs ns with CIs |
| E | — | Ozone RR sensitivity to time-spline df × temperature model; what CV picks for the time spline |

## Key results (answer key)

- **Replication is exact.** Ozone RR per 10 µg/m³: 0.991 (0.987–0.994) unadjusted, 1.007 (1.003–1.010) with the time spline, 1.003 (0.999–1.006) with temperature deciles.
- **The heat tail is the August 2003 heatwave.** 4 of the 5 hottest days are 6–11 Aug 2003 (280 deaths on 10 Aug vs a median of 148), and only 6 days exceed 25 °C. The polynomial RR at 28 °C climbs from 1.45 to 1.82 as the degree goes from 2 to 4. The decile step function gives the same RR (1.11) to everything from 18.9 to 28.2 °C.
- **Splines.** A hockey stick with a knot at 18 °C gives +0.2%/°C below the knot and +3.7%/°C above it (3.2–4.2). At 28 °C the 1-knot cubic gives RR 1.90 with the widest CI, and the natural spline 1.46.
- **CV.** RMSE goes from 14.5 (linear) to ≈ 13.7 (best). The best choices are bs df = 5, ns df = 8 and polynomial degree 4; the 1-SE rule gives df = 3. Differences after df ≈ 4 are about 0.1 SE, so CV detects non-linearity but not its shape.
- **The ozone RR depends on the temperature model more than on the time df.** At 7 df/year it is 1.0027 with deciles and 0.9965–0.9985 with any flexible heat term (hockey stick, ns df 3 or 8). Ozone averages 68 µg/m³ on days > 22 °C vs 31 µg/m³ on days ≤ 15 °C, so the coarse top decile leaves heat confounding that is attributed to ozone.
- **Random-fold CV picks 12–15 df/year for the time spline**, about twice the paper's pre-specified 7, because it interpolates between neighbouring days. This is the prediction vs confounding-control point (Peng, Dominici & Louis 2006).
