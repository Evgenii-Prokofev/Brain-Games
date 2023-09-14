from random import randint
from brain_games.engine import start_game


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    return num1 + num2


RANDOM_START = 1
RANDOM_END = 50


def get_answer_for_question():
    num1 = randint(RANDOM_START, RANDOM_END)
    num2 = randint(RANDOM_START, RANDOM_END)
    question = f"{num1} {num2}"
    answer = get_gcd(num1, num2)
    return question, str(answer)
