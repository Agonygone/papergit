import open3d as o3d
import time

start = time.time()
# mesh = o3d.geometry.TriangleMesh.create_sphere()
mesh = o3d.io.read_triangle_mesh('bim1358.obj')
mesh.compute_vertex_normals()
# o3d.visualization.draw_geometries([mesh],width=800,height=800)
pcd = mesh.sample_points_uniformly(number_of_points=366605)#
end = time.time()
# o3d.visualization.draw_geometries([pcd],width=600,height=600)
o3d.io.write_point_cloud(r"D:\PycharmProject\论文需要\对比\bim1358.pcd", pcd)

# o3d.io.write_triangle_mesh("copy_of_knot.ply", mesh) # 保存mesh
print(end-start)
