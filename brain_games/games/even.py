from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


RANDOM_START = 1
RANDOM_END = 100


def get_answer_for_question():
    question = randint(RANDOM_START, RANDOM_END)
    answer = "yes" if is_even(question) else "no"
    return question, answer
