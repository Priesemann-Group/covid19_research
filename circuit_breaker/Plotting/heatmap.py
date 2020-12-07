# ------------------------------------------------------------------------------ #
# @Author:        F. Paul Spitzner
# @Email:         paul.spitzner@ds.mpg.de
# @Created:       2020-11-14 17:15:43
# @Last Modified: 2020-11-16 16:20:36
# ------------------------------------------------------------------------------ #
import os
import sys
import glob
import h5py
import argparse
import logging

log = logging.getLogger(__name__)

import locale

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import (
    MultipleLocator,
    LinearLocator,
    FormatStrFormatter,
    AutoMinorLocator,
)
import numpy as np
import seaborn as sns  # v 0.11
import pandas as pd


import datetime
from datetime import datetime as dt

from matplotlib.colors import LinearSegmentedColormap

# default fonts
mpl.rcParams["font.sans-serif"] = "Arial"
mpl.rcParams["font.family"] = "sans-serif"

custom_cmaps = dict()
custom_cmaps["cold"] = [
    (0, "white"),
    (0.25, "#DCEDC8"),
    (0.45, "#42B3D5"),
    (0.75, "#1A237E"),
    (1, "black"),
]
custom_cmaps["hot"] = [
    (0, "white"),
    (0.3, "#FEEB65"),
    (0.65, "#E4521B"),
    (0.85, "#4D342F"),
    (1, "black"),
]
custom_cmaps["pinks"] = [
    (0, "white"),
    (0.2, "#FFECB3"),
    (0.45, "#E85285"),
    (0.85, "#6A1B9A"),
    (1, "black"),
]


def cmap_to_mpl(colors, n_bins=512):
    return LinearSegmentedColormap.from_list("custom_cmap", colors, N=n_bins)


def reverse_cmap(cmap, name="my_cmap_r"):
    reverse = []
    k = []

    for key in cmap._segmentdata:
        k.append(key)
        channel = cmap._segmentdata[key]
        data = []

        for t in channel:
            data.append((1 - t[0], t[2], t[1]))
        reverse.append(sorted(data))

    LinearL = dict(zip(k, reverse))
    my_cmap_r = mpl.colors.LinearSegmentedColormap(name, LinearL)
    return my_cmap_r


if __name__ == "__main__":
    cmap = reverse_cmap(cmap_to_mpl(custom_cmaps["cold"]))

    t = np.loadtxt("/Users/paul/Downloads/Ts_LD.csv", delimiter=",")
    k = np.loadtxt("/Users/paul/Downloads/kt_LD.csv", delimiter=",")
    d = np.loadtxt("/Users/paul/Downloads/D_LD.csv", delimiter=",")

    fig, ax = plt.subplots(figsize=(6, 4))

    # sns.heatmap(
    #     data=d,
    #     ax=ax,
    #     cmap=cmap,
    #     vmin=0,
    #     vmax=9,
    #     xticklabels=k,
    #     yticklabels=t,
    #     square=False,
    #     cbar_ax=ax_bar,
    # )
    # ax.invert_yaxis()

    fig, ax = plt.subplots()
    levels = np.arange(-0.25, 9.75, 0.5)
    CS = ax.contourf(k, t, d, levels, cmap=cmap, origin="lower")
    CS2 = ax.contour(CS, levels=[4, 8], colors=["white", "black"], origin="lower")

    # Make a colorbar for the ContourSet returned by the contourf call.
    cbar = fig.colorbar(CS, ticks=np.arange(0, 10))
    cbar.ax.set_ylabel("required lockdown (weeks)")
    # Add the contour line levels to the colorbar
    cbar.add_lines(CS2)

    ax.set_ylabel("start time Ts")
    ax.set_xlabel("contact fraction k")

    fig.tight_layout()
    fig.savefig("/Users/paul/Desktop/heatmap.pdf")

    # redo everyting for png and remove clutter
    fig, ax = plt.subplots()
    levels = np.arange(-0.25, 9.75, 0.5)
    CS = ax.contourf(k, t, d, levels, cmap=cmap, origin="lower")
    # CS2 = ax.contour(CS, levels=[4, 8], colors=["white", "black"], origin="lower")
    fig.tight_layout()
    plt.gca().set_axis_off()
    ax.axis("off")
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    fig.savefig("/Users/paul/Desktop/heatmap.png", dpi=600)
