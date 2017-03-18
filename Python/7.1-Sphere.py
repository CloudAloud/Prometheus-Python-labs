__author__ = 'minin'

import math

'''
import unittest

class MyTests(unittest.TestCase):

    def setUp(self):
        pass
'''


class Sphere:

    def __init__(self, r=1.0, x=0.0, y=0.0, z=0.0):
        self.r, self.x, self.y, self.z = r, x, y, z

    def get_volume(self):
        volume = (4 * math.pi * (self.r ** 3)) / 3.0
        return volume

    def get_square(self):
        square = 4 * math.pi * (self.r ** 2)
        return square

    def get_radius(self):
        return self.r

    def get_center(self):
        center = (self.x, self.y, self.z)
        return center

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def is_point_inside(self, x, y, z):
        d = math.sqrt(((x - self.x) ** 2) + ((y - self.y) ** 2) + ((z - self.z) ** 2))
        if d > self.r:
            return False
        else:
            return True


one = Sphere(5.0, 4.0, 3.0, 2.0)
#two = Sphere(4.0)
#one.x = 2.0
print one.get_center()
print one.get_radius()
print one.get_square()
print one.get_volume()
print one.is_point_inside(8.0, 2.0, 3.0)
#print one.r, one.x, one.y, one.z
