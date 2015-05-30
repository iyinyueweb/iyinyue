__author__ = 'Administrator'
import math


class Vector(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    @classmethod
    def from_points(cls, p1, p2):
        return cls(p2[0] - p1[0], p2[1] - p1[1])

    def get_magnitude(self):  # 计算模
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):  # 单位向量
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude

    def __add__(self, other):  # 向量相加
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # 向量相减
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __div__(self, other):
        return Vector(self.x / other.x, self.y / other.y)
a = (10, 20)
b = (30, 35)
ab = Vector.from_points(a, b)
print(ab)