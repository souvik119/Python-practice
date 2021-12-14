import math

class Line:

    def __init__(self, coor1, coor2):
        self.x1, self.y1 = coor1 #tuple unpacking
        self.x2, self.y2 = coor2

    def distance(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

    def slope(self):
        return abs(self.y2 - self.y1) / abs(self.x2 - self.x1)

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2) #remember this is a tuple
print(li.distance())
print(li.slope())


class Cylinder():
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.14 * (self.radius) ** 2 * self.height

    def surface_area(self):
        return (2 * 3.14 * self.radius * self.height) + (2 * 3.14 * (self.radius) ** 2)


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())