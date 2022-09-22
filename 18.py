condicao = str("sim")

while condicao == "sim":

    try:

        salario = float(input("Qual é o seu atual salário?"))

        if salario <= 280:
            print("O aumento será de 20%, ou +"+str(salario*0.2)+" reais")
            print("O seu futuro salário será "+str(salario*1.2)+" reais")

        if salario >= 280 and salario < 700:
            print("O aumento será de 15%, ou +"+str(salario*0.15)+" reais")
            print("O seu futuro salário será "+str(salario*1.15)+" reais")

        if salario >= 700 and salario < 1500:
            print("O aumento será de 10%, ou +"+str(salario*0.1)+" reais")
            print("O seu futuro salário será "+str(salario*1.1)+" reais")

        if salario >= 1500:
            print("O aumento será de 5%, ou +"+str(salario*0.05)+" reais")
            print("O seu futuro salário será "+str(salario*1.05)+" reais")

        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()


    except ValueError:
        print("Apenas expresse numericamente o valor do salario!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")