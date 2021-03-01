#x = int(input('Point 1 en x : '))
#y = int(input('Point 1 en y : '))
#dx = int(input('Distance point 1 en x : '))
#dy = int(input('Distance point 1 en y : '))
#x2 = int(input('Point 2 en x : '))
#y2 = int(input('Point 2 en y : '))

from math import sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Point: {self.x}:{self.y}")
    def move(self, dx, dy):
        self.x = dx
        self.y = dy
    def dist(self, other_point):
        calcul = sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)
        return calcul

#p1 = Point(x,y)
#p1.show()
#p1.move(dx,dy)
#p1.show()
#p2 = Point(x2, y2)
#print(p1.dist(p2))

p1 = Point(4,5)
p1.show()
p1.move(9,8)
p1.show()
p2 = Point(12, 5)
print(p1.dist(p2))
