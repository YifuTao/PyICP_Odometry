import os
import numpy as np

class PointCloudDataLoader:
    """Load point cloud data from a folder
    :param point_cloud_folder_path: path to the folder containing point cloud data
    :return: a list of N x 3 point clouds
    """
    def __init__(self, point_cloud_folder_path):
        self.point_cloud_folder_path = point_cloud_folder_path
        self.point_clouds, self.point_clouds_name = self.load_point_cloud()
        print('point clouds are sorted by file name')

    def load_point_cloud(self):
        files = os.listdir(self.point_cloud_folder_path)
        # natural sort
        files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

        print('Files in {}: {}'.format(self.point_cloud_folder_path, files))
        print('check if the files are sorted correctly')
        point_clouds = []
        file_names = []
        for file in files:
            assert file.endswith('.npy')
            point_cloud_path = os.path.join(self.point_cloud_folder_path, file)
            try:
                points = np.load(point_cloud_path)
                assert points.shape[1] == 3 and points.shape[0] > 0 and len(points.shape) == 2
                point_clouds.append(points)
                # remove the extension
                file_names.append(file[:-4])
            except Exception as e:
                print('Error: {}'.format(e))
                continue
        print('Loaded {} point clouds'.format(len(point_clouds)))
        return point_clouds, file_names