condicao = str("sim")

while condicao == "sim":

    try:
        print("Considere as expressões D, R e S , onde:")
        print("D = R + S      ,    R = (A + B)² ")
        print("    -----")
        print("      2             S = (B + C)² ")

        a = float(input("Qual o valor de A?"))
        b = float(input("Qual o valor de B?"))
        c = float(input("Qual o valor de C?"))
        r = (a + b) * (a + b)
        s = (b + c) * (b + c)
        d = (r + s) / 2

        print(d)
    
        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()


    except ValueError:
        print("Por favor, apenas números expressos numericamente serão aceitos!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")    