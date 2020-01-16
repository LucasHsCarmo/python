print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3

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
        print("Você acertou o chute\n")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto\n")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto\n")

print("Fim de jogo")