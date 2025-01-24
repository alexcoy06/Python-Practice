import random
import math
from os import system, name


logo = '''
  _   _                 _                  _____                     
 | \ | |               | |                / ____|                    
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __|
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ 
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/
'''

def clear_screen():
  if name == 'nt':
    system('cls')
  else:
    system('clear')
    
def giveClue(howClose):
  temp = ''
  if abs(howClose) < 2:
    temp = 'hot'
  elif abs(howClose) < 3:
    temp = 'warm'
  elif abs(howClose) < 5:
    temp = 'cool'
  else:
    temp = 'cold'
    
  # https://docs.python.org/3/reference/expressions.html#conditional-expressions
  benchmark = 'low' if howClose > 0 else 'high'
    
  return temp, benchmark

def blackJack():
  gameIsActive = True
  gameHard = 5
  gameEasy = 10

  print(logo)
  start = input('Welcome to the Number Guessing Game! Feeling lucky? Type "y" for yes or "n" for no: ').lower()

  if start == 'n':
    gameIsActive = False
  elif start == 'y':
    attempts = 0
    gameMode = input('How lucky are you feeling? Type "very" or "slightly": ').lower()
    if gameMode == 'very':
      attempts = gameHard
    elif gameMode == 'slightly':
      attempts = gameEasy

    if gameMode in ['very', 'slightly']:
      number = random.randint(1, 100)
      print(number)
    else:
      print('Wrong Input')
  else:
    print('Wrong Input')



  while gameIsActive:

    userGuess = int(input(F'You have {attempts} attempts remaining.\nMake a guess: '))

    if userGuess == number:
      gameIsActive = False
      print('Correct')
    else:
      attempts -= 1
      howClose = math.ceil((number - userGuess) / 5)

      temp, benchmark = giveClue(howClose)
      print(f'I\'ll give you a clue, you are getting {temp}; you are {benchmark}')

    if attempts == 0:
      gameIsActive = False
      print(f'Nice try the number was {number}')
      
    if gameIsActive == False:
      playAgain = input('Do you want to play again, yes \'y\' or no \'n\': ')
      if playAgain == 'y':
        blackJack()
        clear_screen()
  clear_screen()

blackJack()
print('Thanks for playing')