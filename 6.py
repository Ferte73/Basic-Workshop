condicao = str("sim")

while condicao == "sim":

    try:

        distancia = float(input("Qual a distância total da viagem? "))
        consumo = float(input("Quanto você gastou de combustível? "))
        print("O consumo médio foi de "+str(consumo/distancia)+" L/km.")
        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()


    except ValueError:

        print("Por favor, apenas utilize números expressos de forma numérica!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")