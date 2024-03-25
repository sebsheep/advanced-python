from typing import Any, Iterable, Iterator, TypeVar


def main() -> None:
    test_accumulate()
    test_chain()
    test_zip()
    test_zip_custom2()
    test_compress()


def accumulate(iterable: Iterable[int]) -> Iterator[int]:
    """
    Yield the cumulative sum of the iterable:

    accumulate([1,2,3,4,5]) → 1 3 6 10 15
    """
    # Hint: for loop/yield for the win!
    res = 0
    for n in iterable:
        res += n
        yield res


def test_accumulate() -> None:
    assert list(accumulate([])) == []
    assert list(accumulate([1])) == [1]
    assert list(accumulate(range(5))) == [0, 1, 3, 6, 10]

    print("test accumulate passed!")


T = TypeVar("T")
S = TypeVar("S")


def chain(*iterables: Iterable[T]) -> Iterator[T]:
    # Hint: for loop/yield for the win!
    for iterable in iterables:
        for x in iterable:
            yield x


def test_chain() -> None:
    assert list(chain()) == []
    assert list(chain([])) == []
    assert list(chain([1, 2, 3])) == [1, 2, 3]
    assert list(chain(range(5), [42, 57])) == [0, 1, 2, 3, 4, 42, 57]

    print("test chain passed!")


def zip_custom(iterable1: Iterable[T], iterable2: Iterable[S]) -> Iterator[tuple[T, S]]:
    """The `zip` function is built-in in Python. It's handy for iterating on
    2  iterables at once. Eg.:

        >>> for (a, b) in zip([42, 50], [1, 6, 8]): print(a, b)
        42 1
        50 6

    Note the longer list is truncated.

    The goal here is to implement it (without using it of course!)
    """
    # Hint: you'll need to use iter, next and yield
    iterator1 = iter(iterable1)
    iterator2 = iter(iterable2)

    while True:
        try:
            x = next(iterator1)
            y = next(iterator2)
            yield (x, y)
        except StopIteration:
            return


def test_zip() -> None:
    assert list(zip_custom([], [])) == []
    assert list(zip_custom([], [1, 2, 3])) == []
    assert list(zip_custom([1, 2, 3], [])) == []
    assert list(zip_custom([1, 2, 3], ["a", "b", "c"])) == [
        (1, "a"),
        (2, "b"),
        (3, "c"),
    ]
    assert list(zip_custom(range(3), ["a", "b", "c"])) == [(0, "a"), (1, "b"), (2, "c")]
    assert list(zip_custom(["apple", "banana", "cherry"], [5, 7, 9])) == [
        ("apple", 5),
        ("banana", 7),
        ("cherry", 9),
    ]

    print("test zip_custom passed!")


def compress(values: Iterable[T], selectors: Iterable[Any]) -> Iterator[T]:
    """Select items for the first iterable depending on the truthiness value
    of the second one."""
    # Hint: you can use zip_custom (or zip if you didn't succeed at the
    # previous exercise) and a generator expression with a `if`
    return (value for (value, condition) in zip_custom(values, selectors) if condition)


def test_compress() -> None:
    assert list(compress([], [])) == []
    assert list(compress([], [True, False, True])) == []
    assert list(compress([1, 2, 3], [])) == []
    assert list(compress([1, 2, 3], [True, True, True])) == [1, 2, 3]
    assert list(compress([1, 2, 3], [True, False, True])) == [1, 3]
    assert list(compress([1, 2, 3], [False, False, False])) == []
    assert list(compress([1, 2, 3], [1, 0, 1])) == [1, 3]
    assert list(compress(["a", "b", "c"], ["a", "", "c"])) == ["a", "c"]
    assert list(compress([1, 2, 3], [[], [1], [2, 3]])) == [2, 3]
    assert list(compress(["a", "b", "c"], [True, False, True])) == ["a", "c"]

    print("test compress passed!")


def zip_custom2(*iterables: Iterable[Any]) -> Iterator[tuple[Any, ...]]:
    """Actually, the zip function can handle an arbitrary number of iterables as
    arguments.

    Let's implement this!

    Note we're cheating a bit at the type level because we want to support things like:

        zip_custom2([1,3], ["hey!", "ho!"])

    The correct output type should be `Iterator[Tuple[int, str]]`, but we have no way to specify this
    on the input type when using a variable number of arguments.

    The chosen solution lose the type we could know by using `Any` but will compile
    for all existing usage of this function.

    Another solution would be to type the function like this:

        zip_custom2(*iterables: Iterable[T]) -> Iterator[Tuple[T, ...]]

    Which doesn't abuse the user with Any but would not be happy with the above
    (and really common) example... Tradeoffs, like always!
    """
    iterators = [iter(iterable) for iterable in iterables]
    if not iterators:
        return

    while True:
        try:
            yield tuple([next(iterator) for iterator in iterators])
        except StopIteration:
            return


def test_zip_custom2() -> None:
    assert list(zip_custom2()) == []
    assert list(zip_custom2([])) == []
    assert list(zip_custom2([1, 2, 3], [4, 5, 6])) == [(1, 4), (2, 5), (3, 6)]
    assert list(zip_custom2([1, 2], ["a", "b", "c"])) == [(1, "a"), (2, "b")]
    assert list(zip_custom2(range(3), ["a", "b", "c"], [True, False, True])) == [
        (0, "a", True),
        (1, "b", False),
        (2, "c", True),
    ]

    print("test zip_custom2 passed!")


if __name__ == "__main__":
    main()
