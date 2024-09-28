import random
from time import sleep

difficulty = 5


def generate_sequence(random_sequence):
    random_sequence = [random.randint(1,101)
                       for _  in range(difficulty)]
    print(f"Remember the sequence:{random_sequence}")
    sleep(0.7)
    return random_sequence


def get_list_from_user():
    user_input = input("Please enter the sequence with a comma:")
    user_list = list(map(int, user_input.split(',')))
    return user_list


def is_list_equal(random_sequence,user_list):
    return random_sequence == user_list

def play1():
    random_sequence = generate_sequence(difficulty)
    user_list =  get_list_from_user()
    if is_list_equal(random_sequence, user_list):
        print("nice You won ")
    else:
        print("better luck next time")



