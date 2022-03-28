"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.


#>>> my_precious_logger("error: file not found")
'error: file not found'


#>>> my_precious_logger("OK")
# stdout
'OK'

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests

You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout


"""
import sys


def my_precious_logger(text: str) -> str:
    default_line = "error"
    line_now = ""
    if len(text) > 4:
        for it in range(0, 5):
            # make sure the first 5 characters are "error"
            line_now += text[it]
    if line_now == default_line:
        # writing to stderr file
        sys.stderr.write(text)
        return "OK"
    else:
        sys.stdout.write(text)


