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
from heatmap import reverse_cmap, cmap_to_mpl
import matplotlib as mpl
import matplotlib.font_manager

# default fonts
mpl.rcParams["font.sans-serif"] = "Arial"
mpl.rcParams["font.family"] = "sans-serif"

custom_cmaps = dict()
custom_cmaps["viridis"] = [
    (0, "white"),
    (0.1, "#a9db33"),
    (0.45, "#23898d"),
    (0.85, "#3f4688"),
    (1, "black"),
]


# Load data
def get_var(filename, var_name, foldername="short_swipe"):
    # Load file
    df = pd.read_csv(f"../Cpp_Implementation/data/{foldername}/{filename}")
    df["time"] = df["time"]
    df = df.set_index("time")
    return df[var_name]


def ts_plot(axes, df, x_min, x_max, color="tab:blue", label=""):
    axes.plot(df.index, df, color=color, label=label)
    axes.set_xlim(x_min, x_max)


def load_data_1(foldername):
    # ------------------------------------------------------------------------------ #
    # Loading data
    # ------------------------------------------------------------------------------ #
    Is, ks, Phis, dfs = [], [], [], []
    N = []
    for filename in os.listdir(f"../Cpp_Implementation/data/{foldername}/"):
        if filename.endswith(".csv"):
            k, Phi = os.path.splitext(filename)[0].split("_")

            new_cases = get_var(filename, "New cases observed", foldername=foldername)
            # print(new_cases.iloc[950])
            # if np.abs(new_cases.iloc[950] - new_cases.iloc[951]) < 1e-4:
            ks.append(k)
            Phis.append(Phi)
            N.append(new_cases.iloc[2800])
            dfs.append(new_cases)

    data = pd.DataFrame()
    data["Phi"] = Phis
    data["k"] = ks
    data["N_equilibrium"] = N
    # data["new_cases"] = dfs
    data = data.astype("float64")

    data = data.set_index(["Phi", "k"])
    data = data.sort_index()
    return data


def load_data_2(foldername):
    # ------------------------------------------------------------------------------ #
    # Loading data
    # ------------------------------------------------------------------------------ #
    Is, ks, Phis = [], [], []
    N = []
    for filename in os.listdir(f"../Cpp_Implementation/data/{foldername}/"):
        if filename.endswith(".csv"):
            I, k, Phi = os.path.splitext(filename)[0].split("_")
            new_cases = get_var(filename, "New cases observed", foldername=foldername)

            Is.append(I)
            ks.append(k)
            Phis.append(Phi)
            N.append(new_cases.iloc[2800])
    data = pd.DataFrame()
    data["Phi"] = Phis
    data["k"] = ks
    data["N_equilibrium"] = N
    # data["new_cases"] = dfs
    data = data.astype("float64")

    return data


if __name__ == "__main__":

    # data_slice = load_data_1("short_swipe")
    # data_heatmap = load_data_2("variate_k_Phi")

    data_heatmap = pd.read_csv("heatmap_eq.csv")
    data_slice = pd.read_csv("slices_eq.csv")
    data_heatmap["k"] = 1.0 - data_heatmap["k"]
    data_slice["k"] = 1.0 - data_slice["k"]
    data_slice = data_slice.set_index(["Phi", "k"])
    cmap = reverse_cmap(cmap_to_mpl(custom_cmaps["viridis"]))

    # ------------------------------------------------------------------------------ #
    # Figure
    # ------------------------------------------------------------------------------ #

    fig, axes = plt.subplots(1, 2, figsize=(6.5, 2.8), constrained_layout=True)

    # First Phi = 0.1
    phi01 = data_slice.xs(0.100, level="Phi")
    phi1 = data_slice.xs(1.000, level="Phi")
    phi10 = data_slice.xs(10.000, level="Phi")

    # Slice no log scale
    axes[0].plot(
        phi01.index, phi01["N_equilibrium"], label=r"$\Phi = 0.1$", color="tab:green"
    )
    axes[0].plot(
        phi1.index, phi1["N_equilibrium"], label=r"$\Phi = 1$", color="tab:orange"
    )
    axes[0].plot(
        phi10.index, phi10["N_equilibrium"], label=r"$\Phi = 10$", color="tab:red"
    )
    axes[0].set_ylim(0, 110)
    axes[0].set_xlim(0.15, 0.8)
    axes[0].set_xlabel(r"Contact reduction $k$")
    axes[0].set_ylabel(r"$N_{eq}$")
    axes[0].legend()

    # Heatmap
    Z = data_heatmap.pivot_table(
        index="k", columns="Phi", values="N_equilibrium"
    ).T.values
    X_unique = np.sort(data_heatmap["k"].unique())
    Y_unique = np.sort(data_heatmap["Phi"].unique())
    X, Y = np.meshgrid(X_unique, Y_unique)

    levels = np.logspace(base=10, start=-1.08, stop=2.1, num=20)
    CS = axes[1].contourf(
        X, Y, Z, levels, cmap=cmap, locator=mpl.ticker.LogLocator(), origin="lower",
    )
    CS2 = axes[1].contour(CS, levels=[1, 10], colors=["white", "black"], origin="lower")
    cbar = fig.colorbar(CS, ticks=[0.1, 1, 10, 100])
    cbar.ax.set_ylabel("$N_{eq}$")
    cbar.add_lines(CS2)

    axes[1].invert_xaxis()
    axes[1].set_ylabel(r"Influx $\Phi$")
    axes[1].set_xlabel(r"Contact reduction $k$")
    axes[1].set_xlim(0.35, 0.8)

    fig.savefig("figures/fig_equilibrium.pdf", transparent=True, dpi=300)
    fig.savefig("figures/fig_equilibrium.png", transparent=True, dpi=300)

    # redo everyting for png and remove clutter
    fig, ax = plt.subplots()
    levels = np.logspace(base=10, start=-1.08, stop=2.1, num=20)
    CS = ax.contourf(
        X, Y, Z, levels, cmap=cmap, locator=mpl.ticker.LogLocator(), origin="lower",
    )
    # CS2 = ax.contour(CS, levels=[4, 8], colors=["white", "black"], origin="lower")
    fig.tight_layout()
    plt.gca().set_axis_off()
    ax.axis("off")
    ax.invert_xaxis()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    fig.savefig("figures/fig_equilibrium_free.png", dpi=600)
