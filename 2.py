condicao = str("sim")

while condicao == "sim":
    try:
        salario_por_hora = float(input("Quanto você ganha por hora? "))
        horas_trabalhadas = float(input("Quantas horas você trabalha por dia? "))
        dias_trabalhados = float(input("Quantos dias você trabalha em um mês? "))

        salario = salario_por_hora * horas_trabalhadas * dias_trabalhados

        print("Você recebe "+str(salario)+" reais por mês")

        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()


    except ValueError:
        print("Apenas será lido valores numéricos")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("Obrigado por usar meu programa!")