condicao = str("sim")
#Trying to don't spent much time on this!!

while condicao == "sim":
    try:

        print("Para as operação de: 2ab/2 ou ab")
        print("                        3a+c")
        print("                          c³")


        a = int(input("Qual é o primeiro número? (inteiro) "))
        b = int(input("Qual é o segundo número? (inteiro) "))
        c = float(input("Qual é o terceiro número? (real) "))
    
        print("a = "+str((a * 2) * (b / 2)))
        print("b = "+str((a * 3) + c))
        print("c = "+str(c*c*c))
        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva ").lower()


    except ValueError:
        print("Apenas utilize números inteiros para 'a' e 'b', e apenas utilize números reais para 'c'!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva ").lower()

print("")
print("Obrigado por usar meu programa!")        