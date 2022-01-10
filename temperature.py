"""
Make a function that takes a temperature in degrees Celsius and converts it to Fahrenheit. The conversion formula
is: F = C * (9.0 / 5.0) + 32.0, where F is the temperature in Fahrenheit and C is the temperature in Celsius.
"""


def degrees(temperature):
    f = temperature * (9 / 5) + 32
    return f"The temperature in degrees Fahrenheit is {f:.1f}"


print(degrees(55))
