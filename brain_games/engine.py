import prompt

TRIES_COUNT = 3


def start_game(get_expression, event):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(event)
    for i in range(TRIES_COUNT):
        question, correct_answer = get_expression()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if correct_answer.lower() == user_answer.lower():
            print("Correct!")
        else:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
