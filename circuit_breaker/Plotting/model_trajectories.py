# ------------------------------------------------------------------------------ #
# @Author:        F. Paul Spitzner
# @Email:         paul.spitzner@ds.mpg.de
# @Created:       2020-11-11 11:46:01
# @Last Modified: 2020-11-12 09:57:43
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
from matplotlib.ticker import MultipleLocator, LinearLocator, FormatStrFormatter, AutoMinorLocator
import numpy as np
import seaborn as sns  # v 0.11
import pandas as pd

import covid19_inference as cov19
import datetime
from datetime import datetime as dt

from matplotlib.colors import LinearSegmentedColormap

# default fonts
mpl.rcParams['font.sans-serif'] = "Arial"
mpl.rcParams['font.family'] = "sans-serif"

my_colors = dict()

my_colors["temperature"] = [
    (0, "white"),
    (0.2, "#FFECB3"),
    (0.45, "#E85285"),
    (0.85, "#6A1B9A"),
    (1, "black"),
]


def clr_to_cmap(colors, n_bins=256):
    return LinearSegmentedColormap.from_list("custom_cmap", colors, N=n_bins)






# set color_norm to the printed value
def plot_trajectories(dat,
    num_lines = 30,
    align_at = 21,
    color_norm=0.205):

    fig, ax = plt.subplots(figsize=[4, 3])


    ylim = (0, 150)
    dy = (ylim[1] - ylim[0]) / num_lines

    # filter trajectories that match wanted line distance
    y = ylim[0]
    use_lines = []
    d = 0
    for l in range(500 * num_lines):
        found = False
        while not found:
            if dat[align_at, d] > y:
                use_lines += [d]
                found = True
            d += 1
            if d == dat.shape[1]:
                break

        if d == dat.shape[1]:
            break
        y = dat[align_at, d-1] + dy


    use_lines = np.unique(use_lines)
    dat = dat[:, use_lines]


    cm = plt.get_cmap('coolwarm')
    # line_trend = dat[60, :] - dat[40, :]
    line_trend = dat[-1, :] - dat[0, :]

    tmin = np.nanmin(line_trend)
    tmax = np.nanmax(line_trend)

    def trend_to_color(line_trend, norm):
        line_color = line_trend
        # line_color[line_color > np.abs(norm)] /= np.abs(norm)
        # line_color[line_color <= np.abs(norm)] /= np.abs(norm)
        line_color /= np.abs(norm)
        line_color = np.clip(line_color, a_min = -1, a_max = + 1)
        line_color = (line_color + 1) / 2

        return line_color

    trajectory_color = trend_to_color(line_trend, tmin)


    # find local minimum value, per arrow
    tmin_local = + np.inf
    tmax_local = - np.inf

    for l in range(dat.shape[1]):
        # x = np.arange(dat.shape[0])
        # ax.plot(x, dat[:, l], alpha=1, color =
        #     cm(trajectory_color[l]),
        #     lw = .5
        # )
        # paul wants white spaces
        for d in range(int(dat.shape[0] / 7) ):
            ledge = d*7
            redge = (d+1)*7
            if redge < dat.shape[0]-3:
                redge += (l % 3) * 3
            if ledge > 3:
                ledge += (l % 3) * 3

            x = np.arange(ledge, redge)
            trend = dat[redge, l] - dat[ledge, l]
            trend /= (redge-ledge)

            ax.plot(x, dat[x, l], alpha=1,
                # color = cm(trajectory_color[l]),
                color = cm(trend_to_color(trend, norm = color_norm) ),
                lw =1.5
            )

            if trend < tmin_local:
                tmin_local = trend
            if trend > tmax_local:
                tmax_local = trend

    print(f"tmin_local = {tmin_local}")

    ax.set_ylim(ylim)

    ax.yaxis.set_major_locator(MultipleLocator(50))
    ax.yaxis.set_minor_locator(MultipleLocator(10))
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_position(("outward", 15))


    ax.xaxis.set_major_locator(MultipleLocator(28))
    ax.xaxis.set_minor_locator(MultipleLocator(7))

    fig.tight_layout()

    return fig, ax

# meta stable
dat = np.loadtxt("/Users/paul/Downloads/lala_k06_checked.csv", delimiter=",")
dat = dat[:, 1:]
fig, ax = plot_trajectories(dat, color_norm=0.1, align_at = 60)
ax.set_xlim(35, 119)
ax.xaxis.set_major_locator(LinearLocator(4))

# unstable
dat = np.loadtxt("/Users/paul/Downloads/lala_k08_checked.csv", delimiter=",")
dat = dat[:, 1:]
fig, ax = plot_trajectories(dat, color_norm=2.1, align_at = 35)
# ax.set_xlim(28, 112)
ax.set_xlim(35, 91)
ax.xaxis.set_major_locator(LinearLocator(3))

# stable
dat = np.loadtxt("/Users/paul/Downloads/lala_k04_checked.csv", delimiter=",")
dat = dat[:, 1:]
fig, ax = plot_trajectories(dat, color_norm=2.1, align_at = 35, num_lines=20)
# ax.set_xlim(28, 112)
ax.set_xlim(35, 91)
ax.xaxis.set_major_locator(LinearLocator(3))

for i in plt.get_fignums():
    plt.figure(i)
    plt.savefig(f"/Users/paul/Desktop/figure_{i:d}.pdf", dpi=300)
