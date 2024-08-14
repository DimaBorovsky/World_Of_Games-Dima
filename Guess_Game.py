import random


secret_number = None
def generate_number(difficulty_level):
    global secret_number
    secret_number = random.randint(1,difficulty_level)


def get_guess_from_user(difficulty_level):
    user_input = input(f"Please Choose a number between 1 and choosen {difficulty_level}: ")
    return int(user_input)


def compare_results(user_input):
    global secret_number
    print(f"secret number is:{secret_number}")
    if user_input == secret_number:
        print("Wow You Won ")
    else:
        print("You lost try again !")


def play(difficulty_level):
    generate_number(difficulty_level)
    user_input = get_guess_from_user(difficulty_level)
    compare_results(user_input)