import time

import matplotlib.pyplot as plt
import pandas as pd
import open3d as o3d
import numpy as np

pcd = o3d.io.read_point_cloud(r"Dbscan_cluster1.pcd")
start = time.time()
point = np.asarray(pcd.points)  # 获取点坐标
kdtree = o3d.geometry.KDTreeFlann(pcd)  # 建立KD树索引
point_size = point.shape[0]  # 获取点的个数
dd = np.zeros(point_size)
for i in range(point_size):
    [_, idx, dis] = kdtree.search_knn_vector_3d(point[i], 2)
    dd[i] = dis[1]  # 获取到最近邻点的距离平方
density = np.mean(np.sqrt(dd))  # 计算平均密度


# print("点云密度为 denstity=", density)


def pl(j):
    # print('阈值')
    # di = density+j
    # print(di)
    plane_model, inliers = pcd.segment_plane(distance_threshold=0.015,
                                             ransac_n=1500,
                                             num_iterations=500 + int(j))

    [a, b, c, d] = plane_model
    print(a, b, c, d)
    # print(round(a, 3), round(b, 3), round(c, 3), round(d, 3))
    end = time.time()
    print(end-start)
    inlier_cloud = pcd.select_by_index(inliers)
    inter = np.asarray(inlier_cloud.points)
    x_, y_, z_ = np.mean(inter[:, 0]), np.mean(inter[:, 1]), np.mean(inter[:, 2])
    D = abs(a * (inter[:, 0] - x_)) + abs(b * (inter[:, 1] - y_)) + abs(c * (inter[:, 2] - z_))
    Dd = pd.DataFrame(D)
    # print('点到平面距离计算')
    # Dd.to_csv('outer/点距离' + str(i) + '.csv', header=False, index=False, index_label=False)
    std = Dd.std(axis=0)
    # print('标准差')
    # print(std)
    # mean = np.mean(Dd)
    # print('均值')
    # print(mean)
    # print('差值')
    # print(mean-std)
    # print('===================================')
    # l = len(Dd)
    # df = pd.DataFrame(np.arange(l),columns=['x'])
    # df['y']=Dd
    # # print(df)
    # df.plot(kind = 'scatter',x = 'x',y = 'y')
    # # plt.show()


for i in range(0, 5000, 500):
    # print(i/1000)
    j = i + 500
    # print(j)
    pl(j)

# pl(0.001)
