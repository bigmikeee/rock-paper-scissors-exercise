# Rock, Paper, Scissors Exercise

import random

#Game description and creating input box for user and randomized computer choice
print("Welcome Player to the Rock, Paper, Scissors Game!")
player_choice = str(input("Please input a move: 'Rock', 'Paper', or 'Scissors':\n")).title()
computer_choice_list =  ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(computer_choice_list)
print(f"\nYou chose {player_choice}, computer chose {computer_choice}.\n")

#Prints results based on user choice and randomized computer choice
if player_choice == computer_choice:
    print("Tie!")
elif player_choice == "Rock":
  if computer_choice == "Paper":
    print("You lose!", computer_choice, "beats", player_choice)
    print("\nThanks for playing. Please play again!")
  else:
    print("You win!", player_choice, "beats", computer_choice)
    print("\nThanks for playing. Please play again!")
elif player_choice == "Paper":
    if computer_choice == "Scissors":
      print("You lose!", computer_choice, "beats", player_choice)
      print("\nThanks for playing. Please play again!")
    else:
      print("You win!", player_choice, "beats", computer_choice)
      print("\nThanks for playing. Please play again!")
elif player_choice == "Scissors":
    if computer_choice == "Rock":
        print("You lose...", computer_choice, "beats", player_choice)
        print("\nThanks for playing. Please play again!")
    else:
        print("You win!", player_choice, "beats", computer_choice)
        print("\nThanks for playing. Please play again!")
else:
      print("That's not a valid play. Please re-run and type a valid input!")