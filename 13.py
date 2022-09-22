from multiprocessing.sharedctypes import Value


condicao = str("sim")

while condicao == "sim":

    try:
    
        publico = float(input("Para o calculo da receita total produzida pela partida ,quantas pessoas foram ao jogo? "))

        print("A receita do jogo foi "+str((publico)+(publico*25)+(publico*30)+(publico*20))+" reais.")
        print("A receita do jogo popular: "+str(publico)+" reais.")
        print("A receita do jogo geral: "+str(publico*25)+ " reais.")
        print("A receita do jogo por arquibancada: "+str(publico*30)+ " reais.")
        print("A receita do jogo por cadeira: "+str(publico*25)+ " reais.")
        condicao = input("Você quer continuar a executar o programa?\nApenas será lido 'sim' como resposta positiva! ").lower()


    except ValueError:
        print("Apenas valores expressos numericamente serão aceitos!!")
        condicao = input("Você quer tentar de novo?\nApenas será lido 'sim' como resposta positiva! ").lower()

print("")
print("Obrigado por usar meu programa!")