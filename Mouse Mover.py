from random import randint
from time import sleep
import pyautogui

def greetings():

    print("Welcome to my Mouse-Mover Program ! :)\n")
    print("The mouse will move in every interval you want! \n")
    sleep(1)
    mover()

def mover():

    eingabe = int(input("Name the seconds between every move! \n"))

    try:

        while True:
            print(f"The mouse will move every {eingabe} seconds.\n")
            x = randint(600, 700)
            y = randint(200, 700)
            pyautogui.move(x, y)
            sleep(eingabe)

    except KeyboardInterrupt:
        print("Thanks for using! :)\n")


if __name__ == "__main__":
    greetings()