from random import choice, choices
from brain_games.games.base import base_game

event = 'What is the result of the expression?'


def get_calculation(num1, num2, sign):
    match sign:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2


def get_expression():
    num_1, num_2 = choices(range(1, 50), k=2)
    sign = choice(["+", "-", "*"])
    answer = get_calculation(num_1, num_2, sign)
    question = "{} {} {}".format(num_1, sign, num_2)
    return question, str(answer)


def calc_game():
    base_game(get_expression, event)
