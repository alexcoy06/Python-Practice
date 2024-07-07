from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def encrypt(user_direction, user_text, user_shift):
    coded_message = ''
    
    if user_direction not in ['encode', 'decode']:
        print(f'The input "{user_direction}" is not a correct choice.')
    else:
        for letter in user_text:
            shifted = user_shift
            if letter in alphabet:
                if user_direction == 'decode':
                    shifted *= -1
                index = (alphabet.index(letter) + shifted) % len(alphabet)
                coded_message += alphabet[index]
            else:
                coded_message += letter
        print(coded_message)

repeat = True
while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(direction, text, shift)
    answer = input('Type "yes" if you want to go again. Otherwise type "no".\n').lower()
    
    if answer == 'no':
        repeat = False
        print('Goodbye')