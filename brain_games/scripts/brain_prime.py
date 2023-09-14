#!/usr/bin/env python3

from brain_games.games import prime
from brain_games.engine import start_game


def main():
    start_game(prime.get_answer_for_question, prime.GAME_RULES)


if __name__ == "__name__":
    main()
