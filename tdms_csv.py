# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 19:56:04 2015

@author: tony
"""
from nptdms import TdmsFile


tdms_file = TdmsFile("clogged capillary.tdms")

df = tdms_file.as_dataframe()

# the column names are a bit rough by default.  we'll clean them up
newnames = df.columns.values
for i in range(len(newnames)):
    if newnames[i] == '/':
        newnames[i] = 'root'
    else:
        temp = newnames[i].split('/')
        newnames[i] = str(temp[-1])

df.columns = newnames

# remove any columns with no data
df=df.dropna(axis=1, how='all')

# we'll also remove the first ten rows
df = df.drop(df.index[[range(10)]])

# we'll save this as a csv for fun
df.to_csv('clogged_cap.csv')
