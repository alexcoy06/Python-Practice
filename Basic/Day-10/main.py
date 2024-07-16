logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    '+': add, 
    '-': subtract, 
    '*': multiply, 
    '/': divide
}

def calculator():
    print(logo)
    
    num1 = float(input('What is the first number?: '))
    for operation in operations:
        print(operation)

    doing_math = True
    repeat = ''
    while doing_math:

        operation_picked = input('Pick an operation: ')
        num_x = float(input('What is the next number?: '))

        calc = operations[operation_picked]
        answer = calc(num1, num_x)
        print(f'{num1} {operation_picked} {num_x} = {answer}')

        repeat = input(f'Type \'y\' to continue calculating with {answer}, type \'n\' to exit, or \'s\' to start over: ').lower()
        if repeat == 'y':
            num1 = answer
        elif repeat == 'n':
            doing_math = False
        elif repeat == 's':
            doing_math = False
            calculator()

calculator()