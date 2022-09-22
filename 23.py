import math

condicao = str("sim")

while condicao == "sim":

    try:

        caixa = float(input("Quanto de dinheiro deseja sacar?"))
        cem = math.floor(caixa/100)
        cinquenta = math.floor((caixa - cem*100)/50)
        dez = math.floor((caixa - cem*100 - cinquenta*50)/10)
        cinco = math.floor((caixa - cem*100 - cinquenta*50 - dez*10)/5)
        um = (caixa - cem*100 - cinquenta*50 - dez*10 - cinco*5)

        if int(caixa) == float(caixa):
            if caixa >= 10 and caixa <=600:
                print("Você receberá de "+str(cem)+" notas de cem!")  
                print("Você receberá de "+str(cinquenta)+" notas de cinquenta!") 
                print("Você receberá de "+str(dez)+" notas de dez!") 
                print("Você receberá de "+str(cinco)+" notas de cinco!") 
                print("Você receberá de "+str(um)+" notas de um!")       
            else:
                print("Por favor, apenas valores entre 10 e 600!")
        else: 
            print("por favor apenas valores inteiros")

        condicao = input("Você quer continuar a sacar dinheiro?\nApenas será lido 'sim' como resposta positiva! ").lower()

    
    except ValueError:
        print("Apenas expresse numericamente os valores que deseja sacar!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")