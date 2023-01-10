import os
import numpy as np

# from icp import ICP
from icp_odometry.icp.icp import ICP
from icp_odometry.util.util_pc import transform_pc, savePlyFromPtsRGB
from icp_odometry.util.util_spatial import convert_matrix_to_translation_quaternion


class Odometry:
    def __init__(self, point_clouds_np, point_clouds_name, save_path=None):
        self.point_clouds_np = point_clouds_np
        self.point_clouds_name = point_clouds_name
        self.poses_stamped = []
        if save_path is None:
            self.save_path = os.path.dirname(os.path.abspath(__file__))
        else: 
            self.save_path = save_path
            os.makedirs(self.save_path, exist_ok=True)
        print('Save path is: {}'.format(self.save_path))


    def compute_trajectory(self, method='point_to_plane', first_pose=np.eye(4), 
                            save_individual_poses_ply=False, save_trajectory_txt=False):
        '''
        :param method: point-to-point or point-to-plane
        :param first_pose: 4x4 transformation matrix for the first point cloud
        :return: 4x4 transformation matrix T_old__new i.e. transform new scan to old scan's frame
        '''
        if save_trajectory_txt:
            save_pose_file_path = os.path.join(self.save_path,'pose.txt')
            with open(save_pose_file_path, 'w') as f:
                f.write('# timestamp tx ty tz qx qy qz qw\n')  
        trajectory = []
        trajectory.append(first_pose)
        self.write_pose_to_txt_TUM(first_pose, self.point_clouds_name[0], save_pose_file_path)

       

        for i in range(len(self.point_clouds_np)-1):
            old_scan = self.point_clouds_np[i]
            new_scan = self.point_clouds_np[i+1]
            icp =  ICP(old_scan, new_scan)
            icp.range_filtering(min_range=3, max_range=100)
            if method == 'point_to_point':
                T_old_new = icp.icp_point_to_point()
            elif method == 'point_to_plane':
                T_old_new = icp.icp_point_to_plane()
            else: raise ValueError('method should be point_to_point or point_to_plane')
            T_W_old = trajectory[i]
            T_W_new = np.matmul(T_W_old, T_old_new)
            trajectory.append(T_W_new)
            if save_individual_poses_ply:
                savePlyFromPtsRGB(transform_pc(T_W_new, new_scan), 
                    os.path.join(self.save_path, self.point_clouds_name[i+1] + '.ply'))
            if save_trajectory_txt:
                self.write_pose_to_txt_TUM(T_W_new, self.point_clouds_name[i+1], save_pose_file_path)
        return trajectory
    def transform_trajectory_points(self, trajectory):
        '''
        :param trajectory: 4x4 transformation matrix T_WB i.e. transform points from base frame to world frame
        :return: transformed points in world frame
        '''
        assert len(trajectory) == len(self.point_clouds_np)
        transformed_points = []
        for i in range(len(self.point_clouds_np)):
            T = trajectory[i]
            scan = self.point_clouds_np[i]
            transformed_scan = transform_pc(T, scan)
            transformed_points.append(transformed_scan)
        return transformed_points
            
    
    def write_pose_to_txt_TUM(self, T, timestamp, file_path):
        with open(file_path, 'a') as f:
            translation, quaternion = convert_matrix_to_translation_quaternion(T)
            f.write(str(timestamp)+' ')
            f.write('{:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f}\n'.format(
                                translation[0], translation[1], translation[2],
                                quaternion[0], quaternion[1], quaternion[2], quaternion[3]))
            
    
        
