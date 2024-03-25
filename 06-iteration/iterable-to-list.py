from typing import Iterable, TypeVar


T = TypeVar("T")


def iterable_to_list(iterable: Iterable[T]) -> list[T]:
    """Transform any iterable in a list.

    >>> iterable_to_list([1, 2, 3])
    [1, 2, 3]

    >>> iterable_to_list((1, 2, 3))
    [1, 2, 3]

    >>> iterable_to_list({1: "a", 2: "b", 3: "c"})
    [1, 2, 3]
    """
    # TODO: Implement this function WITHOUT using list!
    # You can only use:
    # - the empty list: [],
    # - while loop,
    # - .append method,
    # - exception handling.
    #
    # Note that it only is supposed to be an exercise and NOT what you
    # should do in actual Python code base!
    pass
