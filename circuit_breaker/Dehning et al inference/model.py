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
from plot_scenarios import create_plot_scenarios, _format_k
import matplotlib.lines as mlines

try:
    import covid19_inference as cov19
except ModuleNotFoundError:
    sys.path.append("../../toolbox/master")
    import covid19_inference as cov19

## Download data
rki = cov19.data_retrieval.RKI()
rki.download_all_available_data(force_download=True)
data_begin = datetime.datetime(2020, 6, 13)
data_end = datetime.datetime(2020, 11, 10)
new_cases_obs = rki.get_new("confirmed", data_begin=data_begin, data_end=data_end)
total_cases_obs = rki.get_total("confirmed", data_begin=data_begin, data_end=data_end)

""" ## Create weekly changepoints
"""

# Structures change points in a dict. Variables not passed will assume default values.
change_points_a = [
    dict(
        pr_mean_date_transient=datetime.datetime(2020, 6, 9),
        pr_sigma_date_transient=1.5,
        pr_median_lambda=0.12,
        pr_sigma_lambda=0.5,
    ),
]

change_points_a.append(
    dict(
        pr_mean_date_transient=datetime.datetime(2020, 9, 20),
        pr_sigma_date_transient=20.5,
        pr_median_lambda=0.19,
        pr_sigma_lambda=0.5,
    ),
)

# Structures change points in a dict. Variables not passed will assume default values.
change_points_b = [
    dict(
        pr_mean_date_transient=datetime.datetime(2020, 6, 9),
        pr_sigma_date_transient=1.5,
        pr_median_lambda=0.12,
        pr_sigma_lambda=0.5,
    ),
]
change_points_b.append(
    dict(
        pr_mean_date_transient=datetime.datetime(2020, 8, 20),
        pr_sigma_date_transient=7.0,
        pr_median_lambda=0.19,
        pr_sigma_lambda=0.5,
        pr_median_transient_len=65.0,
        pr_sigma_transient_len=0.07,
    ),
)

# Structures change points in a dict. Variables not passed will assume default values.
change_points_c = [
    dict(
        pr_mean_date_transient=datetime.datetime(2020, 6, 9),
        pr_sigma_date_transient=1.5,
        pr_median_lambda=0.12,
        pr_sigma_lambda=0.5,
    ),
]
change_points_c.append(
    dict(
        pr_mean_date_transient=datetime.datetime(2020, 8, 15),
        pr_sigma_date_transient=10.0,
        pr_median_lambda=0.19,
        pr_sigma_lambda=0.5,
        pr_median_transient_len=10.0,
        pr_sigma_transient_len=4.00,
    ),
)


def construct_model(change_points):
    # Number of days the simulation starts earlier than the data.
    # Should be significantly larger than the expected delay in order to always fit the same number of data points.
    diff_data_sim = 16
    # Number of days in the future (after date_end_data) to forecast cases
    num_days_forecast = 10
    params_model = dict(
        new_cases_obs=new_cases_obs[:],
        data_begin=data_begin,
        fcast_len=num_days_forecast,
        diff_data_sim=diff_data_sim,
        N_population=83e6,
    )
    # Median of the prior for the delay in case reporting, we assume 10 days
    pr_delay = 10
    with cov19.model.Cov19Model(**params_model) as this_model:
        # Create the an array of the time dependent infection rate lambda
        cp = change_points
        lambda_t_log = cov19.model.lambda_t_with_sigmoids(
            pr_median_lambda_0=0.4,
            pr_sigma_lambda_0=0.5,
            change_points_list=change_points,  # The change point priors we constructed earlier
            name_lambda_t="lambda_t",  # Name for the variable in the trace (see later)
        )

        # set prior distribution for the recovery rate
        mu = pm.Lognormal(name="mu", mu=np.log(1 / 8), sigma=0.2)

        # This builds a decorrelated prior for I_begin for faster inference.
        # It is not necessary to use it, one can simply remove it and use the default argument
        # for pr_I_begin in cov19.SIR
        prior_I = cov19.model.uncorrelated_prior_I(
            lambda_t_log=lambda_t_log,
            mu=mu,
            pr_median_delay=pr_delay,
            name_I_begin="I_begin",
            name_I_begin_ratio_log="I_begin_ratio_log",
            pr_sigma_I_begin=2,
            n_data_points_used=5,
        )

        # Use lambda_t_log and mu to run the SIR model
        new_cases = cov19.model.SIR(
            lambda_t_log=lambda_t_log,
            mu=mu,
            name_new_I_t="new_I_t",
            name_I_t="I_t",
            name_I_begin="I_begin",
            pr_I_begin=prior_I,
        )

        # Delay the cases by a lognormal reporting delay
        new_cases = cov19.model.delay_cases(
            cases=new_cases,
            name_cases="delayed_cases",
            name_delay="delay",
            name_width="delay-width",
            pr_mean_of_median=pr_delay,
            pr_sigma_of_median=0.2,
            pr_median_of_width=0.3,
        )

        # Modulate the inferred cases by a abs(sin(x)) function, to account for weekend effects
        # Also adds the "new_cases" variable to the trace that has all model features.
        new_cases = cov19.model.week_modulation(
            cases=new_cases,
            name_cases="new_cases",
            name_weekend_factor="weekend_factor",
            name_offset_modulation="offset_modulation",
            week_modulation_type="abs_sine",
            pr_mean_weekend_factor=0.3,
            pr_sigma_weekend_factor=0.5,
            weekend_days=(6, 7),
        )

        # Define the likelihood, uses the new_cases_obs set as model parameter
        cov19.model.student_t_likelihood(new_cases)

    return this_model


""" ## MCMC sampling
"""
mod_a = construct_model(change_points_a)
mod_b = construct_model(change_points_b)
mod_c = construct_model(change_points_c)

tra_a = pm.sample(model=mod_a, init="advi", tune=1000, draws=3000, chains=4)
tra_b = pm.sample(model=mod_b, init="advi", tune=1000, draws=3000, chains=4)
tra_c = pm.sample(model=mod_c, init="advi", tune=1000, draws=3000, chains=4)

with open("./figures/trace.pickle", "wb") as f:
    pickle.dump(([mod_a, tra_a], [mod_b, tra_b], [mod_c, tra_c]), f)

"""with open("./dl/trace.pickle", "rb") as f:
    ([mod_a, tra_a], [mod_b, tra_b], [mod_c, tra_c]) = pickle.load(f)
"""
""" ## Plotting
    
    ### Save path
"""
try:
    # only works when called from python, not reliable in interactive ipython etc.
    os.chdir(os.path.dirname(__file__))
    save_to = "./figures/reproduction_"
except:
    # assume base directory
    save_to = "./figures/reproduction_"

for this_model, trace, change_points, name in zip(
    [
        mod_c,
    ],
    [
        tra_c,
    ],
    [
        change_points_c,
    ],
    [
        "free",
    ],
):

    """### Timeseries
    Timeseries overview, for now needs an offset variable to get cumulative cases
    """
    fig, axes = create_plot_scenarios(this_model, trace, offset=total_cases_obs[0])

    for ax in axes:
        ax.set_xlim(datetime.datetime(2020, 6, 20), datetime.datetime(2020, 11, 14))
    axes[0].set_xlim(datetime.datetime(2020, 6, 20), datetime.datetime(2020, 10, 18))
    # Set y lim for effective growth rate
    axes[0].set_ylim(-0.1, 0.2)
    # axes[1].set_ylim(0, new_cases_obs.max() + 5000)
    # Add vline for today

    # --------------------------------------------------------------------------- #
    # inset new cases
    # --------------------------------------------------------------------------- #
    # Add inset for march to juli
    from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes

    axins = axes[1].inset_axes(bounds=[0.2, 0.5, 0.55, 0.4])
    for line in axes[1].lines:
        axins.lines.append(line)

    ax = axins
    ax.set_alpha(0.1)
    new_cases_inset = (
        rki.get_new(
            "confirmed", data_begin=datetime.datetime(2020, 3, 2), data_end=data_end
        )
        .rolling(7)
        .mean()
        / 83.02e6
        * 1e6
    )

    # model fit
    cov19.plot._timeseries(
        x=new_cases_inset.index,
        y=new_cases_inset,
        ax=ax,
        what="model",
        color=cov19.plot.rcParams["color_data"],
    )
    prec = 1.0 / (np.log10(ax.get_ylim()[1]) - 2.5)

    ticks = ax.get_xticks()
    ax.set_xticks(ticks=[new_cases_inset.index.min(), new_cases_inset.index.max()])

    # Format lambda to R rki
    import matplotlib.ticker as ticker

    axes[0].set_ylabel("Reproduction number\n R")
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

    axes[0].set_ylim(0.8, 1.6)
    axes[1].set_ylabel("Reported cases per million")
    axes[2].remove()
    # save: ts for timeseries
    plt.savefig(
        save_to + name + "_ts.svg",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0.05,
        transparent=True,
    )
    plt.savefig(
        save_to + name + "_ts.png",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0.05,
        transparent=True,
    )

    """ ### Distributions ##################################################
    """
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
            cov19.plot._distribution(this_model, trace, "mu", axes[0, 0])
        else:
            # Plot lambda_i and remove the xlable, we add one big label later.
            cov19.plot._distribution(
                this_model, trace, f"lambda_{i}", axes[-i + num_rows, 0]
            )
            axes[-i + num_rows, 0].set_xlabel("")
    # middle row
    for i in rows:
        if i == 0:
            cov19.plot._distribution(this_model, trace, "sigma_obs", axes[i, 1])
        else:
            # Plot transient_day_i and remove the xlable, we add one big label later.
            cov19.plot._distribution(
                this_model, trace, f"transient_day_{i}", axes[-i + num_rows, 1]
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
                this_model, trace, f"transient_len_{i}", axes[-i + num_rows, 2]
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
    if name == "free":
        axes[1, 2].set_xlim(0, 12)
        axes[1, 1].set_xlim(
            datetime.datetime(2020, 9, 23), datetime.datetime(2020, 10, 16)
        )

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
    labels.append("Data (RKI)")
    legend = axes[0, 2].get_legend()
    legend._legend_box = None
    legend._init_legend_box(handles, labels)
    legend._set_loc(legend._loc)
    legend.set_title(legend.get_title().get_text())

    # dist for distributions
    plt.savefig(
        save_to + name + "_dist.svg",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0.05,
        transparent=True,
    )
    plt.savefig(
        save_to + name + "_dist.png",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0.05,
        transparent=True,
    )


# ------------------------------------------------------------------------------ #
# Model Comparison
# ------------------------------------------------------------------------------ #
mod_a.name = "short"
mod_b.name = "long"
mod_c.name = "free"
comparison = pm.compare({mod_a: tra_a, mod_b: tra_b, mod_c: tra_c}, ic="LOO")
print(comparison)
