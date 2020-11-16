"""
    # Small script to infere the reproduktion number between
    Mid July and mid oktober.

    Runtime ~ 1h
  
"""

## Importing modules
import datetime
import sys
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.stats
import theano
import theano.tensor as tt
import pymc3 as pm
import pickle
import logging

log = logging.getLogger(__name__)
from plot_scenarios import create_plot_scenarios
import matplotlib.lines as mlines
from construct_models import construct_model
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
import matplotlib.ticker as ticker

try:
    import covid19_inference as cov19
except ModuleNotFoundError:
    sys.path.append("../../toolbox/master")
    import covid19_inference as cov19


countries = {
    "Germany": {
        "data_begin": datetime.datetime(2020, 6, 13),
        "data_end": datetime.datetime(2020, 11, 1),
        "population": 83.02e6,
    },
    "Portugal": {
        "data_begin": datetime.datetime(2020, 6, 10),
        "data_end": datetime.datetime(2020, 11, 10),
        "population": 10.28e6,
    },
    "Switzerland": {
        "data_begin": datetime.datetime(2020, 6, 10),
        "data_end": datetime.datetime(2020, 11, 1),
        "population": 8.57e6,
    },
    "Italy": {
        "data_begin": datetime.datetime(2020, 6, 10),
        "data_end": datetime.datetime(2020, 11, 10),
        "population": 60.36e6,
    },
    "Belgium": {
        "data_begin": datetime.datetime(2020, 6, 10),
        "data_end": datetime.datetime(2020, 10, 27),
        "population": 11.46e6,
    },
    "Poland": {
        "data_begin": datetime.datetime(2020, 6, 10),
        "data_end": datetime.datetime(2020, 11, 10),
        "population": 37.97e6,
    },
    "Greece": {
        "data_begin": datetime.datetime(2020, 9, 19),
        "data_end": datetime.datetime(2020, 11, 8),
        "population": 10.72e6,
    },
}

try:
    # only works when called from python, not reliable in interactive ipython etc.
    os.chdir(os.path.dirname(__file__))
    save_to = "./figures/fig_"
except:
    # assume base directory
    save_to = "./figures/fig_"


## Download data
owd = cov19.data_retrieval.OWD()
owd.download_all_available_data(force_download=True)


# ------------------------------------------------------------------------------ #
# Big loop for every country
# ------------------------------------------------------------------------------ #
for c_name, conf in countries.items():

    # Load data for country
    new_cases_obs = owd.get_new(
        "confirmed",
        country=c_name,
        data_begin=conf["data_begin"],
        data_end=conf["data_end"],
    )
    if c_name == "Switzerland":
        new_cases_obs = owd._filter(
            "new_cases_smoothed",
            country="Switzerland",
            data_begin=conf["data_begin"],
            data_end=conf["data_end"],
        )
    total_cases_obs = owd.get_total(
        "confirmed",
        country=c_name,
        data_begin=conf["data_begin"],
        data_end=conf["data_end"],
    )

    # Construct change points
    change_points = [
        dict(
            pr_mean_date_transient=conf["data_begin"] - datetime.timedelta(days=1),
            pr_sigma_date_transient=1.5,
            pr_median_lambda=0.12,
            pr_sigma_lambda=0.5,
            pr_sigma_transient_len=0.5,
        ),
    ]
    log.info(f"Adding possible change points at:")
    for i, day in enumerate(
        pd.date_range(start=conf["data_begin"], end=conf["data_end"])
    ):
        if day.weekday() == 6 and (datetime.datetime.today() - day).days > 7:
            print(f"\t{day}")

            # Prior factor to previous
            change_points.append(
                dict(  # one possible change point every sunday
                    pr_mean_date_transient=day,
                    pr_sigma_date_transient=1.5,
                    pr_sigma_lambda=0.2,  # wiggle compared to previous point
                    relative_to_previous=True,
                    pr_factor_to_previous=1,
                )
            )

    model = construct_model(change_points, new_cases_obs, conf["data_begin"])
    trace = pm.sample(model=model, init="advi", tune=2000, draws=2000)

    with open(f"./traces/{c_name}.pickle", "wb") as f:
        pickle.dump((model, trace), f)

    # ------------------------------------------------------------------------------ #
    # Plotting
    # ------------------------------------------------------------------------------ #

    ## Timeseries
    fig, axes = create_plot_scenarios(
        model, trace, offset=total_cases_obs[0], population=conf["population"]
    )

    for ax in axes:
        ax.set_xlim(conf["data_begin"], conf["data_end"] + datetime.timedelta(days=5))
        ax.yaxis.set_major_formatter(
            matplotlib.ticker.FuncFormatter(_format_k(int(prec)))
        )
    ## Inset full data
    axins = axes[1].inset_axes(bounds=[0.2, 0.5, 0.55, 0.4])
    for line in axes[1].lines:
        axins.lines.append(line)
    new_cases_inset = (
        owd.get_new(
            "confirmed",
            country=c_name,
            data_begin=datetime.datetime(2020, 3, 2),
            data_end=datetime.datetime.today(),
        )
        .rolling(7)
        .mean()
        / conf["population"]
        * 1e6
    )
    cov19.plot._timeseries(
        x=new_cases_inset.index,
        y=new_cases_inset,
        ax=axins,
        what="model",
        color=cov19.plot.rcParams["color_data"],
    )
    ticks = axins.get_xticks()
    axins.set_xticks(ticks=[new_cases_inset.index.min(), new_cases_inset.index.max()])

    ## Format lambda to R rki
    axes[0].set_ylabel("Reproduction number\n $R$")
    axes[0].set_ylim(0.8, 1.4)
    fig.suptitle("")
    axes[0].xaxis.set_major_locator(
        mpl.dates.WeekdayLocator(interval=3, byweekday=mpl.dates.SU)
    )
    axes[1].xaxis.set_major_locator(
        mpl.dates.WeekdayLocator(interval=3, byweekday=mpl.dates.SU)
    )
    axes[2].xaxis.set_major_locator(
        mpl.dates.WeekdayLocator(interval=3, byweekday=mpl.dates.SU)
    )
    axes[1].set_ylabel("Reported cases per million")
    axes[2].remove()
    # save: ts for timeseries
    plt.savefig(
        save_to + c_name + "_ts.svg",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0.05,
        transparent=True,
    )
    plt.savefig(
        save_to + c_name + "_ts.png",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0.05,
        transparent=True,
    )

    ## Distributions
    num_rows = len(change_points) + 1
    num_columns = int(np.ceil(14 / 5))

    fig_width = 4.5 / 3 * num_columns
    fig_height = num_rows * 6 / 4

    fig, axes = plt.subplots(
        num_rows, num_columns, figsize=(fig_width, 4), constrained_layout=True
    )
    rows = [0, num_rows - 1, num_rows - 2]
    # Left row we want mu and all lambda_i!
    for i in rows:
        if i == 0:
            cov19.plot._distribution(model, trace, "mu", axes[0, 0])
        else:
            # Plot lambda_i and remove the xlable, we add one big label later.
            cov19.plot._distribution(
                model, trace, f"lambda_{i}", axes[-i + num_rows, 0]
            )
            axes[-i + num_rows, 0].set_xlabel("")
    # middle row
    for i in rows:
        if i == 0:
            cov19.plot._distribution(model, trace, "sigma_obs", axes[i, 1])
        else:
            # Plot transient_day_i and remove the xlable, we add one big label later.
            cov19.plot._distribution(
                model, trace, f"transient_day_{i}", axes[-i + num_rows, 1]
            )
            axes[-i + num_rows, 1].set_xlabel("")
    # right row
    for i in rows:
        if i == 0:
            # Create legend for everything
            axes[i, 2].set_axis_off()
            axes[i, 2].plot(
                [],
                [],
                color=cov19.plot.rcParams["color_prior"],
                linewidth=3,
                label="Prior",
            )
            axes[i, 2].hist(
                [], color=cov19.plot.rcParams["color_model"], label="Posterior"
            )
            axes[i, 2].legend(loc="center left")
            axes[i, 2].get_legend().get_frame().set_linewidth(0.0)
        else:
            # Plot transient_len_i and remove the xlable, we add one big label later.
            cov19.plot._distribution(
                model, trace, f"transient_len_{i}", axes[-i + num_rows, 2]
            )
            axes[-i + num_rows, 2].set_xlabel("")

    # Add ylabel for the first axes
    axes[0, 0].set_ylabel("Density")
    # Set bold xlabel for Spreading rates Change times and Change durations
    axes[1, 0].set_xlabel("Spreading rates", fontweight="bold")
    axes[1, 1].set_xlabel("Change times", fontweight="bold")
    axes[1, 2].set_xlabel("Change duration", fontweight="bold")

    # Letters
    letter_kwargs = dict(x=-0.3, y=1.1, size="x-large")
    axes[0, 0].text(s="C", transform=axes[0, 0].transAxes, **letter_kwargs)
    axes[1, 0].text(s="D", transform=axes[1, 0].transAxes, **letter_kwargs)

    # Conditional
    marker = mlines.Line2D(
        [],
        [],
        color=cov19.plot.rcParams["color_data"],
        marker="d",
        linestyle="None",
        markersize=6,
    )

    handles, labels = axes[0, 2].get_legend_handles_labels()
    handles.append(marker)
    labels.append("Data (OWD)")
    legend = axes[0, 2].get_legend()
    legend._legend_box = None
    legend._init_legend_box(handles, labels)
    legend._set_loc(legend._loc)
    legend.set_title(legend.get_title().get_text())

    # dist for distributions
    plt.savefig(
        save_to + c_name + "_dist.svg",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0.05,
        transparent=True,
    )
    plt.savefig(
        save_to + c_name + "_dist.png",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0.05,
        transparent=True,
    )


# ------------------------------------------------------------------------------ #
# Model Comparison
# ------------------------------------------------------------------------------ #
#
# comparison = pm.compare({mod_a: tra_a, mod_b: tra_b, mod_c: tra_c}, ic="LOO")
#
