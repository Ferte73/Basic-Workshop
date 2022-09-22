condicao = str("sim")

while condicao == "sim":

    try:

        n1 = float(input("Primeira nota: "))
        n2 = float(input("Segunda nota: "))

        nota = (n1+n2)/2

        if nota <= 10 and nota >= 9:
            print("Sua média é: "+str(nota))
            print("Sua classificação é: A")
            print("APROVADO!")

        if nota <= 9 and nota >= 7.5:
            print("Sua média é: "+str(nota))
            print("Sua classificação é: B")
            print("APROVADO!")

        if nota <= 7.5 and nota >= 6:
            print("Sua média é: "+str(nota))
            print("Sua classificação é: c")
            print("APROVADO!")

        if nota <= 6 and nota >= 4:
            print("Sua média é: "+str(nota))
            print("Sua classificação é: D")
            print("REPROVADO!")

        if nota <= 4 and nota >= 0:
            print("Sua média é: "+str(nota))
            print("Sua classificação é: E")
            print("REPROVADO")
    
        if nota < 0:
            print("Médias negativas não são possíveis")

        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()

        
    except ValueError:
        print("Por favor, apenas expresse a nota de forma numérica!") 
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")