from math import pi

class Shape:
    def area(self):   # self add karna zaroori hai
        pass

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)   # correct formula
    
# Objects
r1 = Rectangle(5, 4)
c1 = Circle(6)

# Polymorphism in action
for shape in (r1, c1):
    print(shape.area())
