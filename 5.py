condicao = str("sim")

while condicao == "sim":
    try:
        custo = float(input("Qual o valor de custo do produto? "))
        porcentagem = float(input("Qual a porcentagem de lucro que você deseja? "))
        print("O preço de venda deve ser "+str(custo + custo*(porcentagem/100))+" reais." )
        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()

    except ValueError:
        print("Por favor, apenas utilize números expressos numericamente!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")