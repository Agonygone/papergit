import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import open3d as o3d

pcd = o3d.io.read_point_cloud("体素栅格.pcd")
print(pcd)  # 输出点云点的个数
# 计算法线，搜索半径1cm，只考虑邻域内的30个点
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.01, max_nn=30))
print(np.asarray(pcd.normals))
np.savetxt('体素栅格法向量.txt', np.asarray(pcd.normals))
DD = np.asarray(pcd.normals)

# DD = np.loadtxt('体素栅格法向量.txt')
df2 = pd.DataFrame(DD, columns=['Nx', 'Ny', 'Nz'])
print(df2)
df2.plot(kind='kde')
plt.show()
