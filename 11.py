condicao = str("sim")

while condicao == "sim":

    try:

        tamanho = float(input("Para o calculo da velocidade de tempo de Download, qual é o tamanho do arquivo expresso em MB/s??"))
        velocidade = float(input("E qual é a velocidade de internet em MB/s?"))

        print("Você vai demorar "+str(tamanho/velocidade)+" segundos.")
        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()


    except ValueError:
        print("por favor, apenas valores expressos numericamente serão aceitos!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")