from selenium import webdriver
import requests
import random
from Live import difficulty
from time import sleep

my_drive = webdriver.Chrome()
random_number = random.randint(1,100)
user_input = input(f"how much is {random_number} in ILS :")

def get_exchange_rate():
    url = "https://v6.exchangerate-api.com/v6/9ddcd0dd2ed9984915656f3e/latest/USD"
    my_drive.get(url)
    sleep(1)


def generate_number():
    print(f"Given this amonunt {random_number} in USD Guess how much in ILS :")
    get_exchange_rate()


def compare_results():
    if user_input == random_number:
        print("nice you won ")
    else:
        print("Wormg try again ")



def play3():
    get_exchange_rate()
    generate_number()
    compare_results()


play3()