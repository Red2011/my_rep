import save_original_info, functools


@save_original_info.print_result
def tested_func(*args):
    """Testing text"""
    return functools.reduce(lambda x, y: x**y, args)


def testing():
    assert tested_func.__doc__ == "Testing text"
    assert tested_func.__name__ == "tested_func"
    assert tested_func(2, 3) == 8
