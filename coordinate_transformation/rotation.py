
import numpy as np
import math

def rotate(point, rotation_degree: float):
    '''
    Rotate a point by a given angle in degrees anticlockwise.
    :param point: a np 2D point (x, y)
    :param rotation_degree: angle in degrees
    :return: rotated point (x, y)
    '''
    # check if point is a 2D np point
    if not isinstance(point, np.ndarray) or point.ndim != 1 or point.shape[0] != 2:
        raise ValueError('point must be a 2D numpy point')
    # rotation_matrix = np.array([[np.cos(np.deg2rad(rotation_degree)), -np.sin(np.deg2rad(rotation_degree))],
    #                             [np.sin(np.deg2rad(rotation_degree)), np.cos(np.deg2rad(rotation_degree))]])        
    # return np.dot(rotation_matrix, point)

    if point[0]==0:
        
        ang=float(rotation_degree)+90
    else:
        ang = float(rotation_degree+np.arctan(point[1]/point[0])/math.pi*180)
    dis = np.sqrt(point[0]**2+point[1]**2)
    points_rotated = np.array([0.0, 0.0])
    points_rotated[0] = float(dis*np.cos(ang/180*math.pi))
    points_rotated[1] = dis*np.sin(ang/180*math.pi)
    return points_rotated






