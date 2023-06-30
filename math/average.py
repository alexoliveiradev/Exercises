"""
Design a function that receives three grades from a student as parameters and a letter.
If the letter is A, the function must calculate the arithmetic mean of the studant; If it is P, it must
calculate the weighted average, with weights 5, 3, and 2.
"""


def average(a, b, c, letter):
    if letter == 'a':
        a_average = (a + b + c) / 3
        return a_average
    elif letter == 'p':
        w_average = ((a * 5) + (b * 3) + (c * 2)) / (5 + 3 + 2)
        return w_average


print(average(8, 9, 7, 'a'))
