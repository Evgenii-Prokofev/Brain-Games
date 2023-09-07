from random import randint
from brain_games.games.base import base_game


event = 'What number is missing in the progression?'


progression_length = 10


def get_progression(start, step, progression_length):
    stop = start + (progression_length * step)
    progression = list(range(start, stop, step))
    return progression


def get_expression():
    start = randint(1, 100)
    step = randint(1, 10)
    missing_index = randint(1, progression_length - 1)
    progression = get_progression(start, step, progression_length)
    answer = progression.pop(missing_index)
    progression.insert(missing_index, "..")
    question = " ".join([str(i) for i in progression])
    return question, str(answer)


def progression_game():
    base_game(get_expression, event)
