""" 
- Generate a random number
- Ask user a number
- Print 'Higher' if generatedNumber is higher
"""

from random import randrange



while True:
    theNumber = randrange(500)

    number = int(input('Guess the Number: '))

    while theNumber is not number:
        print('Couldn\'t make it. The number is', 'Higher' if theNumber > number else 'Lower')
        number = int(input('Guess again: '))

    print('You made it the number was', theNumber)

    for i in range(50):
        print('=', end='')
        print('//', end='')
    
    print('\n')