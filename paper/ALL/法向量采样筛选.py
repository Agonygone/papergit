import math

import numpy as np
import pandas as pd

dev = np.loadtxt('主法向之差.txt')
data = pd.DataFrame(dev, columns=['dev'])
data = round(data['dev'], 2)

L = np.loadtxt('边长.txt')
dataL = pd.DataFrame(L, columns=['l'])

data0 = pd.concat([dataL, data], axis=1)
data1 = data0.sort_values(by='dev',ascending=False)
data2 = data1.drop_duplicates(subset=['dev'], keep='last', inplace=False)


