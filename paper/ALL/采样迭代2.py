import time

import numpy as np
import open3d as o3d
import pandas as pd


def ts(i):
    start = time.time()
    pcd = o3d.io.read_point_cloud("去噪最终结果.pcd")
    aa = str(pcd).strip('PointCloud with ').strip(' points.')
    print(aa)
    downpcd = pcd.voxel_down_sample(voxel_size=i)
    print(i)
    o3d.io.write_point_cloud('体素栅格.pcd', downpcd)
    bb = str(downpcd).strip('PointCloud with ').strip(' points.')
    print(bb)

    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.01, max_nn=30))
    np.savetxt('体素法向量.' + str(i) + 'txt', np.asarray(pcd.normals))
    DD = np.asarray(pcd.normals)
    df2 = pd.DataFrame(DD, columns=['Nx', 'Ny', 'Nz'])
    ε = 0.05
    dfx0 = df2[(abs(df2['Nx']) <= ε) & ((abs(df2['Nz']) - 1) <= ε) & (abs(df2['Ny']) <= ε)]
    print(len(dfx0))
    # end = time.time()
    # print(round(end - start, 4))
    # cc = round(end - start, 4)
    # f = open('下采样记录.txt', 'a')
    # f.write(str(i))
    # f.write('\n')
    # f.write(aa)
    # f.write('\n')
    # f.write(bb)
    # f.write('\n')
    # f.write(str(cc))
    # f.write('\n')
    # f.close()

ts(0.05)

# for j in range(0, 100, 1):
#     i = (j + 1) / 1000
#     ts(i)

