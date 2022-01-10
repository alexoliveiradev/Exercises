"""Where a and b are the legs of a triangle, where the hypotenuse is obtained by the equation hypotenuse = square
root a² + ². Make a functionthat receives the values of a and b and calculate the value of the hypotenuse using the
equation."""


def hypotenuse(a, b):
    h = (a ** 2 + b ** 2) ** (1/2)
    return f"Hypotenuse is {h}"


print(hypotenuse(7, 4))
