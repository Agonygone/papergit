import time

import matplotlib.pyplot as plt
import numpy as np
import open3d as o3d

pcd = o3d.io.read_point_cloud(r"D:\PycharmProject\论文需要\RANSAC\outer\outer2.pcd")
start = time.time()
point = np.asarray(pcd.points)  # 获取点坐标
kdtree = o3d.geometry.KDTreeFlann(pcd)  # 建立KD树索引
point_size = point.shape[0]  # 获取点的个数
dd = np.zeros(point_size)
for i in range(point_size):
    [_, idx, dis] = kdtree.search_knn_vector_3d(point[i], 2)
    dd[i] = dis[1]  # 获取到最近邻点的距离平方
density = np.mean(np.sqrt(dd))
pcd = o3d.io.read_point_cloud(r"D:\PycharmProject\论文需要\RANSAC\outer\outer2.pcd")
# 设置为debug调试模式
with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
    # -------------------密度聚类--------------------------
    labels = np.array(pcd.cluster_dbscan(eps=0.01,  # 邻域距离
                                         min_points=50,
                                           # 最小点数
                                         print_progress=True))  # 是否在控制台中可视化进度条
max_label = labels.max()
print(f"point cloud has {max_label + 1} clusters")
# ---------------------保存聚类结果------------------------
for i in range(max_label + 1):
    ind = np.where(labels == i)[0]
    clusters_cloud = pcd.select_by_index(ind)
    file_name = "Dbscan_cluster" + str(i + 1) + ".pcd"
    # print(clusters_cloud)
    pointnum= int(str(clusters_cloud).strip('PointCloud with ').strip(' points.'))
    if pointnum > 10000:
        print(pointnum)
        o3d.io.write_point_cloud(file_name, clusters_cloud)
        o3d.visualization.draw_geometries([clusters_cloud], window_name="DBSCAN处理",
                                          width=1024, height=768,
                                          left=50, top=50,
                                          mesh_show_back_face=False)

end =time.time()
print(end-start)
# # --------------------可视化聚类结果----------------------
colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
colors[labels < 0] = 0
pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
o3d.visualization.draw_geometries([pcd], window_name="点云密度聚类",
                                  height=480, width=600,
                                  mesh_show_back_face=0)
