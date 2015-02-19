# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 19:56:04 2015

@author: tony
"""

from nptdms import TdmsFile
import numpy as np
import pandas as pd

tdms_file = TdmsFile("clogged capillary.tdms")

fname_template = 'Grid Location # 1-{i}'
channel = tdms_file.object('Header Info','Header and Wavelength')
data = channel.data
data[0:10]=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
wavelengths = np.asarray(data, dtype=float)

shots=np.vstack(tdms_file.object('Main Group', fname_template.format(i=i)).data for i in range(1, len(tdms_file.group_channels('Main Group'))+1))
final = np.vstack((wavelengths,shots))

#np.savetxt("clogged_cap.csv", final[:,10:].T, delimiter=",")


fname_template = 'Shot{i}'
header=[fname_template.format(i=i) for i in range(1, len(tdms_file.group_channels('Main Group'))+1)]
header = ['wavelength']+header

df = pd.DataFrame(final[:,10:].T, columns=header)

df.to_csv('clogged_cap.csv')