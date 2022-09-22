condicao = str("sim")

while condicao == "sim":
    try:
        preco = float(input("Qual o valor do produto que você pensa em comprar? "))
        print("o valor de cada prestração será "+str(preco / 5)+" reais.")
        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()

    except ValueError:
        print("Apenaas valores escritos numericamente, por favor!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")