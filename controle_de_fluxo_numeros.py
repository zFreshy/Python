contagem = 0

for contagem in range (100):
    if contagem == 6:
        print("Não vou mostrar o número 6")
    elif contagem >= 10 and contagem <= 27:
        print("Não vou mostar o número " + str(contagem))
    elif contagem > 40:
        break
    else:
        print(contagem)
        contagem += 1