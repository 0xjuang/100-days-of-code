import random
import time

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

ascii_choices = [rock, paper, scissors]
str_choices = ["rock", "paper", "scissors"]

print("Let's play Rock Paper Scissors!")
time.sleep(1)
usr_choice = input("What do you choose? (rock, paper, scissors): ")

if usr_choice not in str_choices:
    print("Sorry, that's not a valid choice.")
usr_index = str_choices.index(usr_choice)
usr_choice = ascii_choices[usr_index]
comp_index = random.randint(0, 2)
comp_choice = ascii_choices[comp_index]

print("ROCK!")
time.sleep(1)
print("PAPER!")
time.sleep(1)
print("SCISSORS!")
time.sleep(2)
print(f"\nYou chose:\n{usr_choice}")
print(f"Computer chose:\n{comp_choice}")

if usr_index == comp_index:
    print("It's a tie!")
elif (usr_index == 0 and comp_index == 2) or \
    (usr_index == 1 and comp_index == 0) or \
    (usr_index == 2 and comp_index == 1):
    print("You win!")
else:
    print("You lose!")
