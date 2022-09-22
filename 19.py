condicao = str("sim")

while condicao == "sim":

    try:

        s1 = float(input("Qual seu salário por hora?"))
        h = float(input("Quantas horas você trabalha por mês?"))
        s2 = s1 * h 

        if s2 <= 900:
            print("Salário Bruto : ("+str(s1)+" * "+str(h)+") : R$ = 1100,00")
            print("(-) IR (0%) : R$ 0,00")
            print("(-) INSS (10%) : R$ "+str(s2*0.1))
            print("(-) FGTS (11%): R$ "+str(s2*0.11))
            print("Salário Líquido : R$ "+str(s2*0.79))

        if s2 > 900 and s2 <= 1500:
            print("Salário Bruto : ("+str(s1)+" * "+str(h)+") : R$ = 1100,00")
            print("(-) IR (5%) : R$ "+str(s2*0.05))
            print("(-) INSS (10%) : R$ "+str(s2*0.1))
            print("(-) FGTS (11%): R$ "+str(s2*0.11))
            print("Salário Líquido : R$ "+str(s2*0.74))

        if s2 > 1500 and s2 <= 2500:
            print("Salário Bruto : ("+str(s1)+" * "+str(h)+") : R$ = 1100,00")
            print("(-) IR (10%) : R$ "+str(s2*0.1))
            print("(-) INSS (10%) : "+str(s2*0.1))
            print("(-) FGTS (11%): R$ "+str(s2*0.11))
            print("Salário Líquido : R$ "+str(s2*0.69))

        if s2 > 2500:
            print("Salário Bruto : ("+str(s1)+" * "+str(h)+") : R$ = 1100,00")
            print("(-) IR (20%) : R$ "+str(s2*0.2))
            print("(-) INSS (10%) : "+str(s2*0.1))
            print("(-) FGTS (11%): R$ "+str(s2*0.11))
            print("Salário Líquido : R$ "+str(s2*0.59))  

        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()
        

    except ValueError:
        print("Por favor, apenas expresse o Salário Bruto de forma numérica!") 
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")