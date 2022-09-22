condicao = str("sim")

while condicao == "sim":

    try:


        print("                 Até 5kg | Acima de 5kg")
        print("maçãs por kg:    R$1,80  |      R$1,50")
        print("morangos por kg: R$2,50  |      R$2,20")

        morango = float(input("Quantos kg de Morango?"))
        maca = float(input("Quantos kg de Maçã?"))

        if morango > 0 and morango < 5:
            valor1 = morango*2.5
        elif morango >= 5:
            valor1 = morango*2.2
        else:
            print("Favor não colocar valores negativos, favor reniciar o programa.")

        if maca > 0 and maca < 5:
            valor2 = maca*1.8
        elif maca >= 5:
            valor2 = maca*1.5
        else:
            print("Favor não colocar valores negativos, favor reniciar o programa.")

        if maca + morango > 8 or valor1 + valor2 > 25:
            print("você comprou "+str(maca)+"kg de maçãs")
            print("você comprou "+str(morango)+"kg de morangos")
            print("Com o desconto de 10% você deve pagar: "+str((valor1+valor2)*0.9)+" reais")
        else:
            print("você comprou "+str(maca)+"kg de maçãs")
            print("você comprou "+str(morango)+"kg de morangos")
            print("Você deve pagar: "+str(valor1+valor2)+" reais")
        
        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()

    except ValueError:
        print("Apenas serão aceitos respostas expressas numericamente!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")
