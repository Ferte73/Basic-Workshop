condicao = str("sim")

while condicao == "sim":

    try:

        ano = int(input("Digite o ano: "))
        if float(ano/4) == int(ano/4):
            print("O ano será bissexto!")
        else:
            print("O ano não será bissexto!")

        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()


    except ValueError:
        print("Apenas números inteiros serão aceitos!!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")