# Following along with the learning material to build a 
# ticket machine for a roller coaster company

print('Welcome to the rollercoaster!')
feet = int(input('Enter your height in feet: '))
inches = int(input('Enter the additional height in inches: '))

# converting feet and inches to total height
height = feet * 12 + inches
min_height = 48

# initializing the price for the ride
bill = 0

if height >= min_height:
    print('You can ride the rollercoaster!')
    age = int(input('What is your age?'))
    if age < 12:
        bill = 5
        print('Please pay $5.')
    elif age <= 17:
        bill = 7
        print('Please pay $7.')
    elif 45 < age < 55:
        bill = 0
        print('Enjoy the ride, no charge.')
    else:
        bill = 12
        print('Please pay $12.')
    
        
    photo = input('Do you want a photo taken? Y or N.\n')
    if photo == 'Y' or 'y':
        bill += 3    
    
    print(f'Your bill will be ${bill}')
else:
    print(f'Sorry, you are not tall enough({height}in). The minimum height is {min_height}in.')