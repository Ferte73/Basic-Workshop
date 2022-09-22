condicao = str("sim")

while condicao == "sim":

    try:

        salario = float(input("Qual seu salário bruto?"))
        print("Salário bruto = "+str(salario))
        print("Imposto de Renda = "+str(salario*0.11))
        print("INSS = "+str(salario*0.08))
        print("Sindicato = "+str(salario*0.05))
        print("Salário Líquido = "+str(salario*0.76))
        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()


    except ValueError:
        print("Por favor, apenas valores expressos numericamente serão aceitos!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")