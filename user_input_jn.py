def yes_or_no():
    while True:
        choice = str(input("Type in 'y' or 'n'\n").strip().lower())
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("")

