condicao = str("sim")

while condicao == "sim":

    try:

        sexo = input("Digite seu sexo(só será lido pelo programa 'homem' ou 'mulher'): ").lower()
        altura = float(input("Digite sua altura em metros: "))

        if altura >= 0:

            if sexo == "mulher":
                print("Seu peso ideal é "+str(62.1*altura - 44.7)+"kg")

            elif sexo == "homem":
                print("Seu peso ideal é "+str(72.7*altura - 58)+"kg")

            else:
                print("Apenas será reconhecido 'homem' ou 'mulher'")
        
        else:
            print("Apenas alturas válidas!")

        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()


    except ValueError:
        print("Só será aceito altura expressa numericamente!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")