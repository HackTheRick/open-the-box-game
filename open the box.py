import random


def number_guessing_game():
    """plays a number guessing game with the user."""

number = random.randint(1, 5)
attemps = 0


print('''Welcome to the number game bitch!
     /********/| 
    /________/ | 
    |___*____|/   
open the box! 
to open the box guess a number from 1 to 5''')

while True:
    try:
        guess = int(input('enter your guess: '))
    except ValueError:
        print('Invalid input you suck')
        continue
    
    if guess < number:
             print('Reee-tarded')
    elif guess > number:
        print('God you suck try again')
    else:
        print(f'wow you actually did it. your real special')

        break
if __name__ =='__main__':
    number_guessing_game()
