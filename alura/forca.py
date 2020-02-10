import random

def jogar():

    print("***************************")
    print("Bem vindo ao jogo da forca!")
    print("***************************")

    palavras = [] #Lista zerada

    with open("palavras.txt", "r") as arquivo: #Abre e fecha o arquivo após executado o FOR
        for linha in arquivo:
            linha = linha.strip()  #Elimando espaços do arquivo "\n"
            palavras.append(linha)

    palavra_aleatoria = random.randrange(0, len(palavras)) #Escolhendo posição da palavra aleatoriamente
    palavra_secreta = palavras[palavra_aleatoria].upper()

    palpite = ['_' for letra in palavra_secreta] #Insere "_" para cada letra dentro da palavra_secreta

    enforcou = False
    acertou = False
    erros = 0

    print(palpite)

    #enquanto(True):
    while(not enforcou and not acertou):

        chute = input("\nInforme uma letra: ")
        chute = chute.strip().upper() #Retirando os espaços em branco

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra): #Comparando letras maiusculas
                    palpite[index] = letra #Posição correta da letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(len(palpite)-erros))    

        print(palpite)

        if(erros == len(palpite)):
            break
        if("_" not in palpite):
            break

    if("_" not in palpite):
        print("\nVocê ganhou!")
    else:
        print("\nVocê perdeu!")

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()