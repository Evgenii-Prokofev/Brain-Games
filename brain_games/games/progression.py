from random import randint


GAME_RULES = 'What number is missing in the progression?'


PROGRESSION_LENGTH = 10


def get_progression(start, step, PROGRESSION_LENGTH):
    stop = start + (PROGRESSION_LENGTH * step)
    progression = list(range(start, stop, step))
    return progression


RANDOM_START = 1
RANDOM_START_END = 100
RANDOM_STEP_END = 10


def get_answer_for_question():
    start = randint(RANDOM_START, RANDOM_START_END)
    step = randint(RANDOM_START, RANDOM_STEP_END)
    missing_index = randint(RANDOM_START, PROGRESSION_LENGTH - 1)
    progression = get_progression(start, step, PROGRESSION_LENGTH)
    answer = progression.pop(missing_index)
    progression.insert(missing_index, "..")
    question = " ".join([str(i) for i in progression])
    return question, str(answer)
