import time

def countdown():
    min = int(input("How many minutes?\n"))
    sec = int(input("How many seconds?\n"))
    print(f"Time set on {min} min and {sec} sec\n")

    while min > 0:
        time.sleep(60)
        min -= 1
    while sec > 0:
        time.sleep(1)
        sec -= 1

    print("Time is over!")

countdown()