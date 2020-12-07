# ------------------------------------------------------------------------------ #
# @Author:        Sebastian B. Mohr
# @Email:
# @Created:       2020-10-27 11:13:12
# @Last Modified: 2020-12-07 10:58:03
# ------------------------------------------------------------------------------ #
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import datetime
from tqdm.auto import tqdm
import imageio

groups = ["A00-A04", "A05-A14", "A15-A34", "A35-A59", "A60-A79", "A80+"]

df_places = gpd.read_file("./data/landkreise_simplify200.geojson")

# Color of plot
cmap = matplotlib.colors.ListedColormap(["#008000", "#ffd700", "#e50000"])
images = []
count = 0
pbar = tqdm(
    total=pd.date_range(
        start=datetime.datetime(2020, 10, 1), end=datetime.datetime.now()
    ).size
)
for date in pd.date_range(
    start=datetime.datetime(2020, 10, 1), end=datetime.datetime.now()
):

    # Load json
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
    fig, axes = plt.subplots(2, 3, figsize=(16, 9))
    for i, age_group in enumerate(groups):
        if i > 2:
            k = i - 3
            j = 1
        else:
            k = i
            j = 0
        merged.plot(
            column=f"inzidenz_{age_group}", ax=axes[j, k], cmap=cmap, vmin=0, vmax=75,
        )
        axes[j, k].axes.xaxis.set_visible(False)
        axes[j, k].axes.yaxis.set_visible(False)
        axes[j, k].set_title(f"{age_group}")
    # Get legend

    custom_lines = [
        Patch(facecolor=cmap(0),),
        Patch(facecolor=cmap(0.5),),
        Patch(facecolor=cmap(1.1),),
    ]

    fig.legend(custom_lines, [" 0-25", "25-50", "50+"], title="Fälle/100.000EW")
    fig.text(0.51, 0.05, date.strftime("%d. %B"), fontsize=20, ha="center")
    fig.savefig(
        f"./figures/{str(count).zfill(4)}.png", transparent=True, dpi=300,
    )

    # Append to array for gif
    images.append(imageio.imread(f"./figures/{str(count).zfill(4)}.png"))
    count = count + 1
    pbar.update(1)
pbar.close()
imageio.mimsave("Landkreise.gif", images, "GIF", fps=2)
