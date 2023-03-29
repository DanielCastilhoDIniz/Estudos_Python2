""" 
Escreva uma definição para uma classe denominada Circle, 
com os atributos center e radius, onde center é um objeto Point e radius é um número.
"""

from math import pi


class Circle:

    def __init__(self, radius, center: tuple()):
        self.center = center
        self.radius = int(radius)

    def set_center(self, x, y):
        self.center = (x, y)

    def calculate_area(self):
        return pi * pow(self.radius, 2)

    def calculate_circle_length(self):
        return 2 * pi * self.radius
    


c1 = Circle(3, (0, 0))

print(c1.center, c1.radius)

c1.set_center(1, 0)
print(c1.center, c1.radius)

c1.calculate_area

print(c1.calculate_area())
print(c1.calculate_circle_length())
