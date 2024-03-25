from typing import Any, Iterable


def print_twice(elements: Iterable[Any]) -> None:
    print("first display:")
    for element in elements:
        print(element)

    print("second pass:")
    for element in elements:
        print(element)


my_numbers = [5, 8, 6, 42]

plus_one1 = [n + 1 for n in my_numbers]

plus_one2 = (n + 1 for n in my_numbers)

print("plus_one1 type:", type(plus_one1))
print("plus_one2 type:", type(plus_one2))

print("Call print_twice with plus_one1")
print_twice(plus_one1)

print("###############################")
print("Call print_twice with plus_one2")
print_twice(plus_one2)
