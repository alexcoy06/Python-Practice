import random
from game_data import animals, logo, verses
from os import system, name


def clear_screen():
  if name == 'nt':
    system('cls')
  else:
    system('clear')


def animal_picked(pick_from):
    index = random.randint(0, len(pick_from) - 1)
    animal = pick_from.pop(index)
    
    name = animal['name']
    kg = animal['average_weight']
    desc = animal['short_description']
    location = animal['location']
    return name, kg, desc, location, pick_from

# Testing for animal_picked function
#print(animal_picked())
#print(animal_picked())

def play_game():

    print(logo)
    score = 0
    game_is_active = True
    pick_from = animals

    option_a, weight_a, desc_a, location_a, pick_from = animal_picked(pick_from)

    while game_is_active:

        try:
            option_b, weight_b, desc_b, location_b, pick_from = animal_picked(pick_from)
        except TypeError:
            game_is_active = False
        
        print(f'{option_a}: {desc_a} Which are found in {location_a}.')
        print(verses)
        print(f'{option_b}: {desc_b} Which are found in {location_b}.\n')
        
        #View the weights to test choices results
        print(f'Weight B: {weight_b}\nWeight A: {weight_a}')
        choice = input(f"Does a {option_b} weigh more or less than a {option_a}: Type 'Higher' or 'Lower': ").lower()
        
        while (choice != 'higher') & (choice != 'lower'):
            choice = input(f"INCORRECT RESPONSE: Does a {option_b} weigh more or less than a {option_a}: Type 'Higher' or 'Lower': ").lower()
            
        if choice == 'higher':
            if weight_b >= weight_a:
                score += 1
            else:
                game_is_active = False
        else:
            if weight_b <= weight_a:
                score += 1
            else:
                game_is_active = False

        clear_screen()

        # Checking for pick_from list changes
        #print(len(pick_from))

        if game_is_active == True:
            option_a, weight_a, desc_a, location_a = option_b, weight_b, desc_b, location_b


    print(f'Your score is {score}')

    if score == 50:
        print("Wildlife Genius! You scored a perfect 50! You know animals better than most zoologists!")
    elif score >= 40:
        print(f"Animal Expert! With a score of {score}, you’re just shy of perfect! The animals bow to your knowledge!")
    elif score >= 30:
        print(f"Impressive! You scored {score} – you’re well-versed in the animal kingdom!")
    elif score >= 20:
        print(f"Good effort! With {score}, you’re showing potential. Keep exploring the animal world!")
    elif score >= 10:
        print(f"You scored {score} – you know some animals, but it’s time to brush up on your wildlife knowledge!")
    else:
        print(f"It’s a jungle out there! {score} shows you’re just starting your animal adventure!")
        
    restart = input('Do you want to play again, yes \'y\' or no \'n\': ')
    if restart == 'y':
        clear_screen()
        play_game()
        
play_game()
print('Thanks for playing')