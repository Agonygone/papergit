import pandas as pd
import numpy as np

data = np.loadtxt('坐标表.csv', delimiter=',')
data = pd.DataFrame(data[0:6, :], columns=['x', 'y', 'z'])
print(data)
