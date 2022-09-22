condicao = str("sim")

while condicao == "sim":
    try:
        medida = float(input("Qual é a medida em centímetros que busca converter para metros? "))
        medida = medida / 100
        print("O valor em metros da medida que você converteu será "+str(medida)+" metros!")
 
        condicao = input("Você quer continuar a executar o programa?\nApenas'sim' será lido como resposta positiva! ").lower()
    except ValueError:
        print("Por favor, apenas aceitamos valores numéricos maiores do que 0!(Sem ser por extenso)")
        condicao = input("Você quer tentar de novo?\nApenas 'sim' será lido como resposta positiva! ").lower()

print("")
print("Obrigado por exectura meu programa!")
