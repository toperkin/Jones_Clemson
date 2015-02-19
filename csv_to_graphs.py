# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 18:50:24 2015

@author: tony
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('clogged_cap.csv', index_col=0)
print(df.head(5))

mg = df[(284.8< df.wavelength) & (df.wavelength <=285.3)].mean()
oh = df[(309<df.wavelength) & (df.wavelength <=309.99)].mean()
ag328 = df[(327.4<df.wavelength) & (df.wavelength <=328.4)].mean()
ag338 = df[(337.9<df.wavelength) & (df.wavelength <=338.4)].mean()
cs = df[(852<df.wavelength) & (df.wavelength <=852.4)].mean()

plt.figure()

ax=mg.plot(label='mg')
oh.plot(label='oh', ax=ax)
ag328.plot(label='ag328', ax=ax)
ag338.plot(label='ag338', ax=ax)
cs.plot(label='cs', ax=ax)

plt.savefig('clogge_cap')