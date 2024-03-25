from typing import Iterator


def test_custom_range() -> None:
    assert list(custom_range(0)) == []
    assert list(custom_range(5)) == [0, 1, 2, 3, 4]
    assert list(custom_range(-5)) == []

    # iterating twice on custom_range works
    c = custom_range(5)
    assert list(c) == [0, 1, 2, 3, 4]
    assert list(c) == [0, 1, 2, 3, 4]

    print("All tests passed!")


# test_custom_range()
