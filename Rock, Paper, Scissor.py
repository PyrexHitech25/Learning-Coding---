import random

def greetings():
    print("Welcome to my Rock, Paper, Scissor - Game, hope you enjoy! :)\n")
    game()

def comp_choice():
    return random.choice(['Rock', 'Paper', 'Scissor'])

def game():
    print("You can choose between 'Rock', 'Paper' and 'Scissor'!")
    while True:
        player_input = str(input("\n").strip().title())
        if player_input in ('Rock', 'Paper', 'Scissor'):
            break
        else:
            print("Choose between 'Rock', 'Paper' and 'Scissor'!")
    computer_choice = comp_choice()
    try:
        if player_input == computer_choice:
            print("Its a tie!\n")
        elif (
            (player_input == "Rock" and computer_choice == "Scissor") or
            (player_input == 'Paper' and computer_choice == "Rock") or
            (player_input == "Scissor" and computer_choice == "Paper")
        ):
            print(f"You win! :), i got {computer_choice}\n")
        else:
            print(f"You lose! :(, i got {computer_choice}\n")
        play_again()
    except ValueError:
        print("Please choose between 'Rock', Paper' or 'Scissor'!\n")

def play_again():
    print("Do you wanna play again? j/n\n")
    while True:
        again = str(input("").strip().lower())
        if again == "j":
            game()
        elif again == "n":
            print("Thanks fpr playing :)\n")
            break
        else:
            print("Just type 'j' or 'n'\n")
greetings()





