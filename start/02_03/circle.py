"""
A class for representing a circle
"""
# display_circumference()
# formula: C = 2πr pi= 3.14
# display_area()
# formula: A = πr^2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def display_circumference(self):
        circumference = 2 * 3.14 * self.radius
        print(f"Circumference of Circle: {circumference} units")

    def display_area(self):
        area = 3.14 * (self.radius ** 2)
        print(f"Area of Circle: {area} square units") 

# Creating an instance of Circle and displaying its circumference and area
new_circle = Circle(2)
# Using the methods to display circumference and area
new_circle.display_circumference()  # Output: Circumference of Circle: 12.56 units
new_circle.display_area()           # Output: Area of Circle: 12.56 square units