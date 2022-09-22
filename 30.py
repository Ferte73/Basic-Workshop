condicao = str("sim")

while condicao == "sim":

    try:

        print("Para relembrar: Primeiro quadrante é o de x e y positivos,\no Segundo quadrante é o de x negativo e y positivo,\no Terceiro quadrante é o de x e y negativos,\no Quarto quadrante é o de x positivo e y negativo.")

        x = float(input("A coordenada x em valor númerico?"))
        y = float(input("A coordenada y em valor númerico?"))

        if x == 0 and y == 0:
            print("O ponto está no centro!")

        elif x==0 and y>0:
            print("O ponto está entre o primeiro e segundo quadrante.")

        elif x==0 and y<0:
            print("O ponto está entre o Terceiro e Quarto quadrante.")

        elif x>0 and y==0:
            print("O ponto está entre o Quarto e Primeiro quadrante.")

        elif x<0 and y==0:
            print("O ponto está entre o Segundo e Terceiro quadrante.")

        elif x>0 and y>0:
            print("O ponto está no primeiro quadrante.")

        elif x>0 and y<0:
            print("O ponto está no Quadrante quadrante.")

        elif x<0 and y>0:
            print("O ponto está no Segundo quadrante.")

        elif x<0 and y<0:
            print("O ponto está no Terceiro quadrante.")

        condicao = input("Quer continuar a executar o programa?\nApenas 'sim' será considerado uma resposta positiva! ").lower()

    except ValueError:
        print("Favor apenas utilizar números expressos numericamente!!")  
        condicao = input("Quer tentar de novo?\nApenas 'sim' será considerado uma resposta positiva! ").lower()
  