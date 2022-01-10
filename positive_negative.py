"""
Do a function to check if a number is positive or negative.
"""


def check(number):
    if number > 0:
        return f"The number {number} is positive."
    elif number == 0:
        return f"The number {number} is neutral."
    else:
        return f"The number {number} is negative."


print(check(0))
print(check(1))
print(check(3))
print(check(-1))
print(check(-7))
