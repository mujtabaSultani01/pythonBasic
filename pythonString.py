# String in python: Strings are used to store text.
# The way Python stores text in memory is: it store each charecter in each index. look the following example

text = "python string"
print("Each charecter of this printed string is stored in seperate index. ", text)
print("'h' in 'python string' string stored on 3rd index. ", text[3])

# you can use both (single & double) quotes to store a string...
fname = "Ahmad"
lname = 'ahmadi'
print("Hellllooo ", fname, lname)

# You can change the value of string, but not partially.
text = "new python string"
print("New string overwrite the old one.", text)
# the following statement will give you an error...
# text[0] = "a"

# You can also print part of the string using index...
print(text[0:3])
print(text[4:10])
print(text[:10])
print(text[4:])

# You can join multiple string as you want...
# full_name = fname + lname
full_name = fname + " " + lname
print("Welcome ", full_name)

# But when you want to join string with numbers then 1st you need to convert the number to  a string...
# you can use str() function
provinces = "Total provinces of Afghanistan is: "
pro_num = str(34)
print(provinces + pro_num)




