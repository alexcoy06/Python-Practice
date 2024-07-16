import random

print("Welcome to the ultimate Rock, Paper, Scissors showdown!")

# These are the choices
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

# Randomizing the computer choice for the above code
choice = [rock, paper, scissors]
picked = random.randint(0,2)

# Functionality for the users choice
user = input('Choose your weapon: "Rock", "Paper", or "Scissors". Ready, set, shoot!\n').lower()
user_choice = ['rock', 'paper', 'scissors']
user_pick = user_choice.index(user)

#Test the code with the below lines delete the '#'
#Make sure to comment line 36 out using a '#'
#user_pick = 0
#picked = 2

# Printing the user and computer choice
print(f'You choose:\n{choice[user_pick]}')
print(f'Your opponent Choose\n{choice[picked]}')

# Setting the conditions for Win, Lose, and Draw
if user_pick == picked:
    print('Draw')
elif (user_pick == 0) & (picked == 1):
    print('You Lose')
elif (user_pick == 1) & (picked == 2):
    print('You Lose')
elif (user_pick == 2) & (picked == 0):
    print('You Lose')
else:
    print('You Win')