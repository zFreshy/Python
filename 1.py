a = 5
b = 10

def trocar_valores():
    global a, b
    a, b = b, a

def perguntar_usuario():
    print("Deseja trocar os valores de A e B? (S/N)")

    resposta = str(input())

    if resposta ==  "S":
        trocar_valores()
        print("Valores trocados!")
    elif resposta == "N":
        print("Valores mantidos.")

perguntar_usuario()

print("A =", a)
print("B =", b)