def soma(x, y):
    total = 0
    seguinte = x + 1
    for i in range(x, y):
        if seguinte < y:
            total += seguinte
            seguinte += 1
    return f"O valor da soma dos número é {total}"


while True:
    try:
        while True:
            a = int(input("1º número: "))
            b = int(input("2º número: "))
            if a > 0 and b > 0:
                print(soma(a, b))
                break
            else:
                print("Informe números positivos!")
                continue
        break
    except:
        print("Os números devem ser inteiros!")
