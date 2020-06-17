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



def plot_measure_onto_axes(ax,measure, y_pos,**kwargs):
    """
    Plots the measures on a timeline, whereby the x axis is time and the y axis is the country.

    Parameters
    ----------
    measures : one measure

    y_offset : number,

    """
    print(f"Begin = {measure.begin} \t End={measure.end} \t {measure.country}")
    x = np.array([measure.begin,measure.end])
    y = np.array([y_pos]*len(x))
    covplt._timeseries(x=x,y=y,ax=ax,what="model",**kwargs)

    ax.set_xlim(datetime.datetime(2020,3,1),datetime.datetime.today()+datetime.timedelta(days=2))
    #ax.set_ylim(-1,y_pos+1)
    return ax


def set_tick_labels(y_ticks, strings, ax):
    """
    Parameters
    ----------
    array: of tuples number,string

    """
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(strings)


countries = get_possible_countries()

offset_dict = dict()
offsets= []
temp = 0
num_measures_to_plot_per_country = 2
for c,country in enumerate(countries):
    offset_dict[country]= temp + num_measures_to_plot_per_country + 3
    temp = temp + num_measures_to_plot_per_country + 3
    offsets.append(offset_dict[country]+1)

fig, axes = plt.subplots(1,1,figsize=(12,8))


## Get and plot lockdown measures
measures = get_measures(tag="lockdown")
for m, measure in enumerate(measures):
    plot_measure_onto_axes(axes, measure, y_pos=offset_dict[measure.country],lw=5,alpha=1,color="tab:red")

## Get and plot close schools
measures = get_measures(tag="close schools")
for m, measure in enumerate(measures):
    plot_measure_onto_axes(axes, measure, y_pos=offset_dict[measure.country]+1,lw=5,alpha=1,color="tab:green")


## Get and plot close university
measures = get_measures(tag="close universities")
for m, measure in enumerate(measures):
    plot_measure_onto_axes(axes, measure, y_pos=offset_dict[measure.country]+2,lw=5,alpha=1,color="tab:blue")

set_tick_labels(offsets,countries,axes)



## Extra elements
axes.axvline(x=datetime.datetime.today(),ls=':')



## Create legend
from matplotlib.lines import Line2D

custom_lines = [Line2D([0], [0], color="tab:red", lw=6),
                Line2D([0], [0], color="tab:green", lw=6),
                Line2D([0], [0], color="tab:blue", lw=6)]
axes.legend(custom_lines, ['Lockdown', 'Schools closed', 'Universities closed'])

fig.show()

