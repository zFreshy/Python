print("Qual a quantidade de notas a serem colocadas?")
quantidade_notas = int(input())

notas = []

for i in range(quantidade_notas):
    print(f"Qual o valor da nota {i+1}?")
    nota = float(input())
    notas.append(nota)

media = sum(notas) / quantidade_notas

print(f"A média é: {media}")

if (media < 8):
    print("Você precisa estudar mais vagabundo!") 
else: 
    print("Boa")