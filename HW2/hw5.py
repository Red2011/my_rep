"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any

def custom_range(line: str, *args: Any):
    if len(args) == 1:
        #.index searches for the specified element in a string. Returned number char.
        default_index = line.index(args[0])
        #returned end cut.
        # item[START:STOP:STEP] - takes a slice from START number to STOP (not including it), with STEP step.
        return line[:default_index]
    elif len(args) == 2:
        starting_index = line.index(args[0])
        ending_index = line.index(args[1])
        return line[starting_index:ending_index]
    elif len(args) > 2:
        starting_index = line.index(args[0])
        ending_index = line.index(args[1])
        return line[starting_index:ending_index:args[2]]
    else:
        return line

#we create our .index view. The first argument is a string,
# the second argument is the start of the slice,
# the third argument is the end of the slice, and the last argument is the step of the slice.
print(custom_range("abcedjhdiso", "o", "a", -3))


