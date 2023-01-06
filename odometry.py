import os
import numpy as np
import open3d as o3d

from viz_plotly import Plotly
from PointCloudDataLoader import PointCloudDataLoader
from icp import point2point_icp
import simpleicp as point_to_plane_icp
from util_pc import  range_filtering, random_sampling, np_to_o3d_pc

class Odometry:
    def __init__(self, point_cloud_folder_path):
        self.pc_loader = PointCloudDataLoader(point_cloud_folder_path)

class ICP:
    def __init__(self, old_scan, new_scan):
        assert old_scan.shape[1] == 3 and len(old_scan.shape) == 2
        assert new_scan.shape[1] == 3 and len(new_scan.shape) == 2
        self.old_scan = old_scan
        self.new_scan = new_scan
    
    def range_filtering(self, min_range=4, max_range=50):
        '''
        :param min_range: minimum range in meters
        :param max_range: maximum range in meters
        :return: filtered point cloud
        '''
        self.old_scan = range_filtering(self.old_scan, min_range, max_range)
        self.new_scan = range_filtering(self.new_scan, min_range, max_range)

    def run_icp(self, method='point_to_plane'):
        '''
        :param method: point-to-point or point-to-plane
        :return: 4x4 transformation matrix T_old__new i.e. transform new scan to old scan's frame
        '''
        if method == 'point_to_point':
            T_old_new = self.icp_point_to_point()
        elif method == 'point_to_plane':
            T_old_new = self.icp_point_to_plane()
        else:
            raise ValueError('Invalid ICP method. Choose from point_to_point or point_to_plane')
        transformed_new_scan = self.transform_new_scan(T_old_new)
        self.evaluate(T_old_new)
        self.visualise(transformed_new_scan)

    def icp_point_to_plane(self):
        '''
        point-to-plane ICP based on simpleICP
        https://github.com/pglira/simpleICP/tree/master/python
        :return: 4x4 transformation matrix T_old__new i.e. transform new scan to old scan's frame
        '''
        max_overlap_distance = 1 # only corresponds <= max_overlap_distance m are considered as overlapping points
        pc_fix = point_to_plane_icp.PointCloud(self.old_scan, columns=['x', 'y', 'z'])
        pc_mov = point_to_plane_icp.PointCloud(self.new_scan, columns=['x', 'y', 'z'])
        icp_ = point_to_plane_icp.SimpleICP()
        icp_.add_point_clouds(pc_fix, pc_mov)
        H, X_mov_transformed, rigid_body_transformation_params = icp_.run(max_overlap_distance=1) 
        return H
    def icp_point_to_point(self):
        '''
        point-to-plane ICP by Clay Flannigan
        :return: 4x4 transformation matrix T_old__new i.e. transform new scan to old scan's frame
        '''
        N_sampled_points = min(self.old_scan.shape[0], self.new_scan.shape[0])
        old_scan_downsampled = random_sampling(self.old_scan, N_sampled_points)
        new_scan_downsampled = random_sampling(self.new_scan, N_sampled_points)
        T, distances, iterations = point2point_icp.icp(
                    new_scan_downsampled, old_scan_downsampled, tolerance=0.0001)
        return T
        
    def transform_new_scan(self, T):
        '''
        :param T: 4x4 transformation matrix T_old__new i.e. transform new scan to old scan's frame
        :return: transformed new scan
        '''
        def transform_pc(T, pc):
            homogeneous_pc = np.ones((pc.shape[0], 4))
            homogeneous_pc[:, :3] = np.copy(pc)
            transformed_pc = np.dot(T, homogeneous_pc.T).T
            transformed_pc = transformed_pc[:, :3]
            return transformed_pc

        transformed_pc = transform_pc(T, self.new_scan)
        return transformed_pc
    def evaluate(self, T, max_correspondence_distance=0.1):
        '''
        :param transformed_new_scan: transformed new scan
        :return: mean distance between transformed new scan and old scan
        '''
        o3d_pc_old = np_to_o3d_pc(self.old_scan)
        o3d_pc_new = np_to_o3d_pc(self.new_scan)
        evaluation = o3d.pipelines.registration.evaluate_registration(
            o3d_pc_old, o3d_pc_new, max_correspondence_distance, T)
        print(evaluation)
    
    def visualise(self, transformed_new_scan):
        '''
        :param transformed_new_scan: transformed new scan
        :return: None
        '''
        plotly = Plotly()
        plotly.add_axies()
        plotly.add_point_cloud(self.old_scan,name='old',colour='red')
        plotly.add_point_cloud(self.new_scan,name='new',colour='green')
        plotly.add_point_cloud(transformed_new_scan,name='transformed_new_icp',colour='blue')

        plotly.visualise()
        print('The visualisation is saved to {}'.format(plotly.save_path))
def main():
    pass

if __name__ == '__main__':
    main()