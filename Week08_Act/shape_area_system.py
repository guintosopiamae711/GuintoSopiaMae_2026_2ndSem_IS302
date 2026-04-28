# shape_area_system.py

import math

# Parent Class
class Shape:
    def area_smg(self):
        pass  # We will override this method in the child classes

# Child Class 1: Rectangle
class Rectangle(Shape):
    def __init__(self, width_smg, height_smg):
        self.width_smg = width_smg
        self.height_smg = height_smg
    
    def area_smg(self):
        return self.width_smg * self.height_smg

# Child Class 2: Circle
class Circle(Shape):
    def __init__(self, radius_smg):
        self.radius_smg = radius_smg
    
    def area_smg(self):
        return math.pi * self.radius_smg ** 2

# Child Class 3: Triangle
class Triangle(Shape):
    def __init__(self, base_smg, height_smg):
        self.base_smg = base_smg
        self.height_smg = height_smg
    
    def area_smg(self):
        return 0.5 * self.base_smg * self.height_smg

# Instantiate objects of different shapes
shapes_smg = [
    Rectangle(10, 5),   # Rectangle with width 10 and height 5
    Circle(5),          # Circle with radius 5
    Triangle(8, 6)      # Triangle with base 8 and height 6
]

# Calculate and print the area for each shape
for shape_smg in shapes_smg:
    print(f"{shape_smg.__class__.__name__} Area: {shape_smg.area_smg()}")