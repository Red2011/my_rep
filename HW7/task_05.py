"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> b = merge_sorted_files(["1.txt", "2.txt"])
>>> list(b)
[1, 2, 3, 4, 5, 6]
>>> type(b)
<class 'list_iterator'>
>>> for i in range(7): next(b)
#StopIteration is OK
"""
from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    values = []
    for filename in file_list:
        with open(filename) as f:
            for line in f:
                values.append(int(line))
        f.close()
    values_iter = values.__iter__()
    return values_iter


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
