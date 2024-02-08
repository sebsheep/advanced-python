def f(a, b, c):
    d = g(a, b)
    return d + c


def g(x, y):
    return x + y


print("first call:", f(1, 2, 3))


def g(x, y):
    return 5000


print("second call:", f(1, 2, 3))

# of course, we try to not doing that!
