x = lambda a : a + 10
print(x(5))

cube = lambda num: num ** 3
print(cube(3))
print(cube(8))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
