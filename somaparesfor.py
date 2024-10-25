# Solicitar os limites ao usuário
limite_inferior = int(input("Digite o limite maior: "))
limite_superior = int(input("Digite o limite menor: "))

# Garantir que o limite inferior é maior que o superior
while limite_inferior <= limite_superior:
    print("O primeiro número deve ser maior que o segundo. Tente novamente.")
    limite_inferior = int(input("Digite o limite maior: "))
    limite_superior = int(input("Digite o limite menor: "))

# Calcular a soma dos números pares
soma = 0
for i in range(limite_superior, limite_inferior + 1):
    if i % 2 == 0:
        soma += i

print(f"A soma dos números pares entre {limite_superior} e {limite_inferior} é: {soma}")
