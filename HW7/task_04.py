"""
===========doctesting=============
>>> import os
>>> storage = My_storage(os.getcwd() + '//for_task_04//task_04.txt')
>>> print(storage['name'])
kek
>>> print(storage.name)
kek
>>> print(storage.power)
9001
>>> print(storage['power'])
9001
"""


class My_storage:
    this_dict = {}

    def __init__(self, path):
        self.path = path
        self.file_reading()

    def file_reading(self):
        with open(self.path) as f:
            for l in f:
                line = l.split('=')
                # checking for the content of a key in a dictionary
                if not hasattr(self, line[0]):
                    # adding attribute and value to dictionary with current key
                    setattr(self, line[0], (line[1].split('\n'))[0])
                    self.this_dict[line[0]] = (line[1].split('\n'))[0]
        f.close()

    def __getitem__(self, item):
        return self.this_dict[item]


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
