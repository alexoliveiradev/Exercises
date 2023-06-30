"""
Crie um programa que compare duas string
"""


def compara(str1, str2):
    try:
        if str1 == str2:
            return f'{str1} e {str2} são iguais'
        else:
            return f'{str1} e {str2} são diferentes'
    except ValueError:
        return f'Digite caracter, inteiro ou real'

# print(compara('joão', 'Joao'))
# print(compara('joão', 'João'))
# print(compara('MAÇA', 'MAÇA'))
# print(compara('MAÇA', 'MACA'))
# print(compara('12', '12'))
# print(compara(39, '39'))
# print(compara('quatro', '4'))
