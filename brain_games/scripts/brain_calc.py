#!/usr/bin/env python3

from brain_games.games import calc
from brain_games.engine import start_game


def main():
    start_game(calc.get_answer_for_question, calc.GAME_RULES)


if __name__ == "__name__":
    main()
