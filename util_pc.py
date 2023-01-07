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

def transform_pc(T, pc):
    assert T.shape == (4, 4)
    assert pc.shape[1] == 3 and len(pc.shape) == 2
    homogeneous_pc = np.ones((pc.shape[0], 4))
    homogeneous_pc[:, :3] = np.copy(pc)
    transformed_pc = np.dot(T, homogeneous_pc.T).T
    transformed_pc = transformed_pc[:, :3]
    return transformed_pc

def savePlyFromPtsRGB(pts, file_name, RGB=None, alpha=None):
    with open(file_name, 'w') as f:
        f.write('ply\n')
        f.write('format ascii 1.0\n')
        f.write('element vertex %d\n' % pts.shape[0])
        f.write('property float x\n')
        f.write('property float y\n')
        f.write('property float z\n')
        if RGB is not None:
            f.write('property uchar red\n')
            f.write('property uchar green\n')
            f.write('property uchar blue\n')
        if alpha is not None:
            f.write('property uchar alpha\n')
        f.write('end_header\n')
        # write data
        for i in range(pts.shape[0]):
            f.write('%f %f %f' % (pts[i,0], pts[i,1], pts[i,2]))
            if RGB is not None:
                f.write(' %d %d %d' % (RGB[i,0]*255, RGB[i,1]*255, RGB[i,2]*255))
            if alpha is not None:
                f.write(' %d' % (alpha[i]*255))
            f.write('\n')