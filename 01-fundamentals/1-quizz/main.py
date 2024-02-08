import json

def main():
    questions = load_questions()
    game()


def load_questions():
    """This function is correct, just look at it to understand how it works"""
    try:
        file = open("questions.json")
    except:
        print("Oops, the questions.json file seems missing")
    
    try:
        questions = json.load(file)
    except:
        print("Oops, the questions.json file doesn't seem to be in json format")
    
    return questions

def game(questions):
    score = 0
    i = 0
    question = questions[i]
    while questions:
        score += play_question(question)
        i += 1
    
    print(f"Your score is {score}/{len(questions)}!")


def play_question(question):
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
    
def ask_answer(max_answer):
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



if __name__ == "__main__":
    main()