from math import *
from point import Point
class Circle:
    def __init__(self, origin, radius):
        self.origin = origin
        self.radius = radius
    def perimeter(self):
         return pi * self.radius * 2
    def area(self):
        return pi * self.radius**2
    def dist(self, another_circle):
        o1 = self.origin
        o2 = another_circle.origin
        distance_origins = o1.dist(o2)
        dist = distance_origins - (self.radius + another_circle.radius)
        return dist
p1 = Point(5, 4)
c1 = Circle(p1, 5)
print(c1.perimeter())
print(c1.area())
p2 = Point(12, 16)
c2 = Circle(p2, 3)
print(c1.dist(c2))
