# the book.txt file is read here:
F = open("C:\\users/Habib/PycharmProjects/pythonBasic/book.txt", "r")
S = F.read()
print(S)

# now if you want to read Ahmad phone number, then you have to use python JSon modul to read this JSon string and
# pass it to a JSon object.
import json
book = json.loads(S)
print(book)

print(book["Ahmad"])
print(book["Ahmad"]["phone"])

# the difference between 1st and 2nd output is: 1st output was string but the 2nd is dictionary. for confirmation
# we can use type() method.
print(type(S))
print(type(book))
