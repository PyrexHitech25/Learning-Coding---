from datetime import datetime
from time import sleep

birthday_input = input("Name your Birthday like this: Day, Month, Year\n")

birthday = datetime.strptime(birthday_input, '%d, %m, %Y')

calc = datetime.now() - birthday

print("\nThinking....\n")

sleep(1)

print(f"Your whole lifetime is = {calc}!" )



