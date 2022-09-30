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
x = int(x)
y = input("enter the 2nd number: ")
y = int(y)
z = x/y
# z = int(x)/int(y)
print("(x divided y) result is: ", z)


