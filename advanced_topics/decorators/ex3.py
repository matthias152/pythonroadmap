'''
@only_ints
def add(x, y):
    return x + y

add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
'''

from functools import wraps


def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "only ints"
        return fn(*args, **kwargs)
    return inner


@only_ints
def add(x, y):
    return x + y


print(add(1, 2))
