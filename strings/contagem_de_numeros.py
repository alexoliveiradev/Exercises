"""
Faça um programa que conte o número de 1’s que aparecem em um string. Exemplo:
0011001 -> 3
"""


def contagem(numero):
    try:
        quant = 0
        for i in numero:
            if i == '1':
                quant += 1
        return quant
    except TypeError:
        return 'Digite um número em formato de caracteres. Ex: "00110001"'


print(contagem('0011001'))
print(contagem('182030921'))
print(contagem('3652874'))

print(contagem(123456))
print(contagem(True))
