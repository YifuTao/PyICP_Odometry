import os
import numpy as np

class PointCloudDataLoader:
    """Load point cloud data from a folder
    :param point_cloud_folder_path: path to the folder containing point cloud data
    :return: a list of N x 3 point clouds
    """
    def __init__(self, point_cloud_folder_path):
        self.point_cloud_folder_path = point_cloud_folder_path
        self.point_clouds = self.load_point_cloud()

    def load_point_cloud(self):
        files = sorted(os.listdir(self.point_cloud_folder_path))
        print('Files in {}: {}'.format(self.point_cloud_folder_path, files))
        point_clouds = []
        for file in files:
            point_cloud_path = os.path.join(self.point_cloud_folder_path, file)
            try:
                points = np.fromfile(point_cloud_path,dtype=np.float32)
                points = points.reshape(-1, 4)
                points = points[...,:3]
                point_clouds.append(points)
            except Exception as e:
                print('Error: {}'.format(e))
                continue
        print('Loaded {} point clouds'.format(len(point_clouds)))
        return point_clouds