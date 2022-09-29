# JSon is a stand for Java Script Object Notation. JSon is a data exchange format similar to XML.
# Let's understand this by an address record:
JSon = {
    "name": "Ali",
    "Address": "Kabul",
    "Phone": "0784334545"
}

print(JSon["Address"])
for key in JSon:
    print("Key:", key, "\n", "Value:", JSon[key])

# XML
    """
    <name> Ali </name>
    <address> Kabul </address>
    <phone> phone </phone>
    """
# Here you can see in XML each of the keys are represented in opening and closing Tags, that's why XML takes of more
# volume of data, and it's not lightweight as JSon.
# So JSon is a lightweight format compared to XML. and this is the reason JSon is getting popular now-days.
"""
 Now let's write two simple examples, 1st create address book and write some records into it. 2nd read this address
 book. 
 So 1st we'll create a dictionary object, there is no an object called JSon in python. python natives objects are
 numbers, strings, dictionaries and etc... JSon is just a concept. JSon is jsut basically a format which is implemented
 by different languages.
"""
book = {}
book["Ali"] = {
    'name': "Ali",
    'address': "Kabul",
    'phone': "0708478493"
}
book["Ahmad"] = {
    'name': "Ahmad",
    'address': "Kandahar",
    'phone': "0783746733"
}
# we can use python default JSon modul and then we will call dumps() method.
# dumps() method take dictionary object as input then it's dumping it as string, that's why we have string here.
# then it convert book dictionary object into string, and then it converted into JSon format.
import json
S = json.dumps(book)
print(S)

# now we'll save this address book in a book.txt file. when you refresh the page the address will be inserted.

with open("C:\\users/Habib/PycharmProjects/pythonBasic/book.txt", "w") as f:
    f.write(S)

# now you can read this book.txt file from C++, C or other programming language. that's why it's calle data
# exchange format.
# we'll read this data from other python file 'readJSon.py'.
