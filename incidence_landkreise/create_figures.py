# ------------------------------------------------------------------------------ #
# @Author:        Sebastian B. Mohr
# @Email:
# @Created:       2020-10-27 11:13:12
# @Last Modified: 2020-12-17 20:02:07
# ------------------------------------------------------------------------------ #
"""
Script to create an animated gif of the incidence in each age group.
Run timeseries.py for new data!

Runtime: 15-20mins
"""

import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import datetime
from tqdm.auto import tqdm
import imageio

mpl.rcParams["font.sans-serif"] = "Arial"
mpl.rcParams["font.family"] = "sans-serif"

# Agegroups
groups = ["A00-A04", "A05-A14", "A15-A34", "A35-A59", "A60-A79", "A80+"]

# Load geojson file for underground
df_places = gpd.read_file("./data/landkreise_simplify200.geojson")

# Color of plot
cmap = plt.get_cmap("YlOrRd")
count = 0

# Progressbar
pbar = tqdm(
    total=pd.date_range(
        start=datetime.datetime(2020, 3, 2), end=datetime.datetime.now()
    ).size
    * len(groups),
    position=1,
)

# Images dictionary for each agegroup
images = {}
for g in groups:
    images[g] = []


# Loop over each date
for date in pd.date_range(
    start=datetime.datetime(2020, 3, 2), end=datetime.datetime.now()
):

    # Load json with casenumbers
    try:
        df = pd.read_json(
            f"./data/ts/data_{date.strftime('%d_%m')}.json", orient="values"
        )
    except Exception as e:
        break

    df = df.T
    df.index.name = "RS"
    df = df.reset_index()
    df["RS"] = df["RS"].astype(str).apply(lambda x: x.zfill(5))

    merged = df_places.merge(df, left_on="RS", right_on="RS")

    # Create a plot for every agegroup:
    for i, age_group in enumerate(groups):
        fig, ax = plt.subplots(1, 1, figsize=(3.5, 4))
        cm = merged.plot(
            column=f"inzidenz_{age_group}", ax=ax, cmap=cmap, vmin=0, vmax=300
        )

        # ------------------------------------------------------------------------------ #
        # Visual markup
        # ------------------------------------------------------------------------------ #
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        for spine in ax.spines:
            ax.spines[spine].set_visible(False)

        # Text of date
        fig.text(
            0.36,
            0.75,
            date.strftime("%-d. %B %Y"),
            fontsize=8,
            ha="right",
            weight="bold",
        )

        # Colorbar
        cax = fig.add_axes([0.84, 0.1, 0.03, 0.8])
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=300))
        # fake up the array of the scalar mappable. Urgh...
        sm._A = []
        cb = fig.colorbar(sm, cax=cax)
        cb.ax.set_xlabel(
            "Fälle pro\n100.000 EW", horizontalalignment="left", fontsize=8
        )
        cb.ax.tick_params(axis="y", labelsize=8)
        cb.ax.xaxis.set_label_coords(-1.2, -0.025)
        fig.savefig(
            f"./figures/{age_group}/{str(count).zfill(4)}.png",
            transparent=True,
            dpi=300,
        )
        images[age_group].append(
            imageio.imread(f"./figures/{age_group}/{str(count).zfill(4)}.png")
        )
        plt.close(fig)
        pbar.update(1)
        # Append to array for gif
    count = count + 1

pbar.close()


print("Combining images to gifs (could take a min)!")
for age_group in groups:
    imageio.mimsave(
        f"{age_group}.mp4",
        images[age_group],
        fps=10,
        quality=10,
        codec="mjpeg",
        pixelformat="yuvj444p",
    )
