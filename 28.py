condicao = str("sim")

while condicao == "sim":

    try:

        elevador = float(input("Qual o peso máximo em toneladas que o elevador suporta? "))
        peso = float(input("Qual o peso em quilogramas que o elevador está carregando de pessoas no momento?"))
        elevador = elevador * 1000

        if elevador > peso:
            print("O elevador permite carregar esse peso!")
        else:
            print("O elevador não permite carregar esse peso!")

        condicao = input("Quer continuar a utilizar o programa?\nApenas 'sim' será lido como resposta positiva! ").lower()

    
    except ValueError:
        print("Favor apenas utilizar valores expressos numericamente!")
        condicao = input("Quer tentar de novo??\nApenas 'sim' será lido como resposta positiva! ").lower()
