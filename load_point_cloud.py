import os
import numpy as np

from viz_plotly import Plotly
from PointCloudDataLoader import PointCloudDataLoader
from odometry import ICP

def main():
    # Load point cloud data
    current__path = os.path.dirname(os.path.abspath(__file__))
    print('Current folder path is: {}'.format(current__path))
    point_cloud_folder_path = os.path.join(current__path, 'point_cloud_data')
    pc_loader = PointCloudDataLoader(point_cloud_folder_path)
    

    # Run ICP
    old_scan = pc_loader.point_clouds[0]
    new_scan = pc_loader.point_clouds[1]

    odom =  ICP(old_scan, new_scan)
    odom.range_filtering(min_range=4, max_range=50)
    odom.run_icp(method='point_to_plane')
    odom.run_icp(method='point_to_point')



if __name__ == '__main__':
    main()