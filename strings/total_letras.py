"""
Calcule quantas letras possui uma string
"""


def total_de_letras(string):
    try:
        quant = 0
        for i in string:
            quant += 1
        return f"A string '{string}' possui {quant} letras."
    except TypeError:
        return 'Erro! Informe uma palavra.'


print(total_de_letras('Sousa'))
print(total_de_letras(12))
print(total_de_letras(True))