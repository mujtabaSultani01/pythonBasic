"""
First let's talk about class concept, when you're talking about class, it's not specific to a Python, it's applied to
most programming languages as well.
So when you talk human being, every human has a common set of properties such as name, gender, occupation etc. and
also every human will be doing some common activities such as speaking, doing work, sleep etc. so the 1st set of
properties that we covered are called properties in Object Oriented Programming world, and the activities that human
performs are called methods in Object Oriented Programming.
Thus, properties and methods form a central entity called class.so here a human is a class, which has two central
component which are properties and methods.
Human:
    Properties                           Methods
    Name                                 Speaks
    Gender                               Do work
    Occupation                           Sleeps
So class is nothing but abstraction of some entities which contains common properties & methods.
So what's Object? object is nothing, but a specific instance of a class.
Now let's write a class in python:
"""
class Human:
    def __init__(self, na, oc):
        self.name = na
        self.occupation = oc

    def do_word(self):
        if self.occupation == "Tennis player":
            print(self.name, "Play Tennis.")
        elif self.occupation == "actor":
            print(self.name, "Shots a film.")
        else:
            print(self.name, "What are you doing?")

    def speaks(self):
        print(self.name ,"says how are you?")

Ahmad = Human("Ahmad", "actor")
Ahmad.do_word()
Ahmad.speaks()

Maryam = Human("Maryam", "Tennis player")
Maryam.do_word()
Maryam.speaks()

Fawad = Human("Fawad", "doctor")
Fawad.do_word()
Fawad.speaks()
