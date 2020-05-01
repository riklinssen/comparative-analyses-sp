import datetime
import getpass
import glob
import os
import re
from pathlib import Path, PureWindowsPath, WindowsPath

import numpy as np
import pandas as pd
import statsmodels.stats.api as sms


username = getpass.getuser()

#filepaths for data
base_path = Path(__file__).parents[1]
data_path = base_path/"Data"
raw_data_path=base_path/"Data\Raw"
graphs_path = base_path/"Visualisations"
clean_data_path=base_path/"Data\Clean"

files = pd.read_csv(raw_data_path/"filelist_by_project.csv", sep=';', header=0)
files['filelocation_cleaned']=[f.replace('RikL', username) for f in files.filelocation_cleaned]
files['name']=files.country + '_' + files.project
filelist= [ Path(f) for f in files.filelocation_cleaned]


frames = {}

for f, cntry in zip(filelist, files.name):
    df = pd.read_stata(f)
    frames[cntry] = df

for name in files.name:
    df=frames[name]
    print(frames[name].info())
    filename=name+'.pkl'
    fileloc=Path(clean_data_path/filename)
    df.to_pickle(fileloc)
