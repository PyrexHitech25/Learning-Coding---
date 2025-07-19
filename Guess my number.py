import random

def play_game():

  print("Welcome to my Numbers-Game! \n")

  computer_choose = random.randint(1, 101)

  print("Choose a number between 1 and 100!")

  player_trys = 7

  while player_trys > 0:

    try:

      player_input = int(input())

      if player_input == computer_choose:

        print("You won, nice game! \n")
        break
      elif player_input < computer_choose:
        player_trys -= 1
        print(f"Your number was too small! Try again, you have right now {player_trys} trys left! \n")
      else:
        player_trys -= 1
        print(f"Your number was too big! Try again, you have right now {player_trys} trys left! \n")

    except ValueError:
      print("Please name a number, nothing else! :)")

    if player_trys == 0:
      print(f"You lose! my number was {computer_choose} :) \n")

if __name__ == "__main__":
  play_game()