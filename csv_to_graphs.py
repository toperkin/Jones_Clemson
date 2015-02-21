# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('clogged_cap.csv', index_col=0)

LENGTH_OF_ROLLING_MEAN = 10

mg = df[(284.8 < df.wavelength) & (df.wavelength <= 285.3)].mean()
mg = mg.drop('wavelength')
mg_mean = pd.rolling_mean(mg, LENGTH_OF_ROLLING_MEAN, center=True)

oh = df[(309 < df.wavelength) & (df.wavelength <= 309.99)].mean()
oh = oh.drop('wavelength')
oh_mean = pd.rolling_mean(oh, LENGTH_OF_ROLLING_MEAN, center=True)

ag328 = df[(327.4 < df.wavelength) & (df.wavelength <= 328.4)].mean()
ag328 = ag328.drop('wavelength')
ag328_mean = pd.rolling_mean(ag328, LENGTH_OF_ROLLING_MEAN, center=True)

ag338 = df[(337.9 < df.wavelength) & (df.wavelength <= 338.4)].mean()
ag338 = ag338.drop('wavelength')
ag338_mean = pd.rolling_mean(ag338, LENGTH_OF_ROLLING_MEAN, center=True)

cs = df[(852 < df.wavelength) & (df.wavelength <= 852.4)].mean()
cs = cs.drop('wavelength')
cs_mean = pd.rolling_mean(cs, LENGTH_OF_ROLLING_MEAN, center=True)


plt.figure(figsize=(12, 9))
plt.xlabel('Seconds')
plt.ylabel('Average signal intensity')
ax = mg_mean.plot(label='mg', legend=True)
oh_mean.plot(label='oh', legend=True, ax=ax)
ag328_mean.plot(label='ag328', legend=True, ax=ax)
ag338_mean.plot(label='ag338', legend=True, ax=ax)
cs_mean.plot(label='cs', legend=True, ax=ax)

plt.savefig('clogged_cap')
