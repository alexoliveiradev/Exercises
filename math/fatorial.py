"""
- O número deve ser inteiro e não negativo
- n! é a sua multiplicação pelo seus antecessores. Ex: n.(n-1).(n-2)

Conhecemos como fatorial de um número natural a multiplicação desse número por seus antecessores com exceção do zero
Ou seja, fatorial de 2 é 2x1
"""


def fatorial(numero):
    fator = 1
    for i in range(numero, 1, -1):
        fator *= i
    return fator


print(fatorial(0))
