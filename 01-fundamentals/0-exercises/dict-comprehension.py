def id_dicts(elements):
    "Look at tests to know what to do :)"
    # Constraint: use a dict comprehension
    pass


def test_id_dicts():
    assert id_dicts([]) == {}
    assert id_dicts(["Seb"]) == {"Seb": "Seb"}
    assert id_dicts(["HE", "LP", "LO"]) == {"HE": "HE", "LP": "LP", "LO": "LO"}

    print("test_id_dicts passed")


test_id_dicts()


def next_year(users):
    """Return an updated version of the dictionary passed as argument for
    the next year
    """
    # Constraint: use a dict comprehension
    pass


def test_next_year():
    assert next_year({}) == {}
    assert next_year({"Alice": 25, "Bob": 30}) == {"Alice": 26, "Bob": 31}
    assert next_year({"John": 18}) == {"John": 19}

    print("test_next_year passed")


# Uncomment the following to pass the tests
# test_next_year()
