"""
Python class properties
"""


class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self._height = height


new_rectangle = Rectangle(12, 10)
print(new_rectangle.base)      # Output: 12
print(new_rectangle._height)   # Output: 10
# Modifying the base attribute
new_rectangle.base = 15
print()
print(new_rectangle.base)      # Output: 15
