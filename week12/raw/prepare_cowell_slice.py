"""Build cowell_ec_lead1.csv (Week 12 SVM homework) from the authors' CB_bulk_dataset.csv.

This is a line-by-line port of load_data() and drop_lead_time_vars() in beach_model.py
(github.com/rtsearcy/wq-forecasting), run for beach = Cowell, FIB = EC, train 2007-2012,
test 2013-2014. It reproduces Table S5 of the SI exactly (train 290 samples / 85 exceedances,
test 94 / 20). The paper's pipeline decides which ROWS survive (rows with a missing value in
any retained predictor are dropped); we then keep 10 fixed predictors, the ten most often
selected for Cowell E. coli in SI Table S6, instead of the paper's RFECV variable selection.

Usage:  python3 raw/prepare_cowell_slice.py CB_bulk_dataset.csv   (run from week12_svm/)
"""
import sys
import numpy as np
import pandas as pd
from sklearn.feature_selection import VarianceThreshold

path = sys.argv[1]
fib = 'EC'
fib_thresh = {'EC': 400, 'ENT': 104}
train_years = list(range(2007, 2013))
test_years = [2013, 2014]
miss_allow = 0.15
keep_vars = []

df = pd.read_csv(path, index_col=['date'], parse_dates=['date'])
df = df[df.index.year.isin(list(range(min(train_years), max(test_years) + 1)))]
dep_var = fib + '_exc'

drop_list = []
drop_default = [v for v in df.columns if any(x in v for x in ['sample_time', 'MWD', 'wdensity', 'rad0', 'atemp0', 'upwell'])] + \
    [v for v in df.columns if any(x in v for x in ['rain', 'flow', 'chl', 'turb']) and (('log' not in v) and ('q75' not in v))]
drop_list += drop_default
for f in [f for f in fib_thresh if f != fib]:
    drop_list += [v for v in df.columns if f in v]
drop_list += [v for v in df.columns if (fib in v) and (v != dep_var) and (v not in keep_vars)]
drop_same_day = [v for v in df.columns if (not any(ch.isdigit() for ch in v))
                 and not any(x in v for x in ['tide', 'doy', 'dow', 'month', 'weekend'])
                 and (fib not in v)] + ['wspd_q75', 'WVHT_q75', 'DPD_q75', 'chl_q75', 'turb_q75']
drop_list += [v for v in drop_same_day if v not in drop_list]
df = df[[c for c in df if c not in drop_list]]

vt = VarianceThreshold().fit(df)
zero = list(df.columns[vt.variances_ == 0])
print('zero variance:', zero)
df = df[[c for c in df.columns if c not in zero]]

# check_corr
def check_corr(dep, ind, thresh=0.9, method='spearman'):
    c = ind.corr()
    to_drop = []
    for ii in c.columns:
        temp = c.loc[ii]
        temp = temp[temp.abs() > thresh].drop(ii, errors='ignore')
        i_corr = dep.corr(ind[ii], method=method)
        if len(temp) > 0:
            for j in temp.index:
                j_corr = dep.corr(ind[j], method=method)
                if ii not in to_drop and abs(i_corr) < abs(j_corr):
                    to_drop.append(ii)
    return to_drop

drop_corr = check_corr(df[dep_var], df[[v for v in df.columns if v != dep_var]])
print('dropped corr:', len(drop_corr))
df = df[[c for c in df if c not in drop_corr]]

df = df.dropna(subset=[dep_var])
miss_frac = df.isnull().sum() / len(df)
drop_missing = [c for c in miss_frac[miss_frac > miss_allow].index if c != dep_var]
print('dropped missing:', drop_missing)
df = df.drop(drop_missing, axis=1)
n0 = len(df)
df = df.dropna(axis=0)
print('rows dropped for NA:', n0 - len(df))

tr = df[df.index.year.isin(train_years)]
te = df[df.index.year.isin(test_years)]
print('TRAIN', len(tr), int(tr[dep_var].sum()), ' TEST', len(te), int(te[dep_var].sum()))

# lead time 1
def drop_lead_time_vars(d, lead_time):
    dl = []
    if lead_time >= 1:
        dl += [v for v in d.columns if ('1' in v) and ('tide' not in v) and ('T' not in v)] + ['WVHT1', 'WVHT_q75_1']
        dl += ['lograin2T', 'lograin3T', 'lograin4T', 'lograin5T', 'lograin6T', 'lograin7T', 'lograin14T', 'lograin30T'] + \
            [v for v in d.columns if 'lograin1_' in v]
    return d[[c for c in d if c not in dl]]

X = drop_lead_time_vars(df.drop(columns=dep_var), 1)
print('lead-1 predictors (', X.shape[1], '):')
print(sorted(X.columns))
# ---- the homework slice: paper's rows, 10 fixed predictors (SI Table S6, CB-EC column) ----
raw = pd.read_csv(path, index_col=['date'], parse_dates=['date'])
v = ['lograin6', 'logflow4', 'WVHT4', 'APD2', 'APD3', 'APD4', 'APD5', 'tide_max4', 'rad4', 'atemp_min5']
assert all(c in X.columns or c in raw.columns for c in v)
s = raw.loc[df.index, ['EC', 'EC_exc'] + v].copy()
assert s.notna().all().all()
s.insert(0, 'split', ['train' if y <= 2012 else 'test' for y in s.index.year])
s.insert(0, 'year', s.index.year)
s['EC_exc'] = s.EC_exc.astype(int)
assert ((s.EC > 400).astype(int) == s.EC_exc).all()
s = s.reset_index()
s['date'] = s.date.dt.strftime('%Y-%m-%d')
s.to_csv('cowell_ec_lead1.csv', index=False)
print('wrote cowell_ec_lead1.csv', s.shape)
