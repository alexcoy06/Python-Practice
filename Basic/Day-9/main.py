from os import system, name

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
        
bids = {}
bidding = True
highest_bid = 0
winner = ''

while bidding:
    print(logo)
    bidder = input('Enter your name:\n')
    bid = int(input('Enter your bid amount:\n'))
    bids[bidder] = bid
    clear_screen()
    
    another_bid = input('Are there any more bids? Type "Yes" or "No"\n').lower()
    
    if another_bid == 'no':
        clear_screen()
        print(logo)
        bidding = False

        for person in bids:
            if bids[person] > highest_bid:
                highest_bid = bids[person]
                winner = person
                
        print(f'The winner is {winner} with a bid of ${highest_bid}')
