# Iteration is everything in Python

# Iterable

Look at the following piece of code:

```python
def print_names(names: list[str]):
    for name in names:
        print(name)

print_names(["Seb", "Alice", "Rebecca"])
```

Pretty simple, great! ... But actually, this `list[str]` is a bit too restrictive.

Indeed, we can use any thing which is eligible to "iteration". For exemple we could
pass a tuple instead of a list:

```python
print_names(("Seb", "Alice", "Rebecca"))
```

But doing this will make mypy unhappy because a _tuple_ is not a _list_! To solve this
issue, we can use `Iterable` instead:

```python
from typing import Iterable

def print_names(names: Iterable[str]):
    for name in names:
        print(name)

print_names(["Seb", "Alice", "Rebecca"])
print_names(("Seb", "Alice", "Rebecca"))
```

We could also pass a dict:

```python
people = {"Seb": "Hello", "Alice": "Word"}
print_names(people)
```

**Questions**:

- when iterating on a `dict`, does Python iterate on the keys or the values?
- Can we also pass `people.values()` or `people.keys()` to this `print_names` function?
- Python can also iterate on a file. Try `for x in open("README.md"): print(x)`. What does
  iterate on?

## Internals of a `for` loop

Look at `interals_of_for.py`. This is intended to explain how the following for loop
is executed by the interpretor:

```python
names = ["Seb", "Alice", "Eve"]
for name in names:
   print(name)
print("All names displayed!")
```

The `iter` and `next` functions are Python builtin functions.

- Try `next(["Seb", "Alice"])` out in the Python REPL... Does it work?
  On what kind of object can we call `next`?
- Test out:

  ```python
  names = ["Seb", "Alice"]
  iterator1 = iter(names)
  iterator2 = iter(names)
  ```

  in the REPL. What does happen when you call `next(iterator1)` multiple times?
  Is the behavior of `next(iterator2)` altered by `next(iterator1)`?

  You can see `iterator1` and `iterator2` are distinct by typing them in the REPL.
  I should display something like: `<list_iterator at 0x7fabbbcd83a0>` the last
  `0x7f...` part being the address of the object. You should notice the two objects have
  different addresses.

> **Note**: you can call the `iter` function on any Python object which is _iterable_.
> This actually is the definition of _iterable_: an object on which we can call `iter`.
>
> This `iter` function returns an _iterator_. An _iterator_ holds a **state** which is
> modified by calling `next` on it.
>
> When the iterator exhausted its content, it raises a `StopIteration` exception
> indicating we should stop iteration.

Come back to `interals_of_for.py`. Run it... It should raise an exception and not display
the final `"All names displayed!"` text. Fix this by adding a `try/except/else` around
the `name = next(iterator)` instruction (you should always wrap the instructions that may
raise exceptions as closely as possible -- here the only instruction able to raise is
`next(iterator)`).

> **Note**: `try/except/else` works as follow:
>
> ```python
> try:
>     <instructions that may raise exception>
> except <ExceptionType1>:
>     <instructions for exception type1>
> except <ExceptionType2>:
>     <instructions for exception type2>
> else: # this else block is optional
>     <instructions for when no exceptions were raised>
> ```
>
> E.g., you can have the following:
>
> ```python
> try:
>    computation = 1/0
> except ZeroDivisionError:
>    print("oups, something went wrong")
> else:
>    print("The result is", computation)
> ```

- What does it happen in the following situtation?

  ```python
  names = ["Seb", "Alice"]
  iterator1 = iter(names)
  for n in iterator1: print(n)
  for n in iterator1: print(n) # this is line is intended, it's not a copy/paste error!
  ```

  Why did the names be displayed only once?

  What does the following display?

  ```python
  iterator1
  iter(iterator1)
  ```

  You should notice there are the same object, living at the same
  address. (note: there
  is builtin way to ensure this: `A is B` return `True` if `A` and `B`
  actually point to the same memory location; here you could try
  `iter(iterator1) is iterator`).

  So with `for n in iterator1: print(n)`, the interpreter will call
  `iter` on `iterator1`
  which will return `iterator1` itself! On the second `for` loop will
  call `iter(iterator1)` once again which will return `iterator1` which
  is already exhausted!

## Iterable to list conversion

Python has a builtin function to build list from an iterable: you just have to call `list`
on it.

Test this out in the REPL:

```python
numbers = (1, 2, 3)
type(numbers)
list(numbers)
type(list(numbers))

my_name = "Seb"
list(my_name)

d = { "a": 1, "b": 2}
list(d)

l1 = [1, 2, 3]
l2 = list(l1)
l3 = l1
l1[0] = 42
l1
l2
l3
```

**Questions:**

- What does Python do when iterating over a string?
- The above snippet gives the list of the keys of `d`. How would get the _list_ of all the
  values of the dict `d` above? Note that `d.values()` doesn't return a list.
- How could we call the `l2` list compared to `l1`?

**Exercise**: do the exercise in `iterable-to-list.py` (you can
`python -m doctest -v iterable-to-list.py` to run the doctests!).
Note this is an exercise to get used to `iter/next` and shouldn't be
what we'd do in actual Python code base!

## Generators

Here is a way to build iterator objects: `Generator`s.

1. Look at `1-names.py`, focusing on the `names()` and `example1` functions.
   Try to predict what will be printed. Run the file with:

   ```
   python3 06-iteration/1-names.py
   ```

   Before uncommenting the `# example2()` line, answer those questions:

   - What is the role of `yield`?
   - Does `yield` exit the function?
   - What is the generator: `names` or `names()`?

2. In `1-names.py`, look at the `example2` function and try to predict what will be  
   printed.... Run it!

   - Is a generator stateless or stateful?

3. In `1-names.py` paste the `def print_names(names: Iterable[str])` definition above.
   Note that `print_names(names())` typechecks and behaves the same as
   `print_names(["Seb", "Alice", "Rebecca"])`!

4. Look at `2-add-one.py`.

   - Try to predict what will be printed and check it out by running
     the file.
   - The last line is:

     ```python
     print_elements(add_one(my_numbers))
     ```

     Rewrite it using only the `my_numbers` variable, a list comprehension and the `print_elements` functions.

5. Look at `3-print_twice.py`.

   - Analyse really carefully how `plus_one1` and `plus_one2` are defined. One is
     defined with brackets `[...]` (how do we call this construction?), the other one
     with parenthesis `(...)`.
   - Try to predict what will be printed and check it out by running the file.
   - What are the types of `plus_one1` and `plus_one2` (they are very different!).

   > The following definition:
   >
   > ```pyhton
   > (n + 1 for n in my_numbers)
   > ```
   >
   > is called a _generator expression_ and is a concise replacemnt for the `add_one`
   > function from `2-add-one.py`. Since it is a generator it is "statefull", hence it can
   > only be consumed once.
   >
   > **Trick:** if an expression generator is the only argument of a function, you can
   > drop the parenthesis. E.g. the following computes the sum
   > `0^2 + 1^2 + 2^2 + ... + 99^2`
   >
   > ```python
   > s = sum((i ** 2 for i in range(100)))
   > ```
   >
   > you can shorten this with:
   >
   > ```python
   > s = sum(i ** 2 for i in range(100))
   > ```
   >
   > which is pretty elegant from my point of view!

6. Look at `4-big-sum.py`. What is the difference between `s1` and `s2`?

   > **⚠️ WARNING ⚠️**
   >
   > This program will use a lot of memory, I recommend to close other non related
   > programs before running it to prevent a freeze, especially if you have less > than 32GB of RAM.
   >
   > If you know you are short in RAM, you can reduce the value of `N`.
   >
   > **⚠️ WARNING ⚠️**

   Open 2 terminals side by side, run `top` in the left one to see memory and
   CPU usage. In the right one, run `python3 4-big-sum.py`. CPU used by this
   program should be around 100%.

   Observe the memory usage when the program computes `s1` (before `s1 computed`
   is displated) and when the program computes `s2` (after `s1 computed` is
   displayed).

   What is the most memory efficient method? What do we need to allocate for
   `s1`? And for `s2`?

## Generators tradeoff

The main advantage of generator is its ability to _stream_ huge amount of data
without allocating memory (compared to an alternative where we should have
stored all data in a list).

The downside is that a generator has a "state" and can be read only once, which
can lead to sneaky bugs as soon as we try to read them twice, like we'd do with
simple list.

Hence, using generators is an **optimisation**, sacrifying code robustness for
performance. As for all optimisations, keep the following quote (from Dijkstra)
in mind:

> Premature optimisation is the root of (almost) all evil in programming.

So your strategy should be:

- use a simple list _by default_,
- _if_ you have memory issues, try out a generator. Only keep this solution
  if the memory issue is solved.

Such memory issues typically arise when reading huge files: if you load all the
file in memory, you'll probably staturate the RAM. Instead if you process those
files line per line or so, it'll be probably fine!

**Exercise**: to experiment with this idea, complete out the `read_by_chunk`
function in `process_lage_file.py`. Run the script to see the number of "e" in
this `README` (you never wanted to know that, now you know).

**Note:** from a memory point of view, generators clearly wins the game against
lists. For the computing time:

- using a generator implies a little computation overhead over a list version,
- however, we're saving the time needed for allocation

As a result, generator versions can be **slower or faster** than their list
equivalent depending of a lot of factor. Hence, optimising CPU time shouldn't be
he main goal when choosing a generator.

## (Optional) Compose iterables

We often need to "compose" iterables in some ways. The simplest "composition" is
maybe to "chain" iterables: that is, given 2 iterables, iterate on the first one
and then on the second one.

The standard library `itertools` contains a lot of such tools. E.g, the 
following code displays `42`, `4`, `0` then `1`:

```python
from itertools import chain

for i in chain([42, 4], range(2)):
  print(i)
```

To get used with composing iterables, do the exercise `custom_itertools.py`
which re-implement some of the functions in the `itertools` module (read the note
below before starting!).

> **Note**: a function can take a variable numbers of arguments with the `*args` syntax (you
> can use any other variable you want instead of `args`) . In the body of the function
> `args` is a tuple and you can iterate on it:
>
> ```python
> def f(*args):
>     for arg in args:
>         print(arg)
> ```
>
> You can then call `f` with : `f(1)` or `f(1, 2)` or even `f(42, 58, 9, 10, 32)`.
>
> If you have `data` list and you want to pass the elements as arguments, you can use the `*data` syntax:
>
> ```python
> data = [1, 4, 8]
> f(*data)
> ```
>
> For example, it works with `print`:
>
> ```python
> print(*data)
> ```
>
> Note the `*data` works lists but also for any iterable. So you could do:
>
> ```python
> print(*range(10))
> print(*chain([42, 4], range(2)))
> ```
>
> For type annotation, you should use the type of the items, e.g. if `f` can take
> a variable number of integers, you would use:
>
> ```python
> def f(*args: int): ...
> ```

## (Optional) Writing you own iterable

Let's settle the things once again:

- objects you can iterate on in a `for` loop are called _iterable_.
- We can call `iter` on _iterable_ objects to get an _iterators_. An iterator is stateful
  an cannot be iterated twice.
- A _generator_ is a way to build _iterators_.

You might want in some particular cases to write your own iterable and iterators.

- To make instances of a class _iterable_, you have to implement the special `__iter__`
  method on this class which should return an _iterator_.
- To make instacesof a class an _iterator_, you have to implement the special `__next__`
  method on this class which either return the new value of the iterator or raises
  a `StopIteration` exception. It's also customary to implement the `__iter__` method
  on this class which return the iterator itsefl (i.e. `self`); we already encounter this
  convention in the "Internals of a for loop" part above.

In `custom_range.py` you'll reimplement (a simplified version of) the builtin `range`
function. Once again, you should of course use `range` in production or in real projects.
This part is only here to get used with `__iter__` and `__next__`. That said, this kind
of thing is really advanced and it should be quite rare to actually _need_ implementing
an iterator this way.

Our custom_range will only take a single argument `stop`. Iterating on `custom_range(N)`
will be the same as iterating on `range(N)`. In all the code you write, you shouldn't
use any generator or `for` loop.

1. Create a `custom_range_iterator` dataclass with `stop` and `current_value` integer  
   parameters.
2. Add a `__iter__` method which returns `self`.
3. Add a `__next__` method which either
   - raise `StopIteration` depending on `current_value` and `stop`,
   - or increment `current_value` and return it (_return_, not _yield_).
4. Create a `custom_range` dataclass with a single`stop` integer parameter.
5. Add a `__iter__` method on `custom_range` which returns an appropriate
   `custom_range_iterator` instance. The return type of this method should be
   `Iterator[int]` (`Iterator` is already imported at the top of the file).
6. Uncomment the `# test_custom_range()` line and run the file!

## What did we learn?

- It is possible to iterate over a wide range of objects in Python.
- Most of the time, functions should accept `Iterable` instead of `list` to be more
  flexible.
- Internally, `for` loops use `iter`, `next` functions and `StopIteration` exception.
- `iter` returns an _iterator_ which has an internal state.
- `try/except/else` construct.
- Convert any iterable to a list
- Generators are a special case of iterators. They are defined with the `yield` keyword.
- _Generator expressions_ are a concise way to write generators, with a syntax similar to
  the syntax of list comprehension.
- Generators can stream a huge of data with low memory footprint.
- (Optional) We can define custom iterators by implementing the `__iter__` and
  `__next__` magic methods. This should be quite rare.
