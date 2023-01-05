import os
import numpy as np

from viz_plotly import Plotly
from PointCloudDataLoader import PointCloudDataLoader

def main():
    # Load point cloud data

    current__path = os.path.dirname(os.path.abspath(__file__))
    print('Current folder path is: {}'.format(current__path))
    point_cloud_folder_path = os.path.join(current__path, 'point_cloud_data')
    pc_loader = PointCloudDataLoader(point_cloud_folder_path)
    

    plotly = Plotly()
    plotly.add_axies()
    plotly.add_point_cloud(pc_loader.point_clouds[0])
    # plotly.add_point_cloud(pc_loader.point_clouds[1])
    plotly.visualise()
    print('The visualisation is saved to {}'.format(plotly.save_path))

if __name__ == '__main__':
    main()