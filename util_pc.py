import random
import numpy as np
import open3d as o3d


def random_sampling(orig_points, num_points):
    assert orig_points.shape[1] == 3
    assert num_points <= orig_points.shape[0]

    points_down_idx = random.sample(range(orig_points.shape[0]), num_points)
    down_points = orig_points[points_down_idx, :]

    return down_points

def range_filtering(orig_points, min_range, max_range):
    assert orig_points.shape[1] == 3

    range = np.sqrt(np.sum(orig_points**2, axis=1))
    mask = np.logical_and(range > min_range, range < max_range)
    filtered_points = orig_points[mask, :]

    return filtered_points

def np_to_o3d_pc(np_array):
    pc = o3d.geometry.PointCloud()
    pc.points = o3d.utility.Vector3dVector(np_array)
    # compute normals
    pc.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(
        radius=0.1, max_nn=30))
        
    return pc