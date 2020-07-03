"""
    Plots various comparisons between different countries


    Runtime ~ 1min
"""

import sys
import matplotlib
import matplotlib.pyplot as plt
import datetime
import pandas as pd

try:
    sys.path.append("../../toolbox/v0.1.8")
    import covid19_inference as cov19
except ModuleNotFoundError:
    print(
        """"Could not import the covid19_inference toolbox make sure to have github submodules enabled \n
        or install via pip"""
    )


def plot_countries_comparison(retrieval_source):
    # Alligned to 100th case
    fig1_100th, ax1_100th = plt.subplots()  # raw
    fig2_100th, ax2_100th = plt.subplots()  # rolling 3 days
    fig3_100th, ax3_100th = plt.subplots()  # rolling 7 days

    # Alligned to peak
    fig1_peak, ax1_peak = plt.subplots()  # raw
    fig2_peak, ax2_peak = plt.subplots()  # rolling 3 days
    fig3_peak, ax3_peak = plt.subplots()  # rolling 7 days

    for country in countries:

        # Country data
        if country == "US" and retrieval_source.name == "OurWorldinData":
            data = retrieval_source.get_new(
                "confirmed", "United States", data_begin=datetime.datetime(2020, 1, 24)
            )
        else:
            data = retrieval_source.get_new(
                "confirmed", country, data_begin=datetime.datetime(2020, 1, 24)
            )
        data = data.reset_index()
        if retrieval_source.name == "OurWorldinData":
            data = data.rename(columns={"new_cases": "confirmed"})

        # Fills new cases
        data["confirmed_norm"] = (
            1e6 * data["confirmed"] / countries[country]["Population"]
        )
        data["confirmed_norm_rolling3"] = data["confirmed_norm"].rolling(3).mean()
        data["confirmed_norm_rolling7"] = data["confirmed_norm"].rolling(7).mean()

        # Days since 100th case
        date_100 = data[data["confirmed"] > 100]["date"].min()
        data["days_100"] = data["date"].apply(lambda x: (x - date_100).days)

        # Days since/before the peak
        date_max = data["date"][data["confirmed"].idxmax()]
        date_max_rolling3 = data["date"][data["confirmed_norm_rolling3"].idxmax()]
        date_max_rolling7 = data["date"][data["confirmed_norm_rolling7"].idxmax()]

        data["days_max"] = data["date"].apply(lambda x: (x - date_max).days)
        data["days_max_rolling3"] = data["date"].apply(
            lambda x: (x - date_max_rolling3).days
        )
        data["days_max_rolling7"] = data["date"].apply(
            lambda x: (x - date_max_rolling7).days
        )

        # Plot alligned to 100th case
        ax1_100th.plot(
            data["days_100"],
            data["confirmed_norm"],
            label=countries[country]["name"],
            lw=3,
        )
        ax2_100th.plot(
            data["days_100"],
            data["confirmed_norm_rolling3"],
            label=countries[country]["name"],
            lw=3,
        )
        ax3_100th.plot(
            data["days_100"],
            data["confirmed_norm_rolling7"],
            label=countries[country]["name"],
            lw=3,
        )

        # Plot alligned to peak
        ax1_peak.plot(
            data["days_max"],
            data["confirmed_norm"],
            label=countries[country]["name"],
            lw=3,
        )
        ax2_peak.plot(
            data["days_max_rolling3"],
            data["confirmed_norm_rolling3"],
            label=countries[country]["name"],
            lw=3,
        )
        ax3_peak.plot(
            data["days_max_rolling7"],
            data["confirmed_norm_rolling7"],
            label=countries[country]["name"],
            lw=3,
        )

        # Set titles
        ax1_100th.set_title("raw numbers")
        ax2_100th.set_title("3-day average")
        ax3_100th.set_title("7-day average")

        ax1_peak.set_title("raw numbers")
        ax2_peak.set_title("3-day average")
        ax3_peak.set_title("7-day average")

        for ax in [ax1_100th, ax2_100th, ax3_100th]:
            ax.legend(frameon=False, loc="upper left")
            ax.set_xlim(left=0)
            ax.set_ylim([0, 150])
            ax.set_xlabel("Days since 100th case")
            ax.set_ylabel("New daily cases per 1M habitants")
            plt.tight_layout()

        for ax in [ax1_peak, ax2_peak, ax3_peak]:
            ax.legend(frameon=False, loc="upper left")
            ax.set_ylim([0, 150])
            ax.set_xlim([-60, 60])
            ax.set_xlabel("Days before/after the peak")
            ax.set_ylabel("New daily cases per 1M habitants")

    # Save figs
    save_kwargs = dict(transparent=True, format="pdf", dpi=300)
    fig1_100th.savefig(
        f"figures/comparison_new_cases_{retrieval_source.name}_since_100th_raw.pdf",
        **save_kwargs,
    )
    fig2_100th.savefig(
        f"figures/comparison_new_cases_{retrieval_source.name}_since_100th_3day_average.pdf",
        **save_kwargs,
    )
    fig3_100th.savefig(
        f"figures/comparison_new_cases_{retrieval_source.name}_since_100th_7day_average.pdf",
        **save_kwargs,
    )

    fig1_peak.savefig(
        f"figures/comparison_new_cases_{retrieval_source.name}_since_peak_raw.pdf",
        **save_kwargs,
    )
    fig2_peak.savefig(
        f"figures/comparison_new_cases_{retrieval_source.name}_since_peak_3day_average.pdf",
        **save_kwargs,
    )
    fig3_peak.savefig(
        f"figures/comparison_new_cases_{retrieval_source.name}_since_peak_7day_average.pdf",
        **save_kwargs,
    )


if __name__ == "__main__":
    """ ## Data Retrieval an other data
    """
    JHU = cov19.data_retrieval.JHU(True)
    ECDC = cov19.data_retrieval.OWD(True)

    # Population data from https://www.worldometers.info/world-population/population-by-country/
    countries = {
        "Germany": {"name": "Germany", "Population": 83783942},
        "United Kingdom": {"name": "United Kindgom", "Population": 67886011},
        #'Spain': {'name':'Spain', 'Population': 46754778},
        "US": {"name": "United States", "Population": 331002651},
        "Brazil": {"name": "Brazil", "Population": 212559417},
    }

    """ ### Plot for JHU and ECDC
    """

    plot_countries_comparison(JHU)
    plot_countries_comparison(ECDC)
