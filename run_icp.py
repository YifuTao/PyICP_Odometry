import os
import numpy as np
import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), 'util'))
print(sys.path)
from icp_odometry.PointCloudDataLoader import PointCloudDataLoader
from icp_odometry.odometry import Odometry
from icp_odometry.util.util_pc import savePlyFromPtsRGB
from icp_odometry.util.util_viz import Plotly
from icp_odometry.util.util_spatial import convert_translation_quaternion_to_matrix

def main():
    # Load point cloud data
    
    current__path = os.path.dirname(os.path.abspath(__file__))
    print('Current folder path is: {}'.format(current__path))
    point_cloud_folder_path = os.path.join(current__path, 'point_cloud_data')
    pc_loader = PointCloudDataLoader(point_cloud_folder_path)

    first_n_point_clouds= 3
    # first_n_point_clouds = len(pc_loader.point_clouds)
    # save original point clouds
    for i in range(first_n_point_clouds):
        savePlyFromPtsRGB(pc_loader.point_clouds[i], 
                    os.path.join(current__path, 'ply','original', pc_loader.point_clouds_name[i] + '.ply'))
    # Compute trajectory
    odom = Odometry(pc_loader.point_clouds[:first_n_point_clouds], 
                    pc_loader.point_clouds_name[:first_n_point_clouds],
                    save_path=os.path.join(current__path, 'ply/transformed'))
    first_pose = convert_translation_quaternion_to_matrix([186.016083, -302.859222, 2.694699],
                                                        [0.003342, 0.001963, 0.129341, 0.991593])
                                                        
    traj = odom.compute_trajectory(method='point_to_plane',first_pose=first_pose, 
                                    save_individual_poses_ply=True, save_trajectory_txt=True)
    # points_W = odom.transform_trajectory_points(traj) # points in world frame
    # for i in range(len(points_W)):
    #     savePlyFromPtsRGB(points_W[i], 
    #                 os.path.join(current__path, 'ply','transformed', pc_loader.point_clouds_name[i] + '_W.ply'))




if __name__ == '__main__':
    main()