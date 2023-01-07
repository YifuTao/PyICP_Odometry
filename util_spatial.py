import numpy as np
import scipy


def convert_matrix_to_translation_quaternion(transformation_matrix):
    '''
    :param matrix: 4x4 transformation matrix
    :return: qx qy qz qw and tx ty tz
    '''
    assert transformation_matrix.shape == (4,4)
    rotation_matrix = transformation_matrix[:3,:3]
    translation = transformation_matrix[:3,3]
    quaternion = scipy.spatial.transform.Rotation.from_matrix(rotation_matrix).as_quat()
    return translation, quaternion

def convert_translation_quaternion_to_matrix(translation, quaternion):
    '''
    :param translation: tx ty tz
    :param quaternion: qx qy qz qw
    :return: 4x4 transformation matrix
    '''
    if isinstance(translation,list): translation = np.array(translation)
    if isinstance(quaternion, list): quaternion = np.array(quaternion)
    # check if quaternion is list class


    assert translation.shape == (3,)
    assert quaternion.shape == (4,)
    rotation_matrix = scipy.spatial.transform.Rotation.from_quat(quaternion).as_matrix()
    transformation_matrix = np.eye(4)
    transformation_matrix[:3,:3] = rotation_matrix
    transformation_matrix[:3,3] = translation
    return transformation_matrix
