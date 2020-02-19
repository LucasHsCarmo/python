import adivinhacao
import forca

def escolhe_jogo():

    print("***************************")
    print("Bem vindo escolha seu jogo!")
    print("***************************")

    print("\nQual jogo você deseja jogar?")
    print("(1) - Adivinhação")
    print("(2) - Forca")

    jogo = int(input("Escolha seu jogo: "))

    if (jogo == 1):
        print("\nJogando Adivinhação")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("\nJogando Forca")
        forca.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()