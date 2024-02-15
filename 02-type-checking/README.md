# Type checking

## Basics

- Detect errors before execution
- Prevent bugs
- Better documentation
- Can be adopted gradually in an existing project
- Type checking is not native in Python, so it'll never be "perfect"

We can annotate functions to indicate type:

```python
def f(a: int, b: int) -> int:
    return a + b
```

- The Python interpreter will execute the annotations but will do nothing with
  those annotations
- You'll need MyPy to check those annotation. We'll just use IDE's extensions
  to see the errors, but you can integrate it in a CI/CD process to make the
  build fail if it finds errors.
- On VSCode, you can use the extension provided by Microsoft.
- Unfortunately, mypy support on PyCharm doesn't seem great at the time of
  writing (Feb. 2024). This issue asks for integrating mypy to PyCharm natively
  (PyCharm has it own type checker which is not as good as mypy's one).
- By default, MyPy won't check functions that doesn't have type annotation,
  which eases the adoption on existing projects.

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

(note: we'll be more precise a bit later about the `list`s)

**Exercise:**

1. in the `1-quizz/main.py`, you have the same file as in
   `01-fundamentals`. Add appropriate typing annotations on all functions in order
   to make your IDE detect some errors (adding annotations will force MyPy to
   check the functions).
2. Fix the errors (it might no find all the errors)

On new projects, I recommend to activate the `--strict` or at least
`--check-untyped-defs` option (in VSCode, you can add the following config in
the settings.json:
`"mypy-type-checker.args": ["--check-untyped-defs"]`).

## More precise type checking

```python
# We can indicate that the argument is list of dict
def print_users(users: list[dict]) -> None
```

> **Note:** prior to Python 3.9, `list` cannot be subscripted, so we
> have to import `List` (note the uppercase):
>
> ```python
> from typing import List
>
> def print_users(users: List[dict]) -> None
> ```

**Exercise:** improve your typing to indicate the type of elements of the lists
in `1-quizz/main.py`.

We can type the dicts as well, when used as "indexed databases" with
`dict[<key type>, <value type>]`.

For example (by the way, you notice we can annotate a variable):

```python
intToStrDict: dict[str, int] = { "Hello": 45, "Ha!": 15 }
```

**Exercise:** add a type annotation in `01-fundamentals/2-db/join.py` on
the dict mapping the city ids to their names.

> **Note:** prior to Python 3.9, `dict` cannot be subscripted, so we
> have to import `Dict` (note the uppercase):
>
> ```python
> from typing import Dict
>
> intToStrDict: Dict[str, int] = { "Hello": 45, "Ha!": 15 }
> ```

## Type aliases

Sometime, the types are a bit (or really!) long and you don't want to repeat
them.

E.g. in the following snipper, `list[float]` is repeated.

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
> ```python3
> Vector = list[float]
> ```
>
> or explicitly specify this is a type alias for clarity:
>
> ```python3
> from typing import TypeAlias
>
> Vector: TypeAlias = list[float]
> ```
