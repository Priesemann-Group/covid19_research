# ------------------------------------------------------------------------------ #
# @Author:        F. Paul Spitzner
# @Email:         paul.spitzner@ds.mpg.de
# @Created:       2020-11-03 10:40:09
# @Last Modified: 2020-11-04 16:19:07
# ------------------------------------------------------------------------------ #
# todo:
# * mean values and axis are different wihtin a split second
#   -> triangle with numeric vlaue
# * 50 per week per 100 k
# * 20 per day per göttingen lk ~ 300 k
# * per milion per day
#
# * SI
# - portugal vs spain (soccer team colors)
# - bundesländer (zeit online)
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
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator
import numpy as np
import seaborn as sns  # v 0.11
import pandas as pd

import covid19_inference as cov19
import datetime
from datetime import datetime as dt


# ------------------------------------------------------------------------------ #
# colormaps
# https://matplotlib.org/3.1.0/gallery/color/custom_cmap.html#sphx-glr-gallery-color-custom-cmap-py
# https://samanthaz.me/writing/finding-the-right-color-palettes-for-data-visualizations
# e.g. call as cmap = clr_to_cmap(my_colors['pinks'], n_bins=10)
# ------------------------------------------------------------------------------ #

from matplotlib.colors import LinearSegmentedColormap

my_colors = dict()
my_colors["cold"] = [
    (0, "white"),
    (0.25, "#DCEDC8"),
    (0.45, "#42B3D5"),
    (0.75, "#1A237E"),
    (1, "black"),
]
my_colors["hot"] = [
    (0, "white"),
    (0.3, "#FEEB65"),
    (0.65, "#E4521B"),
    (0.85, "#4D342F"),
    (1, "black"),
]
my_colors["pinks"] = [
    (0, "white"),
    (0.2, "#FFECB3"),
    (0.45, "#E85285"),
    (0.85, "#6A1B9A"),
    (1, "black"),
]


def clr_to_cmap(colors, n_bins=256):
    return LinearSegmentedColormap.from_list("custom_cmap", colors, N=n_bins)


owd = cov19.data_retrieval.OWD()
owd.download_all_available_data()


# ------------------------------------------------------------------------------ #
# plots
# ------------------------------------------------------------------------------ #

c_top = [
    "United States",
    "Brazil",
    "Colombia",
    "Chile",
]

c_mid = [
    "Spain",
    "France",
    "Belgium",
    "Switzerland",
    "Czech Republic",
    "Austria",
    "Netherlands",
    "Italy",
    "Poland",
    "Germany",
    "Denmark",
    "Norway",
    "Finland",
]

c_bot = [
    "China",
    "South Korea",
    "Australia",
    "New Zealand",
]


def format_x(ax):
    locale.setlocale(locale.LC_ALL, "de_de.UTF-8")
    ax.xaxis.set_major_formatter(mpl.dates.DateFormatter("%b."))
    ax.xaxis.set_major_locator(mpl.dates.MonthLocator(bymonthday=15))
    ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=1))
    ax.tick_params(axis="x", which="minor", length=8)
    ax.tick_params(axis="x", which="major", length=0)


def plot_ts(
    countries, data_begin, data_end, ax, cmap,
):

    if ax is None:
        fig, ax = plt.subplots()

    if cmap is None:
        cmap = mpl.cm.get_cmap("viridis")

    global df
    df = pd.DataFrame()

    m = []
    color_dict = dict()

    for idx, c in enumerate(countries):

        dat = owd._filter(
            value="new_cases_smoothed_per_million",
            country=c,
            data_begin=data_begin,
            data_end=data_end,
        )
        m.append(dat[np.where(np.isfinite(dat))[0]])
        df[c] = dat
        # store the color-country link for later use
        clr = cmap((idx + 1) / (len(countries) + 1))
        color_dict[c] = clr
        ax.plot(dat, label=c, color=clr)

    for ts in m:
        assert len(ts) == len(m[0])
    m = np.array(m)
    mm = np.median(m)
    log.info(f"median across all countires: {mm}")

    # transformations
    # https://stackoverflow.com/questions/29107800/python-matplotlib-convert-axis-data-coordinates-systems
    axis_to_data = ax.transAxes + ax.transData.inverted()
    data_to_axis = axis_to_data.inverted()

    arrow_from = (mpl.dates.date2num(data_begin + datetime.timedelta(days=-4)), mm)
    arrow_to = (mpl.dates.date2num(data_begin + datetime.timedelta(days=-15)), mm)

    ax.annotate(
        "",
        xy=arrow_to,
        xytext=arrow_from,
        xycoords="data",
        arrowprops=dict(
            arrowstyle="wedge, tail_width=0.8,shrink_factor=0.45",
            facecolor=cmap(0.5),
            edgecolor=cmap(0.5),
        ),
        annotation_clip=False,
    )

    ax.set_xlim(bd, ed)
    format_x(ax)

    ax.legend(loc="upper left")
    handles, labels = ax.get_legend_handles_labels()
    ax.get_legend().set_visible(False)

    fig_legend = plt.figure(figsize=(2, 0.25 * len(countries)))
    axi = fig_legend.add_subplot(111)
    leg = fig_legend.legend(handles, labels, loc="center", scatterpoints=1)
    fig_legend.canvas.draw()
    axi.axis("off")
    leg.get_frame().set_linewidth(0.0)
    leg.get_frame().set_facecolor("#F0F0F0")

    return ax.get_figure(), ax, color_dict


fig, axes = plt.subplots(
    nrows=3,
    ncols=2,
    figsize=[4, 6],
    gridspec_kw={"width_ratios": [8, 1]},
    sharey="row",
)


bd = datetime.datetime(2020, 5, 15)
ed = datetime.datetime(2020, 9, 15)
_, _, c_top = plot_ts(
    countries=c_top,
    data_begin=bd,
    data_end=ed,
    ax=axes[0, 0],
    cmap=clr_to_cmap(my_colors["hot"]),
)
_, _, c_mid = plot_ts(
    countries=c_mid,
    data_begin=bd,
    data_end=ed,
    ax=axes[1, 0],
    cmap=clr_to_cmap(my_colors["pinks"]),
)
_, _, c_bot = plot_ts(
    countries=c_bot,
    data_begin=bd,
    data_end=ed,
    ax=axes[2, 0],
    cmap=clr_to_cmap(my_colors["cold"]),
)

axes[0, 0].set_ylim(0, 250)
axes[1, 0].set_ylim(0, 100)
axes[2, 0].set_ylim(0, 25)

axes[0, 0].yaxis.set_major_locator(MultipleLocator(100))
axes[1, 0].yaxis.set_major_locator(MultipleLocator(50))
axes[2, 0].yaxis.set_major_locator(MultipleLocator(10))

axes[0, 0].yaxis.set_minor_locator(MultipleLocator(50))
axes[1, 0].yaxis.set_minor_locator(MultipleLocator(10))
axes[2, 0].yaxis.set_minor_locator(MultipleLocator(5))

axes[1,0].set_ylabel("New cases per million inhabitants\n(running avg. over 7 days)")

# axes[1, 0].get_legend().set_visible(False)

for ax in axes[:, 0]:
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_position(("outward", 20))
    # remove mai/spet
    ax.xaxis.get_ticklabels()[0].set_visible(False)
    ax.xaxis.get_ticklabels()[-1].set_visible(False)

# ------------------------------------------------------------------------------ #
# displots
# ------------------------------------------------------------------------------ #


def plot_kde(
    countries, data_begin, data_end, ax, cmap,
):

    m = []

    for idx, c in enumerate(countries):

        dat = owd._filter(
            value="new_cases_smoothed_per_million",
            country=c,
            data_begin=data_begin,
            data_end=data_end,
        )
        m.append(dat[np.where(np.isfinite(dat))[0]])

    for ts in m:
        assert len(ts) == len(m[0])

    global df
    # m = pd.DataFrame(data={'col1':np.array(m).flatten()} )
    m = np.array(m).flatten()
    df = m

    sns.kdeplot(
        y=m, ax=ax, fill=True, color=cmap(0.5), alpha=0.75, bw_adjust=0.3, clip_on=True
    )

    return ax.get_figure(), ax


plot_kde(
    countries=c_top,
    data_begin=bd,
    data_end=ed,
    ax=axes[0, 1],
    cmap=clr_to_cmap(my_colors["hot"]),
)
plot_kde(
    countries=c_mid,
    data_begin=bd,
    data_end=ed,
    ax=axes[1, 1],
    cmap=clr_to_cmap(my_colors["pinks"]),
)
plot_kde(
    countries=c_bot,
    data_begin=bd,
    data_end=ed,
    ax=axes[2, 1],
    cmap=clr_to_cmap(my_colors["cold"]),
)

for idx, ax in enumerate(axes[:, 1]):
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_position(("axes", 0))
    ax.set_xticks([])
    ax.set_xlabel("")

fig.tight_layout()


# ------------------------------------------------------------------------------ #
# strong rise
# ------------------------------------------------------------------------------ #

realign_to = 'Belgium'
realign_ref = None

c_rise = {
    "Spain": 0,
    "France": 0,
    "Belgium": 0,
    "Switzerland": 0,
    "Czech Republic": 0,
    "Austria": 0,
    "Netherlands": 0,
    "Italy": 0,
    "Poland": 0,
    "Germany": 0,
    "Denmark": 0,
    "Norway": 0,
    "Finland": 0,
}


def set_offset(country_dict, threshold):
    for c in country_dict.keys():
        dat = owd._filter(
            value="new_cases_smoothed_per_million",
            country=c,
            data_begin=datetime.datetime(2020, 8, 1),
        )
        try:
            offset = int(-np.where(dat > threshold)[0][0])
            if c == realign_to:
                global realign_ref
                realign_ref = dat.index[-offset]
        except:
            offset = 0

        country_dict[c] = offset

    realign = country_dict[realign_to]
    for c in country_dict.keys():
        if country_dict[c] != 0:
            country_dict[c] -= realign


    return country_dict


def plot_rise(
    countries, data_begin, data_end, ax, offsets, color_dict,
):

    if ax is None:
        fig, ax = plt.subplots()

    df = pd.DataFrame()

    for idx, c in enumerate(countries):
        if offsets is not None:
            assert c in offsets.keys()
            o = offsets[c]
        else:
            o = 0

        dat = owd._filter(
            value="new_cases_smoothed_per_million",
            country=c,
            data_begin=data_begin,
            data_end=data_end,
        )
        df[c] = dat
        dat.index = dat.index + datetime.timedelta(days=int(o))

        try:
            if c == realign_to:
                # ref = data_begin + datetime.timedelta(days=realign_ref)
                ax.axvline(x=realign_ref, zorder=2, color='gray')
                log.info(f"aligned at: {realign_ref}")
        except Exception as e:
            log.info(e)

        ax.plot(dat, label=f"{c} ({o} days)", color=color_dict[c])

    ax.legend(loc="upper left")
    ax.set_xlim(bd, ed)



    format_x(ax)

    return ax.get_figure(), ax




c_rise = set_offset(c_rise, threshold=100)

fig, ax = plt.subplots()
ax.set_ylabel("New cases per million inhabitants\n(running avg. over 7 days)")

bd = datetime.datetime(2020, 5, 1) + datetime.timedelta(days = int(c_rise[realign_to]))
ed = datetime.datetime.now()
# ed = datetime.datetime(2020, 10, 25)
plot_rise(
    countries=c_rise.keys(),
    data_begin=bd,
    data_end=ed,
    ax=ax,
    offsets=c_rise,
    color_dict=c_mid,
)

ax.set_ylim(0, 500)
# ax.xaxis.set_ticklabels([])


# ------------------------------------------------------------------------------ #
# export everything
# ------------------------------------------------------------------------------ #

for i in plt.get_fignums():
    plt.figure(i)
    plt.savefig(f"/Users/paul/Desktop/figure_{i:d}.pdf", dpi=600)
