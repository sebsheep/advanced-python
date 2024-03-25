import numpy as np
from numpy.typing import ArrayLike
import timeit
import typing


def main() -> None:
    basics()

    # Uncomment after reading/executing basics()
    # learn_sum()

    # Uncomment after implementing the exercise_mean_students function
    # test_mean_students()  # type: ignore


def basics() -> None:
    # As usual, try to predict what will be printed before running it
    print("## BASIC STUFF ##")
    vector = np.array([4, 5, 6])

    print("type(vector)=", type(vector))
    print("number =", vector)
    # Note that a vector is not displayed as Python list.
    # What special method is used under the hood to have this custom display?

    print("numbers+numbers =", vector + vector)
    print("numbers * 5 =", vector * 5)
    print("numbers / 5 =", vector / 5)
    # What special methods are used to be able to use the +, /, * operators?

    matrix = np.array([[1, 2, 3], [4, 5, 6]])

    print("matrix =")
    print(matrix)
    print("matrix + matrix =")
    print(matrix + matrix)
    print("matrix-vector product :", matrix @ vector)

    print("matrix.shape =", matrix.shape)

    n_rows, n_cols = matrix.shape
    print("n_rows =", n_rows, ", n_cols =", n_cols)


def learn_sum() -> None:
    print("\n\n## LEARN SUM ##")
    matrix = np.array([[1, 2, 3], [4, 5, 6]])

    print("sum all the elements of matrix:", matrix.sum())
    print("sum along the columns:", matrix.sum(axis=0))
    print("sum along the rows:", matrix.sum(axis=1))

    # Let's compare time to sum numbers in an array with 2 methods:
    big_array = np.arange(10000)

    # first using dedicated numpy's method
    np_sum_time = timeit.timeit(lambda: big_array.sum(), number=3)

    # then using a handmade function
    def naive_sum() -> int:
        s = 0
        for n in big_array:
            s += n
        return n  # type: ignore

    naive_sum_time = timeit.timeit(naive_sum, number=3)

    print("sum time with numpy's .sum method:", np_sum_time)
    print("sum time with a for loop:", naive_sum_time)

    # Numpy .sum method is actually waaaaaaay faster because a Numpy array
    # actually is a low level C structure and running .sum actually runs
    # C code under the hood which is faster than Python code.
    #
    # So, you should try as much as possible to use numpy's methods
    # instead of iterating in Python on the arrays.


@typing.no_type_check
def exercise_mean_students(grades):
    """The input consists of a matrix of grades received by students.
    The columns represent the students, the rows represent the exams.

    For example:

        [[ 75  20 ]
         [ 80  15 ]
         [ 85  10 ]]

    represents the grades of 2 students over 3 exams. The first students
    looks really with a mean of 80/100, the second one looks in trouble
    with a mean of 15/100.

    Return the mean for every student in an array like:

         [  80 15 ]
    """
    # Constraint: only use the .sum and .shape methods and arithmetic operators
    pass


@typing.no_type_check
def test_mean_students():
    assert np.all(exercise_mean_students(np.array([])) == np.array([]))
    assert np.all(
        exercise_mean_students(np.array([[75, 20], [80, 15], [85, 10]]))
        == np.array([80, 15])
    )

    print("test mean students pass")


if __name__ == "__main__":
    main()
