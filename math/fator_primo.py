# Este programa vai retornar o maior fator primo do número desejado.

def primo(x):
    """O parâmetro será usado para gerar uma lista de números primos. EX: 220 (parâmetro) vai gerar uma lista com todos
    os números primos entre 220 até 2"""
    total = x
    nprimos = list()
    while total > 0:
        divisores = 0
        for i in range(total):
            resultado = total % (i + 1)
            if resultado == 0:
                divisores += 1
        if divisores == 2:
            nprimos.append(total)
        total -= 1
    nprimos.sort()
    return nprimos  # retorne apenas a variável caso use aspas ou fstring retornará uma string


def fator(numero):
    """Chamando a função primo e passando como argumento o número desejado teremos os números primos entre o nosso
    número até 2 q é o primeiro número primo. Assim será feita a divisão sucessiva até achar O MAIOR FATOR PRIMO."""

    lista = primo(numero)  # Aqui a minha lista é uma string, pq e como resolver? ver comentário na def primo
    quociente = numero
    posicao_numero = 0
    fatorPrimo = list()

    # O loop só para quando o quociente for 1
    while quociente != 1:
        while True:  # Para que nn haja uma divisão real é necessário q seja divido apenas quando o resto for 0
            if quociente % lista[posicao_numero] != 0:
                posicao_numero += 1
            else:
                break
        valor = quociente / lista[posicao_numero]
        quociente = valor
        fatorPrimo.append(lista[posicao_numero])  # Adiciona a lista e depois com a função max() mostrará o maior fator
        if quociente % lista[posicao_numero] != 0:
            posicao_numero += 1
    return f"O maior fator primo de {numero} é {max(fatorPrimo)}"


num = int(input("Informe um número: "))
if num > 0:
    print(fator(num))
else:
    print("Informe números positivos!")
