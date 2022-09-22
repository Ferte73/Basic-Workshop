condicao = str("sim")

while condicao == "sim":

    try:

        print("Tabela de idades e sua respectiva classificação:")
        print("Infantil A - 5 a 7 anos | Infantil B - 8 a 10 anos")
        print("Juvenil A - 11 a 13 anos| Juvenil B - 14 a 17 anos")
        print("Adulto - Acima de 18 anos")

        idade = int(input("Qual a sua idade?"))

        if idade >= 0 and idade < 5:
            print("Você não tem idade para começar natação!")
        elif idade >=5 and idade <= 7:
            print("Você está na classificação Infantil A")
        elif idade >=8 and idade <= 10:
            print("Você está na classificação Infantil B")
        elif idade >=11 and idade <= 13:
            print("Você está na classificação Juvenil A")
        elif idade >=14 and idade <= 17:
            print("Você está na classificação Juvenil B")
        elif idade > 18:
            print("Você é adulto!")
        else:
            print("Digite uma idade válida!")
        
        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()

    except ValueError:
        print("Só serão aceitas idades expressas numericamente, inteiras e positivas!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()


print("")
print("Obrigado por usar meu programa!")