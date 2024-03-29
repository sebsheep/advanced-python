# Object Orienting Programing

## Vect2D

Read the `1-vect2D.py` file. This `Vect2D` class illustrates how to overload
some operators like `+` and `*`. This technique is heavily used by Numpy or
Pandas to manipulate vectors, matrices and dataframes.

You notice there some "doctest" which is
a convinient way to provide documentation while testing the code.
Those tests should be in a string just below the function/method definition.
The test consists of a REPL session, the `>>>` preceding the input.

For example, the test states that `f(1, 8)` should result in `9`:

```python
def f(a, b):
    """Add 2 numbers.

    >>> f(1, 8)
    9
    """
    return a + b
```

You can run those tests with:

```
python3 -m doctest 1-vect2D.py
```

You only see failing tests.
You can add the verbose mode `-v` if you want to see all the tests
(_note you can run the code even if it doesn't type check!_):

```
python3 -m doctest -v 1-vect2D.py
```

Those tests are limited because they only rely on textual representation
plus, it is hard building complex tests with this framework (other tests frameworks exist for that purpose).

> Hey, some tests are failing!

Yeah, that's true. Will you understand what you have to do?

> **Important note:** the body of the `__add__` method only check the type of the
> `other` argument at "compile" time. If you are writing a public library, you'd also
> add this test at "runtime" because all users won't necessarily check their code with
> mypy. This test would look like this:
>
> ```python
> def __add__(self, other: Self) -> Self:
>     if not isinstance(other, Vect2D):
>         raise ValueError(f"Cannot add a `Vect2D` with a {type(other)}")
>     return type(self)(self.x + other.x, self.y + other.y)
> ```

## Role Play

The description on the box of this game says:

> Step into a captivating world of strategy and resilience with our immersive
> `2-roleplay.py` game. Engage in epic battles against formidable foes as you
> navigate through dynamic challenges and make crucial decisions. With rich
> storytelling, intense combat, and strategic depth, every moment promises an
> unforgettable adventure in this enthralling gaming experience.

you can try it with:

```
python3 2-roleplay.py
```

You notice the game only miss one element to match this description: weapons.

**Instructions**

- Add a class `Weapon`. A weapon has a name and a damage.
- Change the `Character` class: the constructor now is:
  ```python
  def __init__(self, name: str, health: int, strength: int, weapon: Weapon)
  ```
  So you have to remove the `damage` field. Still, we want the rest of the code
  still works the same, so create a `damage` _property_ (using the `@property`
  decorator). It will be computed
  by adding the strength of the player and the damage of the weapon.
- Here is a list of weapons you can use:
  ```python
  weapons = [
      Weapon("Byte Blade", 20),
      Weapon("Code Crusher", 15),
      Weapon("Algorithmic Axe", 25),
      Weapon("Binary Blaster", 30),
      Weapon("Syntax Saber", 18)
  ]
  ```
  you can use `choice(weapons)` to randomly pick a weapon when building the
  character.

That's it! Now the description of the game is accurate! ... What, you disagree?
Be careful, I'm looking at you!

**Important Note:** as you can see, this `@property` mechnamism allows to
easily change an attribute into a "method" without changing the users of the
class. Hence, most of the time all (or most of) the attributes are public
and we don't really use getter/setter (`getDamage`/`setDamage` methods)
in Python (we didn't cover the `setter` part, feel free to take a look
on the internet, it's about the same complexity).

## Stocks

A new logistic company delivering breakfast thanks to cargo bike needs a
piece of software to handle stocks. They especially need a way to "merge"
multiple stocks, for example when a cargo bike arrives at the warehouse, we
need to add all the content of the cargo bike in the warehouse.

They noticed that class constructors tend to be the same over and over,
so they switched to `dataclass` for more concise code.

Look at `3-stock.py` and make the test pass (without changing it, of course)!

## Join - revisited

Copy paste what you've done in `01-fundamentals/2-db/join.py` into
`03-OOP/4-join-bis.py`, without the `test2` part.

Create 3 dataclasses:

- Person
- City
- PersonWithCity

and make the signature of `join` be:

```python
def join_people(people: list[Person], cities: list[City]) -> PersonWithCity
```

## Short introduction to Numpy

Numpy is a Python library aiming to provide fast calculation over arrays.
It uses operator overloading a lot to give concise solutions at difficult
problems.

Performance is reached thanks to the use of native C code on the arrays (instead
of Python which has really poor performances).

Look at `5-numpy.py` and read the comments/execute the code/solve the exercise.

## What did we learn?

- Declare a class with the `class` keyword and the special
  `__init__` method.
- Instanciate an object of a class.
- Instance methods all take `self` as the first argument (which is
  the equivalent of `this` in Java/C++).
- Declare special methods like `__add__` to overload operators for
  objects of the class.
- `doctest` provides a simple way to document and test our programs.
- Game descriptions on the boxes can be a huge lie!
- The `@property` decorator makes getter/setter pattern useless.
- We can use `@dataclass` to easily describe the fields of a class.
- Numpy arrays are Python objects backed by a performant C implementation.
- Numpy internally uses special methods like `__add__` and `__str__` a lot
  to provide a smooth experience.
