"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> test_dir = Path("D:/", "Pycharm", "Python_2031", "my_rep", "HW7")
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import glob
import os
from pathlib import Path
from typing import Optional, Callable


def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    counter = 0
    wordline = ""
    # go to directory "dir_path"
    os.chdir(dir_path)
    # read all files with "file_extension" extension
    for file in glob.glob(f"*.{file_extension}"):
        with open(file) as f:
            # create a list with data without line break "/n"
            line = f.read().splitlines()
            # count the number of lines
            counter += len(line)
            # create a string with a separator between the lines in the file
            underline = " ".join(line)
            wordline += underline + " "
        f.close()
    if tokenizer is None:
        return counter
    else:
        return len(tokenizer(wordline))


# P.S. in this assignment I am using 1.txt and 2.txt files which are in HW7 folder on github

if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
