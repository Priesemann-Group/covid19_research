# ------------------------------------------------------------------------------ #
# Shows the tipping point by using our model.
# Needs files created by the cpp model -> see Cpp_Implementation folder
# "stable_model_to_tipping_point()"
#
# ------------------------------------------------------------------------------ #


import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import sys

sys.path.append("../../toolbox/master")
from covid19_inference import plot as covplt


def plot_transient_onto_axes(axes, transient):

    # Load data
    df = pd.read_csv(
        f"../Cpp_Implementation/data/tipping_point/{transient}.000000.csv",
    )
    df["time"] = df["time"]
    df = df.set_index("time")
    df = df[0:400]

    axes[0].plot(
        df.index,
        df["Infectious (hidden)"] / df["New cases observed"],
    )
    axes[0].set_ylabel("New cases observed\n per 1e6 inhibitants")
    axes[0].set_xlabel("Time in days")
    # axes[1].set_ylim(0, 500)
    axes[1].plot(
        df.index,
        df["New cases"] / df["New cases observed"],
    )
    axes[1].set_ylabel("Contact over time")
    # axes[0].set_ylim(0.3, 0.9)


# Create plot
fig, axes = plt.subplots(2, 1, figsize=(6, 4))


transients = [20, 50, 100, 1000]

for transient in transients:
    plot_transient_onto_axes(axes, transient)
