from Guess_Game import play
from Memory_Game import play1
from CurrencyRouletteGame import play3

name = input("What's your name:")
game = [1,2,3]
difficulty = [1,2,3,4,5]

def welcome_user():
  print(f"Hello {name}, and welcome to the World of games !")


def load_game():
    print("1-Memory Game\n2-Guess Game\n3-Currency roulette")
    game_choice = input(f"Please Choose a  game {game}:")

    if game_choice == str(1):
        print("you Chose Memory Game")
    elif game_choice == str(2):
        print("you Chose guess game")
    elif game_choice == str(3):
        print("You choose currency roulette")
    else:
        print("invalid choice")
        return

    difficulty_of_game = int(input(f"Please choose a difficulty level{difficulty}: "))

    if difficulty_of_game in difficulty:
        print(f"You chose level {difficulty_of_game}")
    else:
        print("Invalid choice. Please choose from the following list: 1, 2, 3, 4, 5")
        return

    if game_choice == str(1):
        play1()

    elif game_choice == str(2):
        play()

    elif game_choice == str(3):
        play3()

    else:
        print("Nope")

