import prompt
from random import randint


def even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    tries_count = 3
    for i in range(tries_count):
        value = randint(1, 100)
        print('Question:', value)
        print('You answer:', end='')
        command = input()
        if value % 2 != 0 and command == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, {}!".format(name))
            return
        if value % 2 == 0 and command == 'yes' or (
                value % 2 != 0 and command == 'no'):
            print('Correct!')
        else:
            print("Not correct answer!")
            print("Let's try again, {}!".format(name))
            return
    print('Congratulations, {}!'.format(name))
