"""
Converter uma letra maiúscula em minúscula usando a tabela ASCII
"""


def converte(letra):
    """Usando a função ord() obtêm-se o Unicode daquela letra no qual é somada com 32 que é a diferença que há entre a
    letra maiúscula e a minúscula. Usando a função chr() é retornado uma string de um caractere cujo código ASCII é o
    inteiro."""
    try:
        if letra != letra.lower():
            return f'{letra} = {chr(ord(letra) + 32)}'
        else:
            return f"Informe a letra precisar ser maiúscula -> {letra}"
    except TypeError:
        return 'Informe um caracter'


print(converte('A'))
print(converte('a'))
print(converte('B'))
print(converte('C'))
print(converte('E'))
print(converte('e'))

# print(converte(12))
