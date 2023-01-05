
import numpy as np
import math

def rotate_2D(point, rotation_degree: float):
    '''
    SO(2) rotation matrix
    Rotate a point by a given angle in degrees anticlockwise.
    :param point: a np 2D point (x, y)
    :param rotation_degree: angle in degrees
    :return: rotated point (x, y)
    '''
    # check if point is a 2D np point
    if not isinstance(point, np.ndarray) or point.ndim != 1 or point.shape[0] != 2:
        raise ValueError('point must be a 2D numpy point')
    rotation_matrix = np.array([[np.cos(np.deg2rad(rotation_degree)), -np.sin(np.deg2rad(rotation_degree))],
                                [np.sin(np.deg2rad(rotation_degree)), np.cos(np.deg2rad(rotation_degree))]])        
    return np.dot(rotation_matrix, point)







