import unittest
import numpy as np
import matplotlib.pyplot as plt

from rotation import rotate

class TestRotation(unittest.TestCase):

    def test_rotation_1(self):
        rotation_degree = 90
        point_before = np.array([1, 0])
        point_after = np.array([0, 1])
        self.assertTrue(np.allclose(point_after, rotate(point_before, rotation_degree)))

    def test_rotation_2(self):
        rotation_degree = 60
        point_before = np.array([1, 0])
        point_after = np.array([0.5, np.sqrt(3)/2])
        self.assertTrue(np.allclose(point_after, rotate(point_before, rotation_degree)))

    def test_rotation_3(self):
        rotation_degree = 360
        point_before = np.array([1, 0])
        point_after = np.array([1, 0])
        self.assertTrue(np.allclose(point_after, rotate(point_before, rotation_degree)))
        
    def test_rotation_4(self):
        rotation_degree = 180
        point_before = np.array([0,-1])
        point_after = np.array([0, 1])
        self.assertTrue(np.allclose(point_after, rotate(point_before, rotation_degree)))

    def test_rotation_5(self):
        # generate a rectangle of 10 points of length 5, width 2
        points = np.array([[0, 0], [5, 0], [5, 2], [0, 2], [0, 0]])
        rotation_angle = 90
        # rotate the rectangle by 45 degrees
        points_rotated = np.array([rotate(point, rotation_angle) for point in points])
        
        # plot the rectangle and the rotated rectangle
        plt.plot(points[:, 0], points[:, 1], 'r')
        plt.plot(points_rotated[:, 0], points_rotated[:, 1], 'b')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(['original', 'rotated'])
        plt.axis('equal')
        plt.title('Rotation of a rectangle by {} degrees'.format(rotation_angle))

        plt.show()

if __name__ == '__main__':
    # run the tests verbosely

    unittest.main(verbosity=3)
    