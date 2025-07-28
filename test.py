import open3d as o3d

if __name__ == '__main__':
    pcd = o3d.geometry.PointCloud()
    o3d.visualization.draw_geometries([pcd]) # type: ignore