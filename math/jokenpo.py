from random import randint


def maquina():
    maq_jogada = randint(0, 2)
    return maq_jogada


def vencedor(j1, j2):
    if j1 == 0:
        if j2 == 1:
            return 'VOCÊ PERDEU'
        elif j2 == 2:
            return 'VOCÊ GANHOU'
        else:
            return 'EMPATE'
    elif j1 == 1:
        if j2 == 0:
            return 'VOCÊ GANHOU'
        elif j2 == 2:
            return 'VOCÊ PERDEU'
        else:
            return 'EMPATE'
    elif j1 == 2:
        if j2 == 0:
            return 'VOCÊ PERDEU'
        elif j2 == 1:
            return 'VOCÊ GANHOU'
        else:
            return 'EMPATE'
    else:
        return 'NÚMERO(S) INVÁLIDO(S)'


try:
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    while True:
        jogada = int(input('0 - Pedra | 1 - Papel | 2 - Tesoura | 9 - Sair\n'))
        if jogada in range(0, 3):
            print(vencedor(jogada, maquina()))
        elif jogada not in range(0, 3):
            print('Opção inválida! Tente de novo.')
        else:
            break
except KeyboardInterrupt:
    print('Programa interrompido!')
except TypeError:
    print('Digite um valor inteiro.')
except ValueError:
    print('Tente um número ao invés de espaços em branco.')
except IndexError:
    print('Valor acima do esperado.')