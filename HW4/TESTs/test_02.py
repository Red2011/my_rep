import task02, pytest, os


@pytest.mark.parametrize(
    ["number"],
    [
        [1.1], [0], "r"
    ]
)
def testing(number):
    test_file = open("../Test_file.txt", "w+")
    test_file.write(str(number))
    test_file.close()
    assert task02.read_magic_number("Test_file.txt")
    os.remove("../Test_file.txt")
