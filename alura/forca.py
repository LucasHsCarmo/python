import random

def jogar():

    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    palpite = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(palpite)

    #enquanto(True):
    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, palpite)
        else:
            erros += 1
            desenha_forca(erros)
            print("Ops, você errou! Faltam {} tentativas.".format(7-erros))    

        print(palpite)

        if(erros == len(palpite)):
            break
        if("_" not in palpite):
            break

    if("_" not in palpite):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def mensagem_abertura():
    print("***************************")
    print("Bem vindo ao jogo da forca!")
    print("***************************")

def carrega_palavra_secreta():
    palavras = [] #Lista zerada

    with open("palavras.txt", "r") as arquivo: #Abre e fecha o arquivo após executado o FOR
        for linha in arquivo:
            linha = linha.strip()  #Elimando espaços do arquivo "\n"
            palavras.append(linha)

    palavra_aleatoria = random.randrange(0, len(palavras)) #Escolhendo posição da palavra aleatoriamente
    palavra_secreta = palavras[palavra_aleatoria].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra] #Insere "_" para cada letra dentro da palavra_secreta

def pede_chute():
    chute = input("\nInforme uma letra: ")
    chute = chute.strip().upper() #Retirando os espaços em branco
    return chute

def marca_chute_correto(chute, palavra_secreta, palpite):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra): #Comparando letras maiusculas
            palpite[index] = letra #Posição correta da letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__ == "__main__"):
    jogar()