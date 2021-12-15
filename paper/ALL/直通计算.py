import numpy as np
import pandas as pd

data = np.loadtxt('top一部分.txt')

print(max(data[:, 0]), min(data[:, 0]))
print(max(data[:, 1]), min(data[:, 1]))
print(max(data[:, 2]), min(data[:, 2]))

data = np.loadtxt('噪点一部分.txt')

print(max(data[:, 0]), min(data[:, 0]))
print(max(data[:, 1]), min(data[:, 1]))
print(max(data[:, 2]), min(data[:, 2]))
#
data = np.loadtxt('las1358_50W.txt')
print(max(data[:, 0]), min(data[:, 0]))
print(max(data[:, 1]), min(data[:, 1]))
print(max(data[:, 2]), min(data[:, 2]))
