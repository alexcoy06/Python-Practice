# https://ascii.co.uk/art the treasure tab
print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
    '''
)

print("Welcome to Treasure Island, Vault Hunter!")
print("Your mission, should you choose to accept, is to find the legendary treasure. Let's get this loot!")

first_choice = (input('You stumble upon a gnarly fork in the road. Only options: "left" or "right". What\'s your move, Vault Hunter?\n')).lower()
if first_choice == 'left':
    second_choice = (input('Alright, you\'re now at a raging river. Do you dare to walk "across" the shallow water or take the long mile "hike" around? Choose wisely.\n')).lower()
    if second_choice == 'hike':
        third_choice = (input('Whoa! Two doors appear out of nowhere; one blazing "red", the other electric "blue". Which one do you pick?\n')).lower()
        if third_choice == 'red':
            print('BOOM! Victory is yours!')
        elif third_choice == 'blue':
            print('Chomped by psycho beasts. GAME OVER.')
        else:
            print('Invalid choice. GAME OVER.')
    else:
        print('Ambushed by a pack of mutant trout. GAME OVER.')
else:
    print('Oops! You tumble into a pit of despair. GAME OVER.')