condicao = str("sim")

while condicao == "sim":

    try:

        print("Dentre a tabela a seguir, qual é o seu tipo de veículo?")

        print("Automóvel - Alíquota de 4%")
        print("Caminhonete - Alíquota de 3%")
        print("Motocicleta - Alíquota de 2%")
        print("Transportes publicos - Alíquotas de 2%")
        print("Locação - Alíquota de 1%")
        print("Veículo Grande - Alíquota de 1%")

        tipo = input("Lendo a partir de 'automóvel', 'caminhonete', 'motocicleta', 'publico' , 'locação' e 'veículo grande', digite o seu tipo de veículo: ").lower()
        print("")
        preco = float(input("Digite numericamente (não de forma extensa) o valor venal do veículo: "))

        if tipo == "automóvel":
            print("Sua alíquota é de 4%, e o preço do imposto pago será R$"+str(preco*0.04))
        elif tipo == "caminhonete":
            print("Sua alíquota é de 3%, e o preço do imposto pago será R$"+str(preco*0.03))
        elif tipo == "motocicleta" or tipo == "veículo público":
            print("Sua alíquota é de 2%, e o preço do imposto pago será R$"+str(preco*0.02))
        elif tipo == "locação" or tipo == "veículo grande":
            print("Sua alíquota é de 1%, e o preço do imposto pago será R$"+str(preco*0.03))
        else:
            print("Por favor, apenas será lido os veículos como: Automóvel;")
            print("                                              Caminhonete;")
            print("                                              Motocicleta;")
            print("                                              Veículo Público;")
            print("                                              Locação;")
            print("                                              Veículo Grande;")
        
        condicao = input("Quer continuar a utilizar o programa?\nApenas 'sim' será lido como resposta positiva! ").lower()

    except ValueError:
        print("Por favor, na parte de valores, apenas se expresse numericamente!")
        condicao = input("Quer tentar de novo?\nApenas 'sim' será lido como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")
    