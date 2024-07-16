import random
from os import system, name

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0  
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def blackJack():
    user_hand = []
    computer_hand = []
    gameIsActive = True

    play = input("Would you like to play a game of BlackJack? Enter 'Y' or 'N':").lower()
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    clear_screen()
    print(logo)

    if play == 'n':
        gameIsActive = False
        print('Thank you for playing')
    elif play == 'y':
        for _ in range(2):
            user_hand.append(random.choice(cards))
            computer_hand.append(random.choice(cards))

        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)

        print(f"Your starting hand is {user_hand[0]} and {user_hand[1]}, your current total is: {user_score if user_score != 0 else 'Blackjack!'}")
        print(f"The computer's top card is {computer_hand[1]}")

        if user_score == 0:
            print("Blackjack! You win!")
            gameIsActive = False
        elif computer_score == 0:
            print("Computer has Blackjack. You lose!")
            gameIsActive = False
            
    while gameIsActive:
        draw = input("If you want to draw another card, type 'Y'; otherwise, type 'N':").lower()
        if draw == 'y':
            card_drawn = random.choice(cards)
            user_hand.append(card_drawn)
            current_score = calculate_score(user_hand)
            print(f'You drew a {card_drawn} and your current score is: {current_score}')
            if current_score > 21:
                gameIsActive = False
                print('BUST!!! You Lose!')
        elif draw == 'n':
            gameIsActive = False
            while calculate_score(computer_hand) < 17:
                computer_hand.append(random.choice(cards))

            user_score = calculate_score(user_hand)
            computer_score = calculate_score(computer_hand)

            print(f'The computer had a hand of {computer_hand}, with a score of {computer_score}')

            if user_score > 21:
                print('BUST!!! You Lose!')
            elif computer_score > 21 or user_score > computer_score:
                print('You Win!')
            elif user_score < computer_score:
                print('You Lose!')
            else:
                print('It\'s a Draw!')
        else:
            print('Incorrect input.')

    if gameIsActive == False:
        blackJack()

blackJack()
