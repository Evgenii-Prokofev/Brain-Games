#!/usr/bin/env python3

from brain_games.games import gcd
from brain_games.engine import start_game


def main():
    start_game(gcd.get_answer_for_question, gcd.GAME_RULES)


if __name__ == "__name__":
    main()
