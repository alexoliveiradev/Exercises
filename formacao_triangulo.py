def tipo_triangulo(x):
    a, b, c = x
    if a == b == c:  # Todos os lado IGUAIS.
        return "Triângulo equilátero."
    elif a != b and a != c and b != c:  # Todos os lados DIFERENTES.
        return "Triângulo escaleno."
    else:  # # DOIS lados IGUAIS
        return "Triânculo isósceles."


def lados(*args):
    tri = 0
    for i in range(len(args)):
        if i == len(args) + 1:
            soma = args[0] + args[1]
            if soma > args[2]:
                tri += 1
        elif i == len(args) - 1:
            soma = args[0] + args[2]
            if soma > args[1]:
                tri += 1
        else:
            soma = args[1] + args[2]
            if soma > args[0]:
                tri += 1
    if tri == 3:
        return tipo_triangulo(args)
    else:
        print("Os segmentos não formam um triângulo.")


while True:
    lado1 = int(input("Lado 1: "))
    lado2 = int(input("Lado 2: "))
    lado3 = int(input("Lado 3: "))
    if lado1 > 0 and lado2 > 0 and lado3 > 0:
        print(lados(lado1, lado2, lado3))
        break
    else:
        print("Digite valores maiores que 0! Tente novamente.")
