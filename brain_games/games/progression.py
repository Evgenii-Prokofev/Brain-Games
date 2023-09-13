from random import randint
from brain_games.engine import start_game


event = 'What number is missing in the progression?'


PROGRESSION_LENGTH = 10


def get_progression(start, step, PROGRESSION_LENGTH):
    stop = start + (PROGRESSION_LENGTH * step)
    progression = list(range(start, stop, step))
    return progression


def get_expression():
    start = randint(1, 100)
    step = randint(1, 10)
    missing_index = randint(1, PROGRESSION_LENGTH - 1)
    progression = get_progression(start, step, PROGRESSION_LENGTH)
    answer = progression.pop(missing_index)
    progression.insert(missing_index, "..")
    question = " ".join([str(i) for i in progression])
    return question, str(answer)


def progression_game():
    start_game(get_expression, event)
