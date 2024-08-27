def verifica_ano_bissexto():
    while True:
        ano = int(input("Digite um ano: "))
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            print("O ano é bissexto!")
        else:
            print("O ano não é bissexto.")
        resposta = input("Deseja verificar outro ano? (s/n): ")
        if resposta.lower() != 's':
            break

verifica_ano_bissexto()