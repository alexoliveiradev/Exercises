"""Make a function that receives the current date (month, day and year in full)
and displays it on the screen in full text format.
Exemple: November 1st, 2021."""

months = "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", \
         "december "


def date(d, m, y):
    if d == 1:
        return f"{months[m-1]} {d}st, {y}."
    elif d == 2:
        return f"{months[m]} {d}nd, {y}."
    else:
        return f"{months[m]} {d}rd, {y}."


print(date(1, 12, 2021))
