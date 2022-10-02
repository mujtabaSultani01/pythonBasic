"""
Here we're inheriting a class from two different classes, the benefits of multiple inheritance is, sometimes you
have two classes and you just want to inherit the properties & methods of those classes, just to reuse the code & then
you want to have your own customization. that's why you should use multiple inheritance. you can inherit your class
from many classses as you want. after comma you can type any number of classes and it will work fine.
"""
class Fathe():
    def gardening(self):
        print("I enjoy gardening...")

class Mother():
    def cooking(self):
        print("I love cooking...")

class Child(Fathe, Mother):
    def sports(self):
        print("I love playing cricket and volleyball.")

C = Child()
C.gardening()
C.cooking()
C.sports()
