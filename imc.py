def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def main():
    while True:
        peso = float(input("Digite o seu peso em kg: "))
        if peso < 2.1:
            print("Peso muito baixo! Por favor, digite um peso válido.")
            continue

        altura = float(input("Digite a sua altura em metros: "))
        if altura < 0.546 or altura > 2.51:
            print("Altura inválida! Por favor, digite uma altura entre 0,546 e 2,51 metros.")
            continue

        imc = calcula_imc(peso, altura)
        print(f"Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Você está abaixo do peso!")
        elif imc < 25:
            print("Você está no peso ideal!")
        elif imc < 30:
            print("Você está com sobrepeso!")
        else:
            print("Você está obeso!")

        resposta = input("Deseja calcular novamente? (s/n): ")
        if resposta.lower() != "s":
            break

main()