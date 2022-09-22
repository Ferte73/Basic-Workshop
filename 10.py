condicao = str("sim")
#Trying to don't spent much time on this!!

while condicao == "sim":

    try:
        altura = float(input("Para calcular o seu peso ideal, por favor indique sua altura em metros: "))
        print("Seu peso ideal é :"+str((72.7 * altura) - 58)+" kg.")
        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()

    except ValueError:
        print("Por favor, apenas se expresse numericamente!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")