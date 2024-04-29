import sys
import random


def guessingGame(first, last):
    if last > first:
        while True:
            try:
                answer = input('What is your GUESS?: ')
                random_num = random.randint(first, last)
                answer = int(answer)
                if first <= answer <= last:
                    if answer == random_num:
                        print(
                            'CORRECT: END OF GAME!!\n---------------------\n---------------------')
                        break
                    else:
                        print(
                            f'INCORRECT: ANSWER WAS {random_num}!! \nNUMBER RANGE: {first} - {last -1}\n---------------------')
                        return guessingGame(first, (last - 1))
                elif not (first <= answer <= last):
                    print(
                        'ANSWER IS NOT IN RANGE: PLEASE TRY AGAIN \n---------------------')
                    continue
            except ValueError:
                print(
                    'ANSWER MUST BE A NUMBER: PLEASE TRY AGAIN \n---------------------')
                continue
    elif last < first:
        print('RANGE ERROR: First input is greater than the last input. Please restart.')
        num1 = int(input('Reinput first input: '))
        num2 = int(input('Reinput last input: '))
        guessingGame(num1, num2)
        print('---------------------')
    else:
        print('NO MORE TRIES: YOU LOST!!\n---------------------\n---------------------')


guessingGame(int(sys.argv[1]), int(sys.argv[2]))
