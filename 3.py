from multiprocessing.sharedctypes import Value


condicao = str("sim")

while condicao == "sim":

    try:

        temperatura = float(input("Qual a temperatura da sua casa em graus Farenheit para converter em celsius? "))
    
        print("A temperatura de sua casa é "+str((5 * (temperatura - 32)) / 9 )+" graus celsius")

        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()

    
    except ValueError:
        print("Apenas serão aceitos valores escritos numericamente!")

        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")