import random
from os import system, name
from hangman_art import logo, stages
from hangman_food import food_words

# Printing the game logo
print(logo)

# Setting up the words for the game
word_list = food_words
word_used = random.choice(word_list)

# Setting up the test case for the words
word_picked = []
for letter in word_used:
    word_picked += letter

# Showing the size of the word picked
game_display = []
for letter in word_picked:
    game_display += '_'
print(game_display)

# Initializing the win and lose conditions
win_condition = False
attempts = 6
guesses = []

# Running the game until a the win_condition is met
while not win_condition:
    
    # Taking, storing, and handling the guess letters
    guess_letter = input('Guess a letter: ').lower()
    
    # Clears terminal after each guess
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    
    if guess_letter in guesses:
        print(f'You already used "{guess_letter}", try again')
    else:
        #  fills in the blank values when correct
        for index, letter in enumerate(word_picked):
            if letter == guess_letter:
                game_display[index] = guess_letter

        if guess_letter not in word_picked:
            attempts -= 1
            print(f'The letter "{guess_letter}" is not in this word, try again')

        print(stages[attempts])
    
    guesses += guess_letter
    print(game_display)
    
    if '_' not in game_display:
        win_condition = True
        print('You Win')
    elif attempts == 0:
        win_condition = True
        print('You Lose')
        print(f'The word was "{word_picked}"')
