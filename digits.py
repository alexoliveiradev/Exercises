"""
- Criar uma função que recebe um número inteiro maior do que zero
- Retornar a soma dos seus algarismos
"""


def digits(num):
    soma = 0
    while num:
        soma += num % 10
        num //= 10
    return soma
        

print(digits(1155))
