#!/usr/bin/env python3

from brain_games.games import progression
from brain_games.engine import start_game


def main():
    start_game(progression.get_answer_for_question, progression.GAME_RULES)


if __name__ == "__name__":
    main()
