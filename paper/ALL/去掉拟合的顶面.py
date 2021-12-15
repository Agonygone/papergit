import math
import time
import pandas as pd
from pandas import DataFrame
from pyntcloud import PyntCloud
import numpy as np
import open3d as o3d

data1 = np.loadtxt('off-ground points2.txt')
data2 = np.loadtxt('top.txt')

a = pd.DataFrame(data1)
b = pd.DataFrame(data2)
c = pd.concat([a,b],axis=0)

print(c)
d = c.drop_duplicates(keep=False)
d.to_csv('去掉顶面.txt',index_label=False,index=False,header=False)
print(d)

d.columns = ['x','y','z']
d1 = d[d['z']-10]
print(d1)
d.to_csv('去掉顶面.txt',index_label=False,index=False,header=False)