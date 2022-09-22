from multiprocessing.sharedctypes import Value

condicao = str("sim")


while condicao == "sim":
    Lista = {}
    lista = []

    try:

        print("Por favor, digite o produto e logo após digite o preço desse produto")

        produto1 = input("Digite o produto: ")
        valor1 = float(input("Digite o valor do produto: "))

        produto2 = input("Digite o produto: ")
        valor2 = float(input("Digite o valor do produto: "))

        produto3 = input("Digite o produto: ")
        valor3 = float(input("Digite o valor do produto: "))

        Lista.update({valor1:produto1})
        Lista.update({valor2:produto2})
        Lista.update({valor3:produto3})

        lista.append(valor1)
        lista.append(valor2)
        lista.append(valor3)

        lista_reversa = sorted(lista)


        print("Você deve comprar o/a "+str(Lista.get(lista_reversa[0])))

        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()


    except ValueError:
        print("Por favor, apenas valores expressos numericamente serão aceitos nos valores de produto!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")        