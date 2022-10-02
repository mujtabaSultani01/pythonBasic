"""
When you think about vehicle, you have so many vehicles available for use such as car, trucks, motorcycle etc.
but they provide the same purpose which is transportation, when you go to specific type of vehicle such as car and
motorcycle, they have their own purposes and own characteristics, for example a car has four wheels, it has a roof,
where motorcycle has only two wheels and it has to no roof, car has also specific usages such as commute to work or
vacation with family where motorcycle is primarily used for road trip and racing. so assume in this diagram both of
the these vehicles can be taught of sub classes of base class called vehicle, and they  share the same properties of
vehicle class, which is to provide transportation, but on top of that same share properties they have their own
specific characteristics and purposes such as wheels, roof difference and specific usages.
so here you can say that both car and motorcycle are sub classes of class vehicle, or we can say these two classes
inherit from vehicle class. so this is the initial definition of inheritance here.
the way ou inherit a class form other class is: write tht name of a class in braces.
let's have this explanation as simple example:
"""
class Vehicle:
    def general_usnge(self):
        print("General use: transportation...")

class Car (Vehicle):
    def __init__(self):
        print("I'm car.")
        self.wheels = 4
        self.has_roof = True
    def specific_usage(self):
        self.general_usnge()
        print("Specific usage: commute to work, vacation with family... ")
class Motorcycle (Vehicle):
    def __init__(self):
        print("I'm Motorcycle.")
        self.wheels = 2
        self.has_roof = False
    def specific_usage(self):
        self.general_usnge()
        print("Specific usage: road trip, racing...")

C = Car()
C.specific_usage()
# C.general_usnge()


M = Motorcycle()
M.specific_usage()
# M.general_usnge()

"""
Three main benefits of inheritance are: 1) code re-usability: in upper example you saw, you cna reuse your 
parent class code twice, trice ... & if you've a customization, you can create a sub class.
2) Readability: it provides a very nice structure in your program, especially when you're writing a big programs.
3) Extensibility: ...
"""
print("is C is instance of Car() class? ", isinstance(C, Car))
print("is M is instance of Car() class? ", isinstance(M, Car))
