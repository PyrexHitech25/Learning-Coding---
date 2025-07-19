def entrance():
    print("Welcome to my FizzBuzzGame!\n")
    print("You can name me a number and i will tell you if its 'Fizz','Buzz' or 'FizzBuzz'")
    while True:
        try:
            player_number = int(input("\nName a number!\n"))
            function(player_number)
            break
        except ValueError:
            print("\nPlease name a number!\n")

def function(number):
    if number % 15 == 0:
        print("\nFizzBuzz\n")
    elif number % 5 == 0:
        print("\nBuzz\n")
    elif number % 3 == 0:
        print("\nFizz\n")
    else:
        print("\nNo match\n")
    play_again()

def play_again():
    print("Do you wanna play again? j/n\n")
    while True:
        user_input = str(input("").strip().lower())
        if user_input == "j":
            try:
                player_number = int(input("\nName a number\n"))
                function(player_number)
            except ValueError:
                print("Please name a number!\n")
        elif user_input == "n":
            break
        else:
            print("\nJust type 'j' or 'n'\n")
entrance()
