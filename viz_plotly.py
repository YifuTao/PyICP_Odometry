import plotly.graph_objects as go

class Plotly:
    def __init__(self):
        self.plotly_output = []
        self.save_path = 'example_point_cloud.html'
    def visualise(self):
        fig = go.Figure(
            data=self.plotly_output,
            layout=dict(
                title='3D LiDAR Point Cloud from CARLA Simulator',
                scene=dict(
                    xaxis=dict(visible=True),
                    yaxis=dict(visible=True),
                    zaxis=dict(visible=True),
                    aspectmode='data', # this controls the scale of the axes
                )
            ),

        )
        fig.show()
        fig.write_html(self.save_path)
    def add_axies(self):
        # Create xyz axies: x-Red, y-Green, z-Blue
        self.plotly_output.append(go.Scatter3d(x=[0, 10], y=[0, 0], z=[0, 0],
                                    mode='lines', 
                                    line=dict(color='red', width=10,),
                                    name='x-axis',
                                    legendgroup='axis'))
        self.plotly_output.append(go.Scatter3d(x=[0, 0], y=[0, 10], z=[0, 0],
                                    mode='lines', 
                                    line=dict(color='green', width=10,),
                                    name='y-axis',
                                    legendgroup='axis'))
        self.plotly_output.append(go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, 10],
                                    mode='lines', 
                                    line=dict(color='blue', width=10,),
                                    name='z-axis',
                                    legendgroup='axis'))
    def add_point_cloud(self, points):
        point_cloud = go.Scatter3d(x=points[:,0], y=points[:,1], z=points[:,2],
                        mode='markers', 
                        marker=dict(
                            size=1,color=points[:,2],
                            colorscale='Viridis', 
                            colorbar=dict(title='Z',len=0.5)),
                        name='point cloud',
                        )
        self.plotly_output.append(point_cloud)