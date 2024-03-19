import math


class Vect2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def norm2(self) -> float:
        """'Classical' method computing the norm of the vector.
        >>> v = Vect2D(3, 4)
        >>> v.norm2()
        5.0
        """
        return math.sqrt(self.x**2 + self.y**2)

    def dot(self, other: "Vect2D") -> float:
        """'Classical' method with one argument computing the dot product.
        Here the argument is of the type of the class we are defining, hence
        we must use `Self` for typing. It can be called like:
           >>> v1 = Vect2D(3, 4)
           >>> v2 = Vect2D(1, 2)
           >>> v1.dot(v2)
           11
        """
        return self.x * other.x + self.y * other.y

    def __str__(self) -> str:
        """'Magic' method called:
        - directly when applying `str`:
            >>> v = Vect2D(3, 4)
            >>> str(v)
            '[| x = 3; y = 4 |]'

        - or implicitly when printed:
            >>> v = Vect2D(3, 4)
            >>> print(v)
            [| x = 3; y = 4 |]
        """
        return f"[| x = {self.x}; y = {self.y} |]"

    def __add__(self, other: "Vect2D") -> "Vect2D":
        """'Magic' method called when 2 Vect2D are added
        >>> v1 = Vect2D(3, 4)
        >>> v2 = Vect2D(1, 2)
        >>> print(v1 + v2)
        [| x = 4; y = 6 |]
        """
        return Vect2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vect2D") -> "Vect2D":
        """Vector substraction
        >>> v1 = Vect2D(3, 4)
        >>> v2 = Vect2D(1, 3)
        >>> print(v1 - v2)
        [| x = 2; y = 1 |]
        """
        # TODO!
        pass

    def __mul__(self, scale: float | int) -> "Vect2D":
        """Vector multiplication by a number, the number being on the right,
        the vector on the left.

        Note: the scale can either be float or an int as indicated by the
        `float | int` syntax.
            >>> v1 = Vect2D(3, 4)
            >>> print(v1 * 2)
            [| x = 6; y = 8 |]
        """
        # TODO!
        pass

    def __rmul__(self, scale: float | int) -> "Vect2D":
        """Vector multiplication by a number, the number being on the left,
        the vector on the right (hence `rmul`).
            >>> v1 = Vect2D(3, 4)
            >>> print(2 * v1)
            [| x = 6; y = 8 |]
        """
        # TODO!
        # Hint: you can use the method above!
        pass

    @property
    def is_normalized(self) -> bool:
        """Property which is called like an attribute (without parenthesis).
        >>> v1 = Vect2D(3, 4)
        >>> v1.is_normalized
        False
        >>> v2 = Vect2D(1, 0)
        >>> v2.is_normalized
        True
        """
        return self.norm2() == 1
