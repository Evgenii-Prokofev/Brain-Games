from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num > 1:
        index = 2
        while index < num:
            if num % index == 0:
                return False
            index += 1
        return True


RANDOM_START = 1
RANDOM_END = 50


def get_answer_for_question():
    question = randint(RANDOM_START, RANDOM_END)
    answer = "yes" if is_prime(question) else "no"
    return question, answer
