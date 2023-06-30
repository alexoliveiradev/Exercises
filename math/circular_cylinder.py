"""
Make a function to return volume of a cylinder
V = pi * radius² * height, pi = 3.141592.
"""


def cylinder(radius, height):
    volume = 3.141592 * radius ** 2 * height
    return f"Volume of the cylinder is {volume:.1f}"


print(cylinder(3.1, 10))
