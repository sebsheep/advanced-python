# Sorting

> **Note**: in this `README.md`, most of the exercises are supposed to
> be done in the REPL. We encourage you to keep track of what you've
> done in a separate file or by editing this file to insert your answers.

## Basics: `.sort` and `sorted`

In Python, you can sort lists. Test this out in a REPL:

```python
numbers = [3, 1, 2]
numbers.sort()
print(numbers)
```

**Questions** (you can play with REPL to be sure of the answer):

- Is the sort ascending or descending?
- What does the `.sort` method return?
- Is the list modified when `.sort` is called?

Now try this:

```python
names = ["Laura", "Hélène", "Zineb"]
names.sort(reverse=True)
```

**Questions**:

- What is the role of the named argument `reverse`?
- Is the list modified?

Now try this:

```python
names = ["Laura", "Hélène", "Zineb"]
names_sorted = sorted(names, reverse=True)
```

**Questions**:

- Is `names` modified?
- What does `names_sorted` contain? What is its type?
- What is the difference between `names.sort()` and `sorted(names)`?

Actually, `sorted` can take any _iterable_ as argument:

```python
sorted(range(1, 10), reverse=True)
```

(Note you can specify the `step` in a range so the following would be
simpler and more efficient: `range(9, 0, -1)` [`9` is the beginig, `0` is the
end and `-1` is the step])

## Sort depending on a key

Let's say you want to sort the following list:

```python
words = [
    "river",
    "Zineb",
    "house",
    "code",
    "administration",
]
```

**Questions**:

- What does `sorted(words)` return?
- Why is "Zineb" before "administration"?

We would like to sort this ignoring the case (i.e. "administration" should
be _before_ "Zineb").

**Instruction**: with a generator or list comprehension, transform all the
strings in `words` in lower case (test `"AbCdE".lower()` out!) and sort it
with sorted (you can do that with a one liner).

The issue here is we modified the initial list and Zineb lost its capital Z,
she's sad...

Instead we can provide a `key` argument to explain on what _criteria_
we want to perform the sort, keeping the elements untouched. E.g., we could do:

```python
def to_lower(s : str) -> str:
    return s.lower()

sorted(words, key=to_lower)
```

**Question**: what is the output? Are the elements of the initial list modified?

(ok, well now Zineb is sad because she's at the end of the list, but that's
Alaphebetical order 🤷)

> **Important note**: we don't directly _call_ the `to_lower` function! We only
> specify to `sorted` what function it should use internally to sort the
> elements!
>
> Passing functions as argument to others functions might seem weird at first,
> yet it is a really powerful technique. Functional programming takes huge
> advantage of this.

### Exercise

Here is a list of numbers:

```python
numbers = [5, -2, 9, 1, -10, 11]
```

In a REPL With _one call_ of the `sorted` function, sort the list ignoring the
sign in reverse order, i.e. we want `[11, -10, 9, 5, -2, 1]`.

_Hint_: you can use the `abs` function which compute the _absolute value_
of its argument. E.g. `abs(5) == 5`, `abs(-5) == 5`. Note you can directly
pass `abs` to `sorted`.

Solve this exercise using 2 different methods:

- using the `reverse` argument of `sorted` and `key=abs`.
- defining a `neg_abs` function which returns the opposite of the absolute value
  (that is `neg_abs(-5) == -5` and `neg_abs(5) == -5`) as the key.

> Note that with numeric criteria, we can reverse the sort by taking the
> opposite of the criteria.

### Exercise

Consider the following dict associating a name to an age:

```python
userAges = {
    "John": 20,
    "Jack": 52,
    "James": 42,
}
```

In the REPL, sort the names in ascending order relatively to the age. I.e., we
want `["John", "James", "Jack"]`. Solve this problem in 2 ways:

- use `sorted(userAges.items(), key=...)`, the key function returning
  the second element of a tuple. Then wrap this expression with a list
  comprehension to only keep the names.
- use `sorted(userAges, key=...)`. This will iterate on the keys of the dict.
  The key should be a function that performs a lookup into the `userAges` dict.

### Exercise

Consider the following dataclass and list:

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

users = [
    User(name="John", age=20),
    User(name="Jack", age=52),
    User(name="James", age=42),
]
```

In the REPL, sort this list accordingly to the `age`. That is, we want:

```python
users = [
    User(name="John", age=20),
    User(name="James", age=42),
    User(name="Jack", age=52),
]
```

Use only one call to `sorted`.

## Lambda functions

Didn't you find annoying to define tiny functions just to indicate how
to sort data? We can do this by using **anonymous functions**, also known as
**lambda functions**.

E.g, the following function definitions:

```python
def f(x, y):
    return x + y + 3

def g(x):
    return x + 3
```

can be replaced with:

```python
f = lambda x, y: x + y + 3
g = lambda x : x + 3
```

Note there is no `return` keyword in a lambda function.

With this feature in mind, we can rewrite the first example above:

```python
def to_lower(s : str) -> str:
    return s.lower()

sorted(words, key=to_lower)
```

into the one-liner:

```python
sorted(words, key=lambda s: s.lower())
```

saving us the hassle to find a signifcant name for this insignficant function.

> **Lambda functions have severe limitations in Python**: you can only return
> a single expression in a Python lambda function. This expression can be quite
> complex like:
>
> ```python
> lambda x: [x, 5, f(x, 8, 2), {x: 4}]
> ```
>
> but you cannot e.g. affect a varialbe and reuse it.

### Exercise

Redo all the previous exercises using lambda expression for the `key` instead of
defining new functions.

## Multiple criteria

Let's consider this updated users list:

```python
users = [
    User(name="Alice", age=52),
    User(name="Zineb", age=42),
    User(name="Rebecca", age=20),
    User(name="John", age=20),
    User(name="Jack", age=52),
    User(name="James", age=42),
]
```

If we only consider ages, we have _tights_. Should we sort Alice before or
after Jack? If we only `sorted(users, key=lambda u: u.age)`, Python sort
will preserve the order of the initial list, which means we'll have:

```python
[
    User(age=20, name='Rebecca'),
    User(age=20, name='John'),
    User(age=42, name='Zineb'),
    User(age=42, name='James'),
    User(age=52, name='Alice'),
    User(age=52, name='Jack')
]
```

But most of the time, we'd like to specify something like "sort accordingly to
the age first, and if the ages are the same, sort accordingly to the name".

### Comparing tuples (or list)

Let's have a short journey with the weird idea to compare tuples.

Try to predict the output and then type the following lines into a Python REPL:

```python
(1, 2) < (2, 1)
(1, 2) < (1, 3)
(2, 1) < (1, 2)
(2, 1) < (1, 0)
(1, 3) < (1, 2)
```

When comparing tuples `(a, b) < (c, d)` , Python compares elements of the tuples
in order:

- If `a < c`, we can answer that `(a, b) < (c, d)` is `True`.
- If `a > c`, we can answer that `(a, b) < (c, d)` is `False`.
- If `a == c`, we can not conclude so we have to compare `b` and `d`.

Try to predict the output and then type the following lines into a Python REPL:

```python
(20, "Rebecca") < (20, "John")
(20, "Rebecca") < (52, "Alice")
(52, "Alice") < (52, "Jack")
```

Now you can guess what the following will return:

```python
sorted(users, key=lambda u: (u.age, u.name))
```

**Vocabulary**: this order on tuples is called the _lexicographic order_. It
is similar to the way we found words in the dictionary: we first compare the
first letter, if there are the same we look at the second letter...

**Note**: comparing the lists works the same. That say, tuples are a bit
cheaper in memory so for sorting purpose we use tuples most of the time.

### Exercise

Sort the following list of cities:

- by population ascending
- then by superficy descending
- finally by name ascending

The final list should only contain the cities' names.

```python
from dataclasses import dataclass

@dataclass
class City:
    name: str
    population: int
    superficy_km2: int

cities = [
 City(name='Kinshasa', population=14966000, superficy_km2=9965),
 City(name='Cairo', population=8918653, superficy_km2=1485),
 City(name='Delhi', population=11007835, superficy_km2=1484),
 City(name='Beijing', population=21516000, superficy_km2=16410),
 City(name='Tokyo', population=13929286, superficy_km2=2191),
 City(name='Shanghai', population=11007835, superficy_km2=1484),
 City(name='Nairobi', population=3644826, superficy_km2=696),
 City(name='São Paulo', population=12252023, superficy_km2=1521),
 City(name='Santiago', population=3999759, superficy_km2=641),
 City(name='Johannesburg', population=1000000, superficy_km2=334.81),
 City(name='Chicago', population=2716000, superficy_km2=606),
 City(name='Lima', population=7413362, superficy_km2=2672),
 City(name='Bogotá', population=7413362, superficy_km2=613),
 City(name='Dhaka', population=8550405, superficy_km2=783.8),
 City(name='Rome', population=2872800, superficy_km2=1287),
 City(name='Manila', population=13923452, superficy_km2=42.88),
 City(name='Mexico City', population=8918653, superficy_km2=1485),
 City(name='Paris', population=300000, superficy_km2=75),
 City(name='London', population=9304016, superficy_km2=1572),
 City(name='Hong Kong', population=1000000, superficy_km2=1106.34),
 City(name='Bangkok', population=8280925, superficy_km2=1568),
 City(name='New York City', population=8550405, superficy_km2=783.8),
 City(name='Seoul', population=2872800, superficy_km2=605.21),
 City(name='Karachi', population=15741000, superficy_km2=591),
 City(name='Amsterdam', population=1550221, superficy_km2=219.32),
 City(name='Madrid', population=2716000, superficy_km2=604),
 City(name='Lagos', population=13923452, superficy_km2=1171),
 City(name='Sydney', population=5312163, superficy_km2=1214),
 City(name='Rio de Janeiro', population=6747815, superficy_km2=1200),
 City(name='Istanbul', population=15741000, superficy_km2=5343),
 City(name='Mumbai', population=12252023, superficy_km2=1521),
 City(name='Toronto', population=2731571, superficy_km2=630.2),
 City(name='Berlin', population=3644826, superficy_km2=891.8),
 City(name='Buenos Aires', population=3054300, superficy_km2=203),
 City(name='Moscow', population=12692466, superficy_km2=2561),
 City(name='Los Angeles', population=3999759, superficy_km2=1302),
 City(name='Osaka', population=1922264, superficy_km2=225.21),
 City(name='Kolkata', population=15741000, superficy_km2=185),
 City(name='Munich', population=1550221, superficy_km2=310.43),
]
```

You should have the following list:

```python
[
 'Paris',
 'Hong Kong',
 'Johannesburg',
 'Munich',
 'Amsterdam',
 'Osaka',
 'Chicago',
 'Madrid',
 'Toronto',
 'Rome',
 'Seoul',
 'Buenos Aires',
 'Berlin',
 'Nairobi',
 'Los Angeles',
 'Santiago',
 'Sydney',
 'Rio de Janeiro',
 'Lima',
 'Bogotá',
 'Bangkok',
 'Dhaka',
 'New York City',
 'Cairo',
 'Mexico City',
 'London',
 'Delhi',
 'Shanghai',
 'Mumbai',
 'São Paulo',
 'Moscow',
 'Lagos',
 'Manila',
 'Tokyo',
 'Kinshasa',
 'Istanbul',
 'Karachi',
 'Kolkata',
 'Beijing',
]
```

### Exercise

You are in charge of a website selling "eco-trips" (traveling in train and/or
with bike, low meat diet, and discover the beauty of natural landscape near
the home of the customer).

Those trips have a start date, end date, a minimal age for the participants
and a "promoted status".

You want to display those trips ordered by start date, then by end date, then
by minimal age.

But all the "promoted" trips have to appear at the top of the list, following
the same ordering policy.

Your CTO told you it was possible to do this simply using only one call to
`sorted`. That's your mission! Sort the `eco_trips` below accordingly to those
rules.

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class EcoTrip:
    start_date: datetime
    end_date: datetime
    min_age: int
    place: str
    promoted: bool
eco_trip = [
    EcoTrip(
        start_date=datetime.datetime(2025, 3, 5, 0, 0),
        end_date=datetime.datetime(2025, 3, 12, 0, 0),
        min_age=22,
        place="Coastal Backpacking, California",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2024, 11, 5, 0, 0),
        end_date=datetime.datetime(2024, 11, 12, 0, 0),
        min_age=24,
        place="Wildlife Safari, Alaska",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2024, 6, 10, 0, 0),
        end_date=datetime.datetime(2024, 6, 15, 0, 0),
        min_age=25,
        place="Forest Camping, Oregon",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2025, 10, 10, 0, 0),
        end_date=datetime.datetime(2025, 10, 17, 0, 0),
        min_age=20,
        place="Fall Foliage Bike Tour, Vermont",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2026, 4, 2, 0, 0),
        end_date=datetime.datetime(2026, 4, 9, 0, 0),
        min_age=22,
        place="Historic Bike Tour, Massachusetts",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2025, 4, 2, 0, 0),
        end_date=datetime.datetime(2025, 4, 9, 0, 0),
        min_age=21,
        place="Bike Tour through Vineyards, Oregon",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2025, 1, 15, 0, 0),
        end_date=datetime.datetime(2025, 1, 22, 0, 0),
        min_age=23,
        place="Mountain Biking, Utah",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2024, 9, 3, 0, 0),
        end_date=datetime.datetime(2024, 9, 10, 0, 0),
        min_age=22,
        place="River Kayaking Expedition, Montana",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2024, 4, 1, 0, 0),
        end_date=datetime.datetime(2024, 4, 7, 0, 0),
        min_age=18,
        place="Mountain Retreat, Colorado",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2026, 2, 10, 0, 0),
        end_date=datetime.datetime(2026, 2, 15, 0, 0),
        min_age=19,
        place="Winter Camping, Maine",
        promoted=False,
    ),
    EcoTrip(
        start_date=datetime.datetime(2025, 11, 5, 0, 0),
        end_date=datetime.datetime(2025, 11, 12, 0, 0),
        min_age=22,
        place="Wildlife Photography Safari, Montana",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2025, 9, 1, 0, 0),
        end_date=datetime.datetime(2025, 9, 8, 0, 0),
        min_age=23,
        place="River Rafting, Idaho",
        promoted=False,
    ),
    EcoTrip(
        start_date=datetime.datetime(2025, 5, 10, 0, 0),
        end_date=datetime.datetime(2025, 5, 17, 0, 0),
        min_age=24,
        place="Waterfall Exploration, Washington",
        promoted=False,
    ),
    EcoTrip(
        start_date=datetime.datetime(2026, 3, 5, 0, 0),
        end_date=datetime.datetime(2026, 3, 12, 0, 0),
        min_age=23,
        place="Coastal Birdwatching, Oregon",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2024, 10, 10, 0, 0),
        end_date=datetime.datetime(2024, 10, 17, 0, 0),
        min_age=20,
        place="Desert Exploration, Arizona",
        promoted=False,
    ),
    EcoTrip(
        start_date=datetime.datetime(2025, 2, 10, 0, 0),
        end_date=datetime.datetime(2025, 2, 15, 0, 0),
        min_age=20,
        place="Snowshoeing, Colorado",
        promoted=False,
    ),
    EcoTrip(
        start_date=datetime.datetime(2024, 7, 5, 0, 0),
        end_date=datetime.datetime(2024, 7, 12, 0, 0),
        min_age=20,
        place="Lake Cycling Trip, Minnesota",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2025, 8, 5, 0, 0),
        end_date=datetime.datetime(2025, 8, 12, 0, 0),
        min_age=19,
        place="Canyon Trekking, Arizona",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2026, 1, 15, 0, 0),
        end_date=datetime.datetime(2026, 1, 22, 0, 0),
        min_age=25,
        place="Snowy Mountain Trek, Colorado",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2025, 6, 15, 0, 0),
        end_date=datetime.datetime(2025, 6, 22, 0, 0),
        min_age=18,
        place="Forest Canopy Walk, Georgia",
        promoted=True,
    ),
    EcoTrip(
        start_date=datetime.datetime(2024, 8, 20, 0, 0),
        end_date=datetime.datetime(2024, 8, 25, 0, 0),
        min_age=18,
        place="Nature Hike, Vermont",
        promoted=False,
    ),
    EcoTrip(
        start_date=datetime.datetime(2025, 12, 1, 0, 0),
        end_date=datetime.datetime(2025, 12, 8, 0, 0),
        min_age=21,
        place="Island Hopping, Florida Keys",
        promoted=False,
    ),
    EcoTrip(
        start_date=datetime.datetime(2025, 7, 20, 0, 0),
        end_date=datetime.datetime(2025, 7, 27, 0, 0),
        min_age=25,
        place="Lake Paddleboarding, Michigan",
        promoted=False,
    ),
    EcoTrip(
        start_date=datetime.datetime(2024, 12, 1, 0, 0),
        end_date=datetime.datetime(2024, 12, 8, 0, 0),
        min_age=19,
        place="Island Adventure, Hawaii",
        promoted=False,
    ),
    EcoTrip(
        start_date=datetime.datetime(2024, 5, 15, 0, 0),
        end_date=datetime.datetime(2024, 5, 20, 0, 0),
        min_age=21,
        place="Coastal Bike Tour, California",
        promoted=False,
    ),
]
```

Here is the order of the places you should have:

```python
[
    "Mountain Retreat, Colorado",
    "Forest Camping, Oregon",
    "Lake Cycling Trip, Minnesota",
    "River Kayaking Expedition, Montana",
    "Wildlife Safari, Alaska",
    "Mountain Biking, Utah",
    "Coastal Backpacking, California",
    "Bike Tour through Vineyards, Oregon",
    "Forest Canopy Walk, Georgia",
    "Canyon Trekking, Arizona",
    "Fall Foliage Bike Tour, Vermont",
    "Wildlife Photography Safari, Montana",
    "Snowy Mountain Trek, Colorado",
    "Coastal Birdwatching, Oregon",
    "Historic Bike Tour, Massachusetts",
    "Coastal Bike Tour, California",
    "Nature Hike, Vermont",
    "Desert Exploration, Arizona",
    "Island Adventure, Hawaii",
    "Snowshoeing, Colorado",
    "Waterfall Exploration, Washington",
    "Lake Paddleboarding, Michigan",
    "River Rafting, Idaho",
    "Island Hopping, Florida Keys",
    "Winter Camping, Maine",
]
```
