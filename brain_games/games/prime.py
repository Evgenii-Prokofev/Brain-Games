from random import randint
from brain_games.games.base import base_game


event = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num > 1:
        index = 2
        while index < num:
            if num % index == 0:
                return False
            index += 1
        return True


def get_expression():
    question = randint(1, 50)
    answer = "yes" if is_prime(question) else "no"
    return question, answer


def prime_game():
    base_game(get_expression, event)
