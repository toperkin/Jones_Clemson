# -*- coding: utf-8 -*-
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
    if newnames[i] == "'Header and Wavelength'":
        newnames[i] = 'wavelength'
    if 'Grid' in newnames[i]:
        temp2 = newnames[i].split('-')
        temp3 = temp2[1].split("'")
        temp4 = (float(temp3[0])-1)/10
        newnames[i] = temp4

df.columns = newnames

# remove any columns with no data
df = df.dropna(axis=1, how='all')

# put the columns in the order corresponding to their shot number
df = df.sort_index(axis=1)

# we'll also remove the first ten rows
df = df.drop(df.index[[range(10)]])

# we'll save this as a csv for fun
df.to_csv('clogged_cap.csv')
