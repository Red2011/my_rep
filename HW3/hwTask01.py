from typing import Any, List, Callable


def cache(times) -> Callable:
    def dec_func(func: Callable) -> Callable:
        number_of_calls = times
        result = None

        def cache_func(*args: List[Any]) -> Any:
            # "nonlocal" allows you to call variables from a global function
            nonlocal number_of_calls
            nonlocal result
            # count the number of calls to the function "func"
            if number_of_calls == times:
                result = func(*args)
                number_of_calls = 0
            else:
                number_of_calls += 1
            return result

        return cache_func

    return dec_func


@cache(times=2)
def f():
    return input('? ')


print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
