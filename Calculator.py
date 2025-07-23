from user_input_jn import yes_or_no

def greetings():
    print("Welcome to my Calculator! Enjoy! :)\n")
    calc()

def calc():
    while True:

        number_one = int(input("Name your first number! \n").strip())

        print("Choose your calculation method!\n")
        print("(1) Addition")
        print("(2) Substraction")
        print("(3) Divide")
        print("(4) Multiplication\n")

        while True:
            player_input = int(input("").strip())
            if player_input in (1, 2, 3, 4):
                break
            else:
                print("Choose a Calculation Method!\n")

        number_two = int(input("Name your second number! \n").strip())

        if player_input == 1:
            print("=")
            print(number_one + number_two)
        elif player_input == 2:
            print("=")
            print(number_one - number_two)
        elif player_input == 3:
            print("=")
            print(number_one / number_two)
        else:
            print("=")
            print(number_one * number_two)

        print("\nDo you wanna calculate again? y/n\n")
        if not yes_or_no():
            print("Thanks for using!")
            break
greetings()
