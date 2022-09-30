"""
Exception are errors detected at the time of program execution.
Clear road, when you're reaching your destination is: executing program without any exception, but when there is an
accident on the road which you were not expecting is exception & your action as detour is called exception handling.
Some exception examples are: 23/0, 'abc'+34 ...it will generate exception & will terminate program execution.

Look to the following example: when you are dividing two numbers it work fine, but when you're dividing on zero, it
will generate exception, and it should be noted that after generating exception the last print statement will not
be printed and program will terminate. the goal is when you're writing a program which has thousands line of codes
and exception happend in the middle, then the program will be terminated and the next code won't be executed.
"""
x = input("enter the 1st number: ")
y = input("enter the 2nd number: ")
# z = int(x)/int(y)
# print("(x divided y) result is: ", z)

# so to handle exception we use Try-catch blocks: so we put the probable section of code in try block where
# exception may occur. so after that our program will work fine, either when we divide on zero, the remaining
# code will be executed.

try:
    z = int(x)/ int(y)
except Exception as e:
    print("Exception occured: ", e)
    z = 0
print("division is: ", z)

# Or more specific:
try:
    z = int(x)/int(y)
except ZeroDivisionError as e:
    print("Division by zeor error occured!")
    z = 0
print("Division is: ", z)

# To know about the type of exception:
try:
    z = int(x)/ int(y)
except Exception as e:
    print("Exception type: ", type(e).__name__)
    print("Exception occured: ", e)
    z = 0
print("division is: ", z)

# We may have multiple exceptions, for example if we don't convert user input to integer it will also generate exce
try:
    z = x/int(y)
except TypeError as e:
    print("Exception type: ", type(e).__name__)
    z = 0
except ZeroDivisionError as e:
    print("Division by zero error occured!")
    z = 0
print("Division is: ", z)

# Google for "Python builton exceptions" to see the list of standard exceptions in Python.
