import random
import time
from user_input_jn import yes_or_no


def greetings():
    print("Welcome to my Dice-Code!")
    time.sleep(2)
    dice()

def dice():
    while True:
        dice = random.randint(1, 6)
        print(f"\nThe Dice-number is = {dice}\n")
        time.sleep(4)
        print("Do you wanna dice again? y/n")
        if not yes_or_no():
            print("Thanks for using! :)")
            break

greetings()

