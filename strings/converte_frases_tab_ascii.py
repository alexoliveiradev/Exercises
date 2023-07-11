"""
Leia um vetor contendo letras de uma frase inclusive os espaços em branco. Retirar os
espaços em branco do vetor e depois escrever o vetor resultante.
"""


def frase(vetor):
    vetor = list(vetor)
    vetor_sem_espacos = [letra for letra in vetor if letra != ' ']
    return f'Vetor original: {vetor}\n' \
           f'Vetor sem espaço: {vetor_sem_espacos}'


print(frase('eu amo programação'))
