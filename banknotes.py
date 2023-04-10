"""
In this problem you have to read an integer value and calculate the smallest possible number of banknotes in which the
value may be decomposed. The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the list of
banknotes.
"""


def number(x):
    if 0 < x < 1000000:
        return x
    else:
        return 0


def decompose(n):
    num = number(n)
    dicio = dict()
    division, cont = num, 0
    while len(banknotes) != cont:
        if division // banknotes[cont] >= 1:
            value = division // banknotes[cont]
            dicio.update({banknotes[cont]: value})
            division = division % banknotes[cont]
            cont += 1
        elif division // banknotes[cont] == 0:
            dicio.update({banknotes[cont]: 0})
            cont += 1
        else:
            break
    return form(dicio, n)


def form(array, n):
    print(n)
    for bkn, values in array.items():
        print(f'{values} nota(s) de R$ {bkn},00')


banknotes = [100, 50, 20, 10, 5, 2, 1]

money = int(input(''))
decompose(money)
