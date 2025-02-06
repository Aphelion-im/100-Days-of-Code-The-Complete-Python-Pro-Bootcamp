# https://ascii.co.uk/art

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
player_choice = int(input("0 for rock. 1 for paper. 2 for scissors: "))

if 0 <= player_choice < 3:
    print(f"Player chose: {choices[player_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

if player_choice == computer_choice:
    print("Draw!")
elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (
        player_choice == 2 and computer_choice == 1):
    print("Player wins!")
elif player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number. You lose!")
else:
    print("Computer wins!")
