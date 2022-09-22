condicao = str("sim")

while condicao == "sim":

    try:
        racao = float(input("Quantos kg você comprou de ração?"))
        consumo = float(input("Quanto de ração em gramas, cada grupo de aves consome?"))
        taxa = racao*1000 - consumo*14

        if taxa < 0:
            print("Falta "+str(taxa)+" gramas.")
        elif taxa == 0:
            print("A taxa é igual o consumo das aves por uma semana!")
        else: 
            print("Sobraram "+str(taxa)+" gramas.")
        
        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()


    except ValueError:
        print("Por favor, apenas serão aceitos numeros expressos numericamente, não por extenso ou quaisquer outra forma de representação!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("Obrigado por usar meu programa!")