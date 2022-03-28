"""
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests



>>> list(fizzbuzz(5))
['1', '2', 'fizz', '4', 'buzz']
>>> list(fizzbuzz(20))
['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz buzz', '16', '17', 'fizz', '19', 'buzz']


* https://en.wikipedia.org/wiki/Fizz_buzz
"""
from typing import List, Generator


# The generator allows you to output
# certain data without storing all the data in memory to save RAM.
# When calling the next() function, the generator uses the given conditions.
# The order in which the values are output is set by the conditions,
# and the generator outputs the values one by one, using the conditions.
def fizzbuzz(n: int) -> Generator[str, None, None]:
    for x in range(1, n + 1):
        if x % 15 == 0:
            yield "fizz buzz"
        elif x % 3 == 0:
            yield "fizz"
        elif x % 5 == 0:
            yield "buzz"
        else:
            yield str(x)
