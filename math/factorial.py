def factorial(n):
    cont = 0
    while cont != n:
        fac = 1
        for i in range(1, n+1):
            fac *= i
            cont += 1
        return f"{n}! = {fac}"
    if n == 0:
        return f"{n}! = 0"
    elif n == 1:
        return f"{n}! = 1"


try:
    print(factorial(7))
except TypeError:
    print("Real and negative numbers are invalid.")
