"""
in our today life many devices and tools created by others like computer, car or calculator. these are the devices
created or invented by other people but once they invented we can use it. this whole idea of 'reuse' applies to
programming world as well.
Modules is a way to reuse a code written by someone else. the best part about python is: you can use these modules for
free, you don't have to pay anything.
let's use a simple module 'math'
"""
import math
print("Methods available in math module: ", dir(math))
print("The square root of 25 is: ", math.sqrt(25))
print("2 power of 3 is: ", math.pow(2,3))
print("The pi default price is: ", math.pi)
print("price of log 100 base on 10 (log10(100)) is: ", math.log10(100))
print("price of log 1000 base on 10 (log10(1000)) is: ", math.log10(1000))

# We can also use calendar module: let's find the calendar of Jan-2016:
import calendar
dir(calendar)
jan = calendar.month(2016,1)
print("Calendar of Jan-2016 is: ", jan)
print(calendar.isleap(2016))

# To find all python modules: search in google python 3.10.5 moduls list. it will show you all the moduls installed
# in your PC with python installation. but we have other 3rd party moduls for using them you should install them.

