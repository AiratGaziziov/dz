import math

class GeometricFigure:
    def arena(self):
        pass

class Rect(GeometricFigure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def arena(self):
        return self.width * self.height

class Circle(GeometricFigure):
    def __init__(self, radius):
        self.radius = radius

    def arena(self):
        return math.pi * self.radius ** 2

class Rhomb(GeometricFigure):
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def arena(self):
        return (self.diagonal1 * self.diagonal2) / 2

rectangle = Rect(10, 15)
circle = Circle(10)
rhombus = Rhomb(10, 15)

print("Площадь прямоугольника:", rectangle.arena())
print("Площадь круга:", circle.arena())
print("Площадь ромба:", rhombus.arena())
