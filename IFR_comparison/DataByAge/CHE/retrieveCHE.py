#!/usr/bin/env python3.7
#coding:utf-8

"""
Retrieves Swiss data from secondary source:

https://rsalzer.github.io/COVID_19_AGE/

"""


import urllib3
import datetime
import os
import pandas as pd

def Process(files):
    age_groups = ["%d-%d"%(x*10,x*10+9) for x in range(8)]+["80+"]
    print(age_groups)
    for k,v in files.items():
        print(k)
        
        df = v["df"]
        if "totalbag" in df:
            del df["totalbag"]
        for ag in age_groups:
            df[ag] = df["m"+ag]+df["f"+ag]
            del df["m"+ag]
            del df["f"+ag]
        
        print(df)
        df.to_csv(v["fn"]+".csv")

def main():

    files = {}
    files["deahts"] = {"fn":"swiss_deaths","url":"https://raw.githubusercontent.com/rsalzer/COVID_19_BAG/master/data/deaths.csv"}
    files["cases"] = {"fn":"swiss_cases","url":"https://raw.githubusercontent.com/rsalzer/COVID_19_BAG/master/data/allagesdetails.csv"}
    files["hospitalized"] = {"fn":"swiss_hospitalized","url":"https://raw.githubusercontent.com/rsalzer/COVID_19_BAG/master/data/hospitalised.csv"}
    
    dt = datetime.datetime.now()
    tindex = "%02d%02d%02d"%(dt.year,dt.month,dt.day)
    
    http = urllib3.PoolManager()
    for k,v in files.items():
        fn,url = v["fn"],v["url"]
        fn_full = tindex+"_"+fn+"_raw.csv"
        if not os.path.exists(fn_full):
            r = http.request('GET',url)
            print(k,r.status)
            
            with open(fn_full,"wb+") as f:
                f.write(r.data)
                
        else:
            print(k,"up to date")
            
        v["df"] = pd.read_csv(fn_full,header=0,index_col=0)
        
    Process(files)

if __name__ == "__main__":
    main()
