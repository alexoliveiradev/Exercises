"""
Make a program to print:
1
2   2
3   3   3
.....
n   n   n   n   n   n  ... n
is a user-entered n. Use a function that takes an integer n value and prints up to the nth line.
"""


def nth(n):
    """
    We have the parameter 'n' which will be the total number of times the number is displayed on the screen.
    :param n: 'n' is the number and how many times it will be shown
    :return: return 'N', 'n' times
    """
    for i in range(n):
        repeat = 0
        number = i + 1
        while True:
            if repeat == number:
                print("")
                break
            else:
                print(number, end=" ")
            repeat += 1


nth(10)
