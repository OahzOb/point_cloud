import plotly.graph_objects as go
import numpy as np
import os
from functools import singledispatch
import open3d as o3d
import logging
import config
import datetime

log_filename = datetime.date.today().isoformat() + '.log'
logging.basicConfig(
    filename=os.path.join(config.pathConfig.log_dir, log_filename),
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s | %(message)s'
)

def points2html(points: np.ndarray, mode: str = 'scatter'):
    num_points = len(points)
    if num_points == 0:
        return
    if points.shape[1] >= 6: 
        colors = points[:, 3:6]
    else:
        colors = np.random.rand(num_points, 3)
    if mode == 'scatter':
        fig = go.Figure(data=[go.Scatter3d(
            x=points[:, 0],
            y=points[:, 1],
            z=points[:, 2],
            mode='markers',
            marker=dict(
                size=3,
                color=colors,
                opacity=0.8
            )
        )])
        fig.update_layout(
            title='scatter',
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z',
                aspectmode='cube'
            ),
            width=1000,
            height=700
        )
    path = os.path.join(config.pathConfig.html_dir, 'pcd.html')
    fig.write_html(path)
    logging.info(f"Wrote pcd html at {path}")


@singledispatch
def pcd2html(pcd, mode: str = 'scatter'):
    raise NotImplementedError(f"Unsupported pcd type: {type(pcd)}")


@pcd2html.register(o3d.geometry.PointCloud)
def _(pcd: o3d.geometry.PointCloud, mode: str = 'scatter'):
    points = pcd.points
    points2html(points=points, mode=mode)


@pcd2html.register(np.ndarray)
def _(pcd: np.ndarray, mode: str = 'scatter'):
    points2html(points=pcd, mode=mode)

if __name__ == '__main__':
    # 生成随机点云数据
    num_points = 2000
    points = np.random.rand(num_points, 3) * 10
    pcd2html(points)
