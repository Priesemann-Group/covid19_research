"""
Trying to reproduce https://arxiv.org/pdf/2006.05532.pdf
"""


import sys
sys.path.append("../../../covid19_inference/")
import covid19_inference as cov19
import matplotlib.pyplot as plt
import matplotlib
import datetime

owd = cov19.data_retrieval.OWD(True)
jhu = cov19.data_retrieval.JHU(True)
countries = ["Austria",
    "Belgium",
    "Croatia",
    #"Czech Republic",
    "Denmark",
    "Estonia",
    "Finland",
    #"France",
    "Greece",
    "Italy",
    #"Ireland",
    "Lithuania",
    "Latvia",
    #"Netherlands",
    "Norway",
    "Poland",
    "Portugal",
    "Serbia",
    "Slovakia",
    #"Spain",
    "Slovenia",
    #"Sweden",
    "Switzerland",
    "United Kingdom"]


"""
Fig 1 for every country
"""

clr_left= "tab:blue"
clr_right = "tab:red"
data_begin = datetime.datetime(2020,2,10)
data_end = datetime.datetime.today()-datetime.timedelta(days=3)


for country in countries:
    fig, axes = plt.subplots(2,1,figsize=(12,9))
    total_tests_daily = owd.get_new("tests",country,data_begin=data_begin,data_end=data_end)
    total_pos_daily = jhu.get_new("confirmed",country,data_begin=data_begin,data_end=data_end)
    
    # ------------------------------------------------------------------------------ #
    # Plot fig1
    # ------------------------------------------------------------------------------ #
    ax2 = axes[0].twinx()
    cov19.plot._timeseries(
        x=total_tests_daily.index,
        y=total_tests_daily,
        ax=axes[0],
        color=clr_right,
        what="model")
    cov19.plot._timeseries(
        x=total_pos_daily.index,
        y=total_pos_daily,
        ax=ax2,
        color=clr_left,
        what="model")

    # Colored ticks
    axes[0].tick_params(axis='y',labelcolor=clr_left)
    ax2.tick_params(axis='y',labelcolor=clr_right)

    # Get min max values for y_lim
    x_min = total_tests_daily.index.min()
    x_max = total_tests_daily.index.max()
    axes[0].set_xlim(x_min,x_max)
    ax2.set_xlim(x_min,x_max)

    # Set title and axis label
    axes[0].set_ylabel("Total tests performed",color=clr_left)
    ax2.set_ylabel("Total positive tests",color=clr_right)

    axes[0].set_title(f"Trying to reproduce Fig1 and Fig2 from 2006.05532 for \n {country} ")

    # ------------------------------------------------------------------------------ #
    # Plot fig2
    # ------------------------------------------------------------------------------ #
    total_negativ_daily = total_tests_daily-total_pos_daily
    cov19.plot._timeseries(
        x=total_pos_daily.index,
        y=total_pos_daily/total_negativ_daily,
        ax=axes[1],
        color=clr_left,
    )

    # Set logscale
    axes[1].set_yscale('log')
    axes[1].set_xlim(x_min,x_max)
    axes[1].set_ylim(1e-4,1.5)
    axes[1].set_ylabel(r"$tests_{pos}/tests_{neg}$")

    plt.savefig("./figures/reproduce_2006.05532/"+country+".pdf",dpi=300,transparent=True)