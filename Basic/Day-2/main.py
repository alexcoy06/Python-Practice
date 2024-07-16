print('Welcome to the tip calculator!')

bill = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give? 10, 12, or 15? '))
split = int(input('How many people to split the bill? '))
pay = (bill * (1 + tip / 100)) / split
pay = '{:.2f}'.format(pay)
print(f'Each person should pay: ${pay}')

# Replit allows you to code in real-time and save your code online. 
# You can also bookmark your code and share it with others. 