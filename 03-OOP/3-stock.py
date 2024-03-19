from dataclasses import dataclass


@dataclass
class Stock:
    apples: int
    breads: int
    marmelade_jars: int

    @property
    def total_count(self) -> int:
        "dataclass is a 'normal', you can add methods to it"
        return self.apples + self.breads + self.marmelade_jars


def example() -> None:
    # building like a "normal" class
    # we could use positional arguments but for clarity it is
    # usually prefered to use named arguments to build dataclasses.
    warehouse = Stock(apples=1052, breads=304, marmelade_jars=510)

    print(
        "The warehouse contains",
        # access attribute in a normal way
        warehouse.apples,
        "apples and",
        warehouse.breads,
        "breads",
    )
    print("There is", warehouse.total_count, "items in the warehouse")


example()


def test_merge_stocks() -> None:

    cargo_bike = Stock(apples=3, breads=20, marmelade_jars=10)
    warehouse = Stock(apples=1052, breads=304, marmelade_jars=510)

    assert cargo_bike + warehouse == Stock(apples=1055, breads=324, marmelade_jars=520)
    # Note: it is really debatable to support + on a class like "Stock", as
    # it can lead to unclear meaning. As a general rule, try be conservative
    # with operators and prefer actual names describing what you do. E.g. here
    # `merge`, or `deliver(from: Stock, to: Stock)` looks like a reasonable names.


# uncomment the test when you're ready!
# test_merge_stock()
