"""
Here we'll define three topics:
    1) how to raise standard exception
    2) how to raise a user-defined exception
    3) finally statement
"""
# Standard exception-raising
try:
    raise MemoryError('Memory error')
except MemoryError as e:
    print(e)

# User-defined exception:
class Accident (Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_exception(self):
        print("User-defined exception:", self.msg)
try:
    raise Accident("Crash between two cars!")
except Accident as e:
    e.print_exception()

# Finally is something which could be used for cleaning.
def file_process():
    try:
        F = open("C:\\Users\\Habib\\PycharmProjects\\pythonBasic/funny.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("Inside exception")
        #F.close()
#file_process()

# here in this code we didn't catch divideByZero exception, so the file will not close. so if you define the exception
# for this two line codes, in other case if we have a thousand line code then it's impossible to catch all exceptions.
# So we'll use finally.. , so after we'll still have exceptions but all catches will executed.
    finally:
        print("Cleaning up file")
        F.close()
file_process()

