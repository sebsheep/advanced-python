def join_people(people, cities):
    """Return the list of people's name, occupation and city in a dictionary."""
    # Hint 1: look at test1 to see the exact expected output.
    # Hint 2: to be efficient, you should go into 2 passes:
    # * the first pass will iterate on cities and build a dict mapping the city id to its
    #   name. E.g. { 1: "New York", 2: "San Francisco", 3: "Paris"}
    # * the second pass will iterate on people and use the previous dict
    #   to get the city from its id.
    #
    # Question: What is the time complexity (number of operations performed) for
    #           this function?

    # Note: "pass" is Python keyword to indicate there is nothing
    # to do in the block. You have to remove it when solving this exercise.
    pass


def test1():
    PEOPLE = [
        {"id": 1, "name": "Alice", "age": 25, "occupation": "Engineer", "city_id": 3},
        {"id": 2, "name": "Bob", "age": 30, "occupation": "Doctor", "city_id": 1},
        {"id": 3, "name": "Charlie", "age": 35, "occupation": "Teacher", "city_id": 2},
        {"id": 2, "name": "Dylan", "age": 48, "occupation": "Judge", "city_id": 1},
    ]

    CITIES = [
        {"city_id": 1, "city": "New York", "country": "United States"},
        {"city_id": 2, "city": "San Francisco", "country": "United States"},
        {"city_id": 3, "city": "Paris", "country": "France"},
    ]

    assert join_people(PEOPLE, CITIES) == [
        {"name": "Alice", "occupation": "Engineer", "city": "Paris"},
        {"name": "Bob", "occupation": "Doctor", "city": "New York"},
        {"name": "Charlie", "occupation": "Teacher", "city": "San Francisco"},
        {"name": "Dylan", "occupation": "Judge", "city": "New York"},
    ]
    print("test1 passed!")


# just run
# python3 join.py
# to execute the tests
test1()


def test2():
    """This test just measures the time needed to exectue on very large
    amount of data. It shouldn't be more than 1 sec.

    This big_db file contains tow big lists (44K cities, 100K people).
    """
    import big_db
    import timeit

    # join_people(big_db.people, big_db.cities)
    elapsed = timeit.timeit(
        lambda: join_people(big_db.people, big_db.cities), number=10
    )
    print("test2, elpased: ", elapsed, "s")


# Before uncommenting test2, please run the following to generate the big_db file:
# python3 generate_tables.py
# test2()
