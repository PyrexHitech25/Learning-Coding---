import random
from user_input_jn import yes_or_no


def greetings():
    print("Welcome to my Rock, Paper, Scissor - Game, hope you enjoy! :)\n")
    game_loop()


def comp_choice():
    return random.choice(['Rock', 'Paper', 'Scissor'])


def game_loop():
    while True:
        print("You can choose between 'Rock', 'Paper' and 'Scissor'!")
        while True:
            player_input = str(input("\n").strip().title())
            if player_input in ('Rock', 'Paper', 'Scissor'):
                break
            else:
                print("Choose between 'Rock', 'Paper' and 'Scissor'!")

        computer_choice = comp_choice()

        if player_input == computer_choice:
            print("It's a tie!\n")
        elif (
                (player_input == "Rock" and computer_choice == "Scissor") or
                (player_input == 'Paper' and computer_choice == "Rock") or
                (player_input == "Scissor" and computer_choice == "Paper")
        ):
            print(f"You win! :), I got {computer_choice}\n")
        else:
            print(f"You lose! :(, I got {computer_choice}\n")

        print("Do you wanna play again? y/n\n")
        if not yes_or_no():
            print("Thanks for playing!\n")
            break
greetings()