from random import choices
from brain_games.engine import start_game


event = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    return num1 + num2


def get_expression():
    num1, num2 = choices(range(1, 50), k=2)
    question = "{} {}".format(num1, num2)
    answer = get_gcd(num1, num2)
    return question, str(answer)


def gcd_game():
    start_game(get_expression, event)
