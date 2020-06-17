""" #Plot
Script to plot the measures on a timescale 
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
import sys
import numpy as np

sys.path.append("../../covid19_inference-model_cleanup")
from covid19_inference import plot as covplt

from measure import get_measures,get_possible_countries
import keywords as kw

def plot_measure_onto_axes(ax,measure,**kwargs):
    """
    Plots the measures on a timeline, whereby the x axis is time and the y axis is the country.

    Parameters
    ----------
    measures : one measure

    y_pos: number
    """
    print(f"Begin = {measure.begin} \t End={measure.end} \t {measure.country}")
    x = np.array([measure.begin,measure.end])
    y = np.array([measure.country]*len(x))
    covplt._timeseries(x=x,y=y,ax=ax,what="model",**kwargs)

    ax.set_xlim(datetime.datetime(2020,3,1),datetime.datetime.today()+datetime.timedelta(days=2))
    #ax.set_ylim(-1,y_pos+1)
    return ax



countries = get_possible_countries()

fig, axes = plt.subplots(1,1,figsize=(10,4))

measures = get_measures(tag="lockdown")
for m, measure in enumerate(measures):
    plot_measure_onto_axes(axes, measure,lw=10,alpha=0.5)
    axes.set_title("Lockdown measures in different countries")
    axes.axvline(datetime.datetime.today(),ls=":")
""" ## Plot for every country
"""


