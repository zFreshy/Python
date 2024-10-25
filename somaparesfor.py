#Matheus Vinícius
limite_inferior = int(input("Digite o limite maior: "))
limite_superior = int(input("Digite o limite menor: "))

while limite_inferior <= limite_superior:
    print("O primeiro número deve ser maior que o segundo. Tente novamente.")
    limite_inferior = int(input("Digite o limite maior: "))
    limite_superior = int(input("Digite o limite menor: "))

soma = 0
for i in range(limite_superior, limite_inferior + 1):
    if i % 2 == 0:
        soma += i

print(f"A soma dos números pares entre {limite_superior} e {limite_inferior} é: {soma}")
