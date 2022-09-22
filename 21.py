condicao = str("sim")

while condicao == "sim":

    try:

        lista = []

        l1 = float(input("Qual o primeiro lado do triangulo?"))
        l2 = float(input("Qual o segundo lado do triangulo?"))
        l3 = float(input("Qual o terceiro lado do triangulo?"))

        lista.append(l1)
        lista.append(l2)
        lista.append(l3)

        lista = sorted(lista)

        if lista[2] <= lista[1] + lista[0]:
            print("Esse triângulo é possível!")
            if lista[2] == lista[1] and lista [2] == lista[0]:
                print("Esse triângulo é Equilátero!")
            elif lista[2] == lista[1] and lista[2] > lista[0]:
                print("Esse triângulo é Isóceles!")
            elif lista[2] > lista[1] and lista[1]==lista[0]:
                print("Esse triângulo é Isóceles!")
            elif lista[2]*lista[2] == lista[1]*lista[1] + lista[0]*lista[0]:
                print("Esse triângulo é Retangulo!")
            else:
                print("Esse triângulo é Escaleno!")
        else: 
            print("Esse triângulo não é possível!")

        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()

    
    except ValueError:
        print("Apenas expresse os lados do triângulo de forma numerica!!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")