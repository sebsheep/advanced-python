from typing import Any, Iterable, Generator


def add_one(numbers: Iterable[int]) -> Generator[int, None, None]:
    for number in numbers:
        yield number + 1


def print_elements(elements: Iterable[Any]) -> None:
    for element in elements:
        print(element)


my_numbers = [5, 4, 8, 13]
print_elements(add_one(my))
