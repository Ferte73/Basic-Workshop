condicao = str("sim")

while condicao == "sim":


    try:
        lista = []

        lista.append(float(input("digite o número que você deseja colocar (limite de três números):")))
        lista.append(float(input("digite o número que você deseja colocar (limite de três números):"))) 
        lista.append(float(input("digite o número que você deseja colocar (limite de três números):"))) 

        lista_reversa = sorted(lista, reverse=True)

        print(lista_reversa[0])

        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()


    except ValueError:
        print("Faça o programa apenas com numeros reais")
    condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")