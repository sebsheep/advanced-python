# Type checking

## Basics

Why using typing?

- Detect wide range of errors even before execution
- Prevent bugs
- Better documentation
- Better developper experience thanks to improved autocompletion

Type checking...

- can be adopted gradually in an existing project
- is not native in Python, so it'll never be "perfect"

## Installation

On VSCode, install the Mypy Type Checker extension from Microsoft. Go to the settings
(`Ctrl+,`) and search for `mypy`. Add the following flag to the "Mypy type checker: Args":

```
--strict
```

This `--strict` option makes mypy safer by checking more stuff. It is
recommend on new
project but might cause a lot of errors to fix on legacy ones.

We can e.g. annotate functions to indicate expected types:

```python
def f(a: int, b: int) -> int:
    return a + b
```

Mypy will then check that all usages of `f` actually use 2 integers as
arguments, that the resulting value is used as an integer and that
inside the `f` function you use `a` and `b` as proper integers. E.g.
this code will not type check... Can you spot all the errors Mypy would
raise?

```python
def f(a: int, b: int) -> int:
    return a + len(b)

f("hello", 4) + "hello!"
```

Check you hypothesis by creating a new python file and copy pasting the
above snippet. Your IDE should highlight multiple pieces of code (you
have to save the file to rerun mypy)!

The Python interpreter will execute the annotations but will do nothing
with those annotations.

> **Important note:** the Python can run a code that is not correct
> regarding the types. Those are 2 separate processes. If you want to
> get maximum benefit of type checking, you'd need to ensure your code
> type checks before running it.
>
> In local development you can use your IDE to highlight errors, in
> production, you should integrate a `mypy main.py` step which would
> make the deployment fail if the code doesn't typecheck.

## Any

A value with the `Any` type is dynamically typed. Mypy doesn’t know
anything about the possible runtime types of such value. `Any`
operations are permitted on the value, and the operations are only
checked at runtime. You can use `Any` as an “escape hatch” when you
can’t use a more precise type for some reason.

`Any` is compatible with every other type, and vice versa. You can
freely assign a value of type `Any` to a variable with a more precise
type:

```python
from typing import Any

a: Any = None
s: str = ''
a = 2     # OK (assign "int" to "Any")
s = a     # OK (assign "Any" to "str")
```

You need to be careful with `Any` types, since they let you **lie** to
mypy, and this could easily hide bugs.

If you do not define a function return value or argument types, these
default to `Any`:

```python
def show_heading(s) -> None:
    print('=== ' + s + ' ===')  # No static type checking, as s has type Any

show_heading(1)  # OK (runtime error only; mypy won't generate an error)
```

With the `--strict` option, mypy forbids you to define unannotated
functions so you cannot have implicit `Any` in your code.

_(this part about `Any` is mainly inspired by the [Mypy documentation](https://mypy.readthedocs.io/en/stable/kinds_of_types.html#the-any-type)
)_

## Some examples

Here are some examples annotating functions:

```python
# A function that returns nothing
def print_users(users: list) -> None

# concat multiple time a string
def concat(s: str, n: int) -> str

# Select a user (represented as a dict) among a list
# of users
def oldest_user(users: list) -> dict
```

However, this lacks an important piece of information: what type of
elements does the `list`s and `dict`s contain? Implicitly they would
have `Any` type, but we're using `--strict` so this escape hatch is
not allowed.

For example, we can say `names: list[str]` which means `names`
will be a list of strings like:

```python
names = ["Hello", "world"]
```

For the dictionaries, we have to indicate 2 types: the type of the
key and the type of the value:

```python
d1: dict[str, int] = { "a": 2, "c": 12 }
d2: dict[str, str] = { "j": "jioj", "ml": "qvq"}
```

> **Note:** prior to Python 3.9, `list` and `dict` cannot be
> subscripted, so we have to import `List` and `Dict` (note the
> uppercase):
>
> ```python
> from typing import List, Dict, Any
>
> def print_users(users: List[Dict["str", Any]]) -> None
> ```

**Exercise 1**

1. In the `1-quizz/main.py`, you have the same file as in
   `01-fundamentals`. Add appropriate typing annotations on all
   functions in order to make your IDE detect some errors.

   For a "question", we'll use this type: `dict[str, Any]`.
   You'll probably need to force mypy to pretend the `questions`
   variable has type `list[dict[str, Any]]` by transforming the
   line

   ```pyton
   questions = json.load(file)
   ```

   into:

   ```python
   questions: list[dict[str, Any]] = json.load(file)
   ```

   Note this is far from ideal because we're casting a `Any`
   (the returned type of `json.load`) into something we _wish_
   has the given type. We'll see a better technique later.

2. Fix all the errors (typing only might no find all the errors!)

**Exercise 2**

Add a type annotation in `01-fundamentals/2-db/join.py` on
the dict mapping the city ids to their names.

## Type aliases

Sometime, the types are a bit (or really!) long and you don't want to repeat
them.

E.g. in the following snippet, `list[float]` is repeated.

```python
def scale(scalar: float, vector: list[float]) -> list[float]:
    return [scalar * num for num in vector]
```

To improve clarity and reduce duplication, we can alias it:

```python
type Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]
```

> **Note** the `type Vector = ...` syntax is new in Python 3.12. Prior to
> Python 3.12 you can just use simple affectation:
>
> ```python
> Vector = list[float]
> ```
>
> or explicitly specify this is a type alias for clarity:
>
> ```python
> from typing import TypeAlias
>
> Vector: TypeAlias = list[float]
> ```

## What did we learn?

- Using Mypy as a type checker
- Annotate functions and variables
- `Any` escape hatch
- `list` and `dict` as type annotation
- Type aliases
