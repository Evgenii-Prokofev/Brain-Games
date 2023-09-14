from random import choice, randint
from brain_games.engine import start_game

GAME_RULES = 'What is the result of the expression?'


def get_calculation(num1, num2, sign):
    match sign:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2


RANDOM_START = 1
RANDOM_END = 50
PLUS = '+'
MINUS = '-'
MULTIPLY = '*'


def get_answer_for_question():
    num1 = randint(RANDOM_START, RANDOM_END)
    num2 = randint(RANDOM_START, RANDOM_END)
    sign = choice((PLUS, MINUS, MULTIPLY))
    answer = get_calculation(num1, num2, sign)
    question = f"{num1} {sign} {num2}"
    return question, str(answer)
