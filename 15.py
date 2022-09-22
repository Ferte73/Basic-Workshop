from multiprocessing.sharedctypes import Value


condicao = str("sim")

while condicao == "sim":

    try:

        n1 = float(input("Qual foi a sua primeira nota?"))
        n2 = float(input("Qual foi a sua segunda nota?"))
        n3 = (n1 + n2) / 2

        if n3 < 7:
            print("Você reprovou!")
        if n3 == 10:
            print("Você passou com distinção")
        if n3 >= 7:
            print("Você passou!")

        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()


    except ValueError:
        print("Só será lido numeros expressos numericamente!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")