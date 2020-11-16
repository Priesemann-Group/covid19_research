# ------------------------------------------------------------------------------ #
# Shows equilibrium with influx event
# Needs files created by the cpp model -> see Cpp_Implementation folder
#
# Runtime ~ 1min
# ------------------------------------------------------------------------------ #


import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import sys
import seaborn as sns
from matplotlib.colors import LogNorm

# Load data
def get_var(filename, var_name):
    # Load file
    df = pd.read_csv(f"../Cpp_Implementation/data/short_swipe/{filename}")
    df["time"] = df["time"]
    df = df.set_index("time")
    return df[var_name]


def ts_plot(axes, df, x_min, x_max, color="tab:blue", label=""):
    axes.plot(df.index, df, color=color, label=label)
    axes.set_xlim(x_min, x_max)


if __name__ == "__main__":
    # ------------------------------------------------------------------------------ #
    # Loading data
    # ------------------------------------------------------------------------------ #
    Is, ks, Phis, dfs = [], [], [], []
    N = []
    for filename in os.listdir("../Cpp_Implementation/data/short_swipe/"):
        if filename.endswith(".csv"):
            k, Phi = os.path.splitext(filename)[0].split("_")

            new_cases = get_var(filename, "New cases observed")
            # print(new_cases.iloc[950])
            # if np.abs(new_cases.iloc[950] - new_cases.iloc[951]) < 1e-4:
            ks.append(k)
            Phis.append(Phi)
            N.append(new_cases.iloc[3000])
            dfs.append(new_cases)

    data = pd.DataFrame()
    data["Phi"] = Phis
    data["k"] = ks
    data["N_equilibrium"] = N
    # data["new_cases"] = dfs
    data = data.astype("float64")

    data = data.set_index(["Phi", "k"])
    data = data.sort_index()

    heatmap = pd.read_csv("heatmap_data.csv")
    heatmap_low = heatmap[heatmap["I_0"] < 5.0]
    heatmap_high = heatmap[heatmap["I_0"] > 5.0]
    heatmap_low = heatmap_low.pivot(index="k", columns="Phi", values="N_equilibrium")
    heatmap_high = heatmap_high.pivot(index="k", columns="Phi", values="N_equilibrium")

    heatmap_combined = ((heatmap_low + heatmap_high) / 2)[
        (heatmap_low - heatmap_high) > -1000
    ]

    # ------------------------------------------------------------------------------ #
    # Figure
    # ------------------------------------------------------------------------------ #

    fig, axes = plt.subplots(1, 2, figsize=(8, 3), constrained_layout=True)

    # First Phi = 0.1
    phi01 = data.xs(0.100, level="Phi")
    phi1 = data.xs(1.000, level="Phi")
    phi10 = data.xs(10.000, level="Phi")

    # Upper left Overview
    axes[0].plot(phi01.index, phi01["N_equilibrium"], label=r"$\Phi = 0.1$")
    axes[0].plot(phi1.index, phi1["N_equilibrium"], label=r"$\Phi = 1$")
    axes[0].plot(phi10.index, phi10["N_equilibrium"], label=r"$\Phi = 10$")
    axes[0].set_ylim(0, 500)
    axes[0].legend()
    # TTI capacity

    sns.heatmap(
        heatmap_combined,
        cmap="viridis",
        ax=axes[1],
        norm=LogNorm(),
        vmax=100,
        cbar_kws={"label": r"$N_{eq}$"},
    )
    axes[1].set_ylim(0, 42)
    axes[1].set_xlim(0, 500)

    fig.savefig("figures/fig_equilibrium.svg", transparent=True, dpi=300)
    fig.savefig("figures/fig_equilibrium.pdf", transparent=True, dpi=300)

# Plot
"""


ts_plot(axes[0], phi, 0, 200)
ts_plot(axes[1], low, 0, 200, color="tab:purple", label=r"$N_{eq}^-$")
ts_plot(axes[1], high, 0, 200, color="tab:orange", label=r"$N_{eq}^+$")

ts_plot(axes[2], low_hidden, fig.0, 200, color="tab:purple", label=r"$N_{eq}^+$")
ts_plot(axes[2], high_hidden, 0, 200, color="tab:orange", label=r"$N_{eq}^+$")

plt.legend()
axes[1].set_ylim(8, 18)
axes[1].set_xlabel("days")
axes[1].set_ylabel("New cases observed")  #
axes[0].set_ylabel("Influx")
plt.tight_layout()
fig.savefig("figures/fig_influx_event_eq.svg", transparent=True, dpi=300)
fig.savefig("figures/fig_influx_event_eq.pdf", transparent=True, dpi=300)
"""
