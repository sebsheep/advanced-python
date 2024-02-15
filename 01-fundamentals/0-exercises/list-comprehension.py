def compute_lengths(strings):
    """Return the list of the length of the strings given in parameter."""
    # Constraint: use list comprehension
    pass


def test_compute_lengths():
    assert compute_lengths([]) == []
    assert compute_lengths(["Hello", "world"]) == [5, 5]
    assert compute_lengths(["I", "am", "Lord", "Voldemort"] == [1, 2, 4, 9])
    print("test_compute_lengths passed!")


test_compute_lengths()


def welcome_users(users):
    """Input: list of user (a dict with "name", and "age")
    Output: a list of strings containing "Welcome <name of user>"
    """
    # Constraint: use list comprehension
    pass


def test_welcome_users():
    assert welcome_users([]) == []
    assert welcome_users([{"name": "Alice", "age": 25}]) == ["Welcome Alice"]

    users = [
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 40},
        {"name": "David", "age": 35},
    ]
    assert welcome_users(users) == ["Welcome Bob", "Welcome Charlie", "Welcome David"]

    print("test_welcome_users passed")


# Uncomment the following to pass the tests
# test_welcome_users()
