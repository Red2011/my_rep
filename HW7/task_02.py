"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
>>> s = "ab#c"
>>> t = "ad#c"
>>> print(backspace_method(t) == backspace_method(s))
True
>>> s = "a#c"
>>> t = "b"
>>> print(backspace_method(t) == backspace_method(s))
False

   Input: s = "ab#c", t = "ad#c"
   Output: True
   Both s and t become ac

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def backspace_method(line: str):
    new_line = list(line)
    for i in range(0, len(line)):
        if line[i] == '#':
            new_line[i - 1] = ''
            new_line[i] = ''
    line = ''.join(new_line)
    return line


def backspace_compare(first: str, second: str):
    first_line = backspace_method(first)
    second_line = backspace_method(second)
    if first_line == second_line:
        return f"Input: s = {first}, t = {second}\nOutput: True\nExplanation: Both s and t become {first_line}"
    else:
        return f"Input: s = {first}, t = {second}\nOutput: False\nExplanation: s becomes {first_line} while t becomes {second_line}"


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
