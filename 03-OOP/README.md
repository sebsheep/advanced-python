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
You can add the verbose mode `-v` if you want to see all the tests:

```
python3 -m doctest -v 1-vect2D.py
```

Those tests are limited because they only rely on textual representation
plus, it is hard building complex tests with this framework (other tests frameworks exist for that purpose).

> Hey, some tests are failing!

Yeah, that's true. Will you understand what you have to do?

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

That's it! Now the description is accurate!

**Important Note:** as you can see, this `@property` mechnamism allows to
easily change an attribute into a "method" without changing the users of the
class. Hence, most of the time all (or most of) the attributes are public
and we don't really use getter/setter (`getDamage`/`setDamage` methods)
in Python (we didn't cover the `setter` part, feel free to take a look
on the internet, it's about the same complexity).

## Stocks

A new logistic company delivering breakfast thanks to cargo bike need a
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
