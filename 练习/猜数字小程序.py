# This is guess the number game
import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number betweenn 1 and 20.')

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess:',end=' ')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break  # This condition is the correct guess!
if guess == guessesTaken:
    print('Good job!you guessed my number in'+ str(guessesTaken) + 'guesses')
else:
    print('Nope .The number I was thinking of was '+str(secretNumber))