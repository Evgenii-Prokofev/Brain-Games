import prompt

TRIES_COUNT = 3


def start_game(get_answer_for_question, GAME_RULES):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(GAME_RULES)
    for i in range(TRIES_COUNT):
        question, correct_answer = get_answer_for_question()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if correct_answer.lower() != user_answer.lower():
            print(
                f'"{user_answer}" is wrong answer ;(.'
                f'Correct answer was "{correct_answer}".'
                 )
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
