import task05


def testing(n: int = 100):
    val = task05.fizzbuzz(n)
    i = 1
    p = ""
    while i <= 45:
        p = next(val)
        i += 1
    assert p == "fizz buzz"
