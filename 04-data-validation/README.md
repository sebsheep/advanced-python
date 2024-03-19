# Data Validation

## Bullet proof quizz

Look at `1-quizz/main.py`. It should be what you got at the end of
the `02-type-checking` chapter. Note it totally typechecks.

Launch the program:

```
python3 1-quizz.main.py
```

... What does it happen at the last question? Why?

This is pretty annoying since we have almost reached the end of the
program. The source of the bug (loading ill structured data) is pretty
far away from where the bug happens (we can even easily imagine a
bigger code base where those two pieces of code are even more
spaced apart). All of this make it really hard to find and fix this
bug.

> We **need** to ensure the data has correct shape as soon as we load
> it, so we can detect potential errors as soon as possible.
>
> This kind of situation where we load external data can arise in
> multiple ways:
>
> - loading data from file,
> - receiving data from an HTTP request in an API response,
> - receiving data in the HTTP body of a POST request in a server,
> - reading data from a database...
>
> Even if you're not working in a typed environnement, you HAVE to
> ensure the data has the shape you expect (it can even lead to
> security concerns if you don't!).

There are multiple solutions for data validation in Python.
We'll use [Pydantic](https://docs.pydantic.dev/).
Install it on your machine with

```
pip3 install pydantic
```

Then, add this snippet at the begining of `1-quizz/main.py` (you can
remove `import json` as well, we won't use it anymore).

```python
from pydantic import BaseModel, ValidationError, TypeAdapter
import sys

class Question(BaseModel):
    question: str
    answers: list[str]
    correct: int
```

**Notes:**

- the `Question(BaseModel)` syntax in the definition of the class
  indicates the `Question` class _inherits_ from
  `BaseModel`. The Java equivalent syntax would be `class Question extends BaseModel`.
- the `BaseModel` subclasses behaves pretty like the same of the
  dataclasses we encountered in the `03-OOP` chapter.
  You can build them with `q = Question(question="blah blah", correct=1, answers=["a", "b"])` and
  then access the fields through `q.question`.

Now, we can replace the `load_question` function to be:

```python
def load_questions() -> list[Question]:
    """This function is correct, just look at it to understand how it works"""
    try:
        file = open("questions.json")
    except:
        print("Oops, the questions.json file seems missing")
        sys.exit(-1)

    try:
        file_content = file.read()
        # Here we check the shape of the json! We want it to be a list of questions
        questions = TypeAdapter(list[Question]).validate_json(file_content)
    except ValidationError as e:
        print("It seems like the questions.json file has some incorrect data")
        print(e.errors())
        sys.exit(-1)

    file.close()

    return questions
```

Fix all the type errors (the `list[dict[str, Any]]` annotations should
now be `list[Question]`,
and you'll need to access the question fields with `question.answers`
instead of `question["answers"]`).

Rerun the script, it should issue an error at the begining of the
program!

## Board Game

We want to build a game dashboard handling multiple games and multiple
players.

Here is a complete JSON snippet describing a dashboard:

```json
{
  "players": [
    {
      "name": "Ford",
      "score": 42,
      "favorite_color": "red",
      "from": "Betelgeuse"
    },
    {
      "name": "Arthur",
      "score": 69,
      "favorite_color": "blue",
      "from": "Earth"
    }
  ],
  "games": ["tetris", "pong"]
}
```

The score has to be an integer, the favorite color can be either
"blue" or "red", no other color is accepted.

In the `2-game-dashboard`, create a first Pydantic model `Player`.
You can run the file with `python3 2-game-dashboard/game_dashboard.py`.

You'll probably need to use the `Literal` type annotation to restrict
a value to be a special one. For example:

```python
from typing import Literal

def f(n : Literal[5] | Literal[10]) -> None:
    print(n)
```

In the previous example, `n` can only be `5` or `10`.

> **Vocabulary:** at type level, `A | B` reads as "`A` _union_ `B`".

When the first test passes, write the `Board` model!

## What did we learn?

- Blindly load data without checking its shape can lead to sneaky bugs.
- Pydantic is a solution to validate data from the outside of the
  program.
- Simple inheritance syntax.
- We can restrict values taken by a variable at the type level thanks
  to `Literal`.
- We can express that a variable can have either the type `A` or the
  type `B` with an **union**: `A | B`.
