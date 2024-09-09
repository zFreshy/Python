while (True):
    numero = int(input("Digite um número: "))
    contador = 0

    for i in range(numero, 0, -1):
        if (i % 2 == 0):
            contador += i

    print(contador)