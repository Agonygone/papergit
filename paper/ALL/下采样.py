import time

import numpy as np
import open3d as o3d
import pandas as pd


def cleartxt(path):
    with open(path, 'a+', encoding='utf-8') as test:
        test.truncate(0)
        test.close()


cleartxt('边长.txt')
cleartxt('采样率.txt')
cleartxt('主法向之差.txt')
cleartxt('差值-采样率.txt')
cleartxt('计算时间.txt')


def ts(i):
    pcd = o3d.io.read_point_cloud("去噪最终结果.pcd")  # 导入数据
    start = time.time()
    aa = str(pcd).strip('PointCloud with ').strip(' points.')
    print('源数据量', aa)
    downpcd = pcd.voxel_down_sample(voxel_size=i)  # 下采样处理
    print('L取值', i)
    bb = str(downpcd).strip('PointCloud with ').strip(' points.')
    print('下采样后的数据量', bb)
    cc = int(bb) / int(aa)
    print('下采样率', cc)
    # 计算下采样后数据的法向量情况
    ε = 0.05
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.01, max_nn=30))
    DD = np.asarray(pcd.normals)
    df1 = pd.DataFrame(DD, columns=['Nx', 'Ny', 'Nz'])
    dfx0 = df1[(abs(df1['Nx']) <= ε) & ((abs(df1['Nz']) - 1) <= ε) & (abs(df1['Ny']) <= ε)]
    Ndown = len(dfx0)
    NN1 = Ndown / int(aa)

    downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.01, max_nn=30))
    DD1 = np.asarray(downpcd.normals)
    df01 = pd.DataFrame(DD1, columns=['Nx', 'Ny', 'Nz'])
    dfx1 = df01[(abs(df01['Nx']) <= ε) & ((abs(df01['Nz']) - 1) <= ε) & (abs(df01['Ny']) <= ε)]
    Ndown1 = len(dfx1)
    NN2 = Ndown1 / int(bb)

    print('源数据主法向占比', NN1)
    print('采样后主法向占比', NN2)
    print('主法向之差', NN2 - NN1)
    print('主法向之差-采样率', abs(NN2 - NN1 - cc))
    end = time.time()
    f1 = open('边长.txt', 'a')
    f1.write(str(i))
    f1.write('\n')
    f1.close()
    f2 = open('采样率.txt', 'a')
    f2.write(str(cc))
    f2.write('\n')
    f2.close()
    f3 = open('主法向之差.txt', 'a')
    f3.write(str(NN2 - NN1))
    f3.write('\n')
    f3.close()
    f4 = open('差值-采样率.txt', 'a')
    f4.write(str(abs(NN2 - NN1 - cc)))
    f4.write('\n')
    f4.close()
    f5 = open('计算时间.txt', 'a')
    f5.write(str(round(end - start, 4)))
    f5.write('\n')
    f5.close()


for j in range(0, 100, 1):
    i = (j + 1) / 1000
    ts(i)

