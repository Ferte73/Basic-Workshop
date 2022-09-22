i = 0

while True:

    try:
        tipo = input("Entre residencial, comercial e industrial. Qual é o seu tipo de consumidor? ").lower()

        consumo = float(input("Qual foi o consumo em m³ de água?"))

        if tipo == "residencial":
            consumo = consumo*0.05 + 50
            print("O valor a ser pago é R$"+str(consumo))
    
        elif tipo == "comercial":
            if consumo <= 80:
                print("O valor a ser pago é de R$500,00")
            else: 
              print("O valor a ser pago é de "+str(500 + (consumo-80)*0.25))

        elif tipo == "industrial":
            if consumo <=100:
               print("O valor a ser pago é de R$800,00")
            else:
             print("O valor a ser pago é de R$"+str(800+(consumo-100)*0.04))

        i = i + 1
        print("O número da sua conta é : 00"+str(i))

        condicao= input("Quer colocar mais uma conta de luz? (Sim/Não) ").lower()
        if condicao == "sim":
            continue
        else: 
            break
    except ValueError:
        print("Favor utilizar apenas valores expressos numericamente na questão de consumo\ne apenas os nomes entre 'industrial', 'residencial' e 'comercial' na resposta de tipo de consumidor!")
        condicao= input("Quer tentar de novo? (Sim/Não) ").lower()
        if condicao == "sim":
            continue
        else: 
            break

print("Obrigado por usar meu programa")