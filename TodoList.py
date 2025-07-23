def greetings():
    print("Welcome to my Todo-List! :)\n")
    list()

def list():
    user_input = str(input("Add your task!\n").strip().title())
    list = []
    list.append(user_input)

    while True:
        print("\n(1) Add a Task")
        print("(2) View list")
        print("(3) Remove a item")
        print("(4) Quit")

        while True:
            try:
                method = int(input("\n").strip())
                if method in (1, 2, 3, 4):
                    break
                else:
                    print("Name one of the functions above! \n")
            except ValueError:
                print("Name one of the functions above! \n")

        if method == 1:
            add = str(input("\nAdd your task!\n").strip().title())
            list.append(add)
            print("The task was added to the list!")
        elif method == 2:
            print(list)
        elif method == 3:
            delete = str(input("Which task do you want to remove?\n").strip().title())
            list.remove(delete)
            print("The task was removed from the list!\n")
        else:
            print("\nThanks for using!")
            break

greetings()