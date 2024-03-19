# Fundamentals

Let's be precise to deeply understand Python!

## Python 2 vs 3

Today, new projects are all written in Python3. Starting 2024, Python3.7 is not maintained anymore, and the last version is 3.12.

Python2 is not maintained anymore.... BUT, still millions of LoC
running on it!

## Basic types

- bool: True or False!
- int: illimited precision integers
- float: standard 64 bit float.
- str: `"Hello"` or `'Hello'`. Multilines options:
  ```python
   """Hello
   World"""
  ```
  or
  ```python
  '''Hello
  World'''
  ```
  **Note:** string interpolation with f-strings (most practical method):
  ```python
  name = "Seb"
  say_hi = f"Welcome {name}"
  ```
- bytes: a binary string (e.g. when reading a file)
- None: a special value, can be used as "null pointer" or "No value"

Know the type of an expression:

- type(5)
- type("hello")

Conversions to int:

- int("56") == 56
- int("hello") ---> Exception
- int("10EF", 16) == 4335 (hexadecimal)
- int(True) == 1
- int(False) == 0
- int(None) --> Exception

Conversions to string:

- str(45) == "45"
- str(True) == "True"
- str(None) == "None"

--> all values are converted to their Python string representation

**Conversion to bool**

- bool(5) == True
- bool(0) == False
- bool("") == False
- bool("a") == True
- bool(None) == False

--> all values converted to True except "empty" ones (like 0, empty string, empty list,...)

## Truthiness value

The "truthiness" value of a variable is the boolean obtained by applying `bool`
on it.

It is often used in conditionnals:

```python
if value:
    print("it's true!")
else:
    print("it's false!")
```

actually is interpreted by Python as

```python
if bool(value):
    print("it's true!")
else:
    print("it's false!")
```

It is used a lot to test if a **string** is empty:

```python
user_input = input("Enter your name")
# note that user_input is a string!
if not user_input:
   print("Name is empty!!")
else:
    print("Hello", user_input)
```

So for strings, the snippet above is equivalent to:

```python
user_input = input("Enter your name")
if user_input == "":
    print("Name is empty!!")
else:
    print("Hello", user_input)
```

We can also used it for integers (maybe it's preferable to use an
explicit `grade == 0` test here for clarity):

```python
grade = 0
if grade:
    print("your grade is not 0")
else:
    print("oh no! your grade is 0")
```

> **Note:** a value `x` such that `bool(x) == True` is said _truthy_.
> Otherwise it is said _falsy_.
>
> E.g. `"hello"` is truthy, `""` is falsy.

## Functions

```python
def f(a, b, c):
    return a + b + c
```

Here, all arguments are mandatory. We can call `f` in multiple ways:

```python
# positional arguments
f(1, 2, 3) # a = 1, b = 2, c = 3
# named arguments (for clarity)
f(a=1, b=2, c=3)
# with named arguments, order doesn't matter
f(b=2, c=3, a=1)
# named arguments can be mixed with named arguments
f(1, c=3, b=2) # a = 1
# all the following examples raise exception  because some argument is missing
f(1, c=3)
f(1, 2)
f(a=1, c=3)
```

> **Note:** the PEP-8 indicates some guidelines to format the code. This includes the following details about spaces around `=`:
>
> - when allocating a variable, spaces around : `a = 5`
> - when using named arguments, no spaces: `f(a=1, b=2)`

### Optional arguments

```python
def f(a, b, c=3):
    return a + b + c

f(1, 2) # c=3 provided by default
f(1, 2, 5) # c=5
# we can use named arguments as well:
f(a=1, b=4, c=8)
f(b=4, a=3) # c=3 provided by default
```

### No return statement

If a function doesn't reach a `return` statement, the returned
value is `None`

```python
def f(a, b, c):
    d = a + b + c

r = f(1, 2, 3) # r is None
```

It is the case with `print`:

```python
m = print("Hello") # m is None
```

## Interpretation flow

Python is dynamically interpreted, one line being interpreted after the other
one.

Look at the python files in `execution-flow/` and try to predict
the behavior when executed (what is displayed, what error is raised...).

Then execute the file with the following command:

```bash
python3 execution-flow/1.py
```

## Data structures

### Lists

```python
l = [1, "Hello", 5]
print(l[0]) # 1
print(l[1]) # "Hello"

l.append(42)
print(l) # [1, "Hello", 5, 42]

l[3] = 58
print(l) # [1, "Hello", 5, 58]

l.pop() # 58
print(l) # [1, "Hello", 5]

# iteration on list (display 1, then Hello, then 5)
for element in l:
    print(l)

```

Even if lists can be heterogeneous, most of the time it is used as a "collection"
of similar objects (list of users, list of articles in a cart, ...).

**Comprehension**: we can build lists using a list comprehension:

```python
numbers = [1, 5, 2]
doubles = [number*2 for number in numbers] # [2, 10, 4]
```

This avantagely replaces the equivalent code:

```python
numbers = [1, 5, 2]
doubles = []
for number in numbers:
    doubles.append(number*2)
```

Do the **exercise** in `0-exercises/list-comprehension.py`. Just run
`python3 list-comprehension.py` to launch the tests.

More on lists later!

### Tuples

Tuples are really similar as lists but immutable!

```python
t = (1, "Hello", 5)
print(t[0]) # 1
print(t[1]) # "Hello"

t[3] = 58 # Exception !
```

Tuples are intended to store multiple values of different types and meaning (compare to
lists which are more used with homogeneous types). For
example, we could represent a user with:

```python
person = ("Seb", 42, "Paris")

# You can access tuple elements by indexing
print(person[0], "is", person[1], "years old and live in", person[2])

# Note you can destructure a tuple:
(name, age, city) = person

# and use the left hand side variables:
print(name, "is", age, "years old and live in", city)
```

### Dictionary

Key/Value Association. Most of the time, keys are strings or integers.

You can use a dictionary as a kind of indexed database. E.g. here we store
the age of the user:

```python
userAges = {
    "John": 20,
    "Jack": 32,
    "James": 42,
}
# "John", "Jack" and "James" are the keys
# 20, 32, 42 are the values

# Access:
userAges["John"] # 20
userAges["Jessie"] # Exception, Jessie doesn't exist in this dict

userAges.get("John") # 20
userAges.get("Jessie") # None
userAges.get("John", 78) # 20
userAges.get("Jessie", 78) # 78 (default value if not found)

# iterate on the keys (will print John, then Jack, then James)
for name in userAges:
    print(name)


# /!\ The insertion order is preserved, but it's an implementation
# /!\ detail and could change in next versions of Python!

# iterate on key and value at the same time
# (will print:
# John is 20 years old
# Jack is 32 years old
# James is 42 years old
# )
for (name, age) in userAges.items():
    print(name, "is", age, "years old")

# iterate on the values only (will print 20, 32, 42):
for age in userAges.values():
    print(age)

# Write
# inserting new item...
userAges["Jessie"] = 36
# or replaceing existing item as well
userAges["John"] = 15
```

**Note**: we can use a dict an indexed database because the "get" operation (`userAges["John"]` executes in constant time, regardless of the size of the dict).

The values don't have to be of the same type (neither the keys!), so you can also use a
dictionnary to structure your data (even if there are better ways to do this,
as we'll see later in the course):

```python
person = {
    "name": "John",
    "age": 20,
    "city": "Paris",
}
```

You can perform the same kind of operations described above, but iterating on
a person doesn't seem to make a lot of sense.

You can even nest dictionnaries and combine both approaches (here the key of the
top level dictionnary could be UID from the DB):

```python
users = {
    "4e3abc": {
        "name": "John",
        "age": 20,
        "city": "Paris",
    },
    "5d68e7": {
        "name": "James",
        "age": 32,
        "city": "London",
    },
}
```

Actually, keys can be a really large range of types: int, string, tuples, ... But no mutable ones like lists. To be more precise, the keys has to be "hashable",
more on that later.

There also is a dict comprehension syntax:

```python
numbers = [1, 5, 2]
doubles = {number: number*2 for number in numbers} # {1: 2, 5: 10, 2: 4}
```

which replaces the following code:

```python
numbers = [1, 5, 2]
doubles = {}
for number in numbers:
    doubles[number] = number * 2
```

Do the `0-exercises/dict-comprehension.py` exercise.

> **Note:** you maybe noticed that the last element in a multiline list or
> dict has a trailing comma like in (after `"Paris"`):
>
> ```python
> person = {
>     "name": "John",
>     "age": 20,
>     "city": "Paris",
> }
> ```
>
> This comma is totally optional but is allowed by Python in order to
> easily add new items in the list.

## Exercises

### Quizz

Look at the `1-quizz` folder. It is a simple quizz game. It contains:

- `questions.json` you have to read it but you cannot modify it. This file is "correct", no bugs in it!
- `main.py` which runs the program.

The program contains a lot of mistakes you'll have to fix!

To run the program, open a terminal in the `1-quizz` folder, then:

```bash
python3 main.py
```

it will print an error, it's normal, you have to fix it!

Here is an expected execution of the program (note that the score is correctly computed):

```

What is the velocity of a swallow carrying a coconut?

1. A swallow cannot hold a coconut
2. 50 mph
3. Is it an Asian or African swallow?
4. I don't know that!
Choose your answer (1 to 4): 3

How many times do you need to fold a paper sheet such that it reaches the top of Eiffel's tower?

1. 10
2. 23
3. 103
4. 1303
Choose your answer (1 to 4): 2

What did inspire Guido van Rossum (Python's original author) to name of the Python programming language?

1. Guido is a big fan of The Monty Python, an English comedy group
2. Guido is a big fan of snakes
3. Because we can write recursive functions in Python, like a snake biting its tail
4. Guido randomly chose a name in the dictionary
Choose your answer (1 to 4): 4
Your score is 2/3!
```

Fix all the errors to have a functionning program!

### Join with dicts

We'll illustrate here how convinient it is to use dicts as an "index" to quickly
find data.

Look at the `join.py` file and fulfill the `join_people` definition.

## What did we learn?

- Python basic types and conversions
- Truthiness value (truthy/falsy)
- Function (optional) arguments. Call functions by naming arguments
- Function without return statement
- Interpretation flow
- Lists, list comprehension, read/write, `.append`, `.pop`, iteration
- Tuples, tuple destructuration
- Dictionaries, dict comprehension, use as DB or to structure data,
  iteration on the keys/the values/both, nest dicts.
