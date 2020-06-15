
from data.data_retrieval import get_all_icu_cases
import matplotlib.pyplot as plt

import sys
sys.path.append('../../../covid19_inference')
import covid19_inference as cov19
import datetime
""" # Retrieve data
"""

icu = get_all_icu_cases()




jhu = cov19.data_retrieval.JHU(True)

new_cases = dict()
for key in icu:
    new_cases[key]=jhu.get_new(country=key.title(),data_begin=datetime.datetime(2020,3,1))

# For some strange reason spain and portugal have faulty values
new_cases["Spain"].drop(datetime.datetime(2020,4,24))
new_cases["Portugal"].drop(datetime.datetime(2020,5,2))

""" # Create an plot for each country

    For each country we want one axes
    * total new cases
    * icu cases
    * percent in icu
"""

for key in icu:
    print(f"Country: {key}")
    # Create figure
    fig, axes = plt.subplots(2,1,figsize=(10,4))
    axes[0].set_title(f"Intensive care covid patients in {key}")

    # Plot on first axes
    cov19.plot._timeseries(
        x=icu[key]["cases"].index,
        y=icu[key]["cases"],
        ax=axes[0])
   
    # Plot on second axes
    cov19.plot._timeseries(
        x=new_cases[key].index,
        y=new_cases[key],
        ax=axes[1])    

    # Labels
    axes[0].set_ylabel("In ICU")
    axes[1].set_ylabel("Daily new cases (JHU)")
    if key == "Austria":
        axes[0].set_ylim(0,30)
        axes[0].set_ylabel("Percent of icu beds\n occupied by covid patients")
        
    for ax in axes:
        ax.set_xlim(datetime.datetime(2020,3,1),datetime.datetime.today())
    plt.tight_layout()
    plt.savefig(f"figures/icu_{key}.pdf",dpi=300,transparent=True) 