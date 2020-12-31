from random import randint
from time import sleep

def jogar():

    print('-' * 30)
    print("     GAME MEGA SENA  ")
    print('-' * 30)

    card = list()
    games = list()

    qtade = int(input("\nHow many games do you want to make: "))
    attempt = 1
    print("\n")

    while attempt <= qtade:
        count = 0
        while True:
            numero = randint(1,60)
            if numero not in games:    
                games.append(numero)
                count += 1
            if count >= 6:
                break
        games.sort() # sorting list
        card.append(games[:]) # copying the list games to card
        games.clear() # cleaning list games
        attempt += 1
            
    print('-' * 10, f'Drawing {qtade} games', '-' * 10, "\n")

    for key, value in enumerate(card):
        print(f'Game {key+1}: {value}')
        sleep(1)

    print("\n",'-' * 10, f'Good Luck', '-' * 10, )

if(__name__ == "__main__"):
    jogar()