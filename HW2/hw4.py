"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from collections.abc import Callable
from functools import lru_cache


def function(a, b):
    return (a ** b) ** 2


def cache(func: Callable) -> Callable:
    return lru_cache()(lambda *args: func(*args))


cache_func = cache(function)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

# value equality check
assert val_1 is val_2

print(val_1)
print(val_2)
# information about the size of the cache and its statistics
print(cache_func.cache_info())
