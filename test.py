import plotly.graph_objects as go
import numpy as np
import os

# 生成随机点云数据
num_points = 2000
points = np.random.rand(num_points, 3) * 10
colors = np.random.rand(num_points, 3)

# 创建3D散点图
fig = go.Figure(data=[go.Scatter3d(
    x=points[:, 0], 
    y=points[:, 1], 
    z=points[:, 2],
    mode='markers',
    marker=dict(
        size=3,
        color=colors,  # 使用RGB颜色
        opacity=0.8
    )
)])

# 设置布局
fig.update_layout(
    title='交互式3D点云',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='cube'
    ),
    width=1000,
    height=700
)

# 保存为HTML文件
path = os.path.join('htmls', 'interactive_point_cloud.html')
fig.write_html(path)