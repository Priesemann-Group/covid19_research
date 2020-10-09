import sys

sys.path.append("../../toolbox/master")

import covid19_inference as cov19
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Validation of number of deaths with other repository
rki = cov19.data_retrieval.RKI()
begin = datetime.datetime(2020, 7, 15)
data_cases = rki.get_new("confirmed", data_begin=begin,)
data_deaths = rki.get_new("deaths", data_begin=begin,)
cases_weeks = []
deaths_week = []

# New cases
summ = 0
for date, cases in data_cases.iteritems():
    summ += cases
    if date.weekday() == 6:
        cases_weeks.append(summ)
        summ = 0
kws_1 = list(range(29, 29 + len(cases_weeks)))


# Deaths
summ = 0
for date, cases in data_deaths.iteritems():
    summ += cases
    if date.weekday() == 6:
        deaths_week.append(summ)
        summ = 0
kws_2 = list(range(29, 29 + len(deaths_week)))


# Plot
width = 0.35  # the width of the bars
clr_left = "tab:blue"
clr_right = "tab:red"

fig, axes = plt.subplots(1, 2, figsize=(6, 3))

axes[0].bar(np.array(kws_1) - width / 2, cases_weeks, width, color=clr_left)
axes[0].set_ylabel("Cases", color=clr_left)

axes[1].bar(np.array(kws_2) + width / 2, deaths_week, width, color=clr_right)
axes[1].set_ylabel("Deaths", color=clr_right)
# Colored ticks
axes[0].tick_params(axis="y", labelcolor=clr_left)
axes[1].tick_params(axis="y", labelcolor=clr_right)
axes[0].set_xlabel("KW")
axes[1].set_xlabel("KW")

plt.show()

# 2. IFR validation weighted for agegroups
def f(a):
    if a <= 100:
        return 0.1 * 10 ** (1 / 20 * (a - 82))
    else:
        return 0.6


# Read age data
pop = pd.read_csv("population.csv")

pop = pop.set_index("age")

ratios = pop / pop.sum()

x = []
for age in pop.index:
    x.append(f(age) * ratios.loc[age].values[0])

print(f"IFR_eff = {sum(x)*100}")
