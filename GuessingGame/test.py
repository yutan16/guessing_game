from random import randint

# Creates the answer
ans = randint(1, 50)

# Checks if the input (guess) of the user is equal to the answer (random integer)


def guess_the_number():
    attempt = 1
    while True:
        if attempt <= 10:
            guess = int(input(
                'I\'m thinking of a number between 1 and 50. Can you guess the number?\nEnter your first guess: '))
            if 1 <= guess <= 50:
                if guess == ans:
                    return print('Thats correct!')
                elif guess > ans:
                    print(
                        f'Your guess is too high. Try again!\nAttempts: {attempt} / 10')
                    attempt = attempt + 1
                else:
                    print(
                        f'Your guess is too low. Try again!\nAttempts: {attempt} / 10')
                    attempt = attempt + 1
            else:
                print('Your guess is out of range. Try again!')
                continue
        else:
            return print(f'You are out of tries! The answer was {ans}!')


guess_the_number()
