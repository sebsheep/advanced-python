from typing import Generator


# We'll ignore the last two parameters of `Generator` type for this course.
# Let's focus on the first one (`str` here).
def names() -> Generator[str, None, None]:
    yield "Seb"
    yield "Alice"
    yield "Rebecca"


def main() -> None:
    example1()
    example2()


def example1() -> None:
    print("#########")
    print("EXAMPLE 1")
    print("type of names:", type(names))
    print("type of names():", type(names()))
    print()
    print("first iteration:")
    for name in names():
        print(name)

    print("second iteration:")
    for name in names():
        print(name)

    print("---------")


def example2() -> None:
    print("#########")
    print("EXAMPLE 2")

    foo = names()
    print("type of foo:", type(foo))

    print("first iteration:")
    for name in foo:
        print(name)

    print("second iteration:")
    for name in foo:
        print(name)

    print("---------")


if __name__ == "__main__":
    main()
