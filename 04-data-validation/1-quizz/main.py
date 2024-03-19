import json
import sys
from typing import Any


def main() -> None:
    questions = load_questions()
    game(questions)


def load_questions() -> list[dict[Any, Any]]:
    """This function is correct, just look at it to understand how it works"""
    try:
        file = open("questions.json")
    except:
        print("Oops, the questions.json file seems missing")
        sys.exit(-1)

    try:
        questions: list[dict[Any, Any]] = json.load(file)
    except:
        print("Oops, the questions.json file doesn't seem to be in json format")
        sys.exit(-1)

    file.close()

    return questions


def game(questions: list[dict[Any, Any]]) -> None:
    score = 0
    i = 0
    question = questions[i]
    while questions:
        score += play_question(question)
        i += 1

    print(f"Your score is {score}/{len(questions)}!")


def play_question(question: dict[Any, Any]) -> int:
    answers = question["answers"]

    print()
    print(question["question"])
    print()

    for i, answer in enumerate(answers):
        print(f"{i + 1}. {answer}")

    user_answer_int = ask_answer(len(answers))

    if user_answer_int == question["correct"]:
        return 1
    else:
        return 0


def ask_answer(max_answer: int) -> int:
    user_answer_ok = False
    while not user_answer_ok:
        user_answer_string = input(f"Choose your answer (1 to {max_answer}): ")
        try:
            user_answer_int = int(user_answer_string)
        except:
            # user_anwser_ok will stay False, so the while
            # loop condition holds.
            print(f"Illegal input!")
            continue

        if 1 <= user_answer_int <= max_answer:
            user_answer_ok = True
        else:
            print(f"Illegal input!")
    return user_answer_int


if __name__ == "__main__":
    main()
