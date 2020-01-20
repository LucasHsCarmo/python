import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randint(1,100)
total_tentativas = 0
pontuacao = 1000

print("\nQual o nível de dificuldade?")
print("(1) - Fácil")
print("(2) - Médio")
print("(3) - Difícil")

nivel = int(input("\nEscolha o seu nível: "))

if(nivel == 1):
    total_tentativas = 20
elif(nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

for rodada in range(1, total_tentativas+1):
    print("Tentativa {} de {}".format(rodada,total_tentativas))

    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou:", chute)

    if(chute < 1 or chute > 100):
        print("Você deve chutar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto 
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou o chute e fez {} pontos!\n".format(pontuacao))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto\n")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto\n")
        pontos_perdidos = abs(pontos_perdidos - chute)
        pontuacao -= pontos_perdidos

print("Fim de jogo")