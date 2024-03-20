def f(a, b, c):
    d = g(a, b)
    return d + c



def g(x, y):
    return x - y

result = f(1, 2, 3)

print(result)
