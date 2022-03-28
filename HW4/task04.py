"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions




* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
>>> fizzbuzz(5)
['1', '2', 'fizz', '4', 'buzz']
>>> fizzbuzz(20)
['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz buzz', '16', '17', 'fizz', '19', 'buzz']
"""
from typing import List
import string


def fizzbuzz(n: int) -> List[str]:
    list = []
    for x in range(1, n + 1):
        if x % 15 == 0:
            list.append("fizz buzz")
        elif x % 3 == 0:
            list.append("fizz")
        elif x % 5 == 0:
            list.append("buzz")
        else:
            list.append(str(x))
    return list
