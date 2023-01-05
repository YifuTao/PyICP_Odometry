import os
import numpy as np

from viz_plotly import Plotly

class PointCloudDataLoader:
    def __init__(self, point_cloud_folder_path):
        self.point_cloud_folder_path = point_cloud_folder_path
        self.point_clouds = self.load_point_cloud()

    def load_point_cloud(self):
        files = os.listdir(self.point_cloud_folder_path)
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