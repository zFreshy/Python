def verifica_voto(idade):
    if idade < 16:
        return "Não vota"
    elif idade >= 16 and idade < 18:
        return "Voto opcional"
    elif idade >= 18 and idade <= 65:
        return "Voto obrigatório"
    else:
        return "Voto opcional"

idade = int(input("Digite sua idade: "))
resultado = verifica_voto(idade)
print(f"Com {idade} anos, {resultado}.")