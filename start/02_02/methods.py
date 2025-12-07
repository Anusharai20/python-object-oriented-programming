"""
Python class methods
"""


class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def display_Area(self):
        area = self.base * self.height
        print(f"Area of Rectangle: {area} square units")


new_rectangle = Rectangle(12, 10)
new_rectangle.display_Area()  # Output: Area of Rectangle: 120 square units
