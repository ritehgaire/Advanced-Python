import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1: 
lam = 7

## Task 2:
pmf_at_lam = stats.poisson.pmf(lam, lam)

## Task 3:
cdf_4 = stats.poisson.cdf(4, lam)

## Task 4:
prob_more_than_9 = 1 - stats.poisson.cdf(9, lam)

### Task Group 2 ###
## Task 5:
year_defects = stats.poisson.rvs(lam, size=365)

## Task 6:
first_20_defects = year_defects[0:20]

## Task 7:
expected_yearly_defects = lam * 365

## Task 8:
total_yearly_defects = sum(year_defects)

## Task 9:
mean_yearly_defects = np.mean(year_defects)

## Task 10:
max_daily_defects = year_defects.max()

## Task 11:
prob_of_max_defects = 1 - stats.poisson.cdf(max_daily_defects, lam)

### Extra Bonus ###
## Task 12
quantile_90th = stats.poisson.ppf(0.9, lam)

## Task 13
proportion_above_90th = sum(year_defects >= quantile_90th) / len(year_defects)

results = {
    "PMF at λ": pmf_at_lam,
    "CDF for 4 defects": cdf_4,
    "Probability of more than 9 defects": prob_more_than_9,
    "First 20 generated daily defects": first_20_defects,
    "Expected yearly defects": expected_yearly_defects,
    "Total yearly defects": total_yearly_defects,
    "Mean yearly defects": mean_yearly_defects,
    "Maximum daily defects": max_daily_defects,
    "Probability of observing more defects than the maximum": prob_of_max_defects,
    "90th percentile (quantile)": quantile_90th,
    "Proportion of days with defects >= 90th percentile": proportion_above_90th
}

import ace_tools as tools; tools.display_dataframe_to_user(name="Poisson Distribution Analysis Results", dataframe=pd.DataFrame.from_dict(results, orient='index', columns=['Value']))
