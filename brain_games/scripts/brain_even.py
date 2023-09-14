#!/usr/bin/env python3

from brain_games.games import even
from brain_games.engine import start_game


def main():
    start_game(even.get_answer_for_question, even.GAME_RULES)


if __name__ == "__name__":
    main()
