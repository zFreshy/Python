numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Soma de todos os números: {soma}")
