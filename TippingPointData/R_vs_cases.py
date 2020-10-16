# ------------------------------------------------------------------------------ #
# @Author:        Sebastian B. Mohr
# @Email:
# @Created:       2020-10-14 11:10:57
# @Last Modified: 2020-10-16 11:04:43
# ------------------------------------------------------------------------------ #
import sys
import pandas as pd
import numpy as np
import datetime

sys.path.append("../toolbox/master")
import covid19_inference as cov19

rki = cov19.data_retrieval.RKI(True)

# Population by landkreis
sys.path.append("../SurvStat_RKI/")
from Landkreise import Landkreise

lkr = Landkreise("../SurvStat_RKI/risklayer_kreise.csv")
data = rki.data
data = data.set_index(
    [
        "Landkreis",
        "IdLandkreis",
        "Altersgruppe",
        "date",
        "date_ref",
        "Bundesland",
        "IdBundesland",
    ]
)
data = data.drop(columns=["Altersgruppe2", "FID", "Datenstand", "Geschlecht"])
data = data["confirmed"]  # Ist Erkrankungsbegin?


def RKI_R(infected_t, window=14, gd=4):
    """ Calculate R value as published by the RKI on 2020-05-15
    in 'Erkäuterung der Schätzung der zeitlich variierenden Reproduktionszahl R'

    infected: Timeseries or trace, in general: last index is considered to calculate R
    window: averaging window, average over 4 days is default
    """
    r = np.zeros(infected_t.shape)  # Empty array with the same shape as Timeseries

    if window == 1:
        r[..., gd:] = infected_t[..., gd:] / infected_t[..., :-gd]
    else:
        if window == 7:
            offset = 1
        elif window == 4:
            offset = 0
        else:
            offset = 0
        for t in range(window + gd, infected_t.shape[-1] - offset):
            # NOTE: R7_Wert[t-1] <- sum(data$NeuErk[t-0:6]) / sum(data&NeuErk[t-4:10])
            # Indexing in R (the stat-language) is inclusive, in numpy exclusive: upper boundary in sum is increased by 1

            right_block = infected_t[..., t - window : t]
            left_block = infected_t[..., t - window - gd : t - gd]

            r[..., t - 1 - offset] = np.sum(right_block, axis=-1) / np.sum(
                left_block, axis=-1
            )

    # mask of R_values that were not calculated to match time-index of output to input
    return np.ma.masked_where((r == 0) | np.isinf(r) | np.isnan(r), r)


def Landkreise():
    # Confirmed cases save
    data_l = pd.DataFrame()
    ratio = pd.DataFrame()
    for landkreis in data.index.get_level_values("Landkreis").unique():
        data_l[landkreis] = (
            data.xs(landkreis, level="Landkreis").groupby("date").sum() + 0.1
        )

        # Calc ratio 100.000 i.e pop/100000 * cases

        # get id by name
        for key, value in lkr.lkrNames.items():
            if value == landkreis:
                ratio[landkreis] = 100000 * data_l[landkreis] / lkr.lkrN[key]
                continue
            if landkreis == "LK Göttingen (alt)":  # Expetion
                ratio[landkreis] = 100000 * data_l[landkreis] / lkr.lkrN[3159]
                continue

    # Expand so each day is in the data and fill nans with 0
    data_l = data_l.asfreq("D")
    data_l = data_l.fillna(0)
    ratio = ratio.asfreq("D")
    ratio = ratio.fillna(0)
    ratio = ratio.rolling(window=14).mean() * 7

    # Calc R
    data_R = pd.DataFrame()
    for landkreis in data_l.columns:
        data_masked = data_l[data_l.rolling(window=7).sum() > 20]
        data_R[landkreis] = RKI_R(data_masked[landkreis].to_numpy())
    data_R.index = data_l.index

    # Sum over weeks calc mean for ratio per 100000
    weekly_cases = data_l.resample("W-Sun").sum()
    weekly_ratio = ratio.resample("W-Sun").mean()
    weekly_R = data_R.resample("W-Sun").mean()

    # Calc R weekly

    # R = R / R.max()

    # Create one big dataframe:
    # ratio - R

    # Plotting
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 1, figsize=(12, 9))

    begin = datetime.datetime(2020, 8, 2)
    end = datetime.datetime(2020, 10, 12)
    # Daily cases
    axes[0].plot(ratio[begin:end], data_R[begin:end], "d-")
    axes[0].set_xlabel(
        f"Cases per 100.000\nfrom {begin.strftime('%m-%d')} to {datetime.date.today().strftime('%m-%d')}"
    )
    # axes[0].set_ylabel("R\n(window of 7 days, generation duration of 4 days)")
    axes[0].set_xlim(0, 80)
    axes[0].set_ylim(0.25, 2.25)

    # Weekly cases

    # Daily cases
    axes[1].plot(weekly_ratio[begin:end], weekly_R[begin:end], "d-")
    axes[1].set_xlabel(
        f"Weekly cases per 100.000\nfrom {begin.strftime('%m-%d')} to {datetime.date.today().strftime('%m-%d')}"
    )
    # axes[1].set_ylabel("R\n(window of 7 days, generation duration of 4 days)")
    axes[1].set_xlim(0, 80)
    axes[1].set_ylim(0.25, 2.25)

    fig.text(
        0.06,
        0.5,
        "R\n(window of 7 days, generation duration of 4 days)",
        ha="center",
        va="center",
        rotation="vertical",
    )

    fig.show()

    # Correlation

    import scipy

    x = []
    y = []
    for landkreis in ratio.columns:
        x.append(data_R[landkreis].to_numpy().flatten())
        y.append(ratio[landkreis].to_numpy().flatten())
    x = np.array(x).flatten()
    y = np.array(y).flatten()

    df = pd.DataFrame()
    df["x"] = x
    df["y"] = y
    df["y"] = df["y"][df["y"] > 0.3]
    df = df[df < 1e12].dropna()

    x = df["x"].to_numpy()
    y = df["y"].to_numpy()

    print(scipy.stats.pearsonr(x, y))
    plt.savefig("R_vs_cases_landkreise.png", dpi=300)


def Bundeslaender():
    pop = {
        "Baden-Württemberg": 11100394,
        "Bayern": 13124737,
        "Berlin": 3669491,
        "Brandenburg": 2521893,
        "Bremen": 681202,
        "Hamburg": 1847253,
        "Hessen": 6288080,
        "Mecklenburg-Vorpommern": 1608138,
        "Niedersachsen": 7993608,
        "Nordrhein-Westfalen": 17947221,
        "Rheinland-Pfalz": 4093903,
        "Saarland": 986887,
        "Sachsen": 4071971,
        "Sachsen-Anhalt": 2194782,
        "Schleswig-Holstein": 2903773,
        "Thüringen": 2133378,
    }
    # Confirmed cases save
    data_b = pd.DataFrame()
    ratio = pd.DataFrame()
    for bundesland in data.index.get_level_values("Bundesland").unique():
        data_b[bundesland] = (
            data.xs(bundesland, level="Bundesland").groupby("date").sum() + 0.1
        )

        # Calc ratio 100.000 i.e pop/100000 * cases
        ratio[bundesland] = 100000 * data_b[bundesland] / pop[bundesland]

    # Expand so each day is in the data and fill nans with 0
    data_b = data_b.asfreq("D")
    data_b = data_b.fillna(0)
    ratio = ratio.asfreq("D")
    ratio = ratio.fillna(0)
    ratio = ratio.rolling(window=14).mean() * 7
    # ratio = ratio[data_l.rolling(window=7).sum() > 20]

    # Calc R
    data_R = pd.DataFrame()
    for bundesland in data_b.columns:
        # data_masked = data_l[data_l.rolling(window=7).sum() > 20]
        data_R[bundesland] = RKI_R(data_b[bundesland].to_numpy())
    data_R.index = data_b.index

    # Sum over weeks calc mean for ratio per 100000
    weekly_cases = data_b.resample("W-Sun").sum()
    weekly_ratio = ratio.resample("W-Sun").mean()
    weekly_R = data_R.resample("W-Sun").mean()

    # Calc R weekly

    # R = R / R.max()

    # Create one big dataframe:
    # ratio - R

    # Plotting
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 1, figsize=(12, 9))

    begin = datetime.datetime(2020, 8, 2)
    end = datetime.datetime(2020, 10, 12)

    # Daily
    axes[0].plot(ratio[begin:end], data_R[begin:end], "d-")
    axes[0].set_xlabel(
        f"Daily cases per 100.000\nfrom {begin.strftime('%m-%d')} to {datetime.date.today().strftime('%m-%d')}"
    )
    # axes[0].set_ylabel("R\n(window of 7 days, generation duration of 4 days)")
    axes[0].set_xlim(0, 80)
    axes[0].set_ylim(0.25, 2.25)

    # Weekly

    axes[1].plot(weekly_ratio[begin:end], weekly_R[begin:end], "d-")
    axes[1].set_xlabel(
        f"Weekly cases per 100.000\nfrom {begin.strftime('%m-%d')} to {datetime.date.today().strftime('%m-%d')}"
    )
    # axes[0].set_ylabel("R\n(window of 7 days, generation duration of 4 days)")
    axes[1].set_xlim(0, 80)
    axes[1].set_ylim(0.25, 2.25)

    fig.text(
        0.06,
        0.5,
        "R\n(window of 7 days, generation duration of 4 days)",
        ha="center",
        va="center",
        rotation="vertical",
    )

    plt.savefig("R_vs_cases_bundesländer.png", dpi=300)


if __name__ == "__main__":
    Bundeslaender()
    Landkreise()
