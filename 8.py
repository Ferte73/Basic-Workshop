condicao = str("sim")

#Trying to don't spent much time on this!!

while condicao == "sim":
    
    try:

        nome = str(input("Qual o nome do vendedor? "))
        salario = float(input("Qual o seu salario fixo? "))
        venda = float(input("Qual o valor total das vendas que você efetuou? "))

        print("seu nome é "+nome)
        print("seu salário fixo é "+str(salario)+" reais por mês")
        print("você recebe "+str(salario+(venda*0.15))+" reais por mês")
        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()


    except ValueError:

        print("Por favor, apenas expresse numericamente o valor de seu salário e da venda!") 
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")   
    