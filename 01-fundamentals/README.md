# Fundamentals

Let's be precise to deeply understand Python!

## Python 2 vs 3

Today, new projects are all written in Python3.

Python2 is not maintained anymore.... BUT, still millions of LoC
running on it!

## Basic types

- bool: True or False!
- int: illimited precision integers
- float: standard 64 bit float.
- str: "Hello"
- bytes: a binary string (e.g. when reading a file)
- None: a special value, can be used as "null pointer" or "No value"

Know the type of an expression:

- type(5)
- type("hello")

Conversions :

- int("56") == 56
- int("hello") ---> Exception
- int("10EF", 16) == 4335 (hexadecimal)
- int(True) == 1
- int(False) == 0
- int(None) --> Exception

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

--> all values convert to True except "empty" ones (like 0, empty string,...)

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
if user_input:
   print("Name is empty!!")
```

So for strings, the snippet above is equivalent to:

```python
user_input = input("Enter your name")
if user_input != "":
    print("Name is empty!!")
else:
    print("Hello", user_input)
```

We can also used it for integers (maybe it's preferable to use an explicit `grade == 0` test here
for clarity):

```python
grade = 0
if grade:
    print("oh no! your grade is 0")
else:
    print("your grade is greater than 0")
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

## Execution flow

Python is dynamically interpreted, one line being interpreted after the other
one.

Does the following code work?

Look at the python files in `execution-flow/` and try to predict
the behavior when executed.

Then execute the file with the following command:

```bash
python3 execution-flow/1.py
```

## Data structures

### Lists

Lists are mutable!

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

More on lists later!

### Tuples

Tuples are really similar as lists but immutable!

```python
l = (1, "Hello", 5)
print(l[0]) # 1
print(l[1]) # "Hello"

l[3] = 58 # Exception !
```

### Dictionary

Key/Value Association. Most of the time, keys are string or integers.

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
userAges["Jessie"] # Exception

userAges.get("John") # 20
userAges.get("Jessie") # None
userAges.get("John", 78) # 20
userAges.get("Jessie", 78) # 78 (default value if not found)

# iterate on the keys (will print John, then Jack, then James)
for name in userAges:
    print(name)


# /!\ The order is preserved, but it's an implementation
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

The values don't have to be of the same type, so you can also use a dictionnary
to structure your data (even if there are better ways to do this,
as we'll see later in the course):

```python
person = {
    "name": "John",
    "age": 20,
    "city": "Paris",
}
```

You can perform the same kind of operations described above, but iterate on
a person doesn't seem to make a lot of sense.

You can even nest dictionnaries to combine both approaches (here the key of the
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

Fix all the errors to have a functionning program.

### Join with dicts
